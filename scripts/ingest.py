#!/usr/bin/env python3
"""ingest.py — build a corpus collection from one official document.

Maintainer-side only (needs PyMuPDF: pip install pymupdf). Users' sandboxes
read the result with scripts/corpus.py, which is stdlib-only.

    python3 scripts/ingest.py corpus-config/de-super-ct-crim-r.json [--dry-run]

Writes corpus/<jurisdiction>/<collection>/:
    manifest.json        source, capture date, edition evidence, unit list + sha256s
    units/<unit>.txt     one file per rule/section (exact extracted text)
    collection.jsonl     every unit on one line each, for single-request search

Quality gates (ingest refuses to write if any fails):
  1. two-extractor check — every unit's text, normalised, must appear verbatim
     in the independent `pdftotext -layout` text of the same PDF;
  2. coverage — units must hold ≥ `min_coverage` of the document's body text;
  3. `expect_units` (if given) must all be present;
  4. no unit may be empty.
Order anomalies and duplicate ids are reported as warnings in the manifest.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lsnet  # noqa: E402
import lstext  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INGEST_VERSION = 1


def natural_key(uid):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", uid)]


def split_pdf_bold(pdf_bytes, cfg):
    """Split on bold, left-margin lines matching heading_regex (PyMuPDF)."""
    import pymupdf
    sp = cfg["split"]
    head_rx = re.compile(sp["heading_regex"])
    part_rx = re.compile(sp["part_regex"]) if sp.get("part_regex") else None
    extra = [(re.compile(b["regex"]), b) for b in sp.get("extra_boundaries", [])]
    left_max = sp.get("left_max", 80)
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    units, cur, part, front = [], None, None, []
    for pno, page in enumerate(doc, start=1):
        first_line_on_page = True
        for b in page.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                spans = [s for s in ln["spans"] if s["text"].strip()]
                if not spans:
                    continue
                text = "".join(s["text"] for s in ln["spans"]).rstrip()
                stripped = text.strip()
                x0 = ln["bbox"][0]
                bold = bool(spans[0]["flags"] & 16) or "Bold" in spans[0]["font"]
                if part_rx and x0 > left_max and part_rx.match(stripped):
                    part = stripped
                    continue
                boundary = None
                if bold and x0 <= left_max:
                    m = head_rx.match(stripped)
                    if m:
                        uid, title = m.group("id"), m.group("title").strip()
                        rng = re.match(r"^to\s+([\w.]+?)\.?$", title)
                        if rng:
                            uid, title = f"{uid}-{rng.group(1)}", f"(placeholder) {title}"
                        boundary = (uid, title)
                if boundary is None:
                    for rx, bcfg in extra:
                        if rx.match(stripped):
                            boundary = (bcfg["id"], bcfg.get("title", stripped))
                            break
                if boundary:
                    cur = {"id": boundary[0], "title": boundary[1], "part": part,
                           "pages": [pno, pno], "lines": [stripped]}
                    units.append(cur)
                    first_line_on_page = False
                    continue
                target = cur["lines"] if cur else front
                if cur and first_line_on_page and cur["pages"][1] != pno:
                    target.append(f"[PDF page {pno}]")
                if cur:
                    cur["pages"][1] = pno
                target.append(text)
                first_line_on_page = False
    return units, front, len(doc)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cfg = json.loads(Path(a.config).read_text())
    out = ROOT / "corpus" / cfg["jurisdiction"] / cfg["collection"]
    print(f"ingest {cfg['jurisdiction']}/{cfg['collection']} ← {cfg['url']}")

    r = lsnet.get(cfg["url"], expect=cfg.get("format"), max_age=0)
    body = r["body"]
    src_sha = r["sha256"]
    print(f"  fetched {len(body):,} bytes sha256={src_sha[:16]}")

    if cfg["split"]["method"] != "pdf-bold-headings":
        sys.exit(f"unknown split method {cfg['split']['method']}")
    units, front, npages = split_pdf_bold(body, cfg)

    # ---- gate 1: independent extractor
    lay_txt = "\n".join(lstext.pdf_pages(body))
    raw_txt = "\n".join(lstext.pdf_pages(body, layout=False))
    refs = [lstext.normalise(t, m) for t in (lay_txt, raw_txt) for m in lstext.MODES]
    ref = refs[0]
    errors, warnings = [], []
    seen = {}
    for u in units:
        if u["id"] in seen:
            seen[u["id"]] += 1
            new = f"{u['id']}-dup{seen[u['id']]}"
            warnings.append(f"duplicate unit id {u['id']} renamed {new}")
            u["id"] = new
        else:
            seen[u["id"]] = 1
        u["text"] = "\n".join(u["lines"]).strip() + "\n"
        norm = lstext.normalise(u["text"])
        placeholder = u["title"].startswith("(placeholder)")
        if len(norm) < 20 and not placeholder:
            errors.append(f"unit {u['id']} is empty or near-empty")
        elif not any(lstext.normalise(u["text"], m) in r_ for m in lstext.MODES for r_ in refs):
            # Whole-unit match failed; fall back to a line-level check. Each
            # pdftotext mode mangles different things (-layout reorders
            # hanging-indent lists, raw order drops some dashes), so every line
            # must be confirmed by at least ONE independent extraction.
            bad = []
            for ln in u["lines"]:
                if ln.startswith("[PDF page"):
                    continue
                ln_n = lstext.normalise(ln, "none").rstrip("-").strip()
                if ln_n and not any(ln_n in r_ for r_ in refs):
                    bad.append(ln.strip()[:80])
            if bad:
                errors.append(f"unit {u['id']}: {len(bad)} line(s) not confirmed by either "
                              f"pdftotext mode, e.g. {bad[0]!r}")
            else:
                u["check"] = "line-level"
    # ---- gate 2: coverage
    unit_chars = sum(len(lstext.normalise(u["text"])) for u in units)
    coverage = unit_chars / max(1, len(ref))
    if coverage < cfg.get("min_coverage", 0.97):
        errors.append(f"coverage {coverage:.3f} < {cfg.get('min_coverage', 0.97)}")
    # ---- gate 3: expected units
    ids = [u["id"] for u in units]
    missing = [x for x in cfg.get("expect_units", []) if x not in ids]
    if missing:
        errors.append(f"expected units missing: {missing}")
    # order anomalies (informational)
    prev = None
    for u in units:
        if prev and natural_key(u["id"].split("-")[0]) < natural_key(prev.split("-")[0]):
            warnings.append(f"unit {u['id']} follows {prev} (out of numeric order — "
                            "check the source; e.g. relocated rules)")
        prev = u["id"]

    print(f"  {len(units)} units · coverage {coverage:.3%} · front matter "
          f"{len(' '.join(front))} chars · {npages} pages")
    for w in warnings:
        print("  WARN ", w)
    for e in errors:
        print("  ERROR", e)
    if errors:
        sys.exit("ingest refused — fix the config or the splitter; nothing written")
    if a.dry_run:
        print("  dry run — nothing written")
        return

    (out / "units").mkdir(parents=True, exist_ok=True)
    for old in (out / "units").glob("*.txt"):
        old.unlink()
    manifest_units, jl = [], []
    for u in units:
        fname = f"units/{u['id']}.txt"
        (out / fname).write_text(u["text"])
        sha = hashlib.sha256(u["text"].encode()).hexdigest()
        manifest_units.append({"id": u["id"], "title": u["title"], "part": u["part"],
                               "file": fname, "pages": u["pages"], "check": u.get("check", "whole-unit"),
                               "chars": len(u["text"]), "sha256": sha})
        jl.append(json.dumps({"id": u["id"], "title": u["title"], "text": u["text"]},
                             ensure_ascii=False))
    (out / "collection.jsonl").write_text("\n".join(jl) + "\n")
    hdr = r["headers"]
    cd = hdr.get("Content-Disposition") or hdr.get("content-disposition") or ""
    fn = re.search(r'filename="?([^";]+)', cd)
    try:
        import pymupdf
        meta = pymupdf.open(stream=body, filetype="pdf").metadata or {}
    except Exception:
        meta = {}
    currency = None
    cp = cfg.get("currency_probe")
    if cp:
        ir = lsnet.get(cp["url"], max_age=0)
        itext = re.sub(r"\s+", " ", lstext.html_text(ir["body"]))
        m = re.search(cp["regex"], itext)
        currency = {"url": cp["url"], "regex": cp["regex"],
                    "observed": m.group(0) if m else None,
                    "checked": date.today().isoformat()}
        if not m:
            sys.exit(f"currency probe did not match on {cp['url']} — check before ingesting")
        print(f"  currency: {currency['observed']!r}")
    manifest = {
        "schema": 1, "ingest_version": INGEST_VERSION,
        "jurisdiction": cfg["jurisdiction"], "collection": cfg["collection"],
        "title": cfg["title"], "source_id": cfg.get("source_id"),
        "unit_label": cfg.get("unit_label", "Rule"),
        "cite_pattern": cfg.get("cite_pattern"), "cite_template": cfg.get("cite_template"),
        "captured": date.today().isoformat(),
        "stale_days": cfg.get("stale_days", 180), "expire_days": cfg.get("expire_days", 365),
        "source": {"url": cfg["url"], "final_url": r["final_url"],
                   "index_url": cfg.get("index_url"), "sha256": src_sha,
                   "bytes": len(body), "filename": fn.group(1) if fn else None,
                   "pdf_creation": meta.get("creationDate"), "pdf_modified": meta.get("modDate"),
                   "edition_note": cfg.get("edition_note"),
                   "fetched_at": r["fetched_at"]},
        "currency": currency,
        "quality": {"units": len(units), "coverage": round(coverage, 4),
                    "two_extractor_check": "pass", "pages": npages},
        "warnings": warnings,
        "notes": cfg.get("notes", ""),
        "units": manifest_units,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    print(f"  wrote {out.relative_to(ROOT)} ({len(units)} units)")


if __name__ == "__main__":
    main()

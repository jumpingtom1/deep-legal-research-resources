#!/usr/bin/env python3
"""Validate data/*.json, render jurisdictions/*.md, write index.json.

    python3 scripts/build.py            # validate + render + index
    python3 scripts/build.py --check    # validate only (non-zero exit on error)

The .md files are what the deep-legal-research skill reads at run time; they
are generated, never hand-edited, so they cannot drift from the records.
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "jurisdictions"

FAMILIES = ["statutes", "constitution", "court_rules", "admin_code",
            "admin_register", "case_law", "subsequent_history"]
FAMILY_TITLES = {
    "statutes": "A. Statutes / code",
    "constitution": "B. Constitution",
    "court_rules": "C. Court rules",
    "admin_code": "D. Administrative code",
    "admin_register": "D. Administrative register",
    "case_law": "E. Case law",
    "subsequent_history": "F. Subsequent history",
}
STATUSES = {"verified", "reported", "blocked", "absent"}
TIER2_HOSTS = ("public.law", "law.justia.com", "justia.com", "law.cornell.edu")
STALE_DAYS = 90


def err(errors, where, msg):
    errors.append(f"{where}: {msg}")


def validate(rec, fname):
    errors, warnings = [], []
    for k in ("schema_version", "jurisdiction", "name", "compiled",
              "citation_map", "sources"):
        if k not in rec:
            err(errors, fname, f"missing top-level '{k}'")
    if rec.get("jurisdiction") and f"{rec['jurisdiction']}.json" != fname:
        err(errors, fname, "jurisdiction code does not match file name")
    ids = set()
    for i, s in enumerate(rec.get("sources", [])):
        w = f"{fname} sources[{i}] {s.get('id', '?')}"
        for k in ("id", "family", "title", "tier", "access", "text",
                  "verification"):
            if k not in s:
                err(errors, w, f"missing '{k}'")
        if s.get("id") in ids:
            err(errors, w, "duplicate id")
        ids.add(s.get("id"))
        if s.get("family") not in FAMILIES:
            err(errors, w, f"unknown family {s.get('family')!r}")
        v = s.get("verification", {})
        if v.get("status") not in STATUSES:
            err(errors, w, f"bad verification.status {v.get('status')!r}")
        a = s.get("access", {})
        if a.get("mode") == "constructible" and not a.get("url_pattern"):
            err(errors, w, "constructible but no url_pattern")
        if a.get("mode") == "index-anchored" and not a.get("index_url"):
            err(errors, w, "index-anchored but no index_url")
        urls = " ".join(str(a.get(k) or "") for k in ("url_pattern", "index_url"))
        if s.get("tier") == 2 and urls and not any(h in urls for h in TIER2_HOSTS):
            err(errors, w, "tier 2 source on a host outside the vetted list")
        if v.get("status") == "verified":
            if not (s.get("probe") or {}).get("url"):
                err(errors, w, "verified without probe.url")
            if not v.get("evidence"):
                err(errors, w, "verified without evidence")
        ev = v.get("evidence") or ""
        quoted = re.findall(r'"([^"]+)"', ev)
        if any(len(q.split()) > 15 for q in quoted):
            warnings.append(f"{w}: evidence quote over 15 words")
    for i, p in enumerate(rec.get("citation_map", {}).get("citation_patterns", [])):
        w = f"{fname} citation_patterns[{i}]"
        try:
            rx = re.compile(p.get("regex", ""), re.I)
        except re.error as e:
            err(errors, w, f"regex does not compile: {e}")
            continue
        for ex in p.get("examples", []):
            if not rx.search(ex):
                warnings.append(f"{w}: regex misses its own example {ex!r}")
        for r in p.get("routes_to", []):
            if r not in ids:
                err(errors, w, f"routes_to unknown source id {r!r}")
    return errors, warnings


def age(d):
    try:
        return (date.today() - date.fromisoformat(d)).days
    except Exception:
        return None


def flag(s):
    v = s["verification"]
    st = v["status"]
    if st == "verified":
        a = age(v.get("date", ""))
        stale = a is None or a > STALE_DAYS or v.get("result") == "FAIL"
        tag = "VERIFIED" + (" [!]" if stale else "")
        return f"{tag} {v.get('date', '?')} ({v.get('by', '?')})"
    return st.upper() + (f" {v.get('date')}" if v.get("date") else "")


def _pattern_regexes(j, label):
    """The corpus resolves citations with the jurisdiction record's own regexes
    (every pattern whose label starts with `label`, including generic
    context_required variants), so the two can never drift apart."""
    if not label:
        return []
    rec = json.loads((DATA / f"{j}.json").read_text())
    out = [{"regex": p["regex"], "context_required": bool(p.get("context_required"))}
           for p in rec["citation_map"]["citation_patterns"] if p["label"].startswith(label)]
    if not out:
        raise SystemExit(f"corpus {j}: no citation pattern labelled {label!r} in data/{j}.json")
    return out


def load_corpora():
    """corpus/<j>/<c>/manifest.json → {source_id: [manifest summary]} and the index."""
    by_source, idx = {}, {}
    for mf in sorted((ROOT / "corpus").glob("*/*/manifest.json")):
        raw = mf.read_bytes()
        m = json.loads(raw)
        cid = f"{m['jurisdiction']}/{m['collection']}"
        entry = {"title": m["title"], "jurisdiction": m["jurisdiction"],
                 "source_id": m.get("source_id"), "captured": m["captured"],
                 "units": len(m["units"]), "stale_days": m.get("stale_days"),
                 "expire_days": m.get("expire_days"),
                 "cite_regexes": _pattern_regexes(m["jurisdiction"], m.get("cite_pattern")),
                 "cite_template": m.get("cite_template"),
                 "manifest_sha256": hashlib.sha256(raw).hexdigest()}
        idx[cid] = entry
        by_source.setdefault(m.get("source_id"), []).append((cid, entry))
    return by_source, idx


CORPORA, CORPUS_INDEX = {}, {}


def routes_for(s):
    """Ordered read routes for a source: corpus → script → fetch-tool."""
    out = []
    for cid, e in CORPORA.get(s["id"], []):
        out.append(f"**corpus** `{cid}` ({e['units']} units, captured {e['captured']})")
    if s["verification"]["status"] in ("blocked", "absent"):
        return out
    au = s.get("automation", {})
    if au.get("shell") == "ok" and s.get("text") == "fetch-and-quote":
        out.append("**script**")
    if str(au.get("webfetch", "")).startswith("ok"):
        out.append("**fetch tool**")
    return out


def render(rec):
    L = []
    j = rec["jurisdiction"].upper()
    L.append(f"# {rec['name']} ({j}) — free legal sources")
    L.append("")
    L.append(f"_Generated from `data/{rec['jurisdiction']}.json` "
             f"(compiled {rec['compiled']}, schema v{rec['schema_version']}). "
             "Do not edit by hand._")
    L.append("")
    L.append("**Rules.** Use only the sources below for this jurisdiction. "
             "Never construct a URL that is not a `constructible` pattern here; "
             "for `index-anchored` sources fetch the index and follow real links. "
             "Quote only from rows marked VERIFIED, and only under the skill's "
             "two-fetch rule. Tier 2 text must be disclosed in the report with its "
             "currency string. A BLOCKED host is never fetched by any route.")
    L.append("")
    L.append("**Read routes**, tried in the order each row lists them: "
             "**corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, "
             "integrity-checked extraction of the official document (state its capture date; "
             "run `corpus.py check` if STALE/EXPIRED); "
             "**script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live "
             "official file as exact text with no truncation (needs the host reachable from "
             "your sandbox; exit 3 = refused, never retry another way); "
             "**fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to "
             "locate and link, and quote from it only under the two-fetch rule.")
    L.append("")
    if rec.get("summary"):
        L += ["## Summary", "", rec["summary"], ""]

    cm = rec.get("citation_map", {})
    L += ["## G. Citation map", ""]
    if cm.get("courts"):
        L += ["| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |",
              "|---|---|---|---|---|"]
        for c in cm["courts"]:
            cl = c.get("courtlistener_id") or "—"
            if c.get("courtlistener_id_unverified"):
                cl += " (unverified)"
            L.append(f"| {c.get('name','')} | `{cl}` | {c.get('bluebook_abbrev') or '—'} | "
                     f"{', '.join(c.get('reporters') or []) or '—'} | "
                     f"{c.get('public_domain_citation') or '—'} |")
        L.append("")
    if cm.get("citation_patterns"):
        L += ["| Recognise | Examples | Route to (in order) |", "|---|---|---|"]
        for p in cm["citation_patterns"]:
            ex = "; ".join(f"`{e}`" for e in p.get("examples", []))
            ctx = " *(only once this jurisdiction is known)*" if p.get("context_required") else ""
            L.append(f"| {p.get('label','')}{ctx} | {ex} | "
                     f"{' → '.join(f'`{r}`' for r in p.get('routes_to', []))} |")
        L.append("")
        L.append("Regexes (case-insensitive):")
        L.append("")
        for p in cm["citation_patterns"]:
            L.append(f"- {p.get('label','')}: `{p.get('regex','')}`")
        L.append("")
    if cm.get("law_aliases"):
        L += ["Short forms → URL key:", "",
              "; ".join(f"{k} → `{v}`" for k, v in cm["law_aliases"].items()), ""]
    if cm.get("notes"):
        L += [cm["notes"], ""]

    by_fam = {}
    for s in rec.get("sources", []):
        by_fam.setdefault(s["family"], []).append(s)
    for fam in FAMILIES:
        rows = by_fam.get(fam)
        if not rows:
            continue
        L += [f"## {FAMILY_TITLES[fam]}", ""]
        rows.sort(key=lambda s: (s.get("tier", 9), s["id"]))
        for s in rows:
            a = s.get("access", {})
            au = s.get("automation", {})
            cur = s.get("currency", {})
            pr = s.get("probe", {})
            v = s["verification"]
            L.append(f"### `{s['id']}` — {s.get('title','')}")
            L.append("")
            L.append(f"- **Status:** {flag(s)} · **Tier {s.get('tier')}** · "
                     f"{s.get('publisher','')} · text: **{s.get('text','')}** · "
                     f"official: {s.get('official_status','unknown')}")
            if s.get("coverage"):
                L.append(f"- **Coverage:** {s['coverage']}")
            rts = routes_for(s)
            if rts:
                L.append("- **Read via (in order):** " + " → ".join(rts))
            L.append(f"- **Access:** `{a.get('mode','')}`"
                     + (f" · format {a['format']}" if a.get("format") else ""))
            if a.get("url_pattern"):
                L.append(f"  - Pattern: `{a['url_pattern']}`")
            if a.get("pattern_rules"):
                L.append(f"  - Placeholders: {a['pattern_rules']}")
            if a.get("index_url"):
                L.append(f"  - Index: `{a['index_url']}`")
            if a.get("navigation"):
                L.append(f"  - Navigation: {a['navigation']}")
            if a.get("read_via"):
                L.append(f"  - Read via: {a['read_via']}")
            if au:
                L.append(f"- **Automation:** WebFetch {au.get('webfetch','untested')} · "
                         f"shell {au.get('shell','untested')}"
                         + (f" · robots: {au['robots_txt']}" if au.get("robots_txt") else ""))
                if au.get("notes"):
                    L.append(f"  - {au['notes']}")
            if cur:
                L.append(f"- **Currency:** {cur.get('where','')}"
                         + (f" — observed: \"{cur['observed']}\"" if cur.get("observed") else ""))
            if s.get("official_status_evidence"):
                L.append(f"- **Official status:** {s['official_status_evidence']}")
            for h in s.get("hazards", []) or []:
                L.append(f"- **Hazard:** {h}")
            if pr:
                L.append(f"- **Probe:** {pr.get('citation','')} → `{pr.get('url','')}`"
                         + (f" — expect: \"{pr['expect']}\"" if pr.get("expect") else ""))
            if v.get("evidence"):
                L.append(f"- **Evidence ({v.get('date','')}):** {v['evidence']}")
            if s.get("notes"):
                L.append(f"- **Notes:** {s['notes']}")
            L.append("")

    if rec.get("absent"):
        L += ["## Not available (do not look for these again)", ""]
        for x in rec["absent"]:
            L.append(f"- **{x.get('family','')}** — {x.get('what','')}: "
                     f"{x.get('evidence','')} ({x.get('date','')})")
        L.append("")
    if rec.get("corpus_candidates"):
        L += ["## Corpus candidates (maintainers)", ""]
        for c in rec["corpus_candidates"]:
            L.append(f"- `{c.get('source_id','')}` — {c.get('why','')}"
                     + (f" · bulk: {c['bulk']}" if c.get("bulk") else ""))
        L.append("")
    if rec.get("open_questions"):
        L += ["## Open questions", ""]
        L += [f"- {q}" for q in rec["open_questions"]]
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def source_hosts(s):
    from urllib.parse import urlsplit
    a = s.get("access", {})
    urls = [a.get("url_pattern"), a.get("index_url"), (s.get("probe") or {}).get("url")]
    out = set()
    for u in urls:
        if not u or not u.startswith("http"):
            continue
        h = urlsplit(re.sub(r"\{[^}]*\}", "x", u)).hostname
        if h:
            out.add(h.lower())
    return out


def write_hosts():
    """hosts.json: the live-fetch allowlist used by scripts/lsnet.py."""
    hosts = {}
    for f in sorted(DATA.glob("*.json")):
        rec = json.loads(f.read_text())
        for s in rec["sources"]:
            st = s["verification"]["status"]
            for h in source_hosts(s):
                e = hosts.setdefault(h, {"ok": [], "blocked": []})
                (e["blocked"] if st in ("blocked", "absent") else e["ok"]).append(s["id"])
    # raw.githubusercontent.com is the corpus host; it is reached by corpus.py, not fetch_doc.py
    out = {"generated": date.today().isoformat(), "hosts": {}}
    for h, e in sorted(hosts.items()):
        out["hosts"][h] = {"status": "allowed" if e["ok"] else "blocked",
                           "sources": e["ok"] or e["blocked"],
                           "blocked_sources": e["blocked"] if e["ok"] else []}
    (ROOT / "hosts.json").write_text(json.dumps(out, indent=1) + "\n")


def cross_check():
    """Every jurisdiction's citation examples against every OTHER jurisdiction's
    regexes. A hit means a citation would be routed to the wrong state."""
    recs = {}
    for f in sorted(DATA.glob("*.json")):
        try:
            recs[f.stem] = json.loads(f.read_text())
        except Exception:
            pass
    hits = []
    for j, r in recs.items():
        for p in r.get("citation_map", {}).get("citation_patterns", []):
            for ex in p.get("examples", []):
                for k, r2 in recs.items():
                    if k == j:
                        continue
                    for p2 in r2.get("citation_map", {}).get("citation_patterns", []):
                        if p2.get("context_required"):
                            continue      # generic form: routes only once the state is known
                        try:
                            if re.search(p2.get("regex", ""), ex, re.I):
                                hits.append((j, ex, k, p2.get("label", "")))
                        except re.error:
                            pass
    return hits


def main():
    global CORPORA, CORPUS_INDEX
    if "--cross" in sys.argv:
        hits = cross_check()
        for j, ex, k, lab in hits:
            print(f"CROSS {j}: {ex!r} also matches {k} / {lab}")
        print(f"{len(hits)} cross-jurisdiction match(es)")
        sys.exit(1 if hits else 0)
    CORPORA, CORPUS_INDEX = load_corpora()
    check_only = "--check" in sys.argv
    OUT.mkdir(exist_ok=True)
    all_err, all_warn, index = [], [], {"generated": date.today().isoformat(),
                                        "schema_version": 1, "jurisdictions": {}}
    for f in sorted(DATA.glob("*.json")):
        try:
            rec = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            all_err.append(f"{f.name}: invalid JSON: {e}")
            continue
        e, w = validate(rec, f.name)
        all_err += e
        all_warn += w
        if check_only or e:
            continue
        md = render(rec)
        (OUT / f"{rec['jurisdiction']}.md").write_text(md)
        counts = {}
        for s in rec["sources"]:
            st = s["verification"]["status"]
            if st == "verified" and s["verification"].get("by") == "independent":
                st = "verified_independent"
            counts[st] = counts.get(st, 0) + 1
        index["jurisdictions"][rec["jurisdiction"]] = {
            "name": rec["name"],
            "file": f"jurisdictions/{rec['jurisdiction']}.md",
            "sha256": hashlib.sha256(md.encode()).hexdigest(),
            "compiled": rec["compiled"],
            "counts": counts,
            "citation_patterns": [
                {"label": p.get("label"), "regex": p.get("regex"),
                 "context_required": bool(p.get("context_required"))}
                for p in rec.get("citation_map", {}).get("citation_patterns", [])
            ],
        }
    if not check_only and not all_err:
        write_hosts()
        (ROOT / "corpus").mkdir(exist_ok=True)
        ci = ROOT / "corpus" / "index.json"
        try:
            prev = json.loads(ci.read_text())
        except Exception:
            prev = {}
        if prev.get("collections") != CORPUS_INDEX:      # no date-only churn
            ci.write_text(json.dumps({"generated": date.today().isoformat(),
                                      "collections": CORPUS_INDEX}, indent=1) + "\n")
    for w in all_warn:
        print("WARN ", w)
    for e in all_err:
        print("ERROR", e)
    if not check_only and not all_err:
        (ROOT / "index.json").write_text(json.dumps(index, indent=2) + "\n")
        print(f"built {len(index['jurisdictions'])} jurisdiction file(s) + index.json")
    sys.exit(1 if all_err else 0)


if __name__ == "__main__":
    main()

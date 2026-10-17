#!/usr/bin/env python3
"""corpus.py — read pre-built official text from the deep-legal-research-resources corpus.

Stdlib only. Works against a local checkout or the published repo:

    export LEGAL_SOURCES_BASE=https://raw.githubusercontent.com/jumpingtom1/deep-legal-research-resources/<sha>
    (default: the checkout this script lives in)

    corpus.py list [--jurisdiction de]
    corpus.py resolve "Super. Ct. Crim. R. 61(i)(1)"        citation → collection + unit, then get
    corpus.py get de/super-ct-crim-r 61
    corpus.py search de/super-ct-crim-r "postconviction" ["more terms"] [--any] [-n 10]
    corpus.py verify de/super-ct-crim-r 61 "exact quote"
    corpus.py check de/super-ct-crim-r [61]                  is the corpus still current? (live)

Every result starts with a banner: the official source, the capture date and
age, and a freshness verdict — OK, STALE (past the collection's stale_days)
or EXPIRED (past expire_days). EXPIRED text must not be quoted as current;
run `check`, which re-fetches the official source through fetch_doc's
allowlist/robots layer and tells you whether the unit's text is unchanged.

Integrity: each unit's sha256 is checked against its manifest and each
manifest's sha256 against corpus/index.json. A mismatch stops with an error.

Exit codes: 0 ok · 2 not found / not verified · 3 refused · 4 error · 5 integrity failure.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lstext  # noqa: E402

LOCAL_ROOT = HERE.parent
BASE = os.environ.get("LEGAL_SOURCES_BASE", "").rstrip("/")
CACHE = Path(os.environ.get("LEGAL_SOURCES_CACHE",
                            Path.home() / ".cache" / "us-legal-sources")) / "corpus"
REMOTE_HOSTS = ("raw.githubusercontent.com",)


class IntegrityError(Exception):
    pass


def _read(rel, max_age=6 * 3600):
    """Read a repo-relative file from the local checkout or the remote base."""
    if not BASE:
        p = LOCAL_ROOT / rel
        if not p.exists():
            raise FileNotFoundError(rel)
        return p.read_bytes()
    url = f"{BASE}/{rel}"
    host = re.match(r"https://([^/]+)/", url + "/")
    if not host or host.group(1) not in REMOTE_HOSTS:
        raise SystemExit(f"LEGAL_SOURCES_BASE must be https on {REMOTE_HOSTS}")
    CACHE.mkdir(parents=True, exist_ok=True)
    cf = CACHE / hashlib.sha256(url.encode()).hexdigest()[:32]
    if cf.exists() and time.time() - cf.stat().st_mtime < max_age:
        return cf.read_bytes()
    req = urllib.request.Request(url, headers={"User-Agent": "deep-legal-research-resources-corpus/1.0 (+https://github.com/jumpingtom1/deep-legal-research-resources)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise FileNotFoundError(rel)
        raise
    cf.write_bytes(data)
    return data


def index():
    return json.loads(_read("corpus/index.json"))


def manifest(cid):
    idx = index()["collections"]
    if cid not in idx:
        raise FileNotFoundError(f"collection {cid} not in corpus/index.json "
                                f"(have: {', '.join(sorted(idx))})")
    raw = _read(f"corpus/{cid}/manifest.json")
    if hashlib.sha256(raw).hexdigest() != idx[cid]["manifest_sha256"]:
        raise IntegrityError(f"manifest for {cid} does not match corpus/index.json")
    return json.loads(raw)


def unit_text(m, uid):
    u = next((x for x in m["units"] if x["id"].lower() == uid.lower()), None)
    if u is None:
        return None, None
    raw = _read(f"corpus/{m['jurisdiction']}/{m['collection']}/{u['file']}")
    if hashlib.sha256(raw).hexdigest() != u["sha256"]:
        raise IntegrityError(f"unit {uid} of {m['jurisdiction']}/{m['collection']} "
                             "fails its sha256 check")
    return u, raw.decode("utf-8")


def freshness(m):
    age = (date.today() - date.fromisoformat(m["captured"])).days
    if age > m.get("expire_days", 365):
        verdict = "EXPIRED — do not quote as current; run `corpus.py check`"
    elif age > m.get("stale_days", 180):
        verdict = "STALE — run `corpus.py check` before relying on it"
    else:
        verdict = "OK"
    return age, verdict


def banner(m, u=None):
    age, verdict = freshness(m)
    s = m["source"]
    cur = (m.get("currency") or {}).get("observed")
    lines = [f"CORPUS {m['jurisdiction']}/{m['collection']} — {m['title']}",
             f"  official source: {s['url']}" + (f" ({s['filename']})" if s.get("filename") else ""),
             f"  captured {m['captured']} ({age} days ago) · freshness: {verdict}"]
    if cur:
        lines.append(f"  edition at capture: \"{cur}\" (from {m['currency']['url']})")
    if u:
        lines.append(f"  {m.get('unit_label', 'Unit')} {u['id']} — {u['title']} · PDF pages "
                     f"{u['pages'][0]}–{u['pages'][1]} · extraction check: {u.get('check', '?')}")
        if m.get("cite_template"):
            lines.append(f"  cite as: {m['cite_template'].format(id=u['id'])} (official "
                         "PDF; corpus text is a verified extraction of it)")
    return "\n".join(lines)


# ------------------------------------------------------------------ commands
def cmd_list(a):
    for cid, c in sorted(index()["collections"].items()):
        if a.jurisdiction and not cid.startswith(a.jurisdiction + "/"):
            continue
        print(f"{cid:28} {c['units']:4} units · captured {c['captured']} · {c['title']}")


def _resolve(cite):
    for cid, c in index()["collections"].items():
        rx = c.get("cite_regex")
        if not rx:
            continue
        m = re.search(rx, cite, re.I)
        if m:
            gd = {k: v for k, v in m.groupdict().items() if v}
            uid = next((gd[k] for k in ("rule", "rule2", "section", "id") if k in gd), None)
            if uid:
                return cid, uid
    return None, None


def cmd_resolve(a):
    cid, uid = _resolve(a.citation)
    if not cid:
        print(f"NOT IN CORPUS: no collection's citation pattern matches {a.citation!r}")
        sys.exit(2)
    print(f"RESOLVED {a.citation!r} → {cid} unit {uid}\n")
    a.collection, a.unit = cid, uid
    cmd_get(a)


def cmd_get(a):
    m = manifest(a.collection)
    u, text = unit_text(m, a.unit)
    if u is None:
        near = [x["id"] for x in m["units"] if x["id"].split(".")[0] == a.unit.split(".")[0]]
        print(banner(m) + f"\n\nNOT FOUND: {m.get('unit_label', 'unit')} {a.unit} is not in "
              f"this collection. Nearby: {', '.join(near[:12]) or '—'}. This is a real "
              "answer — do not reconstruct the text.")
        sys.exit(2)
    print(banner(m, u) + "\n\n" + text)


def cmd_search(a):
    m = manifest(a.collection)
    raw = _read(f"corpus/{a.collection}/collection.jsonl")
    terms = [t.lower() for t in a.terms]
    hits = []
    for line in raw.decode("utf-8").splitlines():
        u = json.loads(line)
        t = lstext.normalise(u["text"]).lower()
        ok = any(x in t for x in terms) if a.any else all(x in t for x in terms)
        if ok:
            k = t.find(terms[0]) if terms[0] in t else 0
            hits.append((u["id"], u["title"], t[max(0, k - 120):k + 180]))
    print(banner(m) + f"\n\n{len(hits)} unit(s) match")
    for uid, title, snip in hits[:a.n]:
        print(f"\n— {uid} · {title}\n  …{snip}…")
    sys.exit(0 if hits else 2)


def cmd_verify(a):
    m = manifest(a.collection)
    u, text = unit_text(m, a.unit)
    if u is None:
        print(f"NOT FOUND: unit {a.unit}")
        sys.exit(2)
    print(banner(m, u))
    res = lstext.find_quote(text, a.quote)
    if res["found"]:
        before = text[:res["start"]]
        pages = re.findall(r"\[PDF page (\d+)\]", before)
        pg = pages[-1] if pages else u["pages"][0]
        print(f"\nVERIFIED (exact, {res['mode']}) · PDF page {pg}")
        return
    if res.get("case_only"):
        print("\nNOT VERIFIED — matches only if case is ignored. Quote the source's capitalisation.")
        sys.exit(2)
    k, n = lstext.longest_prefix_found(text, a.quote)
    print(f"\nNOT VERIFIED — the first {k} of {n} words appear in sequence in this unit.")
    sys.exit(2)


def cmd_check(a):
    """Re-fetch the official source and compare. Needs network access to it."""
    import lsnet
    m = manifest(a.collection)
    print(banner(m))
    hosts = None
    if BASE:
        hosts = json.loads(_read("hosts.json"))["hosts"]
    try:
        r = lsnet.get(m["source"]["url"], expect="pdf", max_age=3600, hosts=hosts)
    except lsnet.RefusedError as e:
        print(f"\nREFUSED: {e}\nCannot check currency live; rely on the capture date above.")
        sys.exit(3)
    except lsnet.FetchError as e:
        print(f"\nCHECK FAILED: {e}\nCannot check currency live; rely on the capture date above.")
        sys.exit(4)
    if r["sha256"] == m["source"]["sha256"]:
        print(f"\nCURRENT — the official file is byte-identical to the one captured "
              f"{m['captured']}.")
    else:
        print(f"\nSOURCE CHANGED — the official file differs from the capture "
              f"({m['source']['sha256'][:12]} → {r['sha256'][:12]}).")
        if a.unit:
            u, text = unit_text(m, a.unit)
            live = "\n".join(lstext.pdf_pages(r["body"])) + "\n" + \
                   "\n".join(lstext.pdf_pages(r["body"], layout=False))
            body = re.sub(r"^\[PDF page \d+\]$", "", text, flags=re.M)
            paras = [p for p in re.split(r"\n(?=\(\w+\) )", body) if len(p.strip()) > 40]
            missing = [p.strip()[:70] for p in paras
                       if not lstext.find_quote(live, p.strip())["found"]]
            if missing:
                print(f"  {len(missing)} of {len(paras)} paragraph(s) of unit {a.unit} are "
                      f"NOT in the current official file, e.g. {missing[0]!r}…\n"
                      "  Do not quote the corpus text; read the live file with fetch_doc.py.")
                sys.exit(2)
            print(f"  …but every paragraph of unit {a.unit} is still present verbatim in "
                  "the current official file. Safe to quote; re-ingest soon.")
        else:
            print("  Re-ingest, or pass a unit id to check whether that unit changed.")
    cp = m.get("currency")
    if cp:
        try:
            ir = lsnet.get(cp["url"], max_age=3600, hosts=hosts)
            t = re.sub(r"\s+", " ", lstext.html_text(ir["body"]))
            mm = re.search(cp["regex"], t)
            now = mm.group(0) if mm else None
            same = now == cp["observed"]
            print(f"  edition statement now: \"{now}\" — "
                  + ("unchanged since capture." if same else "CHANGED since capture — check "
                     "for amendments before quoting."))
        except Exception as e:  # noqa: BLE001
            print(f"  edition statement could not be re-read: {e}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("list")
    s.add_argument("--jurisdiction")
    s = sub.add_parser("resolve")
    s.add_argument("citation")
    s = sub.add_parser("get")
    s.add_argument("collection")
    s.add_argument("unit")
    s = sub.add_parser("search")
    s.add_argument("collection")
    s.add_argument("terms", nargs="+")
    s.add_argument("--any", action="store_true")
    s.add_argument("-n", type=int, default=10)
    s = sub.add_parser("verify")
    s.add_argument("collection")
    s.add_argument("unit")
    s.add_argument("quote")
    s = sub.add_parser("check")
    s.add_argument("collection")
    s.add_argument("unit", nargs="?")
    a = p.parse_args()
    try:
        globals()["cmd_" + a.cmd](a)
    except IntegrityError as e:
        print(f"INTEGRITY FAILURE: {e}. Do not use this text.")
        sys.exit(5)
    except FileNotFoundError as e:
        print(f"NOT FOUND: {e}")
        sys.exit(2)


if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # quiet when piped into head
    main()

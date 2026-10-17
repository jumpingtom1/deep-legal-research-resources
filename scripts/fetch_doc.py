#!/usr/bin/env python3
"""fetch_doc.py — exact text from an allowlisted official page or PDF.

The replacement for the fetch tool on long documents: nothing is summarised,
nothing is truncated, and every quote check is an exact string match.

    fetch_doc.py check   URL                      allowlist + robots only (no download)
    fetch_doc.py info    URL                      download; type, pages, size, dates
    fetch_doc.py read    URL [--pages 3-5 | --offset N] [--length 20000]
    fetch_doc.py grep    URL PATTERN [--regex] [--context 300] [--max 20]
    fetch_doc.py section URL --start REGEX [--end REGEX] [--max-chars 60000]
    fetch_doc.py verify  URL "exact quote"

Exit codes: 0 ok · 2 not found / quote not verified · 3 REFUSED (blocked
host, robots, bot challenge — never try another route) · 4 fetch error.

Hosts come from hosts.json (built from the jurisdiction records). Requests
are spaced ≥1.1 s per host across processes; responses are cached for a day
(LEGAL_SOURCES_CACHE, default ~/.cache/us-legal-sources).
"""
import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lsnet  # noqa: E402
import lstext  # noqa: E402


RESEARCH = False


def load(url, max_age):
    r = lsnet.get(url, max_age=max_age, allow_unlisted=RESEARCH)
    body = r["body"]
    ctype = r["headers"].get("Content-Type", r["headers"].get("content-type", "")).lower()
    tcache = lsnet._cache_dir("text") / f"{r['sha256']}.json"
    if tcache.exists():
        pages = json.loads(tcache.read_text())
    else:
        if body[:5] == b"%PDF-" or "pdf" in ctype:
            kind, pages = "pdf", lstext.pdf_pages(body)
            raw = lstext.pdf_pages(body, layout=False)
        else:
            m = re.search(r"charset=([\w-]+)", ctype)
            kind, pages = "html", [lstext.html_text(body, m.group(1) if m else None)]
            raw = None
        pages = {"kind": kind, "pages": pages, "raw_pages": raw}
        tcache.write_text(json.dumps(pages))
    r["kind"], r["pages"] = pages["kind"], pages["pages"]
    r["raw_pages"] = pages.get("raw_pages")
    starts, pos = [], 0
    for p in r["pages"]:
        starts.append(pos)
        pos += len(p) + 1
    r["text"] = "\n".join(r["pages"])
    r["page_starts"] = starts
    return r


def page_of(r, offset):
    import bisect
    return bisect.bisect_right(r["page_starts"], offset)


def header(r):
    h = r["headers"]
    lm = h.get("Last-Modified") or h.get("last-modified") or "—"
    cd = h.get("Content-Disposition") or h.get("content-disposition") or ""
    fn = re.search(r'filename="?([^";]+)', cd)
    return (f"SOURCE {r['final_url']}\n"
            f"  kind={r['kind']} pages={len(r['pages'])} chars={len(r['text'])} "
            f"sha256={r['sha256'][:16]} fetched={r['fetched_at']}"
            f"{' (cached)' if r.get('cached') else ''}\n"
            f"  last-modified={lm}" + (f" filename={fn.group(1)}" if fn else ""))


def cmd_check(a):
    if not RESEARCH:
        lsnet.check_allowlist(a.url)
    delay = lsnet.robots_check(a.url)
    print(f"OK  {a.url}\n  allowlisted; robots.txt permits"
          + (f"; crawl-delay {delay}s" if delay else ""))


def cmd_info(a):
    r = load(a.url, a.max_age)
    print(header(r))


def cmd_read(a):
    r = load(a.url, a.max_age)
    print(header(r))
    if a.pages:
        lo, _, hi = a.pages.partition("-")
        lo, hi = int(lo), int(hi or lo)
        for n in range(lo, min(hi, len(r["pages"])) + 1):
            print(f"\n[PDF page {n} of {len(r['pages'])}]\n{r['pages'][n - 1]}")
        return
    t = r["text"][a.offset:a.offset + a.length]
    end = a.offset + len(t)
    print(f"\n[chars {a.offset}–{end} of {len(r['text'])}; starts on page "
          f"{page_of(r, a.offset)}]" + ("" if end >= len(r["text"]) else
                                        f" — next: --offset {end}"))
    print(t)


def cmd_grep(a):
    r = load(a.url, a.max_age)
    print(header(r))
    if a.regex:
        rx = re.compile(a.pattern, re.I)
    else:   # plain text: any run of whitespace in the pattern matches any run in the page
        rx = re.compile(r"\s+".join(re.escape(w) for w in a.pattern.split()), re.I)
    hits = list(rx.finditer(r["text"]))
    print(f"\n{len(hits)} match(es)" + (f"; showing {a.max}" if len(hits) > a.max else ""))
    for m in hits[:a.max]:
        s, e = max(0, m.start() - a.context), min(len(r["text"]), m.end() + a.context)
        snip = re.sub(r"\s+", " ", r["text"][s:e])
        print(f"\n— offset {m.start()} · page {page_of(r, m.start())}\n  …{snip}…")
    sys.exit(0 if hits else 2)


def cmd_section(a):
    r = load(a.url, a.max_age)
    print(header(r))
    t = r["text"]
    ms = re.search(a.start, t, re.M)
    if not ms:
        print(f"\nNOT FOUND: start pattern {a.start!r}")
        sys.exit(2)
    end = len(t)
    if a.end:
        me = re.compile(a.end, re.M).search(t, ms.end())
        if me:
            end = me.start()
    chunk = t[ms.start():end]
    clipped = len(chunk) > a.max_chars
    print(f"\n[section chars {ms.start()}–{end}; pages {page_of(r, ms.start())}–"
          f"{page_of(r, max(ms.start(), end - 1))}"
          + (f"; CLIPPED at {a.max_chars} chars — raise --max-chars or use read --offset "
             f"{ms.start() + a.max_chars}" if clipped else "") + "]")
    print(chunk[:a.max_chars])


def cmd_verify(a):
    r = load(a.url, a.max_age)
    print(header(r))
    res = lstext.find_quote(r["text"], a.quote)
    if res["found"]:
        print(f"\nVERIFIED (exact, {res['mode']}) · page {page_of(r, res['start'])} "
              f"· offset {res['start']}")
        return
    if r.get("raw_pages"):
        # -layout can scramble hanging-indent lists; try pdftotext's reading order
        raw_text = "\n".join(r["raw_pages"])
        rr = lstext.find_quote(raw_text, a.quote)
        if rr["found"]:
            import bisect
            starts, pos = [], 0
            for ptxt in r["raw_pages"]:
                starts.append(pos)
                pos += len(ptxt) + 1
            print(f"\nVERIFIED (exact, reading-order text, {rr['mode']}) · page "
                  f"{bisect.bisect_right(starts, rr['start'])}")
            return
    if res.get("case_only"):
        print(f"\nNOT VERIFIED — matches only if case is ignored (page "
              f"{page_of(r, res['start'])}). Quote the source's capitalisation.")
        sys.exit(2)
    k, n = lstext.longest_prefix_found(r["text"], a.quote)
    print(f"\nNOT VERIFIED — the first {k} of {n} words appear in sequence; "
          "the quote is not in this document as written.")
    sys.exit(2)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--max-age", type=int, default=86400,
                   help="cache lifetime in seconds (default 1 day)")
    p.add_argument("--research", action="store_true",
                   help="maintainers only: skip the hosts.json allowlist (robots.txt, "
                        "bot-challenge refusal and rate limits still apply) to test a "
                        "host before it has a record")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("check", "info"):
        s = sub.add_parser(name)
        s.add_argument("url")
    s = sub.add_parser("read")
    s.add_argument("url")
    s.add_argument("--pages")
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--length", type=int, default=20000)
    s = sub.add_parser("grep")
    s.add_argument("url")
    s.add_argument("pattern")
    s.add_argument("--regex", action="store_true")
    s.add_argument("--context", type=int, default=300)
    s.add_argument("--max", type=int, default=20)
    s = sub.add_parser("section")
    s.add_argument("url")
    s.add_argument("--start", required=True)
    s.add_argument("--end")
    s.add_argument("--max-chars", type=int, default=60000)
    s = sub.add_parser("verify")
    s.add_argument("url")
    s.add_argument("quote")
    a = p.parse_args()
    global RESEARCH
    RESEARCH = a.research
    try:
        globals()["cmd_" + a.cmd](a)
    except lsnet.RefusedError as e:
        print(f"REFUSED: {e}")
        sys.exit(3)
    except (lsnet.FetchError, RuntimeError) as e:
        print(f"FETCH ERROR: {e}")
        sys.exit(4)


if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # quiet when piped into head
    main()

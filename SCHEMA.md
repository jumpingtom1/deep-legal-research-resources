# deep-legal-research-resources — record schema (v1, 2026-10-16)

One JSON file per jurisdiction in `data/<xx>.json` (two-letter postal code,
lower-case; `dc` for the District of Columbia). The human-readable
`jurisdictions/<xx>.md` files are **generated** from these — never edit them
by hand. The JSON is the allowlist the deep-legal-research skill obeys: a URL
or host that is not in a jurisdiction's record is not a permitted source for
that jurisdiction.

## Source policy

| Tier | What | Use |
|---|---|---|
| 1 | Official / government publisher (legislature, courts, secretary of state, state law library, official reporter) | First choice; citation target and link |
| 2 | Vetted third party: **public.law, Justia (law.justia.com), Cornell LII (law.cornell.edu)** — nothing else | Only after tier 1 fails or where no tier 1 serves text; always disclosed in the report with its currency string |

**Never guess a URL.** Every row says whether its per-item URL is
*constructible* from a citation (pattern verified on at least one real
citation) or *index-anchored* (fetch the stated index, follow real links).
**Robots.txt and bot challenges are respected, never worked around.** A host
that refuses (robots disallow, Cloudflare challenge, HTTP 401/403/451,
"site blocked") is recorded as such, not retried by another route.

## Families (A–G)

| Code | `family` value | Covers |
|---|---|---|
| A | `statutes` | The code / compiled statutes; also session laws if they matter for history |
| B | `constitution` | State constitution |
| C | `court_rules` | Rules of civil procedure, evidence, appellate procedure, criminal procedure, rules of court; where local rules live |
| D | `admin_code`, `admin_register` | Administrative code and register |
| E | `case_law` | Opinions of the high court and intermediate appellate courts (and any specialised court that matters — e.g. Delaware Chancery); official reports if free online |
| F | `subsequent_history` | Where review / leave / certiorari dispositions are published |
| G | — (top-level `citation_map`) | How to recognise this jurisdiction's authorities in a query and map them to CourtListener |

## File shape

```jsonc
{
  "schema_version": 1,
  "jurisdiction": "ca",
  "name": "California",
  "compiled": "2026-10-16",            // date this file was last edited
  "summary": "2–4 sentences: the best free route for each family, and the big gaps.",

  "citation_map": {                      // family G
    "courts": [
      { "name": "Supreme Court of California",
        "courtlistener_id": "cal",       // verified against CourtListener's court list if possible; else mark in notes
        "bluebook_abbrev": "Cal.",
        "reporters": ["Cal. 5th", "Cal. Rptr. 3d", "P.3d"],
        "public_domain_citation": null }  // e.g. "2023 IL 128004" format if the state has one
    ],
    "citation_patterns": [               // used to detect the jurisdiction from a query and route to a source
      { "family": "statutes",
        "label": "California codes",
        "examples": ["Cal. Civ. Code § 1714", "Civil Code section 1714", "Cal. Code Civ. Proc. § 437c"],
        "regex": "python regex, named groups where useful (?P<code>…) (?P<section>…)",
        "routes_to": ["ca-codes-leginfo", "ca-codes-publiclaw"] }   // source ids, in preference order
    ],
    "law_aliases": {                     // optional: citation short forms → the URL key the statute pattern needs
      "Gen. Oblig. Law": "GOB", "GOL": "GOB" },
    "notes": ""
  },

  "sources": [
    {
      "id": "ca-codes-leginfo",            // <xx>-<short-name>, unique, stable
      "family": "statutes",
      "title": "California Law (codes)",
      "publisher": "California Legislative Counsel",
      "tier": 1,
      "official_status": "official | unofficial | unknown",   // does the publisher say the online text is official?
      "official_status_evidence": "the disclaimer or statute that says so, paraphrased, with URL",
      "coverage": "what it holds; date range for case law",
      "access": {
        "mode": "constructible | index-anchored | search-only | link-only",
        "url_pattern": "https://…{code}…{section}…   (constructible only; placeholders in braces)",
        "pattern_rules": "how placeholders map from the citation (code abbreviations table, zero-padding, …)",
        "index_url": "https://… (index-anchored: where to start)",
        "navigation": "index-anchored: the exact hops, e.g. 'title index → chapter link → subchapter page holds section text'",
        "format": "html | pdf | json | xml",
        "read_via": "optional: when items are LOCATED here but READ elsewhere (e.g. listing on one host, PDFs on another), name the reading host/source id and whether it is reachable"
      },
      "text": "fetch-and-quote | link-only",
      "automation": {
        "webfetch": "ok | ok (truncated) | gated | fail | blocked | untested",  // gated = needs per-URL user approval (built URLs)
        "shell": "ok | blocked-robots | blocked-challenge | tls-error | http-error | untested",  // tested with scripts/fetch_doc.py --research
        "robots_txt": "summary of relevant rules, or 'none (404)'",
        "notes": "rate limits, JS-only rendering, crawl-delay …"
      },
      "currency": {
        "where": "where on the page the currency/edition statement appears, or 'none stated'",
        "observed": "the literal short string seen at verification (≤ 15 words)"
      },
      "hazards": ["truncation of long pages", "JS-injected text", "OCR scans", …],
      "probe": {
        "citation": "Cal. Civ. Code § 1714",
        "url": "the exact URL fetched",
        "expect": "≤ 15 words of the body text a successful fetch must contain"
      },
      "verification": {
        "status": "verified | reported | blocked | absent",
        "date": "2026-10-16",
        "by": "research | independent",
        "result": "OK | FAIL",
        "evidence": "what the probe actually returned (first words, page count, HTTP code …)"
      },
      "notes": ""
    }
  ],

  "absent": [                              // things looked for and NOT available — recorded so no run rediscovers them
    { "family": "case_law", "what": "Official Reports text (California Official Reports)", "evidence": "…", "date": "2026-10-16" }
  ],

  "script_candidates": [                   // structured endpoints that could justify a per-state script later
    { "source_id": "…", "why": "JSON API / stable listings / …" }
  ],

  "corpus_candidates": [                   // long official documents the fetch tool truncates → ingest
    { "source_id": "…", "url": "https://… (the official PDF/page)", "why": "fetch tool stops at Rule 29 of 64",
      "split_hint": "bold 'Rule N.' headings at left margin", "bulk": "official bulk download URL, if any" }
  ],

  "open_questions": []
}
```

## Verification vocabulary

- **verified** — the probe was actually run on `date` and its evidence is
  recorded. Only verified rows may be used to quote.
- **reported** — the source exists (linked from an official page, or
  described reliably) but its probe has not been run or did not run cleanly.
  Usable as a link, never quoted.
- **blocked** — the host refused automated access (robots, challenge,
  401/403/451, site-blocked). Never fetched by another route.
- **absent** — looked for and does not exist / is not free.

`by: research` = verified by the agent that found the source;
`by: independent` = re-verified by a separate agent working only from this
record. A row is release-ready only when independently verified.

## Read routes (derived at build time — not stored in the records)

Each rendered row lists the routes it supports, in order:

| Route | When it appears | Tool |
|---|---|---|
| **corpus** | a manifest in `corpus/<xx>/<collection>/` names the row's `id` as its `source_id` | `scripts/corpus.py` — stdlib only, reads the repo over raw.githubusercontent.com |
| **script** | `automation.shell == "ok"` and `text == "fetch-and-quote"`, row not blocked | `scripts/fetch_doc.py` — live exact text; enforces `hosts.json`, robots.txt, bot-challenge refusal, 1.1 s/host |
| **fetch tool** | `automation.webfetch` starts with `ok` | WebFetch — locate and link; quote only under the two-fetch rule |

`hosts.json` (generated) is the script route's allowlist: a host is
`allowed` if any non-blocked row names it, `blocked` if every row naming it is
blocked or absent. Robots rules are still checked per URL.

## Corpus collections

A collection is one official document split into units (rules or sections),
built by `scripts/ingest.py corpus-config/<xx>-<collection>.json`:

- `split.method` — `pdf-bold-headings` (bold, left-margin lines matching
  `heading_regex` with named groups `id`, `title`); `part_regex` skips
  centred part headings; `extra_boundaries` start non-rule units (appendices).
- `cite_pattern` — label (prefix) of a `citation_map.citation_patterns` entry
  in the jurisdiction record; `corpus/index.json` copies that record's regex,
  so citation routing is defined in exactly one place.
- `currency_probe` — `{url, regex}` for the publisher's edition/amendment
  statement, recorded at ingest and re-checked by `corpus.py check`.
- `stale_days` / `expire_days` — freshness verdicts printed on every read.
- `expect_units`, `min_coverage` — ingest gates.

Ingest refuses to write unless every unit is confirmed by an independent
extraction (`pdftotext` in layout or reading order; whole unit, else line by
line), coverage ≥ `min_coverage`, and all `expect_units` exist. Integrity on
read: unit sha256 ↔ manifest, manifest sha256 ↔ `corpus/index.json`.

Only **official government text** is ingested — never tier-2 publishers'
pages, whose compilations and terms are their own.

## Copyright / evidence hygiene

Evidence strings are short: ≤ 15 words of quoted page text per row. The
records hold URLs and instructions, never reproduced statute or opinion text.

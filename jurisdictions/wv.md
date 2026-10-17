# West Virginia (WV) — free legal sources

_Generated from `data/wv.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: code.wvlegislature.gov serves one page per section at a URL built from the citation (/55-7-8a/), readable by WebFetch and the script, plus whole-chapter PDFs (/pdf/55/); the old www.wvlegislature.gov/WVCODE/ viewer is robots-blocked; Justia 2025 is the tier-2 fallback. The constitution is one long page on code.wvlegislature.gov (WebFetch stops in Art. VII) with a second Legislature copy and Justia. Court rules are single long HTML pages on courtswv.gov (all beyond the WebFetch window: corpus candidates). Code of State Rules: Secretary of State final-file PDFs via id hops (old rules are image scans); Cornell LII mirrors it but can be decades stale; the State Register PDFs are image-only. Case law: courtswv.gov archives (Supreme Court 1991-, ICA 2022-) are searchable by plain GET; slip pagination only; subsequent history by party name.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Appeals of West Virginia | `wva (unverified)` | W. Va. | W. Va., S.E.2d, S.E. | — |
| Intermediate Court of Appeals of West Virginia (from July 2022) | `wvactapp (unverified)` | W. Va. Ct. App. | S.E.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| West Virginia Code | `W. Va. Code § 55-7-8a`; `W. Va. Code § 61-2-1 (2021)`; `W.Va. Code § 55-7-13a(a)`; `W. Va. Code Ann. § 29A-5-4`; `W. Va. Code §§ 55-7-13a to -13d`; `West Virginia Code § 55-7-8a`; `section 8a, article 7, chapter 55 of the Code of West Virginia` | `wv-code-legislature` → `wv-code-justia` → `wv-code-chapter-pdf` |
| West Virginia Code (bare section, in-state style '§55-7-8a') *(only once this jurisdiction is known)* | `§55-7-8a`; `§ 61-2-1 of this code` | `wv-code-legislature` → `wv-code-justia` |
| Acts of the West Virginia Legislature (session laws) | `2015 W. Va. Acts ch. 59`; `2025 W. Va. Acts 1`; `Acts of the Legislature of West Virginia, 2025, ch. 1` | `wv-acts` |
| Code repeal notes ('Acts, 2015 Reg. Sess., Ch. 59') *(only once this jurisdiction is known)* | `Acts, 2015 Reg. Sess., Ch. 59` | `wv-acts` |
| West Virginia Constitution | `W. Va. Const. art. III, § 10`; `W. Va. Const. art. VIII, § 1`; `Article III, Section 10 of the West Virginia Constitution`; `article III, section 17 of the Constitution of West Virginia` | `wv-constitution-code` → `wv-constitution-home` → `wv-constitution-justia` |
| West Virginia Rules of Civil Procedure | `W. Va. R. Civ. P. 12(b)(6)`; `W.Va.R.Civ.P. 56(c)`; `Rule 12(b)(6) of the West Virginia Rules of Civil Procedure` | `wv-rules-civil` |
| West Virginia Rules of Evidence | `W. Va. R. Evid. 702`; `Rule 404(b) of the West Virginia Rules of Evidence` | `wv-rules-evidence` |
| West Virginia Rules of Appellate Procedure | `W. Va. R. App. P. 21(c)`; `Rule 10(c)(7) of the West Virginia Rules of Appellate Procedure` | `wv-rules-appellate` |
| West Virginia Rules of Criminal Procedure | `W. Va. R. Crim. P. 35(b)`; `Rule 11 of the West Virginia Rules of Criminal Procedure` | `wv-rules-criminal` |
| West Virginia Trial Court Rules | `W. Va. Tr. Ct. R. 24.01`; `Rule 22.01 of the West Virginia Trial Court Rules` | `wv-rules-trial-court` |
| Trial Court Rules (bare 'Trial Court Rule 24.01') *(only once this jurisdiction is known)* | `Trial Court Rule 24.01`; `T.C.R. 22.01` | `wv-rules-trial-court` |
| West Virginia Rules of Professional Conduct | `W. Va. R. Prof'l Conduct 1.7`; `Rule 1.7 of the West Virginia Rules of Professional Conduct` | `wv-rules-professional-conduct` |
| Bare 'Rule N of the Rules of Civil/Criminal/Appellate Procedure' (no state named) *(only once this jurisdiction is known)* | `Rule 12(b)(6) of the Rules of Civil Procedure`; `Rule 21 of the Rules of Appellate Procedure` | `wv-rules-civil` → `wv-rules-criminal` → `wv-rules-appellate` |
| West Virginia Code of State Rules | `W. Va. Code R. § 110-1H-1`; `W. Va. C.S.R. § 78-3-1`; `110 C.S.R. 1H`; `110CSR15`; `W. Va. Code St. R. § 64-21-1` | `wv-csr-sos` → `wv-csr-lii` |
| West Virginia State Register | `43 W. Va. Reg. 1201`; `W. Va. Reg. Vol. XLIII, Issue 25` | `wv-register-sos` |
| West Virginia Reports (official reporter) with parallel S.E./S.E.2d | `Painter v. Peavy, 192 W. Va. 189, 451 S.E.2d 755 (1994)`; `State v. Guthrie, 194 W. Va. 657, 461 S.E.2d 163 (1995)`; `Syl. Pt. 3, Aetna Cas. & Sur. Co. v. Fed. Ins. Co. of N.Y., 148 W. Va. 160, 133 S.E.2d 770 (1963)` | `wv-sca-opinions` → `wv-cases-justia` |
| Syllabus point (West Virginia-specific pinpoint form) *(only once this jurisdiction is known)* | `Syl. Pt. 3, Aetna Cas. & Sur. Co. v. Fed. Ins. Co. of N.Y., 148 W. Va. 160, 133 S.E.2d 770 (1963)`; `syl. pt. 2, State v. Guthrie` | `wv-sca-opinions` → `wv-cases-justia` |
| S.E.2d with West Virginia court parenthetical | `461 S.E.2d 163 (W. Va. 1995)`; `451 S.E.2d 755, 758 (W. Va. 1994)` | `wv-sca-opinions` → `wv-ica-opinions` → `wv-cases-justia` |
| Memorandum decisions and docket cites (Supreme Court 'No. 25-884'; R. App. P. 21(e) form) | `Smith v. Jones, No. 11-098 (W.Va. Supreme Court, January 15, 2011) (memorandum decision)`; `Murray Am. Energy, Inc. v. Gasvoda, No. 25-884 (W. Va. June 2026) (memorandum decision)` | `wv-sca-opinions` → `wv-cases-justia` |
| Intermediate Court of Appeals docket ('22-ICA-208') | `Ford Motor Co. v. Tyler, No. 22-ICA-208 (W. Va. Ct. App. Dec. 8, 2023)`; `No. 25-ICA-78` | `wv-ica-opinions` → `wv-cases-justia` |
| Bare Supreme Court docket ('No. 22-765', older 'No. 32783') *(only once this jurisdiction is known)* | `No. 22-765`; `No. 32783` | `wv-sca-opinions` → `wv-cases-justia` |

Regexes (case-insensitive):

- West Virginia Code: `(?:W\.\s*Va\.\s*Code(?:\s+Ann\.)?|West\s+Virginia\s+Code|Code\s+of\s+West\s+Virginia)\s*,?\s*§+\s*(?P<chapter>\d{1,2}[A-Z]?)-(?P<article>\d{1,2}[A-Z]?)-(?P<section>\d{1,3}[A-Za-z]?)(?![\w-])|sec(?:tion|\.)\s+(?P<section2>\d{1,3}[A-Za-z]?),\s+art(?:icle|\.)\s+(?P<article2>\d{1,2}[A-Z]?),\s+ch(?:apter|\.)\s+(?P<chapter2>\d{1,2}[A-Z]?)\s+of\s+the\s+(?:Code\s+of\s+West\s+Virginia|West\s+Virginia\s+Code)`
- West Virginia Code (bare section, in-state style '§55-7-8a'): `§\s*(?P<chapter>\d{1,2}[A-Z]?)-(?P<article>\d{1,2}[A-Z]?)-(?P<section>\d{1,3}[A-Za-z]?)(?![\w-])`
- Acts of the West Virginia Legislature (session laws): `(?P<year>(?:18|19|20)\d\d)\s+W\.\s*Va\.\s*Acts\s+(?:ch\.|c\.)?\s*(?P<chapter>\d+)|Acts\s+of\s+the\s+(?:West\s+Virginia\s+)?Legislature(?:\s+of\s+West\s+Virginia)?,?\s+(?P<year2>(?:18|19|20)\d\d),?\s+(?:ch\.|c\.|chapter)\s*(?P<chapter2>\d+)`
- Code repeal notes ('Acts, 2015 Reg. Sess., Ch. 59'): `Acts,\s*(?P<year>(?:19|20)\d\d)\s+(?:Reg\.|\d\w*\s+Ex\.)\s*Sess\.,\s*Ch\.\s*(?P<chapter>\d+)`
- West Virginia Constitution: `W\.\s*Va\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§+\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+),\s+Section\s+(?P<section2>\d+[a-z]?)\s+of\s+the\s+(?:West\s+Virginia\s+Constitution|Constitution\s+of\s+West\s+Virginia)`
- West Virginia Rules of Civil Procedure: `W\.\s*Va\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Rules\s+of\s+Civil\s+Procedure`
- West Virginia Rules of Evidence: `W\.\s*Va\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Rules\s+of\s+Evidence`
- West Virginia Rules of Appellate Procedure: `W\.\s*Va\.\s*R\.\s*App\.\s*P\.\s*(?P<rule>\d+)|Rule\s+(?P<rule2>\d+)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Rules\s+of\s+Appellate\s+Procedure`
- West Virginia Rules of Criminal Procedure: `W\.\s*Va\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Rules\s+of\s+Criminal\s+Procedure`
- West Virginia Trial Court Rules: `W\.\s*Va\.\s*Tr(?:ial)?\.?\s*C(?:our)?t\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+\.\d+)|Rule\s+(?P<rule2>\d+\.\d+)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Trial\s+Court\s+Rules`
- Trial Court Rules (bare 'Trial Court Rule 24.01'): `(?:Trial\s+Court\s+Rule|T\.\s*C\.\s*R\.)\s*(?P<rule>\d+\.\d+)`
- West Virginia Rules of Professional Conduct: `W\.\s*Va\.\s*R(?:ules)?\.?\s*(?:of\s+)?Prof(?:'?l|essional)\.?\s*Conduct\s*(?P<rule>\d\.\d+)|Rule\s+(?P<rule2>\d\.\d+)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+West\s+Virginia\s+Rules\s+of\s+Professional\s+Conduct`
- Bare 'Rule N of the Rules of Civil/Criminal/Appellate Procedure' (no state named): `Rule\s+(?P<rule>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Rules\s+of\s+(?P<set>Civil|Criminal|Appellate)\s+Procedure`
- West Virginia Code of State Rules: `W\.\s*Va\.\s*(?:Code\s+(?:St\.\s*)?R\.|C\.\s*S\.\s*R\.)\s*§*\s*(?P<title>\d{1,3})-(?P<series>\d{1,2}[A-Z]?)(?:-(?P<section>\d+))?|(?P<title2>\d{1,3})\s*C\.?\s*S\.?\s*R\.?\s*(?P<series2>\d{1,2}[A-Z]?)(?![\w.-])`
- West Virginia State Register: `(?P<volume>\d{1,2})\s+W\.\s*Va\.\s*Reg\.\s*(?P<page>\d+)|W\.\s*Va\.\s*Reg\.,?\s*Vol\.\s*(?P<volroman>[IVXLC]+),?\s*Issue\s*(?P<issue>\d+)`
- West Virginia Reports (official reporter) with parallel S.E./S.E.2d: `(?P<volume>\d{1,3})\s+W\.\s*Va\.\s+(?P<page>\d{1,4})(?!\d)(?:,\s*(?P<sevol>\d{1,3})\s+S\.E\.(?:\s*2d)?\s+(?P<sepage>\d{1,4}))?`
- Syllabus point (West Virginia-specific pinpoint form): `Syl(?:labus)?\.?\s+(?:Pts?\.|points?)\s*(?P<point>\d+)`
- S.E.2d with West Virginia court parenthetical: `(?P<volume>\d{1,3})\s+S\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,4})\s*(?:,\s*\d+)?\s*\((?P<court>W\.\s*Va\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Memorandum decisions and docket cites (Supreme Court 'No. 25-884'; R. App. P. 21(e) form): `No\.\s*(?P<docket>\d{2}-\d{3,4})\s*\((?:W\.\s*Va\.|West\s+Virginia)`
- Intermediate Court of Appeals docket ('22-ICA-208'): `(?P<docket>\d{2}-ICA-\d{1,4})`
- Bare Supreme Court docket ('No. 22-765', older 'No. 32783'): `No\.\s*(?P<docket>\d{2}-\d{3,4}|\d{5})(?!\d)`

Short forms → URL key:

W. Va. Code → `code`; W.Va. Code → `code`; WV Code → `code`; West Virginia Code → `code`; Code of West Virginia → `code`; W. Va. Code Ann. → `code`; W. Va. Code R. → `csr`; W. Va. C.S.R. → `csr`; CSR → `csr`; C.S.R. → `csr`; W. Va. Code St. R. → `csr`; W. Va. R. Civ. P. → `rcp`; WVRCP → `rcp`; W. Va. R. Evid. → `rev`; WVRE → `rev`; W. Va. R. App. P. → `rap`; W. Va. R. Crim. P. → `rcrp`; W. Va. Tr. Ct. R. → `tcr`; TCR → `tcr`; W. Va. R. Prof'l Conduct → `rpc`

West Virginia Code sections are always chapter-article-section (55-7-8a); the URL is https://code.wvlegislature.gov/{chapter}-{article}-{section}/ with letters in either case (site links use upper case: 55-7-8A). Older state and court style writes '§55-7-8a' with no 'W. Va. Code' prefix and the prose form 'section 8a, article 7, chapter 55 of the Code of West Virginia'; the bare § form is context_required because Kentucky-, Tennessee- and Arkansas-style three-part numbers look the same. A '§§ 55-7-13a to -13d' range is a span: the regex takes only the first section (the (?![\w-]) guard keeps '13a' from swallowing the range). Code of State Rules: Bluebook 'W. Va. Code R. § 110-1H-1' = title 110, series 1H, section 1; the SOS lookup key pads the series to two digits (110-01H) while Cornell LII uses the unpadded form (110-1H-1). Case law: the official reporter is West Virginia Reports (W. Va.), printed by West with S.E./S.E.2d parallels; neither is free online, so free texts carry slip pagination only. West Virginia opinions put holdings in numbered syllabus points ('Syl. Pt. 3'), which are cited as pinpoints. Memorandum decisions are citable under R. App. P. 21(e) if labelled '(memorandum decision)'. The Intermediate Court of Appeals (W. Va. Ct. App.) has decided cases since July 2022 with dockets 'YY-ICA-N'. No public-domain citation format exists. Bare 'Rule N of the Rules of Civil Procedure', bare dockets and syllabus points are generic and route only with West Virginia context. CourtListener ids 'wva' and 'wvactapp' are from memory and unverified. Westlaw cites ('2023 WL …') cannot be resolved to a free URL: search by party name instead.

## A. Statutes / code

### `wv-acts` — Acts of the Legislature (session laws, annual PDF volumes)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts 1863 to 2025 (2023 onward split into Vol_1/Vol_2/Vol_3), plus 1872 constitutional convention and municipal charters volumes.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wvlegislature.gov/legisdocs/publications/acts/Acts_{year}[_Vol_{n}].pdf`
  - Placeholders: Older years are a single Acts_{year}.pdf; recent years are split (Acts_2025_Vol_1.pdf, Acts_2024_Vol_3.pdf) and the unsplit name 404s (Acts_2023.pdf → 404). Take the exact file from the index. Inside a volume, chapters start 'CHAPTER N' followed by the bill number.
  - Index: `https://www.wvlegislature.gov/Educational/publications.cfm#acts`
  - Navigation: publications page → Acts section → year/volume PDF → search 'CHAPTER N'
- **Automation:** WebFetch untested · shell ok · robots: www.wvlegislature.gov: /legisdocs/ and /Educational/ not disallowed (Disallow list covers /WVCODE/, /apps/, /media/, /js/ …)
  - Volumes are huge (2025 Vol. 1: 1,088 pp, 2.0M chars): fetch_doc.py grep only.
- **Currency:** none
- **Official status:** Scanned/compiled bound volumes on the Legislature's publications page; no authentication statement.
- **Hazard:** very large PDFs
- **Hazard:** split-volume file names not derivable
- **Hazard:** a chapter can fall in any volume
- **Probe:** 2025 W. Va. Acts ch. 1 (H.B. 3272) → `https://www.wvlegislature.gov/legisdocs/publications/acts/Acts_2025_Vol_1.pdf` — expect: "CHAPTER 1 (H. B. 3272 - By Delegates Akers"
- **Evidence (2026-10-17):** fetch_doc: application/pdf, 1,088 pages, Last-Modified 14 Mar 2026; grep 'CHAPTER 1' at p. 37: 'ACTS SECOND REGULAR SESSION, 2025 CHAPTER 1 (H. B. 3272'. Acts_2023.pdf → HTTP 404 (split volumes).
- **Notes:** Enrolled bills per session are also linked from each Code section's 'Signed Bills' block.

### `wv-code-chapter-pdf` — West Virginia Code — per-chapter PDF

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole chapter as one PDF, generated on request and dated the day of download.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://code.wvlegislature.gov/pdf/{chapter}/`
  - Placeholders: chapter as cited (55, 29A). Sections appear as '§55-7-8a. Heading.' at the left margin.
  - Index: `https://code.wvlegislature.gov/`
- **Automation:** WebFetch untested · shell ok · robots: permitted (see wv-code-legislature)
  - Chapter 55 PDF: 436 pages, 656,691 characters — far beyond WebFetch; use fetch_doc.py or ingest. WebFetch not tried (budget, then rate limit).
- **Currency:** page footer of every page (generation date) — observed: "October 17, 2026       Page 1 of 436"
- **Official status:** Generated by code.wvlegislature.gov (the 'pdf' icon on each chapter page); watermark 'WV Legislature'; no authentication statement.
- **Hazard:** very large (chapter 55 = 436 pp)
- **Hazard:** date in the footer is the generation date, not a currency date
- **Hazard:** diagonal watermark letters interleave with text in extraction on the cover page
- **Probe:** W. Va. Code ch. 55 → `https://code.wvlegislature.gov/pdf/55/` — expect: "No action shall be brought in any of the following cases:"
- **Evidence (2026-10-17):** fetch_doc: 200 application/pdf, 436 pages, 656,691 chars, Last-Modified = fetch time; starts 'WEST VIRGINIA CODE CHAPTER 55' then '§55-1-1. When writing required.'
- **Notes:** Best bulk route for the Code (one request per chapter, ~150 chapters with letter suffixes).

### `wv-code-legacy-wvcode` — Legacy WV Code pages (www.wvlegislature.gov/WVCODE/)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · West Virginia Legislature · text: **link-only** · official: unknown
- **Coverage:** Old ColdFusion code and constitution viewer (e.g. /WVCODE/WV_CON.cfm).
- **Access:** `link-only` · format html
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.wvlegislature.gov: User-agent * — Disallow: /WVCODE/ (plus /apps/, /media/ and others)
  - Use code.wvlegislature.gov instead. Note /wvcodeentire.htm (outside /WVCODE/) is allowed and is a full section index linking to code.wvlegislature.gov.
- **Currency:** not read
- **Official status:** Not read: robots.txt disallows the path.
- **Hazard:** robots disallow — never fetch by any route
- **Probe:** W. Va. Const. (legacy viewer) → `https://www.wvlegislature.gov/WVCODE/WV_CON.cfm`
- **Evidence (2026-10-17):** fetch_doc: REFUSED: robots.txt on www.wvlegislature.gov disallows /WVCODE/WV_CON.cfm (rule: Disallow: /WVCODE/).

### `wv-code-legislature` — West Virginia Code (code.wvlegislature.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** All chapters 1-64 of the West Virginia Code; one HTML page per section, with bill history ('Bill History For §55-7-8a') and links to enrolled bills.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://code.wvlegislature.gov/{chapter}-{article}-{section}/`
  - Placeholders: chapter, article and section exactly as cited, joined by hyphens, letters kept (55-7-8a, 61-2-1, 29A-5-4); letter case does not matter (site links use 55-7-8A, lower-case 55-7-8a also serves the section). Article TOC: https://code.wvlegislature.gov/{chapter}-{article}/ (lists every section with its heading, no text); chapter TOC: https://code.wvlegislature.gov/{chapter}/ (lists articles). A complete section index (every section link on one page) is https://www.wvlegislature.gov/wvcodeentire.htm.
  - Index: `https://code.wvlegislature.gov/`
- **Automation:** WebFetch ok · shell ok · robots: code.wvlegislature.gov: fetch_doc check reports robots.txt permits; reading robots.txt directly got 'Connection reset by peer' once
  - Section pages are ~12-13K characters, mostly the chapter menu; the body sits after the 'ARTICLE N.' heading near offset 6.7K. WebFetch returns the body cleanly.
- **Currency:** page footer (no as-of date) — observed: "updated regularly as new legislation takes effect"
- **Official status:** Footer says only 'These West Virginia Code sections are updated regularly as new legislation takes effect' and refers to the Bill Status database for effective dates; no official-version or UELMA authentication statement found (https://code.wvlegislature.gov/55-7-8a/). The annotated Michie's West Virginia Code (LexisNexis) is the printed edition.
- **Hazard:** no as-of date: check the 'Bill History' block on the page for the latest amending act
- **Hazard:** page text starts with a long chapter menu before the body
- **Hazard:** legacy www.wvlegislature.gov/WVCODE/ pages are robots-disallowed (see wv-code-legacy-wvcode)
- **Probe:** W. Va. Code § 55-7-8a → `https://code.wvlegislature.gov/55-7-8a/` — expect: "In addition to the causes of action which survive at common law"
- **Evidence (2026-10-17):** WebFetch: YES, body '(a) In addition to the causes of action which survive', (a)-(f) complete, not truncated; footer 'Copyright © 2026 West Virginia Code'. fetch_doc: 200 html 13,029 chars, heading '§55-7-8a. Actions which survive' at offset 6714. Second citation W. Va. Code § 61-2-1 at /61-2-1/: fetch_doc body 'Murder by poison, lying in wait, imprisonment, starving'.
- **Notes:** Bill history on each page lists amending bills by session (e.g. 2025 HB3162 for § 55-7-8a).

### `wv-code-justia` — Justia — West Virginia Code (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** West Virginia Code, per-section pages; unversioned URL serves the 2025 edition.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/west-virginia/chapter-{chapter}/article-{article}/section-{chapter}-{article}-{section}/`
  - Placeholders: chapter and article as cited, lower-case letters (chapter-29a); section slug repeats the full number (section-61-2-1, section-55-7-8a). Year-specific: insert /{year}/ after /west-virginia/.
  - Index: `https://law.justia.com/codes/west-virginia/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell (Cloudflare challenge on robots.txt)
  - fetch_doc: 'law.justia.com refused automated access earlier (robots.txt challenge)'. WebFetch only.
- **Currency:** page header and citation line — observed: "2025 West Virginia Code; 'WV Code § 61-2-1 (2025)'"
- **Official status:** Third-party compilation; edition-year banner only.
- **Hazard:** edition lags the official text by up to a year
- **Hazard:** shell blocked by Cloudflare
- **Probe:** W. Va. Code § 61-2-1 → `https://law.justia.com/codes/west-virginia/chapter-61/article-2/section-61-2-1/` — expect: "Murder by poison, lying in wait, imprisonment, starving, or by"
- **Evidence (2026-10-17):** WebFetch: YES, body 'Murder by poison, lying in wait, imprisonment, starving, or by'; '2025 West Virginia Code'; 'WV Code § 61-2-1 (2025)'; not truncated.
- **Notes:** Only one section probed on Justia; the pattern follows Justia's standard code layout.

## B. Constitution

### `wv-constitution-code` — The Constitution of West Virginia (code.wvlegislature.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1872 as amended, whole text on one page with editor's notes and amendment history.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://code.wvlegislature.gov/west-virginia-constitution`
  - Placeholders: Single page; articles headed 'ARTICLE VIII.' and sections '§1.' preceded by a catch-line (e.g. 'Safeguards for Life, Liberty and Property §10.'). Locate by article heading, then '§N.'.
  - Index: `https://code.wvlegislature.gov/west-virginia-constitution`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: permitted
  - WebFetch: page text 134,777 chars; window 1 ends in Art. VII § 14 — Articles VIII onward need offset=100000. fetch_doc reads the whole page (277,437 chars).
- **Currency:** page heading — observed: "As Ratified in 1872 and Subsequently Amended"
- **Official status:** Legislature-hosted; no official/authentication statement.
- **Hazard:** single long page; WebFetch truncation after Art. VII
- **Hazard:** editor's notes and superseded text interleaved with sections
- **Probe:** W. Va. Const. art. III, § 10 → `https://code.wvlegislature.gov/west-virginia-constitution` — expect: "No person shall be deprived of life, liberty, or property, without due process of law"
- **Evidence (2026-10-17):** WebFetch: Art. III § 10 YES 'No person shall be deprived of life, liberty, or property,'; Art. VIII § 1 NOT PRESENT (truncated in Art. VII § 14). fetch_doc: 277,437 chars; Art. VIII § 1 at offset 106,557 'The judicial power of the State shall be vested solely'.
- **Notes:** Corpus candidate.

### `wv-constitution-home` — Constitution of West Virginia (home.wvlegislature.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution on one page; sections headed 'N-N. Catchline.' (e.g. '8-1. Judicial power.').
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://home.wvlegislature.gov/constitution-of-west-virginia/`
  - Placeholders: Single page; section heading '{article_arabic}-{section}.' (Art. VIII § 1 → '8-1.').
  - Index: `https://www.wvlegislature.gov/`
- **Automation:** WebFetch untested · shell ok · robots: not separately read; fetch_doc reported no refusal
  - 211,905 chars by fetch_doc: WebFetch would truncate.
- **Currency:** none observed
- **Official status:** Linked from the Legislature home page menu 'WV CONSTITUTION'; no official statement.
- **Hazard:** single long page
- **Hazard:** second independent tier-1 copy: compare with wv-constitution-code when quoting
- **Probe:** W. Va. Const. art. VIII, § 1 → `https://home.wvlegislature.gov/constitution-of-west-virginia/` — expect: "The judicial power of the state shall be vested solely in a supreme court of appeals"
- **Evidence (2026-10-17):** fetch_doc: 211,905 chars; grep at offset 84,625: 'ARTICLE VIII 8-1. Judicial power. The judicial power of the state shall be vested solely'.

### `wv-constitution-justia` — Justia — West Virginia Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page with in-page #articleN anchors.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/west-virginia/`
  - Placeholders: single page; anchors do not change what WebFetch reads — use offset=100000 for Art. VIII onward.
  - Index: `https://law.justia.com/constitution/west-virginia/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - 136,848 chars; window 1 ends in Art. VIII § 13.
- **Currency:** none stated
- **Official status:** Third-party; no currency statement.
- **Hazard:** page exceeds WebFetch window
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Probe:** W. Va. Const. art. III, § 10 → `https://law.justia.com/constitution/west-virginia/` — expect: "No person shall be deprived of life, liberty, or property,"
- **Evidence (2026-10-17):** WebFetch: § 3-10 YES 'No person shall be deprived of life, liberty, or property,'; single page; truncated in Art. VIII (section 8-13); no currency statement.

## C. Court rules

### `wv-rules-appellate` — West Virginia Rules of Appellate Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules for both the Supreme Court and the Intermediate Court of Appeals (effective for ICA appeals from July 1, 2022), one HTML page; Rule 21 governs memorandum decisions and their citation.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/rules-appellate-procedure`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 21. Memorandum decisions' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch untested · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - Page is 180,778 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. R. App. P. 21(e) → `https://www.courtswv.gov/legal-community/court-rules/rules-appellate-procedure` — expect: "Memorandum decisions may be cited in any court or administrative tribunal in this State"
- **Evidence (2026-10-17):** fetch_doc: 180,778 chars; Rule 21 at offset 102,673; 21(e) 'Memorandum decisions may be cited in any court or administrative tribunal in this State'. WebFetch not run.

### `wv-rules-civil` — West Virginia Rules of Civil Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 1-87 (2025 revision) on one HTML page; the pre-2025 rules are a separate PDF ('Former West Virginia Rules of Civil Procedure', linked from the court rules index).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/rules-civil-procedure-contents`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 12. Defenses and objections' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch ok (truncated) · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - WebFetch window 1 ends in Rule 23(f)(2); a URL typed from the pattern needed approval once (gated), the same URL from a search result went through. Page is 268,988 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. R. Civ. P. 12(b) → `https://www.courtswv.gov/legal-community/court-rules/rules-civil-procedure-contents` — expect: "Every defense to a claim for relief in any pleading"
- **Evidence (2026-10-17):** WebFetch (search-sourced URL): Rule 12(b) YES 'Every defense to a claim for relief in any pleading'; Rule 56(a) NOT PRESENT; truncated in Rule 23(f)(2); no currency statement (first, built-URL attempt was PROVENANCE_REQUIRED). fetch_doc: 268,988 chars; Rule 12 at offset 54,061; Rule 56 'Summary judgment. (a) Motion for summary judgment' at offset 221,933.

### `wv-rules-criminal` — West Virginia Rules of Criminal Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 1-61, one HTML page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/rules-criminal-procedure-contents`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 35. Correction or reduction of sentence' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch untested · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - Page is 148,932 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. R. Crim. P. 35(a) → `https://www.courtswv.gov/legal-community/court-rules/rules-criminal-procedure-contents` — expect: "The court may correct an illegal sentence at any time"
- **Evidence (2026-10-17):** fetch_doc: 148,932 chars; 'Rule 35. Correction or reduction of sentence. (a) Correction of sentence' at offset 110,712. WebFetch not run.

### `wv-rules-evidence` — West Virginia Rules of Evidence

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 101-1101 with reporter's notes, one HTML page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/rules-evidence-contents`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 702. Testimony by Expert Witnesses' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch untested · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - Page is 101,132 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. R. Evid. 702 → `https://www.courtswv.gov/legal-community/court-rules/rules-evidence-contents` — expect: "If scientific, technical, or other specialized knowledge will assist the trier of fact"
- **Evidence (2026-10-17):** fetch_doc: 101,132 chars; 'Rule 702. Testimony by Expert Witnesses (a) If scientific, technical, or other specialized knowledge' at offset 59,165. WebFetch not run.

### `wv-rules-professional-conduct` — West Virginia Rules of Professional Conduct

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 1.0-8.5 with comments, one HTML page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/west-virginia-rules-professional-conduct`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 1.7 Conflict of Interest; Current Clients' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch untested · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - Page is 385,913 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. R. Prof'l Conduct 1.7 → `https://www.courtswv.gov/legal-community/court-rules/west-virginia-rules-professional-conduct` — expect: "Except as provided in paragraph (b), a lawyer shall not represent a client"
- **Evidence (2026-10-17):** fetch_doc: 385,913 chars; 'Rule 1.7 Conflict of Interest; Current Clients (a) Except as provided in paragraph (b)' at offset 82,093. WebFetch not run.

### `wv-rules-trial-court` — West Virginia Trial Court Rules

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Trial Court Rules (decimal numbering, e.g. 24.01), one HTML page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courtswv.gov/legal-community/court-rules/wv-trial-court-rules-contents`
  - Placeholders: One HTML page holds the whole rule set (table of contents, then every rule in order). Locate a rule by its heading 'Rule 24.01. Generally' (e.g. grep 'Rule 12\. ' — the first hit is usually the contents line, the second the rule itself).
  - Index: `https://www.courtswv.gov/legal-community/court-rules`
  - Navigation: court rules index → rule-set link → single full-text page
- **Automation:** WebFetch untested · shell ok · robots: www.courtswv.gov: Drupal default — disallows /admin/, /search/, /user/*, /node/add/; /legal-community/ and /sites/default/pubfilesmnt/ allowed
  - Page is 220,561 characters as extracted by fetch_doc.py, beyond the ~100K WebFetch window: use fetch_doc.py (grep/section) or the corpus.
- **Currency:** none stated on the page; individual rules carry bracketed '[Effective …]' / '[Amended …]' notes
- **Official status:** Published by the Court on courtswv.gov/legal-community/court-rules; no official/unofficial statement found on the page.
- **Hazard:** whole rule set on one long page (WebFetch truncation)
- **Hazard:** no currency statement for the set
- **Hazard:** first grep hit for 'Rule N.' is the table of contents
- **Probe:** W. Va. Tr. Ct. R. 24.01 → `https://www.courtswv.gov/legal-community/court-rules/wv-trial-court-rules-contents` — expect: "Unless otherwise directed by the presiding judicial officer, all orders shall be submitted"
- **Evidence (2026-10-17):** fetch_doc: 220,561 chars; 'Rule 24. Preparation and Submission of Orders. Rule 24.01. Generally.' at offset 142,091. WebFetch not run.

## D. Administrative code

### `wv-csr-sos` — Code of State Rules (Secretary of State)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · West Virginia Secretary of State, Administrative Law Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** Every title-series with all versions (Active and Historical), filing history and PDF/Word files; older rules exist only as scanned image PDFs.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://apps.sos.wv.gov/adlaw/csr/rule.aspx?rule={title}-{series:02d}{suffix}`
  - Placeholders: rule key = title + '-' + series zero-padded to two digits + letter suffix (110-01H, 64-21, 78-03); the unpadded '110-1H' returns an empty table. The rule page lists versions (Date Effective, Active/Historical) linking ruleview.aspx?document={id}; ruleview lists the filings with readfile.aspx?DocId={id}&Format=PDF (also WORD). Neither id is derivable: follow the links.
  - Index: `https://apps.sos.wv.gov/adlaw/csr/`
  - Navigation: rule.aspx?rule={key} → 'Active' row → ruleview.aspx?document={id} → 'Final File' PDF → readfile.aspx?DocId={id}&Format=PDF
- **Automation:** WebFetch gated · shell ok · robots: apps.sos.wv.gov: User-agent * — Disallow /adlaw/executivejournal/senateconfirmation/, /email/, /Templates/, business readpdf paths; /adlaw/csr/ allowed
  - WebFetch of a typed rule.aspx URL: PROVENANCE_REQUIRED (not answered). A probe of the non-existent path /adlaw/register/ returned HTTP 403 and fetch_doc then refused that one address for the day; the real register path /adlaw/registers worked.
- **Currency:** rule page 'Date Effective' column and final-file PDF — observed: "110-01H 4/28/2026 … Active"
- **Official status:** Filing record of the Secretary of State (final-filed rule PDFs with the agency's notice of final filing); no statement that the online copy is official.
- **Hazard:** two-hop id-based navigation
- **Hazard:** older rules are scanned images with no text layer (110-15 active 1993 version: 249 pages, 248 characters)
- **Hazard:** series must be zero-padded in the lookup key
- **Probe:** W. Va. Code R. § 110-1H-1 → `https://apps.sos.wv.gov/adlaw/csr/readfile.aspx?DocId=58902&Format=PDF` — expect: "NOTICE OF FINAL FILING AND ADOPTION OF A LEGISLATIVE RULE"
- **Evidence (2026-10-17):** fetch_doc: rule.aspx?rule=110-01H → Active 4/28/2026 'Valuation of Timberland and Managed Timberland' → ruleview document=18270 → DocId=58902 PDF, 11 pp, 32,214 chars, 'TITLE-SERIES: 110-01H'. Second: rule=78-03 lists Active 6/28/2023 version. Scan-only example: DocId=20946 (110-15) 249 pp, 248 chars.
- **Notes:** Final-file PDFs begin with the agency's notice form; the rule text follows.

### `wv-csr-lii` — Cornell LII — West Virginia Code of State Rules

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All agencies/titles, per-section pages with quarterly version comparison.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-{title}-{series}-{section}`
  - Placeholders: series unpadded, letter suffix upper-case (110-1H-1, 110-15-1). Browse: /regulations/west-virginia/agency-{title}/title-{title}/series-{title}-{series:02d}{suffix}.
  - Index: `https://www.law.cornell.edu/regulations/west-virginia`
- **Automation:** WebFetch untested · shell ok · robots: www.law.cornell.edu: /regulations allowed (Crawl-delay 10 per earlier records)
  - WebFetch attempt hit the WebFetch proxy's HTTP 429 rate limit (not a site refusal) and was not retried.
- **Currency:** page Notes — observed: "State regulations are updated quarterly"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** can be badly stale: 110-1H-1 on LII shows Effective Date May 1, 1999, while the SOS active version is effective 4/28/2026 — always compare with wv-csr-sos
- **Probe:** W. Va. Code R. § 110-1H-1 → `https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-110-1H-1` — expect: "This legislative rule establishes the procedure for the classification and valuation of timberland"
- **Evidence (2026-10-17):** fetch_doc: 2,741 chars, Last-Modified 08 Aug 2025; '1.1. Scope. -- This legislative rule establishes the procedure for the classification'; '1.4. Effective Date. -- May 1, 1999'. Second: W-Va-C-S-R-SS-110-15-1 '1.1. Scope. -- These legislative regulations explain and clarify'.

## D. Administrative register

### `wv-register-sos` — West Virginia State Register (weekly)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · West Virginia Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Weekly issues 2003-2026 (year selector), e.g. Vol. XLIII (43) Issue 33, Aug. 21, 2026.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://apps.sos.wv.gov/adlaw/registers/readpdf.aspx?did={id}`
  - Placeholders: did is an internal id; take it from the listing row ('Friday, August 21, 2026 XLIII (43) 33 View').
  - Index: `https://apps.sos.wv.gov/adlaw/registers`
  - Navigation: registers listing (select year) → issue row → 'View' readpdf.aspx?did={id}
- **Automation:** WebFetch untested · shell unreadable-format · robots: allowed (see wv-csr-sos)
  - Issue PDF did=40275: 74 pages but only 73 characters of text — image-only scans. Listing page reads fine.
- **Currency:** listing rows — observed: "Friday, August 21, 2026 XLIII (43) 33"
- **Official status:** Official publication of the Secretary of State; no statement on the online copy.
- **Hazard:** image-only PDFs: no text to quote without OCR
- **Hazard:** id-based URLs
- **Probe:** W. Va. Reg. Vol. XLIII (2026) → `https://apps.sos.wv.gov/adlaw/registers/readpdf.aspx?did=40275`
- **Evidence (2026-10-17):** fetch_doc: listing 200 (5,345 chars, years 2003-2026); issue PDF did=40275 application/pdf 74 pp, 73 chars extracted (scanned).
- **Notes:** Use the register only to find filing dates; quote rule text from wv-csr-sos final-file PDFs.

## E. Case law

### `wv-ica-opinions` — Intermediate Court of Appeals — opinions and memorandum decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Intermediate Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** July 2022-2026; 1,398 decisions in the archive (single page, 633K characters, unfiltered).
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.courtswv.gov/appellate-courts/intermediate-court-of-appeals/opinions/prior-terms?combine={party}&field_ica_opinion_year_value={YYYY}&field_decision_type_value={SO|MD|SEP}&field_case_type_value={type}`
  - Placeholders: Plain GET; NOTE the ICA filter names differ from the Supreme Court's (field_ica_opinion_year_value, field_decision_type_value, field_case_type_value) — the SCA names are silently ignored and return all 1,398 rows. combine=Battista → 2 rows. PDF file names vary (22-ICA-208 Opinion.pdf, 22-ICA-74_so.pdf, 25-ICA-78_MD.pdf): take from the row.
  - Index: `https://www.courtswv.gov/appellate-courts/intermediate-court-of-appeals/opinions/prior-terms`
  - Navigation: GET prior-terms with filters → row → pubfilesmnt PDF
- **Automation:** WebFetch untested · shell ok · robots: see wv-sca-opinions
  - Unfiltered archive page is 633K characters — always filter. ICA order/decision list PDFs from search results read fine in WebFetch.
- **Currency:** listing (newest first) — observed: "08/27/2026 25-ICA-422"
- **Official status:** Slip opinions; reported opinions appear in S.E.2d (not free).
- **Hazard:** unfiltered archive page is enormous
- **Hazard:** filter parameter names differ from the SCA page
- **Hazard:** slip pagination only
- **Probe:** Ford Motor Co. v. Tyler, No. 22-ICA-208 (W. Va. Ct. App. Dec. 8, 2023) → `https://www.courtswv.gov/sites/default/pubfilesmnt/2023-12/22-ICA-208%20Opinion.pdf` — expect: "REVERSED AND REMANDED"
- **Evidence (2026-10-17):** fetch_doc: GET prior-terms?field_ica_opinion_year_value=2023&field_decision_type_value=SO → 30 rows incl. 22-ICA-208 → PDF 29 pp, 49,514 chars, 'No. 22-ICA-208 … REVERSED AND REMANDED … Filed: December 8, 2023'.

### `wv-sca-opinions` — Supreme Court of Appeals — opinions and memorandum decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 1991-2026 in the archive (year filter starts 1991; 1,797 listing pages); signed opinions (SO), per curiam, memorandum decisions (MD), separate opinions (SEP), orders. Current term on /opinions.
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions/prior-terms?combine={party_or_term}&field_sca_opinion_year_value={YYYY}&field_case_type_sca_value={type}&field_decision_type_sca_value={SO|MD|Per Curiam|SEP|Order}`
  - Placeholders: Plain GET (verified 2026-10-17): every parameter optional; 'combine' is a free-text match on case name (combine=Morrison → 7 rows; combine=Gasvoda → 2). Searching an ICA docket (combine=25-ICA-78) finds nothing, and docket searches are unreliable — search the party name. Year values 1991-2026 or All. Rows give date filed, docket, case name, case type, decision type and the PDF link. PDF URLs are https://www.courtswv.gov/sites/default/pubfilesmnt/{YYYY-MM}/{file}.pdf where YYYY-MM is the upload month (older opinions were re-uploaded 2023-11/12) and the file name varies (22-765-bunn-p.pdf, 25-884 Memorandum Decision.pdf, 32783.pdf) — never construct it; take it from the row.
  - Index: `https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions/prior-terms`
  - Navigation: GET prior-terms with filters → row → pubfilesmnt PDF (current term: /appellate-courts/supreme-court-of-appeals/opinions)
- **Automation:** WebFetch gated · shell ok · robots: www.courtswv.gov: /search/ and /search? disallowed (site search — not used); opinion listings and /sites/default/pubfilesmnt/ allowed
  - WebFetch read a search-sourced listing page (prior-terms?page=1387: rows and filter form present) but opinion PDFs taken from page links were PROVENANCE_REQUIRED (2 tries); a search-sourced pubfilesmnt PDF read fine. fetch_doc reads PDFs in full.
- **Currency:** listing (newest first) — observed: "10/14/2026 25-835 In re M.M. JUV MD"
- **Official status:** Slip opinions with slip pagination; the official reporter is West Virginia Reports (with S.E.2d parallels), not online.
- **Hazard:** slip pagination only; no W. Va. / S.E.2d page numbers
- **Hazard:** PDF file names and month folders not derivable
- **Hazard:** docket search unreliable — use party names
- **Hazard:** separate opinions are separate PDFs
- **Probe:** Monongalia Cnty. Comm'n v. Stewart, No. 22-765 (W. Va. Nov. 14, 2024) → `https://www.courtswv.gov/sites/default/pubfilesmnt/2024-11/22-765-bunn-p.pdf` — expect: "AFFIRMED IN PART, REVERSED IN PART, AND REMANDED"
- **Evidence (2026-10-17):** fetch_doc: GET prior-terms?field_sca_opinion_year_value=2024&field_case_type_sca_value=CIV-O → row 22-765 SO → PDF 46 pp, 82,086 chars; caption 'September 2024 Term … No. 22-765'; no reporter cite. Second: 25-884 memorandum decision (2 pp) '(ICA No. 25-ICA-78)'.
- **Notes:** Decision-type codes: SO signed opinion, MD memorandum decision, SEP separate opinion, Per Curiam, Order.

### `wv-cases-justia` — Justia — West Virginia Supreme Court of Appeals and Intermediate Court of Appeals

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court of Appeals (year listings) and Intermediate Court of Appeals 2022-; ranges not fully checked.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/west-virginia/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court | intermediate-court-of-appeals. docket-slug = docket lower-cased (22-765, 22-ica-243). When a docket has several documents the slugs get suffixes and the bare slug may be a SEPARATE opinion: 22-765.html = Armstead separate opinion, 22-765-0.html = the signed opinion. Some listing entries have no link (22-ICA-208). Always confirm on the year listing https://law.justia.com/cases/west-virginia/{court-slug}/{year}/.
  - Index: `https://law.justia.com/cases/west-virginia/`
  - Navigation: year listing → entry link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copies of slip opinions; no reporter pagination.
- **Hazard:** bare docket slug can be a separate opinion, not the majority
- **Hazard:** some entries unlinked
- **Hazard:** shell blocked
- **Probe:** Folse v. Rollyson, No. 22-ICA-243 (W. Va. Ct. App. Nov. 16, 2023) → `https://law.justia.com/cases/west-virginia/intermediate-court-of-appeals/2023/22-ica-243.html` — expect: "SCARR, Judge: Petitioner, Mr. Jay Folse, appeals the October 13,"
- **Evidence (2026-10-17):** WebFetch: 22-ica-243 YES 'SCARR, Judge: Petitioner, Mr. Jay Folse, appeals the October 13,', complete. SCA 2024 listing: 22-765-0.html = signed opinion, 22-765.html = separate opinion (fetched: separate only). /2023/22-ica-208.html → fetch error (entry unlinked).

## F. Subsequent history

### `wv-order-lists` — Supreme Court and ICA order lists (dispositions by order)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals / Intermediate Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Periodic PDF lists of dispositions (affirmed, vacated, writs refused, with vote counts) — SCA order lists back to at least 2020; ICA 'Order and Decision List' monthly.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: File names are free-form (OrderListJune262025.pdf, 'Order List - 2-20-2024.pdf', '2024-11-4 Order and Decision List.pdf'); take them from the index page.
  - Index: `https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/order-lists`
  - Navigation: SCA order-lists page (or /appellate-courts/intermediate-court-of-appeals/order-lists) → dated PDF → search the docket or party
- **Automation:** WebFetch ok · shell ok · robots: see wv-sca-opinions
  - Short PDFs (3 pp); index lists ~10 recent PDFs per page.
- **Currency:** list date in file name and header — observed: "06/26/2025"
- **Official status:** Court-issued lists of actions; no statement.
- **Hazard:** free-form file names
- **Hazard:** only summaries, not reasons
- **Probe:** SCA order list June 26, 2025 → `https://www.courtswv.gov/sites/default/pubfilesmnt/2025-06/OrderListJune262025.pdf` — expect: "No. 24-120 (Ohio CC-35-2022-C-26) Affirmed (5-0)"
- **Evidence (2026-10-17):** fetch_doc: 3 pp, 4,496 chars, entries like 'No. 24-120 (Ohio CC-35-2022-C-26) Affirmed (5-0)'. WebFetch (search-sourced ICA '2024-11-4 Order and Decision List.pdf'): ICA list dated November 4, 2024, first entry No. 23-ICA-351 'Reversed and Remanded'.

### `wv-subsequent-history-sca` — Supreme Court of Appeals review of ICA decisions (opinion archive)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Appeals of West Virginia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Since 2022 most civil, workers' compensation and family appeals go first to the ICA; a party may then petition the Supreme Court of Appeals, whose decision (often a memorandum decision) cites the ICA docket in its caption ('(ICA No. 25-ICA-78)'). Circuit-court criminal, abuse-and-neglect and other appeals go straight to the Supreme Court. Only further review: US Supreme Court certiorari.
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions/prior-terms?combine={party}`
  - Placeholders: Party-name search only: combine={ICA docket} returns 'No Entries Found.' even when the SCA decision's caption cites that docket. Search a distinctive party name (combine=Gasvoda → 25-884 MD (2026) and 23-143 md (2024)), then confirm '(ICA No. …)' in the PDF caption. Parties may be reversed on appeal.
  - Index: `https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions/prior-terms`
  - Navigation: GET prior-terms?combine={party} → candidate rows → PDF caption shows '(ICA No. YY-ICA-N)'
- **Automation:** WebFetch gated · shell ok · robots: see wv-sca-opinions
- **Currency:** none
- **Official status:** Slip decisions.
- **Hazard:** party-name search only
- **Hazard:** petitions refused without a written decision may not appear in the opinion archive — check the order lists (wv-order-lists)
- **Probe:** Murray Am. Energy, Inc. v. Gasvoda, No. 25-ICA-78 (W. Va. Ct. App. 2025) → No. 25-884 (W. Va. 2026) → `https://www.courtswv.gov/sites/default/pubfilesmnt/2026-06/25-884%20Memorandum%20Decision.pdf` — expect: "No. 25-884 (JCN: 2019025668) (ICA No. 25-ICA-78)"
- **Evidence (2026-10-17):** fetch_doc: SCA combine=Gasvoda → 25-884 MD; PDF 2 pp '(ICA No. 25-ICA-78)'. ICA combine=Gasvoda → 25-ICA-78_MD.pdf (2025-10). SCA combine=25-ICA-78 → 'No Entries Found.'

## Not available (do not look for these again)

- **statutes** — public.law edition of the West Virginia Code: fetch_doc grep of https://www.public.law/ for 'West Virginia': 0 matches. (2026-10-17)
- **statutes** — Cornell LII West Virginia Code / Constitution / opinions: https://www.law.cornell.edu/states/west_virginia links out to courtswv.gov and apps.sos.wv.gov; LII hosts only the Code of State Rules. (2026-10-17)
- **statutes** — Official bulk XML/JSON/API for the West Virginia Code: None linked from code.wvlegislature.gov or the Legislature home page; only the per-chapter PDF generator (/pdf/{chapter}/) and the section index /wvcodeentire.htm. (2026-10-17)
- **case_law** — Free official reporter pagination (West Virginia Reports / S.E.2d): Court PDFs carry slip pagination and no reporter cite (22-765, 22-ICA-208). (2026-10-17)
- **case_law** — courtswv.gov Supreme Court opinions before 1991: Archive year filter offers 1991-2026 only. (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: R. App. P. 21(e) prescribes the docket form 'No. 11-098 (W.Va. Supreme Court, January 15, 2011) (memorandum decision)'; no neutral cite exists. (2026-10-17)

## Corpus candidates (maintainers)

- `wv-constitution-code` — 277K chars; WebFetch stops in Art. VII § 14
- `wv-rules-civil` — 269K chars; WebFetch stops in Rule 23(f)(2)
- `wv-rules-appellate` — 181K chars; Rule 21 at ~103K
- `wv-rules-criminal` — 149K chars; Rule 35 at ~111K
- `wv-rules-trial-court` — 221K chars
- `wv-rules-professional-conduct` — 386K chars with comments
- `wv-rules-evidence` — 101K chars — at the edge of the WebFetch window
- `wv-code-chapter-pdf` — whole-chapter PDFs (ch. 55 = 436 pp) are the only bulk form of the Code · bulk: https://code.wvlegislature.gov/pdf/{chapter}/

## Open questions

- WebFetch hit the proxy's HTTP 429 rate limit after ~17 calls; WebFetch not run on wv-code-chapter-pdf, wv-acts, wv-constitution-home, wv-csr-lii, wv-ica-opinions, wv-register-sos or most court-rule pages (script route verified instead).
- Opinion PDFs taken from courtswv.gov page links were PROVENANCE_REQUIRED in WebFetch; whether they pass once approved is untested.
- Other court rule sets (Family Court, Magistrate Court civil/criminal, child abuse and neglect, juvenile, post-conviction habeas, administrative appeals, judicial discipline) are linked from the court rules index but not probed.
- CourtListener ids 'wva' and 'wvactapp' unverified.
- Whether West Virginia has enacted UELMA and designated an authenticated online Code was not established; no statement found on code.wvlegislature.gov.
- code.wvlegislature.gov/robots.txt could not be read directly (connection reset); fetch_doc's check reported it permits the paths used.

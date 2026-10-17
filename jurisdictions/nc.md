# North Carolina (NC) — free legal sources

_Generated from `data/nc.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution, Rules of Civil Procedure (G.S. 1A-1) and Rules of Evidence (G.S. 8C-1): ncleg.gov per-section and per-rule URLs are constructible from the citation and readable by WebFetch and fetch_doc.py; the site says the text is 'Not Official'. Appellate, General Practice and Business Court rules are single codified PDFs on nccourts.gov, which refuses the script (CloudFront 403); WebFetch reads the rules pages. Case law: appellate.nccourts.org year listings, headnote search and docket sheets work by plain GET, but robots.txt disallows the opinion PDFs under /opinions/, so text comes from Justia (tier 2) and official page numbers from the nccourts.gov N.C./N.C. App. volume PDFs. PDR dispositions are on Supreme Court docket sheets and order PDFs. The NCAC is http-only at reports.oah.state.nc.us (the script's https robots check fails); LII mirrors it but lags.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of North Carolina | `nc (unverified)` | N.C. | N.C., S.E.2d, S.E., S.E.3d | 2021-NCSC-1 (parallel cite, opinions filed 2021-2022 only; withdrawn Jan. 2023) |
| North Carolina Court of Appeals | `ncctapp (unverified)` | N.C. Ct. App. | N.C. App., S.E.2d, S.E.3d | 2021-NCCOA-1 (parallel cite, opinions filed 2021-2022 only; withdrawn Jan. 2023) |
| North Carolina Business Court (Superior Court) | `ncsuperct (unverified)` | N.C. Super. Ct. | NCBC | 2019 NCBC 12 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| N.C. Rules of Civil Procedure (G.S. 1A-1) | `N.C. R. Civ. P. 12(b)(6)`; `N.C.R. Civ. P. 56(c)`; `N.C.G.S. § 1A-1, Rule 12(b)(6)`; `N.C. Gen. Stat. § 1A-1, Rule 4(j1)`; `G.S. 1A-1, Rule 60(b)`; `Rule 12(b)(6) of the North Carolina Rules of Civil Procedure` | `nc-rules-civil-ncleg` |
| N.C. Rules of Evidence (G.S. 8C-1) | `N.C. R. Evid. 702(a)`; `N.C.R. Evid. 403`; `N.C.G.S. § 8C-1, Rule 803(6)`; `G.S. 8C-1, Rule 404(b)`; `Rule 702 of the North Carolina Rules of Evidence` | `nc-rules-evidence-ncleg` |
| North Carolina General Statutes | `N.C. Gen. Stat. § 1-52`; `N.C.G.S. § 1-52`; `G.S. 1-52`; `N.C. Gen. Stat. § 75-1.1`; `N.C.G.S. § 143B-135.40`; `G.S. 160D-102`; `N.C. Gen. Stat. Ann. § 15A-1415(b)`; `section 1-52 of the General Statutes`; `Section 75-1.1 of the North Carolina General Statutes`; `N.C.G.S. §§ 7B-903, -906.1` | `nc-gs-ncleg` → `nc-gs-justia` |
| North Carolina Session Laws | `S.L. 2023-134`; `N.C. Sess. Law 2026-30`; `Session Law 2019-245`; `2019 N.C. Sess. Laws 245` | `nc-session-laws-ncleg` |
| North Carolina Constitution | `N.C. Const. art. I, § 18`; `N.C. Const. art. IV, § 12(1)`; `Article I, Section 19 of the North Carolina Constitution`; `Article IV, Section 12 of the N.C. Constitution` | `nc-constitution-ncleg` → `nc-constitution-justia` |
| N.C. Rules of Appellate Procedure | `N.C. R. App. P. 28(b)(6)`; `N.C.R. App. P. 10(a)(1)`; `N.C. R. App. P. 30(e)(3)`; `Rule 2 of the North Carolina Rules of Appellate Procedure` | `nc-rules-appellate` |
| General Rules of Practice for the Superior and District Courts | `Gen. R. Pract. Super. & Dist. Ct. 2`; `N.C. Super. & Dist. Ct. R. 7`; `Rule 2 of the General Rules of Practice for the Superior and District Courts` | `nc-rules-general-practice` |
| North Carolina Business Court Rules | `N.C. Bus. Ct. R. 7.1`; `BCR 10.9`; `Business Court Rule 7.1` | `nc-rules-business-court` |
| North Carolina Administrative Code | `15A NCAC 02B .0202`; `10A NCAC 13F .0102`; `15A N.C. Admin. Code 2B.0202`; `21 N.C.A.C. 46.1801` | `nc-ncac-oah` → `nc-ncac-lii` |
| North Carolina Register | `41:08 NCR 652`; `40 N.C. Reg. 1234`; `41:08 N.C.R. 700` | `nc-register-oah` |
| Reported N.C. cases (N.C., N.C. App., S.E.2d) | `In re J.N.J., 286 N.C. App. 599 (2022)`; `State v. Smith, 375 N.C. 152 (2020)`; `123 S.E.2d 456 (N.C. 1962)`; `870 S.E.2d 123 (N.C. Ct. App. 2022)` | `nc-cases-justia` → `nc-opinions-appellate-listing` → `nc-reports-volumes` |
| N.C. universal citations 2021-2022 (NCSC / NCCOA) | `2021-NCSC-57`; `State v. Smith, 375 N.C. 152, 2020-NCSC-45, ¶ 16`; `2022-NCCOA-118, ¶ 23` | `nc-opinions-appellate-listing` → `nc-cases-justia` |
| Business Court public-domain citations | `2019 NCBC 12`; `Lucas v. Hopper, 2026 NCBC 39` | `nc-business-court-opinions` |
| Appellate docket numbers and unpublished COA opinions | `No. 353PA23`; `98A24`; `No. COA22-433`; `State v. Doe, No. COA23-1013, slip op. at 4 (N.C. Ct. App. Dec. 31, 2024) (unpublished)` | `nc-opinions-appellate-listing` → `nc-subsequent-history-dockets` → `nc-cases-justia` |
| Business Court Westlaw / Lexis cites | `2023 WL 4567890 (N.C. Super. Ct. May 1, 2023)`; `2019 NCBC LEXIS 12` | `nc-business-court-opinions` |
| Westlaw / Lexis unreported cites | `2023 WL 123456 (N.C. Ct. App. Jan. 3, 2023)`; `2024 N.C. App. LEXIS 12` | `nc-cases-justia` → `nc-opinions-appellate-listing` |

Regexes (case-insensitive):

- N.C. Rules of Civil Procedure (G.S. 1A-1): `N\.\s*C\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|(?:N\.\s*C\.\s*Gen\.\s*Stat\.|N\.C\.G\.S\.|\bG\.S\.)\s*(?:§\s*)?1A-1,?\s*Rule\s*(?P<rule2>\d+(?:\.\d+)?)|Rule\s+(?P<rule3>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:North\s+Carolina|N\.C\.)\s+Rules\s+of\s+Civil\s+Procedure`
- N.C. Rules of Evidence (G.S. 8C-1): `N\.\s*C\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|(?:N\.\s*C\.\s*Gen\.\s*Stat\.|N\.C\.G\.S\.|\bG\.S\.)\s*(?:§\s*)?8C-1,?\s*Rule\s*(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:North\s+Carolina|N\.C\.)\s+Rules\s+of\s+Evidence`
- North Carolina General Statutes: `(?:N\.\s*C\.\s*Gen\.\s*Stat\.(?:\s*Ann\.)?|N\.C\.G\.S\.|\bG\.S\.)\s*(?:§§?\s*)?(?P<chapter>\d{1,3}[A-Z]{0,2})-(?P<section>\d+(?:\.\d+)*[A-Za-z]?)|(?:sec(?:tion|\.)|§)\s*(?P<chapter2>\d{1,3}[A-Z]{0,2})-(?P<section2>\d+(?:\.\d+)*[A-Za-z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+(?:North\s+Carolina\s+)?General\s+Statutes`
- North Carolina Session Laws: `(?:S\.L\.|Session\s+Law|N\.C\.\s*Sess\.\s*Law)\s*(?P<year>(?:19|20)\d\d)-(?P<number>\d+)|(?P<year2>(?:19|20)\d\d)\s+N\.C\.\s*Sess\.\s*Laws\s*(?:ch\.\s*)?(?P<number2>\d+)`
- North Carolina Constitution: `N\.\s*C\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+)\s+of\s+the\s+(?:North\s+Carolina|N\.C\.)\s+Constitution`
- N.C. Rules of Appellate Procedure: `N\.\s*C\.\s*R\.\s*App\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:North\s+Carolina|N\.C\.)\s+Rules\s+of\s+Appellate\s+Procedure`
- General Rules of Practice for the Superior and District Courts: `Gen\.\s*R\.\s*Pract\.\s*Super\.\s*(?:&|and)\s*Dist\.\s*Ct\.\s*(?P<rule>\d+(?:\.\d+)?)|N\.\s*C\.\s*Super\.\s*(?:&|and)\s*Dist\.\s*Ct\.\s*R\.\s*(?P<rule2>\d+(?:\.\d+)?)|Rule\s+(?P<rule3>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+General\s+Rules\s+of\s+Practice\s+for\s+the\s+Superior\s+(?:and|&)\s+District\s+Courts`
- North Carolina Business Court Rules: `N\.\s*C\.\s*Bus\.\s*Ct\.\s*R\.\s*(?P<rule>\d+(?:\.\d+)?)|\bBCR\s*(?P<rule2>\d+(?:\.\d+)?)|Business\s+Court\s+Rule\s+(?P<rule3>\d+(?:\.\d+)?)`
- North Carolina Administrative Code: `(?P<title>\d{1,2}[A-Z]?)\s+(?:NCAC|N\.\s*C\.\s*A\.\s*C\.|N\.\s*C\.\s*Admin\.\s*Code)\s*(?P<chapter>\d{1,2})(?P<subchapter>[A-Z]{1,2})?\s*\.(?P<rule>\d{4})`
- North Carolina Register: `(?P<volume>\d{1,2})(?::(?P<issue>\d{1,2}))?\s+(?:NCR|N\.C\.R\.|N\.C\.\s*Reg\.)\s*(?P<page>\d+)`
- Reported N.C. cases (N.C., N.C. App., S.E.2d): `(?P<volume>\d{1,3})\s+N\.\s*C\.(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4})|(?P<sevol>\d{1,3})\s+S\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<sepage>\d{1,4})(?:,\s*\d+)?\s*\((?P<court>N\.C\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- N.C. universal citations 2021-2022 (NCSC / NCCOA): `(?P<year>(?:19|20)\d\d)-(?P<court>NCSC|NCCOA)-(?P<number>\d+)`
- Business Court public-domain citations: `(?P<year>(?:19|20)\d\d)\s+NCBC\s+(?P<number>\d+)`
- Appellate docket numbers and unpublished COA opinions: `(?:No\.\s*)?(?<!§\s)(?<!§)\b(?P<sc>\d{1,4}(?:PA|AP|A|P)\d{2}(?:-\d)?)\b|(?:No\.\s*)?\bCOA\s?(?P<coa>\d{2}-\d{1,4})`
- Business Court Westlaw / Lexis cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(N\.C\.\s*Super\.|NCBC\s*LEXIS\s+(?P<lexis>\d+))`
- Westlaw / Lexis unreported cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(N\.C\.(?!\s*Super)|N\.C\.(?:\s*App\.)?\s*LEXIS\s+(?P<lexis>\d+))`

Short forms → URL key:

N.C. R. Civ. P. → `1A-1`; N.C.R. Civ. P. → `1A-1`; Rules of Civil Procedure → `1A-1`; N.C. R. Evid. → `8C-1`; N.C.R. Evid. → `8C-1`; Rules of Evidence → `8C-1`; N.C. Gen. Stat. → `GS`; N.C.G.S. → `GS`; G.S. → `GS`; N.C. Gen. Stat. Ann. → `GS`; Juvenile Code → `7B`; Criminal Procedure Act → `15A`; UDTPA → `75`; Unfair and Deceptive Trade Practices Act → `75`; Business Corporation Act → `55`; Workers' Compensation Act → `97`

Order matters: try the 1A-1 and 8C-1 rule patterns before the General Statutes pattern, because 'N.C.G.S. § 1A-1, Rule 12' also matches the statute regex as § 1A-1 (a stub page). The statute URL needs no code key: chapter and section come straight from 'G.S. {chapter}-{section}'; law_aliases maps rule-set and act names to their chapter. 'G.S.' is guarded by requiring the dotted form 'G.S.'; bare 'Rule 12', 'Rules of Civil Procedure' or 'Rules of Evidence' route here only with 'North Carolina'/'N.C.' or 1A-1/8C-1 context. 'S.L. YYYY-N' is also used by other states (e.g. Idaho), so route session laws here only with N.C. context. NC sections are always chapter-hyphen-section, so '§§ 1-52 to 1-56' is a span: take the first; '§§ 7B-903, -906.1' gives 7B-903 then 7B-906.1. Official reporters N.C. and N.C. App. are free as whole-volume PDFs on nccourts.gov (nc-reports-volumes); S.E.2d/S.E.3d are West. Universal citations ('2021-NCSC-1', '2021-NCCOA-1', ¶ pinpoints) were a parallel cite for opinions filed from Jan. 1, 2021; the Supreme Court withdrew the order on Jan. 11, 2023. Business Court 'YYYY NCBC N' is a court-assigned public-domain cite. Unpublished COA opinions (N.C. R. App. P. 30(e)) are cited by docket 'No. COA##-###' plus date and '(unpublished)'. Supreme docket suffixes: A (appeal of right), PA (PDR allowed), P (petition), -2 for a second matter. 'disc. review denied, ___ N.C. ___' is found on the Supreme Court docket sheet (nc-subsequent-history-dockets). CourtListener ids from memory, unverified (Business Court opinions may sit under ncsuperct). Westlaw cites with a '(N.C. Super. Ct.' parenthetical (and NCBC LEXIS) are Business Court decisions: they route to nc-business-court-opinions; the general WL pattern excludes them with a negative lookahead (?!\s*Super). Reported-case text routes to Justia first, because the official volume PDFs have not been read.

## A. Statutes / code

### `nc-gs-ncleg` — North Carolina General Statutes (ncleg.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina General Assembly · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All chapters of the General Statutes, per section (HTML, PDF, RTF), per article and per chapter.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_{chapter}/GS_{chapter}-{section}.html`
  - Placeholders: Citation G.S. {chapter}-{section}: chapter = everything before the hyphen, with its letter suffix kept (1, 1A, 14, 15A, 75, 143B, 160D); section = everything after the hyphen, decimals verbatim (75-1.1 → GS_75-1.1, 143B-135.40 → GS_143B-135.40). No zero-padding. Path case does not matter (search engines index lower-case copies). Same path with /PDF/ and .pdf, or /RTF/ and .rtf. Whole chapter: /EnactedLegislation/Statutes/HTML/ByChapter/Chapter_{chapter}.html (and /PDF/ByChapter/Chapter_{chapter}.pdf); whole article: /HTML/ByArticle/Chapter_{chapter}/Article_{article}.html. The Rules of Civil Procedure (G.S. 1A-1) and Rules of Evidence (G.S. 8C-1) are single sections whose rules sit in separate files: GS_1A-1,_Rule_{rule}.html and GS_8C-1,_Rule_{rule}.html (see nc-rules-civil-ncleg, nc-rules-evidence-ncleg). Section listing per chapter: https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter{chapter} (links only, no ranges needed since the URL is direct).
  - Index: `https://www.ncleg.gov/Laws/GeneralStatutesTOC`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow /WHPTest/, /Ethics/; Crawl-delay: 2
  - Per-section pages are small (G.S. 1-52: 5,444 chars). Chapter-level files are long: Chapter_1A.html is 301,629 chars of HTML (WebFetch reports 131,823 chars of text and stops inside Rule 20; Rule 56(c) NOT PRESENT). Use the per-section/per-rule file, or fetch_doc.py on the chapter file. WebFetch on ncleg.gov URLs only worked for URLs that a web search had returned (provenance gate in this harness).
- **Currency:** https://www.ncleg.gov/Laws/GeneralStatutes page body (not on section pages) — observed: "The General Statutes include changes through S.L. 2026-30."
- **Official status:** https://www.ncleg.gov/Laws/GeneralStatutes has a heading 'Not Official': the General Assembly is not responsible for errors or omissions; editor's notes are only in print or LexisNexis.
- **Hazard:** no currency line on section pages; check the General Statutes landing page
- **Hazard:** GS_1A-1.html and GS_8C-1.html are stubs with only the lead-in sentence; rule text is in the ',_Rule_N' files
- **Hazard:** chapter files exceed the WebFetch window (Chapter 1A stops at Rule 20)
- **Hazard:** recodified or repealed sections return a short notice page, not text (G.S. 116-209.52 → 'Recodified as G.S. § 127A-192')
- **Hazard:** editor's notes referenced as '(see note)' are not online
- **Probe:** N.C. Gen. Stat. § 1-52 → `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1/GS_1-52.html` — expect: "Within three years an action"
- **Evidence (2026-10-16):** WebFetch (ncleg.gov/... GS_1-52.html): body present, 'Within three years an action (1) Upon a contract', complete through (20). G.S. 14-17: '(a) A murder which shall be perpetrated by means of a', complete. Script: GS_1-52 5,444 chars, last-modified 16 Apr 2026; GS_15A-1415, GS_160D-102, GS_75-1.1, GS_143B-135.40 all 200 with text; PDF GS_1-52.pdf 2 pp. | Independent check 2026-10-16: Script: GS_1-52 5,444 chars, 'Within three years an action' found; landing 'changes through S.L. 2026-30.'; second citation N.C. Gen. Stat. § 20-138.1; G.S. 7B-1111 ok
- **Notes:** Two different chapters with letter suffixes and decimal sections prove the pattern (1-52, 14-17, 15A-1415, 160D-102, 75-1.1, 143B-135.40). library.ncleg.gov, house.ncleg.gov, ncleg.net and ftp.ncleg.gov serve the same paths (seen in search results); cite www.ncleg.gov.

### `nc-session-laws-ncleg` — North Carolina Session Laws (ncleg.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina General Assembly · text: **fetch-and-quote** · official: unknown
- **Coverage:** Session laws by biennium, HTML and PDF.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/{biennium}/SL{year}-{number}.html`
  - Placeholders: S.L. {year}-{number}. biennium = 'Y-(Y+1)' when year is odd, '(Y-1)-Y' when even (2023 → 2023-2024; 2026 → 2025-2026). number unpadded. PDF: /SessionLaws/PDF/{biennium}/SL{year}-{number}.pdf. The form 'SessionLaw2023-134.html' 404s.
  - Index: `https://www.ncleg.gov/Laws/SessionLaws`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * — Disallow /WHPTest/, /Ethics/; Crawl-delay: 2
  - Budget acts are huge (S.L. 2023-134 HTML: 2,386,462 chars) — use fetch_doc.py grep/section.
- **Currency:** none stated
- **Official status:** No statement on the session-law pages; the site-wide 'Not Official' notice covers the statutes.
- **Hazard:** very long budget acts
- **Hazard:** SessionLaw{Y}-{N} file names 404; use SL{Y}-{N}
- **Probe:** S.L. 2023-134 → `https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2023-2024/SL2023-134.html` — expect: "SESSION LAW 2023-134 HOUSE BILL 259"
- **Evidence (2026-10-16):** Script: 200 html, grep 'SESSION LAW 2023-134 HOUSE BILL 259' found; SL2026-30.pdf 2 pp. WebFetch not run. | Independent check 2026-10-16: Script: SL2023-134.html 2,386,462 chars, 'SESSION LAW 2023-134 HOUSE BILL 259' found.; second citation S.L. 2025-2 ok

### `nc-gs-justia` — Justia — North Carolina General Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** General Statutes editions 2010-2025; the unversioned URL serves 2025. G.S. 1A-1 has no rule text (only the lead-in sentence).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/north-carolina/chapter-{chapter_lower}/article-{article_lower}/section-{chapter_lower}-{section}/`
  - Placeholders: chapter and suffix lower-case (chapter-1, chapter-1a); the article number is NOT in the citation and must come from the chapter page, which shows no section ranges. A chapter without articles omits the article segment (chapter-1a/section-1a-1/). Year editions: insert /{year}/ after /north-carolina/. Decimal points in the section become hyphens in the slug (75-1.1 → section-75-1-1, verified chapter-75/article-1/section-75-1-1/); always take the section link from the article page.
  - Index: `https://law.justia.com/codes/north-carolina/`
  - Navigation: chapter page (/codes/north-carolina/chapter-{n}/) → article link (titles only, no ranges; pick by subject or try the article page) → article page lists sections → section page. Verified: chapter-1 → article-5 → section-1-52.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt answers 403 Cloudflare 'Just a moment...'
  - fetch_doc.py: REFUSED (robots.txt challenge). WebFetch only.
- **Currency:** page heading and Universal Citation line — observed: "NC Gen Stat § 1-52 (2025)"
- **Official status:** Page disclaimer that the codes may not be the most recent version.
- **Hazard:** article hop: article number not derivable and article links show no section ranges
- **Hazard:** no text for the Rules of Civil Procedure (1A-1) — page has only the lead-in
- **Hazard:** edition lags the official text
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** section slug replaces dots with hyphens (section-75-1-1); constructing section-75-1.1 misses
- **Probe:** N.C. Gen. Stat. § 1-52 → `https://law.justia.com/codes/north-carolina/chapter-1/article-5/section-1-52/` — expect: "Within three years an action"
- **Evidence (2026-10-16):** WebFetch: body present through (20), 'NC Gen Stat § 1-52 (2025)'. chapter-1a/section-1a-1: Rule 12(b) body NOT PRESENT; chapter-1a index lists only § 1A-1. | Independent check 2026-10-16: WebFetch: 'Within three years an action -' then '(1) Upon a contract'; 'NC Gen Stat § 1-52 (2025)'.; second citation N.C. Gen. Stat. § 75-1.1 ok

## B. Constitution

### `nc-constitution-ncleg` — North Carolina Constitution (ncleg.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina General Assembly · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1971 as amended; one page per article, plus a whole-text HTML and PDF.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ncleg.gov/Laws/Constitution/Article{article_arabic}`
  - Placeholders: article_arabic = the article's Roman numeral as an Arabic number (art. I → Article1, art. IV → Article4, art. XIV → Article14). Whole text: https://www.ncleg.gov/EnactedLegislation/Constitution/NCConstitution.html (116,397 chars) and .pdf (39 pp).
  - Index: `https://www.ncleg.gov/Laws/Constitution`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow /WHPTest/, /Ethics/; Crawl-delay: 2
  - Per-article pages fit in WebFetch (Article1: 23,082 chars, through Sec. 38). The whole-text HTML truncates in WebFetch at Article X, Sec. 2.
- **Currency:** no currency line; whole-text file carries editorial notes on pending amendments — observed: "contingent upon the results of the November 3, 2026, referendum"
- **Official status:** Same ncleg.gov site whose statutes landing page is headed 'Not Official'; no separate statement on the constitution pages.
- **Hazard:** whole-text HTML truncates in WebFetch (Art. X onward unreachable without offset)
- **Hazard:** editorial notes print contingent amendment text (S.L. 2026-4, 2026-5, 2024-58) pending the Nov. 3, 2026 vote — check which version is in force
- **Hazard:** whole-text HTML has stray encoding characters ('Sec. 18.�')
- **Probe:** N.C. Const. art. I, § 18 → `https://ncleg.gov/Laws/Constitution/Article1` — expect: "All courts shall be open; every person for an injury"
- **Evidence (2026-10-16):** WebFetch: Sec. 18 body present, last section Sec. 38, not truncated. Script: Article4 Sec. 12 '(1) Supreme Court. The Supreme Court shall have jurisdiction'; NCConstitution.html 116,397 chars, last-modified 10 Jun 2026. | Independent check 2026-10-16: Script: Article1 23,082 chars, 'All courts shall be open; every person for an injury' found.; second citation N.C. Const. art. IX, § 2 ok

### `nc-constitution-justia` — Justia — North Carolina Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble and Article I on preamble.html; other articles one page each.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/constitution/north-carolina/{page}`
  - Placeholders: Art. I → preamble.html#I; Arts. II-VI → article_{roman_lower}.html (article_iv.html); Arts. VII-XIV share one page → article_vii-xiv.html#{ROMAN} (art. IX → article_vii-xiv.html#IX, verified). Prefer taking the link from the index.
  - Index: `https://law.justia.com/constitution/north-carolina/`
  - Navigation: index → article link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare challenge)
- **Currency:** none stated — observed: "This Constitution may not be the most recent version."
- **Official status:** Page says the Constitution may not be the most recent version and points to the official state site.
- **Hazard:** stale: Article I ends at Sec. 37; the official text has Sec. 38
- **Hazard:** shell blocked
- **Hazard:** Articles VII-XIV share article_vii-xiv.html; article_ix.html does not exist
- **Probe:** N.C. Const. art. I, § 18 → `https://law.justia.com/constitution/north-carolina/preamble.html` — expect: "All courts shall be open; every person for an injury"
- **Evidence (2026-10-16):** WebFetch: Sec. 18 body present; Article I ends at Sec. 37 (official ends at Sec. 38) — stale copy. | Independent check 2026-10-16: WebFetch: Sec. 18 present; Article I ends Sec. 37; 'This Constitution may not be the most recent version.'; second citation N.C. Const. art. IX, § 2 ok
- **Notes:** Last resort only.

## C. Court rules

### `nc-rules-appellate` — N.C. Rules of Appellate Procedure (codified PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of North Carolina (Office of Administrative Counsel) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole rule set in one PDF; amendment orders listed separately on the same page.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nccourts.gov/assets/inline-files/North%20Carolina%20Rules%20of%20Appellate%20Procedure%20-%20Codified%202%20September%202025_2.pdf?VersionId=…`
  - Placeholders: File name and VersionId change with each codification; always take the link from the rules page.
  - Index: `https://nccourts.gov/courts/supreme-court/court-rules/north-carolina-rules-of-appellate-procedure`
  - Navigation: rules page → 'Codified …' PDF link (no per-rule pages or anchors)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
  - Rules pages are WebFetch-readable; PDFs expected to exceed the WebFetch window (2023 appellate codification stopped in Rule 18). The script route is refused for www.nccourts.gov, so corpus ingestion by script is not possible either.
- **Currency:** rules page link text — observed: "Codified 2 September 2025"
- **Official status:** Rules page calls the PDF an up-to-date codification by the Supreme Court's Office of Administrative Counsel; the adopting orders are the authoritative text.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** file name/VersionId change on recodification
- **Hazard:** shell blocked (CloudFront 403)
- **Probe:** N.C. R. App. P. 28(b) → `https://nccourts.gov/courts/supreme-court/court-rules/north-carolina-rules-of-appellate-procedure`
- **Evidence (2026-10-16):** WebFetch of the rules page: no rule text, link to 'Codified 2 September 2025' PDF. Current PDF not fetched (provenance gate timed out). Older 1 March 2023 codification PDF: Rule 28(b) NOT PRESENT, WebFetch stops in Rule 18(c)(8). | Independent check 2026-10-16: Script REFUSED (nccourts.gov robots bot check). WebFetch rules page: link 'Codified 2 September 2025'; no rule text.; PDF not read (Codified PDF (link taken from the page) not readable here: WebFetch permission request timed out (harness provenance gate, not site refusal). Script route refused, so the rule text remains unverified; row stays link-only in practice.)

### `nc-rules-business-court` — North Carolina Business Court Rules (codified PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of North Carolina (Office of Administrative Counsel) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole rule set in one PDF; amendment orders listed separately on the same page.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nccourts.gov/assets/inline-files/Business%20Court%20Rules%20-%20Codified%202%20September%202025_0.pdf?VersionId=…`
  - Placeholders: File name and VersionId change with each codification; always take the link from the rules page.
  - Index: `https://www.nccourts.gov/courts/supreme-court/court-rules/north-carolina-business-court-rules`
  - Navigation: rules page → 'Codified …' PDF link (no per-rule pages or anchors)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
  - WebFetch reads the codified PDF through Rule 16 and stops inside Appendix 2. Script refused for www.nccourts.gov (robots bot check), so corpus ingest by script is not possible.
- **Currency:** rules page link text (not in the PDF; PDF history notes cite 'Order Dated 20 August 2025') — observed: "Codified 2 September 2025"
- **Official status:** Rules page calls the PDF an up-to-date codification by the Supreme Court's Office of Administrative Counsel; the adopting orders are the authoritative text.
- **Hazard:** WebFetch truncation inside Appendix 2 (rules 1-16 reachable)
- **Hazard:** PDF cover has no 'Codified' string — currency only from the rules-page link text
- **Hazard:** file name/VersionId change on recodification
- **Hazard:** shell blocked (CloudFront 403)
- **Probe:** N.C. Bus. Ct. R. 7.1 → `https://www.nccourts.gov/assets/inline-files/Business%20Court%20Rules%20-%20Codified%202%20September%202025_0.pdf?VersionId=YbShRXHN681b6gF9gPfkab60_wMQOxF4` — expect: "General provisions. (a) Business Court judge presides."
- **Evidence (2026-10-16):** WebFetch of rules page: link 'Codified 2 September 2025'; script REFUSED (nccourts.gov bot check). | Independent check 2026-10-16: WebFetch of the codified PDF read Rule 7.1 'General provisions. (a) Business Court judge presides.'; Rules 1-16 reachable, truncation inside Appendix 2; second citation N.C. Bus. Ct. R. 7.1 ok

### `nc-rules-civil-ncleg` — N.C. Rules of Civil Procedure (G.S. 1A-1) on ncleg.gov

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina General Assembly · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules 1-84 of G.S. 1A-1, one file per rule (incl. 44.1, 68.1).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1A/GS_1A-1,_Rule_{rule}.html`
  - Placeholders: rule = rule number verbatim incl. decimals (12, 44.1, 68.1); the comma and underscore are literal. PDF: /PDF/BySection/Chapter_1A/GS_1A-1,_Rule_{rule}.pdf. Whole set: /HTML/ByChapter/Chapter_1A.html.
  - Index: `https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter1A`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow /WHPTest/, /Ethics/; Crawl-delay: 2
  - WebFetch on the per-rule URL was not run (provenance gate timed out); WebFetch on Chapter_1A.html returned Rule 12(b) body but stops at Rule 20. Use the per-rule file.
- **Currency:** https://www.ncleg.gov/Laws/GeneralStatutes — observed: "The General Statutes include changes through S.L. 2026-30."
- **Official status:** Statutory rules published with the General Statutes ('Not Official' notice on https://www.ncleg.gov/Laws/GeneralStatutes).
- **Hazard:** GS_1A-1.html (no rule suffix) is a stub
- **Hazard:** whole-chapter file truncates in WebFetch at Rule 20
- **Probe:** N.C. R. Civ. P. 12(b)(6) → `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1A/GS_1A-1,_Rule_12.html` — expect: "(6) Failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-16):** Script: GS_1A-1,_Rule_12.html 7,210 chars, '(6) Failure to state a claim upon which relief can be granted' found. WebFetch Chapter_1A.html: Rule 12(b) 'Every defense, in law or fact, to a claim for'; Rule 56(c) NOT PRESENT (truncated at Rule 20). | Independent check 2026-10-16: Script: Rule_12 7,210 chars, '(6) Failure to state a claim upon which relief can be granted'.; second citation N.C. R. Civ. P. 56(c) ok
- **Notes:** Rule list from the Chapter1A section page: 1-65, 67-70, 83, 84, 44.1, 68.1.

### `nc-rules-evidence-ncleg` — N.C. Rules of Evidence (G.S. 8C-1) on ncleg.gov

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina General Assembly · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules 101-1102 of G.S. 8C-1, one file per rule.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_8C/GS_8C-1,_Rule_{rule}.html`
  - Placeholders: rule verbatim (401, 702, 803). GS_8C-1.html alone is a stub.
  - Index: `https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter8C`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * — Disallow /WHPTest/, /Ethics/; Crawl-delay: 2
  - Same host and layout as nc-rules-civil-ncleg.
- **Currency:** https://www.ncleg.gov/Laws/GeneralStatutes — observed: "The General Statutes include changes through S.L. 2026-30."
- **Official status:** Published with the General Statutes ('Not Official' notice).
- **Hazard:** GS_8C-1.html is a stub
- **Probe:** N.C. R. Evid. 702(a) → `https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_8C/GS_8C-1,_Rule_702.html` — expect: "(a) If scientific, technical or other specialized knowledge will assist"
- **Evidence (2026-10-16):** Script: 6,276 chars, 'Rule 702. Testimony by experts. (a) If scientific, technical' found. WebFetch not run. | Independent check 2026-10-16: Script: Rule_702 6,276 chars, '(a) If scientific, technical or other specialized knowledge will assist' found.; second citation N.C. R. Evid. 404(b) ok

### `nc-rules-general-practice` — General Rules of Practice for the Superior and District Courts (codified PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of North Carolina (Office of Administrative Counsel) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole rule set in one PDF; amendment orders listed separately on the same page.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nccourts.gov/assets/inline-files/General%20Rules%20of%20Practice%20for%20the%20Superior%20and%20District%20Courts%20-%20Administrative%20Counsel%20Codification%20-%206%20August%202025.pdf?VersionId=…`
  - Placeholders: File name and VersionId change with each codification; always take the link from the rules page.
  - Index: `https://nccourts.gov/courts/supreme-court/court-rules/general-rules-of-practice-for-superior-and-district-courts`
  - Navigation: rules page → 'Codified …' PDF link (no per-rule pages or anchors)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
  - Rules pages are WebFetch-readable; PDFs expected to exceed the WebFetch window (2023 appellate codification stopped in Rule 18). The script route is refused for www.nccourts.gov, so corpus ingestion by script is not possible either.
- **Currency:** rules page link text — observed: "Codified 6 August 2025"
- **Official status:** Rules page calls the PDF an up-to-date codification by the Supreme Court's Office of Administrative Counsel; the adopting orders are the authoritative text.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** file name/VersionId change on recodification
- **Hazard:** shell blocked (CloudFront 403)
- **Probe:** Gen. R. Pract. Super. & Dist. Ct. 2 → `https://nccourts.gov/courts/supreme-court/court-rules/general-rules-of-practice-for-superior-and-district-courts`
- **Evidence (2026-10-16):** WebFetch of the rules page: no rule text; link to the 6 August 2025 codification PDF. PDF not fetched. | Independent check 2026-10-16: Script REFUSED. WebFetch rules page: link 'Codified 6 August 2025'; no rule text.; PDF not read (PDF not read: WebFetch permission not answered (harness gate, not site refusal). Rule text unverified.)

## D. Administrative code

### `nc-ncac-oah` — North Carolina Administrative Code (OAH)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Office of Administrative Hearings, Rules Division · text: **link-only** · official: unknown
- **Coverage:** All NCAC titles; per rule HTML/PDF/DOC, plus per-subchapter and per-chapter compilations.
- **Access:** `index-anchored` · format html
  - Pattern: `http://reports.oah.state.nc.us/ncac/title {title_lower} - {title_name_lower}/chapter {chapter:02d} - {chapter_name_lower}/subchapter {sub_lower}/{title_lower} ncac {chapter:02d}{sub_lower} .{rule}.html`
  - Placeholders: All path segments lower-case, spaces URL-encoded as %20. Title and chapter folder names include descriptive names that are not in the citation (e.g. 'title 15a - environmental quality/chapter 02 - environmental management/subchapter b/15a ncac 02b .0202.html'), so take them from the index. Also .pdf and .doc; subchapter compilation '.../subchapter b/subchapter b rules.pdf'. Second verified: 10a ncac 13f .0101 under 'title 10a - health and human services/chapter 13 - nc medical care commission/subchapter f/'.
  - Index: `http://reports.oah.state.nc.us/ncac.asp`
  - Navigation: ncac.asp → ncac.asp?folderName=\Title {T} - {Name} → ?folderName=\Title …\Chapter {CC} - {Name} (lists every rule file in every subchapter) → rule .html/.pdf
  - Read via: No tool route reaches this host (script: https reset; WebFetch: approval gate). Read the text from nc-ncac-lii and disclose its lag; check the latest amendment date here by link.
- **Automation:** WebFetch untested · shell http-error · robots: http://…/robots.txt returns a 404 page; https:// connection reset
  - Host serves plain http only; https resets the connection, so fetch_doc.py fails its robots check ('robots.txt unreachable … Connection reset by peer'). Plain curl over http returned 200 for the index and rule files; chapter listings can take >30 s. WebFetch permission request for the http URL timed out (not a site refusal).
- **Currency:** OAH 'About the NCAC' page; rule History Note gives the latest amendment — observed: "OAH updates this website weekly."
- **Official status:** OAH 'About the NCAC' page: available at no charge on the OAH website, updated weekly; no official-status statement.
- **Hazard:** http only; https resets
- **Hazard:** folder names not derivable from the citation
- **Hazard:** Word-exported HTML (large CSS header before text)
- **Hazard:** slow chapter listings
- **Hazard:** no read route: fetch_doc.py fails (https connection reset) and WebFetch could not be approved — independent check 2026-10-16 failed by every route
- **Probe:** 15A NCAC 02B .0202 → `http://reports.oah.state.nc.us/ncac/title%2015a%20-%20environmental%20quality/chapter%2002%20-%20environmental%20management/subchapter%20b/15a%20ncac%2002b%20.0202.html` — expect: "The definition of any word or phrase used in this Section"
- **Evidence (2026-10-16):** curl over http: 200 text/html 32,770 bytes, '15A NCAC 02B .0202 DEFINITIONS'; History Note ends 'Amended Eff. June 1, 2026'. Neither fetch_doc.py (https reset) nor WebFetch (permission timeout) read it. | Independent check 2026-10-16 FAILED: script 'robots.txt unreachable … Connection reset by peer'; WebFetch permission timed out. Link-only.
- **Notes:** The only current official text; LII (nc-ncac-lii) lags by at least one amendment.

### `nc-ncac-lii` — Cornell LII — North Carolina Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All NCAC titles, per rule.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/north-carolina/{title}-N-C-Admin-Code-{chapter:02d}{subchapter}-{rule}`
  - Placeholders: title verbatim upper-case (15A, 10A); chapter two digits plus subchapter letter (02B, 13F); rule four digits WITHOUT the leading dot (0202). 15A NCAC 02B .0202 → 15A-N-C-Admin-Code-02B-0202. Browse: /regulations/north-carolina/title-15A/chapter-02/subchapter-B/section-.0200. When the citation has no subchapter letter, omit it (21 NCAC 46 .1801 → 21-N-C-Admin-Code-46-1801, verified).
  - Index: `https://www.law.cornell.edu/regulations/north-carolina`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10 (per DE record); /regulations allowed
  - A wrong slug (e.g. 15A-NCAC-02B-.0202) returns HTTP 200 with the North Carolina title index (2,569 chars, same sha256 for every bad slug), not a 404 — check that the rule number appears in the text.
- **Currency:** page Notes — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** stale: 15A NCAC 02B .0202 history ends 'Amended Eff. June 1, 2022' while OAH shows a June 1, 2026 amendment
- **Hazard:** bad slugs return the index with HTTP 200
- **Probe:** 15A NCAC 02B .0202 → `https://www.law.cornell.edu/regulations/north-carolina/15A-N-C-Admin-Code-02B-0202` — expect: ""Acute toxicity to aquatic life" means lethality or other harmful effects"
- **Evidence (2026-10-16):** Script: 25,259 chars, definition (1) found; history ends 'Amended Eff. June 1, 2022'. 10A-N-C-Admin-Code-13F-0102: 8,205 chars, 'Activities of daily living' found. | Independent check 2026-10-16: Script: definition (1) '"Acute toxicity to aquatic life" means lethality' found; history ends 6/1/2022.; second citation 21 NCAC 46 .1801 ok
- **Notes:** Practical second fetch only for rules not amended since LII's last refresh.

## D. Administrative register

### `nc-register-oah` — North Carolina Register

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Office of Administrative Hearings · text: **fetch-and-quote** · official: unknown
- **Coverage:** Twice-monthly issues; listing on oah.nc.gov, PDFs on files.nc.gov (Vol. 41 Issue 08, Oct. 15, 2026 is newest).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://files.nc.gov/oah/documents/{YYYY-MM}/Volume-{vol}-Issue-{issue:02d}-{Month}-{DD}-{YYYY}.pdf`
  - Placeholders: Not constructible: real hrefs carry ?VersionId=… and sometimes _0/_1 suffixes (Volume-40-Issue-07-October-1-2025_0.pdf); the folder is the upload month. Always copy the href from the listing. Register cites give volume:issue and page (41:08 NCR 652).
  - Index: `https://www.oah.nc.gov/documents/north-carolina-register`
  - Navigation: listing (newest first, ?page=N) → issue PDF on files.nc.gov
- **Automation:** WebFetch ok · shell ok · robots: files.nc.gov/robots.txt: S3 AccessDenied XML (treated as none); oah.nc.gov: Drupal default (core/profile assets)
  - Issue PDFs are long (Vol. 41 No. 08: 110 pp, 485,893 chars); WebFetch stops at Register p. 710 of 652-756.
- **Currency:** issue cover — observed: "VOLUME 41 ● ISSUE 08 ● Pages 652 – 756"
- **Official status:** Official OAH publication; no online-status statement seen.
- **Hazard:** WebFetch truncation within an issue
- **Hazard:** upload-month folder not equal to issue date
- **Hazard:** file names may carry _0/_1 suffixes and ?VersionId — follow links, don't construct
- **Probe:** 41:08 NCR 652 (Oct. 15, 2026) → `https://files.nc.gov/oah/documents/2026-10/Volume-41-Issue-08-October-15-2026.pdf` — expect: "NORTH CAROLINA REGISTER VOLUME 41 ● ISSUE 08 ● Pages 652 – 756"
- **Evidence (2026-10-16):** Script: 110 pp PDF, cover line found. WebFetch: cover 'VOLUME 41 ● ISSUE 08 ● Pages 652 – 756', truncated at p. 710. | Independent check 2026-10-16: Script: 110 pp, 'NORTH CAROLINA REGISTER VOLUME 41 ● ISSUE 08 ● Pages 652 – 756'.; second citation 41:07 NCR 541 ok

## E. Case law

### `nc-business-court-opinions` — North Carolina Business Court opinions (nccourts.gov)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · North Carolina Business Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Business Court opinions with NCBC citations (2026 NCBC 1-39 seen); listing newest first.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nccourts.gov/assets/documents/opinions/{YYYY}%20NCBC%20{N}.pdf?VersionId=…`
  - Placeholders: PDF file name is the NCBC citation with spaces ('2026 NCBC 39.pdf'); VersionId taken from the listing or detail page (whether the bare URL works is untested). Detail page slug: /documents/business-court-opinions/{caption-slug}-{yyyy}-ncbc-{n}.
  - Index: `https://www.nccourts.gov/documents/business-court-opinions`
  - Navigation: listing (?page=N; shows citation, date, docket e.g. 24-CVS-502, county, judge) → PDF link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
  - Listing and detail pages: WebFetch ok. Opinion PDFs not fetched (provenance gate timed out).
- **Currency:** none
- **Official status:** Court-published opinions with public-domain citation 'YYYY NCBC N'; no official-status statement.
- **Hazard:** PDF text not verified
- **Hazard:** shell blocked
- **Hazard:** filters not exposed as GET params
- **Probe:** Lucas v. Hopper, 2026 NCBC 39 → `https://nccourts.gov/documents/business-court-opinions?page=2` — expect: "LUCAS v. HOPPER, 2026 NCBC 39"
- **Evidence (2026-10-16):** WebFetch listing: 'LUCAS v. HOPPER, 2026 NCBC 39', April 23, 2026, 24-CVS-502, PDF '2026%20NCBC%2039.pdf'. Detail page (2026 NCBC 1): metadata only, no body. PDF body not read. | Independent check 2026-10-16: Script REFUSED. WebFetch listing: 'LUCAS v. HOPPER, 2026 NCBC 39', April 23, 2026, 24-CVS-502.; PDF not read (Opinion PDF not read: WebFetch permission not answered (harness gate). Body text still unverified.)
- **Notes:** Business Court appeals go directly to the Supreme Court (G.S. 7A-27(a)(2)), so look for the appeal in Supreme Court dockets.

### `nc-opinions-appellate-listing` — N.C. Supreme Court and Court of Appeals opinion filings (appellate.nccourts.org)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina Judicial Branch (Administrative Office of the Courts) · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals, 1998-2026 (year selector 1998-2026); COA unpublished opinions listed separately per filing date.
- **Access:** `constructible` · format html
  - Pattern: `https://appellate.nccourts.org/opinion-filings/?c={sc|coa}&year={YYYY}`
  - Placeholders: Year listing grouped by filing date; each row gives case name, docket (Supreme '353PA23', '98A24'; COA '24-417') and Published/Unpublished, with the PDF as viewOpinion('…/opinions/?c={1|2}&pdf={id}') — c=1 Supreme, c=2 COA. Headnote search by plain GET: https://appellate.nccourts.org/opinion-filings/index-search.php?court={1|2}&sSearchTerm={words}; results show the official cite (e.g. '286 N.C. App. 599 (2022)'). Per-date zip of published opinions: getopzip.php?c={1|2}&d={base64 of YYYY-MM-DD}.
  - Index: `https://appellate.nccourts.org/opinion-filings/?c=sc`
  - Navigation: year listing → row (name, docket) → pdf id → PDF (robots-disallowed; see nc-opinions-appellate-pdf)
  - Read via: PDF text is under /opinions/, which robots.txt disallows: read the opinion on nc-cases-justia; cite page numbers from nc-reports-volumes
- **Automation:** WebFetch untested · shell ok · robots: appellate.nccourts.org: User-agent * — Disallow: /opinions/ (every opinion PDF path); listings, dockets.php, orders.php, getopzip.php allowed
  - WebFetch permission request timed out (harness provenance, not a site refusal). ?c=1 without 'sc' returns the page shell without rows; use c=sc / c=coa. COA year page is ~580 KB.
- **Currency:** none; listing updated per filing date
- **Official status:** Slip opinions; official pagination is in the North Carolina Reports / N.C. App. Reports volumes (nc-reports-volumes).
- **Hazard:** opinion PDFs robots-disallowed
- **Hazard:** slip pagination only
- **Hazard:** pdf id not derivable — take it from the listing or docket sheet
- **Probe:** Cato Corp. v. Zurich Am. Ins. Co., No. 353PA23 (N.C. Dec. 13, 2024) → `https://appellate.nccourts.org/opinion-filings/?c=sc&year=2024` — expect: "Cato Corp. v. Zurich Am. Ins. Co.,  (353PA23 - Published)"
- **Evidence (2026-10-16):** curl/script: 2024 Supreme listing has 'Cato Corp. v. Zurich Am. Ins. Co., (353PA23 - Published)', pdf=44232; COA 2024 listing shows '(24-417 - Unpublished)'; index-search GET 'Cato' returned 25 headnote results with N.C. App. cites. | Independent check 2026-10-16: Script: 2024 listing 'Cato Corp. v. Zurich Am. Ins. Co., (353PA23 - Published)'.; second citation Sneed v. Johnston, No. 130PA24 (N.C. Aug. 14, 2026) ok
- **Notes:** Docket sheets (nc-subsequent-history-dockets) also link the slip opinion.

### `nc-opinions-appellate-pdf` — Slip-opinion PDFs (appellate.nccourts.org/opinions/)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · North Carolina Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals slip opinions 1998-.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://appellate.nccourts.org/opinions/?c={1|2}&pdf={id}`
  - Placeholders: id from the listing or docket sheet.
  - Index: `https://appellate.nccourts.org/opinion-filings/?c=sc`
  - Navigation: listing → pdf id
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent * — Disallow: /opinions/
  - fetch_doc.py: REFUSED 'robots.txt on appellate.nccourts.org disallows /opinions/?c=1&pdf=43543'. Not fetched by any route. getopzip.php (robots-allowed) serves per-date zips of the same PDFs; not used for reading here.
- **Currency:** n/a
- **Official status:** Slip opinions.
- **Hazard:** robots disallow
- **Probe:** pdf=43543 → `https://appellate.nccourts.org/opinions/?c=1&pdf=43543`
- **Evidence (2026-10-16):** robots.txt 'User-agent: * Disallow: /opinions/'; fetch_doc.py REFUSED. | Re-confirmed blocked 2026-10-16: fetch_doc check REFUSED 'Disallow: /opinions/'; WebFetch permission timed out (not a site answer).
- **Notes:** Link to it in reports; read the text elsewhere.

### `nc-opinions-nccourts-gov` — Appellate Court Opinions listing (nccourts.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court and COA opinions, paginated newest first (page 200 ≈ Dec. 2022); each item has a detail page and a PDF link to appellate.nccourts.org/opinions/.
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format html
  - Pattern: `https://www.nccourts.gov/documents/appellate-court-opinions?page={n}`
  - Placeholders: Only ?page=N is visible; filter parameter names (Contains, Author, Filed after/before, Court Type, Opinion Type) not exposed in links. Detail pages: /documents/appellate-court-opinions/{slug}.
  - Index: `https://www.nccourts.gov/documents/appellate-court-opinions`
  - Read via: PDF links point to appellate.nccourts.org/opinions/ (robots-disallowed)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
- **Currency:** none
- **Official status:** Metadata listing of slip opinions.
- **Hazard:** no plain-GET filter found
- **Hazard:** shell blocked
- **Hazard:** ?page=N offsets shift as opinions are added; the page-200 probe date will drift
- **Probe:** Kozec v. Murphy, COA22-433 (N.C. Ct. App. Dec. 29, 2022) → `https://www.nccourts.gov/documents/appellate-court-opinions?page=200` — expect: "Kozec v. Murphy"
- **Evidence (2026-10-16):** WebFetch: page 200 items dated December 29, 2022 (Kozec v. Murphy, COA22-433) with PDF links ?c=2&pdf=41876. | Independent check 2026-10-16: WebFetch page 200: 'Kozec v. Murphy', December 29, 2022, COA22-433, pdf=41876.
- **Notes:** Prefer nc-opinions-appellate-listing (year pages, GET headnote search).

### `nc-reports-volumes` — North Carolina Reports and N.C. Court of Appeals Reports — PDF volumes (nccourts.gov)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · North Carolina Judicial Branch (Reporter of Decisions) · text: **fetch-and-quote** · official: official
- **Coverage:** Bound-volume PDFs; seen: Supreme Court vols. 361-366 and 386; COA vols. 283-293 (full range not enumerated).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nccourts.gov/assets/documents/pdf-volumes/{ncsct|nccoa}{volume}.pdf?VersionId=…`
  - Placeholders: Supreme Court file ncsct{vol}.pdf, COA nccoa{vol}.pdf (ncsct366.pdf, nccoa292.pdf seen). Detail pages are named by volume and date span (e.g. /documents/pdf-volumes/coa-volume-292-02-january-2024-to-05-march-2024), so find the volume on the listing.
  - Index: `https://www.nccourts.gov/documents/pdf-volumes`
  - Navigation: listing (?page=N) → volume detail page → PDF link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nccourts.gov: robots.txt answers HTTP 403 (CloudFront 'Request blocked') — script refuses as bot check
  - Listing and detail pages read by WebFetch; the volume PDFs (2.4-4.8 MB) were not fetched (provenance gate timed out). Expect WebFetch truncation within a volume.
- **Currency:** volume title (date span) — observed: "Volume 366 - 14 June 2012 to 13 June 2013"
- **Official status:** N.C. Reports and N.C. App. Reports are the official reporters; the universal-citation fact sheet says the book-and-page citation remains the official cite.
- **Hazard:** whole-volume PDFs far exceed the WebFetch window
- **Hazard:** volume published long after the opinion
- **Hazard:** shell blocked
- **Probe:** 292 N.C. App. → `https://nccourts.gov/documents/pdf-volumes/coa-volume-292-02-january-2024-to-05-march-2024`
- **Evidence (2026-10-16):** WebFetch: detail page links nccoa292.pdf (2,390 KB, tag 'Court of Appeals'); vol. 366 page links ncsct366.pdf (4,806 KB, 'Supreme Court'). PDFs not read. | Independent check 2026-10-16: Script REFUSED. WebFetch detail page: links nccoa292.pdf, 2,390 KB, title 'COA Volume 292'.; PDF not read (Volume PDF not read: WebFetch permission not answered (harness gate). Whether official page numbers are reachable is still untested, yet the citation map routes reported cases here first.)
- **Notes:** The only free source of official N.C./N.C. App. page numbers. Until a volume PDF is read, use volumes as links only; route case text to nc-cases-justia.

### `nc-cases-justia` — Justia — North Carolina case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals by year (ranges not enumerated).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/north-carolina/{supreme-court|court-of-appeals}/{year}/{docket_slug}.html`
  - Placeholders: year = decision year. Supreme docket lower-case, no spaces (353PA23 → 353pa23; 142A23 → 142a23); COA docket without 'COA' (COA23-1013 → 23-1013). A second decision on one docket gets -2, -3 (20-665-2, 225pa21-2): if the first slug is the wrong decision, check the year listing.
  - Index: `https://law.justia.com/cases/north-carolina/`
  - Navigation: year listing lists every decision
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare challenge)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions; no reporter cites.
- **Hazard:** slip pagination only (page markers -2-, -3-)
- **Hazard:** published/unpublished not labelled
- **Hazard:** docket suffix variants
- **Hazard:** shell blocked
- **Probe:** Cato Corp. v. Zurich Am. Ins. Co., No. 353PA23 (N.C. 2024) → `https://law.justia.com/cases/north-carolina/supreme-court/2024/353pa23.html` — expect: "This is a companion case to North State Deli, LLC"
- **Evidence (2026-10-16):** WebFetch: body present, slip pages -2- to -15-, ends 'MODIFIED AND AFFIRMED.', no N.C./S.E.2d cite. COA: /court-of-appeals/2024/23-1013.html body present, 'This matter concerns a dispute between a church in Wilmington'. | Independent check 2026-10-16: WebFetch: 'This is a companion case to North State Deli, LLC'; -2- to -15-; not truncated.; second citation Sneed v. Johnston, No. 130PA24 (N.C. Aug. 14, 2026) ok
- **Notes:** Practical read route for opinion text, since the official PDFs are robots-disallowed. The body cites other cases by N.C./N.C. App. cites; only the opinion's own reporter cite is missing.

## F. Subsequent history

### `nc-subsequent-history-dockets` — N.C. Supreme Court docket sheets and orders (PDR dispositions)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · North Carolina Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court dockets (PDRs, appeals of right, Business Court appeals) with rulings and dates, lower-court numbers, and order PDFs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://appellate.nccourts.org/dockets.php?court=1&docket={docket}&title={party}&party=&name=&submit=Search`
  - Placeholders: Plain GET. court=1 Supreme, court=2 COA. docket = Supreme docket (353PA23) or COA docket (23-305); title = substring of the caption. Result rows link to the sheet https://appellate.nccourts.org/dockets.php?court=1&docket={internal e.g. 1-2023-0353-001}&pdf=1&a=0&dev=1, which lists each motion/PDR with ruling and date ('(1) PDR … Allowed 05-21-2024'), the COA and trial-court numbers, opinion date and decision ('Modified and Affirmed'). Orders: https://appellate.nccourts.org/orders.php?court=1&docket={docket}&title=&submit=Search → order PDFs at orders.php?t=PA&court=1&id={id}&pdf=1&a=0&docket=1&dev=1.
  - Index: `https://appellate.nccourts.org/dockets.php?c=1`
- **Automation:** WebFetch untested · shell ok · robots: appellate.nccourts.org: User-agent * — Disallow: /opinions/ (every opinion PDF path); listings, dockets.php, orders.php, getopzip.php allowed
  - dockets.php and orders.php are robots-allowed and return text via fetch_doc.py; the slip-opinion link on the sheet is under /opinions/ (blocked).
- **Currency:** docket search page — observed: "All docket sheets are current"
- **Official status:** Clerk's docket data and signed orders; the PDR order PDF is the certified order.
- **Hazard:** from a COA decision you cannot search the Supreme Court by COA number (court=1&docket=23-305 → 0 cases) and the COA docket sheet does not mention the PDR: search Supreme Court dockets by party/title
- **Hazard:** title search is a substring match and returns unrelated cases (Builders → 5 cases)
- **Hazard:** Supreme docket suffix letters: A = appeal of right, PA = PDR allowed, P = petition
- **Probe:** Cato Corp. v. Zurich Am. Ins. Co., COA 23-305 → No. 353PA23 → `https://appellate.nccourts.org/orders.php?t=PA&court=1&id=428065&pdf=1&a=0&docket=1&dev=1` — expect: "Allowed by order of the Court in conference, this the 21st of May 2024."
- **Evidence (2026-10-16):** Script: docket GET 353PA23 → 1 case; sheet shows 'PDR … Allowed 05-21-2024', COA 23-305, 21CVS9525; orders GET → 7 orders; order 428065 PDF 1 p, 'From N.C. Court of Appeals ( 23-305 )'. | Independent check 2026-10-16: Script: order 428065 PDF, 'Allowed by order of the Court in conference, this the 21st of May 2024.'; second citation Sneed v. Johnston, No. 130PA24 ok
- **Notes:** 'disc. review denied' / 'disc. review allowed' parentheticals map to the PDR row of the Supreme Court docket sheet and the order PDF.

## Not available (do not look for these again)

- **statutes** — public.law edition of the N.C. General Statutes: north-carolina.public.law and northcarolina.public.law: proxy CONNECT 502; DE record found public.law covers only CA, CO, FL, NV, NY, OR, TX. (2026-10-16)
- **court_rules** — Justia text of the N.C. Rules of Civil Procedure: law.justia.com/codes/north-carolina/chapter-1a/section-1a-1/ shows only the lead-in sentence; chapter-1a lists only § 1A-1. (2026-10-16)
- **statutes** — Official bulk download / API of the General Statutes: None found on ncleg.gov/Laws/GeneralStatutes; per-chapter HTML/PDF files are the closest substitute. (2026-10-16)
- **case_law** — Script- or WebFetch-readable official slip-opinion text: appellate.nccourts.org robots.txt 'Disallow: /opinions/'; nccourts.gov refuses the script (CloudFront 403). (2026-10-16)

## Corpus candidates (maintainers)

- `nc-rules-appellate` — Whole rule set in one PDF; WebFetch stopped in Rule 18 (2023 codification). Script ingestion blocked by nccourts.gov CloudFront 403 — needs another capture route.
- `nc-rules-general-practice` — Single codified PDF (6 Aug 2025); same block for the script.
- `nc-rules-business-court` — Single codified PDF (2 Sept 2025); WebFetch reads Rules 1-16 and stops inside Appendix 2. Script ingest blocked by nccourts.gov CloudFront 403.
- `nc-constitution-ncleg` — Whole-text HTML (116K chars) truncates in WebFetch at Art. X; per-article pages are the read route, PDF suits ingest (39 pp).
- `nc-rules-civil-ncleg` — 87-page chapter PDF (352,069 chars); WebFetch of the HTML stops at Rule 20. Per-rule files exist, so ingest is optional.
- `nc-register-oah` — Issue PDFs ~110 pp; WebFetch stops at p. 710 of 652-756.

## Open questions

- WebFetch provenance gate: in this run WebFetch only fetched URLs returned by a web search (or listed by a page it had fetched on the same host path); requests for appellate.nccourts.org listings, nccourts.gov asset PDFs (rules, NCBC opinions, report volumes) and reports.oah.state.nc.us timed out awaiting permission. These are harness limits, not site refusals — re-probe.
- Current codified Appellate, General Practice and Business Court Rules PDFs not read; truncation point unknown.
- Business Court opinion PDFs: body text and whether the bare URL (no VersionId) resolves are untested.
- N.C. Reports / N.C. App. volume PDFs: coverage range and whether WebFetch reaches a given page not tested.
- NCAC: whether WebFetch can read the http-only reports.oah.state.nc.us; fetch_doc.py would need an http robots check.
- CourtListener ids nc, ncctapp, ncsuperct unverified; Business Court mapping uncertain.
- Exact last filing date carrying 2022-NCCOA/NCSC universal cites not confirmed (withdrawal order dated Jan. 11, 2023).
- NCAC (nc-ncac-oah) failed by every tool route in the independent check (script https reset; WebFetch approval timeout): find a readable route or keep link-only with LII as the read route.
- Appellate Rules, General Rules of Practice, NCBC opinion PDFs and report-volume PDFs: WebFetch approval timed out in both research and independent check (harness gate, not a refusal) — re-probe and record truncation points.
- Business Court Rules PDF: WebFetch truncates inside Appendix 2 — corpus candidate, but the script is refused on nccourts.gov.

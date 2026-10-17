# South Dakota (SD) — free legal sources

_Generated from `data/sd.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, codified court rules (SDCL 15-6, 15-26A, 19-19, Title 23A) and ARSD rules are constructible per section from the LRC's server-rendered API pages (sdlegislature.gov/api/Statutes/{section}.html, /api/Rules/Rule/{rule}.html); the human /Statutes/ URLs are a JavaScript shell. The constitution is per-section on the same host but the script extracts 0 characters, so WebFetch plus Justia carry it. Supreme Court opinions (2006–, public-domain 'YYYY S.D. N' with ¶ pinpoints) are found by a GET party-name search on ujs.sd.gov and read as PDFs by fetch_doc.py (WebFetch is gated on them); Justia covers older years. Further review is SCOTUS certiorari only, findable by party name.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of South Dakota | `sd (unverified)` | S.D. | N.W.3d, N.W.2d, N.W., S.D. | 2026 S.D. 48 (from Jan. 1, 1996; pinpoint by ¶) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| South Dakota Codified Laws | `SDCL 22-18-1`; `SDCL § 53-1-1`; `S.D. Codified Laws § 32-23-1`; `SDCL ch. 22-18`; `SDCL 2-16-13.1`; `section 22-18-1 of the South Dakota Codified Laws`; `SDCL §§ 22-18-1 to -1.1`; `S.D.C.L. § 32-23-1` | `sd-sdcl-lrc` → `sd-sdcl-justia` |
| South Dakota Session Laws | `2021 S.D. Sess. Laws ch. 92`; `2021 S.D. Laws ch. 92` | `sd-session-laws-lrc` |
| South Dakota Session Laws (bare SL source-note form) *(only once this jurisdiction is known)* | `SL 2021, ch 92`; `SL 1996, ch 312` | `sd-session-laws-lrc` |
| South Dakota Constitution | `S.D. Const. art. VI, § 2`; `S.D. Const. art. V, § 1`; `Article VI, § 2 of the South Dakota Constitution`; `Article V, Section 1 of the South Dakota Constitution` | `sd-constitution-lrc` → `sd-constitution-justia` |
| SDCL-codified court rules (civil, appellate, evidence, criminal procedure) | `SDCL 15-6-56(c)`; `SDCL 15-6-12(b)(5)`; `SDCL 19-19-702`; `SDCL 15-26A-60`; `SDCL 23A-8-3` | `sd-rules-sdcl` → `sd-sdcl-justia` |
| South Dakota Rules of Professional Conduct | `Rule 1.7 of the South Dakota Rules of Professional Conduct`; `SDCL ch. 16-18 App., Rule 1.7`; `S.D. Rules of Prof'l Conduct R. 8.4` | `sd-rules-professional-conduct` |
| Administrative Rules of South Dakota | `ARSD 67:16:01:01`; `S.D. Admin. R. 74:51:01:01`; `ARSD 20:10:01:01.01`; `A.R.S.D. 20:10:01` | `sd-arsd-lrc` → `sd-arsd-lii` |
| South Dakota Register | `44 SDR 94`; `42 SDR 51, effective 10/13/2015` | `sd-register-lrc` |
| South Dakota public-domain citation (1996-) | `State v. Lucero, 2026 S.D. 48`; `Bialota v. Lakota Lakes, LLC, 2026 S.D. 52, ¶ 14`; `Kraft v. Meade Co., 2006 SD 113`; `Kuper v. Lincoln-Union Elec. Co., 1996 SD 145, 557 N.W.2d 748`; `State v. Fierro, 2014 S.D. 62, 853 N.W.2d 235` | `sd-opinions-ujs` → `sd-cases-justia` |
| North Western Reporter with (S.D. YYYY) | `Pickering v. Pickering, 434 N.W.2d 758 (S.D. 1989)`; `Wilson v. Great N. Ry. Co., 83 S.D. 207, 157 N.W.2d 19 (1968)` | `sd-cases-justia` → `sd-opinions-ujs` |
| North Western Reporter (generic, no court parenthetical) *(only once this jurisdiction is known)* | `557 N.W.2d 748`; `853 N.W.2d 235` | `sd-cases-justia` |
| South Dakota Reports (official reporter to 1976) | `83 S.D. 207` | `sd-cases-justia` |
| South Dakota Supreme Court docket number *(only once this jurisdiction is known)* | `#31307-a-SPM`; `No. 31286`; `#25626` | `sd-opinions-ujs` → `sd-cases-justia` |

Regexes (case-insensitive):

- South Dakota Codified Laws: `(?:\bSDCL|\bS\.\s?D\.\s?C\.\s?L\.|\bS\.\s?D\.\s*Codified\s+Laws(?:\s+Ann\.)?)\s*(?:§§?\s*|ch(?:apter|\.)\s*)?(?P<section>\d{1,2}[A-Z]?-\d{1,3}[A-Z]?(?:-(?:\d+(?:\.\d+)*|A))?)(?![\d.]*\d)(?P<sub>\([a-z]\))?|(?:section|§)\s*(?P<section2>\d{1,2}[A-Z]?-\d{1,3}[A-Z]?-\d+(?:\.\d+)*)(?:\([a-z0-9]+\))*\s+of\s+(?:the\s+)?South\s+Dakota\s+Codified\s+Laws`
- South Dakota Session Laws: `(?P<year>(?:18|19|20)\d\d)\s+S\.\s?D\.\s*(?:Sess\.\s*)?Laws,?\s*ch\.?\s*(?P<chapter>\d+)`
- South Dakota Session Laws (bare SL source-note form): `\bSL\s+(?P<year>(?:18|19|20)\d\d),\s*ch\.?\s*(?P<chapter>\d+)`
- South Dakota Constitution: `S\.\s?D\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+),?\s+(?:Section|§)\s*(?P<section2>\d+)\s+of\s+the\s+South\s+Dakota\s+Constitution`
- SDCL-codified court rules (civil, appellate, evidence, criminal procedure): `\bSDCL\s*(?:§§?\s*)?(?P<section>(?:15-6|15-26A|19-19|16-3|23A-\d{1,2}[A-Z]?)-\d+(?:\.\d+)*)(?P<sub>\([a-z]\))?`
- South Dakota Rules of Professional Conduct: `Rule\s+(?P<rule>\d\.\d+)(?:\([a-z0-9]+\))*\s+of\s+the\s+South\s+Dakota\s+Rules\s+of\s+Professional\s+Conduct|SDCL\s*(?:ch\.\s*)?16-18,?\s*App(?:endix|\.)?,?\s*(?:Rule|R\.)\s*(?P<rule2>\d\.\d+)|S\.\s?D\.\s*Rules\s+of\s+Prof(?:'l|essional)\s+Conduct\s*(?:R\.|Rule)\s*(?P<rule3>\d\.\d+)`
- Administrative Rules of South Dakota: `(?:\bARSD|\bA\.\s?R\.\s?S\.\s?D\.|S\.\s?D\.\s*Admin\.\s*R\.)\s*(?:§\s*)?(?P<rule>\d{1,2}:\d{1,2}(?::\d{1,2}(?::\d{1,2}(?:\.\d+)?)?)?)`
- South Dakota Register: `(?P<volume>\d{1,2})\s+SDR\s+(?P<page>\d+)`
- South Dakota public-domain citation (1996-): `(?<!\d)(?P<year>199[6-9]|20\d\d)\s+S\.?\s?D\.?\s+(?P<number>\d{1,3})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- North Western Reporter with (S.D. YYYY): `(?P<volume>\d{1,4})\s+N\.\s?W\.(?:\s?(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\(S\.\s?D\.\s*(?P<year>\d{4})\)|(?P<sdvol>\d{1,2})\s+S\.\s?D\.\s+(?P<sdpage>\d{1,4}),\s*(?P<nwvol>\d{1,4})\s+N\.\s?W\.`
- North Western Reporter (generic, no court parenthetical): `(?P<volume>\d{1,4})\s+N\.\s?W\.(?:\s?(?P<series>[23])d)?\s+(?P<page>\d{1,5})`
- South Dakota Reports (official reporter to 1976): `(?<![\d.])(?P<volume>\d{1,2})\s+S\.\s?D\.\s+(?P<page>\d{1,4})(?!\d)`
- South Dakota Supreme Court docket number: `(?:#|No\.\s*)(?P<docket>\d{5})(?:-[a-z]-[A-Z]{2,4})?(?!\d)`

Short forms → URL key:

SDCL → `SDCL`; S.D.C.L. → `SDCL`; S.D. Codified Laws → `SDCL`; S.D. Codified Laws Ann. → `SDCL`; ARSD → `ARSD`; A.R.S.D. → `ARSD`; S.D. Admin. R. → `ARSD`; SDR → `SDR`; SL → `SessionLaws`; S.D. Sess. Laws → `SessionLaws`

SDCL 15-26A-69.1: opinions released on or after Jan. 1, 1996 are cited 'YYYY S.D. N' with pinpoints to clerk-assigned ¶ numbers; earlier opinions by S.D. Reports (ended 1976, vol. 90 per memory) or N.W./N.W.2d. Court style and practitioners write both 'S.D.' and 'SD' ('2006 SD 113' appears in UJS listing titles). SDCL numbers are title-chapter-section with letters allowed (15-26A, 23A) and decimals (2-16-13.1); a '§§ 22-18-1 to -1.1' range is a span — take the first section. Court rules are codified: civil procedure = SDCL 15-6 (rule subsections are separate sections, e.g. 15-6-56(c)), evidence = 19-19 (FRE numbers), appellate = 15-26A, criminal = Title 23A (federal rule number only in the catchline). Bare 'Rule 56(c)' or 'Rule 702' is generic: route only with South Dakota context, then map to 15-6-56(c) / 19-19-702. Routing guards: 'S.D.' is also the Southern District abbreviation in federal cites ('S.D.N.Y.', 'S.D. Ohio'); the public-domain regex requires a 1996+ year directly before 'S.D.' and a number after, and the N.W. pattern requires '(S.D. YYYY)' or a parallel S.D. Reports cite, so federal district parentheticals do not route here. Bare N.W.2d cites, 'SL YYYY, ch N' and 5-digit docket numbers are context_required (N.W. also covers IA, MI, MN, NE, ND, WI). ARSD numbers use colons (67:16:01:01) and route only with an ARSD / S.D. Admin. R. prefix; register cites are 'NN SDR NNN'. CourtListener id 'sd' is from memory and unverified.

## A. Statutes / code

### `sd-sdcl-lrc` — South Dakota Codified Laws (LRC per-section HTML API)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council (Code Commission) · text: **fetch-and-quote** · official: unknown
- **Coverage:** All titles of the SDCL, including the court rules codified in it (15-6 civil procedure, 15-26A appellate, 19-19 evidence, Title 23A criminal procedure) and chapter appendices (e.g. 16-18-A Rules of Professional Conduct). Section pages carry the 'Source:' history note.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://sdlegislature.gov/api/Statutes/{section}.html`
  - Placeholders: {section} is the SDCL number exactly as cited, hyphens kept, no padding: 22-18-1, 53-1-1, 32-23-1, 19-19-702, 15-26A-60, 23A-8-3, 2-16-13.1. Chapter keys (22-18) and title keys (22) return the chapter's or title's table of contents; append ?all=true to a chapter key to get every section's text on one page (22-18.html?all=true = 21,832 chars). Rule subsections that are separate SDCL sections keep their parenthetical: 15-6-56(c), 15-6-12(b) (literal parentheses in the URL). The bare parent 15-6-56.html returns HTTP 200 with 0 characters: if a page comes back empty, re-try with the citation's first parenthetical letter, never guess further. Constitution sections are NOT served here (see sd-constitution-lrc). The human-facing https://sdlegislature.gov/Statutes/{section} is a Vue app: both fetch routes get only 'Your browser is not supported'. JSON variant: https://sdlegislature.gov/api/Statutes/Statute/{section} (Html field plus Previous/Next/parents).
  - Index: `https://sdlegislature.gov/api/Statutes/{title}.html`
  - Navigation: Only if a section key fails: title page /api/Statutes/22.html (chapter list, no section ranges) → chapter page /api/Statutes/22-18.html lists every section number and catchline with links of the form https://sdlegislature.gov/Statutes?Statute=22-18-1 → take the number and use the url_pattern.
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - The /api/Statutes/{section}.html pages are plain server-rendered HTML (no JS). WebFetch on the built URL /api/Statutes/53-1-1.html went through without an approval prompt. Sitemaps https://sdlegislature.gov/Statutes.1.xml and .2.xml (2.6M chars) list every section URL with a lastmod date.
- **Currency:** None on section pages. The SPA reads https://sdlegislature.gov/api/Statutes/LastStatuesEffectiveDate (sic) for its 'Last Updated' label; the sitemap index shows the same date. — observed: ""2026-09-03T00:00:00-05:00""
- **Official status:** SDCL 2-16-13 (read at https://sdlegislature.gov/api/Statutes/2-16-13.html) defines the official code as the printed revised volumes and supplements; 2-16-13.1 excludes catchlines, notes and appendices. No statement found that the online text is official, and no UELMA authentication.
- **Hazard:** the human /Statutes/{section} URL is a JavaScript shell for both fetch routes; always use /api/Statutes/{section}.html
- **Hazard:** rule-numbered sections in 15-6 need the parenthetical (15-6-56(c)); the bare number gives an empty 200 page, not a 404
- **Hazard:** unknown keys also give an empty 200 page, not a 404: treat 0 characters as not found
- **Hazard:** no currency line on the page itself
- **Probe:** SDCL 22-18-1 → `https://sdlegislature.gov/api/Statutes/22-18-1.html` — expect: "A person is guilty of simple assault, a Class 1 misdemeanor"
- **Evidence (2026-10-17):** fetch_doc.py read: 1,843 chars, '22-18-1. Simple assault--Violation as misdemeanor'; body 'A person is guilty of simple assault, a Class 1 misdemeanor'. Also 53-1-1 (191 chars, 'A contract is an agreement to do or not to do'; WebFetch YES, complete), 32-23-1, 19-19-702, 15-26A-60, 23A-8-3, 15-6-56(c), 15-6-12(b) all returned body text.
- **Notes:** Second-route check for statutes: sd-sdcl-justia (2025 edition).

### `sd-session-laws-lrc` — South Dakota Session Laws (LRC API)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Session laws by session; chapter text as HTML in JSON. SessionId 44 = 2021, 70 = 2025, 71 = 2026 (from /api/Sessions).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format json
  - Pattern: `https://sdlegislature.gov/api/SessionLaws/SessionLaw/{session_law_id}`
  - Placeholders: SL {year}, ch {n}: look up SessionId for {year} in https://sdlegislature.gov/api/Sessions (regular session, SpecialSession false) → GET https://sdlegislature.gov/api/SessionLaws/ChapterToId/{n}?SessionId={SessionId} returns the numeric SessionLawId → GET /api/SessionLaws/SessionLaw/{id} (JSON; Html field holds the act). Whole-session list: /api/SessionLaws/{SessionId}.
  - Index: `https://sdlegislature.gov/api/Sessions`
  - Navigation: Sessions list → ChapterToId → SessionLaw JSON. Verified: SL 2021, ch 92 → SessionId 44 → id 7285.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - JSON with embedded HTML; quote from the Html field.
- **Currency:** none stated
- **Official status:** No official-status statement seen on the API responses.
- **Hazard:** needs two lookups (SessionId, SessionLawId)
- **Hazard:** HTML inside JSON strings
- **Probe:** SL 2021, ch 92 → `https://sdlegislature.gov/api/SessionLaws/SessionLaw/7285` — expect: "An Act to increase the enhanced penalty for the crime of simple assault."
- **Evidence (2026-10-17):** fetch_doc.py: ChapterToId/92?SessionId=44 → '7285'; SessionLaw/7285 2,496 chars, Catchline 'An Act to increase the enhanced penalty for the crime of simple assault.' (House Bill 1080); matches the 22-18-1 source note 'SL 2021, ch 92'.

### `sd-sdcl-justia` — Justia — South Dakota Codified Laws

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Editions 2011–2025 (index lists 2025, 2024, 2023, 2021 …); undated path serves the 2025 edition. Includes the codified court rules.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/south-dakota/title-{title}/chapter-{chapter:02d}/section-{section_slug}/`
  - Placeholders: title as cited (22, 15); chapter zero-padded to two digits (15-6 → chapter-06; 22-18 → chapter-18). section_slug = the full SDCL number with a parenthetical turned into a hyphen suffix: 22-18-1 → section-22-18-1; 15-6-56(c) → section-15-6-56-c. Lettered titles/chapters (23A, 15-26A) were not tested: fetch the chapter index and copy the link. Year editions: /codes/south-dakota/2025/…
  - Index: `https://law.justia.com/codes/south-dakota/`
  - Navigation: title page (/codes/south-dakota/title-15/) lists chapters WITHOUT section ranges → chapter page (/title-15/chapter-06/) lists every section, each subsection rule as its own entry → section page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: fetch_doc.py: law.justia.com robots.txt answered with a bot challenge (host refused for the day, 2026-10-17)
  - Two built URLs (title-15/chapter-6/section-15-6-56-c/ unpadded, and title-53/chapter-1/section-53-1-1/ unpadded) returned 'error while fetching'; the padded chapter form copied from the chapter index worked.
- **Currency:** edition label at top of each section page — observed: "2025 South Dakota Codified Laws"
- **Official status:** Page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** edition lags the LRC text by up to a year
- **Hazard:** chapter must be zero-padded (chapter-06)
- **Hazard:** script route refused (bot challenge)
- **Probe:** SDCL 15-6-56(c) → `https://law.justia.com/codes/south-dakota/title-15/chapter-06/section-15-6-56-c/` — expect: "Unless different periods are fixed or permitted by order of"
- **Evidence (2026-10-17):** WebFetch YES: 'Unless different periods are fixed or permitted by order of'; label '2025 South Dakota Codified Laws'. Also /title-22/chapter-18/section-22-18-1/ YES 'A person is guilty of simple assault, a Class 1'.

## B. Constitution

### `sd-constitution-lrc` — South Dakota Constitution (LRC per-section HTML)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Preamble and Articles I–XXVI by section, with amendment history notes.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://sdlegislature.gov/api/Statutes/Constitution/0N-{article}-{section}.html`
  - Placeholders: {article} = the Roman article converted to Arabic (art. VI → 6, art. V → 5); {section} = section number. '0N' is the LRC's title key for the Constitution. Article page: /api/Statutes/Constitution/0N-{article}.html (lists sections). Preamble key: 0N-Preamble. JSON form /api/Statutes/Constitution/{article}-{section} has an EMPTY Html field — do not use it for text.
  - Index: `https://sdlegislature.gov/api/Statutes/Constitution`
- **Automation:** WebFetch ok · shell unreadable-format · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - fetch_doc.py downloads the page (HTTP 200, 1,788 bytes for 0N-6-2) but extracts 0 characters: the page opens with a doubled '<HTML><HEAD>' and the extractor drops the body. WebFetch reads it. Quote only under the two-fetch rule with sd-constitution-justia as the second fetch.
- **Currency:** none stated; each section ends with its amendment history — observed: "Amendment proposed by SL 1945, ch 315, approved Nov., 1946."
- **Official status:** No official-status statement on the pages.
- **Hazard:** script route extracts 0 characters (malformed HTML head)
- **Hazard:** JSON endpoint has empty Html
- **Hazard:** Roman → Arabic article conversion
- **Probe:** S.D. Const. art. VI, § 2 → `https://sdlegislature.gov/api/Statutes/Constitution/0N-6-2.html` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-17):** WebFetch YES: 'No person shall be deprived of life, liberty or property'; complete. Also 0N-5-1.html YES 'The judicial power of the state is vested in a'. fetch_doc.py: 200 but 0 chars extracted (raw bytes hold the text).
- **Notes:** The Secretary of State's constitution PDFs found by search (sdsos.gov/2025 South Dakota Constitution 20250919.pdf, www.sdsos.gov/2023SouthDakotaConstitution20220124.pdf) returned HTTP 404 to fetch_doc.py.

### `sd-constitution-justia` — Justia — South Dakota Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All articles, per-section pages.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/south-dakota/article-{article}/section-{section}/`
  - Placeholders: {article} Arabic (VI → 6). Article page /article-6/ lists section headings only (no body text).
  - Index: `https://law.justia.com/constitution/south-dakota/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: fetch_doc.py: law.justia.com robots.txt answered with a bot challenge (host refused for the day, 2026-10-17)
- **Currency:** Disclaimer block; no edition date — observed: "This Constitution may not be the most recent version."
- **Official status:** Disclaimer: 'This Constitution may not be the most recent version.'
- **Hazard:** no edition date
- **Hazard:** article pages hold headings only
- **Probe:** S.D. Const. art. VI, § 2 → `https://law.justia.com/constitution/south-dakota/article-6/section-2/` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-17):** WebFetch YES: 'No person shall be deprived of life, liberty or property'. Article page /article-6/: section 2 body NOT PRESENT (headings only).

## C. Court rules

### `sd-rules-orders-ujs` — Supreme Court Published Rules (rule-adoption orders)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Unified Judicial System · text: **link-only** · official: official
- **Coverage:** Rule orders 1991–2026 (year filter); pending proposals on /supreme-court/rules-hearings/.
- **Access:** `search-only` · format pdf
  - Pattern: `https://ujs.sd.gov/supreme-court/published-rules/?keywords={words}&year={year}&archive=true`
  - Placeholders: Plain GET. Without archive=true the current list can be empty ('0 of 0'). Titles name the SDCL section, e.g. 'ADOPTION OF NEW RULES AT SDCL 16-3-5.3'. PDFs at /media/{random}/{file}.pdf — not constructible; take from the listing.
  - Index: `https://ujs.sd.gov/supreme-court/published-rules/`
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * / Allow: / (ujs.sd.gov/robots.txt, 23 chars)
  - fetch_doc.py links works on the listing; the HTML table text itself is dropped by its extractor, use 'links'.
- **Currency:** order dates in listing
- **Official status:** Orders of the Supreme Court; page notes unarchived documents 'do not contain signatures but have been approved by the Court'.
- **Hazard:** random /media/ path segment
- **Hazard:** default view hides archived orders
- **Probe:** rule orders 2025 → `https://ujs.sd.gov/supreme-court/published-rules/?year=2025&archive=true` — expect: "IN THE MATTER OF THE ADOPTION OF NEW RULES AT SDCL 16-3-5.3"
- **Evidence (2026-10-17):** fetch_doc.py links: 10 PDF links, first '[Archive] IN THE MATTER OF THE ADOPTION OF NEW RULES AT SDCL 16-3-5.3' → /media/4rxprw2v/scrule_rsrc_20250305135006.pdf. Default view without archive: '0 of 0'.
- **Notes:** Use for effective dates of amendments; quote rule text from sd-rules-sdcl.

### `sd-rules-professional-conduct` — South Dakota Rules of Professional Conduct (Appendix to SDCL ch. 16-18)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules 1.0–8.5 with source notes, on one page.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://sdlegislature.gov/api/Statutes/16-18-A.html`
  - Placeholders: One page for the whole appendix; find 'Rule {n}.' inside it. The chapter page 16-18 links it as Statute=16-18-A. Other appendices follow the same '-A' key (e.g. 16-2-A code of judicial conduct — untested).
  - Index: `https://sdlegislature.gov/api/Statutes/16-18.html`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - WebFetch reads 100,000 of 118,646 chars: stops inside Rule 7.2(d); Rule 8.4 NOT PRESENT. fetch_doc.py reads all 119,723 chars.
- **Currency:** per-rule source notes only — observed: "SL 2022, ch 250 (Supreme Court Rule 21-09), eff. Sep. 1, 2021"
- **Official status:** SDCL 2-16-13.1(6) excludes 'The Rules of Professional Conduct appearing as an appendix to chapter 16-18' from the official code.
- **Hazard:** WebFetch truncation after Rule 7.2
- **Hazard:** excluded from the official code
- **Probe:** S.D. Rules of Prof'l Conduct R. 1.7 → `https://sdlegislature.gov/api/Statutes/16-18-A.html` — expect: "Rule 1.7. Conflict of Interest: Current Clients"
- **Evidence (2026-10-17):** fetch_doc.py grep 'Rule 1.7': offset 28649 'Rule 1.7. Conflict of Interest: Current Clients (a) Except as provided'. WebFetch: truncated at 100,000 chars, Rule 8.4 NOT PRESENT.

### `sd-rules-sdcl` — Court rules codified in the SDCL (civil, appellate, evidence, criminal procedure)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council (rules adopted by the Supreme Court) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of Civil Procedure = SDCL ch. 15-6 (15-6-1 … 15-6-86, subsections such as 15-6-12(b) are separate sections); Appellate Procedure = ch. 15-26A; Evidence = ch. 19-19 (19-19-101 … 19-19-1103, mirroring FRE numbers); Criminal Procedure = Title 23A (sections carry the federal rule number, e.g. 23A-8-3 '(Rule 12(b))'). Circuit-court rules in ch. 16-3.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://sdlegislature.gov/api/Statutes/{section}.html`
  - Placeholders: Same as sd-sdcl-lrc. Civil rules: 'Rule 56(c)' ↔ SDCL 15-6-56(c) (URL keeps the parenthetical). Evidence: 'Rule 702' ↔ SDCL 19-19-702. Criminal: the federal-rule number is in the catchline, not the key (Rule 12(b) ↔ 23A-8-3): find it on the chapter page or Title 23A index.
  - Index: `https://sdlegislature.gov/api/Statutes/15-6.html`
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - Chapter 15-6 table of contents is 17,518 chars and lists every rule subsection.
- **Currency:** as sd-sdcl-lrc — observed: ""2026-09-03T00:00:00-05:00""
- **Official status:** Supreme Court rules are enacted into the SDCL (source notes cite 'Supreme Court Rule NN-NN'); online text status as sd-sdcl-lrc.
- **Hazard:** 15-6-NN without the subsection returns an empty page
- **Hazard:** criminal rules not keyed by federal rule number
- **Probe:** SDCL 15-6-56(c) → `https://sdlegislature.gov/api/Statutes/15-6-56(c).html` — expect: "Unless different periods are fixed or permitted by order of the court"
- **Evidence (2026-10-17):** fetch_doc.py: 15-6-56(c) 2,550 chars 'Motion for summary judgment and proceedings thereon'; 15-6-12(b) 1,804 chars; 19-19-702 'A witness who is qualified as an expert by knowledge'; 23A-8-3 '(Rule 12(b)) Defenses and objections raised by motion'; 15-26A-60 'Brief of appellant--Contents'.
- **Notes:** Tier-2 fallback: sd-sdcl-justia (chapter-06/section-15-6-56-c verified).

## D. Administrative code

### `sd-arsd-lrc` — Administrative Rules of South Dakota (ARSD), LRC per-rule HTML

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** All ARSD articles/chapters/rules with Source, General Authority and Law Implemented notes.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://sdlegislature.gov/api/Rules/Rule/{rule}.html`
  - Placeholders: {rule} is the ARSD number with colons as cited: 67:16:01:01, 74:51:01:01, 20:10:01:01. A chapter key (20:10:01) returns the chapter's section list and text. JSON form: https://sdlegislature.gov/api/Rules/{rule} (Html field).
  - Index: `https://sdlegislature.gov/api/Rules`
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * — Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; /api/ paths allowed. Sitemaps: /Statutes.xml, /Rules.xml, /api/Documents/Index/Sitemap.xml
  - Human URL https://sdlegislature.gov/Rules/Administrative/{rule} is the JS app; use the /api/ form.
- **Currency:** per-rule Source note (SDR volume/page and effective date) — observed: "44 SDR 94, effective December 4, 2017."
- **Official status:** No official-status statement on the rule pages.
- **Hazard:** no global currency statement
- **Probe:** ARSD 67:16:01:01 → `https://sdlegislature.gov/api/Rules/Rule/67:16:01:01.html` — expect: "Terms used in this article mean"
- **Evidence (2026-10-17):** WebFetch YES 'Terms used in this article mean: (1) "Allowable costs," expenses'; complete. fetch_doc.py: 67:16:01:01 4,869 chars; 74:51:01:01 11,684 chars 'Terms defined in SDCL 34A-2-2, have the same meaning'; 20:10:01:01 'Sessions of commission'.

### `sd-arsd-lii` — Cornell LII — South Dakota Administrative Rules

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All ARSD titles, per-rule pages; can lag the LRC text by years.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/south-dakota/ARSD-{rule_dashed}`
  - Placeholders: rule_dashed = ARSD number with colons replaced by hyphens: 67:16:01:01 → ARSD-67-16-01-01.
  - Index: `https://www.law.cornell.edu/regulations/south-dakota`
  - Navigation: title-67 → article-67-16 → chapter-67-16-01 → ARSD-67-16-01-01
- **Automation:** WebFetch untested · shell ok · robots: User-agent: *, Crawl-delay: 10; /regulations/ not disallowed
  - Pages last-modified Aug 2025.
- **Currency:** none stated; HTTP Last-Modified — observed: "Wed, 06 Aug 2025 21:52:38 GMT"
- **Official status:** Third-party mirror.
- **Hazard:** STALE: ARSD 74:51:01:01 on LII reads 'Words and phrases defined in SDCL 34A-2-2' while LRC reads 'Terms defined in SDCL 34A-2-2'; 67:16:01:01 wording also differs
- **Hazard:** no currency statement
- **Probe:** ARSD 67:16:01:01 → `https://www.law.cornell.edu/regulations/south-dakota/ARSD-67-16-01-01` — expect: "Terms used in this article mean"
- **Evidence (2026-10-17):** fetch_doc.py grep: 'Terms used in this article mean: (1) "Allowable costs," those expenses' (6,176 chars); verify of LRC wording on ARSD-74-51-01-01 NOT VERIFIED (older text).
- **Notes:** Use only to locate; quote from sd-arsd-lrc.

## D. Administrative register

### `sd-register-lrc` — South Dakota Register (weekly)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Legislative Research Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Weekly issues as PDFs (Volume 53 in 2026); cited as '44 SDR 94'.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://sdlegislature.gov/api/Documents/DocumentTypesRSS?Type=50`
  - Navigation: RSS (161K chars) lists every issue as https://mylrc.sdlegislature.gov/api/Documents/{id}.pdf, newest first; the item text does not carry volume/page, so match an SDR cite by opening issues of the right year. The SPA page https://sdlegislature.gov/Rules/Registers is a JS shell.
- **Automation:** WebFetch untested · shell ok · robots: mylrc.sdlegislature.gov: User-agent: * Disallow: (empty) — all allowed
  - An old id from the JS bundle (210727.pdf) failed pdftotext in fetch_doc.py; current ids read fine.
- **Currency:** masthead date line — observed: "Volume 53 … Tuesday, 8:00 a.m., October 13, 2026"
- **Official status:** Masthead: 'Published weekly by the Legislative Research Council'.
- **Hazard:** no volume/page → PDF index; SDR page cite needs scanning issues
- **Probe:** S.D. Register, Oct. 13, 2026 → `https://mylrc.sdlegislature.gov/api/Documents/308375.pdf` — expect: "FILINGS WITH THE LEGISLATIVE RESEARCH COUNCIL"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 3 pages, 8,568 chars; 'SOUTH DAKOTA REGISTER Published weekly by the Legislative Research Council'; 'Volume 53'.

## E. Case law

### `sd-opinions-ujs` — South Dakota Supreme Court opinions (UJS)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Unified Judicial System · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court opinions 2006–present on the site (year filter 2006–2026; year=1996 archive=true returns 0). South Dakota has no intermediate appellate court.
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://ujs.sd.gov/supreme-court/opinions/?keywords={party}&year={year}&archive=true`
  - Placeholders: Plain GET. keywords matches the case TITLE only (party names): docket numbers (31307) and citation strings ('2010 S.D. 105') do not match. Always add archive=true — older opinions (and some 2026 ones) are 'archived' and hidden otherwise. Each row: date, 'STATE v. LUCERO, 2026 S.D. 48', sequence number; the PDF is https://ujs.sd.gov/media/{random}/{docket}.pdf — the random segment is not constructible, take the link from the listing (fetch_doc.py links … pdf). The docket number is the PDF file name.
  - Index: `https://ujs.sd.gov/supreme-court/opinions/`
  - Read via: PDFs on the same host; fetch_doc.py reads them in full. WebFetch on the PDFs is gated.
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * / Allow: / (ujs.sd.gov/robots.txt, 23 chars)
  - WebFetch read the listing at https://ujs.sd.gov/supreme-court/opinions (URL from a search result) but the built listing URL with a trailing slash and both opinion PDFs (31307.pdf, 31286.pdf) hit PROVENANCE_REQUIRED. fetch_doc.py's text extraction drops the listing table; use its 'links' command. The old URL /Supreme_Court/opinions.aspx redirects to /supreme-court/opinions/. RSS: /supreme-court/opinions/?rss=1.
- **Currency:** listing 'Showing 1-10 of N' and filed dates — observed: "10/7/2026 BIALOTA v. LAKOTA LAKES, LLC, 2026 S.D. 52"
- **Official status:** Slip opinions issued by the Court carrying the clerk-assigned public-domain citation ('2026 S.D. 48'), which SDCL 15-26A-69.1 makes the required citation form from 1996.
- **Hazard:** title-only keyword search
- **Hazard:** archived items hidden unless archive=true
- **Hazard:** PDF path has an unpredictable segment
- **Hazard:** slip opinions: paragraph numbers [¶N.] are the official pinpoint; no N.W.3d pages
- **Probe:** State v. Lucero, 2026 S.D. 48 → `https://ujs.sd.gov/media/xw4fesw2/31307.pdf` — expect: "Jeremy Lucero pled guilty to possession of"
- **Evidence (2026-10-17):** fetch_doc.py: listing ?keywords=Lucero&year=2026 → 1 link 'STATE v. LUCERO, 2026 S.D. 48' /media/xw4fesw2/31307.pdf; PDF 8 pages, 13,176 chars, '#31307-a-SPM 2026 S.D. 48', '[¶1.] Jeremy Lucero pled guilty to possession of'. Also ?keywords=Reed&year=2010&archive=true → 25626.pdf (10 pp) '[¶1.] Stanley Reed (Reed) filed a petition'.
- **Notes:** Pinpoints: cite ¶ numbers (SDCL 15-26A-69.1(2)). Docket header form '#31307-a-SPM' = docket-disposition-author initials.

### `sd-summary-dispositions-ujs` — Supreme Court Summary Dispositions (UJS)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Dakota Unified Judicial System · text: **link-only** · official: official
- **Coverage:** Decisions without full opinion under SDCL 15-26A-87.1, 2022–present (year filter), with disposition and circuit judge; not citable as authority (15-26A-87.1(E)).
- **Access:** `search-only` · format pdf
  - Pattern: `https://ujs.sd.gov/supreme-court/summary-dispositions/?keywords={party}&year={year}&archive=true`
  - Placeholders: As sd-opinions-ujs; PDFs named {docket}oadacomp.pdf under /media/{random}/.
  - Index: `https://ujs.sd.gov/supreme-court/summary-dispositions/`
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * / Allow: / (ujs.sd.gov/robots.txt, 23 chars)
- **Currency:** listing — observed: "10/15/2026 Interest of E.L.W., H.L.W., H.L.W. Affirmed (Kelderman) 31521"
- **Official status:** Orders of the Court; page notes unarchived copies are unsigned but approved by the Court.
- **Hazard:** not precedential
- **Probe:** Interest of E.L.W., No. 31521 → `https://ujs.sd.gov/supreme-court/summary-dispositions/` — expect: "Interest of E.L.W., H.L.W., H.L.W."
- **Evidence (2026-10-17):** fetch_doc.py links: 10 PDFs, first 'Interest of E.L.W., H.L.W., H.L.W.' → /media/hvflyt3r/31521oadacomp.pdf; listing 'Showing 1-10 of 33'.
- **Notes:** Lets a docket number with no S.D. citation be identified as a summary affirmance.

### `sd-cases-justia` — Justia — South Dakota Supreme Court opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Year listings 1894–2026 (1894: 1 opinion; early years sparse); full text with [¶] numbers for public-domain-era opinions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/south-dakota/supreme-court/{year}/{docket}.html`
  - Placeholders: {year} = decision year; {docket} = 5-digit SD docket number (31307, 25626). Without the docket, open the year listing /cases/south-dakota/supreme-court/{year}/ and search by party name.
  - Index: `https://law.justia.com/cases/south-dakota/supreme-court/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: fetch_doc.py: law.justia.com robots.txt answered with a bot challenge (host refused for the day, 2026-10-17)
- **Currency:** year listing counts — observed: "2026 (46 opinions)"
- **Official status:** Third-party republication.
- **Hazard:** needs docket number
- **Hazard:** script route refused
- **Probe:** State v. Lucero, 2026 S.D. 48 → `https://law.justia.com/cases/south-dakota/supreme-court/2026/31307.html` — expect: "Jeremy Lucero pled guilty to possession of a controlled substance,"
- **Evidence (2026-10-17):** WebFetch YES: 'Jeremy Lucero pled guilty to possession of a controlled substance,'; full text through ¶15. Also /2010/25626.html (State v. Reed, 2010 S.D. 105) YES 'Stanley Reed (Reed) filed a petition for writ of habeas'.
- **Notes:** Fallback for 1996–2005 public-domain opinions and older N.W.2d-era opinions not on UJS.

## F. Subsequent history

### `sd-scotus-docket` — U.S. Supreme Court docket (certiorari from the South Dakota Supreme Court)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of the United States · text: **fetch-and-quote** · official: official
- **Coverage:** South Dakota has no intermediate appellate court, so further review of a Supreme Court decision is certiorari only (rehearing under SDCL 15-30-4 is decided by the same court and not listed online). Dockets show 'Lower Ct: Supreme Court of South Dakota' and the SD docket numbers.
- **Read via (in order):** **script**
- **Access:** `search-only` · format html
  - Pattern: `https://www.supremecourt.gov/docket/docketfiles/html/public/{scotus_docket}.html`
  - Placeholders: Constructible only once the SCOTUS docket number is known (25-7600, 24A614). From an SD decision alone there is no link: WebSearch '"Supreme Court of South Dakota" <party> supremecourt.gov' or the SD docket number, or search by party name.
  - Index: `https://www.supremecourt.gov/docket/docket.aspx`
- **Automation:** WebFetch untested · shell ok · robots: docket path allowed (fetch_doc.py ok)
- **Currency:** dated docket entries — observed: "Oct 05 2026 Petition DENIED."
- **Official status:** Docket kept by the Clerk of the Supreme Court.
- **Hazard:** no link from the SD opinion or listing to the SCOTUS docket; party-name search only
- **Probe:** No. 25-7600 (from S.D. Nos. 31006, 31007) → `https://www.supremecourt.gov/docket/docketfiles/html/public/25-7600.html` — expect: "Petition DENIED."
- **Evidence (2026-10-17):** fetch_doc.py grep: 'Lower Ct: Supreme Court of South Dakota'; 'Case Numbers: (31006, 31007)'; 'Decision Date: March 11, 2026'; 'Oct 05 2026 Petition DENIED.' Also 24A614: 'Case Numbers: (30448-a-SRJ)'.
- **Notes:** The citation string is a probe label only; party names on 25-7600 not recorded.

## Not available (do not look for these again)

- **statutes** — public.law edition of the SDCL: public.law home page (checked in the DE run, 2026-10-16) lists only CA, CO, FL, NV, NY, OR, TX. (2026-10-17)
- **statutes** — Cornell LII South Dakota statutes / constitution / opinions: https://www.law.cornell.edu/states/south_dakota links out to sdlegislature.gov and ujs.sd.gov; LII hosts only the SD administrative rules. (2026-10-17)
- **statutes** — Official bulk download (XML/JSON/zip) of the SDCL: None linked; the nearest is the per-section JSON API and the section sitemaps Statutes.1.xml / Statutes.2.xml (see script_candidates). (2026-10-17)
- **case_law** — UJS opinions before 2006: Year filter runs 2006–2026; ?year=1996&archive=true returned 0 links. Use sd-cases-justia. (2026-10-17)
- **case_law** — Free N.W.2d / N.W.3d pagination: UJS PDFs carry slip pages and ¶ numbers only; N.W. is a West reporter. SDCL 15-26A-69.1 makes ¶ numbers the official pinpoint from 1996. (2026-10-17)
- **subsequent_history** — Public online list of rehearing dispositions / Supreme Court docket: No rehearing list on the UJS Supreme Court pages; ecourts.sd.gov links to Account/Login.aspx (login required). (2026-10-17)

## Corpus candidates (maintainers)

- `sd-rules-professional-conduct` — Single 118,646-char page; WebFetch stops inside Rule 7.2(d), Rule 8.4 not reached.

## Open questions

- Justia statute URLs for lettered titles/chapters (23A, 15-26A) not tested: is it title-23a / chapter-26a?
- Does ?all=true on large chapters exceed WebFetch's 100K limit (likely for 15-6)? Not tested.
- Code of Judicial Conduct appendix key (16-2-A) not tested.
- Where the UJS posts rehearing grants/denials, if anywhere, is unknown.

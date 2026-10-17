# North Dakota (ND) — free legal sources

_Generated from `data/nd.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution, administrative code and quarterly rule supplements are official PDFs on ndlegis.gov with constructible URLs (chapter PDFs t{title}c{chapter}.pdf; constit/a{NN}.pdf; acdata/pdf/{t-a-c}.pdf) read reliably by fetch_doc.py; WebFetch needs approval for built ndlegis URLs. Court rules are per-rule HTML pages on ndcourts.gov that WebFetch reads, but ndcourts.gov refuses the script (Cloudflare) and opinion and docket pages were gated for WebFetch, so Supreme Court opinion text is read from Justia (docket-keyed URLs) for now. The ND State Library serves scanned North Dakota Reports volumes (official pagination, pre-1953) as per-volume PDFs. Justia also covers the Century Code (chapter pages) and constitution; Cornell LII mirrors the Administrative Code per section. Public-domain cites 'YYYY ND N' since 1997; certiorari via supremecourt.gov dockets.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| North Dakota Supreme Court | `nd (unverified)` | N.D. | N.W.3d, N.W.2d, N.W., N.D. | 2023 ND 32 |
| North Dakota Court of Appeals (temporary) | `ndctapp (unverified)` | N.D. Ct. App. | N.W.2d | 1998 ND App 1 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| North Dakota Century Code | `N.D.C.C. § 28-01-16`; `N.D. Cent. Code § 12.1-32-01`; `N.D.C.C. § 10-19.1-150`; `N.D.C.C. ch. 28-32`; `NDCC 4.1-01-01`; `section 28-01-16 of the North Dakota Century Code`; `N.D.C.C. §§ 28-01-16 to -18` | `nd-cencode-ndlegis` → `nd-cencode-justia` |
| North Dakota session laws | `2025 N.D. Sess. Laws ch. 120`; `2019 N.D. Laws ch. 254` | `nd-session-laws-ndlegis` |
| North Dakota Constitution | `N.D. Const. art. I, § 9`; `N.D. Const. art. VI, § 2`; `Article I, Section 9 of the North Dakota Constitution` | `nd-constitution-ndlegis` → `nd-constitution-justia` |
| North Dakota rules of procedure and evidence (N.D.R.Civ.P., Crim.P., App.P., Ev., Ct.) | `N.D.R.Civ.P. 56(c)`; `Rule 56(c), N.D.R.Civ.P.`; `N.D.R.Crim.P. 11`; `N.D.R.App.P. 40`; `N.D.R.Ev. 802`; `N.D.R.Ct. 3.2`; `Rule 3.2, N.D.R.Ct.`; `N.D. R. Civ. P. 12(b)(6)` | `nd-rules-ndcourts` |
| North Dakota Rules of Professional Conduct / Lawyer Discipline / Supreme Court Administrative Rules | `N.D.R. Prof. Conduct 1.7`; `Rule 1.7, N.D.R. Prof. Conduct`; `N.D.R. Lawyer Discipl. 1.2`; `N.D. Sup. Ct. Admin. R. 27`; `Rule 1.7 of the North Dakota Rules of Professional Conduct` | `nd-rules-ndcourts` |
| North Dakota Administrative Code | `N.D. Admin. Code § 43-02-03-01`; `N.D.A.C. 75-02-02-09`; `N.D. Admin Code 43-02-03-01`; `N.D.A.C. ch. 75-02-02`; `N.D.A.C. § 4.5-02.1-01-01` | `nd-admincode-ndlegis` → `nd-admincode-lii` |
| North Dakota Administrative Rules Supplement *(only once this jurisdiction is known)* | `Administrative Rules Supplement 2016-362`; `Administrative Rules Supplement 401` | `nd-admin-supplements-ndlegis` |
| North Dakota public-domain citation (1997-) | `2023 ND 32`; `2023 ND 32, ¶ 8`; `Queen v. Martel, 2022 ND 178, ¶ 8, 980 N.W.2d 914`; `1998 ND App 1` | `nd-opinions-ndcourts` → `nd-cases-justia` |
| North Western Reporter with (N.D. YYYY) | `Egbert v. City of Dunseith, 24 N.W.2d 907, 910 (N.D. 1946)`; `State v. Julson, 202 N.W.2d 145, 151 (N.D. 1972)`; `Pulkrabek v. Morton Cnty., 389 N.W.2d 609, 615 (N.D. 1986)`; `Anderson v. City of Fargo, 186 N.W. 378 (N.D. 1922)` | `nd-cases-justia` → `nd-opinions-ndcourts` |
| North Western Reporter (generic, no court parenthetical) *(only once this jurisdiction is known)* | `980 N.W.2d 914`; `451 N.W.2d 118, 121` | `nd-cases-justia` → `nd-opinions-ndcourts` |
| North Dakota Reports (official reporter, 1890-1953) | `48 N.D. 722`; `Anderson v. City of Fargo, 48 N.D. 722, 186 N.W. 378 (1922)` | `nd-reports-library` → `nd-cases-justia` |
| North Dakota Supreme Court docket number *(only once this jurisdiction is known)* | `No. 20220121`; `Docket No. 20250066` | `nd-cases-justia` → `nd-opinions-ndcourts` → `nd-docket-ndcourts` |

Regexes (case-insensitive):

- North Dakota Century Code: `(?:\bN\.\s?D\.\s?C\.\s?C\.|\bNDCC\b|\bN\.\s?D\.\s*Cent(?:ury)?\.?\s*Code(?:\s+Ann\.)?)\s*,?\s*(?:§§?\s*|ch(?:apter|\.)\s*)?(?P<title>\d{1,2}(?:\.\d)?)-(?P<chapter>\d{2}(?:\.\d{1,2})?)(?:-(?P<section>\d{2,3}(?:\.\d{1,2})?))?(?![\d.]*\d)|(?:[Ss]ec(?:tion|\.)|§)\s*(?P<title2>\d{1,2}(?:\.\d)?)-(?P<chapter2>\d{2}(?:\.\d{1,2})?)-(?P<section2>\d{2,3}(?:\.\d{1,2})?)(?:\([a-z0-9]+\))*\s+of\s+(?:the\s+)?North\s+Dakota\s+Century\s+Code`
- North Dakota session laws: `(?P<year>(?:18|19|20)\d\d)\s+N\.\s?D\.\s*(?:Sess\.\s*)?Laws,?\s*ch\.?\s*(?P<chapter>\d+)`
- North Dakota Constitution: `N\.\s?D\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+),?\s+(?:Section|§)\s*(?P<section2>\d+)\s+of\s+the\s+(?:North\s+Dakota|N\.\s?D\.)\s+Constitution`
- North Dakota rules of procedure and evidence (N.D.R.Civ.P., Crim.P., App.P., Ev., Ct.): `N\.\s?D\.\s?R\.\s?(?P<set>Civ\.\s?P|Crim\.\s?P|App\.\s?P|Ev(?:id)?|Ct|Juv\.\s?P)\.\s*(?P<rule>\d+(?:\.\d+)*)|Rule\s+(?P<rule2>\d+(?:\.\d+)*)(?:\([a-z0-9]+\))*,\s*N\.\s?D\.\s?R\.\s?(?P<set2>Civ\.\s?P|Crim\.\s?P|App\.\s?P|Ev(?:id)?|Ct|Juv\.\s?P)\.`
- North Dakota Rules of Professional Conduct / Lawyer Discipline / Supreme Court Administrative Rules: `N\.\s?D\.\s?R\.\s*(?P<set>Prof\.\s*Conduct|Lawyer\s+Discipl\.)\s*(?P<rule>\d+(?:\.\d+)*)|Rule\s+(?P<rule2>\d+(?:\.\d+)*),\s*N\.\s?D\.\s?R\.\s*(?:Prof\.\s*Conduct|Lawyer\s+Discipl\.)|N\.\s?D\.\s*Sup\.\s*Ct\.\s*Admin\.\s*R(?:ule)?\.?\s*(?P<rule3>\d+(?:\.\d+)*)|Rule\s+(?P<rule4>\d\.\d+)(?:\([a-z0-9]+\))*\s+of\s+the\s+North\s+Dakota\s+Rules\s+of\s+Professional\s+Conduct`
- North Dakota Administrative Code: `(?:\bN\.\s?D\.\s?A\.\s?C\.|\bN\.\s?D\.\s*Admin\.?\s*Code)\s*(?:§\s*|ch(?:apter|\.)\s*)?(?P<title>\d{1,3}(?:\.\d)?)-(?P<article>\d{2}(?:\.\d{1,2})?)-(?P<chapter>\d{2}(?:\.\d{1,2})?)(?:-(?P<section>\d{2,3}(?:\.\d{1,2})?))?`
- North Dakota Administrative Rules Supplement: `Administrative\s+Rules\s+Supplement\s+(?:(?P<year>(?:19|20)\d\d)-)?(?P<number>\d{3})`
- North Dakota public-domain citation (1997-): `(?<![\w.])(?P<year>199[7-9]|20\d\d)\s+ND\s+(?P<app>App\s+)?(?P<number>\d{1,3})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- North Western Reporter with (N.D. YYYY): `(?P<volume>\d{1,4})\s+N\.\s?W\.(?:\s?(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\(N\.\s?D\.\s*(?:Ct\.\s*App\.\s*)?(?P<year>\d{4})\)`
- North Western Reporter (generic, no court parenthetical): `(?P<volume>\d{1,4})\s+N\.\s?W\.(?:\s?(?P<series>[23])d)?\s+(?P<page>\d{1,5})`
- North Dakota Reports (official reporter, 1890-1953): `(?<![\d.])(?P<volume>\d{1,2})\s+N\.\s?D\.\s+(?P<page>\d{1,4})(?!\d)`
- North Dakota Supreme Court docket number: `No\.\s*(?P<docket>(?:19|20)\d{6})(?!\d)`

N.D.R.Ct. 11.6: opinions from 1997 are cited in public-domain form 'YYYY ND N' (no periods), pinpointed by paragraph '¶ N'; parallel N.W.2d/N.W.3d cite added when available. Temporary Court of Appeals opinions use 'YYYY ND App N'. Pre-1997 cases cite N.W./N.W.2d with '(N.D. YYYY)'; North Dakota Reports ran 1890-1953 (79 vols, per memory). Century Code numbers are title-chapter-section, each part may carry a decimal (12.1-32-01, 10-19.1-150, 4.1-01-01); the code is cited 'N.D.C.C. § …' (court style) or 'N.D. Cent. Code § …' (Bluebook). A '§§ 28-01-16 to -18' range is a span: take the first section. ND court style puts the rule set after the number ('Rule 56(c), N.D.R.Civ.P.'); both orders are covered. Routing guards: '(N.D.' also opens federal district parentheticals ('N.D. Ill.', 'N.D. Cal.'), so only the N.W. reporter form with '(N.D. YYYY)' or '(N.D. Ct. App. YYYY)' routes here; bare N.W.2d cites, bare 8-digit docket numbers and 'Administrative Rules Supplement' are context_required. CourtListener ids 'nd' and 'ndctapp' are from memory and unverified.

## A. Statutes / code

### `nd-cencode-ndlegis` — North Dakota Century Code (chapter PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Legislative Council · text: **fetch-and-quote** · official: official
- **Coverage:** All titles of the Century Code, one PDF per chapter; section-listing HTML per chapter.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://ndlegis.gov/cencode/t{title}c{chapter}.pdf#nameddest={dest}`
  - Placeholders: title and chapter = the cited numbers with '.' replaced by '-' and the integer part zero-padded to 2 digits: 28-01-16 -> t28c01.pdf; 12.1-32-01 -> t12-1c32.pdf; 10-19.1-150 -> t10c19-1.pdf; 4.1-01-01 -> t04-1c01.pdf; 4-02.1 -> t04c02-1.pdf. The PDF holds the whole chapter; the section anchor is #nameddest={section} with '.' in the title written as 'p' (28-01-16 -> 28-01-16; 4.1-01-01 -> 4p1-01-01). Fetch tools ignore the fragment, so grep the chapter text for '{section}. ' (section number + period + space). Section listings: https://ndlegis.gov/cencode/t{title}c{chapter}.html; title listing https://ndlegis.gov/cencode/t{title}.html. www.ndlegis.gov redirects to ndlegis.gov.
  - Index: `https://ndlegis.gov/general-information/north-dakota-century-code/index.html`
  - Navigation: Not needed for well-formed cites. The index page (3.6M chars) lists every section with catchline under each chapter, so it shows section ranges.
- **Automation:** WebFetch gated · shell ok · robots: Drupal default: Disallow /core/, /admin/, /search/, /user/* etc.; /cencode/ not disallowed
  - WebFetch on built cencode URLs and the home page ended in PROVENANCE_REQUIRED (permission prompt not answered); the index page reached via a search result worked but truncated at chapter 6-01. Large chapters exceed the fetch tool window (t10c19-1.pdf: 95 pp, 394,274 chars); use fetch_doc.py grep/section.
- **Currency:** Century Code index page, paragraph under the official-version notice; PDFs carry no date (HTTP last-modified only) — observed: "07/01/25 UPDATE: All statutory changes approved by the 69th Legislative Assembly"
- **Official status:** Century Code index page (https://ndlegis.gov/general-information/north-dakota-century-code): text published on this website 'is the official version of the North Dakota Century Code'.
- **Hazard:** whole chapter per PDF; long chapters (10-19.1) exceed the fetch tool window
- **Hazard:** #nameddest fragment ignored by fetch tools
- **Hazard:** decimal titles/chapters: '.' -> '-' in file name, 'p' in nameddest
- **Hazard:** statutes effective after August 1 are flagged only in the caption parenthetical
- **Hazard:** January and September 2026 special-session changes not covered by the 07/01/25 notice (check session laws)
- **Probe:** N.D.C.C. § 28-01-16 → `https://ndlegis.gov/cencode/t28c01.pdf` — expect: "The following actions must be commenced within six years after the claim for relief"
- **Evidence (2026-10-17):** fetch_doc.py: t28c01.pdf 10 pp, 36,801 chars, grep '28-01-16. Actions having six-year limitations.' + body. t12-1c32.pdf 22 pp starts 'CHAPTER 12.1-32 PENALTIES AND SENTENCING', '12.1-32-01. Classification of offenses - Penalties.' t10c19-1.pdf 95 pp, § 10-19.1-150 found at p. 94. WebFetch on built URLs: PROVENANCE_REQUIRED.
- **Notes:** Official text is free and constructible; the script route is the reliable reader. Chapter section-listing pages link each section as t{t}c{c}.pdf#nameddest={section}.

### `nd-session-laws-ndlegis` — North Dakota Session Laws

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Session laws by assembly (2015- listed on the index, older in archives); per-year full-book PDF and per-category chapter PDFs.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Full book: https://ndlegis.gov/assembly/{assembly}-{year}/session-laws/sl{year}.pdf (2025 seen). Category PDFs: /assembly/{assembly}-{year}/session-laws/documents/{code}.pdf (gnlpr, appro, agric …). A chapter number does not map to a category file without the index.
  - Index: `https://ndlegis.gov/research-and-archives/session-laws`
  - Navigation: session-laws index -> '{year} Session Laws' page (/assembly/69-2025/regular/2025-session-laws) -> 'Full Book (PDF)' or 'Chapter Categories' -> category PDF.
- **Automation:** WebFetch untested · shell ok · robots: see nd-cencode-ndlegis
  - /assembly/69-2025/regular/session-laws returned HTTP 403 (wrong path); the linked /2025-session-laws page works.
- **Currency:** none stated
- **Official status:** No official-status statement seen on the session-law pages.
- **Hazard:** category PDFs not keyed by chapter number
- **Hazard:** full-book PDF very large
- **Probe:** 2025 N.D. Sess. Laws, General Provisions (H.B. 1031) → `https://ndlegis.gov/assembly/69-2025/session-laws/documents/gnlpr.pdf` — expect: "AN ACT to amend and reenact section 1-01-49"
- **Evidence (2026-10-17):** fetch_doc.py: gnlpr.pdf 18 pp, 45,377 chars, 'HOUSE BILL NO. 1031 … AN ACT to amend and reenact section 1-01-49'.

### `nd-cencode-justia` — Justia - North Dakota Century Code (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** N.D. Cent. Code editions incl. 2012-2025; unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/north-dakota/title-{title}/chapter-{chapter_full}/`
  - Placeholders: title with '.' -> '-' (title-28, title-12-1); chapter_full = title-chapter with '.' -> '-' (chapter-28-01, chapter-12-1-32). The CHAPTER page holds the full text of every section (section headings are not links). Year editions: insert /{year}/ after /north-dakota/.
  - Index: `https://law.justia.com/codes/north-dakota/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com refused the script (robots.txt challenge) earlier on 2026-10-17
  - One WebFetch of a built section-level URL (/section-28-01-16/) returned CLIENT_ERROR; chapter-level URLs work.
- **Currency:** page heading — observed: "2025 North Dakota Century Code Title 12.1 - Criminal Code"
- **Official status:** Third-party compilation; older editions are marked 'There Is a Newer Version'.
- **Hazard:** no per-section pages; long chapters may exceed the fetch tool window
- **Hazard:** edition lags official text
- **Hazard:** shell blocked
- **Probe:** N.D. Cent. Code § 12.1-32-01 → `https://law.justia.com/codes/north-dakota/title-12-1/chapter-12-1-32/` — expect: "Offenses are divided into seven classes, which are denominated and"
- **Evidence (2026-10-17):** WebFetch: YES, body of 12.1-32-01 present, runs through 12.1-32-16, not truncated, heading '2025 North Dakota Century Code'. Also /title-28/chapter-28-01/ holds full text of 28-01-01 to 28-01-48 incl. 28-01-16.

## B. Constitution

### `nd-constitution-ndlegis` — Constitution of North Dakota (article PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Preamble, Articles I-XIV and transition schedule, one PDF per article.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://ndlegis.gov/constit/a{article:02d}.pdf`
  - Placeholders: article = Arabic number of the Roman article, zero-padded to 2 (I -> a01, VI -> a06, X -> a10); preamble = /constit/preamble.pdf. Sections appear as 'Section N.' in running text.
  - Index: `https://ndlegis.gov/constitution`
- **Automation:** WebFetch untested · shell ok · robots: see nd-cencode-ndlegis
  - Built ndlegis URLs are expected to be gated in WebFetch (as for cencode).
- **Currency:** constitution page intro; PDFs undated (a01.pdf last-modified 2016-12-08) — observed: "contains the current provisions of the state constitution"
- **Official status:** Constitution page says it 'contains the current provisions of the state constitution'; no authentication statement.
- **Hazard:** no edition date on the PDFs
- **Probe:** N.D. Const. art. I, § 9 → `https://ndlegis.gov/constit/a01.pdf` — expect: "All courts shall be open, and every man for any injury done him"
- **Evidence (2026-10-17):** fetch_doc.py: a01.pdf 5 pp, 'ARTICLE I DECLARATION OF RIGHTS'; grep 'Section 9. All courts shall be open'. a06.pdf 2 pp, 'Section 2. The supreme court shall be the highest court of the state.'

### `nd-constitution-justia` — Justia - North Dakota Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble, Articles I-XIV, transition schedule, Enabling Act; one page per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/north-dakota/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article as lower-case Roman numeral (article-i, article-vi); the article page is a section index only, body text is on the section page.
  - Index: `https://law.justia.com/constitution/north-dakota/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (script refused law.justia.com, robots.txt challenge, 2026-10-17)
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version."
- **Official status:** Page: 'This Constitution may not be the most recent version.'
- **Hazard:** undated
- **Hazard:** index and article pages hold no text
- **Hazard:** shell blocked
- **Probe:** N.D. Const. art. I, § 9 → `https://law.justia.com/constitution/north-dakota/article-i/section-9/` — expect: "All courts shall be open, and every man for any injury done"
- **Evidence (2026-10-17):** WebFetch: YES, 'All courts shall be open, and every man for any injury done'. Index and /article-i/ pages: NOT PRESENT (links only).

## C. Court rules

### `nd-rules-ndcourts` — North Dakota Court Rules (per-rule pages)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of Civil, Criminal, Appellate and Juvenile Procedure, Evidence, Rules of Court, Professional Conduct, Lawyer Discipline, Supreme Court Administrative Rules, local rules; each rule with explanatory note, sources and version history.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ndcourts.gov/legal-resources/rules/{set}/{rule}`
  - Placeholders: set slugs: ndrcivp (N.D.R.Civ.P.), ndrcrimp (N.D.R.Crim.P.), ndrappp (N.D.R.App.P.), ndrev (N.D.R.Ev.), ndrct (N.D.R.Ct.), ndrprofconduct (N.D.R. Prof. Conduct), ndrlawyerdiscipl (N.D.R. Lawyer Discipl.), ndsupctadminr (N.D. Sup. Ct. Admin. R.). rule = rule number with '.' -> '-' (56 -> 56; 56.1 -> 56-1; N.D.R.Ct. 3.2 -> 3-2; 3.2.3 -> 3-2-3; Prof. Conduct 1.7 -> 1-7, unverified). Local rules: /legal-resources/rules/local/{district}/{rule} (e.g. local/east-central/1-1, from search). Rule-set index: /legal-resources/rules/{set}.
  - Index: `https://www.ndcourts.gov/legal-resources/rules`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: none (robots.txt serves the custom error page)
  - fetch_doc.py: HTTP 403 Cloudflare challenge on www.ndcourts.gov (host off for the day). WebFetch read rule pages that came from search results; the built /legal-resources/rules index URL was PROVENANCE_REQUIRED (gated).
- **Currency:** each rule page, 'Effective Date' line and Version History — observed: "Effective Date: 3/1/2021"
- **Official status:** Rule-set index pages carry no official-status statement; each rule page shows effective date and version history.
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** built URLs may need approval in WebFetch
- **Hazard:** dotted rule numbers become hyphens in the URL
- **Probe:** N.D.R.Civ.P. 56 → `https://www.ndcourts.gov/legal-resources/rules/ndrcivp/56` — expect: "A party claiming relief may move, with or without supporting declarations, for"
- **Evidence (2026-10-17):** WebFetch: YES, Rule 56 body (a)-(g), explanatory note, 'Effective Date: 3/1/2021', not truncated. Second: /ndrev/802 YES 'Hearsay is not admissible unless any of the following provides otherwise', 'Effective Date: 3/1/2014'. /ndrcivp index lists /ndrcivp/1 … links; no whole-set PDF.
- **Notes:** No full-set PDF seen, so no corpus candidate; per-rule pages are short.

## D. Administrative code

### `nd-admincode-ndlegis` — North Dakota Administrative Code (chapter PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** All titles; one PDF per chapter; updated quarterly (initially published July 1, 1978).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://ndlegis.gov/information/acdata/pdf/{title}-{article}-{chapter}.pdf`
  - Placeholders: Use the first three parts of the four-part cite exactly as written, decimals kept, no extra padding: 43-02-03-01 -> 43-02-03.pdf; 75-02-02-09 -> 75-02-02.pdf; 4.5-02.1-01 -> 4.5-02.1-01.pdf; 4-07-20.1 -> 4-07-20.1.pdf. Whole title placeholder: /acdata/pdf/title{N}.pdf. Grep the chapter text for '{section}. '.
  - Index: `https://ndlegis.gov/agency-rules/north-dakota-administrative-code/index.html`
  - Navigation: Index lists every title/article/chapter (chapter numbers, not section ranges).
- **Automation:** WebFetch untested · shell ok · robots: see nd-cencode-ndlegis
  - Long chapters (43-02-03: 82 pp, 293,996 chars) exceed the fetch tool window.
- **Currency:** none on index; each section ends with a 'History:' line; PDF last-modified header — observed: "History: Effective December 1, 1996; amended effective April 1, 2014; April 1, 2022."
- **Official status:** Index page: Legislative Council 'publishes the Administrative Code'; Internet version 'derived from the database prepared by' the Council. No official/authentication statement.
- **Hazard:** chapter-level PDFs, long ones exceed fetch window
- **Hazard:** no currency date on the index
- **Probe:** N.D. Admin. Code § 43-02-03-01 → `https://ndlegis.gov/information/acdata/pdf/43-02-03.pdf` — expect: "The terms used throughout this chapter have the same meaning as in North Dakota Century Code"
- **Evidence (2026-10-17):** fetch_doc.py: 43-02-03.pdf 82 pp (last-modified 2026-10-05), grep '43-02-03-01. Definitions. The terms used throughout this chapter …'. 75-02-02.pdf 30 pp, section table lists 75-02-02-09 'Nursing Facility Level of Care'.

### `nd-admincode-lii` — Cornell LII - North Dakota Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles, per-section pages.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-{title}-{article}-{chapter}-{section}`
  - Placeholders: four-part cite verbatim after 'N-D-A-C-' (43-02-03-01 -> N-D-A-C-43-02-03-01). Hierarchy: /regulations/north-dakota/title-{t}/article-{t-a}/chapter-{t-a-c} (chapter page shows the section range).
  - Index: `https://www.law.cornell.edu/regulations/north-dakota`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * Crawl-delay 10; /regulations/ not disallowed
- **Currency:** 'Notes' block at foot of section — observed: "Amended by Administrative Rules Supplement 2016-362, October 2016"
- **Official status:** Third-party mirror; section notes cite Administrative Rules Supplements as the amendment source.
- **Hazard:** crawl-delay 10
- **Hazard:** lag behind quarterly supplements unknown
- **Probe:** N.D. Admin. Code § 43-02-03-01 → `https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-43-02-03-01` — expect: "The terms used throughout this chapter have the same meaning as in North Dakota Century Code"
- **Evidence (2026-10-17):** fetch_doc.py grep: body 'The terms used throughout this chapter have the same meaning …' at offset 1680; Notes list Supplements 2014-352, 2016-362, 368. Second: N-D-A-C-75-02-02-09 'Nursing facility level of care' page present.

## D. Administrative register

### `nd-admin-supplements-ndlegis` — North Dakota Administrative Rules Supplements

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Quarterly supplements of amended rule text (Supplement 401, October 2026, back through earlier numbers on the page). North Dakota has no separate register of proposed rules on this site.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://ndlegis.gov/admcode/arc{YYYYMM}{number}.pdf`
  - Placeholders: File name = 'arc' + year + 2-digit month + supplement number (Supplement 401 Oct 2026 -> arc202610401.pdf; 398 Jan 2026 -> arc202601398.pdf). Month must come from the index.
  - Index: `https://ndlegis.gov/administrative-rules-supplements`
  - Navigation: supplements page -> 'Supplement NNN' link -> PDF
- **Automation:** WebFetch untested · shell ok · robots: see nd-cencode-ndlegis
  - Supplement 401 is 181 pp, 549,686 chars.
- **Currency:** supplements page list — observed: "Supplement 401 (October 2026)"
- **Official status:** Quarterly supplements of rule changes 'submitted to the Legislative Council by agencies'; no authentication statement.
- **Hazard:** very long PDFs
- **Hazard:** file name needs the month
- **Probe:** Administrative Rules Supplement 401 → `https://ndlegis.gov/admcode/arc202610401.pdf` — expect: "ARTICLE 33-41 TATTOO AND BODY ART"
- **Evidence (2026-10-17):** fetch_doc.py: arc202610401.pdf 181 pp, starts 'OCTOBER 2026 … ARTICLE 33-41 TATTOO AND BODY ART', chapter 33-41-01 '[Repealed effective October 1, 2026]'.

## E. Case law

### `nd-opinions-ndcourts` — North Dakota Supreme Court Opinions

- **Status:** REPORTED 2026-10-17 · **Tier 1** · North Dakota Supreme Court · text: **link-only** · official: unknown
- **Coverage:** About 12,400 entries (Oct 2026), newest first, 10 per page; page 596 of 1214 held 2002 opinions, so the listing reaches well before 1997. Each row: case name, 'YYYY ND N', docket number, filed date. Includes temporary Court of Appeals opinions ('ND App', per memory, unverified).
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.ndcourts.gov/supreme-court/opinions/{id}`
  - Placeholders: Opinion pages use an internal numeric id (2026 ND 97 -> /supreme-court/opinions/210815), not derivable from the citation. Listing: /supreme-court/opinions?page={n}. Docket pages: /supreme-court/dockets/{docket} (seen as /Dockets/20220121). A GET search by citation was not tested.
  - Index: `https://www.ndcourts.gov/supreme-court/opinions`
  - Navigation: listing ?page=N (newest first) or the 'New opinion(s)' news post for the filing date (/news/north-dakota/north-dakota-supreme-court/opinions/…) -> opinion link /supreme-court/opinions/{id}. The fetch tool's text omits the hrefs on listing pages; news posts give them.
- **Automation:** WebFetch gated · shell blocked-challenge · robots: none (robots.txt serves the custom error page)
  - fetch_doc.py: HTTP 403 Cloudflare challenge. WebFetch read listing and news pages from search results, but /supreme-court/opinions/210815, /supreme-court/opinion/2023ND32 and /supreme-court/Dockets/20220121 were PROVENANCE_REQUIRED. Opinion body text was never seen.
- **Currency:** listing counter — observed: "681 - 690 of 12446 results"
- **Official status:** Listing shows no official-status statement; the public-domain cite 'YYYY ND N' with ¶ numbers is the court's own citation form (N.D.R.Ct. 11.6), so pinpoints to ¶ are official-equivalent.
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** opinion pages gated for WebFetch
- **Hazard:** id-based opinion URLs
- **Hazard:** listing text lacks hrefs in WebFetch
- **Probe:** City of Bismarck v. Herrera, 2026 ND 97 → `https://www.ndcourts.gov/supreme-court/opinions/210815`
- **Evidence (2026-10-17):** WebFetch: news post new-opinions-may-7-2026 lists 2026 ND 91-99 with /supreme-court/opinions/2108xx links; listing ?page=52 '2023 ND 171 Berger v. Sellers, Docket No. 20220322'. Opinion page itself PROVENANCE_REQUIRED; script REFUSED (Cloudflare 403).
- **Notes:** Use nd-cases-justia to read text until an opinion page can be fetched.

### `nd-reports-library` — North Dakota Reports (Reports of Cases), scanned volumes

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · North Dakota State Library · text: **fetch-and-quote** · official: official
- **Coverage:** North Dakota Reports, one PDF per volume (v1, v17, v48, v79 confirmed present by fetch_doc.py check/info); 1890-1953 per memory.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.library.nd.gov/statedocs/SupremeCourt/ReportsofCases/v{volume}.pdf`
  - Placeholders: volume = unpadded N.D. volume number (48 N.D. 722 -> v48.pdf). Find the case by grepping its running head (case name in capitals, e.g. 'ANDERSON v. CITY OF FARGO'), which is followed by the official page number; PDF page differs from reporter page (48 N.D. 723 is PDF p. 745).
  - Index: `https://www.library.nd.gov/statedocs/SupremeCourt/ReportsofCases/`
- **Automation:** WebFetch untested · shell ok · robots: Drupal default (Disallow /core/, /admin/ ...); /statedocs/ permitted
  - Volumes are huge (v48: 1,430 pp, 2,865,257 chars), far beyond the fetch tool window; script grep/section only. Index URL not fetched.
- **Currency:** n/a (closed historical reporter)
- **Official status:** Scans of the official reporter (Reports of Cases in the Supreme Court of North Dakota) with official page numbers in the running heads.
- **Hazard:** OCR text errors
- **Hazard:** very large PDFs
- **Hazard:** PDF page differs from reporter page
- **Probe:** Anderson v. City of Fargo, 48 N.D. 722, 186 N.W. 378 (1922) → `https://www.library.nd.gov/statedocs/SupremeCourt/ReportsofCases/v48.pdf` — expect: "ANDERSON v. CITY OF FARGO 723 Order affirmed"
- **Evidence (2026-10-17):** fetch_doc.py: v48.pdf 1,430 pp; grep 'Anderson v. City of Fargo' at PDF pp. 745-749 with running heads 723, 725, 727. v17.pdf 771 pp, table of cases '17 N. D. 302'. v17 URL came from a WebSearch result.
- **Notes:** Official pagination for pre-1953 cases is free here; modern opinions have only ¶ numbers (public-domain cite) and West N.W.2d/N.W.3d pages.

### `nd-cases-justia` — Justia - North Dakota Supreme Court decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** North Dakota Supreme Court year listings (2023 and 2024 seen); Court of Appeals listing not checked.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/north-dakota/supreme-court/{year}/{docket}.html`
  - Placeholders: year = decision year; docket = 8-digit ND docket number (2023 ND 32 -> 20220121). The 'YYYY ND N' cite does not give the docket: get it from the year listing https://law.justia.com/cases/north-dakota/supreme-court/{year}/ or the ndcourts listing. A second opinion on one docket gets a suffix (20230034-0.html).
  - Index: `https://law.justia.com/cases/north-dakota/supreme-court/`
  - Navigation: year listing -> docket link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (script refused, robots.txt challenge)
- **Currency:** none
- **Official status:** Justia notes metadata is AI-assisted.
- **Hazard:** docket needed for URL
- **Hazard:** suffixed slugs on shared dockets
- **Hazard:** shell blocked
- **Hazard:** N.W.2d page numbers not shown
- **Probe:** Queen v. Martel, 2023 ND 32 → `https://law.justia.com/cases/north-dakota/supreme-court/2023/20220121.html` — expect: "Lee Queen appealed from a judgment awarding him and Kimber Martel equal residential responsibility"
- **Evidence (2026-10-17):** WebFetch: YES, [¶1]-[¶5] present, complete, header '2023 ND 32'. 2023 listing: Berger v. Sellers (2023 ND 171) -> /2023/20220322.html.

## F. Subsequent history

### `nd-docket-ndcourts` — North Dakota Supreme Court dockets / Appellate Case System

- **Status:** REPORTED 2026-10-17 · **Tier 1** · North Dakota Supreme Court · text: **link-only** · official: unknown
- **Coverage:** The Supreme Court is the only standing appellate court (temporary Court of Appeals hears assigned cases; the Supreme Court may review). Rehearing petitions (N.D.R.App.P. 40) appear on the case docket. Appellate Case System live April 8, 2024; historical data may be incomplete.
- **Access:** `link-only` · format html
  - Pattern: `https://www.ndcourts.gov/supreme-court/dockets/{docket}`
  - Placeholders: docket = 8-digit number shown on the opinion listing (Queen v. Martel -> 20220121, link seen in a news post). Search UI: https://www.ndcourts.gov/supreme-court/docket-search (case, party, calendar, document, publication search).
  - Index: `https://www.ndcourts.gov/supreme-court/docket-search`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: none (custom error page)
  - Docket page /supreme-court/Dockets/20220121 was PROVENANCE_REQUIRED; docket-search page read by WebFetch (from search result).
- **Currency:** none
- **Official status:** Docket search page: registration not required to search public appellate records.
- **Hazard:** docket page never read
- **Hazard:** shell blocked
- **Hazard:** pre-2024 history incomplete
- **Probe:** Queen v. Martel, 2023 ND 32 (No. 20220121) → `https://www.ndcourts.gov/supreme-court/Dockets/20220121`
- **Evidence (2026-10-17):** WebFetch docket-search page: 'You do not need to register to search public appellate records'; Appellate Case System live April 8, 2024. Docket page gated.

### `nd-scotus-docket` — U.S. Supreme Court docket (certiorari from the North Dakota Supreme Court)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of the United States · text: **fetch-and-quote** · official: official
- **Coverage:** Certiorari petitions and applications; docket shows 'Lower Ct: Supreme Court of North Dakota' and the ND docket number.
- **Read via (in order):** **script**
- **Access:** `search-only` · format html
  - Pattern: `https://www.supremecourt.gov/docket/docketfiles/html/public/{scotus_docket}.html`
  - Placeholders: Constructible only once the SCOTUS docket number is known (25-1349, 24A635). From an ND decision there is no link: WebSearch '"Supreme Court of North Dakota" <party> supremecourt.gov' or the 8-digit ND docket number; otherwise party name only.
  - Index: `https://www.supremecourt.gov/docket/docket.aspx`
- **Automation:** WebFetch untested · shell ok · robots: docket path allowed (fetch_doc.py ok)
- **Currency:** dated docket entries — observed: "Jun 17 2026 DISTRIBUTED for Conference of 9/28/2026."
- **Official status:** Docket kept by the Clerk of the Supreme Court.
- **Hazard:** party-name search only from the ND side
- **Probe:** Marschner v. Marschner, No. 25-1349 (from N.D. No. 20250066) → `https://www.supremecourt.gov/docket/docketfiles/html/public/25-1349.html` — expect: "Lower Ct: Supreme Court of North Dakota"
- **Evidence (2026-10-17):** fetch_doc.py: 25-1349 'Lower Ct: Supreme Court of North Dakota', 'Case Numbers: (20250066)', 'Decision Date: March 4, 2026', cert petition filed, response requested. 24A635: 'Case Numbers: (20240022)'.

## Not available (do not look for these again)

- **statutes** — public.law edition of North Dakota law: northdakota.public.law: proxy 'Tunnel connection failed: 502 Bad Gateway' (no such host), 2026-10-17. (2026-10-17)
- **statutes** — Cornell LII North Dakota Century Code / Constitution / opinions: https://www.law.cornell.edu/states/north_dakota links out to legis.nd.gov and ndcourts.gov; LII hosts only the ND Administrative Code. (2026-10-17)
- **statutes** — Official bulk download / API for the Century Code: Century Code index offers per-chapter PDFs and section listings only; no XML/zip link seen. (2026-10-17)

## Corpus candidates (maintainers)

- `nd-reports-library` — Official reporter volume, 1,430 pp OCR, about 2.9M chars; only script grep can reach a case. · bulk: one PDF per volume at /statedocs/SupremeCourt/ReportsofCases/v{N}.pdf
- `nd-cencode-ndlegis` — Business Corporation Act chapter: 95 pp, 394,274 chars, about four fetch-tool windows; WebFetch also gated on built ndlegis URLs.
- `nd-admincode-ndlegis` — Oil and gas conservation rules: 82 pp, 293,996 chars, beyond one fetch-tool window.

## Open questions

- ndcourts.gov opinion pages (/supreme-court/opinions/{id}): does WebFetch return body text and ¶ numbers once a URL is approved? Is there a plain GET search by citation or docket?
- Coverage start of the ndcourts.gov opinion listing (page 1214 of 1214 not fetched).
- Does Justia host ND Court of Appeals opinions (/cases/north-dakota/court-of-appeals/) and ND court rules?
- Rules of Professional Conduct URL form (ndrprofconduct/1-7) not fetched.
- WebFetch on ndlegis.gov constitution and admin-code PDFs untested (expected gated like cencode).

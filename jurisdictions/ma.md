# Massachusetts (MA) — free legal sources

_Generated from `data/ma.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: malegislature.gov General Laws (unofficial) are constructible from chapter and section alone, because /Laws/GeneralLaws/Chapter{c}/Section{s} redirects to the Part/Title URL. A public JSON API (/api/Chapters/{c}/Sections/{s}) returns the same text, and Justia 2025 is the tier-2 fallback. The Constitution is a single 357K-character page that WebFetch cannot read past the early Amendments; fetch_doc.py reads all of it. Court rules and the Guide to Evidence have per-rule pages on mass.gov (index-anchored slugs that drop the decimal point) plus full-set PDFs (corpus candidates). CMR chapters are mass.gov PDFs (unofficial), with LII as a constructible tier-2 source. Case law: mass.gov carries only recent slip opinions; 128archive.com (Reporter of Decisions) has a GET search of Rule 23.0 decisions since 2008; Justia is the free route for older opinions. No free official Mass. Reports pagination exists. The FAR docket host (ma-appellatecourts.org) refuses automated access.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Judicial Court of Massachusetts | `mass (unverified)` | Mass. | Mass., N.E.3d, N.E.2d, N.E. | — |
| Massachusetts Appeals Court | `massappct (unverified)` | Mass. App. Ct. | Mass. App. Ct., N.E.3d, N.E.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Massachusetts General Laws | `G. L. c. 93A, § 9`; `G.L. c. 93A, § 9(3)`; `M.G.L. c. 231, § 85`; `MGL c. 151B § 4`; `Mass. Gen. Laws ch. 93A, § 9`; `Mass. Gen. Laws Ann. ch. 265, § 13A`; `ALM GL ch. 149, § 148`; `G. L. c. 231, §§ 60B-60E`; `section 9 of chapter 93A of the General Laws`; `chapter 231, section 85 of the General Laws` | `ma-gl-malegislature` → `ma-gl-api` → `ma-gl-justia` |
| Massachusetts Session Laws (Acts / St.) | `St. 2016, c. 219, § 35`; `Acts 2024, c. 150`; `Acts of 2016, chapter 219`; `St. 1973, c. 1114` | `ma-session-laws` |
| Massachusetts Constitution | `Mass. Const. art. 89`; `Mass. Const. pt. 1, art. 14`; `Mass. Const. amend. art. 48`; `art. 12 of the Massachusetts Declaration of Rights`; `art. 89 of the Amendments to the Massachusetts Constitution`; `Part the First, Article XIV of the Massachusetts Constitution` | `ma-constitution-malegislature` → `ma-constitution-justia` |
| Massachusetts Rules of Civil Procedure | `Mass. R. Civ. P. 12(b)(6)`; `Mass.R.Civ.P. 56`; `Mass. R. Civ. P. 23.1`; `Rule 12(b)(6) of the Massachusetts Rules of Civil Procedure` | `ma-rules-civil` → `ma-rules-civil-pdf` |
| Massachusetts Rules of Criminal Procedure | `Mass. R. Crim. P. 14(a)(1)`; `Mass.R.Crim.P. 30(b)`; `Rule 14 of the Massachusetts Rules of Criminal Procedure` | `ma-rules-criminal` |
| Massachusetts Rules of Appellate Procedure | `Mass. R. A. P. 27.1`; `Mass. R. App. P. 16(a)(9)`; `Mass.R.A.P. 11`; `Rule 27.1 of the Massachusetts Rules of Appellate Procedure` | `ma-rules-appellate` |
| Rules of the Supreme Judicial Court (incl. Rules of Professional Conduct, SJC Rule 3:07) | `S.J.C. Rule 1:03`; `SJC Rule 3:07`; `Mass. R. Prof. C. 1.7`; `Rule 1:21 of the Supreme Judicial Court` | `ma-rules-sjc` → `ma-rules-sjc-pdf` |
| Appeals Court Rules (incl. Rule 23.0, formerly 1:28) | `Appeals Court Rule 23.0`; `Mass. App. Ct. R. 23.0`; `M.A.C. Rule 23.0`; `Appeals Court Rule 1:28`; `decided under rule 1:28` | `ma-rules-appeals-court` |
| Superior Court Rules | `Superior Court Rule 9A`; `Super. Ct. R. 9A`; `Rule 9A of the Rules of the Superior Court` | `ma-rules-superior` |
| Massachusetts Guide to Evidence | `Mass. G. Evid. § 803(6)(A)`; `Mass. Guide Evid. § 1119`; `Section 803 of the Massachusetts Guide to Evidence` | `ma-guide-evidence` → `ma-guide-evidence-pdf` |
| Code of Massachusetts Regulations | `940 CMR 3.16`; `940 C.M.R. 3.16(1)`; `310 Code Mass. Regs. § 10.02`; `940 CMR 3.00` | `ma-cmr-massgov` → `ma-cmr-lii` |
| Massachusetts Register | `Mass. Register #1420`; `Mass. Reg. No. 1337`; `Massachusetts Register Issue 1475` | `ma-register-statelib` → `ma-register-sos` |
| Massachusetts Reports / Appeals Court Reports / N.E. with Mass. parenthetical | `Commonwealth v. Goncalves, 497 Mass. 1 (2026)`; `Iannacchino v. Ford Motor Co., 451 Mass. 623 (2008)`; `100 Mass. App. Ct. 1101 (2021)`; `888 N.E.2d 879 (Mass. 2008)`; `200 N.E.3d 12 (Mass. App. Ct. 2022)`; `Commonwealth v. Doe, 100 Mass. App. Ct. 1101 (2021) (Rule 23.0 decision)` | `ma-cases-justia` → `ma-opinions-massgov` → `ma-rule23-128archive` |
| Massachusetts appellate docket numbers (SJC-, FAR-, YY-P-, YY-J-) | `SJC-13880`; `FAR-30123`; `No. 25-P-0254`; `2025-P-0383`; `No. 24-J-0101` | `ma-opinions-massgov` → `ma-rule23-128archive` → `ma-cases-justia` |
| Further appellate review dispositions | `further appellate review denied, 491 Mass. 1102 (2023)`; `further appellate review granted, 489 Mass. 1104 (2022)` | `ma-docket-appellatecourts` → `ma-far-lists-massgov` |

Regexes (case-insensitive):

- Massachusetts General Laws: `(?:(?:M\.\s?G\.\s?L\.?|MGL|G\.\s?L\.|ALM\s+GL|Mass\.\s*Gen\.\s*Laws(?:\s+Ann\.)?|Mass\.\s*Ann\.\s*Laws)\s*(?:c|ch|chapter)\.?\s*(?P<chapter>\d{1,3}[A-Z]{0,2})\s*,?\s*(?:§§?|s\.|sec(?:tion|\.)?)\s*(?P<section>\d{1,3}[A-Z]{0,3}(?:½|1/2)?)|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,3}[A-Z]{0,3})(?:\([a-z0-9]+\))*\s+of\s+chapter\s+(?P<chapter2>\d{1,3}[A-Z]{0,2})\s+of\s+the\s+(?:Massachusetts\s+)?General\s+Laws|chapter\s+(?P<chapter3>\d{1,3}[A-Z]{0,2}),?\s+(?:sec(?:tion|\.)|§)\s*(?P<section3>\d{1,3}[A-Z]{0,3})\s+of\s+the\s+(?:Massachusetts\s+)?General\s+Laws)`
- Massachusetts Session Laws (Acts / St.): `(?:\bSt\.|\bStat\.|\bActs\s+(?:of\s+)?)\s*(?P<year>1[6-9]\d{2}|20\d{2}),?\s*(?:c\.|ch\.|chapter)\s*(?P<chapter>\d+)`
- Massachusetts Constitution: `Mass\.\s*Const\.\s*(?:pt\.\s*(?P<part>1|2|I{1,2}),?\s*)?(?:(?:c\.|ch\.)\s*(?P<chapter>[0-9IVX]+),?\s*(?:§\s*(?P<csection>[0-9IVX]+),?\s*)?)?(?:amend\.\s*)?art\.\s*(?P<article>[0-9IVXLC]+)|art(?:icle|\.)?\s*(?P<article2>[0-9IVXLC]+)\s+of\s+the\s+Massachusetts\s+Declaration\s+of\s+Rights|art(?:icle|\.)?\s*(?P<article3>[0-9IVXLC]+)\s+of\s+the\s+Amendments\s+to\s+the\s+Massachusetts\s+Constitution|Part\s+the\s+First,?\s+Article\s+(?P<article4>[IVXLC]+)\s+of\s+the\s+Massachusetts\s+Constitution`
- Massachusetts Rules of Civil Procedure: `Mass\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Massachusetts\s+Rules\s+of\s+Civil\s+Procedure`
- Massachusetts Rules of Criminal Procedure: `Mass\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Massachusetts\s+Rules\s+of\s+Criminal\s+Procedure`
- Massachusetts Rules of Appellate Procedure: `Mass\.\s*R\.\s*A(?:pp)?\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Massachusetts\s+Rules\s+of\s+Appellate\s+Procedure`
- Rules of the Supreme Judicial Court (incl. Rules of Professional Conduct, SJC Rule 3:07): `(?:S\.\s?J\.\s?C\.|SJC|Supreme\s+Judicial\s+Court)\s+Rule\s+(?P<rule>\d:\d{2}[A-Z]?)|Mass\.\s*R\.\s*Prof\.\s*C(?:onduct)?\.\s*(?P<rpc>\d\.\d{1,2})|Rule\s+(?P<rule2>\d:\d{2}[A-Z]?)\s+of\s+the\s+(?:Rules\s+of\s+the\s+)?Supreme\s+Judicial\s+Court`
- Appeals Court Rules (incl. Rule 23.0, formerly 1:28): `(?:Mass\.\s*App\.\s*Ct\.\s*R\.|Appeals\s+Court\s+Rule|M\.A\.C\.\s+Rule)\s*(?P<rule>\d{1,2}\.\d|1:\d{2})|(?:rule|Rule)\s+(?P<rule2>1:28|23\.0)\b`
- Superior Court Rules: `(?:Super(?:ior)?\.?\s*Ct\.?\s*R(?:ule)?\.?|Superior\s+Court\s+Rule)\s*(?P<rule>\d{1,2}[A-Z]?)|Rule\s+(?P<rule2>\d{1,2}[A-Z]?)\s+of\s+the\s+(?:Rules\s+of\s+the\s+)?Superior\s+Court(?:\s+Rules)?`
- Massachusetts Guide to Evidence: `Mass\.\s*G(?:uide|\.)\s*Evid\.\s*§\s*(?P<section>\d{3,4})|(?:Section|§)\s*(?P<section2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Massachusetts\s+Guide\s+to\s+Evidence`
- Code of Massachusetts Regulations: `(?P<title>\d{3})\s*(?:CMR|C\.M\.R\.|Code\s+Mass\.\s+Regs\.)\s*(?:§\s*)?(?P<part>\d{1,3})\.(?P<section>\d{2,3})`
- Massachusetts Register: `(?:Mass\.|Massachusetts)\s*Reg(?:ister|\.)\s*(?:#|No\.\s*|Issue\s*)\s*(?P<issue>\d{3,4})`
- Massachusetts Reports / Appeals Court Reports / N.E. with Mass. parenthetical: `(?P<volume>\d{1,3})\s+Mass\.\s+(?!App\.\s*D)(?P<app>App\.\s+Ct\.\s+)?(?P<page>\d{1,4})\b|(?P<nevol>\d{1,3})\s+N\.E\.(?:2d|3d)?\s+(?P<nepage>\d{1,4})(?:,\s*\d+)?\s*\((?P<ct>Mass\.(?:\s+App\.(?:\s+Ct\.)?)?)\s*\d{4}\)`
- Massachusetts appellate docket numbers (SJC-, FAR-, YY-P-, YY-J-): `\b(?P<sjc>SJC-\d{4,5})\b|\b(?P<far>FAR-\d{4,5})\b|\b(?P<ac>(?:19|20)?\d{2}-[PJ]-\d{1,4})\b`
- Further appellate review dispositions: `further\s+appellate\s+review\s+(?P<disp>denied|granted|allowed)(?:,\s*(?P<volume>\d{1,3})\s+Mass\.\s+(?P<page>\d{1,4}))?`

Short forms → URL key:

G. L. → `General Laws`; G.L. → `General Laws`; M.G.L. → `General Laws`; MGL → `General Laws`; Mass. Gen. Laws → `General Laws`; Mass. Gen. Laws Ann. → `General Laws`; ALM GL → `General Laws`; Mass. Ann. Laws → `General Laws`; Chapter 93A → `93A`; Consumer Protection Act → `93A`; Wage Act → `149 § 148`; Massachusetts Civil Rights Act → `12 § 11I`; MCRA → `12 § 11I`; Massachusetts Tort Claims Act → `258`; MTCA → `258`; anti-SLAPP statute → `231 § 59H`; Chapter 151B → `151B`; Chapter 40B → `40B`; Open Meeting Law → `30A § 18`; Public Records Law → `66 § 10`; Comparative negligence statute → `231 § 85`; Mass. R. Civ. P. → `ma-rules-civil`; Mass. R. Crim. P. → `ma-rules-criminal`; Mass. R. A. P. → `ma-rules-appellate`; Mass. R. App. P. → `ma-rules-appellate`; S.J.C. Rule → `ma-rules-sjc`; Mass. R. Prof. C. → `ma-rules-sjc (Rule 3:07)`; Appeals Court Rule → `ma-rules-appeals-court`; M.A.C. Rule → `ma-rules-appeals-court`; Rule 1:28 → `Appeals Court Rule 23.0`; Super. Ct. R. → `ma-rules-superior`; Mass. G. Evid. → `ma-guide-evidence`; Mass. Guide Evid. → `ma-guide-evidence`; CMR → `Code of Massachusetts Regulations`; C.M.R. → `Code of Massachusetts Regulations`; Code Mass. Regs. → `Code of Massachusetts Regulations`

Massachusetts style (SJC Style Manual) cites 'G. L. c. 93A, § 9', 'St. 2016, c. 219, § 35', 'art. 14 of the Massachusetts Declaration of Rights' / 'art. 89 of the Amendments' (Arabic numerals; the legislature's anchors use Roman), 'Mass. R. Civ. P. 12 (b) (6)' (space before subdivision parentheses), 'Mass. G. Evid. § 803(6)(A)', '940 CMR 3.16'. Bluebook: 'Mass. Gen. Laws ch. 93A, § 9', 'Mass. Const. pt. 1, art. 14', 'Mass. Const. amend. art. 89', '940 Mass. Code Regs. 3.16'. ALM GL is the LexisNexis annotated code. No public-domain citation; Mass. and Mass. App. Ct. are official (LexisNexis), N.E. is West. Rule 23.0 (formerly 1:28) summary decisions are cited by case name, the Mass. App. Ct. table page where noted (pages 1101+), and a Rule 23.0 / 1:28 notation; those issued before Feb. 26, 2008 may not be cited. FAR is cited 'further appellate review denied, 491 Mass. 1102 (2023)' (table pages 1101+). Routing guards: bare 'c. 93A' or 'chapter 93A' without G.L./General Laws, bare 'Rule 12', bare 'Declaration of Rights' (also Maryland, New Hampshire) and bare 'N.E.2d/3d' (also IL, IN, NY, OH) must not route here without a Massachusetts marker; the N.E. regex requires a '(Mass.' or '(Mass. App. Ct.' parenthetical. 'Mass. App. Div.' and 'Mass. App. Dec.' (District Court Appellate Division) are excluded from the case regex. Docket numbers: SJC-NNNNN, FAR-NNNNN, YY-P-NNNN (panel) and YY-J-NNNN (single justice); route on dockets only with Massachusetts context. Section ranges '§§ 60B-60E' are spans: the regex takes the first section (MA section numbers never contain hyphens). law_aliases maps popular names to chapter/section from memory (unverified) and rule abbreviations to source ids. CourtListener ids from memory, unverified.

## A. Statutes / code

### `ma-gl-api` — Massachusetts Legislature public API - General Laws and Session Laws (JSON)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · The General Court of the Commonwealth of Massachusetts · text: **fetch-and-quote** · official: unofficial
- **Coverage:** GET /api/Parts, /api/Chapters, /api/Chapters/{chapter}, /api/Chapters/{chapter}/Sections/{section} (Code, Name, IsRepealed, Text, Part/Title links); /api/SessionLaws (all acts with ChapterText, 3.3M chars); /api/Documents (bills).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format json
  - Pattern: `https://malegislature.gov/api/Chapters/{chapter}/Sections/{section}`
  - Placeholders: Same chapter/section tokens as the HTML route (93A, 13A). No key required. Response is JSON; 'Text' holds the whole section starting 'Section N.'. Verified for c.93A s.9, c.231 s.85, c.265 s.13A.
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * / Disallow: (empty)
  - No Swagger page at /api/swagger/ui/index (404); /api/Constitution 404. /api/SessionLaws and /api/Documents are multi-MB - avoid with WebFetch.
- **Currency:** none in JSON; see General Laws landing page
- **Official status:** Same data as the malegislature.gov General Laws pages, which carry the 'NOT the official version' notice.
- **Hazard:** JSON text has no paragraph markup beyond newlines
- **Hazard:** bulk endpoints are very large
- **Probe:** G. L. c. 231, § 85 → `https://malegislature.gov/api/Chapters/231/Sections/85` — expect: "Section 85. Contributory negligence shall not bar recovery in any action"
- **Evidence (2026-10-16):** WebFetch YES: Text begins 'Section 85. Contributory negligence shall not bar recovery in any action'. fetch_doc.py: /api/Chapters/93A/Sections/9 JSON 'Text':'Section 9. (1) Any person, other than a person entitled'; /api/Parts lists I-V.
- **Notes:** Best script route for statutes: deterministic, no HTML chrome.

### `ma-gl-malegislature` — General Laws of Massachusetts (malegislature.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · The General Court of the Commonwealth of Massachusetts · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All chapters of the General Laws (Parts I-V), section by section; amendments passed before May 31, 2026 per landing-page notice.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://malegislature.gov/Laws/GeneralLaws/Chapter{chapter}/Section{section}`
  - Placeholders: chapter and section exactly as cited, letters upper-case (93A, 151B; 13A, 60B, 11I); lower-case is accepted (Chapter93a redirects). The short form redirects to the canonical /Laws/GeneralLaws/Part{I-V}/Title{roman}/Chapter{chapter}/Section{section} URL, so Part/Title need not be known (verified: c.93A s.9 -> PartI/TitleXV; c.231 s.85 -> PartIII/TitleII; c.151B s.4 -> PartI/TitleXXI; c.265 s.13A -> PartIV/TitleI; c.12 s.11I -> PartI/TitleII; c.149 s.148 -> PartI/TitleXXI). A non-existent section returns HTTP 404 (Chapter93A/Section99), not a soft page. Chapter page without section: /Laws/GeneralLaws/Chapter{chapter} (redirects to the chapter's section list). A section range '§§ 60B-60E' is a span: fetch the first section, then each one.
  - Index: `https://malegislature.gov/Laws/GeneralLaws`
  - Navigation: Not needed (short URL redirects). If a redirect ever fails: /Laws/GeneralLaws -> Part{I..V} page lists Titles WITH chapter ranges (e.g. 'Title XV ... Chapters 93 - 110H') -> Title page -> Chapter page -> Section link.
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * / Disallow: (empty) - everything allowed
  - Section pages are ~13K chars of site chrome plus the section text; body follows 'Print Page Previous Next'. Largest probed (c.151B s.4) 71,576 chars in total, under the WebFetch window. Page header shows today's date and weather (not a currency line).
- **Currency:** General Laws landing page (https://malegislature.gov/Laws/GeneralLaws) notice paragraph; nothing on section pages — observed: "includes all amendments to the General Laws passed before May 31, 2026"
- **Official status:** https://malegislature.gov/Laws/GeneralLaws: 'NOTICE: This is NOT the official version of the General Laws of Massachusetts' ... check the Official Edition (printed every two years).
- **Hazard:** unofficial text - Official Edition is the printed General Laws
- **Hazard:** later amendments (after the stated cut-off) only in Session Laws
- **Hazard:** site header date/weather can be mistaken for a currency statement
- **Hazard:** repealed or renumbered sections: check the section heading and 'IsRepealed' in the API
- **Probe:** G. L. c. 93A, § 9 → `https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A/Section9` — expect: "Any person, other than a person entitled to bring action under section eleven"
- **Evidence (2026-10-16):** WebFetch: YES, body '(1) Any person, other than a person entitled to bring'; complete through (8). Second: /Laws/GeneralLaws/Chapter231/Section85 YES 'Contributory negligence shall not bar recovery in any action by'. fetch_doc.py: both 200, short URLs redirect to Part/Title URLs.
- **Notes:** Constitution is at https://malegislature.gov/Laws/Constitution (see ma-constitution-malegislature). Same host serves a JSON API (ma-gl-api).

### `ma-session-laws` — Session Laws (Acts and Resolves) - malegislature.gov

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · The General Court of the Commonwealth of Massachusetts · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts and Resolves 1997-2026 per the site's year selector.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://malegislature.gov/Laws/SessionLaws/{type}/{year}/Chapter{chapter}`
  - Placeholders: type = Acts | Resolves; 'St. 2016, c. 219' and 'Acts 2016, c. 219' -> /Acts/2016/Chapter219. Earlier years not offered by the selector.
- **Automation:** WebFetch ok · shell ok · robots: everything allowed
  - Omnibus acts are long: Acts 2016 c.219 = 136K chars of text; WebFetch stopped at SECTION 35 (use offset=100000 or fetch_doc.py).
- **Currency:** none stated
- **Official status:** No disclaimer located on the chapter page; the General Laws notice does not address session laws.
- **Hazard:** WebFetch truncation on omnibus acts
- **Hazard:** pre-1997 acts not online here
- **Probe:** St. 2016, c. 219 → `https://malegislature.gov/Laws/SessionLaws/Acts/2016/Chapter219` — expect: "AN ACT RELATIVE TO JOB CREATION AND WORKFORCE DEVELOPMENT"
- **Evidence (2026-10-16):** WebFetch YES, body 'Whereas, The deferred operation of this act would tend to'; truncated at SECTION 35. fetch_doc.py: 241,114 chars, title 'AN ACT RELATIVE TO JOB CREATION AND WORKFORCE DEVELOPMENT'; also Acts 2024 c.150 200.
- **Notes:** Also in the JSON API: /api/SessionLaws.

### `ma-gl-justia` — Justia - Massachusetts General Laws

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 2025 edition (current) plus prior annual editions (2024, 2023 ...).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/massachusetts/part-{part}/title-{title}/chapter-{chapter}/section-{section}/`
  - Placeholders: part and title are lower-case Roman numerals (part-i, title-xv); chapter/section lower-case (chapter-93a). Part/Title are NOT derivable from the chapter: take them from the malegislature.gov redirect target (e.g. /PartIII/TitleII/Chapter231) and lower-case them. Prior editions: insert the year after /massachusetts/ (/codes/massachusetts/2024/part-i/...).
  - Index: `https://law.justia.com/codes/massachusetts/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com robots.txt answered with a bot challenge to fetch_doc.py (REFUSED)
  - WebFetch only.
- **Currency:** page heading — observed: "2025 Massachusetts General Laws"
- **Official status:** Page states 'Disclaimer: These codes may not be the most recent version.'
- **Hazard:** edition lags the legislature site (2025 edition)
- **Hazard:** shell route refused
- **Probe:** G. L. c. 93A, § 9 → `https://law.justia.com/codes/massachusetts/part-i/title-xv/chapter-93a/section-9/` — expect: "Any person, other than a person entitled to bring action"
- **Evidence (2026-10-16):** WebFetch YES '2025 Massachusetts General Laws'; body 'Any person, other than a person entitled to bring action'. Second: part-iii/title-ii/chapter-231/section-85 YES 'Contributory negligence shall not bar recovery in any action by'.

## B. Constitution

### `ma-constitution-malegislature` — Constitution of the Commonwealth of Massachusetts (malegislature.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · The General Court of the Commonwealth of Massachusetts · text: **fetch-and-quote** · official: unknown
- **Coverage:** Preamble; Part the First (Declaration of Rights, arts. I-XXX); Part the Second (Frame of Government); Articles of Amendment through CXXI.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://malegislature.gov/Laws/Constitution#{anchor}`
  - Placeholders: One page; anchors: Declaration of Rights art. N -> #article{ROMAN} (art. 14 -> #articleXIV); Articles of Amendment art. N -> #amendmentArticle{ROMAN} (art. 89 -> #amendmentArticleLXXXIX); Frame of Government -> #chapter{C}Section{S}Article{A} (e.g. #chapterISectionIArticleIV), #chapterVI ... Convert Arabic citation numbers ('art. 14 of the Declaration of Rights') to Roman. Anchor only scrolls: the fetch returns the whole page.
- **Automation:** WebFetch ok (truncated) · shell ok · robots: everything allowed
  - fetch_doc.py returns all 356,822 chars (Article CXXI present at offset ~318K). WebFetch sees ~118K chars: window 0-100K ends inside Articles of Amendment art. V; offset=100000 ends in art. XVI; amendments LXXXIX and CXXI NOT reachable by WebFetch.
- **Currency:** none stated
- **Official status:** No official/unofficial statement on the page.
- **Hazard:** single 357K-char page - WebFetch cannot reach most Articles of Amendment
- **Hazard:** citations use Arabic numerals, anchors use Roman
- **Hazard:** annulled/superseded amendment text is retained in the page
- **Probe:** Mass. Const. pt. 1, art. 14 → `https://malegislature.gov/Laws/Constitution` — expect: "Every subject has a right to be secure from all unreasonable searches"
- **Evidence (2026-10-16):** WebFetch: art. XIV YES 'Every subject has a right to be secure from all'; art. LXXXIX NOT PRESENT (truncated). fetch_doc.py grep: 'Article LXXXIX.' at offset 265906, 'Article CXXI.' at 318167.
- **Notes:** Corpus candidate (see corpus_candidates).

### `ma-constitution-justia` — Justia - Massachusetts Constitution

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **link-only** · official: unofficial
- **Coverage:** Whole constitution on one page with #fragment anchors.
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Pattern: `https://law.justia.com/constitution/massachusetts/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: bot challenge to fetch_doc.py
  - 130,293 chars; WebFetch window ends in Articles of Amendment art. IV.
- **Currency:** none stated
- **Official status:** Third-party compilation; no currency statement.
- **Hazard:** truncated by WebFetch
- **Hazard:** no currency statement
- **Probe:** Mass. Const. pt. 1, art. 14 → `https://law.justia.com/constitution/massachusetts/` — expect: "Every subject has a right to be secure from all"
- **Evidence (2026-10-16):** WebFetch: art. XIV YES 'Every subject has a right to be secure from all'; page truncated at Amendment art. IV; no currency line.
- **Notes:** Weaker than the tier-1 page; use only to locate.

## C. Court rules

### `ma-guide-evidence` — Massachusetts Guide to Evidence (per-section pages)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · SJC Advisory Committee on Massachusetts Evidence Law (mass.gov) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Sections 101-1121 with Notes; 2026 edition.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /guide-to-evidence/section-{N}-{title-slug} (803 -> section-803-hearsay-exceptions-availability-of-declarant-immaterial); take from the index (/guides/... redirects to /guide/...).
  - Index: `https://www.mass.gov/guide/massachusetts-guide-to-evidence`
  - Navigation: guide index -> section link -> section text then long Note
- **Automation:** WebFetch ok (truncated on long sections) · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - § 803 page = 95,435 chars (fetch_doc) / 102,958 (WebFetch): section text complete, Note cut off at (6)(C).
- **Currency:** section page 'Adopted Date'; index intro — observed: "Adopted Date: 02/01/2026 (2026 edition)"
- **Official status:** The Guide is a non-binding SJC committee compilation of Massachusetts evidence law (not rules adopted as such); annual editions.
- **Hazard:** long Notes truncated by WebFetch
- **Hazard:** Notes are commentary, not rule text
- **Hazard:** annual edition: cite the year
- **Probe:** Mass. G. Evid. § 803 → `https://www.mass.gov/guide-to-evidence/section-803-hearsay-exceptions-availability-of-declarant-immaterial` — expect: "The following are not excluded by the hearsay rule, even though the declarant"
- **Evidence (2026-10-16):** WebFetch YES 'The following are not excluded by the hearsay rule, even'; (18) present; Note truncated. fetch_doc.py 200, 95,435 chars.

### `ma-guide-evidence-pdf` — Massachusetts Guide to Evidence - 2026 edition PDF

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · SJC Advisory Committee on Massachusetts Evidence Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole 2026 edition, 446 pp.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.mass.gov/doc/massachusetts-guide-to-evidence-2026-edition/download`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 1,463,018 chars; WebFetch stops in the Note to § 202; § 803 at PDF page 262 (fetch_doc grep).
- **Currency:** PDF cover — observed: "MASSACHUSETTS GUIDE TO EVIDENCE 2026 Edition"
- **Official status:** Committee guide; see ma-guide-evidence.
- **Hazard:** WebFetch truncation (Article II of XI)
- **Hazard:** URL slug changes each edition (...-2026-edition)
- **Probe:** Mass. G. Evid. § 803 → `https://www.mass.gov/doc/massachusetts-guide-to-evidence-2026-edition/download` — expect: "Section 803. Hearsay Exceptions; Availability of Declarant Immaterial"
- **Evidence (2026-10-16):** fetch_doc.py: PDF 446 pp, jud-sjc-Massachusetts-Guide-to-Evidence-2026.pdf; 'Section 803. Hearsay Exceptions' at page 262. WebFetch: '2026 Edition'; § 104 YES; § 803 NOT PRESENT.
- **Notes:** Corpus candidate.

### `ma-rules-appeals-court` — Rules of the Appeals Court (per-rule pages), incl. Rule 23.0 (formerly 1:28)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of the Appeals Court (per-rule pages), incl. Rule 23.0 (formerly 1:28)
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /appeals-court-rules/appeals-court-rule-{N without dot}-{title-slug}: 23.0 -> appeals-court-rule-230-summary-disposition-formerly-known-as-appeals-court-rule-128; 1.0 -> rule-10. Full set PDF: https://www.mass.gov/doc/appeals-court-rules/download (23 pp, July 2024).
  - Index: `https://www.mass.gov/law-library/massachusetts-appeals-court-rules`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' line — observed: "Effective Date: 07/01/2020"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** 'rule-230' slug for 23.0 and 'rule-10' for 1.0
- **Probe:** Appeals Court Rule 23.0 → `https://www.mass.gov/appeals-court-rules/appeals-court-rule-230-summary-disposition-formerly-known-as-appeals-court-rule-128` — expect: "a panel of the justices of this court may determine that no substantial question"
- **Evidence (2026-10-16):** fetch_doc.py 200, 13,703 chars: '(1) Summary disposition without oral argument'; '(2) Citation of summary dispositions'; 'Effective Date: 07/01/2020'.

### `ma-rules-appellate` — Massachusetts Rules of Appellate Procedure (per-rule pages)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Massachusetts Rules of Appellate Procedure (per-rule pages)
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /rules-of-appellate-procedure/appellate-procedure-rule-{N without dot}-{title-slug}; 27.1 -> rule-271-further-appellate-review; 11.1 -> rule-111.
  - Index: `https://www.mass.gov/law-library/massachusetts-rules-of-appellate-procedure`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' line — observed: "Effective Date: 09/01/2021"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** slug drops the decimal point or colon: Rule 23.1 -> 'rule-231', 4.1 -> 'rule-41' (collides with Rule 41)
- **Probe:** Mass. R. A. P. 27.1 → `https://www.mass.gov/rules-of-appellate-procedure/appellate-procedure-rule-271-further-appellate-review` — expect: "Appellate Procedure Rule 27.1: Further appellate review"
- **Evidence (2026-10-16):** fetch_doc.py 200: 'Appellate Procedure Rule 27.1: Further appellate review Effective Date: 09/01/2021'. WebFetch not run.

### `ma-rules-civil` — Massachusetts Rules of Civil Procedure (per-rule pages)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Massachusetts Rules of Civil Procedure (per-rule pages)
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs are /rules-of-civil-procedure/civil-procedure-rule-{N without dot}-{title-slug}; not constructible (title in slug). Decimal dropped: 23.1 -> rule-231, 55.1 -> rule-551, 65.3 -> rule-653. COLLISIONS: Rule 4.1 and Rule 41 both 'rule-41-...' (attachment vs dismissal of actions); 4.2/42 (trustee process vs consolidation); 4.3/43 (arrest vs evidence); 8.1/81 (consumer debts vs applicability) - pick by title. Rule 11 has two pages: effective-until-january-1-2027 and effective-january-1-2027.
  - Index: `https://www.mass.gov/law-library/massachusetts-rules-of-civil-procedure`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' and 'Updates' lines — observed: "Effective Date: 07/01/2008"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** slug drops the decimal point or colon: Rule 23.1 -> 'rule-231', 4.1 -> 'rule-41' (collides with Rule 41)
- **Hazard:** two versions of Rule 11 (amendment effective Jan. 1, 2027)
- **Hazard:** Reporter's Notes on the same page are not rule text
- **Probe:** Mass. R. Civ. P. 12(b)(6) → `https://www.mass.gov/rules-of-civil-procedure/civil-procedure-rule-12-defenses-and-objections-when-and-how-presented-by-pleading-or-motion-motion-for-judgment-on-pleadings` — expect: "After service upon him of any pleading requiring a responsive pleading"
- **Evidence (2026-10-16):** WebFetch YES, (a) 'After service upon him of any pleading requiring a responsive'; (a)-(h) complete; Reporter's Notes 2008/1973; 'Effective Date: 07/01/2008'. fetch_doc.py 200, 36,154 chars.

### `ma-rules-civil-pdf` — Massachusetts Rules of Civil Procedure - full-set PDF

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries · text: **fetch-and-quote** · official: unknown
- **Coverage:** All rules with Reporter's Notes, 271 pp.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.mass.gov/doc/massachusetts-rules-of-civil-procedure/download`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 827,883 chars; WebFetch stops in Rule 6(b).
- **Currency:** PDF cover — observed: "Including amendments effective March 10, 2025"
- **Official status:** No statement in PDF front matter.
- **Hazard:** WebFetch truncation (Rule 6 of 85)
- **Hazard:** edition can lag the per-rule pages (March 2025)
- **Probe:** Mass. R. Civ. P. 12 → `https://www.mass.gov/doc/massachusetts-rules-of-civil-procedure/download` — expect: "Including amendments effective March 10, 2025"
- **Evidence (2026-10-16):** fetch_doc.py: PDF 271 pp, filename jud-lib-rules-of-civil-procedure-effective-March-2025-accessible.pdf. WebFetch: cover 'Including amendments effective March 10, 2025'; Rule 12 NOT PRESENT; ends Rule 6(b).
- **Notes:** Corpus candidate.

### `ma-rules-criminal` — Massachusetts Rules of Criminal Procedure (per-rule pages)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Massachusetts Rules of Criminal Procedure (per-rule pages)
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /rules-of-criminal-procedure/criminal-procedure-rule-{N without dot}-{title-slug}; 14.1 -> rule-141 etc.
  - Index: `https://www.mass.gov/law-library/massachusetts-rules-of-criminal-procedure`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' line — observed: "Effective Date: 03/01/2025"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** slug drops the decimal point or colon: Rule 23.1 -> 'rule-231', 4.1 -> 'rule-41' (collides with Rule 41)
- **Probe:** Mass. R. Crim. P. 14 → `https://www.mass.gov/rules-of-criminal-procedure/criminal-procedure-rule-14-pretrial-discovery-from-the-prosecution` — expect: "Criminal Procedure Rule 14: Pretrial discovery from the prosecution"
- **Evidence (2026-10-16):** fetch_doc.py 200: 'Criminal Procedure Rule 14: Pretrial discovery from the prosecution Effective Date: 03/01/2025'. WebFetch not run (budget).

### `ma-rules-sjc` — Rules of the Supreme Judicial Court (per-rule pages; Rules of Professional Conduct are SJC Rule 3:07)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of the Supreme Judicial Court (per-rule pages; Rules of Professional Conduct are SJC Rule 3:07)
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /supreme-judicial-court-rules/supreme-judicial-court-rule-{chapter}{rule}-{title-slug}: colon dropped (1:03 -> rule-103, 1:02A -> rule-102a). Rules of Professional Conduct (SJC Rule 3:07) are indexed from https://www.mass.gov/info-details/massachusetts-rules-of-professional-conduct (not probed).
  - Index: `https://www.mass.gov/law-library/massachusetts-supreme-judicial-court-rules`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' line — observed: "Effective Date: 01/01/1981"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** colon dropped in slug (1:03 -> 103) - ambiguous with e.g. 10:3 style; pick by title
- **Probe:** S.J.C. Rule 1:03 → `https://www.mass.gov/supreme-judicial-court-rules/supreme-judicial-court-rule-103-uniform-certification-of-questions-of-law` — expect: "Supreme Judicial Court Rule 1:03: Uniform Certification of Questions of Law"
- **Evidence (2026-10-16):** fetch_doc.py 200: 'Supreme Judicial Court Rule 1:03: Uniform Certification of Questions of Law Effective Date: 01/01/1981'. Full-set PDF (ma-rules-sjc-pdf) WebFetch: Rule 1:03 YES.

### `ma-rules-sjc-pdf` — Rules of the Supreme Judicial Court - full-set PDF

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries · text: **fetch-and-quote** · official: unknown
- **Coverage:** All SJC rules (chs. 1-4) incl. Rule 3:07 Rules of Professional Conduct; 470 pp.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.mass.gov/doc/massachusetts-supreme-judicial-court-rules-and-orders/download`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 1,152,705 chars; WebFetch stops inside Rule 1:18 (Uniform Rules on Dispute Resolution, Rule 7(i)); Rule 3:07 NOT PRESENT.
- **Currency:** PDF cover — observed: "Including rule amendments effective August 1, 2026"
- **Official status:** No statement on cover.
- **Hazard:** WebFetch truncation (chapter 1 only)
- **Probe:** S.J.C. Rule 1:03 → `https://www.mass.gov/doc/massachusetts-supreme-judicial-court-rules-and-orders/download` — expect: "Including rule amendments effective August 1, 2026"
- **Evidence (2026-10-16):** fetch_doc.py: PDF 470 pp, jud-lib-sjc-rules-August-2026-accessible.pdf. WebFetch: cover 'Including rule amendments effective August 1, 2026'; Rule 1:03 YES; Rule 3:07 NOT PRESENT.
- **Notes:** Corpus candidate.

### `ma-rules-superior` — Rules of the Superior Court (per-rule pages)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Massachusetts Trial Court Law Libraries / Supreme Judicial Court (mass.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of the Superior Court (per-rule pages)
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Slugs /superior-court-rules/superior-court-rule-{N}{letter}-{title-slug} (9A -> superior-court-rule-9a-civil-motions). Full-set PDF https://www.mass.gov/doc/massachusetts-superior-court-rules-and-orders/download (122 pp, 256,749 chars, 'Sept-2025').
  - Index: `https://www.mass.gov/law-library/massachusetts-superior-court-rules`
  - Navigation: index page lists one link per rule (slug includes the rule title) -> rule page holds the rule text, 'Effective Date' and 'Updates' history, often with Reporter's Notes.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - Per-rule pages are ~10K chars of chrome plus rule text.
- **Currency:** rule page 'Effective Date' line — observed: "Effective Date: 09/15/2025"
- **Official status:** mass.gov rule pages carry no official/unofficial statement; rules are promulgated by the SJC (or the trial-court department).
- **Hazard:** full-set PDF exceeds the WebFetch window
- **Probe:** Superior Court Rule 9A → `https://www.mass.gov/superior-court-rules/superior-court-rule-9a-civil-motions` — expect: "Superior Court Rule 9A: Civil motions"
- **Evidence (2026-10-16):** fetch_doc.py 200: 'Superior Court Rule 9A: Civil motions Effective Date: 09/15/2025'.

## D. Administrative code

### `ma-cmr-massgov` — Code of Massachusetts Regulations - mass.gov (Trial Court Law Libraries) PDFs

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Trial Court Law Libraries / issuing agencies (mass.gov) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** CMR by title (agency) and chapter; per-chapter PDF copies.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Title index /law-library/{title}-cmr (e.g. /law-library/940-cmr, /law-library/310-cmr; full list at /info-details/code-of-massachusetts-regulations-cmr-by-number, some titles use /info-details/ pages e.g. 220 CMR, 452 CMR). Chapter page slug /regulations/{title}-CMR-{chapter x100, no dot}-{title-slug} (940 CMR 3.00 -> 940-CMR-300-general-regulation; 310 CMR 10.00 -> 310-CMR-1000-wetlands-protection). The chapter page holds only a summary; the text is the linked PDF /doc/{slug}/download (slug not derivable).
  - Index: `https://www.mass.gov/law-library/{title}-cmr`
  - Navigation: title index -> chapter page (regulations/{title}-CMR-{chapter}00-...) -> 'Download a PDF copy' link -> PDF; find the section (3.16) inside the PDF.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 940 CMR 3.00 PDF 84,945 chars fits WebFetch; 310 CMR 10.00 PDF 627,647 chars (245 pp) will be truncated.
- **Currency:** PDF page footers (register issue of last amendment) — observed: "(Mass. Register #1420 6/26/20)"
- **Official status:** Regulation page: 'Official Version: Purchase the official print version' (official CMR is published by the Secretary of the Commonwealth).
- **Hazard:** PDF may be stale - check footer register number and file date (310 CMR 10 PDF last-modified 2017)
- **Hazard:** long chapters truncated by WebFetch
- **Hazard:** unofficial copy
- **Probe:** 940 CMR 3.16 → `https://www.mass.gov/doc/940-cmr-3-consumer-protection-general-regulations/download` — expect: "Without limiting the scope of any other rule, regulation or statute"
- **Evidence (2026-10-16):** WebFetch YES 3.16 'Without limiting the scope of any other rule, regulation or'; 3.19 present; footer '(Mass. Register #1420 6/26/20)'. fetch_doc.py: 22 pp. Second: 310 CMR 10.02 found in /doc/310-cmr-10-wetlands-protection/download (245 pp).

### `ma-cmr-lii` — Cornell LII - Code of Massachusetts Regulations

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** CMR titles 101 CMR onward, per section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/massachusetts/{title}-CMR-{chapter}-{section}`
  - Placeholders: 940 CMR 3.16 -> 940-CMR-3-16; 310 CMR 10.02 -> 310-CMR-10-02 (keep the section's leading zero). Title index https://www.law.cornell.edu/regulations/massachusetts.
  - Index: `https://www.law.cornell.edu/regulations/massachusetts`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay 10; disallows /search/, /user/ and admin paths (per DE log)
  - Pages last-modified Aug. 2, 2025 - may lag.
- **Currency:** Notes block at foot of section — observed: "State regulations are updated quarterly"
- **Official status:** Third-party; 'State regulations are updated quarterly'.
- **Hazard:** may lag the official CMR (pages dated Aug 2025)
- **Probe:** 940 CMR 3.16 → `https://www.law.cornell.edu/regulations/massachusetts/940-CMR-3-16` — expect: "Without limiting the scope of any other rule, regulation or statute"
- **Evidence (2026-10-16):** fetch_doc.py 200: '940 CMR, § 3.16 - General' body 'Without limiting the scope of any other rule, regulation or statute'; 310-CMR-10-02 also 200 with body.

## D. Administrative register

### `ma-register-sos` — Massachusetts Register - Secretary of the Commonwealth, State Publications and Regulations Division

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Secretary of the Commonwealth · text: **link-only** · official: official
- **Coverage:** Register issues and official CMR - subscription/purchase (reported).
- **Access:** `link-only` · format html
  - Pattern: `https://www.sec.state.ma.us/divisions/spr/massachusetts-register.htm`
- **Automation:** WebFetch fail · shell http-error · robots: Disallows /spr, /Pubs, /search and many others; /divisions/spr not disallowed
  - fetch_doc.py returned 0 characters; WebFetch errored on /divisions/spr/massachusetts-register.htm and /divisions/spr/index.htm.
- **Currency:** unknown
- **Official status:** The SOS publishes the official CMR and Register (print/subscription); from memory, not seen on a fetched page.
- **Hazard:** not readable by either tool
- **Probe:** Massachusetts Register → `https://www.sec.state.ma.us/divisions/spr/massachusetts-register.htm`
- **Evidence (2026-10-16):** fetch_doc.py: 200 with 0 chars of text; WebFetch: 'There was an error while fetching.' (twice).

### `ma-register-statelib` — Massachusetts Register - State Library of Massachusetts digital collection (DSpace)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · State Library of Massachusetts (issues published by the Secretary of the Commonwealth) · text: **link-only** · official: unknown
- **Coverage:** Issues by number (e.g. no. 1337, 2017-04-21); collection 'Registers 1201 through 1400' seen; latest coverage not checked.
- **Access:** `search-only` · format pdf
  - Index: `https://archives.lib.state.ma.us/`
  - Navigation: Find the issue entity page (via WebSearch 'Massachusetts Register (YYYY-MM-DD; no. NNNN)') -> entity page lists the PDF file; robots disallows /search and /browse/* so the site's own search cannot be used by scripts.
- **Automation:** WebFetch untested · shell ok · robots: Disallow /search, /browse/*, /entities/*/*/*, /statistics; entity pages allowed
  - Entity page server-renders metadata (fetch_doc 1,224 chars) but the PDF link was not found in raw HTML (Angular app); bitstream download untested.
- **Currency:** none
- **Official status:** Scanned issues of the Register published by the Secretary of the Commonwealth; no authentication statement seen.
- **Hazard:** no deterministic issue -> URL mapping
- **Hazard:** PDF link not in raw HTML
- **Probe:** Mass. Register #1337 → `https://archives.lib.state.ma.us/entities/journalfile/b44bea6e-965b-474f-b9a9-04ae8f68f90d` — expect: "Massachusetts Register (2017-04-21; no. 1337)"
- **Evidence (2026-10-16):** fetch_doc.py: entity page 200 'Massachusetts Register (2017-04-21; no. 1337)', file ocm04109606-2017-04-21.pdf listed; PDF not fetched.

## E. Case law

### `ma-mass-reports-lexis` — Massachusetts Reports Public Access (LexisNexis, for the Reporter of Decisions)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · LexisNexis (official reports publisher) · text: **link-only** · official: unofficial
- **Coverage:** Unknown (not fetched).
- **Access:** `link-only` · format html
  - Pattern: `https://www.lexisnexis.com/clients/macourts/`
- **Automation:** WebFetch untested · shell blocked-robots · robots: www.lexisnexis.com: User-agent * Disallow: /clients/
  - Not fetched with WebFetch either, per the no-workaround rule.
- **Currency:** unknown
- **Official status:** Reporter's 'Unofficial collections' page lists it under free unofficial collections.
- **Hazard:** robots-disallowed
- **Probe:**  → `https://www.lexisnexis.com/clients/macourts/`
- **Evidence (2026-10-16):** fetch_doc.py: REFUSED - robots.txt disallows /clients/ (rule: Disallow: /clients/).
- **Notes:** Linked from https://www.mass.gov/lists/unofficial-collections-of-published-opinions.

### `ma-opinions-massgov` — SJC and Appeals Court slip opinions - Reporter of Decisions 'Today's Opinions' (mass.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Office of the Reporter of Decisions, Supreme Judicial Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Recently released published opinions of the SJC and Appeals Court only (listing shows about the last two weeks); plus daily lists of unpublished Appeals Court decisions.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: PDF URL /doc/{case-name-slug}-{sjc|ac}-{letter}{docket digits}/download, e.g. commonwealth-v-goncalves-sjc-c13880 (SJC-13880), bruno-v-alliance-rental-group-llc-ac-s25p0383 (2025-P-0383). The letter prefix (c, p, s, w, j, x) is not derivable from the citation - take the link from the listing.
  - Index: `https://www.mass.gov/info-details/new-opinions`
  - Navigation: new-opinions page -> case link -> PDF (filename = {letter}{docket}.pdf). Older opinions: use ma-cases-justia.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 28-page SJC opinion = 44,757 chars, fits WebFetch.
- **Currency:** listing updated daily
- **Official status:** Slip PDF notice: slip opinions are 'superseded by the advance sheets and bound volumes of the Official Reports'; Reporter's page: 'There is no official version of the Massachusetts Reports available online.'
- **Hazard:** slip pagination only - no Mass. Reports page numbers
- **Hazard:** listing is short-lived; older mass.gov /doc links can 404 (FAR lists from 2022-2026 found by search returned 404)
- **Hazard:** slug letter prefix not derivable
- **Probe:** Commonwealth v. Goncalves, SJC-13880 (Mass. Oct. 6, 2026) → `https://www.mass.gov/doc/commonwealth-v-goncalves-sjc-c13880/download` — expect: "DEWAR, J. The defendant, Clerence H. Goncalves, surreptitiously photographed a"
- **Evidence (2026-10-16):** WebFetch: body present, not truncated, no Mass. cite, slip pagination; 'Dukes County. April 6, 2026. - October 6, 2026.' fetch_doc.py: PDF 28 pp, filename c13880.pdf.
- **Notes:** Appellate Opinion Portal https://www.mass.gov/appellate-opinion-portal links: new opinions, unofficial collections list, Rule 23.0 archive (128archive.com), revisions, bound-volume errata.

### `ma-rule23-128archive` — Appeals Court Summary Dispositions under Rule 23.0 (formerly 1:28) - Reporter of Decisions archive

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Office of the Reporter of Decisions (linked from mass.gov Appellate Opinion Portal) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** About 20,030 Rule 1:28/23.0 decisions; earliest released about Feb. 2008 (9 released before 2/28/2008; 933 through 12/31/2008) to today.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://128archive.com/?DocketNumber={yy}-P-{nnnn}`
  - Placeholders: GET search (form method=get): DocketNumber in 'YY-P-NNNN' form (zero-pad to 4: 25-P-0254); also PartyName={last name}, ReleaseDateFrom/ReleaseDateTo=mm/dd/yyyy, Keywords=term;term, SortColumnName, SortOrder, PageSize. Result rows give case name, docket, release date and links /Disposition/DownloadDisposition/{id}?dispositionId={id2} (PDF) - ids not derivable.
  - Index: `https://128archive.com/`
  - Navigation: GET search -> row -> Download PDF link
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - 'Read in Full' HTML view (ViewDispositionDocInHtml) redirected to an error page for fetch_doc.py; use the PDF link.
- **Currency:** results default to newest first — observed: "newest release date 10/16/2026"
- **Official status:** Each PDF opens with the rule 23.0 notice that summary decisions are primarily directed to the parties and citable only for persuasive value (if issued after Feb. 25, 2008).
- **Hazard:** non-precedential; cite with Rule 23.0 notation
- **Hazard:** HTML view errors; PDF only
- **Hazard:** party-name search is last name only
- **Probe:** Commonwealth v. Washington, No. 25-P-0254 (Mass. App. Ct. Oct. 16, 2026) (Rule 23.0) → `https://128archive.com/?DocketNumber=25-P-0254` — expect: "COMMONWEALTH vs. TRAVIS C. WASHINGTON. Docket Number 25-P-0254"
- **Evidence (2026-10-16):** WebFetch: 'SHOWING RESULTS: 1 of 1', Commonwealth vs. Travis C. Washington, 25-P-0254, 10/16/2026, PDF /Disposition/DownloadDisposition/22056?dispositionId=22080. fetch_doc.py: PartyName=Loreti 2 rows; PDF 25P0907.pdf 5 pp opens with the rule 23.0 NOTICE.
- **Notes:** Host is not on mass.gov but is the archive the Reporter of Decisions' portal links as 'Search Appeals Court summary dispositions'.

### `ma-cases-justia` — Justia - Massachusetts SJC and Appeals Court opinions

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** SJC and Appeals Court by year and by volume archive (year range not stated); slip text only.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/massachusetts/supreme-court/{year}/sjc-{docket}.html`
  - Placeholders: SJC: year = decision year, docket digits from SJC-NNNNN (verified sjc-13880). Appeals Court: https://law.justia.com/cases/massachusetts/court-of-appeals/{year}/{yy}-p-{n}.html with the number UNPADDED (25-p-396, 25-p-1082 seen in the 2026 listing; not fetched individually). Year listings: /cases/massachusetts/supreme-court/{year}/ and /court-of-appeals/{year}/; older by volume: /volumes/.
  - Index: `https://law.justia.com/cases/massachusetts/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot challenge to fetch_doc.py
  - Pages carry an AI-summary notice; quote only opinion text.
- **Currency:** year listing — observed: "newest SJC entry Oct. 14, 2026"
- **Official status:** Listing: opinions 'may not be the official published versions'.
- **Hazard:** slip text, no Mass. Reports pagination
- **Hazard:** AI-generated summaries on page
- **Hazard:** Rule 23.0 coverage unknown
- **Hazard:** shell refused
- **Probe:** Commonwealth v. Goncalves, SJC-13880 (Mass. 2026) → `https://law.justia.com/cases/massachusetts/supreme-court/2026/sjc-13880.html` — expect: "The defendant, Clerence H. Goncalves, surreptitiously photographed a sexual encounter"
- **Evidence (2026-10-16):** WebFetch: body present 'The defendant, Clerence H. Goncalves, surreptitiously photographed a sexual encounter'; no Mass. Reports pagination. Listings 2026 SJC (Daikin SJC-13881 Oct. 14) and Appeals Court (25-P-1082 Sept. 21) OK.
- **Notes:** Main free route for opinions older than the mass.gov listing.

## F. Subsequent history

### `ma-docket-appellatecourts` — Massachusetts Appellate Courts public docket (SJC, Appeals Court, FAR applications)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Judicial Court / Appeals Court clerks · text: **link-only** · official: unknown
- **Coverage:** Dockets for SJC (SJC-NNNNN), FAR applications (FAR-NNNNN), Appeals Court (YY-P-NNNN, YY-J-NNNN) - reported.
- **Access:** `search-only` · format html
  - Index: `https://www.ma-appellatecourts.org/`
  - Navigation: Search by docket number or party in a browser; the Appeals Court docket shows the FAR application and its disposition (reported, not seen).
- **Automation:** WebFetch fail · shell blocked-challenge · robots: robots.txt answered with a bot challenge
  - WebFetch 'There was an error while fetching.' on / and a docket URL.
- **Currency:** unknown
- **Hazard:** bot challenge - never route around it
- **Probe:**  → `https://www.ma-appellatecourts.org/`
- **Evidence (2026-10-16):** fetch_doc.py: REFUSED (robots.txt challenge). WebFetch: CLIENT_ERROR 'There was an error while fetching.'
- **Notes:** The only free place where FAR dispositions are tied to the Appeals Court docket. Without it, FAR history is visible only in later opinions' history lines, in the Mass. Reports FAR tables (cited as 'further appellate review denied, 491 Mass. 1102'), or via party-name search on Justia/CourtListener.

### `ma-far-lists-massgov` — SJC 'Further appellate review denied' lists (mass.gov PDFs)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Judicial Court (mass.gov) · text: **link-only** · official: unknown
- **Coverage:** Periodic PDF lists of FAR applications denied (titles seen in search 2018-2023).
- **Access:** `search-only` · format pdf
  - Index: `https://www.mass.gov/info-details/new-opinions`
  - Navigation: No index page found; WebSearch surfaces /doc/far-denied-list-{date}/download and /doc/further-appellate-review-denied-list-{date}/download URLs, but the ones tried are 404.
- **Automation:** WebFetch untested · shell http-error · robots: User-agent * : Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*, /*?auHash=; /law-library/, /rules-of-*/, /regulations/, /guide-to-evidence/, /doc/*/download allowed. SemrushBot fully disallowed.
  - 404 on /doc/further-appellate-review-denied-list-july-29-2022/download, /doc/far-denied-list-may-12-2023/download, /doc/fard-redacted-order-july-31-2026/download.
- **Currency:** unknown
- **Hazard:** documents removed (404) after posting
- **Hazard:** no index
- **Probe:**  → `https://www.mass.gov/doc/far-denied-list-may-12-2023/download`
- **Evidence (2026-10-16):** fetch_doc.py: HTTP 404 on three search-result URLs (2022, 2023, 2026).

## Not available (do not look for these again)

- **case_law** — Free official Massachusetts Reports / Appeals Court Reports text or pagination: Reporter of Decisions page https://www.mass.gov/lists/unofficial-collections-of-published-opinions: 'There is no official version of the Massachusetts Reports available online.' The LexisNexis public-access site is robots-blocked. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Rule 23.0(2) and the slip opinions cite only Mass. / Mass. App. Ct. reports and docket numbers; no neutral format found. (2026-10-16)
- **statutes** — public.law edition of Massachusetts law: www.public.law home page has no 'Massachusetts' (fetch_doc grep 0 matches); massachusetts.public.law: proxy 502 when fetching robots.txt. (2026-10-16)
- **statutes** — Cornell LII Massachusetts statutes / constitution / opinions: https://www.law.cornell.edu/states/massachusetts links out to state sites; LII hosts only the CMR. (2026-10-16)
- **subsequent_history** — Index page of SJC FAR-denied lists on mass.gov: Only individual /doc/ PDFs surfaced by WebSearch, and the three tried returned HTTP 404. (2026-10-16)

## Corpus candidates (maintainers)

- `ma-guide-evidence-pdf` — 446 pp / 1.46M chars; WebFetch stops in the Note to § 202; per-section pages also cut long Notes (§ 803).
- `ma-rules-civil-pdf` — 271 pp / 828K chars; WebFetch stops in Rule 6(b). Ingest is also the fix for the rule-41 slug collisions.
- `ma-rules-sjc-pdf` — 470 pp / 1.15M chars; WebFetch stops in Rule 1:18; Rule 3:07 (Rules of Professional Conduct) unreachable.
- `ma-constitution-malegislature` — Single 357K-char HTML page; WebFetch cannot reach Articles of Amendment after about art. V.
- `ma-rules-superior` — 122 pp / 257K chars full set, beyond the WebFetch window (not WebFetched).

## Open questions

- Do mass.gov slip-opinion /doc/ links persist after they leave the 'Today's Opinions' listing? The FAR-list PDFs found by search are 404.
- ma-appellatecourts.org (dockets, FAR) refuses automated access: is there any other free official record of FAR dispositions linked to the Appeals Court docket?
- Justia Appeals Court case URLs ({yy}-p-{n}.html, unpadded) were seen only in the listing; fetch one to verify. Justia's year coverage was not checked.
- Rules of Professional Conduct (SJC Rule 3:07) per-rule pages under /info-details/massachusetts-rules-of-professional-conduct were not probed.
- Massachusetts Register: no free official current source was readable (SOS page empty / WebFetch error); State Library DSpace PDF download untested; latest issue held unknown.
- Superior Court opinions (mass.gov 'Published Trial Court Opinions' lists 1980-date) and SJC single-justice decisions (archive from 2019) were not traced to a host.
- law_aliases popular-name chapter mappings (Wage Act, MCRA, MTCA, anti-SLAPP, Open Meeting, Public Records) are from memory.
- Criminal, appellate, SJC, Appeals Court and Superior per-rule pages were verified with fetch_doc.py only; WebFetch was not run on them.

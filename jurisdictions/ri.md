# Rhode Island (RI) — free legal sources

_Generated from `data/ri.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the legislature's per-section HTML (webserver.rilegislature.gov) is constructible straight from the citation and readable by fetch_doc.py, but built URLs are gated for the fetch tool and the site calls itself unofficial/provisional; Justia's 2025 edition is the fetch-tool fallback. Constitution, Public Laws and RICR regulations (rules.sos.ri.gov, constructible part pages, official PDF on S3) are all script-readable. Court rules are long courts.ri.gov PDFs (civil rules 274K chars; fetch tool stops in Rule 26) - corpus candidates. Supreme Court slip opinions are constructible from the docket (Supreme-yy-seq.pdf) only for 2021+ dockets after the 2025 site redesign, with slip pagination; Justia covers 1844-2026. No intermediate appellate court, no public-domain citation, and the docket portal is a JavaScript app that refuses the script.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Rhode Island Supreme Court | `ri (unverified)` | R.I. | A.3d, A.2d, A., R.I. | — |
| Rhode Island Superior Court | `risuperct (unverified)` | R.I. Super. Ct. | A.3d, A.2d | — |
| Rhode Island Family Court | `— (unverified)` | R.I. Fam. Ct. | — | — |
| Rhode Island District Court | `— (unverified)` | R.I. Dist. Ct. | — | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Rhode Island General Laws | `R.I. Gen. Laws § 9-1-14`; `G.L. 1956 § 27-7-2.1(i)`; `R.I. Gen. Laws § 6A-2-725`; `G.L. 1956 § 42-35-15`; `R.I.G.L. § 28-14-19.1`; `section 9-1-14 of the General Laws`; `§ 12-19-19 of the Rhode Island General Laws`; `R.I. Gen. Laws Chapter 27-29`; `Chapter 22-7.4 of the General Laws`; `R.I. Gen. Laws §§ 42-35-1 to 42-35-18` | `ri-gl-legislature` → `ri-gl-justia` |
| Rhode Island General Laws (bare section, no marker) *(only once this jurisdiction is known)* | `§ 9-1-14`; `§ 27-7-2.1(i)`; `section 12-19-19` | `ri-gl-legislature` → `ri-gl-justia` |
| Rhode Island Public Laws (session laws, Bluebook) | `2024 R.I. Pub. Laws ch. 1`; `2025 R.I. Pub. Laws ch. 123` | `ri-public-laws` |
| Rhode Island Public Laws (P.L. year, ch. N) *(only once this jurisdiction is known)* | `P.L. 2019, ch. 82, § 1`; `P.L. 2009, ch. 123, § 1`; `P.L. 1971, ch. 200, § 1` | `ri-public-laws` |
| Rhode Island Constitution | `R.I. Const. art. I, § 2`; `R.I. Const. art. 1, sec. 2`; `R.I. Const. art. X, § 1`; `article 1, section 2 of the Rhode Island Constitution`; `Article X, Section 1 of the Rhode Island Constitution` | `ri-constitution-legislature` → `ri-constitution-justia` |
| Superior Court Rules of Civil Procedure | `Super. R. Civ. P. 56`; `R.I. Super. R. Civ. P. 12(b)(6)`; `Rule 12(b)(6) of the Rhode Island Superior Court Rules of Civil Procedure` | `ri-rules-superior-civil` |
| Superior Court Rules of Criminal Procedure | `Super. R. Crim. P. 32(f)`; `R.I. Super. R. Crim. P. 35` | `ri-rules-superior-criminal` |
| Superior Court Rules of Civil / Criminal Procedure (prose, no state marker) *(only once this jurisdiction is known)* | `Rule 56 of the Superior Court Rules of Civil Procedure`; `Rule 32(f) of the Superior Court Rules of Criminal Procedure` | `ri-rules-superior-civil` → `ri-rules-superior-criminal` |
| Supreme Court Rules (Articles I-X: appellate procedure, discipline, professional conduct, judicial conduct) | `Article I, Rule 12A of the Supreme Court Rules of Appellate Procedure`; `Article III, Rule 13 of the Supreme Court Rules of Disciplinary Procedure for Attorneys`; `Article V, Rule 1.7 of the Supreme Court Rules of Professional Conduct`; `R.I. Sup. Ct. R. art. I, R. 12A`; `R.I. Sup. Ct. R. art. V, R. 1.7` | `ri-rules-supreme` |
| Rhode Island Rules of Evidence | `R.I. R. Evid. 803(6)`; `Rule 701 of the Rhode Island Rules of Evidence`; `R.I. R. Evid. 403` | `ri-rules-evidence` |
| Family Court and District Court rules | `Fam. Ct. R. Dom. Rel. P. 60(b)`; `Rule 60(b) of the Family Court Rules of Domestic Relations Procedure`; `Rule 12 of the District Court Civil Rules`; `R.I. Dist. Ct. R. Civ. P. 12` | `ri-rules-other-courts` |
| Rhode Island Code of Regulations (RICR) | `230-RICR-20-25-13`; `230 R.I. Code R. 230-RICR-20-25-13.2`; `216-RICR-40-05-1`; `250-RICR-150-05-3` | `ri-ricr-sos` → `ri-ricr-lii` |
| Reported Rhode Island cases (Atlantic Reporter) | `Finch v. Centennial Insurance Company, 650 A.2d 495 (R.I. 1994)`; `State v. Regan, 273 A.3d 116, 119 (R.I. 2022)`; `State v. LaRoche, 883 A.2d 1151, 1154 (R.I. 2005)`; `Wilkinson v. Vesey, 110 R.I. 606, 295 A.2d 676 (1972)` | `ri-opinions-supreme` → `ri-cases-justia` |
| Rhode Island Reports (official, to 1980) | `110 R.I. 606`; `122 R.I. 1` | `ri-cases-justia` |
| Rhode Island Supreme Court docket number | `No. 2023-43-C.A.`; `No. 2025-247-Appeal`; `No. 2026-268-M.P.`; `No. 2023-251-Appeal`; `No. 2021-34-C.A. (P2/18-488AG)` | `ri-opinions-supreme` → `ri-orders-supreme` → `ri-cases-justia` |
| Superior Court civil action number (county prefix) *(only once this jurisdiction is known)* | `C.A. No. PC-2025-03316`; `NC-2025-0187`; `PC-2026-4935`; `WC-2026-0552` | `ri-decisions-trial` → `ri-cases-justia` |

Regexes (case-insensitive):

- Rhode Island General Laws: `(?:R\.\s*I\.\s*Gen\.\s*Laws(?:\s+Ann\.)?|R\.\s*I\.\s*G\.\s*L\.|G\.\s*L\.\s*(?:R\.\s*I\.\s*)?1956|Gen(?:eral|\.)?\s+Laws\s+1956)\s*,?\s*(?:\(\d{4}\s+Reenactment\)\s*)?§§?\s*(?P<title>\d{1,2}[A-Z]?)-(?P<chapter>\d{1,3}(?:\.\d+)?)-(?P<section>\d{1,4}(?:\.\d+)?)(?![\d])|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}[A-Z]?-\d{1,3}(?:\.\d+)?-\d{1,4}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Rhode\s+Island\s+)?General\s+Laws|(?:R\.\s*I\.\s*Gen\.\s*Laws|G\.\s*L\.\s*1956)\s*,?\s*ch(?:apter|\.)\s*(?P<chapter3>\d{1,2}[A-Z]?-\d{1,3}(?:\.\d+)?)(?![\d])|chapter\s+(?P<chapter4>\d{1,2}[A-Z]?-\d{1,3}(?:\.\d+)?)\s+of\s+the\s+(?:Rhode\s+Island\s+)?General\s+Laws`
- Rhode Island General Laws (bare section, no marker): `(?:§§?|\bsec(?:tion|\.))\s*(?P<section>\d{1,2}[A-Z]?-\d{1,3}(?:\.\d+)?-\d{1,4}(?:\.\d+)?)(?![\d])`
- Rhode Island Public Laws (session laws, Bluebook): `(?P<year>(?:19|20)\d\d)\s+R\.\s*I\.\s*Pub\.\s*Laws\s+(?:ch\.\s*(?P<chapter>\d{1,3})|(?P<page>\d{1,5}))`
- Rhode Island Public Laws (P.L. year, ch. N): `P\.\s*L\.\s*(?P<year>(?:19|20)\d\d),\s*ch\.\s*(?P<chapter>\d{1,3})`
- Rhode Island Constitution: `R\.\s*I\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+|\d{1,2}),?\s*(?:§|sec\.)\s*(?P<section>\d{1,2})|article\s+(?P<article2>[IVXL]+|\d{1,2}),?\s+section\s+(?P<section2>\d{1,2})\s+of\s+the\s+(?:Rhode\s+Island\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Rhode\s+Island)`
- Superior Court Rules of Civil Procedure: `(?:R\.\s*I\.\s*)?Super\.\s*(?:Ct\.\s*)?R\.\s*Civ\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Rhode\s+Island\s+Superior\s+Court\s+Rules\s+of\s+Civil\s+Procedure`
- Superior Court Rules of Criminal Procedure: `(?:R\.\s*I\.\s*)?Super\.\s*(?:Ct\.\s*)?R\.\s*Crim\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Rhode\s+Island\s+Superior\s+Court\s+Rules\s+of\s+Criminal\s+Procedure`
- Superior Court Rules of Civil / Criminal Procedure (prose, no state marker): `Rule\s+(?P<rule>\d{1,2}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Superior\s+Court\s+Rules\s+of\s+(?P<kind>Civil|Criminal)\s+Procedure`
- Supreme Court Rules (Articles I-X: appellate procedure, discipline, professional conduct, judicial conduct): `Article\s+(?P<article>[IVX]+),?\s+Rule\s+(?P<rule>\d{1,2}(?:\.\d+)?[A-Z]?)\s+of\s+the\s+(?:Rhode\s+Island\s+)?Supreme\s+Court\s+Rules|R\.\s*I\.\s*Sup(?:r|reme)?\.?\s*Ct\.\s*R(?:ules?|\.)?,?\s*art\.\s*(?P<article2>[IVX]+),?\s*R(?:ule|\.)\s*(?P<rule2>\d{1,2}(?:\.\d+)?[A-Z]?)`
- Rhode Island Rules of Evidence: `R\.\s*I\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Rhode\s+Island\s+Rules\s+of\s+Evidence`
- Family Court and District Court rules: `Fam\.\s*Ct\.\s*R\.\s*Dom\.\s*Rel\.\s*P\.\s*(?P<rule>\d{1,2}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Rhode\s+Island\s+)?(?:Family\s+Court\s+Rules\s+of\s+Domestic\s+Relations\s+Procedure|District\s+Court\s+Civil\s+Rules)|R\.\s*I\.\s*Dist\.\s*Ct\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule3>\d{1,2}(?:\.\d+)?)`
- Rhode Island Code of Regulations (RICR): `(?:\d{3}\s+R\.\s*I\.\s*Code\s+R\.\s*)?(?P<title>\d{3})-RICR-(?P<chapter>\d{2,3})-(?P<subchapter>\d{2})-(?P<part>\d{1,3})(?:\.(?P<section>\d+(?:\.\d+)*))?`
- Reported Rhode Island cases (Atlantic Reporter): `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>R\.\s*I\.(?:\s*Super\.(?:\s*Ct\.)?)?)\s*(?:[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*)?(?P<year>\d{4})\)|(?P<rivol>\d{1,3})\s+R\.\s*I\.\s+(?P<ripage>\d{1,4}),\s*(?P<volume2>\d{1,4})\s+A\.(?:\s*(?P<series2>2)d)?\s+(?P<page2>\d{1,5})`
- Rhode Island Reports (official, to 1980): `(?P<volume>\d{1,3})\s+R\.\s*I\.\s+(?P<page>\d{1,4})(?![\d])`
- Rhode Island Supreme Court docket number: `No\.\s*(?P<year>(?:19|20)?\d\d)-(?P<seq>\d{1,4})-(?P<type>Appeal|C\.\s*A\.|M\.\s*P\.|M\.\s*R\.|C\.\s*P\.)`
- Superior Court civil action number (county prefix): `(?:C\.\s*A\.\s*No\.\s*)?(?P<county>[PKNW][CM]|PB)-(?P<year>(?:19|20)\d\d)-(?P<seq>\d{3,5})(?![\d])`

Rhode Island courts cite statutes as 'G.L. 1956 § 9-1-14' (sometimes with '(1997 Reenactment)'); Bluebook 'R.I. Gen. Laws § 9-1-14'. Section numbers are title-chapter-section with optional decimals and letter titles (6A), so the URL needs no alias table. Bare '§ 9-1-14' is shared in shape with Tennessee, Arkansas, Idaho and others: it routes here only with Rhode Island context (context_required). 'P.L. 2019, ch. 82' is RI's session-law form; NJ writes 'P.L.2019, c.82', so the bare P.L. pattern is context_required. A '§§ a to b' range is two sections: take the first. Rules: 'Super. R. Civ. P. 56' (the prose 'Rule N of the Superior Court Rules of Civil/Criminal Procedure' is also D.C.'s title, so without 'Rhode Island' it is context_required), 'Super. R. Crim. P. 32(f)', 'Article I, Rule 12A of the Supreme Court Rules of Appellate Procedure', 'R.I. R. Evid. 803(6)'; Rules of Professional Conduct are Article V of the Supreme Court Rules. Cases: Atlantic Reporter with '(R.I. yyyy)' or '(R.I. Super. Ct. ...)'; Rhode Island Reports (R.I.) ended in 1980 and is the old official reporter; there is no public-domain citation. Supreme Court dockets 'No. 2023-43-C.A.' / '-Appeal' / '-M.P.' carry the docket year (not decision year). Superior civil actions 'PC-2025-03316' (county prefix P/K/N/W + C or M; PB = business calendar) route only with Rhode Island context. Westlaw cites need party-name search (no free WL resolver). CourtListener ids are from memory and unverified.

## A. Statutes / code

### `ri-gl-legislature` — State of Rhode Island General Laws (legislature web edition)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island General Assembly / Law Revision Office · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles of the General Laws of 1956 as amended, one HTML page per section, with 'History of Section' lines (P.L. citations).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://webserver.rilegislature.gov/Statutes/TITLE{title}/{title}-{chapter}/{title}-{chapter}-{section}.htm`
  - Placeholders: Copy the citation's parts verbatim: title as printed with its letter suffix in upper case (TITLE6A, TITLE9, TITLE42); chapter folder = '{title}-{chapter}' including decimals (9-1, 9-1.1, 22-7.4, 42-35); file = full section number + '.htm' including decimals (28-14-19.1.htm). No zero-padding. Chapter index: /Statutes/TITLE{title}/{title}-{chapter}/INDEX.htm lists every section (not ranges); title index /Statutes/TITLE{title}/INDEX.HTM lists chapters. The section number itself encodes title and chapter, so no index hop is needed. A '§§ a to b' range is two sections: take the first.
  - Index: `https://webserver.rilegislature.gov/Statutes/Statutes.html`
  - Navigation: Statutes.html -> TITLE{t}/INDEX.HTM (chapters) -> {t}-{c}/INDEX.htm (all sections listed) -> section page.
- **Automation:** WebFetch gated · shell ok · robots: none (webserver.rilegislature.gov/robots.txt 404)
  - WebFetch read Statutes.html (search-result URL) but built section and title-index URLs timed out on the permission prompt (PROVENANCE_REQUIRED): use fetch_doc.py. Section pages are small (1.5-11K chars), no truncation. Title index links on Statutes.html are http:// with a doubled slash (//Statutes/...).
- **Currency:** Statutes.html home page only; section pages carry no currency line (HTTP last-modified 2025-11-06 on sampled sections) — observed: "Search the 2026 General Laws"
- **Official status:** rilegislature.gov Disclaimer page (https://rilegislature.gov/Pages/Disclaimer.aspx) and the Statutes.html home: informational service only, 'should not be relied upon as an official record'; 'This information is provisional'; refer to the printed official publication.
- **Hazard:** no currency statement on section pages
- **Hazard:** unofficial / provisional per disclaimer
- **Hazard:** built URLs gated for WebFetch
- **Hazard:** title letter suffix (6A) must stay upper case in folder name
- **Probe:** R.I. Gen. Laws § 9-1-14 → `https://webserver.rilegislature.gov/Statutes/TITLE9/9-1/9-1-14.htm` — expect: "Actions for words spoken shall be commenced and sued within one year"
- **Evidence (2026-10-17):** fetch_doc.py read: HTML 1,729 chars, heading 'R.I. Gen. Laws § 9-1-14', body '(a) Actions for words spoken shall be commenced and sued within one year' plus History of Section. Also verified by pattern: § 11-41-1 (1,559 chars), § 6A-2-725 ('An action for breach of any contract for sale must be commenced within four (4) years'), § 42-35-15 ('Judicial review of contested cases'), § 28-14-19.1 ('Misclassification of employees'). WebFetch of Statutes.html OK (disclaimer); WebFetch of built section URL: PROVENANCE_REQUIRED timeout.
- **Notes:** Bulk download: none found on rilegislature.gov (not exhaustively searched; see open_questions).

### `ri-public-laws` — Rhode Island Public Laws (session laws, by chapter)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island General Assembly / Law Revision Office · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Public Laws by year and chapter; law95 (1995) through 2026 seen.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://webserver.rilegislature.gov/PublicLaws/law{yy}/law{yy}{chapter:03d}.htm`
  - Placeholders: yy = last two digits of the year (law24, law95); chapter zero-padded to 3 digits (law24001, law25123). Index for a year: /Lawrevision/laws{yyyy}.htm -> by chapter number /Lawrevision/plshort/pl{yyyy}nu.htm (links to each law{yy}{nnn}.htm), by bill /pl{yyyy}bil.htm, by subject /pl{yyyy}sub.htm; also /lawrevision/plshort/plindx{yyyy}.htm.
  - Index: `https://webserver.rilegislature.gov/Lawrevision/laws2024.htm`
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - /PublicLaws/ directory itself 404; /Lawrevision/laws1995.htm 404 though law95001.htm exists. One transient connection reset on law24/law24.htm (that URL does not exist as an index).
- **Currency:** each act shows 'Enacted MM/DD/YYYY' — observed: "Enacted 02/02/2024"
- **Official status:** Same rilegislature.gov disclaimer (informational, provisional). Index page titled 'THE OFFICIAL 2024 PUBLIC LAWS LIST' refers to the list, not the text.
- **Hazard:** two-digit year folders
- **Hazard:** pre-2000 year indexes missing (laws1995.htm 404)
- **Probe:** P.L. 2024, ch. 1 → `https://webserver.rilegislature.gov/PublicLaws/law24/law24001.htm` — expect: "It is enacted by the General Assembly as follows"
- **Evidence (2026-10-17):** fetch_doc.py: law24001.htm 1,056 chars 'Chapter 001 / 2024 -- H 7068 / Enacted 02/02/2024'; law25123.htm 9,692 chars 'Chapter 123 / 2025 -- S 0509 SUBSTITUTE A'; law95001.htm 928 chars. pl2024nu.htm lists 472 links to law24NNN.htm.

### `ri-gl-justia` — Justia: Rhode Island General Laws

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual editions (2012-2025 seen in search results); current = 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/rhode-island/title-{title}/chapter-{chapter}/section-{section}/`
  - Placeholders: Lower-case title (title-6a); chapter = '{title}-{chapter}' with dots replaced by hyphens (9-1.1 -> chapter-9-1-1); section = full number with dots -> hyphens (28-14-19.1 -> section-28-14-19-1). UCC title 6A has 'part-N' segments (title-6a/chapter-6a-2/part-7/section-6a-2-725/) - take Article/Part from the title page if unsure.
  - Index: `https://law.justia.com/codes/rhode-island/title-9/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com robots.txt answered fetch_doc.py with a bot challenge (REFUSED, host off for the day)
  - Built section URLs were NOT gated for WebFetch.
- **Currency:** page heading/breadcrumb — observed: "2025 Rhode Island General Laws"
- **Official status:** Third-party compilation; edition label '2025 Rhode Island General Laws'.
- **Hazard:** annual snapshot lags the legislature
- **Hazard:** dot-to-hyphen slug conversion
- **Hazard:** UCC part segment
- **Probe:** R.I. Gen. Laws § 9-1-14 → `https://law.justia.com/codes/rhode-island/title-9/chapter-9-1/section-9-1-14/` — expect: "Actions for words spoken shall be commenced and sued within"
- **Evidence (2026-10-17):** WebFetch: YES, body 'Actions for words spoken shall be commenced and sued within'; label '2025 Rhode Island General Laws'. Second: /title-28/chapter-28-14/section-28-14-19-1/ YES 'The misclassification of a worker whether performing work as a'. Title page /codes/rhode-island/title-9/ lists chapter-9-1, chapter-9-1-1, chapter-9-2. fetch_doc.py: REFUSED (robots.txt challenge).

## B. Constitution

### `ri-constitution-legislature` — Constitution of the State of Rhode Island

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island General Assembly · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full text, Articles I-XV, with amendment-history notes; per-article pages and one full-text page.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.rilegislature.gov/riconstitution/Constitution/C{article:02d}.aspx`
  - Placeholders: Article number converted from Roman to Arabic and zero-padded to 2 (Art. I -> C01, Art. X -> C10). Full text (~70.6K chars, all articles): /riconstitution/Constitution/ConstFull.aspx. Index: /riconstitution/pages/default.aspx. Sections are headed 'Section N.' inside the article page.
  - Index: `https://www.rilegislature.gov/riconstitution/pages/default.aspx`
- **Automation:** WebFetch ok · shell ok · robots: www.rilegislature.gov: Disallow only /Special/comdoc/*.pdf and /senators/SenateComDocs/*.pdf
  - WebFetch read ConstFull.aspx (search-result URL) complete through Article XV; the per-article URL C01.aspx was gated (PROVENANCE_REQUIRED). Avoid /riconstitution/Lists/...AllItems.aspx (SharePoint list views).
- **Currency:** none stated
- **Official status:** No disclaimer on the constitution pages (WebFetch of ConstFull.aspx: none); the site-wide rilegislature.gov disclaimer calls online information provisional, not an official record.
- **Hazard:** SharePoint site; per-article built URLs gated for WebFetch
- **Probe:** R.I. Const. art. I, § 2 → `https://www.rilegislature.gov/riconstitution/Constitution/C01.aspx` — expect: "All free governments are instituted for the protection, safety, and happiness of the people."
- **Evidence (2026-10-17):** fetch_doc.py verify on C01.aspx: VERIFIED 'All free governments are instituted for the protection, safety, and happiness of the people.' (12,862 chars); C10.aspx VERIFIED 'The judicial power of this state shall be vested in one supreme court'. WebFetch ConstFull.aspx: Art. X § 1 present, page complete through Article XV.

### `ri-constitution-justia` — Justia: Rhode Island Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-article pages mirroring the legislature's C01..C15 layout.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/rhode-island/C{article:02d}.html`
  - Placeholders: Same 2-digit Arabic article number as the legislature (C01.html); intro at constintro.html.
  - Index: `https://law.justia.com/constitution/rhode-island/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot challenge to fetch_doc.py
- **Currency:** none stated — observed: "This Constitution may not be the most recent version."
- **Official status:** Justia notes 'This Constitution may not be the most recent version.'
- **Hazard:** may lag amendments
- **Probe:** R.I. Const. art. I, § 2 → `https://law.justia.com/constitution/rhode-island/C01.html` — expect: "All free governments are instituted for the protection, safety, and"
- **Evidence (2026-10-17):** WebFetch C01.html: YES, 'All free governments are instituted for the protection, safety, and'; Section 2 heading includes 'No right to abortion granted.' Index page lists constintro.html, C01.html, C02.html.

## C. Court rules

### `ri-rules-evidence` — Rhode Island Rules of Evidence

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 100-1101 in one 26-page PDF.
- **Read via (in order):** **script**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.courts.ri.gov/Legal-Resources/Documents/RulesOfEvidence.pdf`
  - Index: `https://www.courts.ri.gov/Legal-Resources/Pages/court-rules.aspx`
- **Automation:** WebFetch untested · shell ok · robots: permits
  - 70,330 chars: should fit the WebFetch window (untested).
- **Currency:** page footer — observed: "Page 2 of 26    February 2024"
- **Probe:** R.I. R. Evid. 100 → `https://www.courts.ri.gov/Legal-Resources/Documents/RulesOfEvidence.pdf` — expect: "These rules may be known and cited as the Rhode Island Rules of Evidence"
- **Evidence (2026-10-17):** fetch_doc.py verify: VERIFIED 'These rules may be known and cited as the Rhode Island Rules of Evidence' page 1; 26 pages, 70,330 chars.

### `ri-rules-other-courts` — Family, District, Workers' Compensation and Traffic Tribunal rules

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** Family Court: Domestic Relations Procedure, Criminal Procedure, Practice, Juvenile Proceedings. District Court: Civil, Criminal, Small Claims. Also Superior Court Rules of Practice and Arbitration rules.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.courts.ri.gov/Legal-Resources/Pages/court-rules.aspx`
  - Navigation: court-rules.aspx -> court page (Family-Court-Rules.aspx, District-Court-Rules.aspx, Workers'-Compensation-Court-Rules.aspx, Rhode-Island-Traffic-Tribunal-Court-Rules.aspx) -> PDF link (e.g. /Courts/familycourt/Documents/RulesOfDomesticRelationsProcedure.pdf, /Courts/districtcourt/Documents/District_Civil_Rules.pdf).
- **Automation:** WebFetch untested · shell ok · robots: permits
  - Domestic Relations 218,250 chars; District Civil 205,067 chars: both beyond the WebFetch window.
- **Currency:** page footer (not checked on every PDF)
- **Hazard:** long PDFs beyond WebFetch window
- **Probe:** Fam. Ct. R. Dom. Rel. P. 1 → `https://www.courts.ri.gov/Courts/familycourt/Documents/RulesOfDomesticRelationsProcedure.pdf` — expect: "FAMILY COURT RULES OF DOMESTIC RELATIONS PROCEDURE"
- **Evidence (2026-10-17):** fetch_doc.py: RulesOfDomesticRelationsProcedure.pdf 81 pages, 218,250 chars ('FAMILY COURT RULES OF DOMESTIC RELATIONS PROCEDURE'); District_Civil_Rules.pdf 76 pages, 205,067 chars ('DISTRICT COURT CIVIL RULES'); SuperiorCourtRulesOfPractice.pdf 9 pages.

### `ri-rules-superior-civil` — Superior Court Rules of Civil Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Judiciary (Superior Court) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules 1-86 and appendix forms; single 101-page PDF.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.courts.ri.gov/Courts/superiorcourt/Documents/SuperiorCourtRulesOfCivilProcedure.pdf`
  - Index: `https://www.courts.ri.gov/Legal-Resources/Pages/Superior-Court-Rules.aspx`
  - Navigation: One PDF for all rules; find 'N. Title. —' headings with fetch_doc.py grep/section.
- **Automation:** WebFetch ok (truncated) · shell ok · robots: www.courts.ri.gov: Disallow /*AllItems.aspx and /Lists/ only
  - 274,066 chars. WebFetch (via courts.ri.gov without www, a search-result URL) stops mid Rule 26(b)(4)(A), page 38 of 101; Rule 56 NOT PRESENT. Use fetch_doc.py.
- **Currency:** page footer — observed: "Page 2 of 101    February 2024"
- **Official status:** Court-published PDF; no official/unofficial statement seen.
- **Hazard:** WebFetch truncation at Rule 26 of 86
- **Hazard:** rule headings are 'N. Title. —' without the word Rule
- **Probe:** Super. R. Civ. P. 56 → `https://www.courts.ri.gov/Courts/superiorcourt/Documents/SuperiorCourtRulesOfCivilProcedure.pdf` — expect: "A party seeking to recover upon a claim, counterclaim, or cross-claim"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 101 pages, 274,066 chars; grep '56. Summary Judgment' hit at offset 217036 page 80 ('A party seeking to recover upon a claim, counterclaim, or cross-claim'). WebFetch: NOT PRESENT for Rule 56, text stops in Rule 26.

### `ri-rules-superior-criminal` — Superior Court Rules of Criminal Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Judiciary (Superior Court) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Single 47-page PDF.
- **Read via (in order):** **script**
- **Access:** `link-only` · format pdf
  - Pattern: `https://www.courts.ri.gov/Courts/superiorcourt/Documents/SuperiorCourtRulesOfCriminalProcedure.pdf`
  - Index: `https://www.courts.ri.gov/Legal-Resources/Pages/Superior-Court-Rules.aspx`
- **Automation:** WebFetch untested · shell ok · robots: permits
  - 135,035 chars: beyond the WebFetch window (~100K reached page 34 of 47, Rule 35 area).
- **Currency:** page footer — observed: "February 2024"
- **Hazard:** long PDF beyond WebFetch window
- **Probe:** Super. R. Crim. P. 1 → `https://www.courts.ri.gov/Courts/superiorcourt/Documents/SuperiorCourtRulesOfCriminalProcedure.pdf` — expect: "In all criminal proceedings in the Superior Court"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 47 pages, 135,035 chars; opens 'SUPERIOR COURT RULES OF CRIMINAL PROCEDURE / I. SCOPE, PURPOSE, AND CONSTRUCTION'.

### `ri-rules-supreme` — Supreme Court Rules (Articles I-X)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Art. I Appellate Procedure; II Admission; III Disciplinary Procedure; IV Registration; V Rules of Professional Conduct; VI Judicial Conduct; VII Media; VIII Judicial Conference; IX Magistrate review; X E-filing; plus Disciplinary Board, Ethics Advisory Panel and Public Access rules.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.ri.gov/Courts/SupremeCourt/Documents/Supreme-Rules-Article{n}.pdf`
  - Placeholders: n = Arabic article number (Article1 ... Article10) EXCEPT Article IV, which is Supreme-Rules-Article4-2.pdf: always take the link from the index page.
  - Index: `https://www.courts.ri.gov/Legal-Resources/Pages/Supreme-Court-Rules.aspx`
  - Navigation: Supreme-Court-Rules.aspx -> 'Article N - title' PDF link -> grep 'Rule N.' inside.
- **Automation:** WebFetch untested · shell ok · robots: permits
  - Article I = 110,459 chars (just over the WebFetch window); Article V = 449,497 chars (160 pages, comments included).
- **Currency:** page footer — observed: "Page 2 of 40    Revised February 17, 2026"
- **Hazard:** irregular file name for Article IV
- **Hazard:** Article V far beyond WebFetch window
- **Probe:** Article I, Rule 1 of the Supreme Court Rules of Appellate Procedure → `https://www.courts.ri.gov/Courts/SupremeCourt/Documents/Supreme-Rules-Article1.pdf` — expect: "These rules govern procedure in appeals to the Supreme Court"
- **Evidence (2026-10-17):** fetch_doc.py: Article1.pdf 40 pages, 110,459 chars, 'Article I. Appellate Procedure / Rule 1. Scope of rules'; Article5.pdf 160 pages, 449,497 chars, 'ARTICLE V. RULES OF PROFESSIONAL CONDUCT'. Index lists Article1..Article10 plus Article4-2.

## D. Administrative code

### `ri-ricr-sos` — Rhode Island Code of Regulations (RICR)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Department of State · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All active, emergency, proposed and inactive parts filed under the APA, by title-chapter-subchapter-part.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://rules.sos.ri.gov/regulations/part/{title}-{chapter}-{subchapter}-{part}`
  - Placeholders: From '{title}-RICR-{chapter}-{subchapter}-{part}[.{section}]' drop 'RICR' and the section: 230-RICR-20-25-13.2 -> /regulations/part/230-20-25-13. Keep the citation's zero-padding (subchapter always 2 digits: 05, 00). The page carries the whole Part (all sections) plus a 'Download Regulation' PDF link on risos-apa-production-public.s3.amazonaws.com (the official text).
  - Index: `https://rules.sos.ri.gov/regulations/Index/active`
  - Read via: Official PDF on risos-apa-production-public.s3.amazonaws.com (fetch_doc.py read OK, 4 pages for 230-RICR-20-25-13).
- **Automation:** WebFetch untested · shell ok · robots: none (404) on rules.sos.ri.gov
  - rules.sos.ri.gov/ root now shows only the agency admin login; start from /regulations/Index/active or a part URL. Large parts (216-RICR-40-05-1 = 79K chars).
- **Currency:** part page header status line — observed: "ACTIVE RULE"
- **Official status:** The part page says the 'official Final Regulation' is the PDF behind 'Download Regulation' (S3 link); the HTML text is a rendering.
- **Hazard:** HTML rendering vs official PDF
- **Hazard:** root page is a login screen
- **Probe:** 230-RICR-20-25-13 → `https://rules.sos.ri.gov/regulations/part/230-20-25-13` — expect: "This Part shall apply to any solicitation, sale or purchase of"
- **Evidence (2026-10-17):** fetch_doc.py read: 13,559 chars, 'Senior Specifications (230-RICR-20-25-13) ACTIVE RULE', sections 13.1-13.6 present. Second: /regulations/part/216-40-05-1 VERIFIED 'Licensure and Discipline of Physicians'; 250-150-05-3 also resolves. S3 PDF REG_12051_20211217110227.pdf read OK.

### `ri-ricr-lii` — Cornell LII: Rhode Island Administrative Code (RICR)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Cornell Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** RICR by title/chapter/subchapter/part, one page per section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/rhode-island/{title}-RICR-{chapter}-{subchapter}-{part}.{section}`
  - Placeholders: Section-level only: a part-level URL without '.{section}' (e.g. .../230-RICR-20-25-13) returns a generic index page, not the part. Part index: /regulations/rhode-island/title-{title}/chapter-{chapter}/subchapter-{subchapter}/part-{part}.
  - Index: `https://www.law.cornell.edu/regulations/rhode-island`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * Crawl-delay 10; regulations paths not disallowed
  - Pages last-modified Aug. 6, 2025: may lag the SOS.
- **Currency:** none on page; HTTP last-modified — observed: "last-modified Wed, 06 Aug 2025"
- **Official status:** Third-party; cites as '230 R.I. Code R. 230-RICR-20-25-13.2'.
- **Hazard:** part-level URL silently falls back to an index page
- **Hazard:** may lag SOS filings
- **Probe:** 230-RICR-20-25-13.2 → `https://www.law.cornell.edu/regulations/rhode-island/230-RICR-20-25-13.2` — expect: "This Part shall apply to any solicitation, sale or purchase of"
- **Evidence (2026-10-17):** fetch_doc.py verify: VERIFIED on 230-RICR-20-25-13.2 (2,410 chars, '230 R.I. Code R. 230-RICR-20-25-13.2 - Scope'); 216-RICR-40-05-1.1 VERIFIED 'Authority'.

## D. Administrative register

### `ri-ricr-proposed` — RICR proposed-rule notices (Department of State)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Department of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Proposed rules currently open, each linking to a /Promulgations/part/{t}-{c}-{s}-{p} page (overview, regulation, history, rulemaking documents, comments). Rhode Island has no separate periodical register on this site.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Index: `https://rules.sos.ri.gov/regulations/Index/Proposed`
  - Navigation: Index/Proposed (365K chars, list by title) -> /Promulgations/part/{title}-{chapter}-{subchapter}-{part}. Filing history of an adopted part: the 'History' tab on /regulations/part/... .
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Index page 365,775 chars: beyond the WebFetch window; use fetch_doc.py links/grep.
- **Currency:** none stated
- **Hazard:** very long index page
- **Hazard:** not a dated register: notices disappear from the index once adopted
- **Probe:** 100-RICR-50-00-2 (proposed) → `https://rules.sos.ri.gov/Promulgations/part/100-50-00-2` — expect: "PROPOSED RULE"
- **Evidence (2026-10-17):** fetch_doc.py: Index/Proposed 365,775 chars, 296 links; /Promulgations/part/100-50-00-2 'Electronic Records Management 100-RICR-50-00-2 PROPOSED RULE', type of filing Amendment.

## E. Case law

### `ri-decisions-trial` — Superior and District Court decisions (courts.ri.gov PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Superior Court written decisions (/Decisions/Superior-{docket}.pdf) and District Court administrative-appeal decisions (/Decisions/District-AA{yy}-{n}.pdf); seen 2025-2026.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.courts.ri.gov/Decisions/Superior-{county}-{year}-{seq:04d}.pdf`
  - Placeholders: Superior: county prefix (PC, KC, NC, WC, PM, KM, NM, WM, PB) + 4-digit year + sequence zero-padded to 4 digits: 'C.A. No. PC-2025-03316' -> Superior-PC-2025-3316.pdf; NC-2025-0187 -> Superior-NC-2025-0187.pdf (NC-2025-187 = 404). District: 'A.A. No. 2026 - 48' -> District-AA26-48.pdf. Recent list: /Pages/ood.aspx (10 items).
  - Index: `https://www.courts.ri.gov/Pages/ood.aspx`
- **Automation:** WebFetch untested · shell ok · robots: permits
- **Currency:** decision caption — observed: "(FILED: October 6, 2026)"
- **Official status:** Trial-court decisions; unreported unless later printed in A.3d.
- **Hazard:** 5-digit printed docket vs 4-digit file name
- **Hazard:** no index beyond 10 recent items
- **Probe:** C.A. No. PC-2025-03316 → `https://www.courts.ri.gov/Decisions/Superior-PC-2025-3316.pdf` — expect: "Before this Court is an administrative"
- **Evidence (2026-10-17):** fetch_doc.py: Superior-PC-2025-3316.pdf 9 pages '(FILED: October 6, 2026) ... C.A. No. PC-2025-03316 ... DECISION CARNES, J.'; Superior-NC-2025-0187.pdf 9 pages; District-AA26-48.pdf 12 pages 'A.A. No. 2026 - 48'.

### `ri-opinions-supreme` — Rhode Island Supreme Court opinions (courts.ri.gov PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Supreme Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Slip opinions as PDF, slip pagination only (no A.3d page numbers). Files seen for dockets 2021-2026 (Supreme-21-34 ... Supreme-25-247); dockets 2014-2020 tried (e.g. Supreme-14-199, Supreme-14-145, 17-20 samples) all 404 since the 2025 site redesign. Use ri-cases-justia for older opinions.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.courts.ri.gov/Opinions/Supreme-{yy}-{seq}.pdf`
  - Placeholders: From docket 'No. 2023-43-C.A.' take yy = last two digits of the docket year and seq unpadded: Supreme-23-43.pdf. Listings print '2025-0247-Appeal' but the file is Supreme-25-247.pdf (strip zero-padding). Consolidated appeals are filed under the first docket. Lists: recent published opinions with summaries at /Courts/SupremeCourt/Pages/published-opinions.aspx; ten most recent across courts at /Pages/ood.aspx; the SharePoint library views (/Opinions/Forms/AllItems.aspx) are robots-disallowed (/*AllItems.aspx). The search page /Search/Pages/supreme-court-opinions.aspx ignores a GET ?k= query (same default 10 results).
  - Index: `https://www.courts.ri.gov/Courts/SupremeCourt/Pages/published-opinions.aspx`
- **Automation:** WebFetch gated · shell ok · robots: Disallow /*AllItems.aspx and /Lists/
  - WebFetch of Supreme-23-43.pdf timed out on the permission prompt. Long opinions exceed the WebFetch window (Supreme-21-34.pdf = 128,829 chars, with dissent). Occasional 'Connection reset by peer' on courts.ri.gov; retry later.
- **Currency:** listing pages give decision date; PDF cover gives docket — observed: "7/30/2026 (latest on published-opinions.aspx)"
- **Official status:** Each slip opinion: 'subject to formal revision before publication in the Rhode Island Reporter' (West's A.3d offprint).
- **Hazard:** slip pagination only
- **Hazard:** no free search by docket or party (search ignores GET)
- **Hazard:** pre-2021 files not found after redesign
- **Hazard:** long opinions beyond WebFetch window
- **Probe:** State v. Alicea, No. 2023-43-C.A. → `https://www.courts.ri.gov/Opinions/Supreme-23-43.pdf` — expect: "This case came before the Supreme Court on February 28, 2024"
- **Evidence (2026-10-17):** fetch_doc.py: Supreme-23-43.pdf 28 pages, 44,310 chars, 'No. 2023-43-C.A. ... State v. Lydia Alicea ... Justice Goldberg, for the Court'. Supreme-21-34.pdf 78 pages ('No. 2021-34-C.A.'). Old /Courts/SupremeCourt/OpinionsOrders/pdf-files/08-37.pdf 404.

### `ri-cases-justia` — Justia: Rhode Island Supreme Court and Superior Court decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1844-2026; Superior Court 2000-2026. HTML text, slip pagination; no A.3d cite shown on new opinions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/rhode-island/{court}/{year}/{yy}-{seq}.html`
  - Placeholders: court = supreme-court | superior-court; year = DECISION year; slug = docket year 2 digits + '-' + unpadded sequence (No. 2023-251-Appeal decided 2026 -> /supreme-court/2026/23-251.html). Superior slugs DROP the county prefix (NC-2025-0187 -> /superior-court/2026/25-187.html), so two counties' cases can collide: confirm the caption. Year listing: /cases/rhode-island/{court}/{year}/. PDF: cases.justia.com/rhode-island/{court}/{year}-{yy}-{seq}.pdf.
  - Index: `https://law.justia.com/cases/rhode-island/supreme-court/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot challenge to fetch_doc.py
  - Pages may carry AI summaries; quote only the opinion text.
- **Currency:** year listing — observed: "1844 to 2026"
- **Official status:** Third-party; links court PDFs re-hosted on cases.justia.com.
- **Hazard:** superior-court slug omits county prefix
- **Hazard:** decision year in path differs from docket year
- **Probe:** Rhode Island Joint Reinsurance Ass'n v. Ricci, No. 2023-251-Appeal → `https://law.justia.com/cases/rhode-island/supreme-court/2026/23-251.html` — expect: "The defendants, Brenda and Ernest Ricci"
- **Evidence (2026-10-17):** WebFetch: YES, 'The defendants, Brenda and Ernest Ricci (Mrs. Ricci and Mr. Ricci, respectively)', decided July 30, 2026, No. 2023-251-Appeal; superior-court/2026/25-187.html YES ('Before the Court is Michael W. Miller and Karen A. Miller's'), NC-2025-0187. 2015 listing: 14-199.html, 15-53.html, 14-145.html. fetch_doc.py REFUSED (robots challenge).

## F. Subsequent history

### `ri-docket-publicportal` — Rhode Island Judiciary Public Portal (Odyssey case search)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Rhode Island Judiciary · text: **link-only** · official: unknown
- **Coverage:** Docket entries for all state courts including Supreme Court appeals (reported; not seen).
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format html
  - Index: `https://publicportal.courts.ri.gov/PublicPortal`
  - Navigation: Browser only: Smart Search by case number or party; JavaScript and cookies required.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: permits (fetch_doc.py check OK)
  - fetch_doc.py: REFUSED HTTP 403 on /PublicPortal. WebFetch read the landing page only ('JavaScript must be enabled in order for you to use this application').
- **Currency:** unknown
- **Hazard:** JavaScript application
- **Hazard:** 403 to the script
- **Probe:**  → `https://publicportal.courts.ri.gov/PublicPortal`
- **Evidence (2026-10-17):** fetch_doc.py REFUSED HTTP 403; WebFetch read landing page with Smart Search / Search Hearings links; dispositions not reachable without the JS app.

### `ri-orders-supreme` — Rhode Island Supreme Court published orders

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Rhode Island Supreme Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Published orders (e.g. M.P. matters, disciplinary orders, dispositions by order); seen 2026. The Supreme Court is Rhode Island's only appellate court: there is no intermediate court, so subsequent history inside the state is the Supreme Court's own appeal or certiorari (writ to District, Family, WCC, agencies) disposition; U.S. Supreme Court cert is on supremecourt.gov (not recorded here).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.courts.ri.gov/Published%20Orders/Supreme-{yy}-{seq}.pdf`
  - Placeholders: Same docket rule as opinions (No. 2026-268-M.P. -> Supreme-26-268.pdf). Found from the decision below only by knowing the Supreme Court docket: Superior/Family decisions do not print it; otherwise search Justia by party name.
  - Index: `https://www.courts.ri.gov/Pages/ood.aspx`
- **Automation:** WebFetch untested · shell ok · robots: permits
  - Folder name has a space: 'Published%20Orders'. Unpublished orders were not found online.
- **Currency:** order text — observed: "Supreme Court No. 2026-268-M.P."
- **Hazard:** no listing beyond ood.aspx's 10 recent items
- **Hazard:** unpublished orders not online
- **Hazard:** history findable only via the Supreme Court docket number or party name
- **Probe:** In re Dougan, No. 2026-268-M.P. → `https://www.courts.ri.gov/Published%20Orders/Supreme-26-268.pdf` — expect: "In the Matter of Brian T. Dougan"
- **Evidence (2026-10-17):** fetch_doc.py: Supreme-26-268.pdf 3 pages, 3,419 chars, 'Supreme Court No. 2026-268-M.P. In the Matter of Brian T. Dougan. ORDER'.

## Not available (do not look for these again)

- **statutes** — public.law edition of the Rhode Island General Laws: rhode-island.public.law: proxy CONNECT 502 on robots.txt (fetch_doc.py); public.law covers only a handful of states per the DE record. (2026-10-17)
- **statutes** — Cornell LII Rhode Island General Laws / Constitution / opinions: https://www.law.cornell.edu/states/rhode_island links out to rilin.state.ri.us and courts.ri.gov; LII hosts only the RI regulations. (2026-10-17)
- **case_law** — Free official reporter pagination (Rhode Island Reports ended 1980; A.2d/A.3d is West): Slip opinions say they await publication 'in the Rhode Island Reporter' (West offprint of A.3d); PDFs carry slip pages only. (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions cite '273 A.3d 116, 119 (R.I. 2022)' style only; no medium-neutral form seen on court pages. (2026-10-17)
- **case_law** — courts.ri.gov opinions for dockets before 2021 and legacy opinion/order archive pages: Supreme-14-199.pdf, Supreme-14-145.pdf, 39 sampled 2017-2020 docket file names: 404; legacy /Courts/SupremeCourt/OpinionsOrders/pdf-files/08-37.pdf and Orders-(2012-2013).aspx pages: 404. (2026-10-17)
- **admin_register** — A periodical Rhode Island register on the Department of State site: SOS Rules and Regulations page lists the RICR, building/fire code amendments, historic rules, guide, notifications and filing resources only; proposed rules appear as an index, not dated issues. (2026-10-17)

## Corpus candidates (maintainers)

- `ri-rules-superior-civil` — 274,066 chars; fetch tool stops mid Rule 26(b)(4)(A) on page 38 of 101.
- `ri-rules-superior-criminal` — 135,035 chars, beyond the ~100K window (page 34 of 47).
- `ri-rules-supreme` — Appellate rules 110,459 chars; Article V (Rules of Professional Conduct) 449,497 chars at .../Supreme-Rules-Article5.pdf.
- `ri-rules-other-courts` — 218,250 chars; District Court Civil Rules (/Courts/districtcourt/Documents/District_Civil_Rules.pdf) 205,067 chars.
- `ri-ricr-proposed` — 365,775-char index page; only usable by script.

## Open questions

- Is there an official bulk download (zip/XML) of the General Laws? Not found on webserver.rilegislature.gov (not exhaustively searched).
- Where do pre-2021 Supreme Court opinions live on courts.ri.gov after the 2025 redesign, if anywhere? Only Justia was confirmed.
- WebFetch untested on courts.ri.gov rules PDFs other than the civil rules, on rules.sos.ri.gov and on LII RICR pages (budget); script route verified.
- Statutes currency: Statutes.html says '2026 General Laws' but sampled section pages were last modified 2025-11-06; whether 2026 session amendments are integrated was not checked.
- Superior Court decisions on courts.ri.gov: earliest year not established (only 2025-2026 seen); Justia has 2000-2026.
- U.S. Supreme Court certiorari dispositions for Rhode Island cases are on supremecourt.gov dockets; not recorded as a row.

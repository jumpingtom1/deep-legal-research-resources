# Missouri (MO) — free legal sources

_Generated from `data/mo.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and constitution: revisor.mo.gov (unofficial, uncertified) serves one section per constructible URL and reads cleanly with fetch_doc.py; WebFetch is gated on built URLs, and Justia's 2025 RSMo is the tier-2 fallback. Court rules: official per-rule pages on courts.mo.gov have opaque ids (WebFetch reads them, the script gets 403); the courts' Clerk Handbooks Domino database offers a GET search the script can read. CSR and Missouri Register are long two-column PDFs on sos.mo.gov (script ok); LII mirrors the CSR per rule. Case law: courts.mo.gov opinion PDFs refuse the script (403) and error in WebFetch, so Justia (constructible by docket and year) is the quoting route; Supreme Court minutes (Domino, script ok, from 1998) give hand-downs and transfer dispositions by Court of Appeals docket.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Missouri | `mo (unverified)` | Mo. | S.W.3d, S.W.2d, S.W., Mo. | — |
| Missouri Court of Appeals (Eastern, Western, Southern Districts) | `moctapp (unverified)` | Mo. Ct. App. | S.W.3d, S.W.2d, S.W., Mo. App. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Revised Statutes of Missouri (RSMo) | `Mo. Rev. Stat. § 516.120`; `RSMo § 516.120`; `section 516.120, RSMo 2016`; `section 537.765.3, RSMo`; `§ 516.120 RSMo Cum. Supp. 2024`; `516.120 RSMo`; `Mo. Ann. Stat. § 537.765`; `sections 516.110 and 516.120, RSMo` | `mo-rsmo-revisor` → `mo-rsmo-justia` |
| RSMo bare section (no RSMo / Mo. marker) *(only once this jurisdiction is known)* | `section 516.120`; `§ 537.765.3` | `mo-rsmo-revisor` → `mo-rsmo-justia` |
| Missouri Constitution | `Mo. Const. art. I, § 10`; `Mo. Const. art. V, sec. 10`; `Article V, Section 10 of the Missouri Constitution`; `article I, section 2 of the Missouri Constitution` | `mo-constitution-revisor` → `mo-constitution-justia` |
| Missouri Supreme Court Rules (marked) | `Mo. Sup. Ct. R. 55.27(a)(6)`; `Mo. Sup. Ct. R. 4-1.7`; `Mo. R. Civ. P. 55.27`; `Mo. R. Crim. P. 24.035`; `Missouri Supreme Court Rule 84.04`; `Rule 55.27(a)(6) of the Missouri Rules of Civil Procedure`; `Mo. R. Prof'l Conduct 4-1.7` | `mo-rules-courts` → `mo-rules-clerkhandbook` |
| Missouri Supreme Court Rules (bare "Rule 55.27", "Rule 4-1.7") *(only once this jurisdiction is known)* | `Rule 55.27(a)(6)`; `Rule 84.04(d)`; `Rule 4-1.7`; `Rule 74.04(c)` | `mo-rules-courts` → `mo-rules-clerkhandbook` |
| Missouri Code of State Regulations | `10 CSR 10-6.060`; `20 CSR 2150-2.001`; `Mo. Code Regs. Ann. tit. 10, § 10-6.060` | `mo-csr-sos` → `mo-csr-lii` |
| Missouri Register | `51 Mo. Reg. 1313`; `49 Mo. Reg. 1520 (Oct. 1, 2024)` | `mo-register-sos` |
| Reported Missouri cases (South Western Reporter) | `State v. Harris, 700 S.W.3d 100 (Mo. banc 2024)`; `Doe v. Roe, 650 S.W.3d 210, 214 (Mo. App. E.D. 2022)`; `Smith v. Jones, 600 S.W.3d 300 (Mo. App. W.D. 2020)`; `Brown v. Green, 580 S.W.3d 55 (Mo. Ct. App. 2019)`; `ITT Commercial Fin. Corp. v. Mid-Am. Marine Supply Corp., 854 S.W.2d 371 (Mo. banc 1993)`; `Emanuel v. Richards, 426 S.W.2d 716 (Mo. App. 1968)` | `mo-cases-justia` → `mo-opinions-courts` |
| Old official Missouri reporters (Mo., Mo. App.) | `353 Mo. 1146`; `240 Mo. App. 1027` | `mo-cases-justia` |
| Missouri appellate docket numbers (SC / ED / WD / SD) *(only once this jurisdiction is known)* | `SC101233`; `No. ED112690`; `WD86593`; `No. SD39269` | `mo-cases-justia` → `mo-sc-minutes` → `mo-opinions-courts` |
| Westlaw unreported cites (Missouri parenthetical) | `2024 WL 1234567 (Mo. App. E.D. Mar. 5, 2024)`; `2023 WL 456789, at *2 (Mo. banc 2023)` | `mo-cases-justia` |
| Transfer to Supreme Court of Missouri (history phrases) *(only once this jurisdiction is known)* | `transfer denied`; `application for transfer denied`; `cause ordered transferred` | `mo-sc-minutes` |

Regexes (case-insensitive):

- Revised Statutes of Missouri (RSMo): `Mo\.\s*(?:Rev|Ann)\.\s*Stat\.\s*(?:\(\d{4}\)\s*)?(?:§+\s*)?(?P<section>\d{1,3}\.\d{3,4})(?!\d)|RSMo\.?\s*(?:\(\d{4}\)\s*)?§+\s*(?P<section2>\d{1,3}\.\d{3,4})(?!\d)|(?:§+|sec(?:tion)?s?\.?)\s*(?P<section3>\d{1,3}\.\d{3,4})(?!\d)(?:\.\d+)*(?:\([0-9a-z]+\))*(?:(?:,\s*|\s+(?:and|or|to|through)\s+)\d{1,3}\.\d{3,4}(?:\.\d+)*(?:\([0-9a-z]+\))*)*,?\s+RSMo\b|(?<![\d.§])(?P<section4>\d{1,3}\.\d{3,4})(?:\.\d+)*,?\s+RSMo\b`
- RSMo bare section (no RSMo / Mo. marker): `(?:§+|sec(?:tion)?\.?)\s*(?P<section>\d{1,3}\.\d{3,4})(?!\d)(?:\.\d+)*`
- Missouri Constitution: `Mo\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*(?:§|sec\.?|section)\s*(?P<section>\d+(?:\([a-z]\))?)|Article\s+(?P<article2>[IVXL]+),?\s+(?:Section|§)\s*(?P<section2>\d+(?:\([a-z]\))?)\s+of\s+the\s+Missouri\s+Constitution`
- Missouri Supreme Court Rules (marked): `(?:Mo\.\s*Sup\.\s*Ct\.\s*R(?:ule)?\.?|Mo\.\s*R\.\s*(?:Civ|Crim|App)\.\s*P\.|Mo\.\s*R\.\s*Prof'?l\s*Conduct|Missouri\s+Supreme\s+Court\s+Rule)\s*(?P<rule>\d{1,3}-\d\.\d{1,2}|\d{1,3}(?:\.\d{1,3})?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,3})?)(?:\([0-9a-z]+\))*\s+of\s+the\s+Missouri\s+(?:Supreme\s+Court\s+)?Rules`
- Missouri Supreme Court Rules (bare "Rule 55.27", "Rule 4-1.7"): `Rules?\s+(?P<rule>\d{1,3}-\d\.\d{1,2}|\d{1,3}\.\d{2,3})(?!\d)`
- Missouri Code of State Regulations: `(?P<title>\d{1,2})\s+CSR\s+(?P<division>\d{1,4})-(?P<chapter>\d{1,3})(?:\.(?P<rule>\d{3,4}))?|Mo\.\s*Code\s+(?:of\s+State\s+)?Regs?\.\s*(?:Ann\.\s*)?tit\.\s*(?P<title2>\d{1,2}),?\s*§\s*(?P<division2>\d{1,4})-(?P<chapter2>\d{1,3})(?:\.(?P<rule2>\d{3,4}))?`
- Missouri Register: `(?P<volume>\d{1,2})\s+Mo\.\s*Reg\.\s*(?P<page>\d{1,5})`
- Reported Missouri cases (South Western Reporter): `(?P<volume>\d{1,4})\s+S\.\s*W\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>Mo\.(?:\s*banc|\s*(?:Ct\.\s*)?App\.(?:\s*[ESW]\.\s*D\.)?)?)\s*(?:[A-Z][a-z]{2,3}\.?\s+\d{1,2},\s*)?(?P<year>\d{4})\)`
- Old official Missouri reporters (Mo., Mo. App.): `(?P<volume>\d{1,3})\s+Mo\.(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4})(?!\d)`
- Missouri appellate docket numbers (SC / ED / WD / SD): `(?<![A-Z])(?P<court>SC|ED|WD|SD)\s?(?P<number>\d{5,6})(?!\d)`
- Westlaw unreported cites (Missouri parenthetical): `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Mo\.`
- Transfer to Supreme Court of Missouri (history phrases): `(?:application\s+for\s+)?transfer\s+(?:denied|sustained|granted)|ordered\s+transferred`

Short forms → URL key:

Mo. Rev. Stat. → `RSMo`; Mo. Ann. Stat. → `RSMo`; V.A.M.S. → `RSMo`; RSMo → `RSMo`; R.S.Mo. → `RSMo`; Mo. Sup. Ct. R. → `SCR`; Mo. R. Civ. P. → `SCR`; Mo. R. Crim. P. → `SCR`; Mo. R. Prof'l Conduct → `SCR`

Missouri style cites sections as 'section 516.120, RSMo 2016' or 'RSMo Cum. Supp. 2024', with subsections in dotted form (537.765.3) - trim to chapter.section for URLs. Bare 'section 516.120' (no RSMo) is context_required: chapter.section numbering is shared with other states (e.g. Minn. Stat. 609.75). Court rules are cited 'Rule 55.27(a)(6)' with no state marker (context_required); Rule 4 professional-conduct rules are cited 'Rule 4-1.7', the same shape as Florida Bar rules, so bare forms route only with Missouri context. Missouri parentheticals: '(Mo. banc 2022)' for the Supreme Court en banc, '(Mo. App. E.D. 2023)' (Missouri style) or '(Mo. Ct. App. 2023)' (Bluebook) for the Court of Appeals. No public-domain citation. Dockets: SC##### (Supreme Court), ED/WD/SD##### (Court of Appeals districts). Subsequent history 'transfer denied' is shared with other states' usage, so context_required. Supreme Court reports 'Mo.' ended 1956 and 'Mo. App.' 1952 (from memory). CourtListener ids from memory, unverified. A '§§ 516.110-516.120' range is two sections: the regex takes the first.

## A. Statutes / code

### `mo-rsmo-revisor` — Revised Statutes of Missouri (RSMo) online

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Missouri Revisor of Statutes (Joint Committee on Legislative Research) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All chapters of RSMo, current text with effective date, history, prior revisions and annotations; future-effective and multiply-enacted versions listed under 'All versions'.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://revisor.mo.gov/main/OneSection.aspx?section={section}`
  - Placeholders: {section} = chapter.section exactly as cited (516.120, 537.765, 56.067); no title or padding. Drop Missouri-style subsection suffixes before building ('537.765.3' -> 537.765; subsection 3 is in the body). Chapter page: /main/PageSelect.aspx?chapter={chapter}. Where a section has several versions (multiply enacted, future effective, or held unconstitutional) the page shows one version and an 'All versions' table whose PageSelect.aspx?section={section}&bid={bid} links open each version.
- **Automation:** WebFetch gated · shell ok · robots: no robots file: /robots.txt redirects to an HTML 'Object Moved' page -> Home.aspx (no rules); fetch_doc.py check: robots permits
  - WebFetch on a built OneSection URL (537.765) was held for a permission prompt that went unanswered (PROVENANCE_REQUIRED); use fetch_doc.py. Pages are small (7-11K chars). Help page says the site programmatically slows down 'malicious access'; the script's 1.1 s spacing was fine.
- **Currency:** Home page notices (no currency line on section pages); each section page shows 'Effective - <date>' above the text — observed: "2025 Cumulative Supplement to the 2016 Revised Statutes of Missouri is available"
- **Official status:** Home page 'CERTIFICATION STATUS' notice: statutes posted on this website are uncertified and unofficial (https://revisor.mo.gov/main/Home.aspx). The official print edition is RSMo 2016 plus cumulative supplements (2025 Cum. Supp. current).
- **Hazard:** unofficial/uncertified online text: cite RSMo by edition (RSMo 2016 / Cum. Supp.) from the effective-date line
- **Hazard:** multiply-enacted or future-effective sections: OneSection shows one version; check the 'All versions' table (bid links)
- **Hazard:** annotations (case notes) follow the statute text on the same page: stop quoting at the history line '(RSMo 1939 ...)' / '--------'
- **Hazard:** Missouri subsection style 537.765.3 must be trimmed to 537.765 for the URL
- **Probe:** Mo. Rev. Stat. § 516.120 → `https://revisor.mo.gov/main/OneSection.aspx?section=516.120` — expect: "All actions upon contracts, obligations or liabilities, express or implied"
- **Evidence (2026-10-17):** fetch_doc.py --research: 200, html 10,599 chars; header 'Title XXXV CIVIL PROCEDURE AND LIMITATIONS', 'Effective - 28 Aug 1939', '516.120. What actions within five years. — Within five years:'. Second citation 537.765 (Title XXXVI): 7,117 chars, '1. Contributory fault, as a complete bar to plaintiff's recovery'. WebFetch on 537.765: PROVENANCE_REQUIRED (gated).
- **Notes:** Other useful pages: RefsToSect.aspx?section={section} (sections citing this one); MultiEnact.aspx (all multiply-enacted sections); rx.aspx (repeal & transfer). Constitution is on the same host (mo-constitution-revisor).

### `mo-rsmo-justia` — Justia — Missouri Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual snapshots of RSMo; current edition labelled '2025 Missouri Revised Statutes'; older years (2005-2024) under /codes/missouri/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/missouri/title-{title_roman_lower}/chapter-{chapter}/section-{chapter}-{section_suffix}/`
  - Placeholders: 516.120 -> title-xxxv/chapter-516/section-516-120/ ; 537.765 -> title-xxxvi/chapter-537/section-537-765/. The title (lower-case Roman numeral) is not in the citation: read it from the revisor section page header ('Title XXXV ...') or from the /codes/missouri/2025/ index, which lists each title with its chapter range in parentheses. Title pages list chapters without section ranges.
  - Index: `https://law.justia.com/codes/missouri/2025/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com answered robots.txt with a bot check (fetch_doc.py: host off for the day, 2026-10-17)
  - Built section URLs were not gated for WebFetch.
- **Currency:** page heading — observed: "2025 Missouri Revised Statutes"
- **Official status:** Justia page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** tier 2: disclose with the '2025' edition string
- **Hazard:** title Roman numeral needed for URL (index hop)
- **Hazard:** script route refused (bot check)
- **Probe:** Mo. Rev. Stat. § 516.120 → `https://law.justia.com/codes/missouri/title-xxxv/chapter-516/section-516-120/` — expect: "Within five years: (1) All actions upon contracts, obligations or"
- **Evidence (2026-10-17):** WebFetch: YES, body 'Within five years: (1) All actions upon contracts, obligations or'; '2025 Missouri Revised Statutes'; not truncated. Second citation 537.765 at /title-xxxvi/chapter-537/section-537-765/: 'Contributory fault, as a complete bar to plaintiff's recovery in'.

## B. Constitution

### `mo-constitution-revisor` — Constitution of Missouri (revisor.mo.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Missouri Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1945 as amended, per section, with source notes, effective dates and annotations.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://revisor.mo.gov/main/OneSection.aspx?section={article}%20%20%20%20{section}&constit=y`
  - Placeholders: {article} = upper-case Roman numeral, then exactly four spaces (%20 x4), then the section number as printed, with letter suffix in parentheses where used (I 18(a), I 22(a)). Whole article: https://revisor.mo.gov/main/ViewChapter.aspx?chapter={article}&constit=y (Art. I = 138K chars). Index: Home.aspx?constit=y lists every section link (PageSelect.aspx?section=I    10&bid=...&constit=y).
  - Index: `https://revisor.mo.gov/main/Home.aspx?constit=y`
- **Automation:** WebFetch gated · shell ok · robots: no robots file (redirect to Home.aspx)
  - Built URLs gated for WebFetch (same host as mo-rsmo-revisor); use fetch_doc.py. Whole-article pages exceed WebFetch's ~100K window (Art. I 138,558 chars).
- **Currency:** each section page: 'Constitution Effective - <date>' line — observed: "Effective - 27 Feb 1945, see footnote"
- **Official status:** Same site-wide certification notice as RSMo: posted text is uncertified and unofficial (https://revisor.mo.gov/main/Home.aspx).
- **Hazard:** four-space padding inside the section parameter
- **Hazard:** whole-article pages are long (Art. I 138K chars)
- **Hazard:** annotations follow the text
- **Probe:** Mo. Const. art. I, § 10 → `https://revisor.mo.gov/main/OneSection.aspx?section=I%20%20%20%2010&constit=y` — expect: "That no person shall be deprived of life, liberty or property"
- **Evidence (2026-10-17):** fetch_doc.py: 28,795 chars; 'I Section 10. Due process of law. — That no person shall be deprived of life'. Second: Art. V § 10 (V%20%20%20%2010): 'Transfer of cases from court of appeals to supreme court', effective 02 Sep 1976.

### `mo-constitution-justia` — Justia — Missouri Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of Missouri per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/missouri/article-{article_roman_lower}/section-{section}/`
  - Placeholders: Art. I § 10 -> article-i/section-10/. Lettered sections not tested.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py)
- **Currency:** none stated beyond disclaimer — observed: "This Constitution may not be the most recent version."
- **Official status:** Page note: 'This Constitution may not be the most recent version.'
- **Hazard:** tier 2
- **Hazard:** lettered-section slugs unverified
- **Probe:** Mo. Const. art. I, § 10 → `https://law.justia.com/constitution/missouri/article-i/section-10/` — expect: "That no person shall be deprived of life, liberty or"
- **Evidence (2026-10-17):** WebFetch: YES, 'That no person shall be deprived of life, liberty or'; 'Source: Const. of 1875, Art. I, Sec. 30.'; not truncated.

## C. Court rules

### `mo-rules-clerkhandbook` — Clerk Handbooks — Supreme Court Rules database (courts.mo.gov Domino)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Office of State Courts Administrator · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court Rules, one document per rule subdivision, with Subject, Adopted date and 'Revised / Effective Date'; latest effective date seen September 3, 2024 (repeal of 16.07).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.courts.mo.gov/courts/ClerkHandbooksP2RulesOnly.nsf/c0c6ffa99df4993f86256ba50057dcb8?SearchView&Query=%22{rule}%22&Count=100`
  - Placeholders: {rule} as cited (55.27, 84.04, 4-1.7). The GET search returns a result list; follow the link whose text equals the rule number. Rule 4 labels are spaced: '4- 1. 7', '4- 1.10'. Direct key URLs (/{view}/55.27?OpenDocument) 404.
- **Automation:** WebFetch untested · shell ok · robots: courts.mo.gov robots.txt does not disallow /courts/
  - Domino ?SearchView is a plain GET. Not tested with WebFetch (budget).
- **Currency:** each document's header field — observed: "Revised / Effective Date: January 1, 2012"
- **Official status:** Staff reference database ('Clerk Handbooks'); no official-status statement. Treat as a mirror of the rules; check its 'Revised / Effective Date' against the official page's 'Most Recently Effective'.
- **Hazard:** may lag the official rule pages (secondary staff copy)
- **Hazard:** search results ranked by relevance, not rule number
- **Probe:** Rule 55.27(a)(6) → `https://www.courts.mo.gov/courts/ClerkHandbooksP2RulesOnly.nsf/c0c6ffa99df4993f86256ba50057dcb8/a9fdabe676220f8986256ca600521544` — expect: "Failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** fetch_doc.py: 6,571 chars; '55.27. Defenses and Objections ... (a) How Presented. Every defense, in law or fact'; Revised/Effective January 1, 2012 (matches official page). SearchView Query=55.27 -> 55.27 link first. Second: 84.04 (Revised/Effective January 1, 2018) and 4-1.7 doc d06710dff1830d2686256ca600521205 ('RULE 4-1.7: CONFLICT OF INTEREST: CURRENT CLIENTS', July 1, 2007).

### `mo-rules-courts` — Missouri Supreme Court Rules (per-rule pages, courts.mo.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Missouri / Office of State Courts Administrator · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All Supreme Court Rules: Rules 1-18 (Bar and Judiciary; Rule 4 = Rules of Professional Conduct, cited 4-1.7), civil procedure 41-101, criminal procedure 19-36, juvenile, probate, etc. One page per rule subdivision (55.27, 84.04, 4-1.7) with comments and adoption history.
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format html
  - Index: `https://www.courts.mo.gov/page.jsp?id=58122`
  - Navigation: Rule pages are page.jsp?id={opaque id} (55.27 = id 199658; 4-1.7 = id 198912); ids cannot be built from the rule number and the index's tree links are not visible to WebFetch. Locate by WebSearch 'courts.mo.gov Rule {n} {heading words}', or find the rule in mo-rules-clerkhandbook (script GET search) and then search for the official page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: User-agent: * Disallow: /cnet/ /casenet/ /ecf/ /fv/ /bench/ and '/page.jsp?id=236' (prefix: also covers ids 236xxxx under case-insensitive prefix matching); a comment forbids data-scraper software. Rule pages (ids 198xxx-199xxx) are not covered.
  - fetch_doc.py: HTTP 403 on page.jsp (WAF refusal; .nsf paths on the same host return 200). www2.courts.mo.gov mirror fails TLS (hostname mismatch) - not used.
- **Currency:** each rule page, under the heading — observed: "Most Recently Effective: January 01, 2012"
- **Official status:** Rules index page (https://www.courts.mo.gov/page.jsp?id=58122) says the compilation is not considered an official document of the Supreme Court; the Court's orders are official.
- **Hazard:** page ids opaque (search hop)
- **Hazard:** script refused (403)
- **Hazard:** index tree links not readable by WebFetch
- **Probe:** Rule 55.27 → `https://www.courts.mo.gov/page.jsp?id=199658` — expect: "Every defense, in law or fact, to a claim in"
- **Evidence (2026-10-17):** WebFetch: YES, Rule 55.27 body 'Every defense, in law or fact, to a claim in'; 'Most Recently Effective: January 01, 2012'; not truncated. Second: Rule 4-1.7 (id 198912): '(a) Except as provided in Rule 4-1.7(b), a lawyer shall'; 'Most Recently Effective: July 01, 2007'. fetch_doc.py: HTTP 403 REFUSED.

## D. Administrative code

### `mo-csr-sos` — Code of State Regulations (CSR)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Missouri Secretary of State, Administrative Rules Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** All 20+ titles, current edition, one PDF per division chapter; archived editions linked per title.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.sos.mo.gov/cmsimages/adrules/csr/current/{title}csr/{title}c{division}-{chapter}.pdf`
  - Placeholders: 10 CSR 10-6.060 -> 10csr/10c10-6.pdf ; 20 CSR 2150-2.001 -> 20csr/20c2150-2.pdf. Some files carry a suffix (10c20-7a.pdf), so confirm on the title index. Path case varies in links (CMSImages/AdRules vs cmsimages/adrules); both served.
  - Index: `https://www.sos.mo.gov/adrules/csr/current/{title}csr/{title}csr`
  - Navigation: title index (e.g. /adrules/csr/current/10csr/10csr) -> 'Chapter N' link under the division heading -> chapter PDF -> find the rule heading '{title} CSR {division}-{chapter}.{rule}'.
- **Automation:** WebFetch gated · shell ok · robots: curl of /robots.txt through the proxy got a Cloudflare 'Just a moment...' page; fetch_doc.py check reported robots permits and fetched pages and PDFs without a challenge.
  - Chapter PDFs are long (10c10-6 = 164 pages, 1.27M chars) and two-column: extracted text interleaves columns, so quote with fetch_doc.py verify on short spans or ingest with layout extraction.
- **Currency:** footer of every PDF page: Secretary of State name and date — observed: "Denny Hoskins (6/30/26) CODE OF STATE REGULATIONS"
- **Official status:** No certification statement found on the title index; each PDF page carries the Secretary of State's name and an update date.
- **Hazard:** two-column PDF: column interleaving in extracted text
- **Hazard:** very long chapter PDFs exceed WebFetch window
- **Hazard:** irregular file suffixes (10c20-7a)
- **Hazard:** possible Cloudflare challenge for some clients
- **Probe:** 10 CSR 10-6.060 → `https://www.sos.mo.gov/CMSImages/AdRules/csr/current/10csr/10c10-6.pdf` — expect: "PURPOSE: This rule defines sources required to obtain permits"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 164 pp, 1,275,288 chars, last-modified 22 Jun 2026; heading '10 CSR 10-6.060 Construction Permits Required' at p.41 with 'PURPOSE: This rule defines sources required to obtain permits'. Second: 20 CSR 2150-2.001 in 20c2150-2.pdf (28 pp): 'PURPOSE: This rule defines terms used in Chapter 334, RSMo'. Footer '(5/31/26)'. WebFetch on title index: gated.

### `mo-csr-lii` — Cornell LII — Missouri Code of State Regulations

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-rule HTML pages for the CSR.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/missouri/{title}-CSR-{division}-{chapter}-{rule}`
  - Placeholders: 10 CSR 10-6.060 -> 10-CSR-10-6-060 ; 20 CSR 2150-2.001 -> 20-CSR-2150-2-001 (dot becomes hyphen).
- **Automation:** WebFetch untested · shell ok · robots: permits (fetch_doc.py check)
  - Last-Modified headers Aug 2025: may lag the SOS PDFs.
- **Currency:** none on page; HTTP Last-Modified only — observed: "Last-Modified: Sun, 03 Aug 2025"
- **Official status:** Third-party compilation.
- **Hazard:** tier 2; possibly stale (Aug 2025)
- **Probe:** 10 CSR 10-6.060 → `https://www.law.cornell.edu/regulations/missouri/10-CSR-10-6-060` — expect: "PURPOSE: This rule defines sources required to obtain permits to construct"
- **Evidence (2026-10-17):** fetch_doc.py: 90,554 chars; '10 CSR 10-6.060 - Construction Permits Required ... PURPOSE: This rule defines'. Second: 20-CSR-2150-2-001: 'PURPOSE: This rule defines terms used in Chapter 334, RSMo'.

## D. Administrative register

### `mo-register-sos` — Missouri Register

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Missouri Secretary of State, Administrative Rules Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** Semi-monthly issues; year pages listed back to 2007 on the Register index; current Volume 51 (2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.sos.mo.gov/adrules/moreg/moreg`
  - Navigation: Register index -> year page (/adrules/moreg/{year}) or latest issue link -> issue page /adrules/moreg/{year}/v{vol}/n{num} shows 'Volume V, Number N (Pages a-b)' -> PDF (e.g. /CMSImages/AdRules/moreg/2026/v51n20Oct15/v51n20.pdf). To resolve '51 Mo. Reg. 1313' pick the issue whose page range contains the page.
- **Automation:** WebFetch untested · shell ok · robots: as mo-csr-sos
  - fetch_doc.py links on /adrules/moreg/2026 returned only sidebar links (issue list may be script-rendered); the index page's latest-issue link worked.
- **Currency:** PDF cover — observed: "Volume 51, Number 20 October 15, 2026 Pages 1313–1404"
- **Official status:** Published by the Secretary of State; no certification statement seen.
- **Hazard:** year pages may not expose issue links to a plain fetch
- **Hazard:** issue PDF file names include a date slug (v51n20Oct15) - not constructible
- **Probe:** 51 Mo. Reg. 1313 → `https://www.sos.mo.gov/CMSImages/AdRules/moreg/2026/v51n20Oct15/v51n20.pdf` — expect: "Volume 51, Number 20 October 15, 2026 Pages 1313"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 92 pp, 671,011 chars, last-modified 07 Oct 2026; cover 'Volume 51, Number 20 October 15, 2026 Pages 1313–1404'. Located via /adrules/moreg/moreg -> /adrules/moreg/2026/v51/n20.

## E. Case law

### `mo-opinions-courts` — Missouri appellate opinions (courts.mo.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Supreme Court of Missouri / Missouri Court of Appeals · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals (Eastern, Western, Southern Districts) opinions as PDFs (file.jsp?id=N); separate opinions follow the majority in the same PDF.
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.courts.mo.gov/page.jsp?id=1944`
  - Navigation: Supreme Court: minutes view (mo-sc-minutes) lists each hand-down with links to https://www.courts.mo.gov/file.jsp?id={n}. Court of Appeals: listing page.jsp?id=12086&dist=Opinions%20{District}&date=all (reported; WebFetch error).
  - Read via: file.jsp PDFs refused to fetch_doc.py (403) and errored in WebFetch for 2026 opinions; read the same opinion on mo-cases-justia.
- **Automation:** WebFetch fail · shell blocked-challenge · robots: file.jsp not disallowed; '/page.jsp?id=236' disallowed (prefix)
  - fetch_doc.py: HTTP 403 on file.jsp?id=236410 and on page.jsp. WebFetch: file.jsp?id=236410 and 236411 (June 2026 SC opinions) 'error while fetching'; file.jsp?id=214050 (a 2024 WD motion-rulings PDF) did read. Opinion listing page.jsp?id=12086 errored.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Slip opinions; official reporter is S.W.3d (West).
- **Hazard:** script refused (403)
- **Hazard:** WebFetch errors on opinion PDFs
- **Hazard:** slip pagination only
- **Probe:** State v. Harris, No. SC101233 (Mo. banc June 23, 2026) → `https://www.courts.mo.gov/file.jsp?id=236410` — expect: "In his sole point on appeal, Harris contends"
- **Evidence (2026-10-17):** fetch_doc.py: 'refused: HTTP 403' (file.jsp?id=236410, page.jsp?id=58122, 103681). WebFetch: CLIENT_ERROR 'error while fetching' on file.jsp?id=236410, 236411 and page.jsp?id=12086 listing.
- **Notes:** Link to these PDFs as the official slip opinion when the minutes give the id; quote from Justia.

### `mo-cases-justia` — Justia — Missouri Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1852-2026; Court of Appeals 1891-2026 (year listings). Modern pages carry slip pagination, no S.W.3d cite.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/missouri/{court}/{year}/{docket_lower}.html`
  - Placeholders: {court} = supreme-court | court-of-appeals; {docket_lower} = sc101233, ed112690, wd86593, sd39269; {year} = decision year. Year listing https://law.justia.com/cases/missouri/{court}/{year}/ (500 per page, ?page=2) to confirm. Older (pre-~2000) slugs not verified. A built SD URL with a guessed year (2026/sd39269) errored: confirm the year from the listing.
  - Index: `https://law.justia.com/cases/missouri/court-of-appeals/2024/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py)
  - PDF copy linked as cases.justia.com/missouri/{court}/{year}-{docket}.pdf?ts=...
- **Currency:** listing heading — observed: "Missouri Court of Appeals Decisions 2024"
- **Official status:** Third-party copy of the courts' slip opinions (PDF copy at cases.justia.com).
- **Hazard:** tier 2
- **Hazard:** slip pagination only
- **Hazard:** decision year required in URL
- **Probe:** State v. Harris, No. SC101233 (Mo. banc June 23, 2026) → `https://law.justia.com/cases/missouri/supreme-court/2026/sc101233.html` — expect: "In his sole point on appeal, Harris contends the circuit court"
- **Evidence (2026-10-17):** WebFetch: YES, 'In his sole point on appeal, Harris contends the circuit court'; slip pp. 1-16; not truncated. Second: court-of-appeals/2024/ed112690.html 'Mary Beth Fryman sued The Board of Regents of Southeast Missouri State'.

## F. Subsequent history

### `mo-coa-minutes` — Missouri Court of Appeals post-opinion motion minutes (Western District)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Missouri Court of Appeals, Western District · text: **link-only** · official: official
- **Coverage:** Post-Opinion Motion Rulings listed by date (Oct 2024 - June 2025 seen); PDFs via file.jsp.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.courts.mo.gov/page.jsp?id=2557`
  - Navigation: page lists 'Post-Opinion Motion Rulings of <date>' -> PDF (file.jsp?id=N) listing WD docket numbers. Eastern/Southern District equivalents not located.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: not disallowed
  - fetch_doc.py 403 on page.jsp; WebFetch read the page and one ruling PDF (file.jsp?id=214050).
- **Currency:** list — observed: "Post-Opinion Motion Rulings of October 1, 2024"
- **Official status:** Court's own post-opinion motion rulings (rehearing / transfer-to-Supreme-Court motions).
- **Hazard:** only Western District found
- **Hazard:** script refused (403)
- **Probe:** WD85884 post-opinion motions → `https://www.courts.mo.gov/file.jsp?id=214050` — expect: "Motion Rulings"
- **Evidence (2026-10-17):** WebFetch: page.jsp?id=2557 'Missouri Court of Appeals – Western District Minutes'; file.jsp?id=214050 = Motion Rulings report Oct 29, 2024 listing WD85884 ... WD86806.

### `mo-sc-minutes` — Supreme Court of Missouri minutes (hand-downs, transfers, writs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Missouri · text: **fetch-and-quote** · official: official
- **Coverage:** Minutes from May 1998 to date (643 entries in the view): opinions handed down (with file.jsp links) and 'Applications for Transfer' dispositions, each naming the Court of Appeals docket (e.g. 'transfer from the Missouri Court of Appeals, ED113496, denied').
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Index: `https://www.courts.mo.gov/SUP/index.nsf/cfc8c4b5bc15cb158625661d0073593c?OpenView&Start=1&Count=1000`
  - Navigation: view lists 'Minutes of <date>' links newest first -> minutes page -> grep for the Court of Appeals docket (ED/WD/SD number) or SC number. Transfer applications are decided weeks after the appeals opinion: scan minutes dated 1-3 months after it. Domino ?SearchView returned no hits (full-text index not usable).
- **Automation:** WebFetch untested · shell ok · robots: /SUP/ not disallowed
  - Domino .nsf pages return 200 to fetch_doc.py although page.jsp/file.jsp return 403.
- **Currency:** view lists newest minutes first — observed: "Minutes of September 29, 2026"
- **Official status:** The Court's own minutes, signed by the Chief Justice; courts.mo.gov opinions page says minutes cover rehearing motions, transfer applications and writ petitions.
- **Hazard:** no docket search: date-window scan
- **Hazard:** opinion links point to file.jsp (refused to script)
- **Probe:** CBAM, LLC v. ALPS Acquisitions, LLC, ED113496, transfer denied → `https://www.courts.mo.gov/SUP/index.nsf/cfc8c4b5bc15cb158625661d0073593c/a984ebacb282c9d786258e810054d46d?OpenDocument` — expect: "application for transfer from the Missouri Court of Appeals, ED113496, denied"
- **Evidence (2026-10-17):** fetch_doc.py: minutes of Sept 29, 2026, 6,791 chars; 'Applications for Transfer and Recommendations for Transfer' with ED113496, SD39269, WD87003 denials. View: 643 minutes, oldest 'Minutes of May 26, 1998'. Minutes of June 23, 2026 list SC101233 with link file.jsp?id=236410.

## Not available (do not look for these again)

- **case_law** — Public-domain (vendor-neutral) citation format: Missouri cites S.W.3d with (Mo. banc YYYY)/(Mo. App. X.D. YYYY); court PDFs and Justia pages carry only slip pagination and docket numbers. (2026-10-17)
- **case_law** — Free official reporter pagination (S.W.3d): Justia SC101233 and ED112690 pages: slip pagination only, no S.W.3d cite. (2026-10-17)
- **statutes** — Official bulk download / API for RSMo: revisor.mo.gov Info.aspx offers print publications and Appendices/Tables PDFs only; DwnLD.aspx returned an empty page to fetch_doc.py. (2026-10-17)
- **statutes** — Certified/authenticated online RSMo: Home page: 'Currently the statutes posted on this website are uncertified and unofficial'. (2026-10-17)

## Corpus candidates (maintainers)

- `mo-csr-sos` — 164-page two-column chapter PDF (1.27M chars), far beyond WebFetch's window; column interleaving in plain extraction
- `mo-register-sos` — 92-page issue PDF (671K chars); page-cited (51 Mo. Reg. 1313)
- `mo-constitution-revisor` — whole-article pages exceed ~100K chars (Art. I 138K); per-section URLs avoid this, so low priority

## Open questions

- Court of Appeals opinion listings (page.jsp?id=12086&dist=...) and recent opinion PDFs (file.jsp) failed in WebFetch and 403 in the script: re-test whether this is a transient error or a durable refusal.
- Session laws (Laws of Missouri) and bill text (house.mo.gov / senate.mo.gov) not probed.
- missouri.public.law unreachable (proxy 502 on robots.txt) - existence of a public.law Missouri edition unconfirmed.
- Eastern and Southern District post-opinion motion minutes not located.
- Clerk Handbooks rules database currency vs official rule pages: check a rule amended after Sept 2024.
- Justia case slugs before ~2000 not verified.

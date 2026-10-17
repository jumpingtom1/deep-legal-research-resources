# Utah (UT) — free legal sources

_Generated from `data/ut.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: le.utah.gov (Utah Legislature). Each section URL serves a JavaScript shell; the text sits in a versioned file (C{title}-{chapter}-S{section}_{effective}.html) whose name you reach by following index hops. fetch_doc.py reads those files, and also the per-title PDFs (Title 78B: 456 pp). Justia 2025 is a constructible tier-2 fallback that WebFetch reads. Constitution: le.utah.gov uses the same versioned-file scheme. Court rules: legacy.utcourts.gov/rules/view.php gives one constructible HTML page per rule for every rule set. Admin Code: adminrules.utah.gov is a JavaScript app with no text for the script; Cornell LII has constructible per-section pages, and the Utah State Bulletin PDFs on rules.utah.gov are readable. Case law: utcourts.gov opinion PDFs are disallowed by robots.txt, so read opinions on Justia (public-domain cites with ¶ numbers). Certiorari dispositions are in bimonthly PDFs on www.utcourts.gov, listed by Court of Appeals docket number.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Utah Supreme Court | `utah (unverified)` | Utah | P.3d, P.2d, Utah 2d, Utah | 2019 UT 12, ¶ 15 (since 1999) |
| Utah Court of Appeals | `utahctapp (unverified)` | Utah Ct. App. | P.3d, P.2d | 2020 UT App 45, ¶ 10 (since 1999) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Utah Code | `Utah Code Ann. § 78B-2-307`; `Utah Code § 78B-2-307(1)(a)`; `Utah Code Ann. section 76-5-203`; `U.C.A. § 41-6a-502`; `section 78B-2-307 of the Utah Code`; `Utah Code Ann. §§ 78B-2-301 to -307` | `ut-code-le` → `ut-code-justia` |
| Laws of Utah (session laws) | `2023 Utah Laws ch. 185`; `Laws of Utah 2023, ch. 185`; `Chapter 185, 2023 General Session` | `ut-session-laws` |
| Utah Constitution | `Utah Const. art. I, § 11`; `Utah Const. art. VIII, § 3`; `Article I, Section 11 of the Utah Constitution` | `ut-constitution-le` → `ut-constitution-justia` |
| Utah Rules of Civil Procedure | `Utah R. Civ. P. 12(b)(6)`; `URCP 56`; `Rule 12(b)(6) of the Utah Rules of Civil Procedure` | `ut-rules-utcourts` |
| Utah Rules of Evidence | `Utah R. Evid. 702`; `URE 403`; `Rule 702 of the Utah Rules of Evidence` | `ut-rules-utcourts` |
| Utah Rules of Appellate Procedure | `Utah R. App. P. 24(a)`; `URAP 24`; `Rule 24 of the Utah Rules of Appellate Procedure` | `ut-rules-utcourts` |
| Utah Rules of Criminal Procedure | `Utah R. Crim. P. 11`; `URCrP 11(e)`; `Rule 11 of the Utah Rules of Criminal Procedure` | `ut-rules-utcourts` |
| Utah Code of Judicial Administration | `Utah Code Jud. Admin. R4-202.02`; `UCJA 4-202.02`; `rule 4-202.02 of the Utah Code of Judicial Administration` | `ut-rules-utcourts` |
| Utah Rules of Professional Conduct (Supreme Court Rules of Professional Practice ch. 3) | `Utah R. Prof'l Conduct 1.7`; `Utah Rules of Professional Conduct 1.10`; `Rule 1.7 of the Utah Rules of Professional Conduct` | `ut-rules-utcourts` |
| Utah Administrative Code | `Utah Admin. Code R414-1-1`; `Utah Admin. Code r. R307-101-2`; `Utah Administrative Code R414-1` | `ut-admincode-lii` → `ut-admincode-oar` |
| Utah State Bulletin | `Utah State Bulletin Number 2025-05`; `Utah State Bulletin No. 2026-19` | `ut-bulletin` |
| Utah public-domain citations (since 1999) | `2019 UT 12, ¶ 15`; `2025 UT 59`; `2020 UT App 45`; `State v. Leatham, 2025 UT App 194, ¶ 10`; `2008 UT App 400U` | `ut-cases-justia` → `ut-opinions-utcourts` |
| Pacific Reporter / Utah Reports with Utah parenthetical | `Jones v. Smith, 123 P.3d 456 (Utah 2005)`; `456 P.2d 789 (Utah Ct. App. 1995)`; `28 Utah 2d 115` | `ut-cases-justia` |
| Utah appellate docket numbers *(only once this jurisdiction is known)* | `No. 20230556`; `No. 20230824-CA`; `20250519-SC` | `ut-cases-justia` → `ut-cert-petitions` |
| Utah certiorari history | `cert. denied, 566 P.3d 796 (Utah 2025)`; `cert. granted, 569 P.3d 238 (Utah 2025)` | `ut-cert-petitions` |

Regexes (case-insensitive):

- Utah Code: `(?:Utah\s+Code(?:\s+Ann(?:otated|\.)?)?|U\.\s*C\.\s*A\.)\s*(?:§+|sec(?:tion|\.)|)\s*(?P<title>\d{1,2}[A-Za-z]?)-(?P<chapter>\d{1,3}[A-Za-z]?)-(?P<section>\d{1,4}(?:\.\d+)?)(?![\d-])|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2}[A-Za-z]?)-(?P<chapter2>\d{1,3}[A-Za-z]?)-(?P<section2>\d{1,4}(?:\.\d+)?)(?:\([a-zA-Z0-9]+\))*\s+of\s+the\s+Utah\s+Code`
- Laws of Utah (session laws): `(?P<year>(?:19|20)\d\d)\s+Utah\s+Laws,?\s*(?:ch\.|c\.|chapter)\s*(?P<chapter>\d+)|Laws\s+of\s+Utah\s+(?P<year2>(?:19|20)\d\d),?\s*(?:ch\.|chapter)\s*(?P<chapter2>\d+)|Chapter\s+(?P<chapter3>\d+),\s+(?P<year3>(?:19|20)\d\d)\s+(?:General|First\s+Special|Second\s+Special|Third\s+Special|Fourth\s+Special|Fifth\s+Special)\s+Session`
- Utah Constitution: `Utah\s+Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+[A-Za-z]?)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+Utah\s+Constitution`
- Utah Rules of Civil Procedure: `(?:Utah\s+R\.\s*Civ\.\s*P\.|URCP)\s*(?P<rule>\d+[A-Z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[A-Z]?(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Utah\s+Rules\s+of\s+Civil\s+Procedure`
- Utah Rules of Evidence: `(?:Utah\s+R\.\s*Evid\.|URE)\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Utah\s+Rules\s+of\s+Evidence`
- Utah Rules of Appellate Procedure: `(?:Utah\s+R\.\s*App\.\s*P\.|URAP)\s*(?P<rule>\d+[A-Z]?)|Rule\s+(?P<rule2>\d+[A-Z]?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Utah\s+Rules\s+of\s+Appellate\s+Procedure`
- Utah Rules of Criminal Procedure: `(?:Utah\s+R\.\s*Crim\.\s*P\.|URCrP)\s*(?P<rule>\d+[A-Z]?)|Rule\s+(?P<rule2>\d+[A-Z]?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Utah\s+Rules\s+of\s+Criminal\s+Procedure`
- Utah Code of Judicial Administration: `(?:Utah\s+Code\s+Jud(?:icial|\.)\s*Admin(?:istration|\.)?|UCJA)\s*(?:R(?:ule)?\.?\s*)?(?P<rule>\d{1,2}-\d{3}(?:\.\d{2})?)|[Rr]ule\s+(?P<rule2>\d{1,2}-\d{3}(?:\.\d{2})?)\s+of\s+the\s+Utah\s+Code\s+of\s+Judicial\s+Administration`
- Utah Rules of Professional Conduct (Supreme Court Rules of Professional Practice ch. 3): `Utah\s+(?:R\.\s*Prof(?:'|’)?l\s*Conduct|Rules?\s+of\s+Prof(?:essional|'l)\s+Conduct)\s*(?:R(?:ule)?\.?\s*)?(?P<rule>\d\.\d{1,2})|Rule\s+(?P<rule2>\d\.\d{1,2})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Utah\s+Rules\s+of\s+Professional\s+Conduct`
- Utah Administrative Code: `Utah\s+Admin(?:istrative|\.)\s+Code\s*(?:r\.\s*)?(?:§\s*)?(?P<rule>R\d{2,4}-\d+[A-Za-z]?)(?:-(?P<section>\d+[a-z]?))?`
- Utah State Bulletin: `Utah\s+State\s+Bulletin,?\s*(?:Number|No\.)\s*(?P<year>(?:19|20)\d\d)-(?P<issue>\d{1,2})`
- Utah public-domain citations (since 1999): `(?P<year>(?:19|20)\d\d)\s+UT\s+(?P<app>App\s+)?(?P<number>\d{1,3})(?P<unpub>U)?(?:,\s*¶+\s*(?P<para>\d+))?`
- Pacific Reporter / Utah Reports with Utah parenthetical: `(?P<volume>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Utah(?:\s+Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)|(?P<uvol>\d{1,3})\s+Utah(?:\s+2d)?\s+(?P<upage>\d{1,4})(?!\d)`
- Utah appellate docket numbers: `(?:No\.\s*)?(?P<docket>(?:19|20)\d{6})(?:-(?P<court>CA|SC))?`
- Utah certiorari history: `cert\.\s+(?P<disposition>denied|granted|dismissed),?\s+(?P<volume>\d{1,4})\s+P\.\s*(?P<series>[23])d\s+(?P<page>\d{1,5})\s*\(Utah\s+(?P<year>\d{4})\)`

Short forms → URL key:

Utah R. Civ. P. → `urcp`; URCP → `urcp`; Utah R. Evid. → `ure`; URE → `ure`; Utah R. App. P. → `urap`; URAP → `urap`; Utah R. Crim. P. → `urcrp`; URCrP → `urcrp`; Utah R. Juv. P. → `urjp`; URJP → `urjp`; Utah R. Small Claims P. → `srpe`; Utah Code Jud. Admin. → `ucja`; UCJA → `ucja`; Utah R. Prof'l Conduct → `scrp`; Utah Rules of Professional Conduct → `scrp`; Utah Sup. Ct. R. Prof'l Prac. → `scrp`; Utah R. Bus. & Chancery Ct. P. → `urbcp`; URBCP → `urbcp`

Utah adopted public-domain citations in 1999 (YYYY UT N for the Supreme Court, YYYY UT App N for the Court of Appeals). Pinpoints are paragraph cites (¶ N), and the P.2d/P.3d parallel cite follows. Court of Appeals memorandum decisions take UT App numbers too. Pre-2011 'unpublished decisions' are usually cited with a trailing U (e.g. 2008 UT App 400U); that form is from memory and unverified. Bare 'UT' is distinctive to Utah. Statute section numbers have three parts, TITLE-CHAPTER-SECTION, and title and chapter can carry a letter (78B-2-307, 41-6a-502, 26B-3-102). Other states (e.g. Colorado C.R.S. 13-80-102) use similar three-part numbers, so the statute regex requires 'Utah Code' or 'U.C.A.' first. A range like '§§ 78B-2-301 to -307' matches only the first section. 'Utah Code Jud. Admin.' and 'UCJA' are court rules, not statutes: the statute regex does not match them, because a section number must follow 'Utah Code' directly. Bare 'Rule 12' or 'Rule 702' must not route here without 'Utah' context. Rules of Professional Conduct are numbered N.N in citations, but the URL key is scrp rule 3-N.0N (Rule 1.7 → 3-1.07; Rule 1.10 → 3-1.10 unverified). Admin Code citations begin with an R number (R414-1-1). A bare 'R414-1-1' is not routed without 'Utah Admin. Code'. Docket numbers are 8 digits (filing year + sequence), sometimes with a -CA or -SC suffix; they are generic and context_required. CourtListener ids (utah, utahctapp) are from memory. Georgia's 'Code Section NN-N-NNN' pattern also matches the prose form 'Utah Code section 76-5-203' (case-insensitive), so an explicit 'Utah' marker must win in routing.

## A. Statutes / code

### `ut-code-le` — Utah Code (le.utah.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah State Legislature, Office of Legislative Research and General Counsel · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole Utah Code (Titles 3–81) with the current version of each section and an effective date. The per-section version files offer PDF, RTF and XML downloads, and the per-title PDFs hold whole titles.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://le.utah.gov/xcode/Title{title}/Chapter{chapter_upper}/{title}-{chapter}-S{section}.html  (JS shell; text in https://le.utah.gov/xcode/Title{title}/Chapter{chapter_upper}/C{title}-{chapter}-S{section}_{version}.html)`
  - Placeholders: The shell URL is constructible. Title is written as cited (78B, 26B), chapter folder upper-case (Chapter6A), file name keeps the citation's case (41-6a-S102): e.g. 78B-2-307 → /xcode/Title78B/Chapter2/78B-2-S307.html; 41-6a-102 → /xcode/Title41/Chapter6A/41-6a-S102.html. The shell has NO text: its JavaScript sets versionDefault="C78B-2-S307_2023050320230503", and the text lives in that file name + .html in the same folder. {version} is two 8-digit dates (YYYYMMDD twice; 1800010118000101 = unamended since recodification). It cannot be derived from the citation. fetch_doc.py strips scripts, so it cannot read versionDefault. Get the version id from the Part (or Chapter) index file's section link instead: '78B-2-S307.html?v=C78B-2-S307_2023050320230503'. Part number = the section's hundreds digit (307 → P3) in most chapters.
  - Index: `https://le.utah.gov/xcode/C_1800010118000101.html`
  - Navigation: Code index file C_1800010118000101.html → Title link '?v=C78B_1800010118000101' → fetch /xcode/Title78B/C78B_1800010118000101.html → Chapter link '?v=C78B-2_…' → fetch /xcode/Title78B/Chapter2/C78B-2_1800010118000101.html (lists Parts, no section ranges) → Part link '?v=C78B-2-P3_…' → fetch C78B-2-P3_1800010118000101.html (lists every section with its ?v= id) → fetch C78B-2-S307_2023050320230503.html (body). Rule: take the ?v= value, append .html, and fetch it in the same folder. Chapters without parts list their sections directly.
- **Automation:** WebFetch gated · shell ok · robots: User-agent * Crawl-delay: 10; Disallow /templates/, /ASP/, /asp/, /includes/, /JSP/, /RSS/ — /xcode/ allowed
  - WebFetch on the shell URL returned PROVENANCE_REQUIRED (permission not answered). The shell would give WebFetch no text anyway. Version files are small (about 2–5K chars) and fetch_doc.py reads them in full. XML per section (C…_{version}.xml) gives clean text with history ('Amended by Chapter 185, 2023 General Session'). The whole-title PDF (C78B_1800010118000101.pdf) is 456 pp and 1.5M chars.
- **Currency:** per-section version file, under the section heading; no code-wide 'current through' string found — observed: "Effective 5/3/2023"
- **Official status:** https://le.utah.gov/documents/disclaimer.htm: the Legislature 'attempt[s] to ensure' the online information is accurate and gives access on a strictly 'as is' basis. No UELMA authentication statement was found.
- **Hazard:** per-section URL is a JavaScript shell with no text: fetch the versioned C…_{version}.html file
- **Hazard:** version id not derivable from the citation; needs the Part/Chapter index hop
- **Hazard:** chapter folder upper-case vs. file name lower-case letters (Chapter6A / 41-6a-S102)
- **Hazard:** no code-wide currency statement; only per-section effective dates
- **Hazard:** future-effective versions may exist beside the current one; check the 'Effective' date
- **Probe:** Utah Code Ann. § 78B-2-307 → `https://le.utah.gov/xcode/Title78B/Chapter2/C78B-2-S307_2023050320230503.html` — expect: "An action may be brought within four years:"
- **Evidence (2026-10-17):** fetch_doc.py: 2,222 chars, '78B-2-307. Within four years. An action may be brought within four years:', 'Effective 5/3/2023'. Second citation 76-5-203 at /xcode/Title76/Chapter5/C76-5-S203_2026050620260506.html: 'Effective 5/6/2026', body (1) present. Shell 78B-2-S307.html: 4,957 chars of navigation only. Part file C78B-2-P3_1800010118000101.html links Section 307 with ?v=C78B-2-S307_2023050320230503.
- **Notes:** The code index lists Title 75E and Title 76 'Criminal Offenses'. Titles may have been reorganised recently, so always confirm the title from the index. legacy.utcourts.gov/statutes/?s={title}-{chapter} is only a redirect page that links to le.utah.gov.

### `ut-session-laws` — Laws of Utah — chapter lookup to enrolled bills (le.utah.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah State Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Session-law chapters mapped to bills; enrolled bill PDFs per session (~YYYY/bills/hbillenr/).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://le.utah.gov/UtahCode/ChapterLookup.jsp?chap={chapter}&sess={year}GS`
  - Placeholders: sess = year + session code (GS = General Session; special sessions use S1, S2 … — unverified). The lookup redirects to the bill page (2023 ch. 185 → /~2023/bills/static/HB0388.html), which links the enrolled PDF (/~{year}/bills/hbillenr/HB{nnnn}.pdf).
  - Index: `https://le.utah.gov/documents/laws-recent.htm`
  - Navigation: ChapterLookup → bill status page → enrolled PDF
- **Automation:** WebFetch untested · shell ok · robots: allowed (see ut-code-le)
  - Enrolled bills can be long (2023 HB 30: 214 pp, 472K chars).
- **Currency:** none stated
- **Official status:** Bill pages and enrolled-bill PDFs on le.utah.gov; no authentication statement seen.
- **Hazard:** redirect to bill page; the text is in the enrolled PDF
- **Hazard:** omnibus bills exceed the WebFetch window
- **Probe:** 2023 Utah Laws ch. 185 → `https://le.utah.gov/UtahCode/ChapterLookup.jsp?chap=185&sess=2023GS`
- **Evidence (2026-10-17):** fetch_doc.py: final URL https://le.utah.gov/~2023/bills/static/HB0388.html (9,166 chars). Enrolled PDF /~2023/bills/hbillenr/HB0030.pdf: 214 pp.
- **Notes:** Only one chapter was probed. HB0388 matches the 'Chapter 185, 2023 General Session' history note in § 78B-2-307, but the bill page's text was not inspected.

### `ut-code-justia` — Justia — Utah Code (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Utah Code editions incl. 2006, 2010, 2014, 2017, 2023, 2024, 2025; unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/utah/title-{title_lower}/chapter-{chapter_lower}/part-{part}/section-{section}/`
  - Placeholders: title and chapter in lower case (title-78b, chapter-2, chapter-6a). Part = the section's hundreds digit (307 → part-3, 203 → part-2). section = the last component only (78B-2-307 → section-307). Verified: 78B-2-307 → /title-78b/chapter-2/part-3/section-307/ and 76-5-203 → /title-76/chapter-5/part-2/section-203/. For chapters without parts, drop the part segment (unverified); if a URL fails, browse /codes/utah/title-{t}/chapter-{c}/. Year-specific: insert /{year}/ after /utah/. Title pages show NO section ranges.
  - Index: `https://law.justia.com/codes/utah/`
  - Navigation: title page → chapter page → part page → section
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt answers with a bot challenge
  - fetch_doc.py: 'law.justia.com refused automated access earlier (robots.txt challenge)'. Use WebFetch only. Constructed Justia URLs went through WebFetch without a permission prompt.
- **Currency:** page header and Universal Citation line — observed: "2025 Utah Code; 'UT Code § 78B-2-307 (2025)'"
- **Official status:** Pages state 'These codes may not be the most recent version.'
- **Hazard:** edition lags the official text (2025 edition; 2026 session changes missing)
- **Hazard:** part segment must be inferred
- **Hazard:** shell blocked by challenge
- **Probe:** Utah Code Ann. § 78B-2-307 → `https://law.justia.com/codes/utah/title-78b/chapter-2/part-3/section-307/` — expect: "An action may be brought within four years:"
- **Evidence (2026-10-17):** WebFetch: YES, 'An action may be brought within four years: (1) after'; 'UT Code § 78B-2-307 (2025)'; not truncated. Second citation 76-5-203 (/title-76/chapter-5/part-2/section-203/): YES, 'UT Code § 76-5-203 (2025)'.

## B. Constitution

### `ut-constitution-le` — Utah Constitution (le.utah.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah State Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of Utah, current versions per section with effective dates.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://le.utah.gov/xcode/Article{article}/Article_{article},_Section_{section}.html  (JS shell; text in UC_A{article}_S{section}_{version}.html)`
  - Placeholders: Article in Roman numerals. The shell has no text. The text file is /xcode/Article{article}/UC_A{article}_S{section}_{version}.html, and {version} comes from the article index file's links (?v=UC_AI_S11_2020051220210101). Unamended sections use 1800010118000101.
  - Index: `https://le.utah.gov/xcode/UC_1800010118000101.html`
  - Navigation: UC_1800010118000101.html → Article link '?v=UC_AI_1800010118000101' → fetch /xcode/ArticleI/UC_AI_1800010118000101.html → Section link '?v=UC_AI_S11_…' → fetch /xcode/ArticleI/UC_AI_S11_2020051220210101.html
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - WebFetch was not tried, because le.utah.gov URLs were gated in this session.
- **Currency:** per-section version file — observed: "Effective 1/1/2021"
- **Official status:** Same le.utah.gov disclaimer as ut-code-le.
- **Hazard:** JS shell; version id from index hop
- **Probe:** Utah Const. art. I, § 11 → `https://le.utah.gov/xcode/ArticleI/UC_AI_S11_2020051220210101.html` — expect: "All courts shall be open, and every person, for an injury"
- **Evidence (2026-10-17):** fetch_doc.py: 1,404 chars, '[Courts open -- Redress of injuries.]', 'Effective 1/1/2021', body present. Second citation art. VIII, § 3 (UC_AVIII_S3_1800010118000101.html): 'The Supreme Court shall have original jurisdiction to issue all extraordinary writs'.

### `ut-constitution-justia` — Justia — Utah Constitution

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Utah Constitution by article; per-section pages linked from article listing.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Article listing pages are named CO_{NN}.html, where NN = article number + 1 (Article I → CO_02.html). The listing shows only section headings that link to separate section pages; the section-page pattern was not observed.
  - Index: `https://law.justia.com/constitution/utah/`
  - Navigation: index (TOC only) → CO_{NN}.html article listing → section link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (challenge)
- **Currency:** index page — observed: "This Constitution may not be the most recent version."
- **Official status:** 'This Constitution may not be the most recent version.'
- **Hazard:** body text one hop below the article listing
- **Hazard:** may be stale
- **Probe:** Utah Const. art. I, § 11 → `https://law.justia.com/constitution/utah/CO_02.html`
- **Evidence (2026-10-17):** WebFetch: index has TOC only; CO_02.html lists Section 11 heading 'Courts open -- Redress of injuries.' with a link; body NOT PRESENT. Section page not fetched (budget).

## C. Court rules

### `ut-rules-utcourts` — Utah Court Rules (legacy.utcourts.gov/rules)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah State Courts (Utah Supreme Court / Judicial Council) · text: **fetch-and-quote** · official: unknown
- **Coverage:** URCP, URCrP, URAP, URJP, small claims (srpe), ADR, URE, URBCP (Business and Chancery Court), UCJA, and SCRP (Supreme Court Rules of Professional Practice: ch. 2 Code of Judicial Conduct, ch. 3 Rules of Professional Conduct, ch. 4 State Bar, ch. 5 LPP). One HTML page per rule.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://legacy.utcourts.gov/rules/view.php?type={type}&rule={rule}`
  - Placeholders: type: urcp | urcrp | urap | urjp | srpe | adr | ure | urbcp | ucja | scrp (see law_aliases). rule as cited for urcp/urcrp/urap/ure (12, 702, 24, 11) and UCJA (4-202.02). Rules of Professional Conduct: scrp rule 3-1.0N with a two-digit decimal (Rule 1.7 → 3-1.07, Rule 1.0 → 3-1.0). Former UCJA ch. 11–15 now live in SCRP ch. 1–5 (the page says 'previously UCJA Rule 13-1.7'). Code of Judicial Conduct = scrp ch. 2 (pattern unverified). www.utcourts.gov/rules/view.php redirects here. Index per set: /rules/{type}.php; whole set on one page: /rules/viewall.php?type={type}.
  - Index: `https://legacy.utcourts.gov/rules/`
- **Automation:** WebFetch gated · shell ok · robots: utcourts robots.txt (User-agent *): /rules/ allowed; disallows /resources/rules/comments/ and /resources/rules/approved/ (proposed/approved redlines)
  - WebFetch on view.php?type=urcp&rule=12 returned PROVENANCE_REQUIRED. fetch_doc.py: one 'Connection reset by peer' (ure 702), which succeeded on a later run. Plain curl gets HTTP 406 from www.utcourts.gov (WAF); fetch_doc.py is served.
- **Currency:** under the rule heading on each page — observed: "Effective: 5/1/2024 (URCP 12); 'Rule printed on October 17, 2026'"
- **Official status:** Each page says 'Go to https://www.utcourts.gov/rules for current rules.' No official/unofficial statement found.
- **Hazard:** Professional Conduct rule numbers need the 3-1.0N transform
- **Hazard:** UCJA ch. 11–15 renumbered into SCRP
- **Hazard:** intermittent connection resets
- **Hazard:** page shows only the current version; check the Effective date
- **Probe:** Utah R. Civ. P. 12(b) → `https://legacy.utcourts.gov/rules/view.php?type=urcp&rule=12` — expect: "Every defense, in law or fact, to claim for relief in any pleading"
- **Evidence (2026-10-17):** fetch_doc.py: 8,347 chars, 'Rule 12. Defenses and objections.', 'Effective: 5/1/2024', full (a)–(k). Also verified: ure 702 ('Rule 702. Testimony by Experts.', Effective 11/1/2007); urcrp 11 ('Rule 11. Pleas.'); urap 24 ('Principal briefs must contain under appropriate headings'); scrp 3-1.07 ('a lawyer shall not represent a client if the representation involves a concurrent conflict'); ucja 4-202.02 ('Records Classification', Effective 5/18/2026); urbcp 1.
- **Notes:** No tier-2 host was found for Utah court rules: Justia, LII and public.law do not carry them (not exhaustively checked).

## D. Administrative code

### `ut-admincode-oar` — Utah Administrative Code (adminrules.utah.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Utah Office of Administrative Rules (Dept. of Government Operations) · text: **link-only** · official: unknown
- **Coverage:** Current Utah Administrative Code (R-numbered rules).
- **Access:** `search-only` · format html
  - Placeholders: Next.js app. /Code and the home page return only navigation ('Current Rules', 'Agencies'). The old pattern /public/rule/R414-1/Current%20Rules returns HTTP 404. No per-rule URL was found.
  - Index: `https://adminrules.utah.gov/Code`
  - Navigation: interactive search only (JS)
- **Automation:** WebFetch gated · shell ok · robots: none (robots.txt returns the app's 404 page)
  - fetch_doc.py downloads the page but gets an 873-char shell with no rule text. WebFetch on /Code returned PROVENANCE_REQUIRED.
- **Currency:** none observed
- **Official status:** The Bulletin page refers to 'Researching Administrative Rules - Authentication' (MD5 hashes for files). The online code's official status was not confirmed.
- **Hazard:** JS-only app; no rule text for scripts
- **Hazard:** no known per-rule URL
- **Probe:** Utah Admin. Code R414-1-1 → `https://adminrules.utah.gov/Code`
- **Evidence (2026-10-17):** fetch_doc.py: 873 chars, 'Office of Administrative Rules … Current Rules … Agencies', no rule text; /public/rule/R414-1/Current%20Rules → HTTP 404.
- **Notes:** Use ut-admincode-lii for text, and the Utah State Bulletin for amendment history.

### `ut-admincode-lii` — Cornell LII — Utah Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Utah Administrative Code by topic → title (R-number) → rule → section, with Bulletin history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-{rule}-{section}`
  - Placeholders: Section page = the full citation with 'Utah-Admin-Code-' prefixed (R414-1-1 → Utah-Admin-Code-R414-1-1; R307-101-2 → Utah-Admin-Code-R307-101-2). Rule listings: /regulations/utah/{topic}/title-{R###}/rule-{R###-N} (the topic slug is not derivable: health, environmental-quality …). Listings show section ranges (e.g. 'R414-1-1 to R414-1-32').
  - Index: `https://www.law.cornell.edu/regulations/utah`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10; /regulations allowed
- **Currency:** page footer and Notes — observed: "Amended by Utah State Bulletin Number 2025-05, effective 2/18/2025"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag (last-modified Aug 2025 on probed page)
- **Hazard:** compare the latest Bulletin cite before quoting
- **Probe:** Utah Admin. Code R414-1-1 → `https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R414-1-1` — expect: "Title XIX of the Social Security Act and"
- **Evidence (2026-10-17):** fetch_doc.py: 2,715 chars, 'Utah Admin. Code R414-1-1 - Authority and Purpose', '(1)(a) Title XIX of the Social Security Act', note 'Bulletin Number 2025-05'. Second citation R307-101-2: 'Except where specified in individual rules, definitions in'.

## D. Administrative register

### `ut-bulletin` — Utah State Bulletin

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah Office of Administrative Rules · text: **fetch-and-quote** · official: official
- **Coverage:** Semi-monthly issues (1st and 15th) since 1996. Recent issues are full PDFs; older issues also have per-filing HTML (publicat/bulletin/YYYY/YYYYMMDD/{DAR file no}.htm).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://rules.utah.gov/wp-content/uploads/b{YYYYMMDD}.pdf`
  - Placeholders: Issue date YYYYMMDD (01 or 15 of the month). Issue number N of year Y is listed with its date on the index page ('Vol. 2026, No. 19 (10/01/2026)'); map number → date there. Older per-filing HTML: https://rules.utah.gov/publicat/bulletin/{YYYY}/{YYYYMMDD}/{file_no}.htm.
  - Index: `https://rules.utah.gov/publications/utah-state-bulletin/`
  - Navigation: index page lists every issue with its PDF link
- **Automation:** WebFetch untested · shell ok · robots: User-agent * Disallow /wp-admin/; Crawl-delay: 10
  - Issue PDFs are large (b20261001.pdf: 311 pp, 1.3M chars) and far exceed the WebFetch window: use fetch_doc.py grep/section.
- **Currency:** index page list — observed: "Vol. 2026, No. 20 (10/15/2026)"
- **Official status:** The PDF front matter says it 'is an official noticing publication of the executive branch' of Utah government.
- **Hazard:** very large PDFs
- **Hazard:** issue number ↔ date mapping needs the index
- **Probe:** Utah State Bulletin No. 2026-19 → `https://rules.utah.gov/wp-content/uploads/b20261001.pdf` — expect: "is an official noticing publication of the executive branch"
- **Evidence (2026-10-17):** fetch_doc.py: application/pdf 311 pp, 1,304,012 chars; front matter text present. Per-filing HTML /publicat/bulletin/2017/20170301/41321.htm: 'DAR File No. 41321'.

## E. Case law

### `ut-opinions-utcourts` — Utah Appellate Court Opinions (utcourts.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Utah State Courts · text: **link-only** · official: unknown
- **Coverage:** Supreme Court and Court of Appeals year selectors 1997–2026; Court of Appeals unpublished decisions 1997–2010; juvenile decisions 2005–2026; Business and Chancery Court orders 2025–2026.
- **Access:** `link-only` · format pdf
  - Pattern: `https://legacy.utcourts.gov/opinions/view.html?court={supopin|appopin}&opinion={Case Name}{YYYYMMDD}_{docket}_{UT number}.pdf`
  - Placeholders: File name from the RSS feed: 'State v. Conde20261008_20241010_149.pdf' = case name + decision date + docket + public-domain number. Directories /opinions/supopin/, /appopin/, /mds/, /juv/ and every /opinions/*.pdf are robots-disallowed.
  - Index: `https://legacy.utcourts.gov/opinions/`
  - Navigation: Link only. Locate the opinion via the RSS feed (allowed) or Justia; read it on ut-cases-justia.
  - Read via: ut-cases-justia (WebFetch)
- **Automation:** WebFetch gated · shell blocked-robots · robots: legacy.utcourts.gov and www.utcourts.gov: User-agent * Disallow /opinions/*.pdf$, /opinions/supopin/, /opinions/appopin/, /opinions/mds/, /opinions/juv/, */search/*
  - fetch_doc.py REFUSED /opinions/supopin/ (rule Disallow: /opinions/supopin/) and view.html?…pdf (rule Disallow: /opinions/*.pdf$). WebFetch on the RSS-listed URL returned PROVENANCE_REQUIRED. The RSS feed https://legacy.utcourts.gov/rss/opinions/index.xml is allowed and lists recent opinions with file names (fetch_doc.py OK, 1,582 chars).
- **Currency:** RSS last-modified — observed: "Sat, 10 Oct 2026 04:01:01 GMT"
- **Official status:** Slip opinions published by the courts; P.3d pagination not included.
- **Hazard:** robots disallows all opinion PDFs: never fetch them, link only
- **Hazard:** slip pagination; ¶ numbers are the pinpoints
- **Probe:** State v. Conde, 2026 UT App 149 → `https://legacy.utcourts.gov/opinions/view.html?court=appopin&opinion=State%20v.%20Conde20261008_20241010_149.pdf`
- **Evidence (2026-10-17):** fetch_doc.py exit 3: REFUSED robots.txt disallows … (rule: Disallow: /opinions/*.pdf$).
- **Notes:** Appellate docket search: https://apps.utcourts.gov/CourtsPublicWEB/index.jsp (linked from the opinions page; not probed).

### `ut-cases-justia` — Justia — Utah case law

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Utah Supreme Court and Court of Appeals (published) by year; ranges not checked. Pages show the public-domain citation and ¶ numbers.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/utah/{court-slug}/{year}/{docket}.html`
  - Placeholders: court-slug: supreme-court | court-of-appeals-published (an unpublished/memorandum slug was not checked). year = decision year. docket: Supreme Court = 8 digits (20230556.html); Court of Appeals = 8 digits + '-ca' (20230824-ca.html). Year listing /cases/utah/{court-slug}/{year}/ gives name, date, docket, link. Map a public-domain cite to a docket through the year listing or the opinion header.
  - Index: `https://law.justia.com/cases/utah/`
  - Navigation: year listing → case page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (challenge)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** no P.3d page numbers for the case itself
- **Hazard:** public-domain cite → docket needs listing hop
- **Hazard:** memorandum decisions' slug unverified
- **Hazard:** shell blocked
- **Probe:** State v. Jennings, 2025 UT 59 → `https://law.justia.com/cases/utah/supreme-court/2025/20230556.html` — expect: "Deon Andre Jennings is charged with the murder of Willie"
- **Evidence (2026-10-17):** WebFetch: YES, '2025 UT 59', ¶1–¶78, not truncated. Second: State v. Leatham, 2025 UT App 194 (/court-of-appeals-published/2025/20230824-ca.html): YES, 'A driver was stopped by officers and found to lack', ¶1–¶22.

## F. Subsequent history

### `ut-cert-petitions` — Utah Supreme Court — Petitions for Writ of Certiorari (bimonthly dispositions)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Utah Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Certiorari grants and denials on Court of Appeals decisions, bimonthly reporting periods (seen: 2024, 2025). Columns: case title, COA case no., Sup. Ct. no., date, COA citation (P.3d or 'Unpublished').
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.utcourts.gov/content/dam/courts/sup/certs/petitions/{YYYY}cert_{MM}-{MM2}.pdf`
  - Placeholders: Two-month periods 01-02, 03-04, 05-06, 07-08, 09-10, 11-12 (the year and months of the cert decision, not of the COA decision). Search the following several periods for the COA docket number (8 digits). The hosts utcourts.gov and www.utcourts.gov both serve it.
  - Navigation: Earlier index link https://www.utcourts.gov/en/about/courts/sup/certs.html now returns HTTP 404; PDFs found by search and confirmed by pattern.
- **Automation:** WebFetch untested · shell ok · robots: /content/dam/ not disallowed
  - Small one- or two-page PDFs.
- **Currency:** PDF header — observed: "Reporting period: 9/01/2025 - 10/31/2025"
- **Official status:** Court-published PDF lists.
- **Hazard:** index page 404; listing by constructed period
- **Hazard:** docket search by grep within each period PDF only
- **Hazard:** no party-independent search across periods
- **Probe:** State v. Lucke, COA No. 20230428 → cert granted 09/19/2025 → `https://www.utcourts.gov/content/dam/courts/sup/certs/petitions/2025cert_09-10.pdf` — expect: "State v. Lucke 20230428 20250519 09/19/2025 569 P.3d 238"
- **Evidence (2026-10-17):** fetch_doc.py: 1 pp PDF, 'Petitions for Writ of Certiorari', 'Reporting period: 9/01/2025 - 10/31/2025', GRANTED/DENIED tables with COA case nos. Second: 2024cert_07-08.pdf, 'Reporting period: 07/01/2024 - 08/31/2024'.
- **Notes:** Granted cases then show up as Supreme Court opinions (ut-cases-justia), with the Sup. Ct. number as the docket. The columns are spaced, so grep for the docket number, not for the whole row.

## Not available (do not look for these again)

- **statutes** — public.law edition of Utah law: public.law lists only CA, CO, FL, NV, NY, OR, TX (per prior records; not re-probed today). (2026-10-17)
- **statutes** — Code-wide 'current through' statement on le.utah.gov: grep of code index and code.html for current/through/session/official: 0 matches; only per-section 'Effective' dates. (2026-10-17)
- **case_law** — Free P.3d pagination for Utah opinions: Justia shows the public-domain citation and ¶ numbers only (no P.3d cite for the case itself); official PDFs are robots-blocked. (2026-10-17)
- **case_law** — Script-readable official opinion text: utcourts robots.txt disallows /opinions/*.pdf$ and the supopin/appopin/mds/juv directories. (2026-10-17)

## Corpus candidates (maintainers)

- `ut-code-le` — Whole-title PDF (Title 78B: 456 pp, 1.5M chars) far beyond the WebFetch window. Per-title PDFs exist for every title (C{title}_{version}.pdf). · bulk: per-title PDF/RTF/XML via 'Download Options' on each title's version file
- `ut-bulletin` — Semi-monthly issue PDFs of about 300 pp (1.3M chars).

## Open questions

- WebFetch on le.utah.gov, legacy.utcourts.gov and adminrules.utah.gov was gated (PROVENANCE_REQUIRED). Whether WebFetch reads the versioned files and rule pages is untested.
- adminrules.utah.gov: no per-rule URL or public API was found for the official Admin Code text.
- Justia slug for Court of Appeals memorandum/unpublished decisions not checked.
- Justia Constitution section-page URL pattern not observed.
- Index page for cert petition PDFs: the old certs.html link returns 404.
- Whether apps.utcourts.gov/CourtsPublicWEB docket search is robots-allowed and works by GET.
- CourtListener ids (utah, utahctapp) unverified; trailing-U unpublished cite form from memory.

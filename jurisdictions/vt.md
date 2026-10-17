# Vermont (VT) — free legal sources

_Generated from `data/vt.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: legislature.vermont.gov per-section pages (unofficial, 2026 session) need a title-index hop for the chapter, which the index shows as section ranges; Justia 2025 is a WebFetch-only fallback; act PDFs are constructible. Constitution: one legislature page (heading stale but text current). Court rules: full text only in the LexisNexis free-access JavaScript app, which neither tool can read; the judiciary posts promulgation orders for recent amendments. Admin code: official CVR is the same Lexis app; Cornell LII mirrors it; SOS posts proposed-rule notices. Case law: vtcourts.gov library (Supreme Court from ~2006, trial divisions) is searchable by plain GET; public-domain cites 'YYYY VT N, ¶ P'; Justia covers 1950 on.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Vermont Supreme Court | `vt (unverified)` | Vt. | Vt., A.3d, A.2d, A. | YYYY VT N, ¶ P (e.g. 2026 VT 44, ¶ 5); adopted 2003 |
| Vermont Superior Court (Civil, Criminal, Family, Probate, Environmental Divisions) | `vtsuperct (unverified)` | Vt. Super. Ct. | — | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Vermont Statutes Annotated | `12 V.S.A. § 512`; `9 V.S.A. § 2453(a)`; `13 V.S.A. § 2301`; `9A V.S.A. § 2-101`; `11A V.S.A. § 8.30`; `Vt. Stat. Ann. tit. 12, § 512`; `Vt. Stat. Ann. tit. 9, § 2453`; `section 2453 of Title 9 of the Vermont Statutes Annotated`; `Title 12, section 512 of the Vermont Statutes Annotated`; `23 V.S.A. § 1201`; `23 V.S.A. §§ 1201-1205`; `section 6086 of Title 10 of the Vermont Statutes Annotated` | `vt-statutes-leg` → `vt-statutes-justia` |
| Vermont Statutes Annotated appendices (3, 10, 16, 24 App.) | `24 App. V.S.A. ch. 3, § 1`; `3 V.S.A. App. § 1`; `24 V.S.A. App. § 3-1` | `vt-statutes-leg` |
| Vermont Acts and Resolves (session laws), distinctive forms | `2023, No. 181 (Adj. Sess.), § 2`; `1971, No. 185 (Adj. Sess.)`; `2023 Vt. Acts & Resolves No. 181`; `1975, No. 248 (Adj. Sess.), § 2` | `vt-session-laws` |
| Vermont Acts (bare 'YYYY, No. N' / 'Act N of YYYY') *(only once this jurisdiction is known)* | `2025, No. 1`; `Act 153 of 2026`; `1959, No. 261, § 3` | `vt-session-laws` |
| Vermont Constitution | `Vt. Const. ch. I, art. 11`; `Vt. Const. ch. II, § 28`; `Vt. Const. ch. I, art. 22`; `Chapter I, Article 11 of the Vermont Constitution`; `Article 11 of Chapter I of the Vermont Constitution`; `Chapter II, § 37 of the Vermont Constitution` | `vt-constitution-leg` → `vt-constitution-justia` |
| Vermont Rules of Court (V.R.C.P., V.R.Cr.P., V.R.A.P., V.R.E., V.R.F.P., V.R.P.P., V.R.E.C.P., V.R.Pr.C.) | `V.R.C.P. 12(b)(6)`; `V.R.Cr.P. 35(b)`; `V.R.A.P. 40`; `V.R.A.P. 33.1(d)`; `V.R.E. 803(6)`; `V.R.F.P. 4.3(b)`; `V.R.P.P. 80.3(g)`; `V.R.E.C.P. 5`; `V.R.Pr.C. 1.7`; `Rule 55(a) of the Vermont Rules of Civil Procedure`; `Vermont Rule of Criminal Procedure 35(b)`; `Vt. R. Civ. P. 56` | `vt-rules-promulgated` → `vt-rules-lexis` |
| Code of Vermont Rules (CVR) | `Code Vt. R. 13-140-001`; `CVR 04-000-001`; `13-140-001 Vt. Code R. § 1.2`; `13-001 Code Vt. R. 13-140-001-X`; `Vt. Admin. Code 13-140-001` | `vt-admincode-lexis` → `vt-admincode-lii` |
| Secretary of State rule-filing numbers (proposed / emergency) *(only once this jurisdiction is known)* | `26P032`; `26-E03`; `Rule Log # 92-4` | `vt-register-sos` |
| Vermont public-domain citation | `2026 VT 44`; `2014 VT 101, ¶ 6`; `In re All Metals Recycling Inc., 2014 VT 101, ¶ 6, 197 Vt. 481, 107 A.3d 895`; `Solsaa v. Solsaa, 2008 VT 138`; `2016 VT 102` | `vt-opinions-courts` → `vt-cases-justia` |
| Vermont Reports (official reporter) and Atlantic Reporter with (Vt.) | `197 Vt. 481`; `107 A.3d 895 (Vt. 2014)`; `2014 VT 101, ¶ 6, 197 Vt. 481, 107 A.3d 895` | `vt-cases-justia` → `vt-opinions-courts` |
| Vermont Supreme Court docket numbers *(only once this jurisdiction is known)* | `No. 25-AP-345`; `25-AP-364`; `No. 2015-376`; `No. 2008-164` | `vt-opinions-courts` → `vt-cases-justia` |
| Vermont Superior Court docket numbers and decisions *(only once this jurisdiction is known)* | `Case No. 26-CV-04158`; `22-CR-12116`; `25-CV-01449`; `No. 24-ENV-00012` | `vt-opinions-courts` |
| Westlaw / Lexis cites with Vermont parenthetical | `2026 WL 123456 (Vt. Oct. 9, 2026)`; `2019 Vt. LEXIS 55`; `2024 Vt. Super. LEXIS 12` | `vt-opinions-courts` → `vt-cases-justia` |

Regexes (case-insensitive):

- Vermont Statutes Annotated: `(?<!\d)9A\s+V\.\s?S\.\s?A\.(?:\s+Ann\.)?\s*§+\s*(?P<ucc_section>\d+[A-Z]?-\d+[a-z]?)|(?P<title>\d{1,2}[A-C]?)\s+V\.\s?S\.\s?A\.(?:\s+Ann\.)?\s*(?:§§\s*(?P<range_start>\d+[a-z]?(?:\.\d+[a-z]?)?)\s*(?:-|–|to|through)\s*(?P<range_end>\d+[a-z]?(?:\.\d+[a-z]?)?)|§+\s*(?P<section>\d+[a-z]?(?:\.\d+[a-z]?)?))(?!\d)|Vt\.\s*Stat\.\s*Ann\.\s*tit\.\s*(?P<title2>\d{1,2}[A-C]?),?\s*(?:§§\s*(?P<range_start2>\d+[a-z]?(?:\.\d+[a-z]?)?)\s*(?:-|–|to|through)\s*(?P<range_end2>\d+[a-z]?(?:\.\d+[a-z]?)?)|§+\s*(?P<section2>\d+[a-z]?(?:[-.]\d+[a-z]?)?))(?!\d)|(?:[Ss]ec(?:tion|\.)|§)\s*(?P<section3>\d+[a-z]?(?:[-.]\d+[a-z]?)?)(?:\([a-z0-9]+\))*\s+of\s+Title\s+(?P<title3>\d{1,2}[A-C]?)\s+of\s+the\s+Vermont\s+Statutes\s+Annotated|Title\s+(?P<title4>\d{1,2}[A-C]?),\s+(?:[Ss]ection|§)\s*(?P<section4>\d+[a-z]?(?:[-.]\d+[a-z]?)?)\s+of\s+the\s+Vermont\s+Statutes\s+Annotated`
- Vermont Statutes Annotated appendices (3, 10, 16, 24 App.): `(?P<title>3|10|16|24)\s+(?:App\.\s*V\.\s?S\.\s?A\.|V\.\s?S\.\s?A\.\s*App\.)\s*(?:ch\.\s*(?P<chapter>\d+[A-Z]?),?\s*)?§+\s*(?:(?P<chapter2>\d+[A-Z]?)-)?(?P<section>\d+[a-z]?)(?!\d)`
- Vermont Acts and Resolves (session laws), distinctive forms: `(?P<year>(?:18|19|20)\d\d),\s*No\.\s*(?P<number>\d{1,3})\s*\((?:Adj|Sp)\.\s*Sess\.\)|(?P<year2>(?:18|19|20)\d\d)\s+Vt\.\s*Acts\s*(?:&|and)\s*Resolves\s+No\.\s*(?P<number2>\d{1,3})`
- Vermont Acts (bare 'YYYY, No. N' / 'Act N of YYYY'): `(?P<year>(?:18|19|20)\d\d),\s*No\.\s*(?P<number>\d{1,3})(?!\d|,\s*(?:19|20)\d\d)|Act\s+(?:No\.\s*)?(?P<number2>\d{1,3})\s+of\s+(?P<year2>(?:19|20)\d\d)`
- Vermont Constitution: `Vt\.\s*Const\.\s*ch\.\s*(?P<chapter>I{1,2}),?\s*(?:art\.\s*(?P<article>\d+)|§\s*(?P<section>\d+))|Chapter\s+(?P<chapter2>I{1,2}),?\s+(?:Article\s+(?P<article2>\d+)|(?:Section|§)\s*(?P<section2>\d+))\s+of\s+the\s+Vermont\s+Constitution|Article\s+(?P<article3>\d+)(?:th|st|nd|rd)?\s+of\s+Chapter\s+(?P<chapter3>I{1,2})\s+of\s+the\s+Vermont\s+Constitution`
- Vermont Rules of Court (V.R.C.P., V.R.Cr.P., V.R.A.P., V.R.E., V.R.F.P., V.R.P.P., V.R.E.C.P., V.R.Pr.C.): `V\.\s?R\.\s?(?P<set>C\.\s?P|Cr\.\s?P|A\.\s?P|E|F\.\s?P|P\.\s?P|E\.\s?C\.\s?P|Pr\.\s?C|E\.\s?F)\.\s*(?P<rule>\d+(?:\.\d+)?[A-Za-z]?)|Vt\.\s*R\.\s*(?P<set2>Civ\.\s*P|Crim\.\s*P|App\.\s*P|Evid)\.\s*(?P<rule2>\d+(?:\.\d+)?)|Rule\s+(?P<rule3>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Vermont\s+Rules\s+of\s+(?P<set3>Civil|Criminal|Appellate|Family|Probate|Environmental\s+Court)\s+Procedure|Rule\s+(?P<rule5>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Vermont\s+Rules\s+of\s+Evidence|Vermont\s+Rules?\s+of\s+(?P<set4>Civil|Criminal|Appellate|Family|Probate)\s+Procedure\s+(?P<rule4>\d+(?:\.\d+)?)`
- Code of Vermont Rules (CVR): `(?:\d{2}-\d{3}\s+)?Code\s+Vt\.\s*R\.\s*(?P<agency>\d{2})[- ](?P<sub>\d{3})[- ](?P<chapter>\d{3})|CVR\s+(?P<agency2>\d{2})[- ](?P<sub2>\d{3})[- ](?P<chapter2>\d{3})|(?P<agency3>\d{2})-(?P<sub3>\d{3})-(?P<chapter3>\d{3})\s+Vt\.\s*Code\s*R\.|Vt\.\s*Admin\.\s*Code\s+(?P<agency4>\d{2})-(?P<sub4>\d{3})-(?P<chapter4>\d{3})`
- Secretary of State rule-filing numbers (proposed / emergency): `(?<![\w-])(?P<year>\d{2})(?P<kind>P|-E)(?P<number>\d{2,3})(?![\w-])|Rule\s+Log\s*#\s*(?P<log>\d{2}-\d{1,3})`
- Vermont public-domain citation: `(?P<year>(?:19|20)\d\d)\s+VT\s+(?P<number>\d{1,3})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- Vermont Reports (official reporter) and Atlantic Reporter with (Vt.): `(?P<volume>\d{1,3})\s+Vt\.\s+(?P<page>\d{1,4})(?!\d)|(?P<volume2>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page2>\d{1,5})(?:,\s*\d+)?\s*\(Vt\.(?:\s*Super\.\s*Ct\.)?(?:\s+[A-Z][a-z]{2,3}\.(?:\s+\d{1,2},)?)?\s*(?P<year>\d{4})\)`
- Vermont Supreme Court docket numbers: `(?:No\.\s*)?(?P<yy>\d{2})-AP-(?P<seq>\d{3})|No\.\s*(?P<year>(?:19|20)\d\d)-(?P<seq2>\d{1,4})(?!\d)`
- Vermont Superior Court docket numbers and decisions: `(?P<yy>\d{2})-(?P<div>CV|CR|FA|PR|ENV|JV|DM|FS|SC)-(?P<seq>\d{3,5})`
- Westlaw / Lexis cites with Vermont parenthetical: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Vt\.|Vt\.\s*(?:Super\.\s*)?LEXIS\s+(?P<lexis>\d+))`

Statutes: Vermont style is '12 V.S.A. § 512'; Bluebook 'Vt. Stat. Ann. tit. 12, § 512'. Titles carry letter suffixes (9A UCC, 11A business corporations, 11B, 11C). In-code cross-references read 'section 512 of this title' and carry no state marker: route them only with Vermont context. Bare 'section N of Title T' is not claimed here (it would collide with Delaware's 'Section 141(k) of Title 8'); the prose forms routed here name 'the Vermont Statutes Annotated'. A '§§ 1201-1205' range is a span, not a hyphenated section: the statute regex captures it as range_start/range_end (fetch range_start, then each section through range_end); hyphenated sections exist only in Title 9A (UCC article-section, e.g. 2-101) and dotted ones in 11A/11B/11C (8.30). Session laws are cited 'YYYY, No. N (Adj. Sess.), § S' (the year is the session year; even-year adjourned sessions are '(Adj. Sess.)'). Bare 'YYYY, No. N' and 'Act N of YYYY' are generic and need Vermont context. Constitution: two chapters; Chapter I is cited by article ('ch. I, art. 11'), Chapter II by section ('ch. II, § 28'). Historic ordinal forms ('Article 11th') appear in older opinions. Court rules: V.R.C.P., V.R.Cr.P., V.R.A.P., V.R.E., V.R.F.P., V.R.P.P., V.R.E.C.P., V.R.Pr.C. (professional conduct); bare 'Rule 12(b)(6)' must not route here without context. Case law: public-domain citation 'YYYY VT N, ¶ P' since 2003 (paragraph-numbered pinpoints, vendor-neutral); parallel cites to Vt. (official Vermont Reports) and A.2d/A.3d. Unpublished three-justice entry orders (V.R.A.P. 33.1) carry only the docket ('No. 25-AP-364') and are not precedent. Supreme Court dockets: 'YY-AP-NNN' from about 2021; earlier 'YYYY-NNN'. The opinion PDF names derive from the docket (op25-345.pdf; eo25-364.pdf; eo2008-164.pdf; suffixes like '_3' or '.bail_' occur), so go through the library search. Superior Court dockets 'YY-CV-NNNNN' etc. are generic. CourtListener ids 'vt' and 'vtsuperct' are from memory and unverified. Appendices: the site cites them '24 App. V.S.A. ch. 3, § 1'; practitioners also write '3 V.S.A. App. § 1' or '24 V.S.A. App. § 3-1' (chapter-section); the appendix pattern routes all three.

## A. Statutes / code

### `vt-session-laws` — Acts and Resolves (as-enacted act PDFs)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont General Assembly · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts of each biennium as enacted, with act summaries; probed 2024 (Act 181) and 2026 (Act 153).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://legislature.vermont.gov/Documents/{biennium}/Docs/ACTS/ACT{number:03d}/ACT{number:03d}%20As%20Enacted.pdf`
  - Placeholders: biennium = the even (second) year of the two-year session: '2023, No. 181 (Adj. Sess.)' → 2024; '2025, No. 1' → 2026 (odd year + 1). number zero-padded to 3 digits. Acts are numbered across the biennium. Listing JSON: https://legislature.vermont.gov/bill/loadBillActs/{biennium}/regular (fields ActNo, BillNumber, Title, ActLink) — the /bill/acts/{biennium} page loads it by script.
  - Index: `https://legislature.vermont.gov/bill/loadBillActs/{biennium}/regular`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay 30; /Documents/ and /bill/loadBillActs/ not disallowed
  - Not WebFetch-probed (budget). Large acts (Act 181 of 2024: 171 pp., 270K chars) exceed the WebFetch window; use fetch_doc.py.
- **Currency:** none stated
- **Official status:** Act PDFs carry the act number and page header ('No. 153 Page 1 of 33 2026'); no authentication statement seen.
- **Hazard:** biennium folder differs from the cite year for first-year acts
- **Hazard:** long PDFs
- **Hazard:** pre-2000s acts not probed
- **Probe:** 2025, No. 153 (Adj. Sess.) → `https://legislature.vermont.gov/Documents/2026/Docs/ACTS/ACT153/ACT153%20As%20Enacted.pdf` — expect: "An act relating to miscellaneous amendments to laws relating to"
- **Evidence (2026-10-17):** fetch_doc: PDF 33 pp., 49,898 chars, 'No. 153. An act relating to miscellaneous amendments to laws relating to motor vehicles. (S.326)'. Second: /Documents/2024/Docs/ACTS/ACT181/… 171 pp., 'An act relating to community resilience and biodiversity'. loadBillActs/2026/regular → JSON with ActLink. | Independent check 2026-10-17: fetch_doc grep: 'No. 153. An act relating to miscellaneous amendments to laws relating to motor vehicles' (33 pp.); second citation 2019, No. 131 (Adj. Sess.) ok
- **Notes:** Older Acts and Resolves volumes were not looked for.

### `vt-statutes-leg` — The Vermont Statutes Online

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont General Assembly / Office of Legislative Counsel · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles of the V.S.A. including appendices (3, 10, 16, 24 Appendix); per-section HTML pages and whole-chapter pages; current through the latest session.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://legislature.vermont.gov/statutes/section/{title:02d}{title_suffix}/{chapter:03d}{chapter_suffix}/{section:05d}{section_suffix}`
  - Placeholders: title = 2-digit zero-padded plus any letter suffix (01, 09, 12, 09A, 11A). chapter = 3-digit zero-padded plus any suffix (023, 063, 002A). section = numeric part zero-padded to 5 digits, lower-case letter suffix kept (00512, 02453, 02451a). Title 9A (UCC) '§ 2-101' → chapter = article (002), section = part after the hyphen (00101). Titles 11A/11B/11C decimal sections '§ 8.30' → chapter 008, section '00008.30'. The CHAPTER is not encoded in the citation: take it from the title index, whose chapter rows show section ranges ('Chapter 023 : Limitation of Time for Commencement of Actions Contains: §§ 461 - 595'). A wrong chapter returns HTTP 200 with an empty shell '(Cite as: V.S.A. )' — treat that as not found. Whole chapter: https://legislature.vermont.gov/statutes/fullchapter/{title}/{chapter}. Appendices: title key '{title:02d}APPENDIX' (03APPENDIX, 10APPENDIX, 16APPENDIX, 24APPENDIX); URL https://legislature.vermont.gov/statutes/section/{title:02d}APPENDIX/{chapter:03d}/{section:05d} — chapter comes from the citation ('ch. 3' or the part before the hyphen in 'App. § 3-1'), e.g. 24 App. V.S.A. ch. 3, § 1 → /section/24APPENDIX/003/00001 ('(Cite as: 24 App. V.S.A. ch. 3, § 1)'). Appendix title index: /statutes/title/24APPENDIX. Ranges '§§ a-b': fetch each section; they may straddle chapters.
  - Index: `https://legislature.vermont.gov/statutes/title/{title:02d}`
  - Navigation: title index (/statutes/title/12) → the chapter whose 'Contains: §§ a - b' range covers the section → chapter page (/statutes/chapter/12/023) lists per-section links → section page. Verified: 12 V.S.A. § 512 → /section/12/023/00512; 9 V.S.A. § 2453 → /section/09/063/02453; 13 V.S.A. § 2301 → /section/13/053/02301; 9A V.S.A. § 2-101 → /section/09A/002/00101; 11A V.S.A. § 8.30 → /section/11A/008/00008.30.
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * Crawl-delay: 30; Disallow only /bill/loadBillDetailedStatus/, /bill/loadBillRollCalls/, /bill/loadBillRollCallDetails/, /bill/loadBillsIntroduced/
  - Crawl-delay 30 s: fetch_doc.py waits ~30 s between requests to this host. WebFetch reads section pages from search results (12/027/01131: complete, repeal note); a built URL (09/063/02453) was gated on the permission prompt. Pages are small (6-8K chars); the section text sits after ~4.7K chars of navigation.
- **Currency:** banner above the breadcrumb on every statute page — observed: "The Statutes below now include the actions of the 2026 session"
- **Official status:** Every statute page: 'NOTE: The Vermont Statutes Online is an unofficial copy of the Vermont Statutes Annotated that is provided as a convenience.' (https://legislature.vermont.gov/statutes/section/12/023/00512). The official V.S.A. is the LexisNexis print edition.
- **Hazard:** chapter not derivable from the section number (title-index hop)
- **Hazard:** wrong chapter returns HTTP 200 empty shell, not 404
- **Hazard:** unofficial copy per the publisher
- **Hazard:** 30-second crawl-delay
- **Hazard:** repealed sections show only a repeal note (12 V.S.A. §§ 1131-1133)
- **Hazard:** '§§ a-b' citations are spans across several section pages (possibly several chapters), not one hyphenated section
- **Hazard:** appendix sections restart numbering per chapter (24 App. ch. 3, § 1), so the chapter must come from the citation
- **Probe:** 12 V.S.A. § 512 → `https://legislature.vermont.gov/statutes/section/12/023/00512` — expect: "Actions for the following causes shall be commenced within three years"
- **Evidence (2026-10-17):** fetch_doc verify: VERIFIED at offset 5117 (7,100-char page). Also 9 V.S.A. § 2453 ('(a) Unfair methods of competition in commerce and unfair'), 13 V.S.A. § 2301 ('Murder committed by means of poison'), 9A § 2-101, 11A § 8.30 bodies present. Wrong chapter /09/062/02453 → 200 empty shell. WebFetch on /12/027/01131: page complete, unofficial-copy note and 2026-session banner. | Independent check 2026-10-17: WebFetch YES 'Actions for the following causes shall be commenced within three'; banner '...include the actions of the 2026 session'; second citation 23 V.S.A. § 1201 ok
- **Notes:** Fullchapter pages (/statutes/fullchapter/12/023, 33,857 chars) hold every section of a chapter. 'Acts Affecting VSA Sections' (/bill/acts-affecting-statutes/2026) lists recent amendments.

### `vt-statutes-justia` — Justia — Vermont Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Vermont Statutes editions; unversioned URL serves the 2025 edition.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/vermont/title-{title}/chapter-{chapter}/section-{section}/`
  - Placeholders: title and chapter unpadded (title-9, chapter-63, title-12, chapter-23); section verbatim (section-512, section-2453). No subchapter level in the URL. Chapter still comes from an index: Justia's title page shows 'Contains: §§ 461 - 595' per chapter. Year-specific: insert /{year}/ after /vermont/.
  - Index: `https://law.justia.com/codes/vermont/title-{title}/`
  - Navigation: title page (section ranges) → chapter page → section page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a bot check
  - fetch_doc.py: 'law.justia.com answers robots.txt with a bot check (challenge); automated access refused.' WebFetch only.
- **Currency:** page heading and Universal Citation line — observed: "2025 Vermont Statutes; '12 VT Stats § 512'"
- **Official status:** Page says the codes 'may not be the most recent version'.
- **Hazard:** edition lags the official site by up to a year
- **Hazard:** shell blocked by bot check
- **Probe:** 12 V.S.A. § 512 → `https://law.justia.com/codes/vermont/title-12/chapter-23/section-512/` — expect: "Actions for the following causes shall be commenced within three"
- **Evidence (2026-10-17):** WebFetch: body present, '2025 Vermont Statutes', not truncated. Second citation 9 V.S.A. § 2453 (/title-9/chapter-63/section-2453/): '(a) Unfair methods of competition in commerce and unfair or'. | Independent check 2026-10-17: WebFetch YES 'Actions for the following causes shall be commenced within three'; '2025 Vermont Statutes'; not truncated; second citation 23 V.S.A. § 1201 ok

## B. Constitution

### `vt-constitution-leg` — Constitution of the State of Vermont (Vermont General Assembly)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont General Assembly · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution on one page: Chapter I (Declaration of Rights, Articles 1-22) and Chapter II (Plan or Frame of Government, §§ 1-76).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://legislature.vermont.gov/statutes/constitution-of-the-state-of-vermont`
  - Placeholders: Single page (57,836 chars) for every article/section; find 'Article N.' (Chapter I) or '§ N.' (Chapter II) in the text.
  - Index: `https://legislature.vermont.gov/statutes/constitution-of-the-state-of-vermont`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 30; path allowed
  - Fits in one WebFetch window; ch. II § 76 present.
- **Currency:** heading above Chapter I — observed: "AS ESTABLISHED JULY 9, 1793, AND AMENDED THROUGH MARCH 31, 2021"
- **Official status:** Hosted on legislature.vermont.gov beside the 'unofficial' Statutes Online; the constitution page itself carries no official/unofficial statement.
- **Hazard:** the 'amended through March 31, 2021' heading is stale: the page includes the 2022 Article 22 (personal reproductive liberty)
- **Probe:** Vt. Const. ch. I, art. 11 → `https://legislature.vermont.gov/statutes/constitution-of-the-state-of-vermont` — expect: "That the people have a right to hold themselves, their"
- **Evidence (2026-10-17):** WebFetch: ch. I art. 11 YES, ch. II § 76 YES, not truncated. fetch_doc verify at offset 10279; Article 22 '[Personal reproductive liberty]' at 13650; ch. II § 28 '[Courts of justice]' at 28714. | Independent check 2026-10-17: WebFetch YES art. 11; heading 'AMENDED THROUGH MARCH 31, 2021'; Article 22 and ch. II § 76 present; second citation Vt. Const. ch. II, § 37 ok

### `vt-constitution-justia` — Justia — Vermont Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page; stale (lacks 2022 Article 22).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/vermont/`
  - Placeholders: single page
  - Index: `https://law.justia.com/constitution/vermont/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
  - WebFetch reported a garbled break in ch. II § 20.
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version."
- **Official status:** 'This Constitution may not be the most recent version.'
- **Hazard:** stale text: Article 22 NOT PRESENT
- **Hazard:** shell blocked
- **Probe:** Vt. Const. ch. I, art. 11 → `https://law.justia.com/constitution/vermont/` — expect: "That the people have a right to hold themselves, their"
- **Evidence (2026-10-17):** WebFetch: art. 11 YES; Article 22 NOT PRESENT; § 20 text cut mid-word then §§ 21-76 continue. | Independent check 2026-10-17: WebFetch YES art. 11; 'This Constitution may not be the most recent version.'; Article 22 absent; § 20 cut mid-word
- **Notes:** Last resort only; prefer vt-constitution-leg.

## C. Court rules

### `vt-rules-lexis` — Vermont Statutes, Constitution and Court Rules (LexisNexis free public access)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · LexisNexis for the State of Vermont · text: **link-only** · official: unknown
- **Coverage:** Full Vermont Rules of Court plus the annotated V.S.A. and constitution (per link labels).
- **Access:** `link-only` · format html
  - Pattern: `https://www.lexisnexis.com/hottopics/vtstatutesconstctrules/`
  - Placeholders: 302 → advance.lexis.com/container?config=… (JavaScript application; no per-rule URL).
  - Index: `https://www.lexisnexis.com/hottopics/vtstatutesconstctrules/`
  - Navigation: interactive browser only
- **Automation:** WebFetch fail · shell unreadable-format · robots: www.lexisnexis.com and advance.lexis.com robots permit the path
  - fetch_doc: 0 chars after redirect; WebFetch: 'The page content provided is empty.'
- **Currency:** none readable
- **Official status:** Linked from legislature.vermont.gov ('Court Rules at Lexis/Nexis') and vtcourts.gov/attorneys/rules as the place for full rule texts; no statement could be read (JavaScript app).
- **Hazard:** JavaScript-only
- **Hazard:** terms of use not readable
- **Hazard:** no deep links
- **Probe:** V.R.C.P. 12 → `https://www.lexisnexis.com/hottopics/vtstatutesconstctrules/`
- **Evidence (2026-10-17):** fetch_doc info: redirect to advance.lexis.com container, kind=html chars=0. WebFetch on the redirect target: empty page.
- **Notes:** Only route to the consolidated text of the Vermont court rules; give the user the link.

### `vt-rules-promulgated` — Vermont Supreme Court promulgation orders (rule amendments, last two years)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont Supreme Court / Vermont Judiciary · text: **fetch-and-quote** · official: official
- **Coverage:** Amended rule text and Reporter's Notes for amendments promulgated in the last two years (V.R.C.P., V.R.Cr.P., V.R.A.P., V.R.E., V.R.F.P., V.R.P.P., V.R.E.C.P., admission rules, administrative orders). NOT a consolidated rule set.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Link slugs are irregular (some drop all punctuation, e.g. /PROMULGATEDVRCP55aSTAMPED; others keep hyphens, e.g. PROMULGATED-VRPP13--STAMPED, PROMULGATED--VRE106--STAMPED). Never build them: take every URL from the links on the index page (fetch_doc.py links). Order titles also vary ('Promulgation Order Amending Rule …' vs 'Order Promulgating Amendments to Rule …'), so do not match on the title wording. The index also lists FORCOMMENT emergency orders.
  - Index: `https://www.vtcourts.gov/attorneys/rules/promulgated`
  - Navigation: promulgated index → PDF for the rule → amended text with new matter underlined; proposed amendments at /attorneys/rules/proposed
- **Automation:** WebFetch untested · shell ok · robots: www.vtcourts.gov: Drupal default (Disallow /admin/, /search/, /user/*, /node/add/ …); /attorneys/rules and /sites/default/files allowed
  - Only the amended rule (or subdivision) is printed, sometimes with strike/underline markup; text of unamended rules is not here.
- **Currency:** order heading — observed: "OCTOBER TERM, 2026"
- **Official status:** Stamped promulgation orders of the Vermont Supreme Court ('Promulgation Order Amending Rule 55(a) of the Vermont Rules of Civil Procedure'), issued under Vt. Const. ch. II, § 37 and 12 V.S.A. § 1.
- **Hazard:** partial: amended subdivisions only
- **Hazard:** underline/strike-through markup lost in text extraction
- **Hazard:** orders older than two years drop off the index
- **Probe:** V.R.C.P. 55(a) → `https://www.vtcourts.gov/PROMULGATEDVRCP55aSTAMPED` — expect: "Promulgation Order Amending Rule 55(a) of the Vermont Rules of Civil Procedure"
- **Evidence (2026-10-17):** fetch_doc: redirect to …/PROMULGATED-VRCP55%28a%29--STAMPED.pdf, 1 p., 3,233 chars; verify at offset 177; amended Rule 55(a) text and 'Reporter's Notes—2027 Amendment' present. | Independent check 2026-10-17: fetch_doc: 'OCTOBER TERM, 2026 Promulgation Order Amending Rule 55(a) of the Vermont Rules of Civil Procedure'; second citation V.R.Cr.P. 49 ok
- **Notes:** The judiciary's rules page links full rule texts only to LexisNexis (vt-rules-lexis).

## D. Administrative code

### `vt-admincode-lexis` — Code of Vermont Rules (LexisNexis free public access)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · LexisNexis for the Vermont Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Code of Vermont Rules, all agencies.
- **Access:** `link-only` · format html
  - Pattern: `https://www.lexisnexis.com/hottopics/codeofvtrules/`
  - Placeholders: Redirects into advance.lexis.com (JavaScript application).
  - Index: `https://www.lexisnexis.com/hottopics/codeofvtrules/`
  - Navigation: interactive browser only
- **Automation:** WebFetch fail · shell unreadable-format · robots: permits the path
  - Fetched directly by the independent check: 302 to an advance.lexis.com container (different config from vt-rules-lexis), then empty content to WebFetch.
- **Currency:** none readable
- **Official status:** Secretary of State APA page and the rules-posting site link 'Code of Vermont Rules' here; the SOS links individual CVR entries (CVR 04-000-001 Rule on Rulemaking) to advance.lexis.com.
- **Hazard:** JavaScript-only
- **Probe:** CVR 04-000-001 → `https://www.lexisnexis.com/hottopics/codeofvtrules/`
- **Evidence (2026-10-17):** fetch_doc check: allowed by robots; Lexis free-access container returns no text to either tool (see vt-rules-lexis).
- **Notes:** SOS also posts some rule PDFs on outside.vermont.gov (e.g. /dept/sos/Services/APA/21-023.pdf, Rule on Rulemaking), not probed.

### `vt-admincode-lii` — Cornell LII — Vermont Administrative Code (Code of Vermont Rules)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Cornell Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Code of Vermont Rules by agency → subagency → chapter → rule.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/vermont/{agency}-{chapter}-Code-Vt-R-{agency}-{subagency}-{chapter}-X`
  - Placeholders: Observed slug for CVR 13-140-001: '13-001-Code-Vt-R-13-140-001-X'; the '-X' suffix and prefix are not proven general, so navigate.
  - Index: `https://www.law.cornell.edu/regulations/vermont`
  - Navigation: /regulations/vermont → agency-13 → agency-13/subagency-140 → chapter-001 → rule page (13-001-Code-Vt-R-13-140-001-X)
- **Automation:** WebFetch ok (truncated) · shell ok · robots: www.law.cornell.edu: crawl-delay 10; path allowed
  - Rule pages can exceed 100K chars (13-140-001: 123,545 chars); WebFetch stopped before the Notes; use offset=100000 or fetch_doc.py.
- **Currency:** 'Notes' at the end of the rule page — observed: "EFFECTIVE DATE: February 15, 1992 (Secretary of State Rule Log # 92-4)"
- **Official status:** Third-party compilation (LII 'State Regulations').
- **Hazard:** long rules truncated by WebFetch
- **Hazard:** currency only via rule history notes
- **Probe:** Code Vt. R. 13-140-001 → `https://www.law.cornell.edu/regulations/vermont/13-001-Code-Vt-R-13-140-001-X` — expect: "Permissible Exposure Limit"
- **Evidence (2026-10-17):** fetch_doc verify at offset 17521 (123,545 chars). WebFetch: YES, 'Section 1 General Provisions 1.1 Purpose These regulations, as authorized'; truncated at 100K before Notes. | Independent check 2026-10-17: fetch_doc grep: '1.2.48 Permissible Exposure Limit - Airborne concentration of asbestos' (123,545 chars); second citation CVR 04-000-001 (Rule on Rulemaking) ok

## D. Administrative register

### `vt-register-sos` — Proposed Rules Postings (Secretary of State APA notices)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current proposed and emergency rule notices (number, agency, legal authority, persons affected, economic impact, posting date); RSS and calendar.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Recent list at index.php; search.php for older; rule numbers like 26P032 (proposed) / 26-E03 (emergency); detail opens by script (href='#').
  - Index: `https://secure.vermont.gov/SOS/rules/index.php`
  - Navigation: index.php (recent) or rssFeed.php (RSS 2.0 items 'Rule:26P001' with full description)
- **Automation:** WebFetch untested · shell ok · robots: secure.vermont.gov: Disallow /UAT/ only
  - Rule detail popups are script-driven; the RSS feed carries the full notice descriptions.
- **Currency:** list 'Posting Date' column; RSS pubDate — observed: "29 Rules Found; latest posting Oct 07, 2026"
- **Official status:** 'A Service of the Office of the Secretary of State'; Vermont has no printed register: notices are posted here and in newspapers of record (sos.vermont.gov/…/apa-rules/notices-of-rulemaking).
- **Hazard:** notices only, not adopted rule text
- **Hazard:** detail pages script-driven
- **Hazard:** rolling list: counts and the probe rule change as postings age; for a durable check use rssFeed.php or search.php
- **Probe:** 26P032 (Home Health Services) → `https://secure.vermont.gov/SOS/rules/index.php` — expect: "Home Health Services."
- **Evidence (2026-10-17):** fetch_doc: 11,366 chars; '29 Rules Found'; 26P032 Agency of Human Services 'Home Health Services.' Oct 07, 2026. rssFeed.php: RSS 2.0, 27,624 chars, items 'Rule:26P001'. | Independent check 2026-10-17: fetch_doc: '29 Rules Found'; 'Home Health Services. Oct 07, 2026 Agency of Human Services'

## E. Case law

### `vt-opinions-courts` — Opinions, Decisions and Order Library (Vermont Judiciary)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court opinions and three-justice entry orders (sparse 2003-2005; full listing pages from 2006), plus Superior Court Civil, Criminal, Family, Probate and Environmental Division decisions. Library pages for 1998 and 2001 return no Supreme Court items.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.vtcourts.gov/opinions-decisions?search_api_fulltext={docket_or_party}&f%5B0%5D=court_division_opinions_library_%3A7`
  - Placeholders: Plain GET (verified with WebFetch and fetch_doc). Facets: court_division_opinions_library_ 7=Supreme, 1=Civil, 2=Criminal, 3=Environmental, 4=Family, 6=Probate; add f%5B1%5D=document_type%3A94 for Opinions (92 Decisions, 93 Judgements, 96 Orders). Date range: facet_from_date=MM/DD/YYYY&facet_to_date=MM/DD/YYYY. Search matches docket ('25-AP-345', '2015-376') and party name ('Polomsky'); a public-domain cite ('2026 VT 44') does NOT resolve to one row. Result rows link /media/{id}, which redirects to /sites/default/files/documents/{name}.pdf (Supreme: op{yy}-{seq}.pdf, eo{yy}-{seq}.pdf, eo{yyyy}-{seq}.pdf with occasional suffixes; trial: free-form names). The host vermontjudiciary.org redirects to vtcourts.gov.
  - Index: `https://www.vtcourts.gov/opinions-decisions`
  - Navigation: GET search URL → row → /media/{id} → PDF
- **Automation:** WebFetch ok · shell ok · robots: Drupal default: Disallow /search/, /admin/, /user/*, /media/oembed …; /opinions-decisions, /media/{id} and /sites/default/files allowed
  - Supreme Court opinion PDFs are 20-50K chars and fit one WebFetch window (2026 VT 44 complete to ¶ 38).
- **Currency:** listing date column (10/09/2026 = newest Supreme row of any document type; newest Opinion-type row was 10/05/2026) — observed: "latest Supreme Court rows dated 10/09/2026"
- **Official status:** Opinion PDFs: 'subject to motions for reargument under V.R.A.P. 40 as well as formal revision before publication in the Vermont Reports.'
- **Hazard:** slip opinions: Vermont Reports page numbers absent (pinpoint by ¶, which is official)
- **Hazard:** entry orders of three-justice panels are not precedent
- **Hazard:** trial-court PDFs are scans with OCR errors ('7ermont Superior Court')
- **Hazard:** searching a trial docket does not find the appeal
- **Probe:** Ford v. Polomsky, 2026 VT 44 (No. 25-AP-345) → `https://www.vtcourts.gov/sites/default/files/documents/op25-345.pdf` — expect: "Plaintiff appeals a civil division order dismissing his claim"
- **Evidence (2026-10-17):** Search ?search_api_fulltext=25-AP-345 + Supreme facet → 1 row, /media/20708 → op25-345.pdf, 19 pp., '2026 VT 44'; verify at offset 1363. WebFetch: YES, complete to ¶ 38. Second: /media/20731 → eo25-364.pdf entry order (State v. Skinner); 2008 listing → eo2008-164.pdf '2008 VT 138'; 'No. 2015-376' search → op15-376_3.pdf (2016 VT 102). | Independent check 2026-10-17: WebFetch YES 'Plaintiff appeals a civil division order dismissing his claim'; 2026 VT 44; complete to ¶ 38; second citation Wich v. Corcoran, 2026 VT 47 (No. 25-AP-423) ok
- **Notes:** Vermont has no intermediate appellate court. The Environmental Division (land use, Act 250) publishes many decisions in the same library (facet 3).

### `vt-cases-justia` — Justia — Vermont Supreme Court decisions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Vermont Supreme Court, year pages 1950-2026.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/vermont/supreme-court/{year}/{docket_lower}.html`
  - Placeholders: Modern slugs are the lower-case docket ('23-ap-003'); pre-2021 slugs use the old docket '{yyyy}-{nnn}.html' (2019/2019-045.html, 2019 VT 88). PDF copy at cases.justia.com/vermont/supreme-court/{year}-{docket}.pdf.
  - Index: `https://law.justia.com/cases/vermont/supreme-court/{year}/`
  - Navigation: year page → case link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party; reproduces the court's slip with its revision notice.
- **Hazard:** shell blocked
- **Hazard:** slip text
- **Probe:** Rawley v. Heymann, 2023 VT 64 (No. 23-AP-003) → `https://law.justia.com/cases/vermont/supreme-court/2023/23-ap-003.html` — expect: "In this declaratory-judgment action, plaintiffs appeal the trial court's grant of"
- **Evidence (2026-10-17):** WebFetch: full opinion through the dissent, '2023 VT 64'. Year page 2023 lists 22-ap-324, 23-ap-177 … with docket slugs; root lists years 1950-2026. | Independent check 2026-10-17: WebFetch YES 'In this declaratory-judgment action, plaintiffs appeal the trial court's grant of'; 2023 VT 64; second citation Commercial Construction Endeavors v. Ohio Security Ins. Co., 2019 VT 88 (No. 2019-045) ok
- **Notes:** Main free route for Supreme Court opinions before 2003-2006, which the judiciary library lacks.

## F. Subsequent history

### `vt-subsequent-history` — Vermont Supreme Court appeals in the judiciary library

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Vermont Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** The Supreme Court is the only appellate court; appeals from every Superior Court division and the Environmental Division go to it directly. Reargument (V.R.A.P. 40) dispositions follow in the same library; U.S. Supreme Court certiorari is the only further review.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.vtcourts.gov/opinions-decisions?search_api_fulltext={party}&f%5B0%5D=court_division_opinions_library_%3A7`
  - Placeholders: Trial-court decisions ARE indexed, but only in an unpadded lower-case docket form: normalise 'YY-TT-NNNNN' to lower-case type with leading zeros stripped from the sequence ('25-CV-01449' → '25-cv-1449'); the padded upper-case form returns 0 rows. The appellate caption names only the unit and division ('On Appeal from Superior Court, Lamoille Unit, Civil Division'), not the trial docket, so search the Supreme Court side by PARTY NAME (Supreme facet, or no facet to see trial and appellate rows together) and confirm unit, division and trial judge from the caption.
  - Index: `https://www.vtcourts.gov/opinions-decisions`
  - Navigation: normalised trial docket search ('25-cv-1449') → trial row; party-name GET search → Supreme row → /media/{id} → PDF caption
- **Automation:** WebFetch ok · shell ok · robots: see vt-opinions-courts
- **Currency:** none stated
- **Official status:** Slip opinions and entry orders.
- **Hazard:** trial docket must be normalised (lower-case, no leading zeros) — padded form returns nothing
- **Hazard:** appellate caption lacks the trial docket: link by party name
- **Hazard:** parties may be reversed or abbreviated in trial file names ('ford v polomsky')
- **Probe:** Ford v. Polomsky, No. 25-CV-01449 (Vt. Super. Ct. Sept. 24, 2025) → 2026 VT 44 → `https://www.vtcourts.gov/opinions-decisions?search_api_fulltext=Polomsky` — expect: "John Ford v. Marek Polomsky, MD and University of Vermont Medical Center"
- **Evidence (2026-10-17):** fetch_doc links: 'Polomsky' → /media/20708 (Supreme, 25-AP-345, 2026 VT 44) and /media/19500 (Lamoille civil entry, Case No. 25-CV-01449). Search '25-CV-01449' → 0 rows. Caption of op25-345: 'Superior Court, Lamoille Unit, Civil Division', Benjamin Battles, J. | Correction 2026-10-17 (independent check): search '25-cv-1449' → /media/19500; '25-CV-01449' → 0 rows. | Independent check 2026-10-17: WebFetch: row 'John Ford v. Marek Polomsky, MD and University of Vermont Medical Center' 25-AP-345 present; second citation Wich v. Corcoran (No. 25-AP-423) <- Orange Unit trial decision ok
- **Notes:** Three-justice entry orders also dispose of appeals and are listed under the same docket form.

## Not available (do not look for these again)

- **court_rules** — Readable free text of the consolidated Vermont Rules of Court from a tier-1 or tier-2 host: vtcourts.gov/attorneys/rules and legislature.vermont.gov link full rules only to LexisNexis (JavaScript app, 0 chars to both tools); public.law, Justia and LII hold none; search found only non-permitted third parties. (2026-10-17)
- **statutes** — Free bulk statute download / open API: https://legislature.vermont.gov/docs/api/v1/index.html: API requires a secret key from IT@leg.state.vt.us. (2026-10-17)
- **statutes** — public.law and Cornell LII editions of the V.S.A.: public.law home page: 0 matches for 'Vermont'; LII /states/vermont links out to legislature.vermont.gov and hosts only the Code of Vermont Rules. (2026-10-17)
- **case_law** — Supreme Court opinions before about 2003 on vtcourts.gov: Library date filters for 1998 and 2001 (Supreme facet) return no rows; 2003 and 2005 only a few. (2026-10-17)
- **admin_register** — A printed/periodical Vermont register of rules: Notices are posted on secure.vermont.gov/SOS/rules and in newspapers of record (sos.vermont.gov APA pages); no register publication found. (2026-10-17)

## Open questions

- Whether the Vermont Reports (official, 'Vt.') page numbers are available free anywhere: not found.
- vt-session-laws and vt-register-sos not WebFetch-probed; vt-rules-promulgated PDFs not WebFetch-probed.
- Older Acts and Resolves (before the 2000s) not located.
- CourtListener ids 'vt' and 'vtsuperct' unverified.
- SOS adopted-rule PDFs on outside.vermont.gov not explored as an official alternative to the Lexis CVR.

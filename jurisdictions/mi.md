# Michigan (MI) — free legal sources

_Generated from `data/mi.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: legislature.mi.gov serves one PDF per MCL section at a constructible URL (documents/mcl/pdf/MCL-{chapter}-{section}.pdf) with 'Complete Through PA N of YYYY'; WebFetch reads them but built URLs need user approval and the shell is refused (bot check on robots.txt), so Justia (2025, constructible) is the practical second fetch. Constitution: mcl-chap1.pdf (truncates at Art. IV). Court rules (MCR, MRE, MRPC), opinions, bound Mich App volumes and Supreme Court leave orders are only on www.courts.michigan.gov, whose robots.txt disallows everything: blocked, link-only, with no tier-2 text for the rules. Admin Code: ARS rule-set PDFs by GET (shell ok) and Cornell LII. Case law: Justia (Supreme Court; Court of Appeals published, unpublished, orders) by docket, slip pagination only.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Michigan Supreme Court | `mich (unverified)` | Mich. | Mich., N.W.3d, N.W.2d, N.W. | — |
| Michigan Court of Appeals | `michctapp (unverified)` | Mich. Ct. App. | Mich. App., N.W.3d, N.W.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Michigan Compiled Laws | `MCL 600.5805`; `Mich. Comp. Laws § 600.5805`; `MCL 600.2912a`; `M.C.L. § 750.83`; `MCLA 257.625`; `Mich. Comp. Laws Ann. § 691.1407(1)`; `MCL 600.5801-600.5869`; `section 600.5805 of the Michigan Compiled Laws` | `mi-mcl-pdf` → `mi-mcl-justia` → `mi-mcl-html` |
| Michigan Public Acts (session laws) | `1961 PA 236`; `2026 PA 103` | `mi-mcl-html` |
| Michigan Constitution of 1963 | `Const 1963, art 1, § 17`; `Mich. Const. art. I, § 17`; `Mich Const 1963, art 6, § 1`; `Article 1, Section 17 of the Michigan Constitution` | `mi-constitution-legislature` → `mi-constitution-justia` |
| Michigan Court Rules | `MCR 2.116(C)(10)`; `MCR 7.215(J)`; `Mich. Ct. R. 2.116`; `Michigan Court Rule 6.500`; `MCR 1.105` | `mi-rules-mcr` |
| Michigan Rules of Evidence | `Mich. R. Evid. 401`; `Michigan Rule of Evidence 803(6)` | `mi-rules-mre` |
| Michigan Rules of Evidence (bare MRE) *(only once this jurisdiction is known)* | `MRE 702` | `mi-rules-mre` |
| Michigan Rules of Professional Conduct | `Mich. R. Prof'l Conduct 1.10`; `Michigan Rule of Professional Conduct 8.4`; `Mich. R. Prof. Conduct 1.7`; `Michigan Rules of Professional Conduct, Rule 1.7` | `mi-rules-mrpc` |
| Michigan Administrative Code | `Mich. Admin. Code R 408.10011`; `Mich Admin Code, R 336.1201`; `Mich. Admin. Code r. 336.1201(1)` | `mi-admincode-ars` → `mi-admincode-lii` |
| Bare Michigan rule number (R NNN.NNNN) *(only once this jurisdiction is known)* | `R 408.10011`; `R 336.1201` | `mi-admincode-ars` → `mi-admincode-lii` |
| Michigan Register | `2018 MR 2`; `2026 MR 18`; `Mich. Reg. 2018-2` | `mi-register` |
| Michigan Reports / Michigan Appeals Reports | `People v Seals, 285 Mich App 1; 776 NW2d 314 (2009)`; `Rayford v American House Roseville I, LLC, 512 Mich 103 (2025)`; `285 Mich. App. 1`; `463 Mich. 143`; `Barkley v City of Southfield, ___ Mich App ___; ___ NW3d ___ (2026) (Docket No. 369608)` | `mi-cases-justia` |
| North Western Reporter with Michigan court parenthetical | `776 N.W.2d 314 (Mich. Ct. App. 2009)`; `600 N.W.2d 1 (Mich. 1999)` | `mi-cases-justia` |
| Unpublished Court of Appeals opinion (Michigan style, by docket number) *(only once this jurisdiction is known)* | `unpublished per curiam opinion of the Court of Appeals, issued January 12, 2023 (Docket No. 359401)`; `Docket No. 359401` | `mi-cases-justia` |
| Leave to appeal denied / granted (Michigan style) | `lv den 505 Mich 1023 (2020)`; `lv gtd 512 Mich 900 (2023)`; `lv den ___ Mich ___ (2026)` | `mi-cases-justia` → `mi-subsequent-history-msc-orders` |
| Westlaw / Lexis unreported Michigan cites | `2023 WL 191234 (Mich. Ct. App. Jan. 12, 2023)`; `2023 Mich. App. LEXIS 250` | `mi-cases-justia` |

Regexes (case-insensitive):

- Michigan Compiled Laws: `(?:\bMCLA?\b|\bM\.\s*C\.\s*L\.(?:\s*A\.)?|Mich(?:igan|\.)?\s*Comp(?:iled|\.)?\s*Laws(?:\s+Ann(?:otated|\.)?)?)\s*§*\s*(?P<chapter>\d{1,3}[A-Za-z]?)\.(?P<section>\d+[A-Za-z]*)|sec(?:tion|\.)\s+(?P<chapter2>\d{1,3}[A-Za-z]?)\.(?P<section2>\d+[A-Za-z]*)(?:\([a-z0-9]+\))*\s+of\s+the\s+Michigan\s+Compiled\s+Laws`
- Michigan Public Acts (session laws): `(?P<year>(?:18|19|20)\d\d)\s+PA\s+(?P<act>\d{1,3})\b`
- Michigan Constitution of 1963: `(?:Mich(?:igan|\.)?\s*Const(?:itution|\.)?(?:\s+(?:of\s+)?1963)?|\bConst\.?\s+1963),?\s*art(?:icle|\.)?\s*(?P<article>[IVXL]+|\d{1,2}),?\s*§+\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+|\d{1,2}),?\s+Section\s+(?P<section2>\d+[a-z]?)\s+of\s+the\s+(?:1963\s+)?Michigan\s+Constitution`
- Michigan Court Rules: `(?:\bMCR\b|\bM\.\s*C\.\s*R\.|Mich(?:igan|\.)?\s*Ct\.?\s*R(?:ule)?\.?|Michigan\s+Court\s+Rules?)\s*(?P<rule>\d\.\d{3}[A-Z]?)`
- Michigan Rules of Evidence: `Mich(?:igan|\.)?\s*R(?:ules?|\.)?\s*(?:of\s+)?Evid(?:ence|\.)?\s*(?P<rule>\d{3,4})`
- Michigan Rules of Evidence (bare MRE): `(?:\bMRE\b|\bM\.\s*R\.\s*E\.)\s*(?P<rule>\d{3,4})`
- Michigan Rules of Professional Conduct: `Mich(?:igan|\.)?\s*R(?:ules?|\.)?\s*(?:of\s+)?Prof(?:essional|'?l)?\.?\s*Conduct,?\s*(?:Rule\s+)?(?P<rule>\d\.\d{1,2})`
- Michigan Administrative Code: `Mich(?:igan|\.)?\s*Admin(?:istrative|\.)?\s*Code,?\s*(?:R\.?|r\.|Rule)\s*(?P<part>\d{3})\.(?P<rule>\d{1,5}[a-z]?)`
- Bare Michigan rule number (R NNN.NNNN): `\bR\s+(?P<part>\d{3})\.(?P<rule>\d{3,5}[a-z]?)\b`
- Michigan Register: `(?P<year>(?:19|20)\d\d)\s+MR\s+(?P<issue>\d{1,2})\b|Mich\.\s*Reg\.\s*(?P<year2>(?:19|20)\d\d)-(?P<issue2>\d{1,2})`
- Michigan Reports / Michigan Appeals Reports: `(?P<volume>\d{1,3}|_{2,})\s+Mich\.?(?:\s*(?P<app>App)\.?)?\s+(?P<page>\d{1,4}|_{2,})(?!\w)`
- North Western Reporter with Michigan court parenthetical: `(?P<volume>\d{1,4})\s+N\.?\s*W\.?\s*(?P<series>[23])d\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Mich\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Unpublished Court of Appeals opinion (Michigan style, by docket number): `Docket\s+No(?:s)?\.?\s*(?P<docket>\d{6})\b`
- Leave to appeal denied / granted (Michigan style): `\blv\s+(?:den|gtd|gtd\s+in\s+part)\s+(?P<volume>\d{1,3}|_+)\s+Mich\s+(?P<page>\d{1,4}|_+)`
- Westlaw / Lexis unreported Michigan cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Mich\.|Mich\.\s*(?:App\.\s*)?LEXIS\s+(?P<lexis>\d+))`

Short forms → URL key:

MCL → `MCL`; MCLA → `MCL`; M.C.L. → `MCL`; M.C.L.A. → `MCL`; Mich. Comp. Laws → `MCL`; Mich. Comp. Laws Ann. → `MCL`; MSA → `MSA (Michigan Statutes Annotated, superseded numbering: convert to MCL via the MCL tables, no free route)`

MCL numbers are chapter.section (600.5805 = chapter 600, section 5805); the chapter is the leading digits before the dot, so the per-section PDF URL is fully determined: MCL-{chapter}-{section with letters upper-cased}.pdf. Michigan's own style (Michigan Appellate Opinion Manual) drops periods: 'MCL 600.5805', 'MCR 2.116(C)(10)', 'MRE 702', 'Const 1963, art 1, § 17', '285 Mich App 1; 776 NW2d 314 (2009)', 'lv den 505 Mich 1023'. Bluebook: Mich. Comp. Laws § 600.5805; Mich. Ct. R. 2.116; Mich. R. Evid. 702. A range 'MCL 600.5801-600.5869' is a span: the regex captures the first section only. Old 'MSA 27A.5805' (Michigan Statutes Annotated) numbering is not routed. Bare 'R 408.10011' and bare 'Docket No. 359401' are generic and need Michigan context (context_required). 'Const 1963' alone is used only by Michigan in practice, but 'Mich' is preferred. No public-domain citation: Michigan cites to Mich / Mich App (official, West-published) and NW2d/NW3d; unpublished COA opinions are cited by docket number and issue date (MCR 7.215(C)). CourtListener ids mich / michctapp are from memory and unverified. 'MRPC' is also Minnesota's abbreviation, so bare 'MRPC 1.7' is not routed by a Michigan pattern (Minnesota's record owns it); with Michigan context, read it from mi-rules-mrpc. 'Act N of YYYY' collides with Pennsylvania's form and is not routed; use 'YYYY PA N'. Court rules (MCR, MRE, MRPC) route to link-only rows: www.courts.michigan.gov is blocked (robots Disallow: /) and no tier-2 host carries them, so cite them by number and never quote. Case law routes to Justia first (slip pagination only); official Mich/Mich App pages and MSC leave orders have no permitted route. Blank-slip '___ Mich App ___' forms are matched by the reports pattern. Bare 'MRE NNN' / 'M.R.E. NNN' is context_required: Mississippi uses the same abbreviation (split 2026-10-17).

## A. Statutes / code

### `mi-mcl-html` — Michigan Compiled Laws — HTML section and act pages (legislature.mi.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Michigan Legislative Council / Legislative Service Bureau · text: **link-only** · official: unofficial
- **Coverage:** MCL sections, acts, chapter indexes; Public Act lookups.
- **Access:** `index-anchored` · format html
  - Placeholders: No working per-section pattern: Laws/MCL?objectName=mcl-600-5805 served E.R.O. No. 2007-2 (§ 18.44) in the independent check, and GetObject?objectName=mcl-chap600 served chapter 18. Chapter pages list acts with section ranges.
  - Index: `https://legislature.mi.gov/Laws/ChapterIndex`
  - Navigation: ChapterIndex (chapter numbers and titles only, NO section ranges) → GetObject?objectName=mcl-chap{N} (acts with section ranges) → Laws/MCL?objectName=mcl-Act-{n}-of-{year} or section page.
- **Automation:** WebFetch gated · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py refused)
  - ChapterIndex and MCLSearch fetched OK (URLs from a search result / page). GetObject?objectName=mcl-chap600 returned the Chapter 18 page instead (session-dependent redirect?) — do not trust GetObject output without checking the chapter heading. Laws/MCL?objectName=mcl-600-5805 gated twice.
- **Currency:** page header — observed: "Michigan Compiled Laws Complete Through PA 103 of 2026"
- **Official status:** Same disclaimer as mi-mcl-pdf: 'not intended to replace official versions of that information.'
- **Hazard:** objectName pages can serve an unrelated object (mcl-600-5805 → E.R.O. 2007-2): check the section number in the heading
- **Hazard:** GetObject returned the wrong chapter (chap18 for chap600)
- **Hazard:** built URLs gated
- **Hazard:** ChapterIndex shows no section ranges
- **Probe:** MCL chapter index → `https://legislature.mi.gov/Laws/ChapterIndex`
- **Evidence (2026-10-17):** WebFetch: PROVENANCE_REQUIRED (permission not answered) on the section page and on https://www.legislature.mi.gov/. ChapterIndex OK: 'Michigan Compiled Laws Complete Through PA 103 of 2026', links GetObject?objectName=mcl-chap{N}. | Independent check 2026-10-17: FAILED — objectName=mcl-600-5805 returned E.R.O. No. 2007-2, section 18.44
- **Notes:** Use as a link target; read text from mi-mcl-pdf. LitWebServices API reported at https://legislature.mi.gov/litwebservices/litwebservices.asmx (not probed).

### `mi-mcl-pdf` — Michigan Compiled Laws — per-section PDFs (legislature.mi.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Michigan Legislative Council / Legislative Service Bureau · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Every MCL section (including repealed-section notices) and every act as a separate PDF; chapter 1 = Constitution of 1963.
- **Access:** `constructible` · format pdf
  - Pattern: `https://legislature.mi.gov/documents/mcl/pdf/MCL-{chapter}-{section}.pdf`
  - Placeholders: chapter = digits before the dot, section = digits after it, with any letter suffix UPPER-cased (MCL 257.203a → MCL-257-203A.pdf). Lower-case 'mcl-' prefix also served (mcl-26-1.pdf, mcl-chap1.pdf). The www. host serves the same files. Whole act: MCL-ACT-{act}-OF-{year}.pdf. Repealed ranges are served under the first section of the range (600.5040-600.5065 under MCL-600-5040.pdf). Index (chapter → acts with section ranges): https://legislature.mi.gov/Laws/ChapterIndex → GetObject?objectName=mcl-chap{N}.
  - Index: `https://legislature.mi.gov/Laws/ChapterIndex`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: fetch_doc.py: robots.txt on legislature.mi.gov and www.legislature.mi.gov answered with a bot check — host refused
  - WebFetch reads the PDFs when the URL came from a search result (MCL-257-201, MCL-600-5040, MCL-750-567, MCL-750-46 all OK), but built URLs (mcl-600-5805.pdf) waited on a permission prompt and timed out: each built URL needs user approval. Site 'Automated Data Collection Policy' (legislature.mi.gov/Home/AutomatedDataCollectionPolicy) permits automated access at max 1 request/second; nevertheless fetch_doc.py is refused at robots.txt, so do not use the shell. Mirror hostnames seen in search results (zeus-milenia., hercules-milenia., capitol., ombudsman., renderpdf.legislature.mi.gov) are not used.
- **Currency:** PDF header/footer of every section — observed: "Rendered Monday, September 28, 2026 … Complete Through PA 103 of 2026"
- **Official status:** MCL Search page (https://legislature.mi.gov/Laws/MCLSearch) says the information 'is not intended to replace official versions of that information.' PDFs carry only 'Courtesy of legislature.mi.gov'.
- **Hazard:** every built URL needs user approval in WebFetch; if not approved, find the PDF URL by web search or fall back to mi-mcl-justia
- **Hazard:** built URLs are WebFetch-gated (need approval)
- **Hazard:** shell refused at robots.txt (bot check)
- **Hazard:** repealed sections show only a repeal notice; ranges are filed under the first number
- **Hazard:** letter suffixes must be upper-cased in the file name
- **Hazard:** independent second citation (MCL 600.2912a → MCL-600-2912A.pdf) untestable: WebFetch gated and fetch_doc.py refused
- **Probe:** MCL 257.201 → `https://www.legislature.mi.gov/documents/mcl/pdf/MCL-257-201.pdf` — expect: "When a reference is made in this act to "division","
- **Evidence (2026-10-17):** WebFetch 2026-10-16: MCL-257-201.pdf body YES 'When a reference is made in this act to "division",'; 'History: 1949, Act 300'; 'Complete Through PA 103 of 2026'; not truncated. Pattern also confirmed on MCL-600-5040.pdf, MCL-750-567.pdf, MCL-750-46.pdf (repeal notices, 3 chapters). Built URL mcl-600-5805.pdf: PROVENANCE_REQUIRED (gated). | Independent check 2026-10-17: MCL-257-201.pdf 'When a reference is made in this act to "division",'; Complete Through PA 103 of 2026; second citation MCL 600.2912a FAILED (gated + script refused)
- **Notes:** Bulk: the policy page says the full MCL is available as PDF and XML by directory browsing at https://legislature.mi.gov/documents/mcl/ with monthly archives since 2013 (documents/mcl/archive/{YYYY}/{Month}/…); the directory URL itself was gated for WebFetch and refused to the shell, so it is recorded, not verified.

### `mi-mcl-justia` — Justia — Michigan Compiled Laws (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 2025 Michigan Compiled Laws, per-section pages; earlier editions (2010–2024) by year path.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/michigan/chapter-{chapter}/statute-act-{act}-of-{year}/[division-{act}-{year}-{division}/]section-{chapter}-{section}/`
  - Placeholders: Act and division (the act's internal chapter, e.g. RJA chapter 58) are NOT derivable from the MCL number: chapter page lists acts with section ranges (Act 236 of 1961: 600.101-600.9948); act page lists divisions with ranges ('(600.5801...600.5869)'). Section slug: dot → hyphen (600-5805). Omit the division segment when the act page lists sections directly (verified: Act 170 of 1964 → chapter-691/statute-act-170-of-1964/section-691-1407/).
  - Index: `https://law.justia.com/codes/michigan/chapter-{chapter}/`
  - Navigation: chapter-{N}/ (acts with ranges) → statute-act-{a}-of-{y}/ (divisions with ranges) → section page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a Cloudflare challenge
  - WebFetch only.
- **Currency:** page title — observed: "2025 Michigan Compiled Laws"
- **Official status:** Page states 'These codes may not be the most recent version.'
- **Hazard:** edition lag (2025)
- **Hazard:** act/division hop needed
- **Hazard:** shell blocked
- **Probe:** MCL 600.5805 → `https://law.justia.com/codes/michigan/chapter-600/statute-act-236-of-1961/division-236-1961-58/section-600-5805/` — expect: "A person shall not bring or maintain"
- **Evidence (2026-10-17):** WebFetch 2026-10-16: body YES 'Sec. 5805. (1) A person shall not bring or maintain'; through (16)(c) plus History; not truncated. Chapter-600 and act pages show section ranges. | Independent check 2026-10-17: 'Sec. 5805.' '(1) A person shall not bring or maintain'; '2025 Michigan Compiled Laws'; not truncated; second citation MCL 691.1407 ok

## B. Constitution

### `mi-constitution-legislature` — Michigan Constitution of 1963 (legislature.mi.gov, MCL chapter 1 PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Michigan Legislative Council · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current constitution as amended, 93-page PDF; also as-ratified 1963 and 1908 PDFs and an indexed version.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://legislature.mi.gov/documents/mcl/pdf/mcl-chap1.pdf`
  - Placeholders: Single whole-document PDF. Other versions linked from https://legislature.mi.gov/Laws/Constitution: documents/publications/MIConstitution.pdf (TOC+index, 'Updates may be slightly delayed'), documents/mcl/pdf/michiganconstitution1963asratified.pdf, documents/historical/miconstitution1908asratified.pdf. Per-section HTML pages (objectName=mcl-Article-I-17 style) are recalled from memory only.
  - Index: `https://legislature.mi.gov/Laws/Constitution`
  - Navigation: Laws/Constitution (links only, no text) → mcl-chap1.pdf
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: bot check (fetch_doc.py refused)
  - WebFetch window ends at Art. IV § 34 heading; Arts. V–XII not reached in window 1 (offset reads untested).
- **Currency:** PDF page header — observed: "Rendered Wednesday, September 30, 2026 … Complete Through PA 103 of 2026"
- **Official status:** Same legislature.mi.gov disclaimer ('not intended to replace official versions').
- **Hazard:** WebFetch truncation at Art. IV § 34 (Art. VI § 1 NOT PRESENT)
- **Hazard:** shell refused
- **Probe:** Const 1963, art 1, § 17 → `https://legislature.mi.gov/documents/mcl/pdf/mcl-chap1.pdf` — expect: "No person shall be compelled in any criminal case to"
- **Evidence (2026-10-17):** WebFetch 2026-10-16: art 1 § 17 YES 'No person shall be compelled in any criminal case to'; art 6 § 1 NOT PRESENT; 'Page 1 of 93'; truncated mid-heading at Art. IV § 34. | Independent check 2026-10-17: art 1 § 17 'No person shall be compelled in any criminal case to'; Page 31 of 93; cut at '§ 34 Bills, re'; second citation Const 1963, art 4, § 24 ok

### `mi-constitution-justia` — Justia — Michigan Constitution

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **link-only** · official: unofficial
- **Coverage:** Michigan Constitution of 1963 (not probed).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/constitution/michigan/article-{article_roman_lower}/`
  - Index: `https://law.justia.com/constitution/michigan/`
  - Navigation: index → article-{roman, lower-case}/ → section link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com robots.txt answered with Cloudflare challenge
  - Not fetched (budget).
- **Currency:** none stated — observed: "Justia: may not be the most recent version"
- **Official status:** Third-party compilation.
- **Hazard:** unprobed
- **Probe:** Const 1963, art 1, § 17 → `https://law.justia.com/constitution/michigan/`
- **Evidence (2026-10-17):** Not fetched; Justia constitution path pattern known from other states. | Independent check 2026-10-17: index lists preamble and articles; Article I at /constitution/michigan/article-i/; article/section pages not fetched

## C. Court rules

### `mi-rules-mcr` — Michigan Court Rules of 1985 (responsive HTML, one page per chapter)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Supreme Court · text: **link-only** · official: unknown
- **Coverage:** MCR chapters 1–9; each chapter one HTML page with all its rules.
- **Access:** `constructible` · format html
  - Pattern: `https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/michigan-court-rules/michigan-court-rules-responsive-html5.zip/Michigan_Court_Rules/Court_Rules_Chapter_{chapter}/Court_Rules_Chapter_{chapter}.htm`
  - Placeholders: chapter = the digit before the dot in the MCR number (MCR 2.116 → 2). Verified only for chapter 1; chapter 2 URL built from the same pattern was gated (not fetched).
  - Index: `https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/michigan-court-rules/michigan-court-rules-responsive-html5.zip/Michigan_Court_Rules/Updated/Updated.htm`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: WebFetch read chapter 1 in full (URL from search). Built chapter URLs need approval. Large chapters (2 Civil Procedure, 6 Criminal, 7 Appellate) likely exceed the ~100K WebFetch window (untested).
- **Currency:** top of each chapter page; separate 'Updated' page — observed: "Chapter Updated with MSC Order(s) Effective on January 1, 2026"
- **Official status:** Published by the Michigan Supreme Court on courts.michigan.gov; no official/unofficial statement seen on the chapter page.
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** built URLs gated
- **Hazard:** shell disallowed by robots
- **Hazard:** likely WebFetch truncation on long chapters
- **Hazard:** 'Updated' page said 'Updated May 1, 2025' while chapter 1 said Jan. 1, 2026 — trust the chapter line
- **Probe:** MCR 1.105 → `https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/michigan-court-rules/michigan-court-rules-responsive-html5.zip/Michigan_Court_Rules/Court_Rules_Chapter_1/Court_Rules_Chapter_1.htm` — expect: "These rules are to be construed, administered, and employed by"
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: MCR 1.105 YES 'These rules are to be construed, administered, and employed by'; last rule 1.201; not truncated. Chapter 2 (MCR 2.116) built URL: PROVENANCE_REQUIRED.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy

### `mi-rules-mre` — Michigan Rules of Evidence (PDF)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Supreme Court · text: **link-only** · official: unknown
- **Coverage:** MRE 101–1102, about 25 pages.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.michigan.gov/492ca5/siteassets/rules-instructions-administrative-orders/rules-of-evidence/michigan-rules-of-evidence.pdf`
  - Placeholders: The hex segment (492ca5) is a cache-buster that changes on re-publication; the path without it (/siteassets/rules-instructions-administrative-orders/rules-of-evidence/michigan-rules-of-evidence.pdf) is the likely stable form (unverified).
  - Index: `https://www.courts.michigan.gov/rules-administrative-orders-and-jury-instructions/`
  - Navigation: rules page → Michigan Rules of Evidence PDF (index not fetched; URL taken from a search result)
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: Whole document fits one WebFetch window.
- **Currency:** PDF header — observed: "Updated with MSC order(s) effective on 1/28/2026"
- **Official status:** Published on courts.michigan.gov; no statement.
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** cache-buster path segment changes
- **Hazard:** shell disallowed
- **Probe:** MRE 702 → `https://www.courts.michigan.gov/492ca5/siteassets/rules-instructions-administrative-orders/rules-of-evidence/michigan-rules-of-evidence.pdf` — expect: "A witness who is qualified as an expert by knowledge"
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: MRE 702 YES 'A witness who is qualified as an expert by knowledge'; ends at Rule 1102; not truncated.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy

### `mi-rules-mrpc` — Michigan Rules of Professional Conduct (PDF)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Supreme Court · text: **link-only** · official: unknown
- **Coverage:** MRPC with comments, ~130K characters.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/rules-of-professional-conduct/michigan-rules-of-professional-conduct.pdf`
  - Placeholders: Fixed document path (search result carried '?r=1').
  - Index: `https://www.courts.michigan.gov/rules-administrative-orders-and-jury-instructions/`
  - Navigation: rules page → MRPC PDF
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: WebFetch window 1 ends in Rule 1.10(c)(2); rest needs offset=100000 (130,109 chars total).
- **Currency:** PDF page header — observed: "Last Updated 1/1/2025"
- **Official status:** Published on courts.michigan.gov; no statement.
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** WebFetch truncation after Rule 1.10
- **Hazard:** shell disallowed
- **Probe:** MRPC 1.7 → `https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/rules-of-professional-conduct/michigan-rules-of-professional-conduct.pdf?r=1` — expect: "A lawyer shall not represent a client if the representation"
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: MRPC 1.7 YES 'A lawyer shall not represent a client if the representation'; truncated after 1.10(c)(2); 130,109 chars.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy
- **Notes:** No tier-2 text source (Justia, LII, public.law checked by the verifier).

## D. Administrative code

### `mi-admincode-ars` — Michigan Administrative Code (ARS — Administrative Rulemaking System)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Michigan Office of Administrative Hearings and Rules (LARA) · text: **fetch-and-quote** · official: unknown
- **Coverage:** All current rule sets, one PDF (and HTML rendering) per rule set, listed by department and bureau.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://ars.apps.lara.state.mi.us/AdminCode/DownloadAdminCodeFile?FileName=R%20{first}%20to%20R%20{last}.pdf`
  - Placeholders: File name is the rule set's range ('R 408.10001 to R 408.10098.pdf'), not derivable from a single rule number. Append &ReturnHTML=True for HTML. Listing by GET: https://ars.apps.lara.state.mi.us/AdminCode/DeptBureauAdminCode?Department={department name, URL-encoded}[&Bureau={bureau}] — rows show each rule set's first and last rule. The home search form (AdminCode/AdminCode, field RuleNumber) is POST-only; a GET ?RuleNumber= returns the blank form.
  - Index: `https://ars.apps.lara.state.mi.us/AdminCode/AdminCode`
  - Navigation: DeptBureauAdminCode?Department=… (GET) → row whose range covers the rule → DownloadAdminCodeFile PDF. Use fetch_doc.py links on the listing and filter on the part number (e.g. '408\.100'). Filter on the bare part number (no 'R ' prefix): link text is 'PDF'/'HTML' and URLs encode the space as %20, so 'R 338\.3' returns 0 links.
- **Automation:** WebFetch untested · shell ok · robots: none (no robots rules)
  - Department names as in the form: 'Labor and Economic Opportunity', 'Environment, Great Lakes and Energy', 'Licensing and Regulatory Affairs', etc. MIOSHA listing is ~152K chars.
- **Currency:** history note after each rule (no page-level currency) — observed: "History: 1979 AC; 2018 AACS."
- **Official status:** LARA 'Using the Michigan Administrative Code' page warns 'there may be errors contained in the code text'; no official-status statement.
- **Hazard:** rule-set file name not derivable from rule number
- **Hazard:** search form POST-only
- **Hazard:** large rule-set PDFs (R 336.1201-1299: 73 pp, 247K chars)
- **Probe:** Mich. Admin. Code R 408.10011 → `https://ars.apps.lara.state.mi.us/AdminCode/DownloadAdminCodeFile?FileName=R%20408.10001%20to%20R%20408.10098.pdf` — expect: "An employer shall comply with all of the following"
- **Evidence (2026-10-17):** fetch_doc.py: 8-page PDF, 16,094 chars; verify 'An employer shall comply with all of the following' VERIFIED p.2. Second citation R 336.1201 (EGLE listing → 'R 336.1201 to R 336.1299.pdf', 73 pp): verify 'a person shall not install, construct, reconstruct, relocate, or modify any process' VERIFIED p.1. | Independent check 2026-10-17: verify 'An employer shall comply with all of the following' VERIFIED p.2 (8 pp); second citation Mich Admin Code, R 338.303 ok

### `mi-admincode-lii` — Cornell LII — Michigan Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-rule pages with history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-{part}-{rule}`
  - Placeholders: R 408.10011 → Mich-Admin-Code-R-408-10011 (dot → hyphen).
  - Index: `https://www.law.cornell.edu/regulations/michigan`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect crawl delay.
- **Currency:** Notes section — observed: "1979 AC; 2018 MR 2, Eff. 2/2/2018; 'updated quarterly'"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag (Last-Modified Aug 2025 on probed pages)
- **Probe:** Mich. Admin. Code R 408.10011 → `https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-408-10011` — expect: "An employer shall comply with all of the following"
- **Evidence (2026-10-17):** fetch_doc.py: 3,301 chars, body 'Rule 11. An employer shall comply with all of the following'; Last-Modified 2 Aug 2025. Second: Mich-Admin-Code-R-336-1201 body present ('a person shall not install, construct, reconstruct'). | Independent check 2026-10-17: verify 'An employer shall comply with all of the following' VERIFIED; Last-Modified 2 Aug 2025; second citation Mich Admin Code, R 338.303 ok

## D. Administrative register

### `mi-register` — Michigan Register

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Michigan Office of Administrative Hearings and Rules (LARA) · text: **link-only** · official: unknown
- **Coverage:** Current-year issues on michigan.gov (2026 listing page); earlier years in the Library of Michigan CONTENTdm archive.
- **Access:** `index-anchored` · format pdf
  - Placeholders: Year listing: https://www.michigan.gov/lara/bureau-list/moahr/admin-rules/publications/michigan-register/michigan-register-issues-for-year-{YYYY} (2026 linked; other years unverified). Archive: https://cdm16110.contentdm.oclc.org/digital/collection/p16110coll2/search/searchterm/michigan%20register/field/title/mode/exact/conn/and
  - Index: `https://michigan.gov/lara/bureau-list/moahr/admin-rules/publications/michigan-register`
  - Navigation: register page → year listing → issue PDF (not probed)
- **Automation:** WebFetch gated · shell blocked-challenge · robots: www.michigan.gov answered robots.txt with a bot check (fetch_doc.py refused)
  - Register landing page read by WebFetch; the 2026 year listing was gated.
- **Currency:** not seen
- **Official status:** Register page calls it a 'comprehensive source of regulatory information'; no official-status statement.
- **Hazard:** issue PDFs unprobed
- **Hazard:** shell refused
- **Hazard:** older issues on a third-party-hosted state library archive (CONTENTdm)
- **Probe:** 2026 MR (latest issue) → `https://www.michigan.gov/lara/bureau-list/moahr/admin-rules/publications/michigan-register/michigan-register-issues-for-year-2026`
- **Evidence (2026-10-17):** WebFetch: landing page OK (links to 2026 listing and CONTENTdm archive); 2026 listing PROVENANCE_REQUIRED; fetch_doc.py REFUSED (bot check on robots.txt). | Independent check 2026-10-17: landing page links 2026 listing and CONTENTdm archive; no issue PDF URLs on page

## E. Case law

### `mi-coa-bound-volumes` — Michigan Appeals Reports — bound-volume PDFs (courts.michigan.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Reporter of Decisions · text: **link-only** · official: official
- **Coverage:** Mich App volumes as PDFs (vol. 285, July–Oct. 2009 probed); range of volumes and any Michigan Reports equivalent not established.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.michigan.gov/4a5268/siteassets/publications/coa-bound-volumes/bv_miapp{volume}_final.pdf`
  - Placeholders: volume = Mich App volume number; the hex segment is a cache-buster (unverified whether the path works without it). Only vol. 285 probed.
  - Index: `https://www.courts.michigan.gov/`
  - Navigation: publications → Court of Appeals bound volumes (listing page not fetched)
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: WebFetch window 1 ended at p. 46 of vol. 285 (115,086 chars extracted in all — whole volume text likely not fully extracted).
- **Currency:** title page — observed: "Michigan Appeals Reports, vol. 285 (July 14 – Oct. 13, 2009)"
- **Official status:** Volume carries the title page 'Michigan Appeals Reports … Cases Decided in the Michigan Court of Appeals' and names the Reporter of Decisions; official Mich App pagination in running heads.
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** very long PDFs; WebFetch truncation
- **Hazard:** cache-buster path segment
- **Hazard:** shell disallowed
- **Probe:** People v Seals, 285 Mich App 1 (2009) → `https://www.courts.michigan.gov/4a5268/siteassets/publications/coa-bound-volumes/bv_miapp285_final.pdf` — expect: "Cases Decided in the Michigan Court of Appeals"
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: title page present; running heads '285 MICH APP 1'; People v Seals at p. 1 (Docket Nos. 282215, 282216); truncated at p. 46.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy
- **Notes:** The only free source of official Mich App pagination found.

### `mi-opinions-courts` — Michigan Courts — Supreme Court and Court of Appeals opinions and orders (courts.michigan.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Supreme Court / Court of Appeals · text: **link-only** · official: unofficial
- **Coverage:** Court of Appeals opinions (published and unpublished; separate files for majority, concurrence, dissent) and Supreme Court orders and opinions; coverage years not established.
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.courts.michigan.gov/siteassets/case-documents/uploads/OPINIONS/FINAL/COA/{YYYYMMDD}_C{docket}_{seq}_{docket}{type}.OPN.PDF`
  - Placeholders: COA opinion file: decision date, 'C' + 6-digit docket, an internal sequence number (not derivable), docket again, then a type letter (C = concurrence seen; O / D presumably majority / dissent — unverified). Supreme Court orders: /siteassets/case-documents/uploads/sct/public/orders/{SC docket}_{seq}_01.pdf (seq not derivable). An optional hex cache-buster segment (/4927ff/) may precede /siteassets/. Case pages (https://www.courts.michigan.gov/c/courts/coa/case/{docket}) recalled from memory, gated, not verified.
  - Index: `https://www.courts.michigan.gov/`
  - Navigation: Case search at courts.michigan.gov (by docket or party) → case page → opinion/order PDF links. Not verified: the case page URL was gated and robots disallows the shell.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: WebFetch read PDFs whose URLs came from search results; built URLs (case page, site root) were gated.
- **Currency:** none stated
- **Official status:** Slip opinions; official text is Michigan Reports / Michigan Appeals Reports (see mi-coa-bound-volumes).
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** file names contain an internal sequence number — not constructible
- **Hazard:** majority / concurrence / dissent are separate PDFs
- **Hazard:** slip pagination only
- **Hazard:** shell disallowed by robots
- **Hazard:** case search not verified
- **Probe:** Dep't of Env't, Great Lakes & Energy v Brotherton, unpublished opinion of the Court of Appeals, issued January 12, 2023 (Docket No. 359401) → `https://www.courts.michigan.gov/siteassets/case-documents/uploads/OPINIONS/FINAL/COA/20230112_C359401_46_359401C.OPN.PDF` — expect: "SHAPIRO, P.J. (concurring). I concur in the result only."
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: caption EGLE v Brotherton, No. 359401, UNPUBLISHED, Mackinac CC; body 'SHAPIRO, P.J. (concurring). I concur in the result only.'; no reporter cite. Second: SC order 169336_37_01.pdf (People v Cao) read OK.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy
- **Notes:** Mich Bar (michbar.org) mirrors opinions but is not an allowed source.

### `mi-cases-justia` — Justia — Michigan case law

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court; Court of Appeals published, unpublished, and orders (four listings); year ranges not shown.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/michigan/{court-slug}/{year}/{docket}[-N].html`
  - Placeholders: court-slug: supreme-court | court-of-appeals-published | court-of-appeals-unpublished | court-of-appeals-order. year = decision year; docket = 6-digit docket. Several opinions on one docket get suffixes (-0, -1 …), and the unsuffixed page may be a concurrence (359401.html = Shapiro concurrence) — check the year listing. Court PDF: https://cases.justia.com/michigan/{court-slug}/{year}-{docket}.pdf.
  - Index: `https://law.justia.com/cases/michigan/`
  - Navigation: year listing (paginated) shows every decision with docket-based links
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge on robots.txt
  - Long opinions exceed one WebFetch window (Rayford: 118,108 chars).
- **Currency:** none
- **Official status:** Third-party; slip text, no reporter cite on the probed page.
- **Hazard:** docket suffix variants; base slug may be a concurrence
- **Hazard:** WebFetch truncation on long opinions
- **Hazard:** shell blocked
- **Hazard:** slip pagination only — no official Mich / Mich App page numbers
- **Probe:** Rayford v American House Roseville I, LLC, No. 163989 (Mich. July 31, 2025) → `https://law.justia.com/cases/michigan/supreme-court/2025/163989.html` — expect: "In this case, we address whether an employer can contractually"
- **Evidence (2026-10-17):** WebFetch 2026-10-16: body YES; truncated at 100K of 118,108 chars. Second: court-of-appeals-unpublished/2023/359401.html → Shapiro concurrence, Jan. 12, 2023. | Independent check 2026-10-17: Rayford 163989 'In this case, we address whether an employer can contractually'; truncated at 100K of 118,108; second citation Barkley v City of Southfield, No. 369608 (Mich. Ct. App. Aug. 6, 2026) ok

## F. Subsequent history

### `mi-subsequent-history-msc-orders` — Michigan Supreme Court orders on applications for leave to appeal

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Michigan Supreme Court · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court orders (leave denied / granted / peremptory dispositions); each names the COA docket and lower-court number.
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.courts.michigan.gov/siteassets/case-documents/uploads/sct/public/orders/{SC docket}_{seq}_01.pdf`
  - Placeholders: SC docket is a separate 6-digit number; seq not derivable. From a COA docket: courts.michigan.gov case search on the COA docket number should show the related SC docket (memory; not verified — gated and robots-disallowed). Fallback: Justia supreme-court year listings (opinions) and party-name search; Justia does not list MSC leave orders.
  - Index: `https://www.courts.michigan.gov/`
  - Navigation: case search (COA docket) → related Supreme Court case → order PDF; or search engine by party name
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.courts.michigan.gov robots.txt: User-agent: * / Disallow: / — blocked for every route by policy
  - Blocked by policy (SCHEMA robots table). WebFetch had read this document on 2026-10-16 before the policy was settled; it is not used. Cite by number / link only, never quote. Earlier note: Order PDF read when URL came from a search result.
- **Currency:** none stated
- **Official status:** Slip orders; official 'lv den' citations appear later in Michigan Reports order pages.
- **Hazard:** host blocked for every route (robots Disallow: /): link only, never quote
- **Hazard:** no verified docket → order lookup; in practice found by party name
- **Hazard:** shell disallowed
- **Probe:** People v Cao, COA No. 373185, lv den (Mich. Feb. 27, 2026) (SC No. 169336) → `https://www.courts.michigan.gov/4927ff/siteassets/case-documents/uploads/sct/public/orders/169336_37_01.pdf` — expect: "On order of the Court, the application for leave to appeal"
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED — robots.txt on www.courts.michigan.gov disallows the path (rule: Disallow: / for User-agent *). (Earlier WebFetch reads, no longer usable: WebFetch 2026-10-16: SC 169336, COA 373185, Ingham CC 22-000721-FH, Feb. 27, 2026; 'On order of the Court, the application for leave to appeal the October 6, 2025'; leave denied.) | Re-confirmed blocked 2026-10-17: fetch_doc.py check REFUSED (Disallow: /); not WebFetched per policy
- **Notes:** Lookup from the decision below is effectively party-name only for this record until the case search is verified.

## Not available (do not look for these again)

- **case_law** — Public-domain (vendor-neutral) citation format: Michigan cites Mich / Mich App (official reports) and NW2d; unpublished opinions by docket number and issue date. No neutral format seen on any probed opinion. (2026-10-17)
- **court_rules** — Allowed text source for the Michigan Court Rules (MCR): Official text only on www.courts.michigan.gov (robots Disallow: /, blocked). Verifier checked Justia (codes/michigan has only MCL), Cornell LII (states/michigan links out), public.law (no Michigan site) and site-restricted searches for MCR 2.116 / 7.305: none. (2026-10-17)
- **court_rules** — Allowed text source for the Michigan Rules of Evidence (MRE): Official PDF on www.courts.michigan.gov (blocked). Justia, LII and public.law carry no MRE (checked for MRE 702, 404). (2026-10-17)
- **court_rules** — Allowed text source for the Michigan Rules of Professional Conduct (MRPC): Official PDF on www.courts.michigan.gov (blocked). LII ethics paths redirect to wex/legal_ethics; Justia and public.law have none (checked MRPC 1.7, 8.4). (2026-10-17)
- **case_law** — Allowed route for official Mich App / Mich page numbers: Mich App bound-volume PDFs exist only on www.courts.michigan.gov (blocked); Justia gives slip pagination only (Barkley, No. 369608: slip markers, no reporter cite). (2026-10-17)
- **subsequent_history** — Allowed route for Michigan Supreme Court leave-denied / leave-granted orders: Orders are posted only on www.courts.michigan.gov (blocked); Justia lists MSC opinions but not leave orders. Reports must say 'lv den' history was not checked against the order text. (2026-10-17)

## Corpus candidates (maintainers)

- `mi-constitution-legislature` — 93-page PDF; WebFetch stops at Art. IV § 34 heading. Ingest is blocked unless the shell can reach legislature.mi.gov (robots bot check today). · bulk: https://legislature.mi.gov/documents/mcl/ (PDF/XML, per policy page)

## Open questions

- Verify the courts.michigan.gov case search / case page URL (c/courts/coa/case/{docket}) and whether it links the Supreme Court docket for subsequent history.
- Verify Laws/MCL?objectName=mcl-{ch}-{sec} HTML pages and the documents/mcl/ bulk XML directory (both gated).
- Why GetObject?objectName=mcl-chap600 returned chapter 18.
- Michigan Register issue PDF URL pattern and currency (2026 listing gated; michigan.gov refused to the shell).
- Range of Mich App bound volumes online, and whether Michigan Reports bound volumes are also posted.
- Justia Michigan Constitution page not probed; public.law and Cornell LII coverage of MCL / MCR not checked.
- COA opinion file type letters (O/D) and coverage start year unverified.
- CourtListener ids mich / michctapp unverified.
- mi-mcl-pdf: no new citation could be tested by the independent check (WebFetch gated, fetch_doc.py refused at legislature.mi.gov). Re-test MCL-600-2912A.pdf when either route is available.

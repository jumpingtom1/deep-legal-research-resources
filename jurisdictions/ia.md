# Iowa (IA) — free legal sources

_Generated from `data/ia.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: legis.iowa.gov per-section PDFs (/docs/code/{section}.pdf, current Iowa Code 2026; /docs/code/{year}/… for past editions) are constructible and short, but the site labels them unofficial; the eight volume PDFs are the official UELMA edition. Constitution, Iowa Acts, the Iowa Court Rules (per-chapter PDFs, official) and the Iowa Administrative Code and Bulletin (official, constructible per chapter, rule and ARC) are all on legis.iowa.gov, which the script reads freely. Case law: iowacourts.gov case pages are constructible from the docket (about 2018 on) and link slip-opinion PDFs; Justia covers 1859/1977 on. Further-review denials are only on a rolling 'latest batch' page or the docket system; grants show up on the Court of Appeals case page for the same docket.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Iowa Supreme Court | `iowa (unverified)` | Iowa | N.W.3d, N.W.2d, N.W., Iowa | — |
| Iowa Court of Appeals | `iowactapp (unverified)` | Iowa Ct. App. | N.W.3d, N.W.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Iowa Code | `Iowa Code § 614.1(2)`; `Iowa Code section 614.1`; `Iowa Code § 321J.2 (2021)`; `Iowa Code §§ 614.1-.4`; `Iowa Code Ann. § 668.3`; `I.C.A. § 614.1`; `section 614.1 of the Iowa Code`; `Iowa Code ch. 614`; `Iowa Code chapter 17A` | `ia-code-legis` → `ia-code-volumes-legis` → `ia-code-justia` |
| Iowa Acts (session laws) | `2017 Iowa Acts ch. 64, § 2`; `2026 Iowa Acts ch. 1150`; `2019 Iowa Acts, ch. 92` | `ia-acts-legis` |
| Iowa Constitution | `Iowa Const. art. I, § 8`; `Iowa Const. art. I, § 1A`; `article I, section 6 of the Iowa Constitution` | `ia-constitution-legis` → `ia-constitution-justia` |
| Iowa Court Rules (named sets) | `Iowa R. Civ. P. 1.421(1)(f)`; `Iowa R. Evid. 5.702`; `Iowa R. App. P. 6.1103`; `Iowa R. App. P. 6.904(2)(c)`; `Iowa R. Crim. P. 2.24`; `Iowa R. Prof'l Conduct 32:1.7`; `Iowa Rule of Civil Procedure 1.981`; `Iowa Rule of Evidence 5.803(6)`; `Iowa Rule of Professional Conduct 32:8.4(c)`; `Iowa Ct. R. 32:1.7`; `Iowa Ct. R. 21.1` | `ia-courtrules-legis` |
| Iowa Court Rules (bare chapter-numbered rule, no 'Iowa') *(only once this jurisdiction is known)* | `rule 1.421(1)(f)`; `R.C.P. 1.431`; `rule 6.1103`; `rule 32:1.7`; `Rule 5.702` | `ia-courtrules-legis` |
| Iowa Administrative Code | `Iowa Admin. Code r. 641—1.1`; `Iowa Admin. Code r. 641-1.1(139A)`; `641 IAC 1.1`; `567 Iowa Admin. Code 61.3`; `rule 641—1.1(139A)`; `Iowa Admin. Code ch. 567—61` | `ia-iac-legis` → `ia-iac-lii` |
| Iowa Administrative Bulletin | `ARC 0647D`; `ARC 8070C, IAB 6/12/24`; `IAB 10/14/26`; `IAB Vol. XLIX, No. 8 (10/14/26) p. 2627` | `ia-iab-legis` |
| Reported Iowa cases (N.W. / Iowa Reports) | `Godfrey v. State, 898 N.W.2d 844 (Iowa 2017)`; `State v. Ochoa, 792 N.W.2d 260, 264 (Iowa 2010)`; `State v. Short, 851 N.W.2d 474 (Iowa 2014)`; `[name], 900 N.W.2d 100 (Iowa Ct. App. 2017) (form only)`; `[name], 10 N.W.3d 100 (Iowa 2024) (form only)`; `261 Iowa 1` | `ia-opinions-iowacourts` → `ia-cases-justia` |
| Iowa slip opinions and unpublished Court of Appeals opinions (docket + Iowa parenthetical) | `State v. Reasoner, No. 19-0058 (Iowa Ct. App. Mar. 17, 2021)`; `Davenport v. Fuller, No. 25-1183 (Iowa Oct. 16, 2026)`; `Hart v. Iowa Elec. Examining Bd., No. 24-1358, slip op. at 4 (Iowa Ct. App. Oct. 7, 2026)` | `ia-opinions-iowacourts` → `ia-cases-justia` |
| Bare Iowa appellate docket number *(only once this jurisdiction is known)* | `No. 25-1183`; `No. 19–0058` | `ia-opinions-iowacourts` → `ia-cases-justia` |
| Iowa further-review dispositions | `further review denied (Iowa June 15, 2021)`; `further review granted (Iowa Oct. 3, 2026)` | `ia-further-review-casepage` → `ia-further-review-orders` → `ia-docket-ecourts` → `ia-subsequent-justia` |
| Further review (bare, no Iowa parenthetical) *(only once this jurisdiction is known)* | `further review denied`; `aff'd on further review` | `ia-further-review-casepage` → `ia-further-review-orders` → `ia-docket-ecourts` |

Regexes (case-insensitive):

- Iowa Code: `(?:Iowa\s+Code(?:\s+Ann\.)?|I\.C\.A\.)\s*(?:§§?|sec(?:tions?|s?\.))\s*(?P<section>\d{1,3}[A-Z]{0,2}\.\d+[A-Z]{0,2})|Iowa\s+Code(?:\s+Ann\.)?\s*(?:ch\.|chapters?)\s*(?P<chapter>\d{1,3}[A-Z]{0,2})\b|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,3}[A-Z]{0,2}\.\d+[A-Z]{0,2})(?:\([0-9a-z]+\))*,?\s+of\s+the\s+(?:Iowa\s+Code|Code\s+of\s+Iowa)`
- Iowa Acts (session laws): `(?P<year>(?:18|19|20)\d\d)\s+Iowa\s+Acts,?\s*(?:ch\.|chapter)\s*(?P<chapter>\d{1,4})`
- Iowa Constitution: `Iowa\s+Const\.?\s*art\.?\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+[A-Z]?)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Z]?)\s+of\s+the\s+Iowa\s+Constitution`
- Iowa Court Rules (named sets): `Iowa\s+(?:R\.|Rules?\s+of)\s*(?:Civ(?:il)?\.?\s*P(?:roc(?:edure)?)?\.?|Evid(?:ence)?\.?|App(?:ellate)?\.?\s*P(?:roc(?:edure)?)?\.?|Crim(?:inal)?\.?\s*P(?:roc(?:edure)?)?\.?|Prof(?:'l|essional|\.)?\s*Conduct)\s*(?P<chapter>\d{1,2})(?P<sep>[.:])(?P<rule>\d+(?:\.\d+)?)|Iowa\s+Ct\.\s*R\.\s*(?P<chapter2>\d{1,2})(?P<sep2>[.:])(?P<rule2>\d+(?:\.\d+)?)`
- Iowa Court Rules (bare chapter-numbered rule, no 'Iowa'): `\b(?:rule|R\.C\.P\.)\s+(?P<chapter>[1-9]\d?)(?P<sep>[.:])(?P<rule>\d{1,4}(?:\.\d+)?)`
- Iowa Administrative Code: `Iowa\s+Admin\.?\s+Code\s+r(?:ule)?\.?\s*(?P<agency>\d{1,3})\s*[—–-]\s*(?P<chapter>\d{1,3})\.(?P<rule>\d{1,3})|Iowa\s+Admin\.?\s+Code\s+(?:ch\.|chapter)\s*(?P<agency2>\d{1,3})\s*[—–-]\s*(?P<chapter2>\d{1,3})|(?P<agency3>\d{1,3})\s+(?:IAC|Iowa\s+Admin\.?\s+Code)\s+(?:(?:ch\.|chapter)\s*)?(?P<chapter3>\d{1,3})(?:\.(?P<rule3>\d{1,3}))?(?![-\d.])|(?P<agency4>\d{1,3})—(?P<chapter4>\d{1,3})\.(?P<rule4>\d{1,3})\(\d{1,3}[A-Z]{0,2}\)`
- Iowa Administrative Bulletin: `\bARC\s+(?P<arc>\d{3,4}[A-D])\b|\bIAB\s+(?:Vol\.\s*(?P<vol>[IVXL]+),\s*No\.\s*(?P<no>\d+)\s*\()?(?P<date>\d{1,2}/\d{1,2}/\d{2})\)?(?:\s*p\.\s*(?P<page>\d+))?`
- Reported Iowa cases (N.W. / Iowa Reports): `(?P<volume>\d{1,4})\s+N\.\s*W\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>Iowa(?:\s+Ct\.\s+App\.)?)\s*(?P<year>\d{4})\)|(?P<ivol>\d{1,3})\s+Iowa\s+(?P<ipage>\d{1,4})\b`
- Iowa slip opinions and unpublished Court of Appeals opinions (docket + Iowa parenthetical): `No\.\s*(?P<docket>\d{2}[-–]\d{4})(?:,\s*(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+))?(?:,\s*at\s*\*\d+)?(?:,\s*slip\s+op\.\s+at\s+\d+)?,?\s*\((?P<court>Iowa(?:\s+Ct\.\s+App\.)?)\s+[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*\d{4}\)|(?P<wyear>(?:19|20)\d\d)\s+WL\s+(?P<wl2>\d+)(?:,\s*at\s*\*\d+)?\s*\(Iowa(?:\s+Ct\.\s+App\.)?\s`
- Bare Iowa appellate docket number: `\bNo\.\s*(?P<docket>\d{2}[-–]\d{4})\b`
- Iowa further-review dispositions: `further\s+review\s+(?P<disposition>denied|granted|dismissed)\s*\(Iowa\s+(?P<date>[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*(?P<year>\d{4}))\)`
- Further review (bare, no Iowa parenthetical): `further\s+review\s+(?:denied|granted|dismissed)|on\s+further\s+review`

Short forms → URL key:

Iowa Code → `code`; Iowa Code Ann. → `code`; I.C.A. → `code`; Code of Iowa → `code`; Iowa R. Civ. P. → `1`; R.C.P. → `1`; I.R.C.P. → `1`; Iowa R. Crim. P. → `2`; Iowa R. Evid. → `5`; Iowa R. App. P. → `6`; Iowa R. Prof'l Conduct → `32`; Iowa Ct. R. 32 → `32`

Iowa has no public-domain citation; Iowa Reports ended in 1968, so modern cases cite N.W.2d/N.W.3d with '(Iowa YYYY)' or '(Iowa Ct. App. YYYY)'. Court rules carry their chapter in the rule number (1.xxx civil, 2.xxx criminal, 5.xxx evidence, 6.xxx appellate, 32:x.x professional conduct), so law_aliases map rule-set abbreviations to the court-rules chapter used in the URL; the Code aliases map to the statute source. Bare 'rule 1.421' / 'R.C.P. 1.431' (the Iowa Code's own cross-reference style) and bare 'No. 19-0058' dockets are context_required. 'Further review' is also Nebraska's term, so it routes here only with an '(Iowa' parenthetical. Avoid 'I.C.' (Idaho). Unpublished Court of Appeals opinions are cited by docket and date, often with a WL number (Iowa R. App. P. 6.904(2)(c)). The '§§ 614.1-.4' range form is read as its first section. IAC citations use an em dash between agency and chapter and an implementing-statute parenthetical (641—1.1(139A)); the regex accepts hyphen and en dash too. CourtListener ids from memory, unverified.

## A. Statutes / code

### `ia-acts-legis` — Iowa Acts (session laws), per-chapter PDFs

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: official
- **Coverage:** Iowa Acts by General Assembly and session; current 91st GA (2025-2026).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.legis.iowa.gov/docs/publications/iactc/{ga}.{session}/CH{chapter:04d}.pdf`
  - Placeholders: ga = General Assembly number = 91 + floor((Y - 2025) / 2) for year Y (2017 → 87, 2026 → 91); session = 1 for the odd (first) year, 2 for the even (second) year. Chapter zero-padded to 4 digits (CH0064; unpadded CH64 also served). Second-session chapters are numbered from 1001 (2026 Iowa Acts ch. 1150 → 91.2/CH1150.pdf).
  - Index: `https://www.legis.iowa.gov/law/statutory/acts/actsChapter`
  - Navigation: Acts chapter listing (current session) links each chapter PDF and the governor's letter.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - Built URL; WebFetch not tried (likely gated).
- **Currency:** none on the chapter PDF — observed: "CH1150 last-modified 22 Jun 2026"
- **Official status:** Iowa Acts from the 2014 edition are designated official electronic versions (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** GA/session must be computed from the year
- **Probe:** 2017 Iowa Acts ch. 64 → `https://www.legis.iowa.gov/docs/publications/iactc/87.1/CH0064.pdf` — expect: "IMPROVEMENTS TO REAL PROPERTY — UNSAFE OR DEFECTIVE CONDITIONS"
- **Evidence (2026-10-17):** Script: 87.1/CH0064.pdf 1 p., 'CHAPTER 64 IMPROVEMENTS TO REAL PROPERTY', S.F. 413. Second citation 2026 Iowa Acts ch. 1150 → 91.2/CH1150.pdf: 'CHAPTER 1150 CIVIL ACTIONS', S.F. 512.
- **Notes:** 'Code & Acts Sections Amended' (https://www.legis.iowa.gov/law/statutory/acts/amended) maps Code sections to amending acts.

### `ia-code-legis` — Iowa Code, per-section and per-chapter PDFs (legis.iowa.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Iowa Code editions 2004 to current (Iowa Code 2026, published Dec. 2025). Archive of all editions and supplements 1839- at /archives/code.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.legis.iowa.gov/docs/code/[{year}/]{section}.pdf`
  - Placeholders: section exactly as cited, keeping letters (614.1, 614.4A, 321J.2, 2B.17); case-insensitive (2b.10.pdf works). Without {year} the current edition is served (identical sha256 to /docs/code/2026/614.1.pdf). {year} = Iowa Code edition year (2026, 2025 ... 2004); e.g. /docs/code/2023/614.1.pdf. Whole chapter: /docs/code/[{year}/]{chapter}.pdf (614.pdf, 17 pp.). RTF twin: same path with .rtf. Iowa Code edition N contains acts of the session held in year N-1; acts of the current year's session (effective July 1) are in the next edition only.
  - Index: `https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter={chapter}&year={year}`
  - Navigation: Only needed to list a chapter's sections: /law/iowaCode/sections?codeChapter=614&year=2026 lists every section with PDF and RTF links (plain GET). Title pages (/law/iowaCode/chapters?title=XV&year=2026) list chapters; the Iowa Code page shows chapter ranges per title (e.g. 'Title I ... (Ch. 1 - 38D)').
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - WebFetch returned full text of /docs/code/2023/614.1.pdf and the whole 2021 chapter 614 PDF (to 614.38, not truncated); both URLs came from a search. Per-section PDFs are small (614.1: 3 pp., 10,777 chars). Built URLs may need approval for WebFetch; the script reads them.
- **Currency:** footer of every PDF page — observed: "Iowa Code 2026, Section 614.1 (30, 0); footer dated Fri Dec 12 2025"
- **Official status:** The Iowa Code page (https://www.legis.iowa.gov/law/iowaCode) labels the title/chapter/section PDF and RTF files 'Unofficial Version'; the eight volume PDFs are the 'Official Version' (see ia-code-volumes-legis). Iowa Code ch. 2B (UELMA, 2019 Iowa Acts ch. 92) governs designation (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** per-section PDFs are designated unofficial; cite-check against the official volume PDFs when it matters
- **Hazard:** annual edition: acts of the 2026 session are not in Iowa Code 2026 (check Iowa Acts / 'Code & Acts Sections Amended')
- **Hazard:** page headers and footers are interleaved with the text in extraction
- **Probe:** Iowa Code § 614.1(2) → `https://www.legis.iowa.gov/docs/code/614.1.pdf` — expect: "Actions may be brought within the times limited as follows, respectively"
- **Evidence (2026-10-17):** Script: PDF 3 pp., 10,777 chars, '614.1 Period. Actions may be brought within the times limited'; footer 'Iowa Code 2026, Section 614.1 (30, 0)'. Second citation /docs/code/707.2.pdf: 1 p., '707.2 Murder in the first degree.'; /docs/code/321J.2.pdf 4 pp. WebFetch (search URL /docs/code/2023/614.1.pdf): YES, footer 'Iowa Code 2023, Section 614.1 (27, 0)', not truncated.
- **Notes:** Year-specific editions verified for 2021, 2023, 2025, 2026. Chapter 614 PDF: /docs/code/614.pdf (68,530 chars).

### `ia-code-volumes-legis` — Iowa Code, official volume PDFs (Vol. I-VIII)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: official
- **Coverage:** Current Iowa Code (2026) in eight volumes; official designation for editions from 2014.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Volume file names are opaque document ids (e.g. /docs/publications/ICV/1594658.pdf = Vol VI of 2026); take them from the index each edition.
  - Index: `https://www.legis.iowa.gov/law/statutory`
  - Navigation: Iowa Law page → 'Vol I' ... 'Vol VIII' links → volume PDF; find the section by grep ('614.1 Period.').
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - Volumes are far beyond the fetch tool's ~100K-character window (Vol VI: 1,581 pp., 6.4M chars); use fetch_doc.py grep/section.
- **Currency:** volume title pages and page footers — observed: "last-modified 22 Dec 2025 (Vol VI)"
- **Official status:** https://www.legis.iowa.gov/law/statutory: '2026 Iowa Code and Iowa Constitution (Official Version - PDF format)'; UELMA designation and authentication since Jan. 9, 2020 (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** very large PDFs
- **Hazard:** opaque file ids change every edition
- **Probe:** Iowa Code (2026), Vol. VI → `https://www.legis.iowa.gov/docs/publications/ICV/1594658.pdf` — expect: "Iowa Code 2026"
- **Evidence (2026-10-17):** Script info: PDF 1,581 pages, 6,414,052 chars, last-modified Mon, 22 Dec 2025. Links for Vol I-VIII (ICV/1594653-1594660) read from /law/statutory with fetch_doc.py links. Section-level grep not run.
- **Notes:** Use as the official cross-check; read per-section text from ia-code-legis.

### `ia-code-justia` — Justia — Iowa Code (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Iowa Code editions incl. 2016, 2023, 2024, 2025; unversioned URLs serve 2025 (one edition behind legis.iowa.gov's 2026).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/iowa/[{year}/]title-{title_roman_lower}/chapter-{chapter_lower}/section-{section_dashed}/`
  - Placeholders: title = Roman numeral of the Iowa Code title, lower case (chapter 614 → title-xv, chapter 707 → title-xvi); the title is NOT derivable from the section, take it from the legis.iowa.gov Iowa Code page, whose title links show chapter ranges ('Title I ... (Ch. 1 - 38D)'). chapter lower-case (chapter-614, chapter-321j). section_dashed = section with '.' → '-' and letters lower-case (614.4A → section-614-4a).
  - Index: `https://law.justia.com/codes/iowa/`
  - Navigation: title page (link texts show chapter numbers, no section ranges) → chapter page (section links) → section page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell: law.justia.com robots.txt answers with a Cloudflare challenge
  - Script: 'law.justia.com refused automated access earlier (robots.txt challenge)'. Fetch tool only; a built section URL (707.2) went through without approval.
- **Currency:** page heading and universal citation — observed: "2025 Iowa Code; 'IA Code § 614.1 (2025)'"
- **Official status:** Page disclaimer 'These codes may not be the most recent version'.
- **Hazard:** one edition behind the official site
- **Hazard:** title must be looked up
- **Hazard:** shell blocked
- **Probe:** Iowa Code § 614.1 → `https://law.justia.com/codes/iowa/title-xv/chapter-614/section-614-1/` — expect: "Actions may be brought within the times limited as follows"
- **Evidence (2026-10-17):** WebFetch: YES, subsections 1-14 and history present; '2025 Iowa Code'; 'IA Code § 614.1 (2025)'. Second citation /title-xvi/chapter-707/section-707-2/: YES 'A person commits murder in the first degree when the'. Chapter page /title-xv/chapter-614/ lists section links (614.4A → section-614-4a).

## B. Constitution

### `ia-constitution-legis` — Iowa Constitution — Codified (PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: official
- **Coverage:** Whole codified constitution in one PDF, amendments through Amendments 50 and 51 (2024). Original 1857 text: /docs/publications/ICP/1518289.pdf.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Single document; locate 'Sec. {n}.' within 'ARTICLE {roman}'.
  - Index: `https://www.legis.iowa.gov/law/statutory/constitution`
  - Navigation: Constitution page → 'Iowa Constitution - Codified' → https://www.legis.iowa.gov/docs/publications/ICP/1518288.pdf (opaque id; re-read the link each time).
- **Automation:** WebFetch ok · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - 105,512 chars: right at the fetch tool's window; WebFetch still reached Art. XII §§ 1-2.
- **Currency:** section history notes ('Amended by Amendment N (year)'); PDF last-modified — observed: "Repealed and rewritten by Amendment 51 (2024); last-modified 13 Dec 2024"
- **Official status:** Constitution page: 'The codified Iowa Constitution is an official legal publication' under Iowa's UELMA (Iowa Code ch. 2B) (https://www.legis.iowa.gov/law/statutory/constitution).
- **Hazard:** single 27-page PDF near the fetch tool's limit
- **Hazard:** opaque document id
- **Probe:** Iowa Const. art. I, § 8 → `https://www.legis.iowa.gov/docs/publications/ICP/1518288.pdf` — expect: "The right of the people to be secure in their persons, houses, papers"
- **Evidence (2026-10-17):** Script: 27 pp., 105,512 chars; art. I § 8 'Personal security — searches and seizures' present; art. I § 1A 'Added by Amendment 49 (2022)'. WebFetch: art. XII § 1 present, last body text art. XII § 2, not truncated.

### `ia-constitution-justia` — Justia — Iowa Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages; includes art. I § 1A as amended 2022.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/iowa/article-{article_roman_lower}/section-{section_lower}/`
  - Placeholders: article Roman numeral lower-case (article-i); section lower-case incl. letter (section-1a, section-8). Article pages list section titles only.
  - Index: `https://law.justia.com/constitution/iowa/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell: law.justia.com robots.txt answers with a Cloudflare challenge
  - Fetch tool only.
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version."
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Probe:** Iowa Const. art. I, § 1A → `https://law.justia.com/constitution/iowa/article-i/section-1a/` — expect: "The right of the people to keep and bear arms"
- **Evidence (2026-10-17):** WebFetch: YES 'The right of the people to keep and bear arms'; strict-scrutiny sentence and 'Added by Amendment 49 (2022)' present. Article page /article-i/ lists sections with links (section-8, section-1a), no body text.

## C. Court rules

### `ia-courtrules-legis` — Iowa Court Rules, per-chapter PDFs (legis.iowa.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency for the Iowa Supreme Court · text: **fetch-and-quote** · official: official
- **Coverage:** All chapters of the Iowa Court Rules (ch. 1 Civil Procedure, 2 Criminal Procedure, 5 Evidence, 6 Appellate Procedure, 32 Professional Conduct, ...), monthly publication; editions back to 2002.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.legis.iowa.gov/docs/ACO/CourtRulesChapter/{chapter}.pdf`
  - Placeholders: chapter = the number before the first '.' or ':' of the rule (1.421 → 1; 5.702 → 5; 6.1103 → 6; 2.24 → 2; 32:1.7 → 32). The undated URL serves the current edition: /docs/ACO/CR/LINC/chapter.{n}.pdf redirects to it, and its sha256 equals the dated 09-30-2026.chapter.{n}.pdf on the listing. Dated form for a specific edition: /docs/ACO/CR/LINC/{MM-DD-YYYY}.chapter.{n}.pdf (publication dates are on the listing). Whole set: {date}.FullCourtRules.pdf (1,271 pp.).
  - Index: `https://www.legis.iowa.gov/law/courtRules/courtRulesListings`
  - Navigation: Listing (publication date 'Iowa Court Rules - September 2026') → chapter PDF → grep 'Rule {rule} ' (body headings are 'Rule 1.421 Defenses; how raised...').
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - WebFetch read ch. 5 (78,862 chars) to the end (Rule 5.1103) but cut ch. 1 (424,571 chars) at Rule 1.308: 'Rule 1.981 NOT PRESENT'. Ch. 6 is 199,325 chars and ch. 32 406,602 chars: use fetch_doc.py grep/section or the corpus.
- **Currency:** listing heading; each PDF page header carries that page's revision month — observed: "Iowa Court Rules - September 2026; page headers 'December 2025' (ch. 6), 'December 2022' (ch. 5)"
- **Official status:** Court rules listing is headed '(Official Edition)'; Iowa Court Rules from the 5th edition are designated official under Iowa Code ch. 2B (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** fetch tool truncates the big chapters (1, 6, 32)
- **Hazard:** page-header month is the page's last revision, not the edition date
- **Hazard:** table of contents at the start of each chapter repeats every rule title: grep the body heading with its trailing text
- **Probe:** Iowa R. Evid. 5.702 → `https://www.legis.iowa.gov/docs/ACO/CourtRulesChapter/5.pdf` — expect: "A witness who is qualified as an expert by knowledge, skill, experience"
- **Evidence (2026-10-17):** Script: ch. 5 22 pp., Rule 5.702 body present; ch. 1 130 pp., 'Rule 1.421 Defenses; how raised; consolidation; waiver.' at p. 35; ch. 6 'Rule 6.1103 Application to the supreme court for further review' at p. 40; ch. 32 'Rule 32:1.7 CONFLICT OF INTEREST: CURRENT CLIENTS' at p. 20. WebFetch on dated ch. 5: YES 'A witness who is qualified as an expert by knowledge'.
- **Notes:** iowacourts.gov links its court-rules pages to this legis.iowa.gov publication; amendment orders are posted alongside the listing (e.g. 09-30-2026.CourtOrder.09_25_2026_Order_Ch_17.pdf).

## D. Administrative code

### `ia-iac-legis` — Iowa Administrative Code, per-chapter and per-rule PDFs

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: official
- **Coverage:** Current IAC (updated biweekly) and dated past editions.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.legis.iowa.gov/docs/iac/chapter/{agency}.{chapter}.pdf`
  - Placeholders: From 'Iowa Admin. Code r. 641—1.1' or '641 IAC 1.1': agency = 641, chapter = 1, rule = 1. Undated chapter URL serves the current edition (sha256 identical to the listing's dated 10-14-2026.641.1.pdf). Single rule: /docs/iac/rule/{agency}.{chapter}.{rule}.pdf (641.1.1.pdf, 2 pp.). Dated edition: /docs/iac/chapter/{MM-DD-YYYY}.{agency}.{chapter}.pdf. Whole agency: /docs/iac/agency/[{date}.]{agency}.pdf.
  - Index: `https://www.legis.iowa.gov/law/administrativeRules/chapters?agency={agency}`
  - Navigation: Agency list (/law/administrativeRules/agencies) → 'Chapters' → chapter PDF/RTF links.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - Built URLs; WebFetch not tried to save budget (same host and PDF type as the Code PDFs, which WebFetch reads).
- **Currency:** page header of each chapter PDF — observed: "IAC 6/10/26 Public Health[641] Ch 1, p.1"
- **Official status:** IAC page heading 'Iowa Administrative Code - 10/14/2026 (Official Edition)'; IAC designated official from the July 2, 2008 edition (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** 2023-2026 Red Tape Review rescinded and rewrote many chapters: old chapter numbers may now be empty stubs (701 ch. 400: 295 chars)
- **Hazard:** chapter rescission dates under Iowa Code § 17A.7 printed at the top of each chapter
- **Probe:** Iowa Admin. Code r. 641—1.1 → `https://www.legis.iowa.gov/docs/iac/chapter/641.1.pdf` — expect: "Definitions. For the purpose of these rules, the following definitions will apply"
- **Evidence (2026-10-17):** Script: 641.1.pdf 16 pp., 63,039 chars, header 'IAC 6/10/26', '641—1.1(139A) Definitions.'; rule PDF 641.1.1.pdf 2 pp. Second citation 567.61.pdf: 24 pp., 'CHAPTER 61 WATER QUALITY STANDARDS', header 'IAC 2/5/25'.

### `ia-iac-lii` — Cornell LII — Iowa Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-rule pages by agency and chapter.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/iowa/Iowa-Code-r-{agency}-{chapter}.{rule}`
  - Placeholders: 641—1.1 → Iowa-Code-r-641-1.1 (LII labels IAC rules 'Iowa Code r.'). Chapter index: /regulations/iowa/agency-{agency}/chapter-{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/iowa`
  - Navigation: agency-{agency} → chapter-{chapter} → rule links
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10 (from the MN record); /regulations allowed
  - Respect the crawl delay.
- **Currency:** HTTP Last-Modified; 'Notes' history line — observed: "last-modified Fri, 01 Aug 2025; 'ARC 8070C, IAB 6/12/24, effective 7/17/24'"
- **Official status:** Third-party mirror; no currency statement.
- **Hazard:** snapshot from Aug. 2025: misses Red Tape Review rewrites since then
- **Probe:** Iowa Admin. Code r. 641—1.1 → `https://www.law.cornell.edu/regulations/iowa/Iowa-Code-r-641-1.1` — expect: "For the purpose of these rules, the following definitions will apply"
- **Evidence (2026-10-17):** Script: 8,018 chars, body present, Notes 'ARC 8070C, IAB 6/12/24'; last-modified 01 Aug 2025. Second citation Iowa-Code-r-567-61.3: 28,937 chars. Index links agency-641 → chapter-1 → Iowa-Code-r-641-1.1.

## D. Administrative register

### `ia-iab-legis` — Iowa Administrative Bulletin (issues) and ARC documents

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Legislative Services Agency · text: **fetch-and-quote** · official: official
- **Coverage:** Biweekly issues (Wednesday); per-ARC PDFs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.legis.iowa.gov/docs/aco/bulletin/{MM-DD-YYYY}.pdf`
  - Placeholders: Issue date zero-padded MM-DD-YYYY (IAB 10/14/26 → 10-14-2026.pdf). One filing: https://www.legis.iowa.gov/docs/aco/arc/{arc}.pdf with the ARC number as printed incl. series letter (ARC 0647D → 0647D.pdf).
  - Index: `https://www.legis.iowa.gov/law/administrativeRules/bulletinSupplementListings`
  - Navigation: Listing links each issue PDF by date.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Disallow: /chambers/ only; Sitemap listed
  - Issues are huge (10/14/2026: 235 pp., 818,460 chars); prefer the per-ARC PDF.
- **Currency:** issue cover — observed: "VOLUME XLIX NUMBER 8 October 14, 2026 Pages 2489 to 2723"
- **Official status:** IAB designated official from the July 2, 2008 edition (https://www.legis.iowa.gov/law/officialAndUnofficialEditions).
- **Hazard:** issue PDFs far exceed the fetch tool's window
- **Hazard:** ARC series letter (A-D) must be kept
- **Probe:** ARC 0647D, IAB 10/14/26 → `https://www.legis.iowa.gov/docs/aco/arc/0647D.pdf` — expect: "Notice of Intended Action"
- **Evidence (2026-10-17):** Script: 0647D.pdf 2 pp., 'ARC 0647D EDUCATION DEPARTMENT[281] Notice of Intended Action'. Issue 10-14-2026.pdf: cover 'VOLUME XLIX NUMBER 8'; 09-30-2026.pdf: 423 pp.
- **Notes:** rules.iowa.gov (executive-branch rulemaking tracker, linked from legis via /leaving) serves a tracking page, not rule text; not recorded as a source.

## E. Case law

### `ia-opinions-iowacourts` — Iowa Judicial Branch — Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Case pages with PDF opinions from about Feb. 2018 (monthly archives 2018-2026 seen, e.g. Supreme Court archive/2018/3 and 2021/3); older opinions on yearly archive pages back to 1998 (Supreme Court) and 2006 (Court of Appeals) whose per-opinion links the script did not surface.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.iowacourts.gov/iowa-courts/{court_path}/case/{docket}`
  - Placeholders: court_path = supreme-court/supreme-court-opinions | court-of-appeals/court-of-appeals-court-opinions. docket as YY-NNNN with ASCII hyphen and 4-digit number (25-1183, 19-0058). The case page links 'PDF of the Opinion' at /courtcases/{internal_id}/embed/SupremeCourtOpinion or .../CourtAppealsOpinion (internal id is opaque; read it from the case page). Listing by month (plain GET): /iowa-courts/{court_path}/archive/{year}/{month}[/page/{n}], 12 per page.
  - Index: `https://www.iowacourts.gov/iowa-courts/supreme-court/supreme-court-opinions/archive/{year}/{month}`
  - Navigation: (court, docket) → case page → 'PDF of the Opinion'. (court, date) → monthly archive → case link. Current-release pages: /iowa-courts/supreme-court/supreme-court-opinions/ and /iowa-courts/court-of-appeals/court-of-appeals-court-opinions (latest filing day only, 'Filed Oct 07, 2026').
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * Crawl-delay: 30; Disallow: (empty)
  - WebFetch read the search-surfaced monthly archive /archive/2021/3 (pagination 'Page 1 of 2'), but built case pages and opinion PDFs returned PROVENANCE_REQUIRED. robots asks a 30-second crawl delay: space script calls.
- **Currency:** opinion caption — observed: "Submitted September 9, 2026—Filed October 16, 2026"
- **Official status:** Slip opinions (PDF) as filed; no reporter pagination; Iowa Reports ceased 1968, N.W.2d/N.W.3d is the reporter.
- **Hazard:** slip pagination only; no N.W. cite in the PDF
- **Hazard:** the embed URL serves the latest version: amended opinions replace the original (Donahue 'Filed March 26, 2021 Amended June 1, 2021')
- **Hazard:** a few case slugs are irregular (Banwart '16–1218' → /case/161218); fall back to the monthly archive
- **Hazard:** Court of Appeals unpublished opinions are not controlling authority (Iowa R. App. P. 6.904(2)(c))
- **Hazard:** 30-second crawl delay
- **Probe:** Davenport v. Fuller, No. 25-1183 (Iowa Oct. 16, 2026) → `https://www.iowacourts.gov/courtcases/26518/embed/SupremeCourtOpinion` — expect: "A plaintiff appeals from a district court judgment dismissing his medical malpractice claims"
- **Evidence (2026-10-17):** Script: case page /supreme-court/supreme-court-opinions/case/25-1183 links 'PDF of the Opinion' → /courtcases/26518/embed/SupremeCourtOpinion, PDF 17 pp., 'No. 25–1183 ... Filed October 16, 2026'. Second citation COA No. 24-1358 → /courtcases/27223/embed/CourtAppealsOpinion, 9 pp., 'Filed October 7, 2026'. Older: Donahue No. 18-2239 (8953) 19 pp. COA archive/2021/3 lists case/19-0058.
- **Notes:** Opinions are released on fixed filing days (Supreme Court usually Fridays, Court of Appeals Wednesdays); an 'expected list' is announced in advance at /announcements.

### `ia-cases-justia` — Justia — Iowa Supreme Court and Court of Appeals

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1859-2026; Court of Appeals 1977-2026 (year links on the court pages).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/iowa/{court}/{year}/{docket}.html`
  - Placeholders: court = supreme-court | court-of-appeals; year = filing year; docket YY-NNNN with hyphen (18-2239, 19-0058). Year listing /cases/iowa/{court}/{year}/ shows docket numbers and dates when a slug misses.
  - Index: `https://law.justia.com/cases/iowa/`
  - Navigation: court page → year listing → case
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell: law.justia.com robots.txt answers with a Cloudflare challenge
  - Fetch tool only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions; no reporter citation for the case itself.
- **Hazard:** posting lag (Supreme Court page's newest entry June 30, 2026 on 2026-10-17)
- **Hazard:** amended opinions may not be updated
- **Hazard:** shell blocked
- **Probe:** State v. Donahue, No. 18-2239 (Iowa Mar. 26, 2021) → `https://law.justia.com/cases/iowa/supreme-court/2021/18-2239.html` — expect: "In this case, defendant John Donahue appeals his"
- **Evidence (2026-10-17):** WebFetch: YES, full opinion to 'All justices concur except Christensen, C.J.'; no N.W.2d cite, no amended date. Second citation /court-of-appeals/2021/19-0058.html: YES 'Kyle Reasoner appeals following his guilty plea to carrying weapons.', 'Filed March 17, 2021'.
- **Notes:** Use for opinions before 2018, where iowacourts.gov archive pages gave no per-opinion links to the script.

## F. Subsequent history

### `ia-docket-ecourts` — Iowa Courts Online case search (appellate dockets)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Iowa Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Appellate docket entries, including further-review dispositions (reported, not probed).
- **Access:** `search-only` · format html
  - Index: `https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame`
  - Navigation: Frameset search application; not navigated.
- **Automation:** WebFetch untested · shell untested · robots: robots.txt redirects (302) to /ESAWebApp/robots.txt; fetch_doc.py check: robots permits
  - Entry page is a 90-character frameset ('This page uses frames').
- **Currency:** 
- **Official status:** Docket system.
- **Hazard:** frames / session-based search; not scriptable as tested
- **Probe:**  → `https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame`
- **Evidence (2026-10-17):** Script: 'This page uses frames, but your browser doesn't support them.' Linked as 'Find a Case' from iowacourts.gov opinion pages.

### `ia-further-review-casepage` — Iowa Judicial Branch case page (same docket at both courts)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Cases with case pages (about 2018-): the Court of Appeals case page lists the application for further review, the resistance, and, if review was granted and decided, the Supreme Court opinion.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.iowacourts.gov/iowa-courts/court-of-appeals/court-of-appeals-court-opinions/case/{docket}`
  - Placeholders: The docket number is the same at the Court of Appeals and the Supreme Court; both opinions share one internal id (/courtcases/11098/embed/CourtAppealsOpinion and .../SupremeCourtOpinion). The Supreme Court case page /supreme-court/supreme-court-opinions/case/{docket} holds the decision on further review.
  - Index: `https://www.iowacourts.gov/iowa-courts/court-of-appeals/court-of-appeals-court-opinions/`
  - Navigation: COA case page → 'Application for Further Review' document and 'PDF of the Opinion' links (Supreme Court opinion listed when review was granted).
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * Crawl-delay: 30; Disallow: (empty)
  - Denials of further review are not shown on the case page.
- **Currency:** none
- **Official status:** Court website case pages; slip opinions.
- **Hazard:** shows grants that ended in an opinion; a denial leaves only the application on the page
- **Hazard:** 30-second crawl delay
- **Probe:** Daniels v. Holtz, No. 19-1674 (Iowa Mar. 26, 2021) → `https://www.iowacourts.gov/iowa-courts/court-of-appeals/court-of-appeals-court-opinions/case/19-1674` — expect: "COURT OF APPEALS DECISION VACATED; DISTRICT COURT JUDGMENT AFFIRMED"
- **Evidence (2026-10-17):** Script: COA case page 19-1674 links 'Application for Further Review', 'Resistance to Application for Further Review', COA opinion /courtcases/11098/embed/CourtAppealsOpinion and Supreme Court opinion .../SupremeCourtOpinion ('On review from the Iowa Court of Appeals', 'COURT OF APPEALS DECISION VACATED').

### `ia-further-review-orders` — Iowa Supreme Court — Further Review Orders (latest batch)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Iowa Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Only the most recent batch of grants and denials ('Below is the further review status since our last report'); no archive and no order dates in the table.
- **Read via (in order):** **script**
- **Access:** `link-only` · format html
  - Index: `https://www.iowacourts.gov/iowa-courts/supreme-court/further-review-orders/`
  - Navigation: Tables 'Granted' and 'Denied' with Number, County, Case Name.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Crawl-delay: 30; Disallow: (empty)
- **Currency:** none (no date on the table) — observed: "further review status since our last report"
- **Official status:** Court website table.
- **Hazard:** overwritten with each batch: past denials cannot be found here
- **Hazard:** no dates
- **Probe:** Peer v. IRC II, Inc., No. 25-0461 (further review granted) → `https://www.iowacourts.gov/iowa-courts/supreme-court/further-review-orders/` — expect: "The following table contains review orders with the status of Granted."
- **Evidence (2026-10-17):** Script: 15,774 chars; Granted: 25-0461 Peer v. IRC II, Inc.; 25-0562; 25-1345. Denied list begins 24-1440 Tyson v. State.
- **Notes:** For an older 'further review denied', the free routes are the appellate docket in Iowa Courts Online (ia-docket-ecourts) or a later opinion's subsequent-history parenthetical.

### `ia-subsequent-justia` — Justia — Supreme Court decision on further review, by Court of Appeals docket

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court decisions after a grant of further review (not denials).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/iowa/supreme-court/{year}/{docket}.html`
  - Placeholders: Same docket at both courts; year = Supreme Court filing year (usually the COA year or the next).
  - Index: `https://law.justia.com/cases/iowa/supreme-court/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell: law.justia.com robots.txt answers with a Cloudflare challenge
  - Fetch tool only.
- **Currency:** none
- **Official status:** Third-party copy.
- **Hazard:** denials absent
- **Hazard:** year guess
- **Probe:** State v. Donahue, No. 18-2239 (Iowa Mar. 26, 2021) → `https://law.justia.com/cases/iowa/supreme-court/2021/18-2239.html` — expect: "In this case, defendant John Donahue appeals his"
- **Evidence (2026-10-17):** URL pattern verified for Supreme Court docket pages (18-2239, 2021 listing shows 20-0030, 20-0657); a COA-then-Supreme-Court pair was not fetched on Justia.

## Not available (do not look for these again)

- **case_law** — Public-domain / vendor-neutral citation for Iowa opinions: Opinion PDFs carry only docket and filing date (No. 25–1183, Filed October 16, 2026); no paragraph numbering or neutral cite. (2026-10-17)
- **case_law** — Free official reporter (Iowa Reports) for modern cases: Iowa Reports ceased in 1968; modern cases appear only in the West N.W. reporters; slip PDFs have no reporter pagination. (2026-10-17)
- **statutes** — Official bulk statute data (XML/JSON): 'Hyperlink Legal Downloads' (https://www.legis.iowa.gov/law/hyperlinkDownloads) offers only a Word template; per-section PDF and RTF files are the finest-grained downloads. (2026-10-17)

## Corpus candidates (maintainers)

- `ia-courtrules-legis` — Rules of Civil Procedure: 130 pp., 424,571 chars; fetch tool stops at Rule 1.308 · bulk: https://www.legis.iowa.gov/docs/ACO/CR/LINC/09-30-2026.FullCourtRules.pdf (1,271 pp.)
- `ia-courtrules-legis` — Rules of Appellate Procedure: 84 pp., 199,325 chars (twice the fetch window)
- `ia-courtrules-legis` — Rules of Professional Conduct: 89 pp., 406,602 chars
- `ia-constitution-legis` — 105,512 chars, at the fetch tool's limit

## Open questions

- Do iowacourts.gov yearly archive pages before 2018 link opinion PDFs at all (the script's link list showed none on opinions-archive-2013)? Justia is the fallback until checked.
- Is there a free route to historical further-review denials other than the Iowa Courts Online docket (frameset, not probed)?
- Court of Appeals published vs. unpublished status: the 'Published Cases' page returned only navigation links to the script; not resolved.
- Rules of Criminal Procedure chapter 2 size and fetch-tool reach not checked.

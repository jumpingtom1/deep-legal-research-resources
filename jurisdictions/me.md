# Maine (ME) — free legal sources

_Generated from `data/me.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: legislature.maine.gov serves one static HTML page per section at a URL built straight from the citation (title + section, letters and hyphens kept), plus per-section, per-chapter and per-title PDF/Word files; the text is expressly unofficial (the certified text is the M.R.S.A.), and Justia 2025 is the tier-2 fallback. Session laws: the Law and Legislative Digital Library serves one PDF per chapter at a constructible URL. Constitution: the Revisor's full-text PDF and HTML (through CR 2023, cc. 1-2). Court rules: full-set PDFs on courts.maine.gov (civil 640K chars, criminal 275K) need the script or corpus. Case law: Law Court opinions 2017-present as PDFs keyed by the public-domain cite (2024 ME 84 → 24me084.pdf); 1997-2016 only on Justia; Maine Reports 1-161 (1820-1965, official pagination) as scanned volumes on lldc. The Code of Maine Rules and weekly rulemaking notices on www.maine.gov are bot-walled; Cornell LII's CMR is the only readable admin-code route.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Maine Supreme Judicial Court (sitting as the Law Court) | `me (unverified)` | Me. | A.3d, A.2d, A., Me. | 2024 ME 84 (year ME number; pinpoint by paragraph, e.g. 2024 ME 84, ¶ 12); used for opinions from 1997 on |
| Maine Superior Court (incl. Business and Consumer Docket) | `mesuperct (unverified)` | Me. Super. Ct. | A.3d, A.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Maine Revised Statutes | `14 M.R.S. § 752`; `17-A M.R.S. § 207(1)(A) (2024)`; `11 M.R.S.A. § 2-314`; `5 MRSA §4572`; `14 M.R.S. § 752-C`; `Me. Rev. Stat. Ann. tit. 14, § 752`; `Me. Stat. tit. 39-A, § 201`; `14 M.R.S. §§ 751-753`; `Title 17-A, section 207 of the Maine Revised Statutes`; `section 752 of Title 14 of the Maine Revised Statutes` | `me-statutes-legislature` → `me-statutes-justia` |
| Maine Revised Statutes (bare 'Title N, section N' / 'section N of Title N') *(only once this jurisdiction is known)* | `Title 14, section 752`; `Title 22, section 4002, subsection 6`; `section 4572 of Title 5` | `me-statutes-legislature` → `me-statutes-justia` |
| Laws of Maine (session laws, Bluebook / P. & S.L. forms) | `2023 Me. Laws ch. 405`; `2023 Me. Legis. Serv. ch. 405`; `P. & S.L. 2023, ch. 5`; `2023 Me. Laws, c. 405` | `me-session-laws-lldc` |
| Laws of Maine (bare P.L. / Resolves / CR forms) *(only once this jurisdiction is known)* | `P.L. 2023, ch. 405`; `P.L. 2021, ch. 647, § B-19`; `Resolve 2023, ch. 86`; `CR 2023, c. 1` | `me-session-laws-lldc` |
| Maine Constitution | `Me. Const. art. I, § 6-A`; `Me. Const. art. IV, pt. 3, § 1`; `Article I, section 6-A of the Maine Constitution`; `Constitution of Maine, Article X, Section 6` | `me-constitution-revisor` → `me-constitution-justia` |
| Maine Rules of Civil Procedure | `Me. R. Civ. P. 56(c)`; `Rule 12(b)(6) of the Maine Rules of Civil Procedure`; `Maine Rule of Civil Procedure 80B` | `me-rules-civil` |
| Maine Rules of Civil Procedure (M.R. Civ. P., shared with Montana's 'M. R. Civ. P.') *(only once this jurisdiction is known)* | `M.R. Civ. P. 12(b)(6)`; `M.R. Civ. P. 80B(a)` | `me-rules-civil` |
| Maine Rules of Unified Criminal Procedure | `M.R.U. Crim. P. 11`; `Me. R. Unified Crim. P. 16(a)`; `Rule 11 of the Maine Rules of Unified Criminal Procedure` | `me-rules-criminal` |
| Maine Rules of Evidence | `Me. R. Evid. 401`; `Maine Rule of Evidence 803(4)`; `Rule 404(b) of the Maine Rules of Evidence` | `me-rules-evidence` |
| Maine Rules of Evidence (M.R. Evid., shared with Montana) *(only once this jurisdiction is known)* | `M.R. Evid. 803(2)` | `me-rules-evidence` |
| Maine Rules of Appellate Procedure | `Me. R. App. P. 2B(c)(1)`; `Rule 2A of the Maine Rules of Appellate Procedure` | `me-rules-appellate` |
| Maine Rules of Appellate Procedure (M.R. App. P., shared with Montana) *(only once this jurisdiction is known)* | `M.R. App. P. 12(a)(2)` | `me-rules-appellate` |
| Maine Rules of Professional Conduct | `Me. R. Prof. Conduct 1.7`; `Rule 1.7 of the Maine Rules of Professional Conduct` | `me-rules-professional-conduct` |
| Maine Rules of Professional Conduct (M.R. Prof. Conduct, shared with Montana) *(only once this jurisdiction is known)* | `M.R. Prof. Conduct 1.15(b)` | `me-rules-professional-conduct` |
| Code of Maine Rules | `10-144 C.M.R. ch. 101`; `26-239 C.M.R. ch. 2, § 1`; `10-144-101 Me. Code R. § 2`; `Code Me. R. tit. 26-239, ch. 2` | `me-cmr-lii` → `me-cmr-sos` |
| Maine public-domain citation (YYYY ME N) | `2024 ME 84`; `State v. Sheppard, 2024 ME 84, ¶ 12`; `Dalton v. Quinn, 2010 ME 120`; `Snow v. Bernstein, Shur, Sawyer & Nelson, P.A., 2017 ME 239, ¶¶ 10-12` | `me-opinions-courts` → `me-cases-justia` |
| Atlantic Reporter with Maine parenthetical | `State v. Croteau, 184 A.2d 683 (Me. 1962)`; `123 A.3d 456 (Me. 2015)`; `2019 WL 1234567 (Me. Super. Ct. Mar. 1, 2019)` | `me-cases-justia` → `me-opinions-courts` |
| Maine Reports (official reporter, vols. 1-161, 1820-1965) | `State v. Croteau, 158 Me. 360`; `161 Me. 28`; `150 Me. 18` | `me-maine-reports-lldc` → `me-cases-justia` |
| Law Court docket numbers (county-coded) *(only once this jurisdiction is known)* | `And-23-68`; `Cum-17-54`; `Docket No. BCD-24-112` | `me-opinions-courts` → `me-subsequent-history-lawcourt` |
| Law Court memorandum of decision *(only once this jurisdiction is known)* | `Mem 26-139`; `Mem-23-45`; `Mem. Dec. 24-12` | `me-subsequent-history-lawcourt` |

Regexes (case-insensitive):

- Maine Revised Statutes: `(?:(?P<title>\d{1,2}(?:-[A-D])?)\s+M\.?\s?R\.?\s?S\.?(?:\s?A\.?)?|Me\.\s*(?:Rev\.\s*)?Stat\.(?:\s*Ann\.)?\s*tit\.\s*(?P<title2>\d{1,2}(?:-[A-D])?),?)\s*(?:§(?!§)\s*(?P<section>\d+(?:-\d+)?(?:-[A-Z]{1,2})?)(?![\d-])|§§\s*(?P<section_first>\d+(?:-[A-Z]{1,2})?))|Title\s+(?P<title3>\d{1,2}(?:-[A-D])?),?\s+(?:section|§)\s*(?P<section3>\d+(?:-\d+)?(?:-[A-Z]{1,2})?)(?:,\s*sub(?:section|§)\s*\w+)*\s+of\s+the\s+Maine\s+Revised\s+Statutes|(?:section|§)\s*(?P<section4>\d+(?:-\d+)?(?:-[A-Z]{1,2})?)(?:\([a-z0-9]+\))*\s+of\s+Title\s+(?P<title4>\d{1,2}(?:-[A-D])?)\s+of\s+the\s+Maine\s+Revised\s+Statutes`
- Maine Revised Statutes (bare 'Title N, section N' / 'section N of Title N'): `Title\s+(?P<title>\d{1,2}(?:-[A-D])?),\s+section\s+(?P<section>\d+(?:-\d+)?(?:-[A-Z]{1,2})?)|(?:section|§)\s*(?P<section2>\d+(?:-\d+)?(?:-[A-Z]{1,2})?)(?:\([a-z0-9]+\))*\s+of\s+Title\s+(?P<title2>\d{1,2}(?:-[A-D])?)(?!\d)`
- Laws of Maine (session laws, Bluebook / P. & S.L. forms): `(?P<year>(?:18|19|20)\d\d)\s+Me\.\s*(?:Laws|Legis\.\s*Serv\.),?\s*(?:ch?\.|chapter)\s*(?P<chapter>\d+)|P\.\s*&\s*S\.\s*L\.\s*(?P<year2>(?:18|19|20)\d\d),\s*(?:ch?\.|chapter)\s*(?P<chapter2>\d+)`
- Laws of Maine (bare P.L. / Resolves / CR forms): `(?:P\.\s*L\.|Resolves?|CR|Const\.\s*Res\.)\s*(?P<year>(?:18|19|20)\d\d),\s*(?:ch?\.|chapter)\s*(?P<chapter>\d+)`
- Maine Constitution: `Me\.\s*Const\.\s*art\.\s*(?P<article>[IVX]+),?\s*(?:pt\.\s*(?P<part>\d+|[A-Za-z]+),?\s*)?§+\s*(?P<section>\d+(?:-[A-Z])?)|Article\s+(?P<article2>[IVX]+),?\s+(?:Part\s+(?P<part2>\w+),?\s+)?section\s+(?P<section2>\d+(?:-[A-Z])?)\s+of\s+the\s+(?:Maine\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Maine)|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Maine,\s+Article\s+(?P<article3>[IVX]+),\s+(?:Part\s+(?P<part3>\w+),\s+)?Section\s+(?P<section3>\d+(?:-[A-Z])?)`
- Maine Rules of Civil Procedure: `Me\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d+[A-Z]?)|Rule\s+(?P<rule2>\d+[A-Z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Maine\s+Rules\s+of\s+Civil\s+Procedure|Maine\s+Rules?\s+of\s+Civil\s+Procedure\s+(?P<rule3>\d+[A-Z]?)`
- Maine Rules of Civil Procedure (M.R. Civ. P., shared with Montana's 'M. R. Civ. P.'): `M\.\s?R\.\s?Civ\.\s?P\.\s*(?P<rule>\d+[A-Z]?)`
- Maine Rules of Unified Criminal Procedure: `M\.\s?R\.\s?U\.\s?Crim\.\s?P\.\s*(?P<rule>\d+[A-Z]?)|Me\.\s*R\.\s*Unified\s*Crim\.\s*P\.\s*(?P<rule2>\d+[A-Z]?)|Rule\s+(?P<rule3>\d+[A-Z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Maine\s+Rules\s+of\s+Unified\s+Criminal\s+Procedure`
- Maine Rules of Evidence: `Me\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Maine\s+Rules?\s+of\s+Evidence\s+(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Maine\s+Rules\s+of\s+Evidence`
- Maine Rules of Evidence (M.R. Evid., shared with Montana): `M\.\s?R\.\s?Evid\.\s*(?P<rule>\d{3,4})`
- Maine Rules of Appellate Procedure: `Me\.\s*R\.\s*App\.\s*P\.\s*(?P<rule>\d+[A-Z]?)|Rule\s+(?P<rule2>\d+[A-Z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Maine\s+Rules\s+of\s+Appellate\s+Procedure`
- Maine Rules of Appellate Procedure (M.R. App. P., shared with Montana): `M\.\s?R\.\s?App\.\s?P\.\s*(?P<rule>\d+[A-Z]?)`
- Maine Rules of Professional Conduct: `Me\.\s*R\.\s*Prof(?:'l|\.)?\s*Conduct\s*(?P<rule>\d\.\d+)|Rule\s+(?P<rule2>\d\.\d+)(?:\([a-z0-9]+\))*\s+of\s+the\s+Maine\s+Rules\s+of\s+Professional\s+Conduct`
- Maine Rules of Professional Conduct (M.R. Prof. Conduct, shared with Montana): `M\.\s?R\.\s?Prof\.\s*Cond(?:uct|\.)\s*(?P<rule>\d\.\d+)`
- Code of Maine Rules: `(?P<agency>\d{2})-(?P<unit>\d{3})\s*C\.?\s?M\.?\s?R\.?\s*(?:ch\.?|chapter)\s*(?P<chapter>\d+[A-Z]?)(?:,\s*§\s*(?P<section>\d+))?|(?P<agency2>\d{2})-(?P<unit2>\d{3})-(?P<chapter2>\d+[A-Z]?)\s+Me\.\s*Code\s*R\.(?:\s*§\s*(?P<section2>\d+))?|Code\s+Me\.\s*R\.\s*(?:tit\.\s*)?(?P<agency3>\d{2})-(?P<unit3>\d{3}),?\s*(?:ch\.?|chapter)\s*(?P<chapter3>\d+[A-Z]?)`
- Maine public-domain citation (YYYY ME N): `(?P<year>(?:199[7-9]|20\d\d))\s+ME\s+(?P<number>\d{1,3})(?!\d)`
- Atlantic Reporter with Maine parenthetical: `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Me\.(?:\s*Super\.(?:\s*Ct\.)?|\s*Bus\.\s*&\s*Consumer\s*Ct\.)?)\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>\d{4})\)|(?P<wlyear>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Me\.`
- Maine Reports (official reporter, vols. 1-161, 1820-1965): `(?P<volume>\d{1,3})\s+Me\.\s+(?P<page>\d{1,4})(?!\d)`
- Law Court docket numbers (county-coded): `(?P<county>And|Aro|Cum|Fra|Han|Ken|Kno|Lin|Oxf|Pen|Pis|Sag|Som|Wal|Was|Yor|BCD|WCB|SRP)-(?P<yy>\d{2})-(?P<number>\d{1,4})(?!\d)`
- Law Court memorandum of decision: `Mem(?:\.\s*Dec\.)?[-\s]?(?P<yy>\d{2})-(?P<number>\d{1,3})(?!\d)`

Short forms → URL key:

P.L. → `PL`; Pub. L. → `PL`; P. & S.L. → `PS`; Priv. & Spec. L. → `PS`; CR → `CR`; Const. Res. → `CR`; Resolve → `RS`; Resolves → `RS`; IB → `IB`

Maine style (M.R. App. P. and the Law Court's opinions) cites statutes as '14 M.R.S. § 752 (2024)' (M.R.S. replaced M.R.S.A. in 2009; the year names the M.R.S.A. volume/pamphlet). Bluebook: 'Me. Rev. Stat. Ann. tit. 14, § 752' (21st ed. 'Me. Stat. tit. 14, § 752'). Statute titles carry letter suffixes (17-A, 18-C, 39-A) and sections carry letter suffixes (752-C, 4572-A, 1711-C) or UCC-style hyphenation in a few titles (11 M.R.S. § 2-314, § 1-1201; 18-C § 1-201): the URL keeps them verbatim. A '§§ 751-753' range is a span, not a hyphenated section: the regex refuses it and captures only the first section. Session laws: Maine cites 'P.L. 2023, ch. 405' with the first year of the Legislature (chapters of the second regular session continue the same series and keep that year: P.L. 2023, c. 679 was enacted in 2024); private and special laws 'P. & S.L.', resolves 'Resolve 2023, ch. 86', constitutional resolutions 'CR 2023, c. 1'. Bare 'P.L. YYYY, c. N' is also New Jersey's and Pennsylvania's form, so it routes here only with Maine context. Constitution: Article IV is in Parts (pt. 1-3; Maine text says 'Part First'); Article I is the Declaration of Rights (bare 'Declaration of Rights' is also MA, MD, NH: do not route on it). Court rules: Maine abbreviates 'M.R. Civ. P.', 'M.R. Evid.', 'M.R. App. P.', 'M.R.U. Crim. P.' (unified rules, since 2015; the older 'M.R. Crim. P.' applied before), 'M.R. Prof. Conduct'; Montana uses 'M. R. Civ. P.' / 'M. R. Evid.' / 'M. R. App. P.' so the bare M.R. forms are context_required and the 'Me. R.' and prose forms are distinctive. Montana's own M. R. patterns (data/mt.json) are not context_required and will claim Maine's M.R. examples: that is a conflict to fix in the Montana record. Case law: public-domain citation 'YYYY ME N' (since 1997), pinpoint '¶ N'; reported opinions also in A.2d/A.3d, which the court calls the permanent official version (since 1966). Maine Reports (Me.) ran to vol. 161 (1965). Memoranda of decision are cited 'Mem 26-139' (Mem-YY-N) and are not precedential (M.R. App. P. 12(c)). Law Court dockets are county-coded: 'And-23-68' (Androscoggin), 'Cum-17-54'; BCD = Business and Consumer Docket, WCB = Workers' Compensation Board appeals. Trial-court decisions are cited by WL/LEXIS ('2019 WL ... (Me. Super. Ct. ...)', 'Me. Super. LEXIS', 'Me. Bus. & Consumer LEXIS') plus docket (e.g. 'CV-2019-123', 'BCD-CV-2019-45'); a WL number cannot be resolved to a free URL. CourtListener ids are from memory and unverified. Bare prose 'section N of Title T' is generic (Delaware and others use it) and routes here only with Maine context; with 'of the Maine Revised Statutes' it is distinctive.

## A. Statutes / code

### `me-session-laws-lldc` — Laws of Maine — per-chapter PDFs (Law and Legislative Digital Library)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine State Law and Legislative Reference Library · text: **fetch-and-quote** · official: unknown
- **Coverage:** Directory /Open/Laws/{year}/ per Legislature (odd years, e.g. 2021, 2023, 2025) holding one PDF per chapter of public laws (PL), private and special laws (PS), resolves (RS), constitutional resolutions (CR) and initiated bills (IB); 2023 directory has 922 files, PL c. 1-684. Older years and bound volumes also present; printed-volume PDFs for the 124th-125th Legislatures sit on legislature.maine.gov/ros/LOM/.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://lldc.mainelegislature.org/Open/Laws/{year}/{year}_{type}_c{chapter:03d}.pdf`
  - Placeholders: year = the year in the citation ('P.L. 2023, c. 679' → 2023 even though enacted in 2024); type = PL | PS | CR | IB (others: list the directory); chapter zero-padded to 3 digits (c001, c405). The PDF reprints the printed Laws page(s) holding the chapter, so it can begin or end with neighbouring chapters and is laid out in two columns. 'CHAPTER N' also occurs in cross-references ('Title 22, chapter 405'): take the upper-case 'CHAPTER N' heading that is followed by the chapter's 'H.P./S.P. … - L.D. …' line, not the first bare match.
  - Index: `https://lldc.mainelegislature.org/Open/Laws/`
  - Navigation: IIS directory listing → year folder → file list
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - WebFetch not tried (built URL; quota). Large chapters run to 350K characters (2023_PL_c679.pdf, 54 pp.), beyond a WebFetch window.
- **Currency:** none stated; directory shows 2025 as the newest Legislature folder
- **Official status:** Cover sheet: provided by the Law and Legislative Digital Library, 'Reproduced from electronic originals (may include minor formatting differences from printed original)'; no certification statement.
- **Hazard:** two-column printed layout: extracted text interleaves columns
- **Hazard:** PDF may include parts of adjacent chapters
- **Hazard:** long chapters exceed WebFetch window
- **Hazard:** bare 'CHAPTER N' greps hit cross-references; anchor on the heading with its H.P./S.P. - L.D. line
- **Probe:** P.L. 2023, ch. 405 → `https://lldc.mainelegislature.org/Open/Laws/2023/2023_PL_c405.pdf` — expect: "CHAPTER 405"
- **Evidence (2026-10-17):** fetch_doc: 2023_PL_c405.pdf 27 pp., 174,408 chars, 'CHAPTER 405' at p. 3; 2023_PL_c679.pdf 54 pp. 'CHAPTER 679' (2024 enactment filed under 2023); 2025_PL_c001.pdf 3 pp. Cover 'LAWS OF THE STATE OF MAINE'. | Independent check 2026-10-17: fetch_doc grep: 2023_PL_c405.pdf 27 pp., 'CHAPTER 405' p. 3; second citation P. & S.L. 2021, ch. 5 ok
- **Notes:** The Revisor's Laws of Maine app (https://legislature.maine.gov/ros/LawsOfMaine/#Law) is JavaScript-only; its JSON endpoints (breeze/Law/getLegislatures, getSessions, getLawTypes, getLawGroup) answer by GET but returned only a handful of chapters per session (131st 1R: public laws 1-20; c. 405 → []), so they are not a complete index.

### `me-statutes-legislature` — Maine Revised Statutes (Office of the Revisor of Statutes)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Legislature, Office of the Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles of the Maine Revised Statutes (Titles 1-39-A incl. lettered titles 7-A … 39-A); one HTML page per section, plus PDF and Word per section, chapter and title.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://legislature.maine.gov/statutes/{title}/title{title}sec{section}.html`
  - Placeholders: title verbatim incl. letter suffix in upper case (14, 17-A, 39-A); section verbatim incl. hyphen and letter suffix in upper case (752, 752-C, 2-314 for 11 M.R.S. § 2-314, 4572-A). Subsections are on the section page (no anchors needed). A non-existent section returns HTTP 404 (title14sec9999.html), never a soft page. Same stem with .pdf or .docx gives the section PDF / Word file. Chapter page: /statutes/{title}/title{title}ch{chapter}sec0.html (section links, no text); chapter PDF /statutes/{title}/title{title}ch{chapter}.pdf; title TOC /statutes/{title}/title{title}ch0sec0.html; whole title /statutes/{title}/title{title}.pdf (and .docx).
  - Index: `https://legislature.maine.gov/statutes/`
  - Navigation: Not needed for a cited section. For browsing: list of titles → title TOC (title{T}ch0sec0.html), which DOES show section ranges per chapter ('Chapter 205: LIMITATION OF ACTIONS §751 - §871') → chapter page (section links only) → section page.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow only /bills/default_ps.asp, /bills/search_ps.asp, /LawMakerWeb (and /legis/ variants); /statutes allowed
  - WebFetch reads a section page in full when the URL was reached from a fetched page (statutes index → title TOC → chapter page → section). A section URL typed from the pattern hit a permission prompt that timed out (gated) on 2026-10-17; use fetch_doc.py for built URLs. Section pages are small (2-13K chars); no truncation. The independent check fetched a built section URL by WebFetch without a prompt: gating is intermittent.
- **Currency:** Statutes home page (https://legislature.maine.gov/statutes/) and the footer of every section/chapter/title PDF; section HTML shows only 'Data for this page extracted on' with a timestamp — observed: "reflects changes made through the Second Regular Session of the 132nd Maine Legislature, is current through October 1, 2026"
- **Official status:** Per-section PDF footer (e.g. https://legislature.maine.gov/statutes/14/title14sec752.pdf): a version 'not been officially certified by the Secretary of State'; refer to the Maine Revised Statutes Annotated for certified text. The State claims copyright in its codified statutes and asks republishers to carry a disclaimer.
- **Hazard:** explicitly not the certified text (certified = M.R.S.A., West)
- **Hazard:** built URLs may need per-URL WebFetch approval; script route reads them
- **Hazard:** lettered titles and sections must keep upper-case letters (17-A, 752-C)
- **Hazard:** repealed/renumbered titles (13, 18-A, 19, 20) still listed beside their successors (13-C, 18-C, 19-A, 20-A)
- **Probe:** 14 M.R.S. § 752 → `https://legislature.maine.gov/statutes/14/title14sec752.html` — expect: "All civil actions shall be commenced within 6 years after the cause of action accrues"
- **Evidence (2026-10-17):** fetch_doc verify: quote VERIFIED on title14sec752.html (2,212 chars); 17-A M.R.S. § 207 'A person is guilty of assault if' VERIFIED on /statutes/17-A/title17-Asec207.html; also 200 for title11sec2-314.html, 39-A/title39-Asec201.html, title14sec752-C.html; title14sec9999.html → 404. WebFetch (reached via chapter page): YES, 'All civil actions shall be commenced within 6 years after', not truncated. | Independent check 2026-10-17: fetch_doc + WebFetch: 'All civil actions shall be commenced within 6 years after'; not truncated; second citation 22 M.R.S. § 4002; 18-C M.R.S. § 1-201 ok
- **Notes:** The Laws of Maine 'Information' pages (ros/LawsOfMaine/#Info) are a JavaScript app; the disclaimer is reproduced in every PDF footer instead.

### `me-statutes-justia` — Justia — Maine Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Maine Revised Statutes; unversioned URLs serve the 2025 edition (latest listed on https://law.justia.com/codes/maine/).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/maine/title-{title_lower}/[subtitle-{n}/][part-{n}/]chapter-{chapter}/[subchapter-{n}/]section-{section_lower}/`
  - Placeholders: Use only the canonical URL with every hierarchy segment the title has (subtitle, part, chapter, subchapter), read from Justia's own links: e.g. 22 M.R.S. § 4002 → /title-22/subtitle-3/part-3/chapter-1071/subchapter-1/section-4002/ (2025 edition, verified 2026-10-17); 17-A M.R.S. § 207 → /title-17-a/part-2/chapter-9/section-207/. A shortened URL that omits segments can resolve to an OLD edition (/title-22/chapter-1071/section-4002/ served '2013 Maine Revised Statutes'), so never build it. title lower-case with hyphen (title-17-a); section lower-case verbatim (section-752-c).
  - Index: `https://law.justia.com/codes/maine/`
  - Navigation: title page (/codes/maine/title-{t}/) → subtitle → part → chapter → subchapter → section link; each page shows the edition heading. Before quoting, confirm the page heading reads '2025 Maine Revised Statutes' (the latest edition on /codes/maine/); any other year = stale edition, do not use.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a bot check
  - fetch_doc.py check REFUSED ('answers robots.txt with a bot check'); WebFetch works.
- **Currency:** page heading / breadcrumb — observed: "2025 Maine Revised Statutes"
- **Official status:** Justia pages carry 'may not be the most recent version' and no-warranty disclaimers.
- **Hazard:** edition lags the official site by up to a year
- **Hazard:** shell blocked (bot check)
- **Hazard:** chapter must be known first
- **Hazard:** STALE EDITION: URLs missing hierarchy segments can serve an old edition (2013 for 22 M.R.S. § 4002); detect by the page heading '<year> Maine Revised Statutes' and reject anything but the latest year
- **Hazard:** second citation 22 M.R.S. § 4002 failed in the independent check via the shortened URL (2013 edition served); fixed by requiring the full canonical path
- **Probe:** 14 M.R.S. § 752 → `https://law.justia.com/codes/maine/title-14/part-2/chapter-205/subchapter-1/section-752/` — expect: "All civil actions shall be commenced within 6 years after"
- **Evidence (2026-10-17):** WebFetch: YES, body 'All civil actions shall be commenced within 6 years after', '2025 Maine Revised Statutes'. Second: /title-17-a/chapter-9/section-207/ YES 'A person is guilty of assault if: A. The person'; canonical URL reported with /part-2/. | Independent check 2026-10-17: WebFetch: YES 'All civil actions shall be commenced within 6 years after', '2025 Maine Revised Statutes' | Fix 2026-10-17: canonical /title-22/subtitle-3/part-3/chapter-1071/subchapter-1/section-4002/ reached by following Justia links (title-22 → subtitle-3 → part-3 → chapter-1071 → subchapter-1), WebFetch YES 'As used in this chapter, unless the context indicates otherwise', '2025 Maine Revised Statutes'
- **Notes:** Earlier note that segment-less URLs serve 2025 was wrong for Title 22. Probe URL (Part 2, Subchapter 1) re-fetched 2026-10-17: YES, '2025 Maine Revised Statutes'.

## B. Constitution

### `me-constitution-revisor` — Constitution of the State of Maine (Revisor of Statutes, PDF and HTML)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Legislature, Office of the Revisor of Statutes · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution, 2023 arrangement, 'Includes CR 2023, c. 1 and CR 2023, c. 2'. PDF 50 pp. / 134,452 chars; HTML 177,724 chars.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://legislature.maine.gov/doc/10674`
  - Placeholders: Single document; locate the article/section by heading ('Section 6-A.'). The Revisor page https://legislature.maine.gov/const/ redirects to the JavaScript app ros/LawsOfMaine/#Const, whose view template https://legislature.maine.gov/ros/LawsOfMaine/App/views/constitution.html is the full text in static HTML and links the PDF (doc/10674) as 'Download PDF file'. Article IV's Parts are spelled out in the text ('Part First', 'Part Second', 'Part Third'): grep 'Part Third', not 'pt. 3' or 'Part 3'.
  - Index: `https://legislature.maine.gov/ros/maine-constitution-statutes-and-law/9574`
  - Navigation: Revisor page → 'Maine Constitution' (JS app) → 'Download PDF file' = /doc/10674
- **Automation:** WebFetch untested · shell ok · robots: allowed (legislature.maine.gov disallows only bill-search and LawMakerWeb paths)
  - Both documents exceed 100K characters: WebFetch would stop around Article IV/V. Use fetch_doc.py grep/section.
- **Currency:** heading of the PDF / HTML text — observed: "(Includes CR 2023, c. 1 and CR 2023, c. 2)"
- **Official status:** Text headed as arranged by the Chief Justice and approved by the Legislature (Resolve 2023, chapter 86, under Me. Const. art. X, § 6); no certification or disclaimer on the page.
- **Hazard:** longer than a WebFetch window
- **Hazard:** HTML template last modified Feb. 2024: amendments ratified after CR 2023, c. 2 may be missing — check lldc MeConst_2024_Amd.pdf
- **Hazard:** /const/ is a JavaScript app (empty shell)
- **Probe:** Me. Const. art. I, § 6-A → `https://legislature.maine.gov/doc/10674` — expect: "No person shall be deprived of life, liberty or property without due process of law"
- **Evidence (2026-10-17):** fetch_doc verify: § 6-A quote VERIFIED p. 2 of doc/10674 (PDF, 50 pp.) and in App/views/constitution.html; second citation art. I, § 5 'The people shall be secure in their persons, houses, papers and possessions' VERIFIED in both. | Independent check 2026-10-17: fetch_doc grep doc/10674: 50 pp.; § 6-A 'No person shall be deprived of life' p. 2; second citation Me. Const. art. IV, pt. 3, § 1 ok
- **Notes:** Historical versions (1820-2024) as scanned PDFs at https://lldc.mainelegislature.org/Open/Const/Versions/ (MeConst_2024_Amd.pdf, 75 pp., OCR text).

### `me-constitution-justia` — Justia — Maine Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** One page per article (consar1.html … consar10.html).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/maine/consar{article_arabic}.html`
  - Placeholders: article as Arabic number: art. I → consar1.html, art. VI → consar6.html. EXCEPTION Article IV, which has Parts: Part n → consar4{n}.html (consar41, consar42, consar43); consar4.html errors. Confirm from the index links.
  - Index: `https://law.justia.com/constitution/maine`
  - Navigation: index lists article links only (no text)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check on robots.txt)
- **Currency:** none (disclaimer only) — observed: "This Constitution may not be the most recent version."
- **Official status:** Page says 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Hazard:** Article IV has no consar4.html; use consar41-43 for Parts First-Third
- **Probe:** Me. Const. art. I, § 6-A → `https://law.justia.com/constitution/maine/consar1.html` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-17):** WebFetch: YES § 6-A 'No person shall be deprived of life, liberty or property'; § 1 'All people are born equally free and independent'; Article I complete through § 24, not truncated. Index page: NOT PRESENT (links only). | Independent check 2026-10-17: WebFetch consar1: YES § 6-A text; 'This Constitution may not be the most recent version.' | Fix 2026-10-17: verifier read consar43.html OK ('The Legislature shall convene on the first Wednesday of December')

## C. Court rules

### `me-rules-appellate` — Maine Rules of Appellate Procedure (rules only, PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Supreme Judicial Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** 68 pp., 139,884 chars.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.maine.gov/rules/text/mr_app_p_only_2024-11-01.pdf`
  - Placeholders: Dated file name; re-read the rules index.
  - Index: `https://www.courts.maine.gov/rules/index.html`
  - Navigation: rules index → Appellate 'Rules only--no advisory notes'
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - 140K characters: beyond one WebFetch window.
- **Currency:** first line of the PDF — observed: "Last reviewed and edited September 30, 2024 Includes amendments effective November 1, 2024"
- **Official status:** Published on the Judicial Branch rules page.
- **Hazard:** beyond WebFetch window
- **Hazard:** 2025 Me. Rules 02 amendment order may postdate this compilation
- **Hazard:** rule headings appear first in the table of contents (pp. 1-8): grep the body phrase, or take the last / non-TOC match of a heading
- **Probe:** M.R. App. P. 12 → `https://www.courts.maine.gov/rules/text/mr_app_p_only_2024-11-01.pdf` — expect: "The argument shall contain the contentions of the appellant with respect to the issues presented"
- **Evidence (2026-10-17):** fetch_doc grep: TOC and body (briefs rule text p. 32) present; 68 pp.; currency line on p. 1. | Independent check 2026-10-17: fetch_doc: 68 pp.; currency line matches; Rule 12 heading p. 2 (TOC) and p. 47 body; second citation M.R. App. P. 2A ok

### `me-rules-civil` — Maine Rules of Civil Procedure (rules only, PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Supreme Judicial Court / Maine Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set without advisory notes, 286 pp., 639,810 chars. The rules page also links per-rule PDFs with advisory notes (rules-civil.html → /rules/text/MRCivPPlus/…).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.maine.gov/rules/text/mr_civ_p_only_2026-06-01.pdf`
  - Placeholders: File name carries the amendment date and changes on every amendment (two versions listed on 2026-10-17: 2026-01-23 and 2026-06-01). Re-read the rules index. When the index lists two dated 'Rules only' links, take the later date in the file name.
  - Index: `https://www.courts.maine.gov/rules/index.html`
  - Navigation: rules index → 'Procedural rules' → Civil 'Rules only--no advisory notes'; per-rule annotated PDFs on https://www.courts.maine.gov/rules/rules-civil.html
- **Automation:** WebFetch gated · shell ok · robots: none (404 on www.courts.maine.gov and courts.maine.gov)
  - WebFetch permission prompt for this PDF timed out (gated). At 640K characters the PDF far exceeds a WebFetch window anyway: use fetch_doc.py or the corpus.
- **Currency:** first line of the PDF — observed: "Last reviewed and edited May 14, 2026 Includes amendments effective June 1, 2026"
- **Official status:** Published by the Judicial Branch on its rules page; no official/unofficial statement in the PDF.
- **Hazard:** dated file name changes with each amendment
- **Hazard:** far beyond WebFetch window
- **Hazard:** the index lists more than one dated version at once
- **Hazard:** rule headings appear first in the table of contents (pp. 1-8): grep the body phrase, or take the last / non-TOC match of a heading
- **Probe:** M.R. Civ. P. 12(b) → `https://www.courts.maine.gov/rules/text/mr_civ_p_only_2026-06-01.pdf` — expect: "Every defense, in law or fact, to a claim for relief in any pleading"
- **Evidence (2026-10-17):** fetch_doc grep: Rule 12(b) body at p. 46 ('Every defense, in law or fact, to a claim for relief'); TOC lists Rule 56 SUMMARY JUDGMENT; 286 pp. | Independent check 2026-10-17: fetch_doc verify: Rule 12(b) quote p. 46; 'Last reviewed and edited May 14, 2026'; second citation Me. R. Civ. P. 56 ok

### `me-rules-criminal` — Maine Rules of Unified Criminal Procedure (rules only, PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Supreme Judicial Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** 128 pp., 275,427 chars.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.maine.gov/rules/text/mru_crim_p_only_2026-10-01.pdf`
  - Placeholders: Dated file name; re-read the rules index. Annotated version: mru_crim_p_plus_2026-10-01.pdf.
  - Index: `https://www.courts.maine.gov/rules/index.html`
  - Navigation: rules index → Unified Criminal 'Rules only--no advisory notes'
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Beyond a WebFetch window (275K chars).
- **Currency:** first line of the PDF — observed: "Last reviewed and edited September 24, 2026 Including amendments effective October 1, 2026"
- **Official status:** Published on the Judicial Branch rules page.
- **Hazard:** dated file name
- **Hazard:** beyond WebFetch window
- **Hazard:** rule headings appear first in the table of contents (pp. 1-8): grep the body phrase, or take the last / non-TOC match of a heading
- **Probe:** M.R.U. Crim. P. 11 → `https://www.courts.maine.gov/rules/text/mru_crim_p_only_2026-10-01.pdf` — expect: "RULE 11. PLEAS; SPECIAL CIRCUMSTANCES (body heading p. 39 — the first match is the TOC on p. 3)"
- **Evidence (2026-10-17):** fetch_doc grep: Rule 11 heading at p. 39 (offset 71,104) with body following; 128 pp. | Independent check 2026-10-17: fetch_doc: 128 pp.; 'Last reviewed and edited September 24, 2026'; Rule 11 heading verified; second citation M.R.U. Crim. P. 16 ok

### `me-rules-evidence` — Maine Rules of Evidence (rules only, PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Supreme Judicial Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** 60 pp., 99,142 chars; 2025 and 2026 amendments are separate orders (2025 Me. Rules 08, 2026 Me. Rules 04).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.maine.gov/rules/text/mr_evid_only_2018-06-29.pdf`
  - Placeholders: Dated file name; re-read the rules index and check amendment orders under 'Recent rule amendments'.
  - Index: `https://www.courts.maine.gov/rules/index.html`
  - Navigation: rules index → Evidence 'Rules only--no advisory notes'
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Just under 100K characters: WebFetch might read it whole, untested.
- **Currency:** first line of the PDF — observed: "Last reviewed and edited June 29, 2018 Includes amendment effective August 1, 2018"
- **Official status:** Published on the Judicial Branch rules page.
- **Hazard:** compiled text is from 2018; later amendments (2025 Me. Rules 08, 2026 Me. Rules 04) only in separate orders
- **Hazard:** rule headings appear first in the table of contents (pp. 1-8): grep the body phrase, or take the last / non-TOC match of a heading
- **Probe:** M.R. Evid. 401 → `https://www.courts.maine.gov/rules/text/mr_evid_only_2018-06-29.pdf` — expect: "Evidence is relevant if: (a) It has any tendency to make a fact more or less probable"
- **Evidence (2026-10-17):** fetch_doc grep: Rule 401 body at p. 13 ('Evidence is relevant if: (a) It has any tendency'); 60 pp. | Independent check 2026-10-17: fetch_doc verify: Rule 401 quote p. 13; 'Last reviewed and edited June 29, 2018'; second citation Me. R. Evid. 803 ok

### `me-rules-professional-conduct` — Maine Rules of Professional Conduct (rules only, PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Supreme Judicial Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** 67 pp., 145,567 chars. Same index also links Bar Rules, Bar Admission Rules, Code of Judicial Conduct, Probate Procedure, Small Claims rules, Electronic Court Systems rules.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.maine.gov/rules/text/mr_prof_conduct_only_2023-09-28.pdf`
  - Placeholders: Dated file name; re-read the rules index.
  - Index: `https://www.courts.maine.gov/rules/index.html`
  - Navigation: rules index → 'Rules governing judges, lawyers, and guardians ad litem' → Professional Conduct 'Rules only'
- **Automation:** WebFetch untested · shell ok · robots: none (404)
- **Currency:** first line of the PDF — observed: "Last reviewed and edited September 28, 2023 Including amendments effective September 28, 2023"
- **Official status:** Published on the Judicial Branch rules page.
- **Hazard:** beyond WebFetch window
- **Hazard:** rule headings appear first in the table of contents (pp. 1-8): grep the body phrase, or take the last / non-TOC match of a heading
- **Probe:** M.R. Prof. Conduct 1.7 → `https://www.courts.maine.gov/rules/text/mr_prof_conduct_only_2023-09-28.pdf` — expect: "RULE 1.7 CONFLICT-OF-INTEREST: CURRENT CLIENTS (a) Except as provided in paragraph (b)"
- **Evidence (2026-10-17):** fetch_doc grep: Rule 1.7 body at p. 22 ('(a) Except as provided in paragraph (b), a lawyer'); 67 pp. | Independent check 2026-10-17: fetch_doc verify: Rule 1.7 quote p. 22; 'Last reviewed and edited September 28, 2023'; second citation M.R. Prof. Conduct 1.15 ok

## D. Administrative code

### `me-cmr-sos` — Code of Maine Rules (Secretary of State, agency rules)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Maine Secretary of State, Administrative Procedure Act Office · text: **link-only** · official: unknown
- **Coverage:** Agency rule chapters by umbrella-unit number (e.g. 10-144 ch. 101), linked from LII as http://www.maine.gov/sos/cec/rules/rules.html; current agency-rules pages at /sos/rulemaking/agency-rules/… (from search).
- **Access:** `link-only` · format html
  - Index: `https://www.maine.gov/sos/rulemaking/agency-rules`
- **Automation:** WebFetch fail · shell blocked-challenge · robots: www.maine.gov answers robots.txt with a bot check (fetch_doc REFUSED)
  - WebFetch: /sos/rulemaking/agency-rules and …/department-administrative-financial-services-rules → 'There was an error while fetching'; /sos/cec/rules/rules.html → permission prompt timed out. Copies on www11.maine.gov and apps.web.maine.gov (seen in search results) are alternate hostnames for the walled host and are NOT used.
- **Currency:** not reached
- **Official status:** Not readable: host refuses automated access.
- **Hazard:** bot-walled host
- **Hazard:** mirror hostnames must not be used
- **Probe:** 10-144 C.M.R. ch. 101 → `https://www.maine.gov/sos/rulemaking/agency-rules`
- **Evidence (2026-10-17):** fetch_doc: 'www.maine.gov answers robots.txt with a bot check (refused)'; WebFetch: 'There was an error while fetching' on two agency-rules URLs. | Re-confirmed blocked 2026-10-17: WebFetch: 'There was an error while fetching.'

### `me-cmr-lii` — Cornell LII — Code of Maine Rules

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Code of Maine Rules by department / umbrella unit / chapter / section; one page per section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/maine/{agency}-{unit}-C-M-R-ch-{chapter}-SS-{section}`
  - Placeholders: agency = 2-digit department number, unit = 3-digit umbrella unit (26-239), chapter and section unpadded. Browse: /regulations/maine/department-{agency}/division-{unit}/chapter-{chapter} lists section links with section ranges ('§ 239-2-1 to 239-2-6'). Chapters that LII splits into Roman sub-chapters use SS-{subchapter_roman}-{section}: 10-144 C.M.R. ch. 101 (MaineCare Benefits Manual) → /regulations/maine/10-144-C-M-R-ch-101-SS-II-22 style; browse /department-10/division-144/chapter-101 and its sub-chapter pages to get the real section link (some sub-chapter pages list only repealed sections).
  - Index: `https://www.law.cornell.edu/regulations/maine`
  - Navigation: department list → division (umbrella unit) → chapter page with section links → section page
- **Automation:** WebFetch untested · shell ok · robots: allows /regulations/; Crawl-delay 10
  - fetch_doc honours the 10 s crawl delay. Some large CMR chapters (MaineCare 10-144 ch. 101) are split by LII into many sections.
- **Currency:** section page note plus HTTP last-modified (Aug. 2025 on 2026-10-17 despite the note) — observed: "State regulations are updated quarterly"
- **Official status:** LII states regulations are updated quarterly; third-party compilation.
- **Hazard:** quarterly lag
- **Hazard:** tier 2 only route for admin code (official host bot-walled)
- **Hazard:** Roman sub-chapter sections (ch. 101 SS-II-22) do not fit the plain ch-{n}-SS-{n} pattern
- **Hazard:** page last-modified Aug. 2025: 'quarterly' updates not borne out
- **Probe:** 26-239 C.M.R. ch. 2, § 1 → `https://www.law.cornell.edu/regulations/maine/26-239-C-M-R-ch-2-SS-1` — expect: "The State, after assessing all of the facts in the case, including any valid defenses"
- **Evidence (2026-10-17):** fetch_doc read: breadcrumb 'C.M.R. 26, 239, ch. 2 - FORFEITURE RULES', body 'A. The State, after assessing all of the facts in the case'; chapter page lists § 239-2-1 … 239-2-6. Only one regulation probed. | Independent check 2026-10-17: fetch_doc: 'A. The State, after assessing all of the facts in the case'; 'updated quarterly'; second citation 02-031 C.M.R. ch. 140, § 1 ok

## D. Administrative register

### `me-register-sos` — Weekly Notices of Rulemaking (Secretary of State)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Maine Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Maine has no printed register; the APA Office posts weekly rulemaking notices on www.maine.gov/sos (from memory).
- **Access:** `link-only` · format html
  - Index: `https://www.maine.gov/sos/rulemaking`
- **Automation:** WebFetch untested · shell blocked-challenge · robots: www.maine.gov answers robots.txt with a bot check
  - Same host as me-cmr-sos; WebFetch failed there, so not tried here.
- **Currency:** not reached
- **Official status:** Not readable.
- **Hazard:** bot-walled host
- **Probe:**  → `https://www.maine.gov/sos/rulemaking`
- **Evidence (2026-10-17):** fetch_doc REFUSED for www.maine.gov (bot check on robots.txt); index URL not confirmed by a fetch. | Re-confirmed blocked 2026-10-17: WebFetch permission prompt timed out; fetch_doc check: REFUSED (robots.txt bot check)

## E. Case law

### `me-bcd-orders` — Business and Consumer Docket — Orders and Decisions archive

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Maine Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** BCD orders and decisions from 2008 to about 2016-2020 (newest rows seen 2016 in the appeals table), by docket (BCD-WB-AP-09-02, BCD-AP-14-03).
- **Access:** `index-anchored` · format pdf
  - Placeholders: File paths are irregular (…/ap-orders/AP-09-06/AP-09-06%20Decision%20and%20Order%205.21.09.pdf); read the listing.
  - Index: `https://www.courts.maine.gov/courts/bcd/orders.html`
  - Navigation: listing table (docket, case, order type, date) → PDF
- **Automation:** WebFetch gated · shell unreadable-format · robots: none (404)
  - Probed PDF is an image scan with no text layer (5 pp., 4 characters extracted).
- **Currency:** page note — observed: "Orders and Decisions page is no longer being updated"
- **Official status:** Page says it is no longer being updated; BCD documents now via re:SearchMaine (eCourts).
- **Hazard:** scanned PDFs without text
- **Hazard:** archive frozen
- **Hazard:** re:SearchMaine requires an account
- **Probe:** Nerber v. State Tax Assessor, BCD-WB-AP-09-06 (May 21, 2009) → `https://www.courts.maine.gov/courts/bcd/ap-orders/AP-09-06/AP-09-06%20Decision%20and%20Order%205.21.09.pdf`
- **Evidence (2026-10-17):** Listing read by fetch_doc (559 links); one PDF downloaded: 5 pp., no extractable text. | Independent check 2026-10-17: WebFetch gated (no answer); fetch_doc instead: 'Orders and Decisions page is no longer being updated' (row stays reported: scans have no text)

### `me-maine-reports-lldc` — Maine Reports vols. 1-161 (scanned, Law and Legislative Digital Library)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine State Law and Legislative Reference Library · text: **fetch-and-quote** · official: official
- **Coverage:** Vols. 1-161 (1820-1965), one PDF per volume with OCR text and the printed reporter page numbers in running heads.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/{volume:03d}ME.pdf`
  - Placeholders: volume zero-padded to 3 digits (001ME.pdf … 161ME.pdf). PDF page ≠ reporter page: front matter shifts it (vol. 161: Me. page 28 = PDF page 40; vol. 150: Me. page 18 = PDF page 30). grep the running head '{page} … [{volume}' or the case name. The running head can sit above the tail of the previous case on the same page; the cited case starts after it (158 Me. 360 = PDF p. 370, offset 10).
  - Index: `https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/`
  - Navigation: directory listing (162 links) → volume PDF
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Volumes are 500-750 pages and 1-1.4M characters; WebFetch cannot reach most of a volume.
- **Currency:** closed series — observed: "JANUARY 1, 1965 to DECEMBER 31, 1965 (vol. 161)"
- **Official status:** Scans of the official Maine Reports (title page: 'MAINE REPORTS … CASES ARGUED AND DETERMINED IN THE SUPREME JUDICIAL COURT', Reporter of Decisions).
- **Hazard:** OCR errors ('Sodoniy', '@')
- **Hazard:** very large PDFs
- **Hazard:** PDF page offset from reporter page
- **Probe:** State v. Viles, 161 Me. 28 (1965) → `https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/161ME.pdf` — expect: "MARDEN, J. On appeal. After a verdict of guilty"
- **Evidence (2026-10-17):** fetch_doc: 161ME.pdf 742 pp., 1,372,042 chars; PDF p. 40 running head '28 STATE OF MAINE vs. VILES, SR. [161'. 150ME.pdf 554 pp.; PDF p. 30 head '18 BELFAST, IN EQ. VS. GOODWILL FARM'. | Independent check 2026-10-17: fetch_doc: 161ME.pdf 742 pp.; 'MARDEN, J. On appeal. After a verdict' p. 40; second citation State v. Croteau, 158 Me. 360 (1962) ok
- **Notes:** Official page numbers for pre-1966 Maine cases, which no other free source gives.

### `me-opinions-courts` — Maine Supreme Judicial Court — Published Opinions (Law Court)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Judicial Branch, Reporter of Decisions · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Published opinions 2017-2026 (year pages 2017-2025 plus the current year on opinions.html; /lawcourt/2010/ and /2006/ return 404). Opinions carry the public-domain cite and paragraph numbers; slip pagination only.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://courts.maine.gov/courts/sjc/lawcourt/{YYYY}/{yy}me{number:03d}.pdf`
  - Placeholders: 2024 ME 84 → /lawcourt/2024/24me084.pdf; 2017 ME 239 → /lawcourt/2017/17me239.pdf. Revised opinions and orders add a suffix ('26me075re.pdf' revised, '26me075or.pdf' order on reconsideration) — check the year page when an opinion was revised. Year page: /courts/sjc/lawcourt/{YYYY}/index.html (current year on /courts/sjc/opinions.html) lists cite, case name, date and the PDF link. CURRENT YEAR: /courts/sjc/lawcourt/{current year}/index.html is a 404 — the current year's opinions are listed only on https://courts.maine.gov/courts/sjc/opinions.html (PDF files still live in /lawcourt/{YYYY}/); use /{YYYY}/index.html for 2017 through last year.
  - Index: `https://courts.maine.gov/courts/sjc/opinions.html`
  - Navigation: current year → opinions.html; 2017 to last year → /lawcourt/{YYYY}/index.html → PDF
- **Automation:** WebFetch ok · shell ok · robots: none (404 on courts.maine.gov and www.courts.maine.gov)
  - A 56-page opinion (85,868 chars) fit one WebFetch window; longer ones may not.
- **Currency:** opinions.html lists the newest first — observed: "2026 ME 102 newest on 2026-10-17"
- **Official status:** Year pages state the permanent, official versions are those in the Atlantic Reporter (official reporter since 1966).
- **Hazard:** slip pagination; no A.3d page numbers
- **Hazard:** revised opinions use suffixed file names
- **Hazard:** no docket search; docket appears only inside the PDF
- **Hazard:** no year page for the current year (404); use opinions.html
- **Probe:** State v. Sheppard, 2024 ME 84 → `https://courts.maine.gov/courts/sjc/lawcourt/2024/24me084.pdf` — expect: "Ramel L. Sheppard appeals from a judgment of conviction for domestic violence aggravated assault"
- **Evidence (2026-10-17):** fetch_doc: 24me084.pdf 56 pp., header 'Decision: 2024 ME 84 Docket: And-23-68'; 17me239.pdf 20 pp. 'Decision: 2017 ME 239 Docket: Cum-17-54'. WebFetch (via 2024 year page): YES '[¶1] Ramel L. Sheppard appeals from a judgment of conviction', complete through dissent, not truncated. | Independent check 2026-10-17: fetch_doc verify 24me084.pdf p. 1; opinions.html newest 2026 ME 102 (WebFetch + script); second citation Lee v. Town of Denmark, 2019 ME 54; State v. Bradbury, 2026 ME 99 ok

### `me-cases-justia` — Justia — Maine Supreme Judicial Court opinions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Judicial Court 1838-2026 per the court index page; fills the 1997-2016 gap on the court site.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/maine/supreme-court/{YYYY}/{slug}.html`
  - Placeholders: Recent years: slug = '{YYYY}-me-{number}' unpadded (2024 ME 84 → /2024/2024-me-84.html). Older years use the court's file name plus party initials (2010 ME 120 → /2010/10me120da.html), not derivable: read the year listing. The '{YYYY}-me-{n}' slug was seen for 2019 and 2024; 2010 uses the old form. The first year of the new form is not established: always read the year listing.
  - Index: `https://law.justia.com/cases/maine/supreme-court/`
  - Navigation: court index (years 1838-2026) → year listing (case name, date, cite) → opinion page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check on robots.txt)
  - A guessed /2010/2010-me-1.html returned a fetch error: older slugs differ.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** slug format changes by year
- **Hazard:** shell blocked
- **Hazard:** no reporter pagination
- **Probe:** Dalton v. Quinn, 2010 ME 120 → `https://law.justia.com/cases/maine/supreme-court/2010/10me120da.html` — expect: "Merilyn A. Dalton, individually and as personal representative of the"
- **Evidence (2026-10-17):** WebFetch: YES, 2010 ME 120, Cum-10-120, [¶1]-[¶8], not truncated. Second: /2024/2024-me-84.html YES '[¶1] Ramel L. Sheppard appeals', [¶1]-[¶87], complete. | Independent check 2026-10-17: WebFetch: YES 'Merilyn A. Dalton, individually and as personal representative of the'; Cum-10-120; second citation Lee v. Town of Denmark, 2019 ME 54 ok

## F. Subsequent history

### `me-subsequent-history-lawcourt` — Law Court dispositions (published opinions and recent memoranda of decision)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Maine Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Maine has no intermediate appellate court: appeals from Superior, District, Probate and BCD go to the Supreme Judicial Court sitting as the Law Court, which decides by published opinion (YYYY ME N) or memorandum of decision (Mem YY-N). Memoranda are listed with docket, trial judge and result ('Affirmed') for only about 60-90 days, without PDF links. Further review is only U.S. Supreme Court certiorari.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.maine.gov/courts/sjc/lawcourt/{YYYY}/index.html (2017 … last year); current year: https://courts.maine.gov/courts/sjc/opinions.html`
  - Placeholders: Year pages list case name, cite and date only, not the docket or the court below: find the appeal by party name (State of Maine v. {defendant}; civil captions keep the trial-court order of parties) in the year(s) after the trial decision, then confirm the trial docket/county inside the PDF ('trial court (Androscoggin County, Stewart, J.)'). Recent memoranda: https://courts.maine.gov/courts/sjc/memdec.html (columns Docket #, Mem Dec #, Case Title, Date, Subject, Trial Judge, Result). CURRENT YEAR: /courts/sjc/lawcourt/{current year}/index.html is a 404 — the current year's opinions are listed only on https://courts.maine.gov/courts/sjc/opinions.html (PDF files still live in /lawcourt/{YYYY}/); use /{YYYY}/index.html for 2017 through last year.
  - Index: `https://courts.maine.gov/courts/sjc/opinions.html`
  - Navigation: current year → opinions.html; earlier years → /lawcourt/{YYYY}/index.html → party-name match → PDF; memdec.html for the last ~90 days
- **Automation:** WebFetch ok · shell ok · robots: none (404)
- **Currency:** memdec.html header — observed: "listed on this page for approximately 60-90 days after they are issued"
- **Official status:** Slip opinions; official text in A.3d.
- **Hazard:** party-name search only
- **Hazard:** memoranda of decision vanish from the page after ~90 days and have no free text
- **Hazard:** no docket search
- **Hazard:** no year page for the current year (404); use opinions.html
- **Probe:** State v. Sheppard, And-23-68 → 2024 ME 84 → `https://courts.maine.gov/courts/sjc/memdec.html` — expect: "Memoranda of decision are listed on this page for approximately 60-90 days"
- **Evidence (2026-10-17):** fetch_doc: memdec.html 30,496 chars, first row 'Yor-26-37 Mem 26-139 In re Child of Emily V. 10/15/26 … Affirmed'; no PDF links. 24me084.pdf names the trial court (Androscoggin County) and docket And-23-68. | Independent check 2026-10-17: fetch_doc memdec.html: '...listed on this page for approximately 60-90 days'; first row Mem 26-139; second citation State v. Bradbury, Pis-25-160 -> 2026 ME 99 ok

## Not available (do not look for these again)

- **case_law** — Law Court opinions 1997-2016 on courts.maine.gov: opinions.html links year pages 2017-2025 only; /courts/sjc/lawcourt/2010/index.html and /2006/index.html and 10me001.pdf → HTTP 404. Use Justia. (2026-10-17)
- **case_law** — Text of memoranda of decision (Mem YY-N) and any memoranda older than ~90 days: memdec.html lists rows without document links and keeps them 60-90 days. (2026-10-17)
- **case_law** — Free official (A.2d/A.3d) pagination for Maine opinions since 1966: Court year pages: official versions are those in the Atlantic Reporter (West); court PDFs have slip pagination and ¶ numbers only. (2026-10-17)
- **statutes** — public.law and Cornell LII editions of the Maine Revised Statutes / Constitution: LII's Maine page (https://www.law.cornell.edu/states/maine) links out to the legislature for statutes and constitution and hosts only the CMR; public.law covers other states only (per prior records). (2026-10-17)
- **statutes** — Certified/official online text of the Maine Revised Statutes: Section PDF footer: not officially certified by the Secretary of State; certified text is the M.R.S.A. (2026-10-17)

## Corpus candidates (maintainers)

- `me-rules-civil` — 286 pp., 640K chars; far beyond a WebFetch window
- `me-rules-criminal` — 128 pp., 275K chars
- `me-rules-appellate` — 68 pp., 140K chars
- `me-rules-professional-conduct` — 67 pp., 146K chars
- `me-rules-evidence` — 60 pp., 99K chars — at the edge of a WebFetch window
- `me-constitution-revisor` — 50 pp., 134K chars; later articles beyond a WebFetch window
- `me-maine-reports-lldc` — 161 volumes of 500-750 pp. with official pagination; OCR text · bulk: https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/
- `me-statutes-legislature` — per-title PDF/DOCX is a bulk alternative to per-section pages · bulk: https://legislature.maine.gov/statutes/{title}/title{title}.docx

## Open questions

- WebFetch ran out of session quota midway (2026-10-17) and built URLs were gated: WebFetch untested on lldc session laws, the constitution PDF, rule PDFs other than civil (gated), Maine Reports and LII CMR.
- Does the Revisor constitution text (CR 2023, cc. 1-2) include amendments ratified Nov. 2023 and later? Compare with lldc MeConst_2024_Amd.pdf.
- Official CMR and weekly rulemaking notices on www.maine.gov are bot-walled; no tier-1 admin route. Is there a legislature-hosted copy linked by the publisher?
- Laws of Maine JSON API (breeze/Law/getLawGroup) returned only ~20 chapters per session — partial index or different parameters?
- Superior Court decisions: any free official listing besides the frozen BCD archive (Maine State Law Library)?
- CourtListener ids 'me' and 'mesuperct' unverified.
- me-statutes-justia: which Maine titles' segment-less Justia URLs fall back to old editions (seen: Title 22 → 2013)?

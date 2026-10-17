# Alaska (AK) — free legal sources

_Generated from `data/ak.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and the Administrative Code: akleg.gov's interactive pages are JavaScript shells, but a print endpoint (statutes.asp / aac.asp?media=print&secStart=…&secEnd=…) returns exact section text from the citation, current to 'Alaska Statutes 2025'; Justia (statutes) and Cornell LII (AAC, with Register history) are tier-2 fallbacks. Constitution: one ltgov.alaska.gov page (105K chars). Court rules: one long PDF per set on courts.alaska.gov (Civil 955K chars; the fetch tool stops at Rule 6), so corpus ingest is needed. Case law: the Appellate CMS gives GET docket search and slip PDFs only until P.3d publication; the court's full 1960-on database (govt.westlaw.com) is behind Cloudflare, leaving Justia as the archive; no public-domain citation.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Alaska Supreme Court | `alaska (unverified)` | Alaska | P.3d, P.2d | — |
| Alaska Court of Appeals | `alaskactapp (unverified)` | Alaska App. | P.3d, P.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Alaska Statutes | `AS 09.10.070`; `Alaska Stat. § 09.10.070`; `AS 11.41.100(a)(1)`; `AS 11.41.410 - 11.41.470`; `Alaska Stat. §§ 09.10.010-.240`; `former AS 09.10.070`; `AS 9.10.070`; `section 34.03.220 of the Alaska Statutes` | `ak-statutes-akleg` → `ak-statutes-justia` |
| Session Laws of Alaska | `ch. 70, SLA 1996`; `§ 1, ch. 166, SLA 1988` | `ak-session-laws-akleg` |
| Alaska Constitution | `Alaska Const. art. I, § 22`; `Alaska Const. art. IV, § 1`; `Article I, Section 22 of the Alaska Constitution`; `article I, section 7 of the Alaska Constitution`; `section 1 of the Alaska Constitution, article VIII`; `article VIII, section 3 of the Alaska Constitution` | `ak-constitution-ltgov` |
| Alaska Rules of Civil Procedure | `Alaska R. Civ. P. 12(b)(6)`; `Alaska Civil Rule 82`; `Rule 56(c) of the Alaska Rules of Civil Procedure` | `ak-rules-civil` |
| Alaska Rules of Criminal Procedure | `Alaska R. Crim. P. 35.1`; `Alaska Criminal Rule 11` | `ak-rules-criminal` |
| Alaska Rules of Evidence | `Alaska R. Evid. 702`; `Alaska Evidence Rule 404(b)` | `ak-rules-evidence` |
| Alaska Rules of Appellate Procedure | `Alaska R. App. P. 214(d)`; `Alaska Appellate Rule 302` | `ak-rules-appellate` |
| Alaska Rules of Administration | `Alaska R. Admin. 37.5`; `Alaska Administrative Rule 9` | `ak-rules-administrative` |
| Alaska court rules, Alaska practitioners' short forms without state name *(only once this jurisdiction is known)* | `Civil Rule 82(b)(2)`; `Criminal Rule 35.1`; `Evidence Rule 702`; `Appellate Rule 214(d)`; `Administrative Rule 37.5` | `ak-rules-civil` → `ak-rules-criminal` → `ak-rules-evidence` → `ak-rules-appellate` → `ak-rules-administrative` |
| Alaska Administrative Code | `7 AAC 160.900`; `18 AAC 75.400(a)`; `1 AAC 05.010`; `Alaska Admin. Code tit. 7, § 160.900` | `ak-aac-akleg` → `ak-aac-lii` |
| Reported Alaska cases (Pacific Reporter, Alaska court parenthetical) | `West v. Municipality of Anchorage, 174 P.3d 224 (Alaska 2007)`; `McCoy v. State, 80 P.3d 757, 764 (Alaska App. 2002)`; `594 P.3d 183 (Alaska 2026)` | `ak-opinions-cms` → `ak-cases-justia` |
| Alaska slip and unpublished opinions (opinion / MO&J numbers) | `King v. Carty, Op. No. 7834 (Alaska Oct. 9, 2026)`; `Marino v. State, Op. No. 2814 (Alaska App. Aug. 22, 2025)`; `Smith v. State, 2024 WL 123456, at *2 (Alaska App. Mar. 6, 2024) (unpublished)`; `Alaska App. Mem. Op. & J. No. 7012` | `ak-opinions-cms` → `ak-cases-justia` |
| Alaska appellate docket numbers, bare *(only once this jurisdiction is known)* | `Supreme Court No. S-19268`; `Court of Appeals No. A-13337`; `No. S-12164` | `ak-opinions-cms` → `ak-subsequent-history-cms` |
| Petition for hearing dispositions *(only once this jurisdiction is known)* | `petition for hearing denied`; `pet. for hearing granted` | `ak-subsequent-history-cms` |

Regexes (case-insensitive):

- Alaska Statutes: `(?<![A-Za-z])(?:AS|Alaska\s+Stat(?:utes|\.)?(?:\s+Ann\.)?\s*§§?)\s*(?P<title>\d{1,2})\.(?P<chapter>\d{2})\.(?P<section>\d{3})(?!\d)|sec(?:tion|\.)\s+(?P<title2>\d{1,2})\.(?P<chapter2>\d{2})\.(?P<section2>\d{3})(?:\([a-z0-9]+\))*\s+of\s+the\s+Alaska\s+Statutes`
- Session Laws of Alaska: `ch\.\s*(?P<chapter>\d+),?\s*(?:FSSLA|SSSLA|TSSLA|SLA)\s*(?P<year>(?:19|20)\d\d)`
- Alaska Constitution: `Alaska\s+Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+)\s+of\s+the\s+Alaska\s+Constitution|sec(?:tion|\.)\s+(?P<section3>\d+)\s+of\s+(?:the\s+)?Alaska\s+Constitution,?\s+art(?:icle|\.)\s+(?P<article3>[IVXL]+)|art(?:icle|\.)\s+(?P<article4>[IVXL]+),?\s+sec(?:tion|\.)\s+(?P<section4>\d+)\s+of\s+the\s+Alaska\s+Constitution`
- Alaska Rules of Civil Procedure: `Alaska\s+(?:R\.\s*Civ\.\s*P\.|Civil\s+Rule)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Alaska\s+Rules\s+of\s+Civil\s+Procedure`
- Alaska Rules of Criminal Procedure: `Alaska\s+(?:R\.\s*Crim\.\s*P\.|Criminal\s+Rule)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Alaska\s+Rules\s+of\s+Criminal\s+Procedure`
- Alaska Rules of Evidence: `Alaska\s+(?:R\.\s*Evid\.|Evidence\s+Rule)\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Alaska\s+Rules\s+of\s+Evidence`
- Alaska Rules of Appellate Procedure: `Alaska\s+(?:R\.\s*App\.\s*P\.|Appellate\s+Rule)\s*(?P<rule>\d+(?:\.\d+)?)`
- Alaska Rules of Administration: `Alaska\s+(?:R\.\s*Admin\.|Administrative\s+Rule)\s*(?P<rule>\d+(?:\.\d+)?)`
- Alaska court rules, Alaska practitioners' short forms without state name: `(?P<set>Civil|Criminal|Evidence|Appellate|Administrative)\s+Rule\s+(?P<rule>\d+(?:\.\d+)?)`
- Alaska Administrative Code: `(?P<title>\d{1,2})\s+AAC\s+(?P<chapter>\d{2,3})\.(?P<section>\d{3})|Alaska\s+Admin\.\s*Code\s+tit\.\s*(?P<title2>\d{1,2}),?\s*§\s*(?P<chapter2>\d{2,3})\.(?P<section2>\d{3})`
- Reported Alaska cases (Pacific Reporter, Alaska court parenthetical): `(?P<vol>\d{1,4})\s+P\.(?:\s*[23]d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Alaska(?:\s+App\.)?)\s*(?P<year>\d{4})\)`
- Alaska slip and unpublished opinions (opinion / MO&J numbers): `Op(?:inion)?\.?\s*No\.\s*(?P<opno>\d{4})[^()]{0,40}\(Alaska|(?P<wlyear>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)[^()]{0,30}\(Alaska|Alaska\s+App\.\s*Mem\.\s*Op\.\s*(?:&|and)\s*J\.\s*No\.\s*(?P<moj>\d+)`
- Alaska appellate docket numbers, bare: `(?:(?:Supreme\s+Court|Court\s+of\s+Appeals)\s+)?No\.\s*(?P<docket>[SA]-?\d{4,5})`
- Petition for hearing dispositions: `pet(?:ition|\.)\s+for\s+hearing\s+(?P<disp>denied|granted|dismissed)`

Statutes are cited 'AS 09.10.070' in Alaska courts' own style and 'Alaska Stat. § 09.10.070' in Bluebook; the regex requires the AS / Alaska Stat. prefix and the two-two-three digit form, reads 'AS 11.41.410 - 11.41.470' (a range) as its first section, and the print URL takes a range directly (secStart/secEnd). Bare 'AS' only routes with the dotted NN.NN.NNN number. The Administrative Code is '7 AAC 160.900' (title, chapter, section). Court rules are cited by Alaska courts as 'Civil Rule 82', 'Evidence Rule 702', 'Criminal Rule 35.1', 'Appellate Rule 214', 'Administrative Rule 37.5' without the state name: these short forms are shared with other states and are context_required; Bluebook forms 'Alaska R. Civ. P.', 'Alaska R. Evid.' carry the marker. Bare 'Rule 12(b)(6)' must not route here. Case law: no public-domain citation; reporter cites are P./P.2d/P.3d with '(Alaska YYYY)' or '(Alaska App. YYYY)'. Slip cites use the opinion number ('Op. No. 7834' Supreme; Court of Appeals numbers are in a separate, lower series, e.g. 2814) and docket numbers S-NNNNN (Supreme) / A-NNNNN (Court of Appeals). Court of Appeals memorandum opinions (MO&Js) carry their own numbers and are non-precedential under Appellate Rule 214(d). Supreme Court review of the Court of Appeals is by petition for hearing (Appellate Rules 302-305). The short-form rule pattern covers only Civil, Criminal, Evidence, Appellate and Administrative Rules (sets with source rows); Probate, CINA, Delinquency and other sets (PDFs on https://courts.alaska.gov/rules/) have no row and are not routed. One-digit titles ('AS 9.10.070') are zero-padded to two digits for the print URL. Prose forms 'section 34.03.220 of the Alaska Statutes' and 'section 1 of the Alaska Constitution, article VIII' are matched.

## A. Statutes / code

### `ak-session-laws-akleg` — Session Laws of Alaska (SLA chapter PDFs)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Alaska State Legislature · text: **link-only** · official: unknown
- **Coverage:** Chapter PDFs by year from 1959 (e.g. SLA 1963, 1996); older years are OCR'd scans.
- **Access:** `link-only` · format pdf
  - Placeholders: Observed form https://www.akleg.gov/pdf/billfiles/SLAs/SLA%20{year}/CH%20{chapter}%20SLA%20{year}.pdf (from a search result); not tested on a second chapter, so treat as link-only.
  - Index: `https://www.akleg.gov/basis/start.asp`
  - Navigation: start.asp → 'Session Laws and Resolves {year}' → chapter PDF
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.akleg.gov: 200; Disallow /PDF/, /cgi-bin/, /basis/get_jrn_page.asp and other legacy paths; /basis/statutes.asp and /basis/aac.asp permitted. fetch_doc.py matches 'Disallow: /PDF/' case-insensitively and so refuses lower-case /pdf/ URLs.
  - robots.txt 'Disallow: /PDF/' covers /pdf/billfiles/ (paths matched case-insensitively; www.akleg.gov is IIS). Not fetched by any route; cite and link only.
- **Currency:** none stated
- **Official status:** Enrolled chapter PDFs posted by the Legislature; not fetched (robots).
- **Hazard:** robots-disallowed on every route
- **Probe:** ch. 70, SLA 1996 → `https://www.akleg.gov/pdf/billfiles/SLAs/SLA%201996/CH%2070%20SLA%201996.pdf`
- **Evidence (2026-10-17):** fetch_doc.py check: REFUSED robots.txt on www.akleg.gov disallows /pdf/billfiles/SLAs/SLA%201996/CH%2070%20SLA%201996.pdf (rule: Disallow: /PDF/), exit 3. | Re-confirmed blocked 2026-10-17: Not WebFetched (policy: Disallow /PDF/ covers /pdf/). fetch_doc.py check: REFUSED robots 'Disallow: /PDF/', exit 3
- **Notes:** Session-law citation style: 'ch. 70, SLA 1996' or '§ 1, ch. 166, SLA 1988'. An earlier WebFetch read of this PDF (2026-10-17) predates the case-insensitive robots policy and is withdrawn.

### `ak-statutes-akleg` — Alaska Statutes (Alaska Legislature BASIS)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska State Legislature, Legislative Affairs Agency · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All 47 titles of the Alaska Statutes, current edition (labelled 'Alaska Statutes 2025'). Section text only; the print endpoint omits history notes and annotations.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.akleg.gov/basis/statutes.asp?media=print&secStart={TT.CC.SSS}&secEnd={TT.CC.SSS}`
  - Placeholders: Use the citation's section number with two-digit title (zero-pad a one-digit title: 'AS 9.10.070' → 09.10.070) and chapter and three-digit section (AS 09.10.070 → secStart=09.10.070&secEnd=09.10.070; AS 11.41.100 → 11.41.100). The same number goes in both parameters for one section. A range (AS 09.10.010 - 09.10.240) puts the first section in secStart and the last in secEnd, and returns every section between them; never read 'AS 11.41.410 - 11.41.470' as a single section. secStart={TT}&secEnd={TT}.99.999 returns a whole title (Title 9: 589,488 chars). The interactive page statutes.asp#09.10.070 is a JavaScript shell: the #fragment is not sent to the server and the page has no section text. Title TOC: statutes.asp?media=js&type=TOC&title={n} lists chapters (no section ranges).
  - Index: `https://www.akleg.gov/basis/statutes.asp`
- **Automation:** WebFetch gated · shell ok · robots: www.akleg.gov: 200; Disallow /PDF/, /cgi-bin/, /basis/get_jrn_page.asp and other legacy paths; /basis/statutes.asp and /basis/aac.asp permitted. fetch_doc.py matches 'Disallow: /PDF/' case-insensitively and so refuses lower-case /pdf/ URLs.
  - WebFetch refused the built print URL and the #anchor URL (PROVENANCE_REQUIRED). WebFetch of the search-result URL /basis/statUTES.asp returned only the title list (JS shell) and a cached 'Alaska Statutes 2024' label, while the live page (script) says 2025. Use the script route with the print URL. Whole-title print pages are 0.5MB+ and are not for the fetch tool.
- **Currency:** statutes.asp page header / breadcrumb (not on the print page); the print page that is quoted carries no currency line, so read it from statutes.asp — observed: "Alaska Statutes 2025"
- **Official status:** Alaska Court System law library guide (https://courts.alaska.gov/library/aklegal.htm): 'The official publisher of the Alaska Statutes is LexisNexis' (13-volume print set, biennial with annual supplement). No UELMA authentication statement found on akleg.gov.
- **Hazard:** interactive statutes.asp page is a JavaScript shell; #anchors are not fetchable
- **Hazard:** print endpoint omits history and annotations
- **Hazard:** section ranges are expressed 'AS x - y' and must not be read as one section
- **Hazard:** whole-title print pages exceed 500K chars
- **Probe:** AS 09.10.070 → `https://www.akleg.gov/basis/statutes.asp?media=print&secStart=09.10.070&secEnd=09.10.070` — expect: "unless the action is commenced within two years of the accrual of the cause of action"
- **Evidence (2026-10-17):** Script: 200 html 1,132 chars, 'Sec. 09.10.070. Actions for torts...'; verify of expect string VERIFIED. Second citation AS 11.41.100 → 7,196 chars 'Sec. 11.41.100. Murder in the first degree.' Range 09.10.010-09.10.240 → 17,804 chars with every Sec. heading. Bare statutes.asp#09.10.070 → 2,327-char shell, 0 matches. | Independent check 2026-10-17: WebFetch PROVENANCE_REQUIRED (gated). Script verify: VERIFIED 'unless the action is commenced within two years...' (1,132 chars); second citation AS 34.03.220; range AS 11.41.410 - 11.41.470 ok
- **Notes:** The same statutes.js serves /basis/aac.asp (see ak-aac-akleg). The Statute Information Retrieval System (/basis/Statutes/Sirs/34) tracks pending bills affecting a section.

### `ak-statutes-justia` — Alaska Statutes on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual editions; edition list on /codes/alaska/2020/ shows 2025, 2024, 2023, 2020 (older years 1997-2019 also exist).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/alaska/title-{title}/chapter-{chapter:02d}/[article-{n}/]section-{TT}-{CC}-{SSS}/`
  - Placeholders: Current (2025) edition lives at UNYEARED URLs: /codes/alaska/title-34/chapter-03/article-6/section-34-03-220/ (AS 34.03.220). Title unpadded, chapter two-digit, section slug = section number with dots as hyphens. Chapters divided into articles add an /article-{n}/ level and the chapter page lists only articles, so the article number is not derivable: take it from the chapter page. Year-prefixed URLs (/codes/alaska/2020/title-9/chapter-10/section-09-10-070/) are prior editions. Title pages list chapters without section ranges.
  - Index: `https://law.justia.com/codes/alaska/`
  - Navigation: /codes/alaska/title-{n}/ → chapter-{cc}/ → article-{n}/ (if the chapter lists articles) → section link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answers 403 Cloudflare 'Just a moment...' challenge
  - Script route refused (robots.txt challenge). WebFetch works on URLs reached from search results and fetched pages.
- **Currency:** edition year in URL; notice at top — observed: "These codes may not be the most recent version."
- **Official status:** Page notice 'These codes may not be the most recent version.'
- **Hazard:** edition year must be chosen; older editions carry 'There Is a Newer Version' banners
- **Hazard:** script route blocked
- **Hazard:** article level between chapter and section is not derivable from the citation
- **Probe:** AS 09.10.070 (2020 ed.) → `https://law.justia.com/codes/alaska/2020/title-9/chapter-10/section-09-10-070/` — expect: "(a) Except as otherwise provided by law, a person may"
- **Evidence (2026-10-17):** WebFetch: body present, first words '(a) Except as otherwise provided by law, a person may'; title-9 and chapter-10 index pages fetched; script REFUSED (challenge). | Independent check 2026-10-17: YES: '(a) Except as otherwise provided by law, a person may'; 'These codes may not be the most recent version.'; second citation AS 34.03.220 (2025 ed.) ok

## B. Constitution

### `ak-constitution-ltgov` — Constitution of the State of Alaska (Lieutenant Governor)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Office of the Lieutenant Governor · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full text, Articles I-XV with '[Amended YYYY]' notes; single HTML page (105,195 chars) plus the 64-page pocket PDF.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Index: `https://ltgov.alaska.gov/information/alaskas-constitution/`
  - Navigation: one page holds the whole Constitution; locate 'Article {roman} – {title}' then the numbered section ('22. Right of Privacy'). /services/alaskas-constitution/ (linked from akleg) redirects here. PDF: https://ltgov.alaska.gov/wp-content/uploads/PDF-Pocket-Constitution.pdf
- **Automation:** WebFetch gated · shell ok · robots: ltgov.alaska.gov: 200, Yoast block, 'Disallow:' empty
  - WebFetch refused the URL (PROVENANCE_REQUIRED). At 105K chars the page sits at the fetch-tool limit: later articles may be cut; use the script.
- **Currency:** '[Amended YYYY]' after each section; PDF page 2 print line — observed: "Printed in April 2023 (PDF); HTML has no date"
- **Official status:** No official-status statement on the page; the court law library guide says the Constitution is published in Volume 1 of the Alaska Statutes (LexisNexis).
- **Hazard:** page length near the 100K fetch-tool limit
- **Hazard:** section headings are '22. Right of Privacy' without '§'
- **Hazard:** each section heading also appears in the table of contents at the top (offset < ~6K): skip that first grep hit
- **Probe:** Alaska Const. art. I, § 22 → `https://ltgov.alaska.gov/information/alaskas-constitution/` — expect: "The right of the people to privacy is recognized and shall not be infringed"
- **Evidence (2026-10-17):** Script: 200 html 105,195 chars; expect VERIFIED; second citation art. I, § 7 'No person shall be deprived of life, liberty, or property, without due process of law' VERIFIED. PDF 64 pp, 116,813 chars, last-modified 12 Mar 2026. | Independent check 2026-10-17: WebFetch PROVENANCE_REQUIRED (gated). Script verify VERIFIED 'The right of the people to privacy is recognized...' (105,195 chars); second citation Alaska Const. art. VIII, § 3 ok

## C. Court rules

### `ak-rules-administrative` — Alaska Rules of Administration

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Supreme Court (Alaska Court System) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Complete unannotated rule set, one PDF (72 pp, 493,151 chars), with SCO amendment histories after each rule.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.alaska.gov/rules/`
  - Navigation: rules page → 'Alaska Rules of Administration' PDF https://courts.alaska.gov/rules/docs/adm.pdf; locate 'Rule N.' heading (two-column layout)
- **Automation:** WebFetch gated · shell ok · robots: courts.alaska.gov: 200; Disallow /cip/, /mediation/, /covid19/deleted/; PiplBot disallowed
  - Two-column PDF: headings read 'Rule 12. Defenses and Objections' inside a column; adjacent-column text interleaves in some extractions, so verify short quotes. courts.alaska.gov intermittently reset connections (empty reply) on 2026-10-17; retry later.
- **Currency:** HTTP last-modified; rules page lists recent SCO changes — observed: "last-modified 07 Oct 2026"
- **Official status:** Rules page (https://courts.alaska.gov/rules/): 'The official publisher of the Alaska Rules of Court is Tower Publishing.' The PDFs are the court's own current text including recent changes.
- **Hazard:** single long PDF (corpus candidate)
- **Hazard:** two-column layout
- **Hazard:** intermittent connection resets
- **Hazard:** grep 'Rule N.' plus the first word of the title only: headings use curly apostrophes (Attorney’s) and adjacent-column text interleaves
- **Probe:** Alaska R. Admin. 37.5 → `https://courts.alaska.gov/rules/docs/adm.pdf` — expect: "Rule 37.5. Access to Court Records."
- **Evidence (2026-10-17):** Script: pdf 72 pp, 493,151 chars, last-modified 07 Oct 2026. Body not quote-verified. | Independent check 2026-10-17: Script (WebFetch gated): 'Rule 37.5. Access to Court Records.' p. 32; last-modified 07 Oct 2026
- **Notes:** Other sets on the same page: Adoption (adop.pdf), Bar Rules (bar.pdf), CINA (cina.pdf), Code of Judicial Conduct (cjc.pdf), Delinquency (del.pdf), District Court Civil (dciv.pdf), Minor Offense (mo.pdf), Probate (prob.pdf), Professional Conduct (prof.pdf), Evidence Commentary (evcomm.pdf); Civil Rule 90.3 and commentary separately (civ90-3.pdf). Supreme Court Orders (SCO) adopting amendments: https://courts.alaska.gov/sco/index.htm.

### `ak-rules-appellate` — Alaska Rules of Appellate Procedure

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Supreme Court (Alaska Court System) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Complete unannotated rule set, one PDF (56 pp, 356,901 chars), with SCO amendment histories after each rule.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.alaska.gov/rules/`
  - Navigation: rules page → 'Alaska Rules of Appellate Procedure' PDF https://courts.alaska.gov/rules/docs/app.pdf; locate 'Rule N.' heading (two-column layout)
- **Automation:** WebFetch gated · shell ok · robots: courts.alaska.gov: 200; Disallow /cip/, /mediation/, /covid19/deleted/; PiplBot disallowed
  - Two-column PDF: headings read 'Rule 12. Defenses and Objections' inside a column; adjacent-column text interleaves in some extractions, so verify short quotes. courts.alaska.gov intermittently reset connections (empty reply) on 2026-10-17; retry later.
- **Currency:** HTTP last-modified; rules page lists recent SCO changes — observed: "last-modified 24 Jul 2025"
- **Official status:** Rules page (https://courts.alaska.gov/rules/): 'The official publisher of the Alaska Rules of Court is Tower Publishing.' The PDFs are the court's own current text including recent changes.
- **Hazard:** single long PDF (corpus candidate)
- **Hazard:** two-column layout
- **Hazard:** intermittent connection resets
- **Hazard:** grep 'Rule N.' plus the first word of the title only: headings use curly apostrophes (Attorney’s) and adjacent-column text interleaves
- **Probe:** Alaska R. App. P. 214 → `https://courts.alaska.gov/rules/docs/app.pdf` — expect: "Rule 214. Summary Disposition of Appeals."
- **Evidence (2026-10-17):** Script: pdf 56 pp, 356,901 chars, last-modified 24 Jul 2025. Body not quote-verified (grep 'Rule 302.' 0 matches: two-column headings split). | Independent check 2026-10-17: Script (WebFetch gated): 'Rule 214. Summary Disposition of Appeals.' p. 22; last-modified 24 Jul 2025

### `ak-rules-civil` — Alaska Rules of Civil Procedure

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Supreme Court (Alaska Court System) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Complete unannotated rule set, one PDF (150 pp, 955,507 chars), with SCO amendment histories after each rule.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.alaska.gov/rules/`
  - Navigation: rules page → 'Alaska Rules of Civil Procedure' PDF https://courts.alaska.gov/rules/docs/civ.pdf; locate 'Rule N.' heading (two-column layout)
- **Automation:** WebFetch ok (truncated) · shell ok · robots: courts.alaska.gov: 200; Disallow /cip/, /mediation/, /covid19/deleted/; PiplBot disallowed
  - Two-column PDF: headings read 'Rule 12. Defenses and Objections' inside a column; adjacent-column text interleaves in some extractions, so verify short quotes. courts.alaska.gov intermittently reset connections (empty reply) on 2026-10-17; retry later. WebFetch reaches only Rules 1-6 of ~99.
- **Currency:** HTTP last-modified; rules page lists recent SCO changes — observed: "last-modified 29 Apr 2026"
- **Official status:** Rules page (https://courts.alaska.gov/rules/): 'The official publisher of the Alaska Rules of Court is Tower Publishing.' The PDFs are the court's own current text including recent changes.
- **Hazard:** single long PDF (corpus candidate)
- **Hazard:** two-column layout
- **Hazard:** intermittent connection resets
- **Hazard:** grep 'Rule N.' plus the first word of the title only: headings use curly apostrophes (Attorney’s) and adjacent-column text interleaves
- **Probe:** Alaska R. Civ. P. 12(b)(6) → `https://courts.alaska.gov/rules/docs/civ.pdf` — expect: "failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** Script: pdf 150 pp, 955,507 chars; expect VERIFIED on p. 32; Rule 12 heading on p. 32. WebFetch (search-result URL COURTS.ALASKA.GOV/rules/docs/civ.pdf): 'Content truncated', stops in Rule 6 history; Rule 12(b) NOT PRESENT. | Independent check 2026-10-17: Script verify VERIFIED 'failure to state a claim upon which relief can be granted' p. 32; last-modified 29 Apr 2026; second citation Alaska Civil Rule 82 ok

### `ak-rules-criminal` — Alaska Rules of Criminal Procedure

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Supreme Court (Alaska Court System) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Complete unannotated rule set, one PDF (80 pp, 474,580 chars), with SCO amendment histories after each rule.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.alaska.gov/rules/`
  - Navigation: rules page → 'Alaska Rules of Criminal Procedure' PDF https://courts.alaska.gov/rules/docs/crpro.pdf; locate 'Rule N.' heading (two-column layout)
- **Automation:** WebFetch gated · shell ok · robots: courts.alaska.gov: 200; Disallow /cip/, /mediation/, /covid19/deleted/; PiplBot disallowed
  - Two-column PDF: headings read 'Rule 12. Defenses and Objections' inside a column; adjacent-column text interleaves in some extractions, so verify short quotes. courts.alaska.gov intermittently reset connections (empty reply) on 2026-10-17; retry later.
- **Currency:** HTTP last-modified; rules page lists recent SCO changes — observed: "last-modified 09 Oct 2026"
- **Official status:** Rules page (https://courts.alaska.gov/rules/): 'The official publisher of the Alaska Rules of Court is Tower Publishing.' The PDFs are the court's own current text including recent changes.
- **Hazard:** single long PDF (corpus candidate)
- **Hazard:** two-column layout
- **Hazard:** intermittent connection resets
- **Hazard:** grep 'Rule N.' plus the first word of the title only: headings use curly apostrophes (Attorney’s) and adjacent-column text interleaves
- **Probe:** Alaska R. Crim. P. 35.1 → `https://courts.alaska.gov/rules/docs/crpro.pdf` — expect: "Rule 35.1. Post-Conviction Procedure."
- **Evidence (2026-10-17):** Script: pdf 80 pp, 474,580 chars; grep 'Rule 35.1. Post-Conviction Procedure.' at p. 61. | Independent check 2026-10-17: Script grep 'Rule 35.1. Post-Conviction Procedure.' p. 61; last-modified 09 Oct 2026; second citation Alaska Criminal Rule 11 ok

### `ak-rules-evidence` — Alaska Rules of Evidence

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Supreme Court (Alaska Court System) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Complete unannotated rule set, one PDF (26 pp, 159,059 chars), with SCO amendment histories after each rule.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.alaska.gov/rules/`
  - Navigation: rules page → 'Alaska Rules of Evidence' PDF https://courts.alaska.gov/rules/docs/ev.pdf; locate 'Rule N.' heading (two-column layout)
- **Automation:** WebFetch gated · shell ok · robots: courts.alaska.gov: 200; Disallow /cip/, /mediation/, /covid19/deleted/; PiplBot disallowed
  - Two-column PDF: headings read 'Rule 12. Defenses and Objections' inside a column; adjacent-column text interleaves in some extractions, so verify short quotes. courts.alaska.gov intermittently reset connections (empty reply) on 2026-10-17; retry later.
- **Currency:** HTTP last-modified; rules page lists recent SCO changes — observed: "last-modified 24 Dec 2024"
- **Official status:** Rules page (https://courts.alaska.gov/rules/): 'The official publisher of the Alaska Rules of Court is Tower Publishing.' The PDFs are the court's own current text including recent changes.
- **Hazard:** single long PDF (corpus candidate)
- **Hazard:** two-column layout
- **Hazard:** intermittent connection resets
- **Hazard:** grep 'Rule N.' plus the first word of the title only: headings use curly apostrophes (Attorney’s) and adjacent-column text interleaves
- **Probe:** Alaska R. Evid. 702 → `https://courts.alaska.gov/rules/docs/ev.pdf` — expect: "Rule 702. Testimony by Experts."
- **Evidence (2026-10-17):** Script: pdf 26 pp, 159,059 chars; 'Rule 702. Testimony by Experts.' on p. 19 (two-column interleave with a note on Rule 613). Commentary is a separate PDF: https://courts.alaska.gov/rules/docs/evcomm.pdf | Independent check 2026-10-17: Script grep 'Rule 702. Testimony by Experts.' p. 19; last-modified 24 Dec 2024; second citation Alaska Evidence Rule 404(b) ok

## D. Administrative code

### `ak-aac-akleg` — Alaska Administrative Code (Alaska Legislature BASIS)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska State Legislature (hosting); regulations filed with the Lieutenant Governor · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All AAC titles 1-20 (current). Print endpoint gives section text without history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.akleg.gov/basis/aac.asp?media=print&secStart={T}.{CC}.{SSS}&secEnd={T}.{CC}.{SSS}`
  - Placeholders: '7 AAC 160.900' → secStart=7.160.900&secEnd=7.160.900 (title unpadded or padded both work: 07.160.900 returned the same page); '18 AAC 75.400' → 18.75.400. Chapter may be 2 or 3 digits as printed. Title TOC: aac.asp?media=js&type=TOC&title={n} lists parts with section ranges (e.g. 'Part 8 ... (7 AAC 105.100 — 7 AAC 160.990)').
  - Index: `https://www.akleg.gov/basis/aac.asp`
- **Automation:** WebFetch gated · shell ok · robots: www.akleg.gov: 200; Disallow /PDF/, /cgi-bin/, /basis/get_jrn_page.asp and other legacy paths; /basis/statutes.asp and /basis/aac.asp permitted. fetch_doc.py matches 'Disallow: /PDF/' case-insensitively and so refuses lower-case /pdf/ URLs.
  - aac.asp itself is a JS shell (title list only). Not tried in WebFetch (built URL; statutes print URLs were refused).
- **Currency:** none on the akleg page; history notes ('Eff. ..., Register NNN') appear only on Cornell LII — observed: "none stated"
- **Official status:** Court law library guide: 'The official publisher of the AAC is LexisNexis... The AAC is updated quarterly.' The Lt. Governor's regulations page links to akleg.gov as the AAC host.
- **Hazard:** print endpoint omits history notes and Register numbers
- **Hazard:** aac.asp landing page is a JS shell
- **Probe:** 7 AAC 160.900 → `https://www.akleg.gov/basis/aac.asp?media=print&secStart=7.160.900&secEnd=7.160.900` — expect: "The following documents referenced in 7 AAC 105 - 7 AAC 160 are adopted by reference"
- **Evidence (2026-10-17):** Script: 200 html 18,874 chars, '7 AAC 160.900. Requirements adopted by reference.'; second citation 18 AAC 75.400 → 5,689 chars '18 AAC 75.400. Applicability.'; 'Register' 0 matches. | Independent check 2026-10-17: Script verify VERIFIED 'The following documents referenced in 7 AAC 105 - 7 AAC 160...'; second citation 3 AAC 26.020 ok

### `ak-aac-lii` — Alaska Administrative Code on Cornell LII

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages with history notes (Register numbers).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/alaska/{title}-AAC-{chapter}.{section}`
  - Placeholders: '7 AAC 160.900' → 7-AAC-160.900; '18 AAC 75.400' → 18-AAC-75.400; '1 AAC 05.010' → 1-AAC-05.010 (chapter keeps its leading zero).
  - Index: `https://www.law.cornell.edu/regulations/alaska`
- **Automation:** WebFetch untested · shell ok · robots: law.cornell.edu robots.txt does not disallow /regulations/
  - Pages are large (7 AAC 160.900: 125,488 chars including navigation).
- **Currency:** HTTP last-modified; history note — observed: "last-modified 30 Jul 2025"
- **Official status:** Third-party republication.
- **Hazard:** may lag the akleg text (last-modified July 2025)
- **Probe:** 7 AAC 160.900 → `https://www.law.cornell.edu/regulations/alaska/7-AAC-160.900` — expect: "are adopted by reference"
- **Evidence (2026-10-17):** Script: 200 html 125,488 chars; expect VERIFIED; history note 'Eff. 2/1/2010, Register 193; am 8/25/2010, Register 195'. 18-AAC-75.400 → 200, 8,615 chars. | Independent check 2026-10-17: Script verify VERIFIED 'are adopted by reference'; last-modified 30 Jul 2025; second citation 3 AAC 26.020 ok
- **Notes:** Use for history notes / Register numbers, which the akleg print page omits.

## D. Administrative register

### `ak-online-public-notices` — Alaska Online Public Notice System (regulation notices)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · State of Alaska / Office of the Lieutenant Governor · text: **link-only** · official: official
- **Coverage:** Active and archived public notices, including proposed and adopted regulations, by department.
- **Access:** `search-only` · format html
  - Pattern: `https://aws.state.ak.us/OnlinePublicNotices/Notices/Search.aspx?status=4&cat=10&subcat={9|10}`
  - Placeholders: GET listing linked from https://ltgov.alaska.gov/information/regulations/ ('Proposed Regulations' / 'Adopted Regulations' use cat=10 with subcat=9 or 10). Free-text search fields exist on the form; not tested as GET parameters.
  - Index: `https://ltgov.alaska.gov/information/regulations/`
  - Navigation: regulations page → Proposed/Adopted Regulations link → notice rows
- **Automation:** WebFetch untested · shell ok · robots: aws.state.ak.us: 200; Disallow /*.axd?, /OAH/Files/*, /OAH/Decision/Download* (OPNS paths permitted)
  - ASP.NET form page; listing is 56,686 chars with form chrome.
- **Currency:** notice dates in rows
- **Official status:** Lt. Governor regulations page: proposed and adopted regulation notices must be published to a newspaper and to the Online Public Notice System (OPNS). Alaska has no current periodic register; 'Register NNN' in AAC history notes is the quarterly AAC supplement number.
- **Hazard:** notices, not a compiled register
- **Hazard:** ASP.NET postback paging
- **Probe:** adopted regulation notices → `https://aws.state.ak.us/OnlinePublicNotices/Notices/Search.aspx?status=4&cat=10&subcat=10` — expect: "Online Public Notice"
- **Evidence (2026-10-17):** Script: 200 html 56,686 chars; search form with Status/Title/Full Text/Department fields. | Independent check 2026-10-17: Script: 56,686 chars, 'Online Public Notice Search' form; second citation proposed regulation notices (subcat=9) ok
- **Notes:** The historic Alaska Administrative Journal (Lt. Governor, 1990s) survives as PDFs, e.g. https://aws.state.ak.us/onlinepublicnotices/Files/AAJ/aaj49.pdf ('ISSUE 49, December 6, 1999', 34 pp) — script-verified; historical only.

## E. Case law

### `ak-cases-westlaw-govt` — Alaska Case Law database (govt.westlaw.com/akcases)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Thomson Reuters for the Alaska Court System · text: **link-only** · official: unofficial
- **Coverage:** 1960-present published opinions plus selected unpublished opinions.
- **Access:** `search-only` · format html
  - Index: `https://govt.westlaw.com/akcases/Index`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: govt.westlaw.com/robots.txt returns Cloudflare 'Attention Required!' page
  - Script REFUSED (robots.txt challenge). Not retried by any other route.
- **Currency:** none observed
- **Official status:** Court law library guide: all Supreme Court and Court of Appeals opinions from 1960 published in West's Pacific Reporter, through the latest advance sheets, without West headnotes.
- **Hazard:** Cloudflare challenge
- **Probe:**  → `https://govt.westlaw.com/akcases/Index`
- **Evidence (2026-10-17):** Script: REFUSED robots.txt challenge; curl robots.txt → Cloudflare 'Attention Required! | Cloudflare'. | Re-confirmed blocked 2026-10-17: WebFetch PROVENANCE_REQUIRED (not answered); script check REFUSED robots.txt bot challenge, exit 3
- **Notes:** Linked from https://courts.alaska.gov/library/aklegal.htm. The only free full archive that the court itself points to.

### `ak-opinions-cms` — Alaska appellate opinions, MO&Js and orders (Appellate Case Management System)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Court System, Clerk of the Appellate Courts · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court slip opinions (listing dates 2022-2026; 87 rows show 'No Document Available' once a P.3d cite is assigned); Court of Appeals slip opinions (2018-2026, 62 without documents); Supreme Court and Court of Appeals MO&Js (2022-2026 rows; many without documents); Court of Appeals summary dispositions; published Supreme Court orders. Docket pages for all appellate cases. Older text is not here.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://appellate-records.courts.alaska.gov/CMSPublic/Search/CaseNumber?CaseNumber={S-NNNNN|A-NNNNN}&TrialCourtNumber=`
  - Placeholders: Listings (plain GET): .../CMSPublic/Home/Opinions?isCOA=False (Supreme) or True (Court of Appeals); MOJOpinions?isCOA=..., SummaryDispositions?isCOA=True, PublishedOrders?isCOA=False. Rows: opinion number (Supreme 'No. 7834', Court of Appeals 'No. 2814'), case number (S19268 / A13337), title, P.3d reference when assigned, 'Document Download' link. Docket search (plain GET, verified): /CMSPublic/Search/CaseNumber?CaseNumber=S-19268&TrialCourtNumber= (hyphen optional) or TrialCourtNumber={trial no.}; party search /CMSPublic/Search/PartyNameSearch?CourtTypeString={SC|COA|-1}&IsActiveStatus=-1&LastName=&FirstName=&CompanyName=. The PDF link OpenOpinionDocument?q={token} and docket link Case/General?q={token} carry opaque encrypted tokens (not constructible); take them from the listing or search result. Hrefs end with a stray apostrophe (q=...=') which the server accepts.
  - Index: `https://appellate-records.courts.alaska.gov/CMSPublic/Home/AppellateOpinions`
  - Navigation: (court, docket) → CaseNumber GET search → Case/General docket page (Opinions table: number, decision, date, citation, Document Download) → OpenOpinionDocument PDF (filename sp-{no}.pdf / ap-{no}.pdf). By date: listing page → row → PDF.
- **Automation:** WebFetch untested · shell ok · robots: appellate-records.courts.alaska.gov: robots.txt 404 (IIS 'File or directory not found')
  - Listing pages are ~105K chars of text (Supreme) — at the fetch-tool limit. The legacy courts.alaska.gov/ops/sp-{no}.pdf pattern returns 404. Weekly release: opinions Fridays 9 a.m.; MO&Js Wednesdays.
- **Currency:** date headings on the listing — observed: "Friday, October 16, 2026"
- **Official status:** Supreme Court slip PDFs: 'This opinion is subject to correction before publication in the PACIFIC REPORTER.' Court of Appeals slip PDFs: 'The text of this opinion can be corrected before ... Pacific Reporter.' Listing page: documents are downloadable 'until they are published in the official reporter' (P.2d/P.3d, Alaska Reporter).
- **Hazard:** documents removed after P.3d publication (no free official text for older cases)
- **Hazard:** slip pagination only
- **Hazard:** opaque tokens in PDF/docket URLs
- **Hazard:** MO&Js: non-precedential (App. R. 214(d))
- **Probe:** King v. Carty, No. S-19268, Op. No. 7834 (Alaska Oct. 9, 2026) → `https://appellate-records.courts.alaska.gov/CMSPublic/Search/CaseNumber?CaseNumber=S-19268&TrialCourtNumber=` — expect: "Scott King v. Courtenay Carty"
- **Evidence (2026-10-17):** Script: listing isCOA=False → row 'S19268 7834 Scott King v. Courtenay Carty'; PDF sp-7834.pdf 15 pp, 'Supreme Court No. S-19268 ... OPINION No. 7834'. CaseNumber GET search → full match S19268, 'Opinion Issued', 3DI-23-00110CI. Second citation: Marino v. State, No. A-13337, Op. No. 2814 (Alaska App. Aug. 22, 2025) → ap-2814.pdf 58 pp. Court of Appeals MO&J PDF A-14138 carries the Rule 214(d) legend. | Independent check 2026-10-17: Script: CaseNumber=S-19268 → 'S19268 Scott King v. Courtenay Carty 204 Appeal Opinion Issued'; second citation Collins v. State, No. A-12816, Op. No. 2833 (Alaska App. Oct. 2, 2026) ok
- **Notes:** Court of Appeals MO&Js say they 'do not create legal precedent' but may be cited for persuasive value (Appellate Rule 214(d)); the court page says MO&Js and summary dispositions are retained for three months, but the MO&J listing still shows rows back to 2022. An email list for slip opinions exists at list.state.ak.us (archive disallowed by robots).

### `ak-cases-justia` — Alaska Supreme Court and Court of Appeals decisions on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court by year (2007, 2023, 2024 verified; includes entries marked '(Unpublished)'); Court of Appeals 1980-2026 per index.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/alaska/{supreme-court|court-of-appeals}/{year}/`
  - Placeholders: Opinion slugs are the docket number lower-case with an optional suffix: /supreme-court/2024/s-18521.html, /2023/s-18114.html, /2007/s-12164-1.html. The suffix is not predictable, so take the link from the year listing.
  - Index: `https://law.justia.com/cases/alaska/`
  - Navigation: /cases/alaska/{supreme-court|court-of-appeals}/ (year links are on the per-court page, not /cases/alaska/) → year listing → case link (docket shown); e.g. /cases/alaska/court-of-appeals/2025/a-13337.html
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answers 403 Cloudflare challenge
  - Year pages have no links to other years; the court index lists years.
- **Currency:** none stated
- **Official status:** Third-party republication; reporter cites shown where assigned.
- **Hazard:** slug suffix unpredictable
- **Hazard:** script route blocked
- **Hazard:** no official pagination
- **Hazard:** long opinions exceed the fetch-tool limit (Marino, A-13337: 116,385 chars, cut at 100K; use offset)
- **Probe:** West v. Municipality of Anchorage, 174 P.3d 224 (Alaska 2007) → `https://law.justia.com/cases/alaska/supreme-court/2007/s-12164-1.html` — expect: "A dog bit or pawed a seven-week-old baby, causing several"
- **Evidence (2026-10-17):** WebFetch: full text incl. dissent and footnote 44; '174 P.3d 224 (Alaska 2007)', docket S-12164. 2024 listing first rows s-18729 (Dec 18, 2024), s-18521; COA index 1980-2026. | Independent check 2026-10-17: YES: 'A dog bit or pawed a seven-week-old baby, causing several'; 174 P.3d 224 (Alaska 2007); second citation Marino v. State, No. A-13337, Op. No. 2814 (Alaska App. Aug. 22, 2025) ok

## F. Subsequent history

### `ak-subsequent-history-cms` — Petitions for hearing (Supreme Court review of Court of Appeals) in the Appellate CMS

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alaska Court System · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Each Court of Appeals docket page lists 'Related Appellate Cases'; the Supreme Court petition is the row whose Case Type is '302 Petition for Hearing' (the Relationship column may read 'Petition for Hearing' or 'Same Trial Court Number'). The S-case Case Summary shows only status (e.g. 'Closed', 'No Opinions'); the outcome appears on its Docket tab as a 'Disposition Order' entry, often without granted/denied wording, which may require the order document. Supreme Court published orders listing: /CMSPublic/Home/PublishedOrders?isCOA=False.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://appellate-records.courts.alaska.gov/CMSPublic/Search/CaseNumber?CaseNumber=A-{NNNNN}&TrialCourtNumber=`
  - Placeholders: Search the Court of Appeals case number by GET, open the Case/General link from the result, find the 'Related Appellate Cases' row with Case Type '302 Petition for Hearing' (do not rely on the Relationship column), follow its S-number link, then open the Docket tab (Case/Docket?q={token}) and read the 'Disposition Order' entry. Searching the A-number as TrialCourtNumber finds nothing; party search in the Supreme Court (CourtTypeString=SC) also finds the petition.
  - Index: `https://appellate-records.courts.alaska.gov/CMSPublic/`
  - Navigation: CaseNumber GET → Case/General?q={token} → Related Appellate Cases (Case Type '302 Petition for Hearing') → S-case → Docket tab → 'Disposition Order'
- **Automation:** WebFetch untested · shell ok · robots: appellate-records.courts.alaska.gov: robots.txt 404 (IIS 'File or directory not found')
  - US Supreme Court certiorari is not tracked here.
- **Currency:** docket status — observed: "Briefing Stage (S19597, opened 2025-11-04)"
- **Official status:** Court docket records.
- **Hazard:** docket tokens opaque
- **Hazard:** A-number not searchable as trial-court number
- **Hazard:** disposition shown only as 'Disposition Order' on the Docket tab, often without grant/deny wording
- **Hazard:** Relationship column unreliable (e.g. 'Same Trial Court Number')
- **Probe:** Marino v. State, No. A-13337 (Alaska App. Aug. 22, 2025) → S-19597 → `https://appellate-records.courts.alaska.gov/CMSPublic/Search/CaseNumber?CaseNumber=A-13337&TrialCourtNumber=` — expect: "A13337"
- **Evidence (2026-10-17):** Script: A-13337 search → Case/General page: Opinion 2814 Reverse/Remand 8/22/2025; Related Appellate Cases 'S19597 State of Alaska v. Gregory Marino 302 Petition for Hearing ... Briefing Stage'. Party search SC 'Marino' → S19597 opened 2025-11-04. TrialCourtNumber=A-13337 → no match. | Independent check 2026-10-17: Script: A-13337 docket 'Related Appellate Cases' → 'S19597 State of Alaska v. Gregory Marino 302 Petition for Hearing ... Briefing Stage'; second citation Baines v. State, No. A-13596 → S-18846 ok
- **Notes:** Appellate Rules 302-305 govern petitions for hearing.

## Not available (do not look for these again)

- **case_law** — Free official text of Alaska opinions after P.3d publication on courts.alaska.gov / Appellate CMS: Listing pages say documents are downloadable only until published in the Pacific Reporter; 87 Supreme Court rows show 'No Document Available'. Legacy courts.alaska.gov/ops/sp-7834.pdf → 404. (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions cite P.3d with '(Alaska YYYY)'; slip opinions carry only docket and opinion numbers (sp-7834: 'Supreme Court No. S-19268 ... No. 7834'). (2026-10-17)
- **statutes** — public.law edition of the Alaska Statutes: alaska.public.law: CONNECT tunnel 502 at the proxy. (2026-10-17)
- **statutes** — Official bulk download (XML/JSON) of the Alaska Statutes: None linked from akleg.gov/basis/start.asp; the nearest equivalent is the whole-title print URL (secStart=09&secEnd=09.99.999, 589,488 chars). (2026-10-17)
- **admin_register** — A current periodic Alaska administrative register: Lt. Governor regulations page routes notices to newspapers and the Online Public Notice System; the Alaska Administrative Journal PDFs are 1990s only; 'Register NNN' is the AAC supplement number. (2026-10-17)
- **statutes** — Fetchable (robots-permitted) official source for Session Laws of Alaska text: akleg.gov SLA PDFs sit under /pdf/billfiles/, disallowed by 'Disallow: /PDF/' (case-insensitive policy); no other tier-1 or tier-2 host for session-law text found. (2026-10-17)

## Corpus candidates (maintainers)

- `ak-rules-civil` — 150 pp, 955,507 chars; WebFetch stops in Rule 6
- `ak-rules-criminal` — 80 pp, 474,580 chars
- `ak-rules-evidence` — 26 pp, 159,059 chars; columns interleave in extraction
- `ak-rules-appellate` — 56 pp, 356,901 chars
- `ak-rules-administrative` — 72 pp, 493,151 chars
- `ak-constitution-ltgov` — HTML page is 105K chars (fetch-tool limit); the 64-page PDF is the stable official print
- `ak-statutes-akleg` — whole-title print pages (Title 9: 589,488 chars); per-section URLs make corpus optional · bulk: per-title print URL: statutes.asp?media=print&secStart={TT}&secEnd={TT}.99.999

## Open questions

- WebFetch was refused (PROVENANCE_REQUIRED) on built akleg print URLs, the ltgov constitution page and the CMS URLs; an independent verifier with URL permissions should retest WebFetch on ak-statutes-akleg, ak-aac-akleg, ak-constitution-ltgov and ak-opinions-cms.
- Does the Appellate CMS keep MO&J and summary-disposition PDFs longer than the three months the court page states (MO&J listing rows go back to 2022, many without documents)?
- Where the Supreme Court publishes orders denying petitions for hearing other than on the S-case docket page (PublishedOrders listing not inspected).
- Exact first year on Justia's Alaska Supreme Court index and whether a 2025 Justia statutes edition is complete.

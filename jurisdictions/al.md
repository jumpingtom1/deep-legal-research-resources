# Alabama (AL) — free legal sources

_Generated from `data/al.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Alabama's official hosts are open and scriptable. The Code of Alabama 1975 and the Constitution of 2022 live in the Legislature's ALISON JavaScript app, but its public GraphQL endpoint answers plain GET URLs with section text (script route; WebFetch gated on built URLs). Court rules are per-rule PDFs on judicial.alabama.gov with constructible names; the Administrative Code and Alabama Administrative Monthly are PDFs at admincode.legislature.state.al.us/api/... Opinions and certiorari dispositions come from the Appellate Courts public-portal JSON API (release lists → opinion PDFs, slip pagination only). Justia (WebFetch only; script refused by bot check) is the tier-2 fallback for code, constitution and opinions; LII for the Administrative Code.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Alabama | `ala (unverified)` | Ala. | So. 3d, So. 2d, So., Ala. | — |
| Alabama Court of Civil Appeals | `alacivapp (unverified)` | Ala. Civ. App. | So. 3d, So. 2d | — |
| Alabama Court of Criminal Appeals | `alacrimapp (unverified)` | Ala. Crim. App. | So. 3d, So. 2d | — |
| Alabama Court of Appeals (1911-1969) | `alactapp (unverified)` | Ala. Ct. App. | Ala. App., So. 2d, So. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Code of Alabama 1975 | `Ala. Code § 6-5-410`; `Ala. Code 1975, § 6-5-410`; `§ 6-5-410, Ala. Code 1975`; `§ 13A-6-2(a)(1), Ala. Code 1975`; `Code of Alabama 1975, § 6-2-38`; `Code of Ala. 1975, §22-22A-3`; `Section 40-1-1, Code of Alabama 1975`; `Ala. Code §§ 6-5-410 to -411`; `Ala. Code 1975 § 10A-2A-1.01`; `Section 6-5-410 of the Code of Alabama 1975` | `al-code-alison` → `al-code-justia` |
| Alabama Acts (session laws) | `Ala. Acts 2016, No. 2016-29`; `Act No. 2021-123, Ala. Acts`; `Ala. Act No. 2006-427` | `al-acts-alison` |
| Alabama act numbers (bare) *(only once this jurisdiction is known)* | `Act 2016-29`; `Act No. 2006-427` | `al-acts-alison` |
| Constitution of Alabama (2022 recompilation; 1901 numbering) | `Ala. Const. art. I, § 13`; `Ala. Const. 2022, § 13`; `Ala. Const. 1901, § 111.08`; `§ 13, Ala. Const. 1901`; `Article I, Section 13 of the Alabama Constitution`; `Section 13 of the Constitution of Alabama`; `Art. I, § 6, Ala. Const. 2022` | `al-constitution-alison` → `al-constitution-justia` |
| Alabama Rules of Civil, Criminal, Appellate, Juvenile Procedure, Evidence, Professional Conduct | `Ala. R. Civ. P. 12(b)(6)`; `Rule 12(b)(6), Ala. R. Civ. P.`; `Ala. R. Evid. 702`; `Rule 702(b), Ala. R. Evid.`; `Ala. R. App. P. 39`; `Rule 28(a)(10), Ala. R. App. P.`; `Ala. R. Crim. P. 32.1`; `Rule 32.2(c), Ala. R. Crim. P.`; `Ala. R. Prof'l Conduct 1.7`; `Rule 1.7, Ala. R. Prof. Cond.`; `Ala. R. Juv. P. 28`; `Alabama Rule of Civil Procedure 56`; `Rule 56(c) of the Alabama Rules of Civil Procedure` | `al-rules-judicial` |
| Alabama court rules (bare forms) *(only once this jurisdiction is known)* | `Rule 32 petition`; `Rule 39(a)(1)(D)` | `al-rules-judicial` |
| Alabama Administrative Code | `Ala. Admin. Code r. 335-6-1-.01`; `Ala. Admin. Code ch. 335-6-1`; `Ala. Admin. Code (ADEM) r. 335-6-1-.01`; `Rule 420-5-10-.01, Ala. Admin. Code`; `Ala. Admin. Code r. 30-X-1-.01`; `Ala. Admin. Code r. 220-2-.01` | `al-admincode-lsa` → `al-admincode-lii` |
| Alabama Administrative Code rule numbers (bare) *(only once this jurisdiction is known)* | `Rule 335-6-1-.01`; `r. 290-3-1-.01`; `Rule 220-2-.01` | `al-admincode-lsa` → `al-admincode-lii` |
| Alabama Administrative Monthly | `Ala. Admin. Monthly, Vol. XLIV, No. 11`; `Alabama Administrative Monthly, Volume XLIV, Issue No. 12` | `al-aam-lsa` |
| Alabama appellate docket numbers (2023- portal format) | `SC-2026-0199`; `No. SC-2025-0784`; `CL-2026-0261`; `CR-2025-0237` | `al-opinions-portal` → `al-cases-justia` |
| Alabama legacy docket numbers *(only once this jurisdiction is known)* | `No. 1200113`; `2011207`; `CR-18-0123` | `al-opinions-portal` → `al-cases-justia` |
| Alabama court parentheticals and Alabama Reports | `123 So. 3d 456 (Ala. 2013)`; `(Ala. Civ. App. 2021)`; `(Ala. Crim. App. 2020)`; `2021 WL 1234567, at *2 (Ala. Civ. App. Mar. 5, 2021)`; `290 Ala. 123`; `45 Ala. App. 300` | `al-opinions-portal` → `al-cases-justia` |
| Southern Reporter (regional, generic) *(only once this jurisdiction is known)* | `123 So. 3d 456`; `987 So. 2d 1` | `al-cases-justia` |
| Alabama certiorari history | `cert. denied (Ala. 2015)`; `cert. quashed, 123 So. 3d 456 (Ala. 2014)`; `writ denied (Ala. Mar. 4, 2022)`; `cert. denied, 987 So. 3d 12 (Ala. 2019)` | `al-cert-portal` |

Regexes (case-insensitive):

- Code of Alabama 1975: `Ala\.\s*Code(?:\s*(?:19)?75)?,?\s*(?:§§?|sec(?:tion|s?\.)s?)?\s*(?P<title>\d{1,2}[A-Z]?)-(?P<chapter>\d{1,3}[A-Z]?)-(?P<section>\d{1,4}(?:\.\d+)?)(?![\d])|Code\s+of\s+Ala(?:bama|\.)(?:,?\s*(?:19)?75)?,?\s*(?:§§?|sec(?:tion|s?\.)s?)?\s*(?P<title2>\d{1,2}[A-Z]?)-(?P<chapter2>\d{1,3}[A-Z]?)-(?P<section2>\d{1,4}(?:\.\d+)?)(?![\d])|(?:§§?|[Ss]ection)\s*(?P<title3>\d{1,2}[A-Z]?)-(?P<chapter3>\d{1,3}[A-Z]?)-(?P<section3>\d{1,4}(?:\.\d+)?)(?![\d])(?:\s*\([a-zA-Z0-9]+\))*,?\s*(?:Ala\.\s*Code|Code\s+of\s+Ala(?:bama|\.))|(?:§§?|[Ss]ection)\s*(?P<title4>\d{1,2}[A-Z]?)-(?P<chapter4>\d{1,3}[A-Z]?)-(?P<section4>\d{1,4}(?:\.\d+)?)(?![\d])(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:Code\s+of\s+Alabama|Alabama\s+Code)`
- Alabama Acts (session laws): `Ala\.\s*Acts?\s*(?:(?P<year>(?:18|19|20)\d\d),?\s*)?(?:Act\s+)?No\.\s*(?P<act>(?:19|20)\d\d-\d{1,4})|Act\s+No\.\s*(?P<act2>(?:19|20)\d\d-\d{1,4}),\s*Ala\.\s*Acts`
- Alabama act numbers (bare): `\bAct\s+(?:No\.\s*)?(?P<act>(?:19|20)\d\d-\d{1,4})\b`
- Constitution of Alabama (2022 recompilation; 1901 numbering): `Ala\.\s*Const\.(?:\s*(?:of\s*)?(?:1901|2022))?,?\s*(?:art\.\s*(?P<article>[IVXL]+),?\s*)?(?:§|sec\.|section)\s*(?P<section>\d{1,3}(?:\.\d{1,2})?)|(?:§|[Ss]ection)\s*(?P<section2>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-z0-9]+\))*,?\s*(?:of\s+the\s+)?(?:Ala\.\s*Const\.|Alabama\s+Constitution|Constitution\s+of\s+Alabama)|(?:Art\.|Article)\s*(?P<article3>[IVXL]+),?\s*(?:§|[Ss]ec\.|[Ss]ection)\s*(?P<section3>\d{1,3}(?:\.\d{1,2})?),?\s*(?:of\s+the\s+)?(?:Ala\.\s*Const\.|Alabama\s+Constitution|Constitution\s+of\s+Alabama)`
- Alabama Rules of Civil, Criminal, Appellate, Juvenile Procedure, Evidence, Professional Conduct: `Ala\.\s*R\.\s*(?P<set>Civ\.\s*P|Evid|App\.\s*P|Crim\.\s*P|Juv\.\s*P|Prof(?:'l|\.)\s*Cond(?:uct|\.)?|Jud\.\s*Admin|Small\s*Claims)\.?\s*(?P<rule>\d{1,4}(?:\.\d{1,2})?)|Rule\s+(?P<rule2>\d{1,4}(?:\.\d{1,2})?)(?:\s*\([a-zA-Z0-9]+\))*,\s*Ala\.\s*R\.\s*(?P<set2>Civ\.\s*P|Evid|App\.\s*P|Crim\.\s*P|Juv\.\s*P|Prof(?:'l|\.)\s*Cond(?:uct|\.)?|Jud\.\s*Admin|Small\s*Claims)|Alabama\s+Rules?\s+of\s+(?P<set3>Civil\s+Procedure|Evidence|Appellate\s+Procedure|Criminal\s+Procedure|Juvenile\s+Procedure|Professional\s+Conduct)\s*(?P<rule3>\d{1,4}(?:\.\d{1,2})?)|Rule\s+(?P<rule4>\d{1,4}(?:\.\d{1,2})?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Alabama\s+Rules\s+of\s+(?P<set4>Civil\s+Procedure|Evidence|Appellate\s+Procedure|Criminal\s+Procedure|Juvenile\s+Procedure|Professional\s+Conduct)`
- Alabama court rules (bare forms): `\bRule\s+32\s+petition|\bRule\s+(?P<rule>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-zA-Z0-9]+\))+`
- Alabama Administrative Code: `Ala\.\s*Admin\.\s*Code\s*(?:\([^)]{1,40}\)\s*)?(?:r\.|ch\.|rule|chapter)?\s*(?P<rule>\d{2,3}-[0-9X]{1,3}(?:-[0-9A-Z]{1,3})?(?:-\.\d{2}[A-Z]?)?)|(?:Rule|Chapter)\s+(?P<rule2>\d{2,3}-[0-9X]{1,3}(?:-[0-9A-Z]{1,3})?(?:-\.\d{2}[A-Z]?)?),\s*Ala\.\s*Admin\.\s*Code`
- Alabama Administrative Code rule numbers (bare): `\b(?:Rule|r\.)\s*(?P<rule>\d{2,3}-[0-9X]{1,3}(?:-[0-9A-Z]{1,3})?-\.\d{2}[A-Z]?)`
- Alabama Administrative Monthly: `(?:Ala\.\s*Admin\.\s*Monthly|Alabama\s+Administrative\s+Monthly),?\s*(?:Vol\.|Volume)\s*(?P<vol>[IVXL]+),?\s*(?:No\.|Issue\s+No\.)\s*(?P<issue>\d{1,2})`
- Alabama appellate docket numbers (2023- portal format): `\b(?P<docket>(?P<court>SC|CL|CR)-(?P<year>20\d\d)-(?P<num>\d{4}))\b`
- Alabama legacy docket numbers: `\b(?:No\.\s*)?(?P<docket>[12]\d{6}|CR-\d{2}-\d{3,4})\b`
- Alabama court parentheticals and Alabama Reports: `(?<!denied )(?<!quashed )(?<!granted )(?<!dismissed )(?<!denied, \d{1} So\. [23]d \d{1} )(?<!denied, \d{1} So\. [23]d \d{2} )(?<!denied, \d{1} So\. [23]d \d{3} )(?<!denied, \d{1} So\. [23]d \d{4} )(?<!denied, \d{1} So\. [23]d ___ )(?<!denied, \d{2} So\. [23]d \d{1} )(?<!denied, \d{2} So\. [23]d \d{2} )(?<!denied, \d{2} So\. [23]d \d{3} )(?<!denied, \d{2} So\. [23]d \d{4} )(?<!denied, \d{2} So\. [23]d ___ )(?<!denied, \d{3} So\. [23]d \d{1} )(?<!denied, \d{3} So\. [23]d \d{2} )(?<!denied, \d{3} So\. [23]d \d{3} )(?<!denied, \d{3} So\. [23]d \d{4} )(?<!denied, \d{3} So\. [23]d ___ )(?<!quashed, \d{1} So\. [23]d \d{1} )(?<!quashed, \d{1} So\. [23]d \d{2} )(?<!quashed, \d{1} So\. [23]d \d{3} )(?<!quashed, \d{1} So\. [23]d \d{4} )(?<!quashed, \d{1} So\. [23]d ___ )(?<!quashed, \d{2} So\. [23]d \d{1} )(?<!quashed, \d{2} So\. [23]d \d{2} )(?<!quashed, \d{2} So\. [23]d \d{3} )(?<!quashed, \d{2} So\. [23]d \d{4} )(?<!quashed, \d{2} So\. [23]d ___ )(?<!quashed, \d{3} So\. [23]d \d{1} )(?<!quashed, \d{3} So\. [23]d \d{2} )(?<!quashed, \d{3} So\. [23]d \d{3} )(?<!quashed, \d{3} So\. [23]d \d{4} )(?<!quashed, \d{3} So\. [23]d ___ )(?<!granted, \d{1} So\. [23]d \d{1} )(?<!granted, \d{1} So\. [23]d \d{2} )(?<!granted, \d{1} So\. [23]d \d{3} )(?<!granted, \d{1} So\. [23]d \d{4} )(?<!granted, \d{1} So\. [23]d ___ )(?<!granted, \d{2} So\. [23]d \d{1} )(?<!granted, \d{2} So\. [23]d \d{2} )(?<!granted, \d{2} So\. [23]d \d{3} )(?<!granted, \d{2} So\. [23]d \d{4} )(?<!granted, \d{2} So\. [23]d ___ )(?<!granted, \d{3} So\. [23]d \d{1} )(?<!granted, \d{3} So\. [23]d \d{2} )(?<!granted, \d{3} So\. [23]d \d{3} )(?<!granted, \d{3} So\. [23]d \d{4} )(?<!granted, \d{3} So\. [23]d ___ )(?<!dismissed, \d{1} So\. [23]d \d{1} )(?<!dismissed, \d{1} So\. [23]d \d{2} )(?<!dismissed, \d{1} So\. [23]d \d{3} )(?<!dismissed, \d{1} So\. [23]d \d{4} )(?<!dismissed, \d{1} So\. [23]d ___ )(?<!dismissed, \d{2} So\. [23]d \d{1} )(?<!dismissed, \d{2} So\. [23]d \d{2} )(?<!dismissed, \d{2} So\. [23]d \d{3} )(?<!dismissed, \d{2} So\. [23]d \d{4} )(?<!dismissed, \d{2} So\. [23]d ___ )(?<!dismissed, \d{3} So\. [23]d \d{1} )(?<!dismissed, \d{3} So\. [23]d \d{2} )(?<!dismissed, \d{3} So\. [23]d \d{3} )(?<!dismissed, \d{3} So\. [23]d \d{4} )(?<!dismissed, \d{3} So\. [23]d ___ )\((?P<court>Ala\.(?:\s*(?:Civ\.\s*App|Crim\.\s*App)\.)?)\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>(?:18|19|20)\d\d)\)|\b(?P<vol>\d{1,3})\s+Ala\.(?:\s*App\.)?\s+(?P<page>\d{1,4})\b`
- Southern Reporter (regional, generic): `\b(?P<vol>\d{1,3})\s+So\.\s*(?:2d|3d)?\s+(?P<page>\d{1,4})\b`
- Alabama certiorari history: `(?P<disp>cert\.\s*(?:denied|quashed|granted|dismissed)|writ\s+(?:denied|quashed)),?\s*(?:(?P<vol>\d{1,3})\s+So\.\s*(?:2d|3d)\s+(?P<page>\d{1,4}|_{2,5})\s*)?\(Ala\.\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>(?:19|20)\d\d)\)`

Short forms → URL key:

Ala. R. Civ. P. → `cv`; Ala. R. Evid. → `ev`; Ala. R. App. P. → `ap`; Ala. R. Crim. P. → `cr`; Ala. R. Juv. P. → `jv`; Ala. R. Prof'l Conduct → `cond`; Ala. R. Prof. Cond. → `cond`; Alabama Rules of Civil Procedure → `cv`; Alabama Rules of Evidence → `ev`; Alabama Rules of Appellate Procedure → `ap`; Alabama Rules of Criminal Procedure → `cr`; Alabama Rules of Juvenile Procedure → `jv`; Alabama Rules of Professional Conduct → `cond`

Statutes need no code key: the Code of Alabama 1975 is one code, sections title-chapter-section with letter suffixes (13A-6-2, 22-22A-3) and decimals (10A-2A-1.01). Alabama courts put the code name AFTER the section ('§ 6-5-410, Ala. Code 1975'); the regex's third branch requires that trailing 'Ala. Code'/'Code of Alabama'. Ranges ('§§ 6-5-410 to -411') capture only the first section. law_aliases map rule-set citation forms to the judicial.alabama.gov PDF prefix (cv, ev, ap, cr, jv, cond). Alabama courts likewise cite rules as 'Rule 12(b)(6), Ala. R. Civ. P.'. Bare 'Rule 32 petition', bare 'Rule N(x)', bare admin-rule numbers, bare 'Act 2016-29', legacy 7-digit dockets and regional So./So. 2d/So. 3d cites are context_required. Portal dockets SC-/CL-/CR-YYYY-NNNN are Alabama-specific (4-digit year + 4-digit number). Constitution: the Constitution of 2022 kept the 1901 section numbers and gave amendments decimal sections (111.08); old 'Amend. No. 328' cites do not map to a 2022 section without a lookup. Cert history: Alabama Supreme Court certiorari cases are captioned 'Ex parte <petitioner>'; 'cert. denied (Ala. ...)' routes to the release lists, and the court parenthetical has negative lookbehinds so it does not double-route. No public-domain citation format; unpublished Court of Civil/Criminal Appeals decisions are 'no-opinion' affirmances or unpublished memoranda (table cites in So. 3d). CourtListener ids from memory, unverified. Independent-check fixes 2026-10-17: prose 'Section 6-5-410 of the Code of Alabama 1975' added; admin-code regex accepts three-part rules (220-2-.01); the court-parenthetical branch carries fixed-width negative lookbehinds for 'denied/quashed/granted/dismissed, <vol> So. 2d|3d <page> ' (and '___'), so 'cert. denied, 987 So. 3d 12 (Ala. 2019)' routes only to certiorari history. Spacing variants ('So.3d') are not covered by the lookbehinds.

## A. Statutes / code

### `al-acts-alison` — Alabama Acts (enrolled bills, ALISON)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts linked to instruments in ALISON (2016 verified); older sessions untested.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://alison.legislature.state.al.us/graphql?query=%7Binstruments(where%3A%5B%7BactNbr%3A%7Beq%3A%22{act}%22%7D%7D%5D%2Climit%3A2)%7Bdata%7BactNbr%20instrumentNbr%20sessionYear%20enrolledFileUrl%7D%7D%7D`
  - Placeholders: {act} = 'YYYY-NNN' as cited (Act 2016-29). The JSON gives enrolledFileUrl, e.g. https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2016RS/PrintFiles/SB22-Enr.pdf; read that PDF.
  - Index: `https://alison.legislature.state.al.us/acts`
  - Navigation: GraphQL lookup by act number → enrolledFileUrl PDF
- **Automation:** WebFetch gated · shell ok · robots: none (robots.txt returns app HTML)
  - Acts page is a JavaScript app; use the GraphQL lookup.
- **Currency:** n/a (session law)
- **Official status:** Enrolled bill PDFs on the Legislature's site; no authentication statement.
- **Hazard:** enrolled-bill PDFs interleave line numbers with text
- **Hazard:** page numbers of the bound Acts volume not given
- **Hazard:** an act number may belong to a joint resolution: enrolledFileUrl can be an HJR/SJR PDF (2021-123 → HJR92-Enr.pdf)
- **Probe:** Act 2016-29 → `https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2016RS/PrintFiles/SB22-Enr.pdf` — expect: "SB22"
- **Evidence (2026-10-17):** GraphQL actNbr 2016-29 → SB22, Regular Session 2016, enrolledFileUrl .../2016RS/PrintFiles/SB22-Enr.pdf; script read: PDF 5 pp, starts '1 SB22 2 171578-3 3 By Senator Whatley'. | Independent check 2026-10-17: script grep SB22-Enr.pdf: 5 pp, '1 SB22 2 171578-3 3 By Senator Whatley'; second citation Act No. 2021-123, Ala. Acts ok
- **Notes:** Provenance: the code-of-alabama page config sets NEXT_PUBLIC_FE_GRAPHQL_URL = https://alison.legislature.state.al.us/graphql (publisher's own front-end endpoint, same host); robots.txt returns app HTML, no directives (independent check 2026-10-17).

### `al-code-alison` — Code of Alabama 1975 (ALISON, via its public GraphQL endpoint)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Legislature, Legislative Services Agency · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole Code of Alabama 1975, section text plus history notes; versions with future effective dates are kept (effectiveDate/supersessionDate fields).
- **Read via (in order):** **script**
- **Access:** `constructible` · format json
  - Pattern: `https://alison.legislature.state.al.us/graphql?query=%7BcodesOfAlabama(where%3A%7Btype%3A%7Beq%3ASection%7D%2CdisplayId%3A%7Beq%3A%22{section}%22%7D%7D)%7Bdata%7BdisplayId%20title%20effectiveDate%20supersessionDate%20content%20history%7D%7D%7D`
  - Placeholders: {section} = the full section number exactly as cited, e.g. 6-5-410, 13A-6-2, 22-22A-3, 10A-2A-1.01 (title letters upper-case). The URL is the URL-encoded GraphQL query {codesOfAlabama(where:{type:{eq:Section},displayId:{eq:"<section>"}}){data{displayId title effectiveDate supersessionDate content history}}}. Response is JSON; 'content' holds the text with subsection line breaks, 'history' the Acts list. Enclosing article/chapter and its section range: query {codesOfAlabama(where:{codeId:{in:["<parentId>"]}}){data{displayId title sectionRange parentId}}} using parentId from the section. The human page https://alison.legislature.state.al.us/code-of-alabama?section={section} is a JavaScript shell (no text to either tool). A nonexistent or mistyped section returns HTTP 200 with {"data":{"codesOfAlabama":{"data":[]}}} (39 chars), not a 404 or error: empty data[] means no such section (check the cite, or it may be repealed/renumbered). The parent node may be an Article, Part or Division (7-2-314's parent is 'Part 3'), not always an Article.
  - Index: `https://alison.legislature.state.al.us/graphql?query=%7Bscaffold%3A%20codeOfAlabamaScaffold%7D`
  - Navigation: Index nodes carry sectionRange (e.g. 'Article 23 Death.' §6-5-410 to §6-5-411). codeOfAlabamaScaffold returns the whole hierarchy (codeId/parentId/displayId, ~1.15M chars).
- **Automation:** WebFetch gated · shell ok · robots: none: /robots.txt returns the app's HTML page (200 text/html), no rules; fetch_doc.py check: robots permits
  - The site is a Next.js app (code-of-alabama page = 1,822 chars of navigation only). The GraphQL endpoint (NEXT_PUBLIC_FE_GRAPHQL_URL in the page config) accepts GET with ?query=. WebFetch of https://alison.legislature.state.al.us/code-of-alabama was refused by the URL-provenance gate (unanswered permission prompt); GraphQL URLs are built, so expect the same. Use the script.
- **Currency:** none stated (effectiveDate is null for in-force text)
- **Official status:** Served by the Legislature's site (meta: 'Official website of the Alabama Legislature ... access the Code and Constitution of Alabama'). No statement that the online Code text is official or authenticated was found; the app shell renders none.
- **Hazard:** JavaScript-only human pages
- **Hazard:** built GraphQL URLs are gated for WebFetch
- **Hazard:** sections with delayed amendments may return more than one version; check effectiveDate/supersessionDate
- **Hazard:** text is JSON-escaped (\n, \" ) - verify quotes against the decoded content
- **Hazard:** missing section = empty data[] with HTTP 200, no error
- **Probe:** Ala. Code § 6-5-410 → `https://alison.legislature.state.al.us/graphql?query=%7BcodesOfAlabama%28where%3A%7Btype%3A%7Beq%3ASection%7D%2CdisplayId%3A%7Beq%3A%226-5-410%22%7D%7D%29%7Bdata%7BdisplayId%20title%20effectiveDate%20content%20history%7D%7D%7D` — expect: "A personal representative may commence an action and recover such damages"
- **Evidence (2026-10-17):** fetch_doc.py read: JSON 2,018 chars, title 'Section 6-5-410 Wrongful Act, Omission, or Negligence Causing Death.', body (a)-(e). Second/third cites 13A-6-2 ('A person commits the crime of murder if') and 40-1-1, 6-2-38 also returned body + history. Article node: 'Article 23 Death.' sectionRange '§6-5-410 to §6-5-411'. | Independent check 2026-10-17: script: JSON 2,018 chars, '(a) A personal representative may commence an action and recover such damages'; second citation Ala. Code 1975, § 7-2-314 ok
- **Notes:** Script candidate: one GET per section, deterministic. The legacy alisondb.legislature.state.al.us/alison/CodeOfAlabama/1975/<section>.htm pages are unreachable (proxy 502 on the host). Provenance: the code-of-alabama page config sets NEXT_PUBLIC_FE_GRAPHQL_URL = https://alison.legislature.state.al.us/graphql (publisher's own front-end endpoint, same host); robots.txt returns app HTML, no directives (independent check 2026-10-17).

### `al-code-justia` — Code of Alabama (Justia)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual editions; current pages labelled '2025 Code of Alabama'; year archives /codes/alabama/{year}/ back to 2006 style URLs.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/alabama/title-{title}/chapter-{chapter}/article-{article}/section-{section}/`
  - Placeholders: Usual form https://law.justia.com/codes/alabama/title-{title}/chapter-{chapter}/article-{article}/section-{section}/ ({title}, {chapter}, {section} lower-case: 13a, 22a, 13a-6-2). {article} is not in the citation: take it from ALISON (parent node of the section). The hierarchy differs by title: Title 7 (UCC) is title-7/article-{chapter}/part-{part}/section-7-2-314/ (ALISON chapter = Justia 'article', ALISON parent 'Part N' = Justia part); /title-7/chapter-2/ errors. If a built URL fails, navigate from the title page.
  - Index: `https://law.justia.com/codes/alabama/`
  - Navigation: codes/alabama/title-N/ → follow the listed child (chapter-N, or for Title 7 article-N) → article-N or part-N (names only, no section ranges) → section-...
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com answers robots.txt with a bot check (fetch_doc.py REFUSED)
  - Built section URLs were not gated for WebFetch.
- **Currency:** page heading — observed: "2025 Code of Alabama"
- **Official status:** Page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** article number not derivable from citation
- **Hazard:** lags the Legislature's text by up to a year
- **Hazard:** built URL fails where the hierarchy differs: Title 7 uses title-7/article-2/part-3/section-7-2-314/ (independent check: second citation § 7-2-314 failed with the chapter/article pattern, reached via title-page navigation)
- **Probe:** Ala. Code § 6-5-410 → `https://law.justia.com/codes/alabama/title-6/chapter-5/article-23/section-6-5-410/` — expect: "A personal representative may commence an action and recover such damages"
- **Evidence (2026-10-17):** WebFetch: YES, body (a)-(f) + history, not truncated. Second cite title-13a/chapter-6/article-1/section-13a-6-2/: YES, '(a) A person commits the crime of murder if he', heading '2025 Code of Alabama'. | Independent check 2026-10-17: WebFetch YES: 'A personal representative may commence an action...'; '2025 Code of Alabama'; not truncated

## B. Constitution

### `al-constitution-alison` — Constitution of Alabama of 2022 (ALISON GraphQL)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Legislature, Legislative Services Agency · text: **fetch-and-quote** · official: unknown
- **Coverage:** Articles and sections of the 2022 recompiled Constitution (original 1901 section numbers; amendments as decimal sections, e.g. 3.01, 111.08).
- **Read via (in order):** **script**
- **Access:** `constructible` · format json
  - Pattern: `https://alison.legislature.state.al.us/graphql?query=%7BconstitutionItem(where%3A%7BisContentNode%3A%7Beq%3Atrue%7D%2CdisplayId%3A%7Beq%3A%22{section}%22%7D%7D)%7BdisplayId%20title%20content%20history%7D%7D`
  - Placeholders: {section} = section number only (13, 6.01, 111.08); the article is not part of the key. Article list with section ranges: query {constitutionTitles} (e.g. 'Article I Declaration of Rights §1 to §36.06').
  - Index: `https://alison.legislature.state.al.us/graphql?query=%7BconstitutionTitles%7D`
  - Navigation: constitutionTitles lists articles with sectionRange and every section title
- **Automation:** WebFetch gated · shell ok · robots: none (robots.txt returns app HTML)
  - Human page /law-sublanding is a JS app.
- **Currency:** none stated
- **Official status:** Legislature site; no authentication statement found.
- **Hazard:** built GraphQL URLs gated for WebFetch
- **Hazard:** 1901 'Amendment No. N' citations need a lookup to the 2022 section
- **Probe:** Ala. Const. art. I, § 13 → `https://alison.legislature.state.al.us/graphql?query=%7BconstitutionItem%28where%3A%7BisContentNode%3A%7Beq%3Atrue%7D%2CdisplayId%3A%7Beq%3A%2213%22%7D%7D%29%7BdisplayId%20title%20content%20history%7D%7D` — expect: "That all courts shall be open; and that every person, for any injury"
- **Evidence (2026-10-17):** Script: JSON 411 chars, 'Section 13 Courts to Be Open; Remedies for All Injuries...'. Second: 111.08 'Implementation Date of Laws Providing for Conduct of the General Election.' with body. | Independent check 2026-10-17: script: JSON 411 chars, 'That all courts shall be open; and that every person, for any injury'; second citation Ala. Const. art. I, § 6 ok
- **Notes:** Provenance: the code-of-alabama page config sets NEXT_PUBLIC_FE_GRAPHQL_URL = https://alison.legislature.state.al.us/graphql (publisher's own front-end endpoint, same host); robots.txt returns app HTML, no directives (independent check 2026-10-17).

### `al-constitution-justia` — Alabama Constitution (Justia)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Section-by-section text; version not labelled.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Section pages have opaque ids (Section 13 = CA-245544.html).
  - Index: `https://law.justia.com/constitution/alabama/`
  - Navigation: index (108K chars; WebFetch reads first 100K, use offset 100000 for the end) → 'Section N - ...' link → CA-NNNNNN.html
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: bot check on robots.txt
  - Index page truncated at 100K of 108K chars.
- **Currency:** none stated — observed: "This Constitution may not be the most recent version."
- **Official status:** Page note: 'This Constitution may not be the most recent version.' Version (1901 vs 2022) not stated.
- **Hazard:** opaque per-section ids
- **Hazard:** index truncation
- **Hazard:** version unlabelled (may be 1901 text)
- **Hazard:** 2022 decimal amendment sections (e.g. 111.08) not found in the Justia index; treat Justia text as 1901-era and do not use it for 2022-only sections
- **Probe:** Ala. Const. § 13 → `https://law.justia.com/constitution/alabama/CA-245544.html` — expect: "That all courts shall be open; and that every person,"
- **Evidence (2026-10-17):** WebFetch index: 'Alabama Constitution', Section 13 href CA-245544.html; section page YES, 'That all courts shall be open; and that every person,'. | Independent check 2026-10-17: WebFetch YES: 'That all courts shall be open; and that every person'; 'may not be the most recent version'; second citation Ala. Const. art. I, § 6 ok

## C. Court rules

### `al-rules-judicial` — Alabama Rules of Court (per-rule PDFs, Alabama Supreme Court Law Library)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Supreme Court / State Law Library (Alabama Judicial System) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of Civil, Criminal, Appellate, Juvenile Procedure, Evidence, Judicial Administration, Small Claims, Professional Conduct, Bar rules; committee comments and notes in each rule PDF.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://judicial.alabama.gov/docs/library/rules/{set}{rule}.pdf`
  - Placeholders: {set}: cv = Civ. P., ev = Evid., ap = App. P., cr = Crim. P., jv = Juv. P., cond = Prof'l Conduct (see law_aliases). {rule}: rule number with '.' → '_' (cv4_1, cr32_1, cond1_7, ev702, ap39). Case does not matter (index shows CV28.pdf; cv28.pdf works). Irregular names exist (crcr18.pdf, JA20B.pdf, JV33.pdf); if a built URL 404s, use the set page: fetch_doc.py links https://judicial.alabama.gov/library/{CivilProcedure|RulesEV|AppellateProcedure|CriminalProcedure|JuvenileProcedure|RulesBarConduct|RulesJudicialAdm}.
  - Index: `https://judicial.alabama.gov/library/rulesofcourt`
  - Navigation: rulesofcourt → rule-set page (e.g. /library/CivilProcedure) → 'Rule 12.' → docs/library/rules/cv12.pdf
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - Each rule PDF is short (Rule 12: 7 pp; App. P. 39: 19 pp), within WebFetch's window.
- **Currency:** bracketed amendment note after each rule's text — observed: "[Amended 10-14-76, eff. 1-16-77; ... Amended 11-28-2012.]"
- **Official status:** Published at judicial.alabama.gov/library/rulesofcourt; no official/unofficial statement in the PDFs.
- **Hazard:** irregular file names for some rules
- **Hazard:** no edition/currency date for the set; rule changes posted separately at /rules/index
- **Probe:** Ala. R. Civ. P. 12(b)(6) → `https://judicial.alabama.gov/docs/library/rules/cv12.pdf` — expect: "failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** Script verify exact on cv12.pdf (7 pp). Built URLs ev702 (Evidence, 6 pp), cond1_7 (Prof. Conduct), cr32_1 ('Rule 32. Post-conviction remedies.'), ap39, cv28 all returned rule text. WebFetch cv12.pdf: YES, 'A defendant shall serve an answer within thirty (30) days'. | Independent check 2026-10-17: script verify exact cv12.pdf; WebFetch YES, '[Amended 10-14-76, eff. 1-16-77; ... Amended 11-28-2012.]'; second citation Ala. R. Civ. P. 56; Ala. R. Evid. 403 ok
- **Notes:** No tier-2 copy: Justia and LII do not host Alabama court rules.

## D. Administrative code

### `al-admincode-lsa` — Alabama Administrative Code (rule and chapter PDFs)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Legislative Services Agency, Administrative Procedure Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current rules by agency/chapter/rule, with Author, Statutory Authority and History notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://admincode.legislature.state.al.us/api/rule/{rule}`
  - Placeholders: {rule} as cited, e.g. 335-6-1-.01. Whole chapter: https://admincode.legislature.state.al.us/api/chapter/{chapter} (335-6-1). Both return a PDF (filename 'Rule 335-6-1-.01.pdf'). HTTP 404 = no such rule/chapter (482-1-1 and 810-3-1-.01 404'd). Three-part rule numbers exist (Conservation: 220-2-.01) and work the same way.
  - Index: `https://admincode.legislature.state.al.us/`
  - Navigation: Human site is a JavaScript app; its GraphQL API (/api/graphql) is persisted-query only (error 'PersistedQueryOnly'), so there is no tool-readable index: build the rule URL.
- **Automation:** WebFetch gated · shell ok · robots: none (robots.txt returns app HTML)
  - Script is the primary route. WebFetch read /api/chapter/335-1-A only because it came from a search result; WebFetch of built rule URLs was refused (PROVENANCE_REQUIRED, independent check).
- **Currency:** History note at end of each rule; page footers on some chapters — observed: "Revised 4/14/24 (chapter 335-1-A footer)"
- **Official status:** Published by the LSA (the Code's compiler) at admincode.legislature.state.al.us; no authentication statement seen in the PDFs.
- **Hazard:** no browsable index for tools
- **Hazard:** chapter PDFs can be long
- **Probe:** Ala. Admin. Code r. 335-6-1-.01 → `https://admincode.legislature.state.al.us/api/rule/335-6-1-.01` — expect: "Code of Ala. 1975, §§22-22-1 to 22-22-14"
- **Evidence (2026-10-17):** Script: PDF 2 pp, 'ALABAMA DEPARTMENT OF ENVIRONMENTAL MANAGEMENT WATER DIVISION', definitions + 'Author: David Ludder Statutory Authority'. Second: r. 420-5-10-.01 (7 pp) and 290-3-1-.01; chapter 335-6-1 (8 pp). | Independent check 2026-10-17: script verify exact: 'Code of Ala. 1975, §§22-22-1 to 22-22-14' (2 pp PDF); second citation Ala. Admin. Code r. 810-6-1-.01; also r. 540-X-1-.01, r. 220-2-.01 ok
- **Notes:** Provenance: admincode index.html sets NX_PUBLIC_API_URL '/api' (same origin); the bundle builds API_URL+'graphql' and AAM print links API_URL+'aam/'+id; rule/chapter PDFs come from GraphQL fileUrl fields; robots.txt returns app HTML, no directives (independent check 2026-10-17).

### `al-admincode-lii` — Alabama Administrative Code (Cornell LII)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rule-by-rule HTML with Notes (amendment history).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/alabama/Ala-Admin-Code-r-{rule}`
  - Placeholders: {rule} as cited, e.g. 335-6-1-.01.
  - Index: `https://www.law.cornell.edu/regulations/alabama`
- **Automation:** WebFetch untested · shell ok · robots: robots permits; crawl-delay 10
- **Currency:** Notes section (amendment dates) — observed: "Ala. Admin. Code r. 335-6-1-.01 Amended: October 10, 1984."
- **Official status:** Third-party republication.
- **Hazard:** may lag the LSA text; compare History notes before quoting
- **Hazard:** crawl-delay 10 s
- **Hazard:** no 404 for a nonexistent rule: LII returns a 200 page without rule text (810-5-1-.01, 8,621 chars); confirm the heading names the rule
- **Probe:** Ala. Admin. Code r. 335-6-1-.01 → `https://www.law.cornell.edu/regulations/alabama/Ala-Admin-Code-r-335-6-1-.01` — expect: ""AWPCA" means the Alabama Water Pollution Control Act"
- **Evidence (2026-10-17):** Script grep: definitions (a),(b) present; Notes 'Amended: October 10, 1984'. Second: r. 420-5-10-.01 18,012 chars. | Independent check 2026-10-17: script grep: 'meanings set forth in the AWPCA "waters," "pollution,"'; second citation Ala. Admin. Code r. 810-6-1-.01 ok

## D. Administrative register

### `al-aam-lsa` — Alabama Administrative Monthly

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Legislative Services Agency · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly issues (notices of intended action, certified rules). Current issues via /api/aam/YYYY-MM; older issues (c. 2007-2017) as HTML/PDF under file.admincode.legislature.state.al.us/UpdatedMonthly/AAM-MON-YY/.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://admincode.legislature.state.al.us/api/aam/{yyyy}-{mm}`
  - Placeholders: {yyyy}-{mm} is the issue month. Volume year runs October-September: Issue No. 1 = October, so Issue No. N → month ((N+8) mod 12)+1 (No. 6 = March, No. 11 = August, No. 12 = September). Vol. XLIV = Oct 2025 - Sep 2026 (2026-08 returned 'VOLUME XLIV, ISSUE NO. 11 August 31, 2026').
  - Index: `https://admincode.legislature.state.al.us/`
- **Automation:** WebFetch untested · shell ok · robots: none (robots.txt returns app HTML); file.admincode host robots permits
  - Issues run ~100-120K chars: beyond a single WebFetch window; use the script.
- **Currency:** cover page — observed: "VOLUME XLIV, ISSUE NO. 11 August 31, 2026"
- **Official status:** LSA publication; no authentication statement seen.
- **Hazard:** long PDFs (65 pp)
- **Hazard:** URL key is the calendar month; issue No. 1 = October
- **Probe:** Ala. Admin. Monthly, Vol. XLIV, No. 11 → `https://admincode.legislature.state.al.us/api/aam/2026-08` — expect: "ALABAMA Administrative Monthly"
- **Evidence (2026-10-17):** Script: PDF 65 pp, 119,551 chars, filename Volume_XLIV_Issue_No_11.pdf; 'NOTICE OF INTENDED ACTION' entries found. 2026-09: 60 pp. Legacy AAM-FEB-16 .htm: 8,547 chars. | Independent check 2026-10-17: script: 'ALABAMA Administrative Monthly VOLUME XLIV, ISSUE NO. 11 August 31, 2026'; second citation Ala. Admin. Monthly, Vol. XLIV, No. 6 ok
- **Notes:** Provenance: admincode index.html sets NX_PUBLIC_API_URL '/api' (same origin); the bundle builds API_URL+'graphql' and AAM print links API_URL+'aam/'+id; rule/chapter PDFs come from GraphQL fileUrl fields; robots.txt returns app HTML, no directives (independent check 2026-10-17).

## E. Case law

### `al-opinions-portal` — Alabama Appellate Courts Public Portal (release lists and opinion PDFs, JSON API)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Appellate Courts · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court, Court of Civil Appeals, Court of Criminal Appeals release lists from May 2023 (SC: 155+ lists); dockets searchable back to at least 2002 (e.g. 2011207, 1200113).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://publicportal-api.alappeals.gov/courts/{courtUUID}/cms/case/{caseInstanceUUID}/docketentrydocuments/{documentLinkUUID}`
  - Placeholders: courtUUID: Supreme Court 68f021c4-6a44-4735-9a76-5360b2e8af13; Civil Appeals 1da1a297-c391-4e4f-9480-1bc68b46f21a; Criminal Appeals b82b30d5-bd3c-46d7-9451-1cb05e470873. (1) Release lists: https://publicportal-api.alappeals.gov/courts/cms/publications?courtID={courtUUID}&page=0&size=10&sort=publicationDate,desc (page is 0-based) → publicationUUID. (2) List detail: https://publicportal-api.alappeals.gov/courts/{courtUUID}/cms/publication/{publicationUUID} → JSON key publicationItems: each with caseNumber, caseInstanceUUID, decision, title and documents[{documentName:'Opinion', documentLinkUUID}]. (3) Opinion PDF: url_pattern. Docket lookup: https://publicportal-api.alappeals.gov/courts/{courtUUID}/cms/cases/search?caseNumber={docket} (or /courts/cms/cases?caseHeader.caseNumber={docket}) → caseInstanceUUID; docket entries: /courts/{courtUUID}/cms/cases/{caseInstanceUUID}/docketentries?size=100.
  - Index: `https://publicportal.alappeals.gov/`
  - Navigation: court + date → release list for that Friday → item by docket → Opinion documentLinkUUID → PDF
- **Automation:** WebFetch gated · shell ok · robots: publicportal.alappeals.gov: robots.txt returns app HTML (no rules); publicportal-api.alappeals.gov: 404 JSON (no rules)
  - The portal UI is a JavaScript app (apiRoot in /properties.js). The portal's own search URL exceeded WebFetch's URL length limit (proxy 403); API URLs were provenance-gated for WebFetch.
- **Currency:** release list name/date and 'Rel:' line on each opinion — observed: "Supreme Court Release List - October 16, 2026"
- **Official status:** Linked from judicial.alabama.gov court pages as 'Decisions and Opinions Released After May 19, 2023'. Opinions carry the notice that they are subject to formal revision before publication in Southern Reporter.
- **Hazard:** slip pagination only (no So. 3d pages)
- **Hazard:** opinions subject to revision before So. 3d publication
- **Hazard:** no-opinion affirmances have no document
- **Hazard:** several dockets can share one opinion document
- **Hazard:** 'Affirmed by Unpublished Memorandum' and no-opinion items have documents []; rehearing items carry a 'Rehearing Notice', not an 'Opinion'
- **Hazard:** caseInstanceUUID comes back lower-case from case search, upper-case in release lists; the PDF route accepts either
- **Probe:** Lima One Capital, LLC v. City of Birmingham, No. SC-2026-0199 (Ala. Aug. 21, 2026) → `https://publicportal-api.alappeals.gov/courts/68f021c4-6a44-4735-9a76-5360b2e8af13/cms/case/C2B8B5A5-02D9-4286-977F-CF92A8EB87D1/docketentrydocuments/38D82535-7B20-4740-83E4-8EAD9218FDC7` — expect: "In early 2025, the City of Birmingham ("the City") determined that"
- **Evidence (2026-10-17):** Script: Opinion.pdf 14 pp, 'Rel: August 21, 2026 ... SUPREME COURT OF ALABAMA ... SC-2026-0199'. Civil Appeals CL-2026-0261 opinion from CL-RELEASE-2026-10-16: 16 pp. Criminal Appeals list CR-RELEASE-2026-10-16 read (7 items). caseNumber search returned SC-2026-0199 and SC-2022-0474. | Independent check 2026-10-17: script: Opinion.pdf 14 pp, 'COOK, Justice. In early 2025, the City of Birmingham ("the City")'; second citation Ex parte Shaun Michael Davis, No. CR-2026-0250 (Ala. Crim. App. Oct. 9, 2026) ok
- **Notes:** Provenance: https://publicportal.alappeals.gov/properties.js sets apiRoot 'https://publicportal-api.alappeals.gov' (publisher's own front end, linked from judicial.alabama.gov); API robots.txt 404 = no rules (independent check 2026-10-17).

### `al-releases-legacy` — Decisions released 2020 - May 19, 2023 (judicial.alabama.gov release-list PDFs on acis.alabama.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Appellate Courts · text: **link-only** · official: official
- **Coverage:** Weekly 'Decisions on Friday ...' lists Jan 3, 2020 - May 19, 2023 (Supreme Court; civildecisions and criminaldecisions pages for the two intermediate courts). Lists only: opinions themselves are fetched via the portal docket lookup.
- **Access:** `index-anchored` · format pdf
  - Placeholders: List links are acis.alabama.gov/displaydocs2.cfm?no=NNNNN&event=XXXXXXXXX (opaque).
  - Index: `https://judicial.alabama.gov/decision/supremecourtdecisions`
  - Navigation: fetch_doc.py links on /decision/supremecourtdecisions (or /decision/civildecisions, /decision/criminaldecisions) → 'Decisions on Friday, <date>' → displaydocs2.cfm PDF list → docket → portal caseNumber search
- **Automation:** WebFetch untested · shell ok · robots: judicial.alabama.gov none (404); acis.alabama.gov robots permits
  - Index page is 255K chars; use fetch_doc.py links, not WebFetch.
- **Currency:** list heading — observed: "DECISIONS ANNOUNCED ON FRIDAY, MAY 19, 2023"
- **Official status:** Court's own release lists.
- **Hazard:** opaque document ids
- **Hazard:** lists only, no opinion text
- **Probe:** Supreme Court release list, May 19, 2023 → `https://acis.alabama.gov/displaydocs2.cfm?no=10613&event=6MD0V6TYR` — expect: "SUPREME COURT OF ALABAMA DECISIONS ANNOUNCED ON FRIDAY, MAY 19, 2023"
- **Evidence (2026-10-17):** Script: 151 displaydocs links on the index (Jan 3, 2020 - May 19, 2023); May 19, 2023 PDF 4 pp listing '2022-0474 Debbie Berry v. PHH Mortgage Corporation ... Affirmed.' | Independent check 2026-10-17: script: 'SUPREME COURT OF ALABAMA DECISIONS ANNOUNCED ON FRIDAY, MAY 19, 2023'; second citation Court of Civil Appeals release list, May 12, 2023 ok

### `al-cases-justia` — Alabama appellate opinions (Justia)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court; Court of Civil Appeals; Court of Criminal Appeals (1933-2026 listed); old Court of Appeals. Opinions only (no no-opinion affirmances).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/alabama/{court}/{year}/{docket}.html`
  - Placeholders: {court}: supreme-court, court-of-appeals-civil, court-of-appeals-criminal, court-of-appeals. {docket} lower-case, but multi-docket opinions use one of the dockets (not always the first) and may add '-0' (sc-2025-0242-0.html): locate from the year listing.
  - Index: `https://law.justia.com/cases/alabama/`
  - Navigation: cases/alabama/ → court → year listing (name, dockets, date) → opinion page; PDF at cases.justia.com/alabama/{court}/{year}-{docket}.pdf
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt
  - WebFetch failed (CLIENT_ERROR) on /court-of-civil-appeals/2026/ and /court-of-criminal-appeals/2026/ — wrong slugs; correct slugs come from the cases/alabama/ index.
- **Currency:** year listing — observed: "September 25, 2026 (latest Supreme Court listing entry)"
- **Official status:** Third-party republication of slip opinions.
- **Hazard:** slip pagination only
- **Hazard:** lags the portal by weeks
- **Hazard:** multi-docket file names
- **Probe:** Bauman v. Gentle, No. SC-2026-0563 (Ala. Sept. 25, 2026) → `https://law.justia.com/cases/alabama/supreme-court/2026/sc-2026-0563.html` — expect: "In this wrongful-death case, Adam Bauman and Beth Bauman, as"
- **Evidence (2026-10-17):** WebFetch: 2026 Supreme Court listing (3 latest entries); opinion page YES, not truncated, slip pages 1-10, PDF link cases.justia.com/alabama/supreme-court/2026-sc-2026-0563.pdf. Court of Criminal Appeals index: years 1933-2026, latest cr-2023-0282.html (Aug. 21, 2026). | Independent check 2026-10-17: WebFetch YES: 'In this wrongful-death case, Adam Bauman and Beth Bauman, as'; slip pages; not truncated; second citation DeMike v. Littrell, No. CL-2025-1072 (Ala. Civ. App. Sept. 18, 2026) ok

## F. Subsequent history

### `al-cert-portal` — Certiorari and rehearing dispositions (Supreme Court release lists, public portal API)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Alabama Appellate Courts · text: **fetch-and-quote** · official: official
- **Coverage:** Every Supreme Court disposition incl. 'Certiorari Pre Examination Decision - Writ Denied. No Opinion.', 'Petition/Writ Quashed', rehearing overruled; May 2023 on (portal), 2020-2023 (legacy PDFs).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format json
  - Pattern: `https://publicportal-api.alappeals.gov/courts/68f021c4-6a44-4735-9a76-5360b2e8af13/cms/publication/{publicationUUID}`
  - Placeholders: Find lists with https://publicportal-api.alappeals.gov/courts/cms/publications?courtID=68f021c4-6a44-4735-9a76-5360b2e8af13&page=0&size=10&sort=publicationDate,desc. Each cert item's title names the lower case: 'Ex parte N.V. PETITION FOR WRIT OF CERTIORARI TO THE COURT OF ... (In re: ...; Civil Appeals: CL-2022-0762)'. The cert proceeding has its own SC- docket; no tested API filter goes from the lower docket to the cert docket. Items are under the JSON key publicationItems.
  - Index: `https://publicportal.alappeals.gov/`
  - Navigation: From a CL-/CR- decision: scan Supreme Court release lists after the decision date for its docket in item titles, or search the portal by party name ('Ex parte <petitioner>') → SC- docket → caseNumber search → docket entries.
- **Automation:** WebFetch gated · shell ok · robots: none (404 JSON)
- **Currency:** publicationName — observed: "Supreme Court Release List - September 11, 2026"
- **Official status:** Court's release lists.
- **Hazard:** lower-docket → cert-docket link only via item titles or party name
- **Probe:** Ex parte N.V., No. SC-2026-0671 (Ala. Sept. 11, 2026) (writ denied) → `https://publicportal-api.alappeals.gov/courts/68f021c4-6a44-4735-9a76-5360b2e8af13/cms/publication/6db2874a-e0d8-432d-9722-a560c91d73b4` — expect: "Certiorari Pre Examination Decision - Writ Denied. No Opinion."
- **Evidence (2026-10-17):** Script: SC-RELEASE-2026-09-11 JSON lists SC-2026-0461, -0671, -0564 etc. 'Certiorari Pre Examination Decision - Writ Denied. No Opinion.' each with an Order documentLinkUUID. | Independent check 2026-10-17: script: SC-2026-0461 'Certiorari Pre Examination Decision - Writ Denied. No Opinion.'; second citation Ex parte City of Gulf Shores, No. SC-2026-0718 (Ala. Oct. 9, 2026) (writ denied; CR-2025-0826) ok
- **Notes:** Cert grants are decided by opinion under captions 'Ex parte <name>' (In re: <lower case>); cite form 'cert. denied, ___ So. 3d ___ (Ala. 2021)'. Provenance: https://publicportal.alappeals.gov/properties.js sets apiRoot 'https://publicportal-api.alappeals.gov' (publisher's own front end, linked from judicial.alabama.gov); API robots.txt 404 = no rules (independent check 2026-10-17).

## Not available (do not look for these again)

- **statutes** — Legacy ALISON static Code pages (alisondb.legislature.state.al.us/alison/CodeOfAlabama/1975/*.htm): Proxy 502 'Tunnel connection failed' on robots.txt and host, twice on 2026-10-17; the new ALISON app replaced them. (2026-10-17)
- **statutes** — Official authentication statement / currency line for the online Code: None in the ALISON page payload or GraphQL fields (effectiveDate null for in-force text). (2026-10-17)
- **court_rules** — Tier-2 copy of Alabama court rules: Not on Justia or LII (none found). (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions identified by docket (SC-2026-0199) and So. 3d cites only. (2026-10-17)
- **case_law** — Free official reporter pagination: Portal and Justia opinions carry slip pagination; So. 3d page numbers not given. (2026-10-17)
- **statutes** — public.law edition of the Code of Alabama: alabama.public.law: proxy 502 on robots.txt (2 tries); not tested further. (2026-10-17)

## Corpus candidates (maintainers)

- `al-aam-lsa` — Monthly issues are 100-120K chars, past one WebFetch window; low priority (register, not a rule set).

## Open questions

- Is the ALISON online Code official? No statement found; the printed Code of Alabama 1975 (Thomson Reuters) is the commonly cited edition.
- Admin Code GraphQL is persisted-query only; no tool-readable agency/chapter index was found. Look for a static index (or LII's index) to map agency names to numbers.
- Portal API: is there a filter from originating (lower-court) docket to the Supreme Court cert docket? Not found in the bundle's route list.
- WebFetch access to the GraphQL and portal-API URLs depends on per-URL approval; untested with approval.
- Pre-2020 opinions: portal docket search finds 2002+ cases; whether opinion PDFs are attached for pre-2023 dockets was not tested.
- Justia Code hierarchy differs by title (Title 7 uses article/part); other titles with Parts/Divisions not mapped. Navigate from the title page when a built URL fails.

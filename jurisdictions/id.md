# Idaho (ID) — free legal sources

_Generated from `data/id.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and Constitution: legislature.idaho.gov serves one HTML page per section, constructible from the citation (chapter = section digits minus the last two, or the middle number in three-part UPC/UCC sections), current through the 2026 session; Justia 2025 is the tier-2 fallback. Court rules: isc.idaho.gov serves every I.R.C.P./I.A.R./I.R.E./I.C.R. rule on its own constructible print page; full-set pages are 120K-420K characters and truncate in the fetch tool. IDAPA rules and the Administrative Bulletin are chapter/issue PDFs at constructible adminrules.idaho.gov URLs that redirect to files.dfm.idaho.gov (the fetch tool will not follow that redirect; the script does); Cornell LII mirrors IDAPA per section. Case law: the new isc.idaho.gov site is a JavaScript app, but its public GET JSON API (/api/cms-content-search, /api/cms-document) finds Supreme Court (late 2019 on) and Court of Appeals (2013-16, 2020 on) opinions by docket or party and links slip PDFs the script reads; Justia covers 1866 on; old isc.idaho.gov opinion URLs now 404; iCourt is behind a Cloudflare challenge.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Idaho Supreme Court | `idaho (unverified)` | Idaho | Idaho, P.3d, P.2d, P. | — |
| Idaho Court of Appeals | `idahoctapp (unverified)` | Idaho Ct. App. | Idaho, P.3d, P.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Idaho Code | `Idaho Code § 5-219`; `I.C. § 5-219(4)`; `Idaho Code Ann. § 18-4001`; `I.C. § 15-2-101`; `section 5-219, Idaho Code`; `Idaho Code section 67-5279`; `I.C. §§ 5-216 to 5-219`; `Idaho Code § 63-3022A`; `chapter 16, title 6, Idaho Code` | `id-statutes-leg` → `id-statutes-justia` |
| Idaho Session Laws | `2025 Idaho Sess. Laws ch. 1`; `1971 Idaho Sess. Laws 845`; `am. 1971, ch. 180, sec. 1, p. 845` | `id-session-laws` |
| Idaho Constitution | `Idaho Const. art. I, § 13`; `Idaho Const. art. V, sec. 9`; `Article I, Section 22 of the Idaho Constitution`; `Art. I, § 17, Idaho Constitution` | `id-constitution-leg` → `id-constitution-justia` |
| Idaho court rules (I.R.C.P., I.A.R., I.R.E., I.C.R., I.C.A.R., I.R.F.L.P., I.M.C.R., I.J.R., I.I.R., I.R.E.F.S.) | `I.R.C.P. 56(c)`; `IRCP 12(b)(6)`; `Idaho R. Civ. P. 56`; `I.A.R. 118`; `I.R.E. 702`; `Idaho R. Evid. 403`; `I.C.R. 35`; `I.C.R. 33.1`; `Idaho Crim. R. 11`; `I.C.A.R. 32`; `I.R.F.L.P. 101`; `Rule 56 of the Idaho Rules of Civil Procedure`; `Idaho Appellate Rule 11(a)`; `Idaho Criminal Rule 35(b)`; `Idaho Rule of Evidence 404(b)`; `Idaho Rules of Civil Procedure 56` | `id-rules-isc` |
| Idaho Rules of Professional Conduct | `I.R.P.C. 1.7`; `IRPC 8.4(c)`; `Idaho Rule of Professional Conduct 1.15`; `Rule 1.7 of the Idaho Rules of Professional Conduct` | `id-rules-irpc` |
| IDAPA (Idaho Administrative Code) | `IDAPA 16.03.09.010`; `IDAPA 58.01.02`; `Idaho Admin. Code r. 58.01.02.001`; `IDAPA 58.01.02.250.02` | `id-idapa-dfm` → `id-idapa-lii` |
| Idaho Administrative Bulletin | `Idaho Admin. Bull. Vol. 26-10`; `Idaho Administrative Bulletin, Vol. 25-1, p. 45`; `Vol. 26-10 Idaho Admin. Bull.` | `id-bulletin-dfm` |
| Reported Idaho cases (Idaho Reports / Pacific Reporter) | `State v. Dorff, 171 Idaho 818, 526 P.3d 988 (2023)`; `172 Idaho 825, 537 P.3d 66 (2023)`; `State v. Doe, 140 Idaho 271, 92 P.3d 521 (Ct. App. 2004)`; `526 P.3d 988 (Idaho 2023)`; `92 P.3d 521 (Idaho Ct. App. 2004)` | `id-opinions-isc-api` → `id-cases-justia` |
| Unpublished / slip opinions by docket number | `State v. Cowell, Docket No. 53548 (Idaho Ct. App. Oct. 16, 2026) (unpublished)`; `Docket No. 53539`; `No. 46085-2018`; `2024 WL 123456 (Idaho Ct. App. Jan. 5, 2024)` | `id-opinions-isc-api` → `id-cases-justia` |

Regexes (case-insensitive):

- Idaho Code: `(?:Idaho\s+Code(?:\s+Ann\.)?|I\.\s?C\.)\s*(?:§§?|sec(?:tion|s?\.)?)?\s*(?P<title>\d{1,2})-(?:(?P<chapter3>\d{1,2})-(?P<section3>\d{3,4}[A-Z]{0,2})|(?P<section>\d{3,4}[A-Z]{0,2}))(?!\d)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?:(?P<chapter3b>\d{1,2})-(?P<section3b>\d{3,4}[A-Z]{0,2})|(?P<section2>\d{3,4}[A-Z]{0,2}))(?!\d)(?:\([0-9a-z]+\))*,?\s+(?:of\s+the\s+)?Idaho\s+Code|chapter\s+(?P<chapter4>\d{1,3}[A-Z]?),\s*title\s+(?P<title4>\d{1,2}),\s*Idaho\s+Code`
- Idaho Session Laws: `(?P<year>(?:18|19|20)\d\d)\s+Idaho\s+Sess\.\s*Laws(?:\s+ch\.\s*(?P<chapter>\d+)|\s+(?P<page>\d+))|am\.\s+(?P<year2>(?:18|19|20)\d\d),\s*ch\.\s*(?P<chapter2>\d+)`
- Idaho Constitution: `Idaho\s+Const\.?\s*art\.\s*(?P<article>[IVXL]+),?\s*(?:§|sec\.?)\s*(?P<section>\d+[A-Za-z]?)|Art(?:icle|\.)\s+(?P<article2>[IVXL]+),?\s+(?:Section|sec\.?|§)\s*(?P<section2>\d+[A-Za-z]?),?\s+(?:of\s+the\s+)?Idaho\s+Constitution`
- Idaho court rules (I.R.C.P., I.A.R., I.R.E., I.C.R., I.C.A.R., I.R.F.L.P., I.M.C.R., I.J.R., I.I.R., I.R.E.F.S.): `(?P<set>I\.?\s?R\.?\s?C\.?\s?P\.?|I\.?\s?A\.?\s?R\.?|I\.?\s?R\.?\s?E\.?(?!F)|I\.?\s?C\.?\s?R\.?|I\.?\s?C\.?\s?A\.?\s?R\.?|I\.?\s?R\.?\s?F\.?\s?L\.?\s?P\.?|I\.?\s?M\.?\s?C\.?\s?R\.?|I\.?\s?J\.?\s?R\.?|I\.?\s?I\.?\s?R\.?|I\.?\s?R\.?\s?E\.?\s?F\.?\s?S\.?|Idaho\s+R\.\s*(?:Civ\.\s*P|Evid|App\.\s*P|Crim\.\s*P)\.|Idaho\s+Crim\.\s*R\.|Idaho\s+(?:Appellate|Criminal|Evidence|Civil\s+Procedure)\s+Rule|Idaho\s+Rules?\s+of\s+(?:Evidence|Civil\s+Procedure|Criminal\s+Procedure|Appellate\s+Procedure)(?:\s+Rule)?)\s*(?P<rule>\d{1,4}(?:\.\d+)?)(?![\d.]\d)|Rule\s+(?P<rule2>\d{1,4}(?:\.\d+)?)(?:\([0-9a-zA-Z]+\))*\s+of\s+the\s+Idaho\s+(?P<setname>Rules\s+of\s+Civil\s+Procedure|Appellate\s+Rules|Rules\s+of\s+Evidence|Criminal\s+Rules|Court\s+Administrative\s+Rules|Rules\s+of\s+Family\s+Law\s+Procedure)`
- Idaho Rules of Professional Conduct: `(?:I\.?\s?R\.?\s?P\.?\s?C\.?|Idaho\s+Rules?\s+of\s+Professional\s+Conduct)\s*(?:Rule\s+)?(?P<rule>\d\.\d{1,2})|Rule\s+(?P<rule2>\d\.\d{1,2})(?:\([a-z0-9]+\))*\s+of\s+the\s+Idaho\s+Rules\s+of\s+Professional\s+Conduct`
- IDAPA (Idaho Administrative Code): `(?:IDAPA|Idaho\s+Admin\.\s*Code\s+r\.)\s*(?P<agency>\d{2})\.(?P<title>\d{2})\.(?P<chapter>\d{2})(?:\.(?P<section>\d{3}))?(?:\.(?P<subsection>\d{2}))?`
- Idaho Administrative Bulletin: `(?:Idaho\s+Admin(?:\.|istrative)\s*Bull(?:\.|etin),?\s*Vol\.\s*(?P<yy>\d{2})-(?P<issue>\d{1,2})|Vol\.\s*(?P<yy2>\d{2})-(?P<issue2>\d{1,2}),?\s+Idaho\s+Admin\.\s*Bull\.)(?:,?\s*p\.\s*(?P<page>\d+))?`
- Reported Idaho cases (Idaho Reports / Pacific Reporter): `(?P<idvol>\d{1,3})\s+Idaho\s+(?P<idpage>\d{1,4})(?:,\s*\d+)?(?:,\s*(?P<pvol>\d{1,4})\s+P\.(?:\s*[23]d)?\s+(?P<ppage>\d{1,5}))?|(?P<pvol2>\d{1,4})\s+P\.(?:\s*[23]d)?\s+(?P<ppage2>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Idaho(?:\s+Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Unpublished / slip opinions by docket number: `(?:Docket\s+)?No\.\s*(?P<docket>\d{5})(?:-(?P<year>(?:19|20)\d\d))?|(?P<wlyear>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)[^()]{0,30}\(Idaho`

Short forms → URL key:

I.R.C.P. → `ircp`; IRCP → `ircp`; Idaho R. Civ. P. → `ircp`; Idaho Rules of Civil Procedure → `ircp`; I.A.R. → `iar`; IAR → `iar`; Idaho App. R. → `iar`; Idaho Appellate Rules → `iar`; I.R.E. → `ire`; IRE → `ire`; Idaho R. Evid. → `ire`; Idaho Rules of Evidence → `ire`; I.C.R. → `icr`; ICR → `icr`; Idaho Crim. R. → `icr`; Idaho R. Crim. P. → `icr`; Idaho Criminal Rules → `icr`; I.C.A.R. → `icar`; ICAR → `icar`; Idaho Court Administrative Rules → `icar`; I.R.F.L.P. → `irfl`; IRFLP → `irfl`; Idaho Rules of Family Law Procedure → `irfl`; I.M.C.R. → `imcr`; I.J.R. → `ijr`; I.I.R. → `iir`; I.R.E.F.S. → `irefs`; I.R.S.C.A. → `irsca`; I.R.T.C. → `irtc`; Idaho R. App. P. → `iar`; Idaho Rule of Evidence → `ire`

Idaho Code sections are cited 'Idaho Code § 5-219', 'I.C. § 5-219' (Idaho courts' own style) or 'section 5-219, Idaho Code' (statutory cross-reference style); Bluebook uses 'Idaho Code Ann. § 5-219'. Two-part sections (title-NNNN[A]) encode the chapter as the digits before the last two (5-219 → ch. 2; 18-4001 → ch. 40; 67-5279 → ch. 52; 63-3022A → ch. 30); three-part sections in uniform-act titles (15 UPC, 28 UCC, 30 business entities, etc.) give the chapter in the middle (15-2-101 → ch. 2). The regex reads '§§ 5-216 to 5-219' as its first section and never reads a hyphenated range as a three-part section (three-part needs a 1-2 digit middle and 3-4 digit tail). Guards: bare 'I.C.' is routed only when followed by § or a T-NNN section number; bare 'Rule 56', 'Evidence Rule 702' or 'Criminal Rule 35' without an Idaho marker must not route here; 'I.R.E.' and 'I.C.R.' collide with other states' informal abbreviations, so route on them only with Idaho context. Rule-set aliases map to the isc.idaho.gov print-page slug in law_aliases. Unpublished Court of Appeals opinions are marked 'THIS IS AN UNPUBLISHED OPINION AND SHALL NOT BE CITED AS AUTHORITY' and are cited by docket number and date. Idaho has no public-domain citation; reporter cites are Idaho Reports (West) parallel with P./P.2d/P.3d, with '(Ct. App. YYYY)' for the Court of Appeals in Idaho style. Docket numbers are five digits, sometimes with a filing-year suffix ('46085-2018'); a granted petition for review moves the case to a NEW Supreme Court docket number (46085-2018 → 48109-2020). CourtListener ids 'idaho' and 'idahoctapp' are from memory and unverified. Interstate: Idaho shares the Snake River boundary with Oregon; no compact surfaced during probing. Chapter-form cites ('chapter 16, title 6, Idaho Code') route to the chapter index /Title6/T6CH16/. 'Fed. R. Evid. 702' and bare 'Evidence Rule 702' must not route here (verified: no match).

## A. Statutes / code

### `id-session-laws` — Idaho Session Laws (annual volumes)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** PDF volumes 1945-2025; split vol1/vol2 from 1993 and also in some earlier years (1969, 1971, 1972, 1974 at least); current-session acts via /sessioninfo/{year}/legislation/.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://legislature.idaho.gov/statutesrules/sessionlaws/`
  - Navigation: Always take the exact href from the index: files are /wp-content/uploads/sessionlaws/sessionlaws_vol{1|2}_{year}.pdf or sessionlaws_{year}.pdf, and the split is not limited to 1993+ (sessionlaws_1971.pdf is HTTP 404; the 1971 volumes are vol1/vol2). Choose the volume from the index's chapter-range labels (2025: Vol 1 ch. 1-162, Vol 2 ch. 163-330) or, for a page cite ('1971, ch. 180, p. 845'), by comparing the page with vol 1's page count; then grep 'CHAPTER {n}' with fetch_doc.py.
- **Automation:** WebFetch gated · shell ok · robots: as id-statutes-leg
  - Volumes are huge (2025 vol 1: 779 pp, 2.7M chars) — script grep only; the fetch tool would see a tiny fraction.
- **Currency:** index page — observed: "latest volume listed: sessionlaws_vol1_2025.pdf / vol2_2025.pdf"
- **Official status:** Site Disclaimer: official copies of Session Laws are published for the Legislature by Custom Printing.
- **Hazard:** very large PDFs
- **Hazard:** split vol1/vol2 in some pre-1993 years: the plain sessionlaws_{year}.pdf pattern 404s — navigate from the index
- **Hazard:** older volumes are OCR scans ('H. IJ. No. 7'), so exact greps can miss; grep short phrases or regexes
- **Probe:** 2025 Idaho Sess. Laws ch. 1 → `https://legislature.idaho.gov/wp-content/uploads/sessionlaws/sessionlaws_vol1_2025.pdf` — expect: "CHAPTER 1"
- **Evidence (2026-10-16):** Script: application/pdf 779 pp, last-modified 3 Jul 2025; grep found '2025 IDAHO SESSION LAWS 3 CHAPTER 1 (H.B. No. 3)' on p. 3. | Independent check 2026-10-16: Script: vol1_2025 779 pp, p.3 'CHAPTER 1 (H.B. No. 3) AN ACT RELATING TO TAXATION'; second citation 1971 Idaho Sess. Laws ch. 180 (p. 845) ok

### `id-statutes-leg` — Idaho Statutes (Idaho Code)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Legislature, Legislative Services Office · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles of the Idaho Code, one HTML page per section with history note; per-chapter PDF downloads.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://legislature.idaho.gov/statutesrules/idstat/Title{title}/T{title}CH{chapter}/SECT{title}-{section}/`
  - Placeholders: title and chapter unpadded integers. Two-part section 'T-NNNN[A]': chapter = section digits without the last two (5-219 → T5CH2/SECT5-219; 18-4001 → T18CH40/SECT18-4001; 67-5279 → T67CH52/SECT67-5279; 63-3022A → T63CH30/SECT63-3022A). Three-part section 'T-C-NNN': chapter = middle number, section kept whole (15-2-101 → Title15/T15CH2/SECT15-2-101; 28-9-109 → Title28/T28CH9/SECT28-9-109). Letter suffix upper-case (SECT5-214A). Path is case-insensitive (search engines index the lower-case form title5/t5ch2/sect5-219/). A wrong chapter or non-existent section returns HTTP 404 ('not found'), so a bad guess is detectable; then use the chapter index, which lists every section number and catchline.
  - Index: `https://legislature.idaho.gov/statutesrules/idstat/`
  - Navigation: Fallback when the chapter cannot be inferred: /statutesrules/idstat/Title{title}/ lists chapters (titles only, NO section ranges) → /Title{title}/T{title}CH{chapter}/ lists every section with catchline → SECT page holds text.
- **Automation:** WebFetch gated · shell ok · robots: 200; User-agent * disallows only /wp-admin/ and committee-calendar paths; Semrushbot disallowed entirely
  - Primary route for constructed URLs: the script (fetch_doc.py). gated: hand-built URLs refused with PROVENANCE_REQUIRED; ok only for URLs from a WebSearch/WebFetch result (verifier: 5-219 and 6-1603 both refused). Section pages are 4-21K characters, so no truncation.
- **Currency:** Section pages carry only the update-policy banner ('updated to the website July 1 following the legislative session'); the 'current through' string is only on https://legislature.idaho.gov/statutesrules/howcurrentisthislaw/ — observed: "Idaho Statutes and Constitutions are current through the 2026 Legislative Session."
- **Official status:** Site Disclaimer (https://legislature.idaho.gov/site-disclaimer/) says official copies of the Idaho Code are published for the Idaho Code Commission by LEXIS Publishing; no UELMA authentication statement on section pages.
- **Hazard:** chapter must be derived from the section number (two-part vs three-part forms)
- **Hazard:** web text updated only July 1 after each session: mid-year amendments with emergency clauses are not shown
- **Hazard:** fetch tool may refuse constructed URLs (provenance) — use the script route or a search-result URL
- **Probe:** Idaho Code § 5-219 → `https://legislature.idaho.gov/statutesrules/idstat/Title5/T5CH2/SECT5-219/` — expect: "An action against a sheriff, coroner"
- **Evidence (2026-10-16):** WebFetch (search-result URL /title5/t5ch2/sect5-219/): YES, 'Within two (2) years: An action against a sheriff, coroner'; not truncated. WebFetch /title18/t18ch40/sect18-4001/: YES 'Murder is the unlawful killing of a human being including'. Script: 5-219 (6,981 chars), 18-4001, 5-214A, 67-5279, 15-2-101, 28-9-109, 63-3022A all body present; T5CH3/SECT5-219 → 404. | Independent check 2026-10-16: Script: 'Within two (2) years: 1. An action against a sheriff, coroner'; WebFetch: PROVENANCE_REQUIRED; second citation Idaho Code § 6-1603; Idaho Code § 28-2-302 ok
- **Notes:** Per-chapter PDF: https://legislature.idaho.gov/wp-content/uploads/statutesrules/idstat/Title{title}/T{title}CH{chapter}.pdf (T5CH2.pdf: 13 pp, last-modified 15 Sep 2025, script OK). No whole-code bulk XML/JSON found.

### `id-statutes-justia` — Justia — Idaho Code (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Idaho Code editions incl. 2013-2025; unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/idaho/title-{title}/chapter-{chapter}/section-{title}-{section}/`
  - Placeholders: Same title/chapter derivation as id-statutes-leg; section lower-case incl. letter suffix (section-5-214a). Insert /{year}/ after /idaho/ for an edition (e.g. /codes/idaho/2021/title-5/chapter-2/). Title pages list chapters without section ranges.
  - Index: `https://law.justia.com/codes/idaho/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: could not read: robots.txt answers with a Cloudflare challenge
  - fetch_doc.py: 'law.justia.com answers robots.txt with a bot check (challenge); automated access refused.' Use WebFetch only.
- **Currency:** page header and Universal Citation line — observed: "2025 Idaho Code; 'ID Code § 5-219 (2025)'"
- **Official status:** Pages state 'These codes may not be the most recent version.'
- **Hazard:** edition lags official text by a session
- **Hazard:** shell blocked by Cloudflare
- **Probe:** Idaho Code § 5-219 → `https://law.justia.com/codes/idaho/title-5/chapter-2/section-5-219/` — expect: "ACTIONS AGAINST OFFICERS, FOR PENALTIES, ON BONDS"
- **Evidence (2026-10-16):** WebFetch: YES body present; 'ID Code § 5-219 (2025)'; chain /codes/idaho/2025 → /title-5/ ('2025 Idaho Code', no section ranges) → /chapter-2/ (section-5-214a, section-5-219 hrefs). | Independent check 2026-10-16: WebFetch: title line present; body 'Within two (2) years: An action against a sheriff, coroner'; '2025 Idaho Code'; second citation Idaho Code § 6-1603 ok

## B. Constitution

### `id-constitution-leg` — Idaho Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full constitution, one page per section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://legislature.idaho.gov/statutesrules/idconst/Art{article_roman}/Sect{section}/`
  - Placeholders: article as upper-case Roman numeral (ArtI, ArtV, ArtXXI); section unpadded integer. Path case-insensitive. Article index /idconst/Art{roman}/ lists sections.
  - Index: `https://legislature.idaho.gov/statutesrules/idconst/`
- **Automation:** WebFetch gated · shell ok · robots: as id-statutes-leg
  - Primary route: the script. gated: hand-built URLs refused with PROVENANCE_REQUIRED; ok only for URLs from a WebSearch/WebFetch result (ArtI/Sect22 got through for the verifier). Script normalises to a trailing slash (…/Sect22/).
- **Currency:** Constitution section pages carry only the update-policy banner ('The Idaho Constitution is updated to the website July 1 following the legislative session'); the 'current through' string is only on https://legislature.idaho.gov/statutesrules/howcurrentisthislaw/ — observed: "Idaho Statutes and Constitutions are current through the 2026 Legislative Session."
- **Official status:** Same site disclaimer as id-statutes-leg; no authentication statement.
- **Probe:** Idaho Const. art. I, § 22 → `https://legislature.idaho.gov/statutesrules/idconst/ArtI/Sect22` — expect: "Rights of crime victims. A crime victim, as"
- **Evidence (2026-10-16):** WebFetch ArtI/Sect22: YES 'Section 22. Rights of crime victims. A crime victim, as'; not truncated. Script ArtI/Sect13 ('the party accused shall have the right to a speedy and public trial') and ArtV/Sect9 OK. | Independent check 2026-10-16: WebFetch YES 'Section 22. Rights of crime victims. A crime victim, as'; script ok; second citation Idaho Const. art. IX, § 1 ok

### `id-constitution-justia` — Justia — Idaho Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/idaho/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article lower-case Roman (article-i); section unpadded.
  - Index: `https://law.justia.com/constitution/idaho/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge on robots.txt
  - WebFetch only.
- **Currency:** page notice — observed: "This Constitution may not be the most recent version."
- **Official status:** Page: 'This Constitution may not be the most recent version.'
- **Hazard:** shell blocked by Cloudflare
- **Probe:** Idaho Const. art. I, § 22 → `https://law.justia.com/constitution/idaho/article-i/section-22/` — expect: "A crime victim, as defined by statute, has the following"
- **Evidence (2026-10-16):** WebFetch: YES 'A crime victim, as defined by statute, has the following'. | Independent check 2026-10-16: WebFetch YES 'A crime victim, as defined by statute, has the following'; 'may not be the most recent version'; second citation Idaho Const. art. IX, § 1 ok

## C. Court rules

### `id-rules-irpc` — Idaho Rules of Professional Conduct

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho State Bar · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole IRPC with comments in one PDF.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://isb.idaho.gov/bar-counsel/irpc/`
  - Navigation: Index page links one PDF: https://isb.idaho.gov/wp-content/uploads/IRPC-acc.pdf. Grep with fetch_doc.py using a regex such as '^RULE\s+8\.4\b' (escape the dot; headings vary: 'RULE 1.7: CONFLICT OF INTEREST' vs 'RULE 8.4 MISCONDUCT' with no colon) and take matches past the table of contents (page > 2), or grep a body phrase.
- **Automation:** WebFetch untested · shell ok · robots: 200; Yoast block, User-agent * Disallow: (nothing)
  - 67 pp, 544,451 chars — far beyond the fetch tool's ~100K window.
- **Currency:** none stated in PDF; HTTP last-modified only — observed: "last-modified Mon, 09 Mar 2026"
- **Official status:** Bar-published PDF; no authentication statement found.
- **Hazard:** two-column layout: extracted text interleaves table-of-contents columns
- **Hazard:** length beyond fetch tool window
- **Hazard:** headings inconsistent (colon after the rule number or not); the full-title grep hits only the table of contents because two-column extraction splits body headings
- **Probe:** I.R.P.C. 1.7 → `https://isb.idaho.gov/wp-content/uploads/IRPC-acc.pdf` — expect: "RULE 1.7: CONFLICT OF INTEREST"
- **Evidence (2026-10-16):** Script: application/pdf 67 pp; grep 'RULE 1.7: CONFLICT OF INTEREST: CURRENT' found (31 matches incl. body on p. 15). | Independent check 2026-10-16: Script: PDF 67 pp; 'RULE 1.7: CONFLICT OF INTEREST' on p.15 (body), plus TOC; index links IRPC-acc.pdf (WebFetch); second citation I.R.P.C. 8.4(c) ok

### `id-rules-isc` — Idaho Court Rules (I.R.C.P., I.A.R., I.R.E., I.C.R., I.C.A.R., I.R.F.L.P. and others)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rule sets: iar, icar, icr, iir, ijr, imcr, ircp, ire, irefs, irfl, irsca, irtc.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://isc.idaho.gov/rules-procedure/print/{set}/{rule}`
  - Placeholders: set = law_aliases slug (ircp, iar, ire, icr, icar, irfl, imcr, ijr, iir, irefs, irsca, irtc); rule = number as cited incl. decimal (icr/33.1, iar/11.1); subsection dropped (I.R.C.P. 56(c) → print/ircp/56). Non-existent rule → HTTP 404 (icr/11.1). Full set on one page: https://isc.idaho.gov/rules-procedure/{set}#rule-{rule} (anchors id='rule-56'). Legacy short URLs like isc.idaho.gov/ire702 301 to the full-set page.
  - Index: `https://isc.idaho.gov/rules-procedure`
- **Automation:** WebFetch gated · shell ok · robots: 200; disallows /admin, /cdn-cgi/, /isc-network/, /__preview, /api/cms-page-preview
  - Primary route for constructed URLs: the script. gated: hand-built URLs refused with PROVENANCE_REQUIRED; ok only for URLs from a WebSearch/WebFetch result (print/ircp/56 and ire/702 worked; print/icr/11 was refused for the verifier). Per-rule print pages are usually small but can be large (icar/32: 45,991 chars). Full-set pages: ircp 417,681 chars, icr 263,642, iar 232,420, ire 127,721; WebFetch on /ire702 stopped at ~100K in Rule 703.
- **Currency:** adoption/amendment note at end of each rule — observed: "(Adopted March 26, 2018, effective July 1, 2018.) [I.R.E. 702]"
- **Official status:** No official/unofficial statement on rule pages; each rule carries its adoption/amendment history and orders are linked as PDFs.
- **Hazard:** full-set pages truncate in the fetch tool
- **Hazard:** old isc.idaho.gov rule URLs (printpdf/NNN) now 404
- **Probe:** I.R.C.P. 56(a) → `https://isc.idaho.gov/rules-procedure/print/ircp/56` — expect: "A party may move for summary judgment, identifying each claim"
- **Evidence (2026-10-16):** WebFetch print/ircp/56: YES, '(Adopted March 1, 2016, effective July 1, 2016'; print/ire/702: YES 'A witness who is qualified as an expert by knowledge,'. Script OK: iar/118, icr/35, icr/33.1, iar/11, ircp/12. | Independent check 2026-10-16: WebFetch YES 'A party may move for summary judgment, identifying each claim'; '(Adopted March 1, 2016, effective July 1, 2016).'; second citation I.C.R. 11; I.R.F.L.P. 101; I.C.A.R. 32 ok
- **Notes:** I.A.R. 118 governs petitions for review of Court of Appeals decisions.

## D. Administrative code

### `id-idapa-dfm` — IDAPA — Idaho Administrative Rules (current chapters)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Office of the Administrative Rules Coordinator, Division of Financial Management · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current rule chapters as PDFs; annual archives back to 1996 (rules/{year} Archive/...).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://adminrules.idaho.gov/rules/current/{agency}/{agency}{title}{chapter}.pdf`
  - Placeholders: IDAPA AA.TT.CC[.SSS] → /rules/current/AA/AATTCC.pdf (58.01.02 → /rules/current/58/580102.pdf). The URL 301-redirects to https://files.dfm.idaho.gov/dfm-admin-website/rules/current/AA/AATTCC.pdf. Archive years: /rules/{YYYY}%20Archive/AA/AATTCC.pdf (2021, 2025 verified). Section SSS is a heading inside the PDF ('010. DEFINITIONS.'), grep it. A 404 means the chapter number is not current — IDAPA 16 (Health and Welfare) chapters were renumbered (16.03.09, 16.03.10 → 404; 16.03.01 OK). Find a section by grepping its number heading with fetch_doc.py, regex '^\s*{SSS}\.\s' (headings may carry a '(RULE n)' suffix, e.g. '001. TITLE AND SCOPE (RULE 1).'); do not rely on title wording such as 'These rules are titled', which not every chapter uses.
  - Index: `https://adminrules.idaho.gov/current-rules/`
- **Automation:** WebFetch fail · shell ok · robots: none (404 on adminrules.idaho.gov and files.dfm.idaho.gov)
  - WebFetch does not follow the cross-host redirect to files.dfm.idaho.gov and was refused the files.dfm URL (PROVENANCE_REQUIRED). The current-rules listing is filled by a POST-only, nonce-protected WP REST call (/wp-json/dfm-document-display/fetch-documents); on 2026-10-16 the site showed a banner about a technical issue with document search and listings. WebFetch on /rules/current/58 returned a listing without links while the shell got 404 — treat agency index pages as unreliable.
- **Currency:** each section ends with its effective-date stamp, e.g. '(3-31-22)'; HTTP last-modified — observed: "58.01.02 PDF last-modified Thu, 30 Jul 2026"
- **Official status:** No official-status statement found on adminrules.idaho.gov current-rules page.
- **Hazard:** cross-host redirect to files.dfm.idaho.gov
- **Hazard:** long PDFs (58.01.02: 181 pp, 713,747 chars)
- **Hazard:** IDAPA 16 renumbering makes older chapter cites 404
- **Hazard:** listing pages JavaScript/POST-only
- **Probe:** IDAPA 58.01.02 → `https://adminrules.idaho.gov/rules/current/58/580102.pdf` — expect: "These rules are titled IDAPA 58.01.02"
- **Evidence (2026-10-16):** Script: 301 → files.dfm.idaho.gov/.../580102.pdf, 181 pp; '001. TITLE AND SCOPE. 01. Title. These rules are titled IDAPA 58.01.02'. 16/160301.pdf 20 pp OK. WebFetch on adminrules bulletin URL: '302 Found' redirect not followed. | Independent check 2026-10-16: Script: 301→files.dfm; p.5 'These rules are titled IDAPA 58.01.02, “Water Quality Standards.”'; second citation IDAPA 31.01.01.001 ok
- **Notes:** Cumulative index and History Notes pages exist on adminrules.idaho.gov.

### `id-idapa-lii` — Cornell LII — Idaho Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages for IDAPA titles.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/idaho/IDAPA-{agency}.{title}.{chapter}.{section}`
  - Placeholders: IDAPA 58.01.02.001 → /regulations/idaho/IDAPA-58.01.02.001 (two-digit groups, three-digit section). Chapter listing: /regulations/idaho/title-IDAPA-{agency}/rule-{agency}.{title}.{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/idaho`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 10 (per DE record); Idaho regulation paths permitted
- **Currency:** page note — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party compilation; 'State regulations are updated quarterly'.
- **Hazard:** lag behind official chapter (58.01.02.001 last-modified 1 Aug 2025)
- **Hazard:** IDAPA 58.01.08.900 returned NOT PRESENT (section may not exist) — confirm numbers on the chapter listing
- **Probe:** IDAPA 59.01.01.001 → `https://www.law.cornell.edu/regulations/idaho/IDAPA-59.01.01.001` — expect: "Sections 50-1507, 50-1508, 50-1524, 59-1301"
- **Evidence (2026-10-16):** WebFetch: YES body present; chapter page rule-58.01.02 lists IDAPA-58.01.02.001 / .010 hrefs. Script: IDAPA-58.01.02.001 200, 2,865 chars, title-and-scope text present. | Independent check 2026-10-16: WebFetch YES 'Sections 50-1507, 50-1508, 50-1524, 59-1301'; 'updated quarterly'; second citation IDAPA 31.01.01.001 ok

## D. Administrative register

### `id-bulletin-dfm` — Idaho Administrative Bulletin

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Office of the Administrative Rules Coordinator, Division of Financial Management · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly issues; archives on adminrules.idaho.gov (2003 and 2018 issues indexed by search engines).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://adminrules.idaho.gov/bulletin/{year}/{month:02d}.pdf`
  - Placeholders: Vol. YY-M → /bulletin/20YY/MM.pdf (Vol. 26-10 → /bulletin/2026/10.pdf). Redirects (301/302) to https://files.dfm.idaho.gov/dfm-admin-website/bulletin/{year}/{MM}.pdf.
  - Index: `https://adminrules.idaho.gov/latest-bulletins/`
- **Automation:** WebFetch fail · shell ok · robots: none (404)
  - WebFetch stopped at the redirect ('302 Found') and was refused the files.dfm URL (PROVENANCE_REQUIRED). Issues are huge (Vol. 26-10: 428 pp, 1.88M chars) — script grep only.
- **Currency:** cover page — observed: "October 7, 2026 – Vol. 26-10"
- **Official status:** Cover: published monthly by the Office of the Administrative Rules Coordinator; no authentication statement.
- **Hazard:** cross-host redirect
- **Hazard:** very long PDFs
- **Probe:** Idaho Admin. Bull. Vol. 26-10 → `https://adminrules.idaho.gov/bulletin/2026/10.pdf` — expect: "IDAHO ADMINISTRATIVE BULLETIN October 7, 2026 – Vol. 26-10"
- **Evidence (2026-10-16):** Script: 301 → files.dfm.idaho.gov, application/pdf 428 pp, last-modified 7 Oct 2026; cover 'October 7, 2026 – Vol. 26-10'. 2026/09 and 2025/01 also 301 to files.dfm. | Independent check 2026-10-16: Script: 301→files.dfm, 428 pp, 'October 7, 2026 – Vol. 26-10'; second citation Idaho Admin. Bull. Vol. 24-3 ok

## E. Case law

### `id-icourt` — Idaho iCourt Portal (case search / dockets)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Idaho Judicial Branch (Tyler Odyssey) · text: **link-only** · official: unknown
- **Coverage:** Trial and appellate case registers.
- **Access:** `link-only` · format html
  - Index: `https://icourt.idaho.gov/`
- **Automation:** WebFetch untested · shell blocked-challenge · robots: robots.txt itself returns HTTP 403 Cloudflare 'Just a moment...' challenge
  - fetch_doc.py: 'icourt.idaho.gov answers robots.txt with a bot check (challenge); automated access refused.' Link for humans only.
- **Currency:** n/a — observed: "n/a"
- **Official status:** not reachable
- **Hazard:** Cloudflare managed challenge
- **Probe:**  → `https://icourt.idaho.gov/robots.txt`
- **Evidence (2026-10-16):** HTTP 403, cf challenge page 'Just a moment...' on robots.txt and /. | Independent check 2026-10-16: not re-reached — WebFetch refused on provenance before any request, so the block was not re-observed.

### `id-opinions-isc-api` — Idaho Supreme Court and Court of Appeals opinions (isc.idaho.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Supreme Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Slip-opinion PDFs. Supreme Court ('ISC Opinion'): earliest entry 2019-09-11 (2018 tag holds petition-for-review orders), full years 2020-2026. Court of Appeals ('ICA Opinion', incl. unpublished and per curiam): 2013-2016 and 2020-2026; 2017-2019 essentially absent (2017: 1 record; 2018-2019: 0).
- **Read via (in order):** **script**
- **Access:** `constructible` · format json
  - Pattern: `https://isc.idaho.gov/api/cms-content-search?scope=documents&document_type={ISC%20Opinion|ICA%20Opinion}&q={docket_or_party}&limit=20`
  - Placeholders: Plain GET JSON. q matches docket number (result 'name' = docket, e.g. '53539' or '50045.pdf') and party names in the summary ('Dorff' → 48119). Optional tag={year}, sort_by=entry_date&sort_direction=DESC|ASC, cursor={nextCursor}. Then GET https://isc.idaho.gov/api/cms-document?id={id} → content[0].content.opinion_file.value.url = https://api.isc.idaho.gov/uploads/Documents/{ISC|ICA}/{Category}/{year}/{timestamp}-{docket}.pdf (not constructible: timestamp prefix). Categories: ISC Civil, ISC Criminal, ICA Civil, ICA Criminal & Post-Conviction, ICA Unpublished, ICA Unpublished Per Curiam.
  - Index: `https://isc.idaho.gov/cases-opinions/isc-opinions`
  - Read via: PDFs on api.isc.idaho.gov (no robots.txt; 'Cannot GET /robots.txt' 404) — fetch_doc.py reads them in full.
- **Automation:** WebFetch fail · shell ok · robots: isc.idaho.gov: 200; disallows /admin, /cdn-cgi/, /isc-network/, /__preview, /api/cms-page-preview (search API permitted)
  - The HTML listing pages (/cases-opinions/isc-opinions, /cases-opinions/ica-opinions) are a Nuxt JavaScript app: WebFetch saw only the search form, no opinions. WebFetch refuses API/PDF URLs that did not come from a search result (PROVENANCE_REQUIRED). All old-site opinion URLs (isc.idaho.gov/opinions/*.pdf, /print/appeals-court/*) return 404; /appeals-court/isc_civil 301s to the new page. The cms-document JSON contains raw control characters: parse leniently (Python json.loads(..., strict=False)). API 'categories' can contradict the PDF path (53539 tagged 'ISC Civil', file under ISC/Criminal) — trust the PDF caption. The unpublished legend sits in a caption column, so grep 'UNPUBLISHED' alone rather than the full sentence.
- **Currency:** API entry_date / last_modified — observed: "latest ICA entry 2026-10-16 (docket 53548); latest ISC 2026-10-14 (53539)"
- **Official status:** Opinions page: 'subject to formal revision before publication in the preliminary print of the Pacific Reporter'; West publishes Idaho Reports and P.3d.
- **Hazard:** slip pagination only; no Idaho Reports / P.3d pagination
- **Hazard:** coverage gaps (ISC before late 2019; ICA 2017-2019)
- **Hazard:** legacy opinion links 404
- **Hazard:** PDF URL carries an unpredictable timestamp
- **Hazard:** JSON needs lenient parsing (control characters)
- **Hazard:** category tags unreliable
- **Hazard:** caption-column layout breaks multi-word greps
- **Probe:** State v. Pendleton, Docket No. 53539 (Idaho Oct. 14, 2026) → `https://isc.idaho.gov/api/cms-content-search?scope=documents&document_type=ISC%20Opinion&sort_by=entry_date&sort_direction=DESC&limit=2` — expect: ""name":"53539""
- **Evidence (2026-10-16):** Script: search JSON returned id 22184 name '53539'; cms-document?id=22184 → opinion_file .../ISC/Criminal/2026/1791997359508-53539.pdf; PDF 22 pp, 'IN THE SUPREME COURT OF THE STATE OF IDAHO Docket No. 53539'. q=Dorff → 48119 (2023); q=50045 → Shumway v. IDOL PDF 12 pp. | Independent check 2026-10-16: Script: results[0] name '53539', 'ISC Opinion'; PDF 'Docket No. 53539' 22 pp; second citation State v. Cowell, Docket No. 53548 (Idaho Ct. App. Oct. 16, 2026) (unpublished) ok
- **Notes:** Opinion headers give docket, term and 'Opinion Filed' date; no opinion-number line in 2023/2026 samples. ICA unpublished headers carry 'THIS IS AN UNPUBLISHED OPINION AND SHALL NOT BE CITED AS AUTHORITY'. Email alerts offered on the opinions page.

### `id-cases-justia` — Justia — Idaho Supreme Court and Court of Appeals

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1866-2026; Court of Appeals 1982-2026.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/idaho/{court-category}/{year}/{docket}[-N].html`
  - Placeholders: court-category is supreme-court, supreme-court-civil, supreme-court-criminal, court-of-appeals, court-of-appeals-civil or court-of-appeals-criminal (newer cases sit in the civil/criminal paths); some dockets carry '-0' suffix (48846-0.html). Category and suffix cannot be predicted — use the year listing.
  - Index: `https://law.justia.com/cases/idaho/`
  - Navigation: /cases/idaho/ → supreme-court/ or court-of-appeals/ (year list) → /{year}/ list of cases with hrefs → case page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge on robots.txt
  - WebFetch only.
- **Currency:** year listing pages — observed: "Supreme Court latest year 2026 (112 decisions)"
- **Official status:** Third-party; mirrors slip opinions.
- **Hazard:** slip pagination only (no star paging)
- **Hazard:** category path unpredictable
- **Hazard:** shell blocked by Cloudflare
- **Probe:** State v. Dorff, 171 Idaho 818, 526 P.3d 988 (2023) → `https://law.justia.com/cases/idaho/supreme-court-criminal/2023/48119.html` — expect: "Kirby Dorff appeals from the denial of his motion to"
- **Evidence (2026-10-16):** WebFetch: YES full text, 'Docket No. 48119', no reporter cite, slip page markers 1-19, ends with dissent; not truncated. Year indexes: supreme-court 1866-2026, court-of-appeals 1982-2026. | Independent check 2026-10-16: WebFetch YES 'Kirby Dorff appeals from the denial of his motion to'; docket 48119; pages 1-19; second citation State v. Ash, Docket No. 50783 (Idaho Ct. App. Dec. 19, 2024) ok

## F. Subsequent history

### `id-subsequent-history-isc` — Petition-for-review orders and Supreme Court opinions on review (isc.idaho.gov API)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Idaho Supreme Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Some orders granting review are posted as 'ISC Opinion' documents (e.g. 46085ORD.pdf, SMITHORD.pdf, 2020); routine denials are not posted.
- **Read via (in order):** **script**
- **Access:** `search-only` · format json
  - Pattern: `https://isc.idaho.gov/api/cms-content-search?scope=documents&q={ica_docket_or_party}&limit=20`
  - Placeholders: Search by the Court of Appeals docket number or party name (no document_type filter). An order granting review names the ICA docket and the NEW Supreme Court docket (46085-2018 → 48109-2020); then search that new docket for the Supreme Court opinion. Denials of review appear only as 'review denied' in West's P.3d/Idaho Reports history — no free official source found. Verified chain: 46085 → order → q=48109 → 2021 Supreme Court opinion (State v. Huckabay).
  - Index: `https://isc.idaho.gov/cases-opinions/isc-opinions`
- **Automation:** WebFetch fail · shell ok · robots: as id-opinions-isc-api
  - q='Petition for Review' returned the 46085 and 45758 orders; q='Petition for Review denied' returned nothing.
- **Currency:** n/a — observed: "orders dated 06/23/2020 and 2020-10-09"
- **Official status:** Same as id-opinions-isc-api.
- **Hazard:** docket changes on grant of review
- **Hazard:** denials not published
- **Hazard:** ICA 2017-2019 opinions absent, so the decision below may be missing
- **Hazard:** orders are OCR scans; phrases are not contiguous ('Petition for Review PIaintiff—Respondent, Docket No. 46085-2018')
- **Hazard:** order PDFs can sit under a mismatched path (46085ORD.pdf under ISC/Civil/2018 for a criminal case)
- **Probe:** State v. Huckabay, No. 46085-2018 (petition for review) → `https://isc.idaho.gov/api/cms-content-search?scope=documents&q=46085&limit=10` — expect: "Order Granting Petition for Review"
- **Evidence (2026-10-16):** Script: q=46085 → 46085ORD.pdf (ISC Opinion, category ICA Criminal & Post-Conviction); PDF: 'Court of Appeals Case No. 46085-2018 is CLOSED And Supreme Court Case No. 48109-2020'; 'Order Granting Petition for Review'. | Independent check 2026-10-16: Script: q=46085 → 46085ORD.pdf; 'Order Granting Petition for Review … Docket No. 46085-2018'; second citation State v. Huckabay, Docket No. 48109 (Idaho 2021) (opinion on review) ok
- **Notes:** I.A.R. 118 (id-rules-isc, print/iar/118) governs petitions for review.

## Not available (do not look for these again)

- **statutes** — public.law edition of the Idaho Code: www.public.law home lists Oregon among its states but not Idaho; idaho.public.law fails at the proxy (CONNECT 502). (2026-10-16)
- **statutes** — Cornell LII Idaho Code / Constitution / opinions: https://www.law.cornell.edu/states/idaho links out to legislature.idaho.gov, isc.idaho.gov, adminrules; LII hosts only the Idaho Administrative Code. (2026-10-16)
- **statutes** — Official bulk download (XML/JSON) of the Idaho Code: Only per-chapter PDFs (T{t}CH{c}.pdf) linked from title pages; no bulk or API found. (2026-10-16)
- **case_law** — Free official reporter (Idaho Reports / P.3d) pagination: Opinions page: West publishes cited opinions in Pacific Reporter and Idaho Reports; court PDFs carry slip pagination only. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinion PDFs carry docket number and filing date only; none observed. (2026-10-16)
- **case_law** — isc.idaho.gov Supreme Court opinions before late 2019 and Court of Appeals 2017-2019: API: ISC Opinion ASC earliest entry 2019-09-11; tag counts ISC 2010-2017 = 0; ICA 2017 = 1, 2018 = 0, 2019 = 0. Old-site PDFs (/opinions/*.pdf) 404. (2026-10-16)
- **subsequent_history** — Published list of petition-for-review denials: API q='Petition for Review denied' → 0 results; old weekly 'casesfiled' PDFs (isc.idaho.gov/opinions/casesfiledMMDDYY.pdf) return 404. (2026-10-16)

## Corpus candidates (maintainers)

- `id-rules-isc` — 417,681 chars on one page; fetch tool stops ~100K. Per-rule print pages exist, so corpus is optional.
- `id-rules-isc` — 263,642 chars
- `id-rules-isc` — 232,420 chars
- `id-rules-isc` — 127,721 chars; WebFetch stopped in Rule 703
- `id-rules-irpc` — 67 pp, 544,451 chars; only source for IRPC
- `id-idapa-dfm` — IDAPA chapters run to 700K+ chars (58.01.02: 181 pp)
- `id-statutes-leg` — official per-chapter PDFs suit ingest of whole chapters · bulk: per-chapter PDFs only: /wp-content/uploads/statutesrules/idstat/Title{t}/T{t}CH{c}.pdf

## Open questions

- WebFetch could not be tested on api.isc.idaho.gov opinion PDFs or files.dfm.idaho.gov PDFs because hand-built URLs were refused (PROVENANCE_REQUIRED); an independent verifier with URL permissions should retest.
- Do Supreme Court opinions on review still receive a new docket number after 2020, or keep the Court of Appeals docket?
- Where (if anywhere) are pre-2019 Supreme Court and 2017-2019 Court of Appeals opinions on the new isc.idaho.gov site (the 'Include Archived' toggle did not change API results)?
- Current mapping of renumbered IDAPA 16 chapters (e.g. former 16.03.09 Medicaid Basic Plan) — the listing API is POST-only and the site reported a listings outage on 2026-10-16.
- id-icourt: blocked status (Cloudflare challenge) not independently re-confirmed; the verifier's WebFetch was refused on provenance before any request.

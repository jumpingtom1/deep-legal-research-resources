# Oklahoma (OK) — free legal sources

_Generated from `data/ok.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

OSCN (oscn.net), the official free host of the statutes, constitution, court-rule appendices, case law with public-domain citations (2019 OK 12, ¶ 10) and dockets, now refuses all automated access by robots.txt 'Disallow: /' (earlier the same day a Cloudflare Turnstile wall), so every OSCN row is blocked; the Legislature's statute files are robots-disallowed and rules.ok.gov (OAC, Oklahoma Register) answers robots.txt with a bot check. Working routes: Justia 2025 statutes, constitution and year-listed opinions of all three appellate courts (WebFetch; tier 2), the Senate's constitution PDFs (script, tier 1, Jan 2022) and Cornell LII for the OAC (script). Supreme Court Rules, ORPC, District Court Rules, OCCA Rules, the Register and certiorari dispositions have no unblocked free source. Justia's 2025 page for a section amended by several 2025 acts is a text-less version list: fall back to the linked 2024 edition and disclose it.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Oklahoma | `okla (unverified)` | Okla. | P.3d, P.2d, P., Okla. | 2024 OK 82, ¶ 10 |
| Oklahoma Court of Civil Appeals | `oklacivapp (unverified)` | Okla. Civ. App. | P.3d, P.2d | 2025 OK CIV APP 8, ¶ 5 |
| Oklahoma Court of Criminal Appeals | `oklacrimapp (unverified)` | Okla. Crim. App. | P.3d, P.2d, P., Okla. Crim. | 2024 OK CR 33, ¶ 5 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Oklahoma Statutes (O.S. / Okla. Stat.) | `12 O.S. § 95`; `12 O.S.2021 § 2012(B)(6)`; `12 O.S. Supp. 2024 § 3226`; `12 O.S. 2011, § 95`; `Okla. Stat. tit. 12, § 95`; `Okla. Stat. Ann. tit. 21, § 701.7`; `Okla. Stat. tit. 63, § 1-705`; `10A O.S. § 1-1-105`; `12 Okla. St. Ann. § 95`; `12 O.S. §§ 2001-2027`; `Section 1-1-105 of Title 10A of the Oklahoma Statutes`; `title 12, section 95 of the Oklahoma Statutes`; `21 O.S.2021, § 701.7`; `§ 701.7 of Title 21 of the Oklahoma Statutes`; `47 O.S.2021, § 11-902`; `12 Okl.St.Ann. § 2012` | `ok-statutes-justia` → `ok-statutes-oscn` |
| Oklahoma Constitution | `Okla. Const. art. 2, § 7`; `Okla. Const. art. II, § 7`; `Okla. Const. art. 5, § 46`; `Art. 2, § 7, Okla. Const.`; `Article 2, Section 7 of the Oklahoma Constitution`; `Section 46 of Article 5 of the Oklahoma Constitution`; `Okla. Const. art. 10, § 9A` | `ok-constitution-senate` → `ok-constitution-justia` → `ok-constitution-oscn` |
| Oklahoma court rules (marked: Supreme Court Rules, ORPC, RGDP, District Court Rules, OCCA Rules) | `Okla. Sup. Ct. R. 1.36`; `Rule 1.180, Oklahoma Supreme Court Rules, 12 O.S. Supp. 2021, ch. 15, app. 1`; `Rule 8.4, Oklahoma Rules of Professional Conduct, 5 O.S. 2021, ch. 1, app. 3-A`; `Okla. R. Prof'l Conduct 1.7`; `ORPC 8.4`; `RGDP 6.2A`; `Rule 6.2A, Rules Governing Disciplinary Proceedings, 5 O.S. 2021, ch. 1, app. 1-A`; `Rule 4, Rules for District Courts of Oklahoma, 12 O.S. 2021, ch. 2, app.`; `Rule 3.5(A)(5), Rules of the Oklahoma Court of Criminal Appeals, Title 22, Ch. 18, App. (2024)`; `12 O.S. Supp. 2021, ch. 15, app. 1`; `22 O.S. 2021, Ch. 18, App.`; `Rule 1.191, Okla. Sup. Ct. R.`; `Rule 13, Rules for District Courts of Oklahoma` | `ok-rules-oscn` |
| Oklahoma Pleading Code / Evidence Code (court-rule-like statutes in Title 12) | `12 O.S. § 2012(B)(6)`; `12 O.S.2021 § 2702`; `12 O.S. § 3226(B)(1)`; `12 Okl.St.Ann. § 2012` | `ok-rules-justia` → `ok-statutes-oscn` |
| Oklahoma court rules (bare 'Rule 1.36') *(only once this jurisdiction is known)* | `Rule 1.36`; `Rule 1.180(a)`; `Rule 3.5(A)(5)` | `ok-rules-oscn` |
| Oklahoma Administrative Code (OAC title:chapter-subchapter-section) | `OAC 310:667-1-1`; `OAC 165:10-3-1`; `Okla. Admin. Code § 165:10-3-1`; `Okla. Admin. Code 310:667-1-1` | `ok-oac-lii` → `ok-oac-rules` |
| Oklahoma Administrative Code (bare 165:10-3-1) *(only once this jurisdiction is known)* | `165:10-3-1`; `310:667-1-1` | `ok-oac-lii` → `ok-oac-rules` |
| Oklahoma Register | `39 Ok Reg 2992`; `12 Ok Reg 1555`; `41 Okla. Reg. 450` | `ok-register-rules` |
| Oklahoma public-domain citations (YYYY OK N / OK CIV APP / OK CR) | `2024 OK 82`; `In re J.O., 2024 OK 82, ¶ 10`; `2025 OK CIV APP 8`; `Jimenez v. State, 2024 OK CR 33, ¶ 5`; `Halladay v. Board of County Commissioners, 2004 OK CIV APP 37, 90 P.3d 578`; `2009 OK AG 7` | `ok-cases-justia` → `ok-cases-oscn` |
| Pacific Reporter with Oklahoma parenthetical | `Doe v. Roe, 900 P.2d 100 (Okla. 1995)`; `Smith v. State, 850 P.2d 1050, 1055 (Okla. Crim. App. 1993)`; `Brown v. Green, 910 P.2d 300 (Okla. Civ. App. 1996)` | `ok-cases-justia` → `ok-cases-oscn` |
| Old official Oklahoma reporters (Okla., Okla. Crim.) | `120 Okla. 45`; `95 Okla. Crim. 1` | `ok-cases-justia` → `ok-cases-oscn` |
| Pacific Reporter without court parenthetical (generic) *(only once this jurisdiction is known)* | `90 P.3d 578`; `891 P.2d 1243` | `ok-cases-justia` → `ok-cases-oscn` |
| Oklahoma docket numbers with Oklahoma parenthetical (unpublished opinions) | `Smith v. Jones, No. 118,123 (Okla. Civ. App. Mar. 3, 2021) (unpublished)`; `Doe v. State, No. F-2022-123 (Okla. Crim. App. May 4, 2023) (unpublished)` | `ok-cases-justia` → `ok-dockets-oscn` |
| Oklahoma bare docket numbers (OCCA F-/C-/S-YYYY-N; Supreme Court No. 121,610; SCBD-N) *(only once this jurisdiction is known)* | `C-2023-951`; `S-2023-1045`; `F-2022-123`; `No. 121,610`; `SCBD-7791` | `ok-cases-justia` → `ok-dockets-oscn` |
| Westlaw unreported cites (Oklahoma parenthetical) | `2023 WL 1234567 (Okla. Civ. App. Mar. 5, 2023)`; `2022 WL 456789, at *2 (Okla. Crim. App. 2022)` | `ok-cases-justia` |
| Certiorari history (cert. denied / granted) *(only once this jurisdiction is known)* | `cert. denied`; `certiorari denied`; `cert. granted`; `certiorari previously granted` | `ok-dockets-oscn` → `ok-history-justia` |
| Court of Civil Appeals publication order | `Released for publication by order of the Court of Civil Appeals` | `ok-history-justia` → `ok-dockets-oscn` |

Regexes (case-insensitive):

- Oklahoma Statutes (O.S. / Okla. Stat.): `(?P<title>\d{1,3}[A-Z]?)\s+O\.\s*S\.\s*(?:Supp\.\s*)?(?:\d{4})?,?\s*(?:§(?!§)\s*(?P<section>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*)|§§\s*(?P<sectionr>\d{1,4}(?:\.\d{1,3})*[A-Z]?))|Okla\.\s*Stat\.\s*(?:Ann\.\s*)?tit\.\s*(?P<title2>\d{1,3}[A-Z]?),?\s*(?:§(?!§)\s*(?P<section2>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*)|§§\s*(?P<section2r>\d{1,4}(?:\.\d{1,3})*[A-Z]?))|(?P<title3>\d{1,3}[A-Z]?)\s+Okla?\.\s*St(?:at)?\.\s*(?:Ann\.\s*)?(?:§(?!§)\s*(?P<section3>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*)|§§\s*(?P<section3r>\d{1,4}(?:\.\d{1,3})*[A-Z]?))|[Ss]ections?\s+(?P<section4>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*)*)\s+(?:(?:to|through|and)\s+\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*\s+)?of\s+[Tt]itle\s+(?P<title4>\d{1,3}[A-Z]?)\s+of\s+the\s+Oklahoma\s+Statutes|[Tt]itle\s+(?P<title5>\d{1,3}[A-Z]?),\s+[Ss]ection\s+(?P<section5>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*)\s+of\s+the\s+Oklahoma\s+Statutes|§\s*(?P<section6>\d{1,4}(?:\.\d{1,3})*[A-Z]?(?:-\d{1,4}(?:\.\d{1,3})*[A-Z]?)*)\s+of\s+[Tt]itle\s+(?P<title6>\d{1,3}[A-Z]?)\s+of\s+the\s+Oklahoma\s+Statutes`
- Oklahoma Constitution: `Okla\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+|\d{1,2}),?\s*(?:§|sec\.?|section)\s*(?P<section>\d{1,3}[A-Z]?(?:-[A-Z])?)|[Aa]rt(?:\.|icle)\s*(?P<article2>[IVXL]+|\d{1,2}),?\s*(?:§|[Ss]ec\.?|[Ss]ection)\s*(?P<section2>\d{1,3}[A-Z]?),?\s+(?:of\s+the\s+)?(?:Okla\.\s*Const\.|Oklahoma\s+Constitution)|[Ss]ection\s+(?P<section3>\d{1,3}[A-Z]?)\s+of\s+[Aa]rticle\s+(?P<article3>[IVXL]+|\d{1,2})\s+of\s+the\s+Oklahoma\s+Constitution`
- Oklahoma court rules (marked: Supreme Court Rules, ORPC, RGDP, District Court Rules, OCCA Rules): `(?:Okla\.\s*Sup\.\s*Ct\.\s*R\.|Okla\.\s*R\.\s*Prof'?l\s*Conduct|Okla\.\s*Ct\.\s*Crim\.\s*App\.\s*R\.|Okla\.\s*Dist\.\s*Ct\.\s*R\.|\bORPC|\bRGDP)\s*(?P<rule>\d{1,2}(?:\.\d{1,3})?[A-Z]?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d{1,3})?[A-Z]?)(?:\([0-9A-Za-z]+\))*,\s*(?P<set>(?:Oklahoma\s+)?Supreme\s+Court\s+Rules,\s*12\s+O\.\s*S\.|Oklahoma\s+Supreme\s+Court\s+Rules|Oklahoma\s+Rules\s+of\s+Professional\s+Conduct|Rules\s+Governing\s+Disciplinary\s+Proceedings,\s*5\s+O\.\s*S\.|Rules\s+for\s+District\s+Courts\s+of\s+Oklahoma|Rules\s+of\s+the\s+(?:Oklahoma\s+)?Court\s+of\s+Criminal\s+Appeals)|(?P<title>\d{1,2})\s+O\.\s*S\.\s*(?:Supp\.\s*)?(?:\d{4})?,?\s*[Cc]h\.\s*(?P<chapter>\d{1,3}),\s*[Aa]pp\.\s*(?P<app>\d{1,2}(?:-[A-Z])?)?|Rule\s+(?P<rule3>\d{1,2}(?:\.\d{1,3})?[A-Z]?)(?:\([0-9A-Za-z]+\))*,\s*(?:Okla\.\s*Sup\.\s*Ct\.\s*R\.|Okla\.\s*R\.\s*Prof'?l\s*Conduct|Okla\.\s*Dist\.\s*Ct\.\s*R\.)`
- Oklahoma Pleading Code / Evidence Code (court-rule-like statutes in Title 12): `(?P<title>12)\s+(?:O\.\s*S\.|Okla?\.\s*St(?:at)?\.\s*(?:Ann\.)?)\s*(?:Supp\.\s*)?(?:\d{4})?,?\s*§\s*(?P<section>[23]\d{3}(?:\.\d{1,2})?)(?!\d)`
- Oklahoma court rules (bare 'Rule 1.36'): `Rules?\s+(?P<rule>\d{1,2}\.\d{1,3}[A-Z]?)(?!\d)`
- Oklahoma Administrative Code (OAC title:chapter-subchapter-section): `(?:\bOAC|Okla\.\s*Admin\.\s*Code)\s*(?:§\s*)?(?P<title>\d{1,3}):(?P<chapter>\d{1,4})-(?P<subchapter>\d{1,3})-(?P<section>\d{1,4}(?:\.\d{1,2})?)`
- Oklahoma Administrative Code (bare 165:10-3-1): `(?<![\d:])(?P<title>\d{1,3}):(?P<chapter>\d{1,4})-(?P<subchapter>\d{1,3})-(?P<section>\d{1,4})(?![\d.-])`
- Oklahoma Register: `(?P<volume>\d{1,2})\s+Ok(?:la)?\.?\s+Reg\.?\s+(?P<page>\d{1,5})`
- Oklahoma public-domain citations (YYYY OK N / OK CIV APP / OK CR): `(?P<year>(?:18|19|20)\d\d)\s+OK\s+(?:(?P<court>CIV\s+APP|CR|AG|JC|JEAP)\s+)?(?P<number>\d{1,4})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- Pacific Reporter with Oklahoma parenthetical: `(?P<volume>\d{1,4})\s+P\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>Okla\.(?:\s*(?:Civ\.|Crim\.)\s*App\.)?)\s*(?:[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*)?(?P<year>\d{4})\)`
- Old official Oklahoma reporters (Okla., Okla. Crim.): `(?P<volume>\d{1,3})\s+Okla\.\s*(?P<crim>Crim\.\s*)?(?P<page>\d{1,4})(?!\d)`
- Pacific Reporter without court parenthetical (generic): `(?P<volume>\d{1,4})\s+P\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?!\d)`
- Oklahoma docket numbers with Oklahoma parenthetical (unpublished opinions): `No\.\s*(?P<docket>[A-Z]{1,2}-\d{4}-\d{1,5}|\d{2,3},?\d{3})\s*\((?:Okla\.|OK\s)`
- Oklahoma bare docket numbers (OCCA F-/C-/S-YYYY-N; Supreme Court No. 121,610; SCBD-N): `(?<![A-Z\d-])(?P<docket>(?:F|C|S|RE|PC|M|J|D|MA|PR|O|SR|SCBD)-(?:(?:19|20)\d\d-)?\d{1,5})(?![\d-])|No\.\s*(?P<docket2>\d{2,3},\d{3})(?!\d)`
- Westlaw unreported cites (Oklahoma parenthetical): `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Okla\.`
- Certiorari history (cert. denied / granted): `cert(?:\.|iorari)\s+(?:denied|granted|dismissed)|certiorari\s+previously\s+granted`
- Court of Civil Appeals publication order: `Released\s+for\s+publication\s+by\s+order\s+of\s+the\s+Court\s+of\s+Civil\s+Appeals`

Short forms → URL key:

O.S. → `OS`; Okla. Stat. → `OS`; Okla. Stat. Ann. → `OS`; Okl. St. Ann. → `OS`; Okla. St. Ann. → `OS`; OAC → `OAC`; Okla. Admin. Code → `OAC`; Ok Reg → `OKREG`; Okla. Reg. → `OKREG`; Okla. Sup. Ct. R. → `SCR`; ORPC → `ORPC`; Okla. R. Prof'l Conduct → `ORPC`; RGDP → `RGDP`

Oklahoma style: '12 O.S.2021 § 2012(B)(6)' (edition year glued to O.S.), '12 O.S. Supp. 2024 § 3226'; Bluebook 'Okla. Stat. tit. 12, § 95'; West 'Okl.St.Ann.'. Statute sections may be dotted (701.7) or hyphenated (63 O.S. § 1-705, 10A O.S. § 1-1-105): a single § keeps hyphens; after §§ only the first number is taken, so '§§ 2001-2027' reads as 2001. Civil procedure and evidence are statutes (Pleading Code 12 O.S. §§ 2001-2027, Evidence Code §§ 2101-3009), routed by the 'Pleading Code / Evidence Code' pattern as well. Court rules are cited as statute appendices ('Rule 1.36, Oklahoma Supreme Court Rules, 12 O.S. Supp. 2021, ch. 15, app. 1'; ORPC 5 O.S. ch. 1, app. 3-A; RGDP app. 1-A; OCCA Rules 22 O.S. ch. 18, app.); bare 'Rule 1.36' is context_required. Public-domain citations: 'YYYY OK N' (Supreme Court), 'YYYY OK CIV APP N', 'YYYY OK CR N', 'YYYY OK AG N' (AG opinions), pinpoint by ¶; mandatory since 1997 and assigned retroactively on OSCN (from memory). COCA neutral-citation year is the publication year and may follow the decision year. Bare P.2d/P.3d cites, bare dockets (OCCA F-/C-/S-/RE-/PC-YYYY-N, Supreme Court 'No. 121,610', SCBD-N) and 'cert. denied' are context_required. OAC colon form '165:10-3-1' is distinctive only with 'OAC'/'Okla. Admin. Code'; the bare form is context_required (New Jersey N.J.A.C. also uses a colon). The earlier clash with Ohio's bare 'OAC …' pattern was fixed in oh.json (now context_required). CourtListener ids from memory, unverified. Trailing-marker rule cites ('Rule 1.191, Okla. Sup. Ct. R.') and prose '§ 701.7 of Title 21 of the Oklahoma Statutes' are covered (independent regex tests 2026-10-17).

## A. Statutes / code

### `ok-statutes-legislature` — Oklahoma Statutes complete titles (Oklahoma Legislature)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma Legislature · text: **link-only** · official: unknown
- **Coverage:** Whole-title PDF/RTF files (OK_Statutes/CompleteTitles/os{title}.pdf) linked from osstatuestitle.html (from WebSearch).
- **Access:** `link-only` · format pdf
  - Index: `https://www.oklegislature.gov/osstatuestitle.html?title=12`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * ... Disallow: / (also Disallow: /*.pdf$, /cf_pdf/)
  - Not fetched by any route.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Not read: robots.txt disallows the whole site.
- **Hazard:** robots Disallow: / — blocked for every route
- **Probe:** 12 O.S. (whole title) → `https://www.oklegislature.gov/OK_Statutes/CompleteTitles/os12.pdf`
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED robots.txt disallows /OK_Statutes/CompleteTitles/os12.pdf (Disallow: /*.pdf$); osstatuestitle.html and os12.rtf refused (Disallow: /). | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check: REFUSED os12.pdf (Disallow: /*.pdf$); osstatuestitle.html REFUSED (Disallow: /)

### `ok-statutes-oscn` — Oklahoma Statutes Citationized (OSCN)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma Supreme Court / Oklahoma State Courts Network · text: **fetch-and-quote** · official: unknown
- **Coverage:** All titles of the Oklahoma Statutes, one page per section with 'Historical Data' (session-law history, superseded versions) and a Citationizer table of citing cases and AG opinions.
- **Access:** `index-anchored` · format html
  - Index: `https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKST{title}&level=1`
  - Navigation: title index (ftdb=STOKST12 for Title 12; level=1 lists every chapter and '§ N. Heading' link for the whole title — Title 12 index 89K chars, complete to § 3408) -> link text '§ {section}.' -> DeliverDocument.asp?CiteID={opaque id} (12 O.S. § 95 = 439150; § 2012 = 94873; 21 O.S. § 701.7 = 69297). CiteIDs are not derivable. Index shows section numbers, not ranges.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * Disallow: / (fetch_doc.py, 2026-10-17). Earlier the same day robots.txt served an 'OSCN Turnstile' Cloudflare challenge instead (history).
  - Blocked for every route by robots Disallow: /. History: before that, fetch_doc.py read three statute pages, then received a Turnstile interstitial ('verify they are human'), and WebFetch returned ROBOTS_DISALLOWED. 
- **Currency:** 'Cite as:' line under the section heading — observed: "Cite as: 21 O.S. § 701.7 (OSCN 2026)"
- **Official status:** No certification statement seen on the section pages read; OSCN is the courts' free public service.
- **Hazard:** robots.txt Disallow: / — blocked for every route, fetch tool included
- **Hazard:** CiteIDs opaque: index hop required
- **Hazard:** Citationizer table of citing cases follows the 'Historical Data' line on the same page: stop quoting there
- **Hazard:** superseded versions are separate documents ('superseded document available')
- **Probe:** 12 O.S. § 95 → `https://www.oscn.net/applications/oscn/DeliverDocument.asp?CiteID=439150` — expect: "Civil actions other than for the recovery of real property can only be brought"
- **Evidence (2026-10-17):** Before the wall: fetch_doc.py 15,447 chars, 'A. Civil actions other than for the recovery of real property'; § 2012 38,320 chars; 21 O.S. § 701.7 39,947 chars. Then OSCN Turnstile (Cloudflare) wall: fetch_doc.py read 12 O.S. §§ 95, 2012 and 21 O.S. § 701.7 at 10:31-10:32, then got a 444-char page 'verify they are human' for the Title 23 index (10:31:47; not detected by fetch_doc.py's phrase list); robots.txt itself now serves 'OSCN Turnstile' (curl read of robots.txt only); WebFetch: ROBOTS_DISALLOWED on index.asp STOKCN and STOKST74 and on /robots.txt. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check DeliverDocument.asp?CiteID=439150: REFUSED robots.txt 'Disallow: /'
- **Notes:** If the wall lifts, this is the best tier-1 statute route (complete, current, with history). The site is also the only free official host of the court rules appendices and dockets.

### `ok-statutes-justia` — Justia — Oklahoma Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual snapshots; current edition '2025 Oklahoma Statutes'; prior years at /codes/oklahoma/{year}/title-{title}/. Statute titles only: court-rule appendices (Supreme Court Rules, ORPC, District Court Rules) are not included.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/oklahoma/title-{title}/section-{title}-{section_dashed}/`
  - Placeholders: {title} as cited, lower-case (10A -> title-10a); {section_dashed} = section with dots and hyphens both as '-': 12 O.S. § 95 -> title-12/section-12-95/ ; 21 O.S. § 701.7 -> title-21/section-21-701-7/ ; 47 O.S. § 11-902 -> title-47/section-47-11-902/ ; 10A O.S. § 1-1-105 -> title-10a/section-10a-1-1-105/ (both tested independently). If the page says 'See the following versions' (no text), follow its link to the 2024 edition /codes/oklahoma/2024/title-{title}/section-{title}-{section_dashed}/ and disclose the 2024 edition. Title index: https://law.justia.com/codes/oklahoma/title-{title}/.
  - Index: `https://law.justia.com/codes/oklahoma/2025/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com answered robots.txt with a bot check (fetch_doc.py: host off for the day, 2026-10-17)
  - Built section URLs were not gated for WebFetch.
- **Currency:** page heading and title tag — observed: "2025 Oklahoma Statutes"
- **Official status:** Page disclaimer: 'These codes may not be the most recent version.' 'Please check official sources.'
- **Hazard:** tier 2: disclose with the '2025' edition string
- **Hazard:** may lag session laws effective after the snapshot
- **Hazard:** script route refused (bot check)
- **Hazard:** 2025 version index: a section amended by more than one 2025 act (47 O.S. § 11-902, 10A O.S. § 1-1-105) has a 2025 page 'See the following versions' listing unlinked versions with NO text; follow the page's link to the 2024 edition (/codes/oklahoma/2024/title-{title}/section-...) and disclose '2024 edition; 2025 amendments not reflected' with any quote
- **Hazard:** dotted and hyphenated sections share the '-' slug form (701.7 -> 701-7, 11-902 -> 11-902): confirm on the title index if both could exist
- **Probe:** 12 O.S. § 95 → `https://law.justia.com/codes/oklahoma/title-12/section-12-95` — expect: "A. Civil actions other than for the recovery of real property"
- **Evidence (2026-10-17):** WebFetch: YES, 'A. Civil actions other than for the recovery of real property'; '2025 Oklahoma Statutes'; not truncated. Second: built /title-21/section-21-701-7/: YES 'A person commits murder in the first degree when that'; third /title-12/section-12-2012/ subsection B 'Every defense, in law or fact, to a claim for'. | Independent check 2026-10-17: WebFetch YES 'A. Civil actions other than for the recovery of real property'; '2025 Oklahoma Statutes'; not truncated

## B. Constitution

### `ok-constitution-oscn` — Oklahoma Constitution (OSCN)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma State Courts Network · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution per section (ftdb=STOKCN), linked from the Oklahoma Department of Libraries 'Library Laws' page.
- **Access:** `index-anchored` · format html
  - Index: `https://www.oscn.net/applications/oscn/index.asp?level=1&ftdb=STOKCN&year=`
  - Navigation: constitution index -> 'Section N' links -> DeliverDocument.asp?CiteID={opaque}
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * Disallow: / (fetch_doc.py, 2026-10-17). Earlier the same day robots.txt served an 'OSCN Turnstile' Cloudflare challenge instead (history).
  - Blocked for every route by robots Disallow: /. History: before that, fetch_doc.py read three statute pages, then received a Turnstile interstitial ('verify they are human'), and WebFetch returned ROBOTS_DISALLOWED. 
- **Currency:** n/a — observed: "n/a"
- **Official status:** Not read (bot wall).
- **Hazard:** robots.txt Disallow: / — blocked for every route, fetch tool included
- **Probe:** Okla. Const. art. 2, § 7 → `https://www.oscn.net/applications/oscn/index.asp?level=1&ftdb=STOKCN&year=`
- **Evidence (2026-10-17):** WebFetch (URL taken from oklahoma.gov/libraries page): ROBOTS_DISALLOWED. OSCN Turnstile (Cloudflare) wall: fetch_doc.py read 12 O.S. §§ 95, 2012 and 21 O.S. § 701.7 at 10:31-10:32, then got a 444-char page 'verify they are human' for the Title 23 index (10:31:47; not detected by fetch_doc.py's phrase list); robots.txt itself now serves 'OSCN Turnstile' (curl read of robots.txt only); WebFetch: ROBOTS_DISALLOWED on index.asp STOKCN and STOKST74 and on /robots.txt. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check index.asp?level=1&ftdb=STOKCN: REFUSED (rule: Disallow: /)

### `ok-constitution-senate` — Oklahoma Constitution (Oklahoma State Senate PDFs)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Oklahoma State Senate · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution in one PDF (231 pp., Last-Modified 4 Jan 2022) and per-article PDFs (2019-12 folder, Last-Modified 22 Dec 2019); headings 'SECTION II-7.' with history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://oksenate.gov/sites/default/files/2019-12/oc{article_arabic}.pdf`
  - Placeholders: Per-article file: Art. 2 -> oc2.pdf, Art. 5 -> oc5.pdf (arabic article number). Prefer the newer whole-constitution PDF https://oksenate.gov/sites/default/files/2022-01/AllOKConstitutionArticles.pdf and grep for 'SECTION {ARTICLE_ROMAN}-{section}.' (Art. 2 § 7 -> 'SECTION II-7.'); per-article files use 'SECTION II-7' without the period. Pages 1-11 of the whole PDF are a table of contents with the same headings: take the second match.
  - Index: `https://oksenate.gov/sites/default/files/2022-01/AllOKConstitutionArticles.pdf`
- **Automation:** WebFetch untested · shell ok · robots: Drupal default robots: /sites/default/files/ not disallowed (fetch_doc.py: permits)
  - No Senate HTML index page for these PDFs was found (oksenate.gov/oklahoma-constitution 404); files located by WebSearch. Whole PDF 691K chars exceeds WebFetch's window.
- **Currency:** none stated; HTTP Last-Modified only — observed: "Last-Modified: Tue, 04 Jan 2022"
- **Official status:** Senate staff compilation; no certification or currency statement in the PDF.
- **Hazard:** may omit amendments adopted after Jan 2022 (no currency statement): check the section's history note against later State Questions
- **Hazard:** per-article PDFs older (Dec 2019)
- **Hazard:** table of contents repeats every heading: skip to the body match
- **Hazard:** file paths contain upload-month folders (2019-12, 2022-01): a newer upload would have a new path
- **Hazard:** probe responses may come from fetch_doc.py's one-day cache: use --max-age 0 for a fresh download when currency matters
- **Probe:** Okla. Const. art. 2, § 7 → `https://oksenate.gov/sites/default/files/2022-01/AllOKConstitutionArticles.pdf` — expect: "No person shall be deprived of life, liberty, or property, without due process of law."
- **Evidence (2026-10-17):** fetch_doc.py: PDF 231 pp, 691,110 chars; 'SECTION II-7. Due process of law. No person shall be deprived of life' at p.14 (TOC match at p.1). Second: 'SECTION V-46. Local and special laws on certain subjects prohibited.' p.41; per-article oc2.pdf (13 pp) and oc5.pdf (19 pp) also read. | Independent check 2026-10-17: fetch_doc grep: 231 pp; p.14 'SECTION II-7. Due process of law. No person shall be deprived' (cached today); second citation Okla. Const. art. 10, § 9A ok

### `ok-constitution-justia` — Justia — Oklahoma Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Oklahoma Constitution per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/oklahoma/{article_roman}-{section}.html`
  - Placeholders: Art. 2 § 7 -> II-7.html; Art. 5 § 46 -> V-46.html; Art. 10 § 9A -> X-9A.html (upper-case Roman article; lettered sections tested). Index: https://law.justia.com/constitution/oklahoma/
  - Index: `https://law.justia.com/constitution/oklahoma/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py, 2026-10-17)
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version."
- **Official status:** Page note: 'This Constitution may not be the most recent version.'
- **Hazard:** tier 2
- **Probe:** Okla. Const. art. 2, § 7 → `https://law.justia.com/constitution/oklahoma/II-7.html` — expect: "No person shall be deprived of life, liberty, or property,"
- **Evidence (2026-10-17):** WebFetch: YES 'No person shall be deprived of life, liberty, or property,'; not truncated. Second: built V-46.html YES 'The Legislature shall not, except as otherwise provided in this'. | Independent check 2026-10-17: WebFetch YES 'No person shall be deprived of life, liberty, or property,'; disclaimer 'may not be the most recent version'; second citation Okla. Const. art. 10, § 9A ok

## C. Court rules

### `ok-rules-oscn` — Oklahoma court rules (OSCN statute appendices)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma Supreme Court / OSCN · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of the Supreme Court (12 O.S. ch. 15, app. 1), Rules for District Courts (12 O.S. ch. 2, app.), Rules of Professional Conduct (5 O.S. ch. 1, app. 3-A), Rules Governing Disciplinary Proceedings (5 O.S. ch. 1, app. 1-A), Rules of the Court of Criminal Appeals (22 O.S. ch. 18, app.) — published as appendices in the OSCN statute database (from memory; not read).
- **Access:** `index-anchored` · format html
  - Index: `https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKST12&level=1`
  - Navigation: title index -> chapter appendix entries -> DeliverDocument.asp?CiteID={opaque} per rule (not verified).
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * Disallow: / (fetch_doc.py, 2026-10-17). Earlier the same day robots.txt served an 'OSCN Turnstile' Cloudflare challenge instead (history).
  - Blocked for every route by robots Disallow: /. History: before that, fetch_doc.py read three statute pages, then received a Turnstile interstitial ('verify they are human'), and WebFetch returned ROBOTS_DISALLOWED. 
- **Currency:** n/a — observed: "n/a"
- **Official status:** Not read (bot wall).
- **Hazard:** robots.txt Disallow: / — blocked for every route, fetch tool included
- **Hazard:** appendix structure not verified
- **Probe:** Okla. Sup. Ct. R. 1.36 → `https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKST12&level=1`
- **Evidence (2026-10-17):** WebFetch on the Title 12 index: PROVENANCE_REQUIRED (gated) — then ROBOTS_DISALLOWED on other OSCN index pages. OSCN Turnstile (Cloudflare) wall: fetch_doc.py read 12 O.S. §§ 95, 2012 and 21 O.S. § 701.7 at 10:31-10:32, then got a 444-char page 'verify they are human' for the Title 23 index (10:31:47; not detected by fetch_doc.py's phrase list); robots.txt itself now serves 'OSCN Turnstile' (curl read of robots.txt only); WebFetch: ROBOTS_DISALLOWED on index.asp STOKCN and STOKST74 and on /robots.txt. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check index.asp?ftdb=STOKST12&level=1: REFUSED (rule: Disallow: /)

### `ok-rules-justia` — Justia — Oklahoma Pleading Code and Evidence Code (Title 12 statutes)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Oklahoma's civil-procedure and evidence rules are statutes: Pleading Code 12 O.S. §§ 2001-2027, Evidence Code §§ 2101-3009, Discovery Code §§ 3224-3237. Court-rule appendices are NOT on Justia (Title 5 page lists no appendix or rules entries).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/oklahoma/title-12/section-12-{section}/`
  - Placeholders: As ok-statutes-justia: 12 O.S. § 2012 -> section-12-2012/.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check (fetch_doc.py)
- **Currency:** page heading — observed: "2025 Oklahoma Statutes"
- **Official status:** As ok-statutes-justia.
- **Hazard:** tier 2
- **Hazard:** no Supreme Court / District Court / ORPC / OCCA rules
- **Hazard:** inherits the 2025 version-index gap from ok-statutes-justia: if the page lists versions without text, use the linked 2024 edition and disclose it
- **Probe:** 12 O.S. § 2012(B) → `https://law.justia.com/codes/oklahoma/title-12/section-12-2012/` — expect: "Every defense, in law or fact, to a claim for"
- **Evidence (2026-10-17):** WebFetch: YES, subsection B 'Every defense, in law or fact, to a claim for'; '2025 Oklahoma Statutes'; reaches history line. WebFetch on /codes/oklahoma/title-5/: no appendix or rules entries. | Independent check 2026-10-17: WebFetch YES 'Every defense, in law or fact, to a claim for relief'; '2025 Oklahoma Statutes'; second citation 12 O.S. § 3226 ok

## D. Administrative code

### `ok-oac-rules` — Oklahoma Administrative Code (rules.ok.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma Secretary of State, Office of Administrative Rules · text: **link-only** · official: unknown
- **Coverage:** OAC and Oklahoma Register (single site, linked from agency pages such as opers.ok.gov as 'Office of Administrative Rules').
- **Access:** `search-only` · format html
  - Index: `https://rules.ok.gov`
  - Navigation: not established (site not read)
- **Automation:** WebFetch gated · shell blocked-challenge · robots: rules.ok.gov answers robots.txt with a bot check (fetch_doc.py)
  - WebFetch on https://rules.ok.gov (link taken from opers.ok.gov) held for approval and timed out. Independent check: reached from the opers.ok.gov link, WebFetch was still gated; a future run should retry from that linking page with an approver present.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Not read (bot check / gated).
- **Hazard:** bot check on robots.txt
- **Hazard:** probably a JavaScript application (unconfirmed)
- **Probe:** OAC 165:10-3-1 → `https://rules.ok.gov/`
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED 'rules.ok.gov answers robots.txt with a bot check (challenge)'. WebFetch https://rules.ok.gov/ and https://rules.ok.gov: PROVENANCE_REQUIRED (not answered). | Re-confirmed blocked 2026-10-17: WebFetch https://rules.ok.gov/: PROVENANCE_REQUIRED (approval timed out); fetch_doc check: REFUSED robots bot check

### `ok-oac-lii` — Cornell LII — Oklahoma Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section OAC pages with 'Notes' history (Ok Reg citations).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/oklahoma/OAC-{title}-{chapter}-{subchapter}-{section}`
  - Placeholders: OAC 165:10-3-1 -> OAC-165-10-3-1 ; 310:667-1-1 -> OAC-310-667-1-1 (colon and hyphens become '-'). Index hops: /regulations/oklahoma/title-{title} -> /chapter-{chapter} -> /subchapter-{n} (lists section range). A wrong slug returns the state title list (200), not 404: check the heading 'Okla. Admin. Code § {cite}'.
  - Index: `https://www.law.cornell.edu/regulations/oklahoma/title-165`
- **Automation:** WebFetch untested · shell ok · robots: permits (fetch_doc.py)
  - Last-Modified headers Aug 2025.
- **Currency:** Notes block (latest Ok Reg amendment); HTTP Last-Modified — observed: "Last-Modified: Tue, 05 Aug 2025"
- **Official status:** Third-party compilation; page says state regulations are updated quarterly.
- **Hazard:** tier 2; possibly stale (Aug 2025)
- **Hazard:** wrong slug returns a 200 index page, not 404
- **Hazard:** some sections show only an editorial note (310:667-1-1 body: 'Removed supplement date ...')
- **Probe:** OAC 165:10-3-1 → `https://www.law.cornell.edu/regulations/oklahoma/OAC-165-10-3-1` — expect: "the operator shall obtain for the well a Permit to Drill approved by the Conservation Division"
- **Evidence (2026-10-17):** fetch_doc.py: 12,620 chars; heading 'Okla. Admin. Code § 165:10-3-1 - Required approval of notice of intent to drill'; '(1) Except as provided in (I) of this Section'. Second: OAC-310-667-1-1 (2,512 chars) heading '§ 310:667-1-1 - Purpose', Notes 'Amended by Oklahoma Register, Volume 39, Issue 24'. Guessed slug Okla-Admin-Code-SS-310-667-1-1 returned the title list. | Independent check 2026-10-17: fetch_doc grep: 12,620 chars; 'shall obtain for the well a Permit to Drill approved by the Conservation Division'; second citation OAC 252:100-1-3 ok

## D. Administrative register

### `ok-register-rules` — Oklahoma Register (rules.ok.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma Secretary of State, Office of Administrative Rules · text: **link-only** · official: unknown
- **Coverage:** Semi-monthly Register (cited '39 Ok Reg 2992'); agencies repost individual issues (e.g. oklahoma.gov/content/dam/ok/en/omma/... Volume 41 Number 3) but no complete free archive outside rules.ok.gov was found.
- **Access:** `search-only` · format pdf
  - Index: `https://rules.ok.gov`
  - Navigation: not established
- **Automation:** WebFetch gated · shell blocked-challenge · robots: bot check (fetch_doc.py)
  - As ok-oac-rules.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Not read.
- **Hazard:** bot check
- **Hazard:** agency reposts are partial and not a substitute
- **Probe:** 39 Ok Reg 2992 → `https://rules.ok.gov/`
- **Evidence (2026-10-17):** As ok-oac-rules: fetch_doc.py REFUSED (robots.txt bot check); WebFetch PROVENANCE_REQUIRED. | Re-confirmed blocked 2026-10-17: Same host/probe as ok-oac-rules: WebFetch PROVENANCE_REQUIRED; fetch_doc REFUSED bot check

## E. Case law

### `ok-cases-oscn` — OSCN case law (Supreme Court, Court of Civil Appeals, Court of Criminal Appeals)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma State Courts Network · text: **fetch-and-quote** · official: official
- **Coverage:** All three appellate courts, with neutral citations (also assigned retroactively to older cases, e.g. '2004 OK CIV APP 37' in the Citationizer of 12 O.S. § 95), P.2d/P.3d parallels and Citationizer tables.
- **Access:** `index-anchored` · format html
  - Index: `https://www.oscn.net/`
  - Navigation: court/year index -> DeliverDocument.asp?CiteID={opaque} (from memory; not verified)
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * Disallow: / (fetch_doc.py, 2026-10-17). Earlier the same day robots.txt served an 'OSCN Turnstile' Cloudflare challenge instead (history).
  - Blocked for every route by robots Disallow: /. History: before that, fetch_doc.py read three statute pages, then received a Turnstile interstitial ('verify they are human'), and WebFetch returned ROBOTS_DISALLOWED. 
- **Currency:** n/a — observed: "n/a"
- **Official status:** Oklahoma's public-domain citations (YYYY OK N, ¶ pinpoints) are assigned and published by the courts on OSCN (from memory; pages not read today).
- **Hazard:** robots.txt Disallow: / — blocked for every route, fetch tool included
- **Probe:** In re J.O., 2024 OK 82 → `https://www.oscn.net/`
- **Evidence (2026-10-17):** OSCN Turnstile (Cloudflare) wall: fetch_doc.py read 12 O.S. §§ 95, 2012 and 21 O.S. § 701.7 at 10:31-10:32, then got a 444-char page 'verify they are human' for the Title 23 index (10:31:47; not detected by fetch_doc.py's phrase list); robots.txt itself now serves 'OSCN Turnstile' (curl read of robots.txt only); WebFetch: ROBOTS_DISALLOWED on index.asp STOKCN and STOKST74 and on /robots.txt. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check https://www.oscn.net/: REFUSED (rule: Disallow: /)

### `ok-cases-justia` — Justia — Oklahoma Supreme Court, Court of Civil Appeals, Court of Criminal Appeals

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Court of Civil Appeals 1950-2026, Court of Criminal Appeals 1900-2026, Supreme Court (year listings; 2024 has 81 entries, 2024 OK 1 to 2024 OK 83); also Court on the Judiciary and Judicial Ethics Advisory Panel. Opinion pages carry ¶ paragraph numbers.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Index: `https://law.justia.com/cases/oklahoma/`
  - Navigation: court index (/cases/oklahoma/{supreme-court|court-of-appeals-civil|court-of-appeals-criminal}/) -> year listing /{year}/ (one page, each entry shows name, date, docket and 'YYYY OK N' citation) -> case page. Slugs vary: docket ('121610.html', 'c-2023-951.html', 'scbd-7791.html') or citation ('2024-ok-80.html'), so pick from the listing, never build. The listing year is the DECISION year; the neutral-citation year can be later (COCA 2024 listing: decided Dec 20, 2024, cited 2025 OK CIV APP 8).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check (fetch_doc.py)
  - Listings are single pages (no pagination).
- **Currency:** listing heading — observed: "Oklahoma Supreme Court Decisions 2024"
- **Official status:** Third-party copy; listings show the neutral citation, docket and date.
- **Hazard:** tier 2
- **Hazard:** slug not constructible (docket vs citation forms)
- **Hazard:** COCA neutral-citation year may differ from listing year
- **Hazard:** ¶ pinpoints are the official pinpoint form; no P.3d page numbers
- **Hazard:** case-name typos in Justia headers (OCCA 2025 OK CR 25: header 'NAPOLEAN', opinion 'Napoleon'): take the name from the opinion body
- **Hazard:** some Supreme Court pages carry 'NOT RELEASED FOR PUBLICATION' (2024 OK 82): check release status before relying on or quoting as final
- **Probe:** In re J.O., 2024 OK 82 → `https://law.justia.com/cases/oklahoma/supreme-court/2024/121610.html` — expect: "The State of Oklahoma moved to terminate Father's (Parker) parental rights."
- **Evidence (2026-10-17):** WebFetch: YES 'The State of Oklahoma moved to terminate Father's (Parker) parental rights.'; ¶ numbers present; not truncated. Second: Jimenez v. State, 2024 OK CR 33 (court-of-appeals-criminal/2024/c-2023-951.html) 'On January 9, 2023, Petitioner, Luis Jimenez, entered a semi-blind plea'; third: 2025 OK CIV APP 8 (court-of-appeals-civil/2024/121092.html) 'Mandate Issued: 03/27/2025', ¶1-¶36. | Independent check 2026-10-17: WebFetch YES 'The State of Oklahoma moved to terminate Father's (Parker) parental rights.'; ¶1-¶19; 2024 OK 82; second citation Napolean v. State, 2025 OK CR 25 (F-2024-123, Dec. 18, 2025) ok

## F. Subsequent history

### `ok-dockets-oscn` — OSCN appellate dockets (certiorari, mandate)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Oklahoma State Courts Network · text: **link-only** · official: official
- **Coverage:** Supreme Court docket entries for COCA cases (certiorari petitions, orders, mandate) and OCCA dockets (from memory).
- **Access:** `search-only` · format html
  - Index: `https://www.oscn.net/`
  - Navigation: docket search by case number (not verified)
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-agent: * Disallow: / (fetch_doc.py, 2026-10-17). Earlier the same day robots.txt served an 'OSCN Turnstile' Cloudflare challenge instead (history).
  - Blocked for every route by robots Disallow: /. History: before that, fetch_doc.py read three statute pages, then received a Turnstile interstitial ('verify they are human'), and WebFetch returned ROBOTS_DISALLOWED. Docket paths never probed.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Courts' own docket (from memory; not read).
- **Hazard:** robots.txt Disallow: / — blocked for every route, fetch tool included
- **Probe:** No. 121,092 (cert. history) → `https://www.oscn.net/`
- **Evidence (2026-10-17):** Host-wide: OSCN Turnstile (Cloudflare) wall: fetch_doc.py read 12 O.S. §§ 95, 2012 and 21 O.S. § 701.7 at 10:31-10:32, then got a 444-char page 'verify they are human' for the Title 23 index (10:31:47; not detected by fetch_doc.py's phrase list); robots.txt itself now serves 'OSCN Turnstile' (curl read of robots.txt only); WebFetch: ROBOTS_DISALLOWED on index.asp STOKCN and STOKST74 and on /robots.txt. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check https://www.oscn.net/: REFUSED (rule: Disallow: /)

### `ok-history-justia` — Justia opinion headers (mandate / publication notes)

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Court of Civil Appeals pages show 'Mandate Issued: <date>' in the header; certiorari dispositions were not seen.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Index: `https://law.justia.com/cases/oklahoma/court-of-appeals-civil/`
  - Navigation: as ok-cases-justia: read the header of the COCA opinion. A mandate date implies certiorari was not granted or was resolved, but does not state the disposition.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check (fetch_doc.py)
- **Currency:** opinion header — observed: "Mandate Issued: 03/27/2025"
- **Official status:** Third-party copy of the opinion header.
- **Hazard:** no certiorari disposition text: absence is not evidence of no cert history
- **Hazard:** tier 2
- **Probe:** Rocket Properties LLC v. City of Tulsa, 2025 OK CIV APP 8 → `https://law.justia.com/cases/oklahoma/court-of-appeals-civil/2024/121092.html` — expect: "Mandate Issued: 03/27/2025"
- **Evidence (2026-10-17):** WebFetch: header 'Mandate Issued: 03/27/2025'; no cert. denied / certiorari note on the page. Only one page checked; whether Justia shows cert dispositions is unknown.

## Not available (do not look for these again)

- **court_rules** — Unblocked free source for Oklahoma Supreme Court Rules, Rules for District Courts, ORPC, RGDP and OCCA Rules: Only on OSCN (Turnstile wall). Justia Title 5 lists no appendix/rules entries; okbar.org/ec/conduct/ neither holds nor links the ORPC text. (2026-10-17)
- **admin_register** — Complete free Oklahoma Register archive outside rules.ok.gov: WebSearch found only agency reposts of single issues (oklahoma.gov/content/dam/ok/en/omma/...). (2026-10-17)
- **case_law** — Free official reporter pagination (P.3d): Justia pages carry ¶ numbers and neutral citations only; Oklahoma pinpoints by ¶ make this unnecessary for post-1997 cases. (2026-10-17)
- **statutes** — Reachable official bulk statute download: Legislature complete-title PDFs/RTF (OK_Statutes/CompleteTitles/os{n}.pdf) exist but robots.txt disallows the whole site. (2026-10-17)

## Corpus candidates (maintainers)

- `ok-constitution-senate` — 231-page whole-constitution PDF (691K chars), far beyond WebFetch's window; the only tier-1 constitution text reachable today

## Open questions

- OSCN robots Disallow: / (earlier a Turnstile wall): re-test on another day whether oscn.net (statutes, constitution, court rules, opinions, dockets) and its robots.txt are reachable; if so, re-research every ok-*-oscn row.
- rules.ok.gov (OAC and Oklahoma Register): WebFetch was gated; test whether it reads the site, whether it is a JS app, and whether the Register is browsable.
- oklahoma.public.law: robots.txt unreachable (proxy 502) — existence of a public.law Oklahoma edition unconfirmed.
- Does Justia ever show certiorari dispositions for COCA opinions? Only one page checked.
- Senate constitution PDF currency: check for amendments adopted after Jan 2022.
- Justia 2025 version-index pages (multiple 2025 amendments) carry no text: is there any free reachable source of the current text for such sections while OSCN is robots-blocked?

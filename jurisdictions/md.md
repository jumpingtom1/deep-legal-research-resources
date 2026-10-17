# Maryland (MD) — free legal sources

_Generated from `data/md.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and the Constitution: mgaleg.maryland.gov StatuteText pages are constructible from (article code, section) and give one section per page (script route verified; WebFetch needs per-URL approval for built URLs); per-article PDFs under /{YYYY}RS/Statute_Web/ are the bulk/corpus route; Justia (2025) is the WebFetch-readable tier-2. Maryland Rules are online only on Westlaw's government site, which refuses automated access; only amendment Rules Orders are free on mdcourts.gov, and no tier-2 host carries the Rules. COMAR moved to regs.maryland.gov (Open Law Library; constructible per regulation, bulk XML on GitHub; unofficial text); the Maryland Register's last 15 issues are free as HTML on dsd.maryland.gov. Case law: mdcourts.gov serves reported Supreme Court / Appellate Court opinions from 1995 through a plain-GET index (official and UELMA-authenticated since July 1, 2018, but slip pagination only) and unreported Appellate Court opinions from May 2015 by monthly list; certiorari grants/denials are monthly HTML lists searchable only by party name.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Maryland (Court of Appeals of Maryland before Dec. 14, 2022) | `md (unverified)` | Md. | Md., A.3d, A.2d, A. | — |
| Appellate Court of Maryland (Court of Special Appeals of Maryland before Dec. 14, 2022) | `mdctspecapp (unverified)` | Md. App. (pre-2022 opinions: Md. Ct. Spec. App.) | Md. App., A.3d, A.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Annotated Code of Maryland (articles) | `Md. Code Ann., Cts. & Jud. Proc. § 5-101`; `CJP § 5-101`; `Md. Code Ann., Crim. Law § 2-201(a)`; `Md. Code Ann., Real Prop. § 8-401(b)`; `Md. Code Ann., Health-Gen. § 4-301`; `Md. Code Ann., Cts. & Jud. Proc. § 3-2A-04`; `CP § 8-301.1`; `Courts and Judicial Proceedings Article, § 5-101`; `Md. Code (1974, 2020 Repl. Vol.), Courts and Judicial Proceedings Article § 5-101`; `section 10-1601 of the State Government Article`; `§ 5-101 of the Courts & Judicial Proceedings Article`; `§§ 10-1601 et seq. of the State Government Article`; `Md. Code Ann., State Gov't §§ 10-1601–10-1611` | `md-code-mgaleg` → `md-code-mgaleg-pdf` → `md-code-justia` |
| Maryland Constitution and Declaration of Rights | `Md. Const. art. IV, § 14`; `Md. Const. art. XI-A, § 2`; `Md. Const. Decl. of Rts. art. 24`; `Md. Decl. of Rts. art. 24`; `Article 24 of the Maryland Declaration of Rights`; `Article IV, Section 18 of the Maryland Constitution` | `md-constitution-mgaleg` → `md-constitution-msa` → `md-constitution-justia` |
| Maryland Rules | `Md. Rule 2-322(b)`; `Md. Rule 5-702`; `Maryland Rule 8-605.1`; `Md. Rules 1-104`; `Rule 2-322(b) of the Maryland Rules`; `Md. Rule 19-301.7`; `MARPC 1.7`; `Maryland Rule 5- 404(a)(2)(B)` | `md-rules-westlaw` → `md-rules-orders` |
| Code of Maryland Regulations (COMAR) | `COMAR 26.08.02.03`; `Md. Code Regs. 26.08.02.03`; `COMAR 13A.03.02.01B(2)`; `COMAR 10.09.10.01`; `COMAR 26.08.02.03-2`; `COMAR 26.08.02` | `md-comar-regs` → `md-comar-lii` |
| Maryland Register | `53 Md. Reg. 975 (Oct. 2, 2026)`; `20:11 Md. R. 917`; `8:15 Md. R. 1308` | `md-register-dsd` |
| Reported Maryland cases (Md. / Md. App.) | `Hollins v. State, 489 Md. 296 (2024)`; `Syed v. Lee, 488 Md. 537 (2024)`; `Potts v. State, 231 Md. App. 398 (2016)`; `Bennett v. Gentile, 487 Md. 487 (2024)` | `md-opinions-reported` → `md-cases-justia` |
| Atlantic Reporter with Maryland parenthetical | `300 A.3d 1 (Md. 2023)`; `250 A.3d 100 (Md. Ct. Spec. App. 2021)`; `300 A.3d 50 (Md. App. 2024)` | `md-opinions-reported` → `md-cases-justia` |
| Maryland appellate docket form (No. N, September Term, YYYY) - reported and unreported | `Hollins v. State, No. 5, September Term, 2024`; `Farmer v. State, No. 2330, Sept. Term, 2024 (Md. App. Sept. 30, 2026)`; `Midaro Invs. 2021, LLC v. Gerzowski, Nos. 1991 and 1992, Sept. Term, 2023`; `Misc. No. 26, September Term, 2021` | `md-opinions-reported` → `md-opinions-unreported` → `md-cases-justia` |
| Westlaw / Lexis unreported cites | `2024 WL 123456 (Md. App. Mar. 1, 2024)`; `2019 WL 654321 (Md. Ct. Spec. App. Feb. 1, 2019)`; `2023 Md. App. LEXIS 100` | `md-opinions-unreported` → `md-cases-justia` |
| Certiorari dispositions | `cert. denied, 475 Md. 1 (2021)`; `cert. granted, 489 Md. 296 (2024)`; `cert. denied, ___ Md. ___ (2026)` | `md-cert-petitions` |

Regexes (case-insensitive):

- Annotated Code of Maryland (articles): `(?:Md\.\s*Code(?:\s*Ann\.)?,?\s*(?:\([^)]*\),?\s*)?)?(?P<article>(?:Alc\.\s*Bev\.\s*(?:&|and)\s*Cannabis|State\s*Pers\.\s*(?:&|and)\s*Pens\.|State\s*Fin\.\s*(?:&|and)\s*Proc\.|Hous\.\s*(?:&|and)\s*Cmty\.\s*Dev\.|Bus\.\s*Occ\.\s*(?:&|and)\s*Prof\.|Cts\.\s*(?:&|and)\s*Jud\.\s*Proc\.|Corps\.\s*(?:&|and)\s*Ass['’]ns|Corps\.\s*(?:&|and)\s*Ass['’]ns|Est\.\s*(?:&|and)\s*Trusts|Gen\.\s*Provis\.|Lab\.\s*(?:&|and)\s*Empl\.|Corr\.\s*Servs\.|Crim\.\s*Proc\.|State\s*Gov['’]t|Pub\.\s*Utils\.|Pub\.\s*Safety|Local\s*Gov['’]t|Hum\.\s*Servs\.|Local\s*Gov['’]t|Health\s*[-–]\s*Gen\.|Health\s*[-–]\s*Gen\.|Health\s*Occ\.|State\s*Gov['’]t|Pub\.\s*Util\.|Econ\.\s*Dev\.|Real\s*Prop\.|Gen\.\s*Prov\.|Fin\.\s*Inst\.|Tax\s*[-–]\s*Prop\.|Alc\.\s*Bev\.|Tax\s*[-–]\s*Prop\.|Nat\.\s*Res\.|Elec\.\s*Law|Crim\.\s*Law|Bus\.\s*Reg\.|Land\s*Use|Tax\s*[-–]\s*Gen\.|Fam\.\s*Law|Tax\s*[-–]\s*Gen\.|Com\.\s*Law|Transp\.|Envir\.|Agric\.|Educ\.|Env['’]t|Ins\.)|(?:Business\s*Occupations\s*(?:&|and)\s*Professions|Housing\s*(?:&|and)\s*Community\s*Development|Alcoholic\s*Beverages\s*(?:&|and)\s*Cannabis|Courts\s*(?:&|and)\s*Judicial\s*Proceedings|State\s*Finance\s*(?:&|and)\s*Procurement|Corporations\s*(?:&|and)\s*Associations|State\s*Personnel\s*(?:&|and)\s*Pensions|Financial\s*Institutions|Correctional\s*Services|Labor\s*(?:&|and)\s*Employment|Economic\s*Development|Alcoholic\s*Beverages|Business\s*Regulation|Criminal\s*Procedure|Estates\s*(?:&|and)\s*Trusts|Health\s*Occupations|General\s*Provisions|Natural\s*Resources|State\s*Government|Public\s*Utilities|Health\s*\s*[-–]\s*\s*General|Local\s*Government|Commercial\s*Law|Human\s*Services|Health\s*General|Tax\s*\s*[-–]\s*\s*Property|Health\s*[-–]\s*General|Transportation|Public\s*Safety|Tax\s*\s*[-–]\s*\s*General|Real\s*Property|Criminal\s*Law|Tax\s*[-–]\s*Property|Election\s*Law|Tax\s*Property|Tax\s*[-–]\s*General|Agriculture|Environment|Tax\s*General|Family\s*Law|Education|Insurance|Land\s*Use))(?:\s+Article)?,?\s*(?:\(\W*[A-Z]{2,3}\W*\)\s*)?§+\s*(?P<section>\d+[A-Z]?[-–](?:\d+[A-Z][-–])?\d+(?:\.\d+)?[A-Z]?)|(?P<article2>(?-i:\b(?:SPP|SFP|HCD|CJP|BOP|PUA|CL|CS|CA|EC|AG|FI|BR|ET|CP|CR|SF|HS|PU|FL|CJ|LU|AB|IN|LG|NR|HG|TP|RP|ED|GP|HO|SG|EN|TG|SP|PS|HU|EL|TR|LE|BO)\b))\s*§+\s*(?P<section2>\d+[A-Z]?[-–](?:\d+[A-Z][-–])?\d+(?:\.\d+)?[A-Z]?)|(?:§+|[Ss]ec(?:tion|\.))\s*(?P<section3>\d+[A-Z]?[-–](?:\d+[A-Z][-–])?\d+(?:\.\d+)?[A-Z]?)(?:\([A-Za-z0-9]+\))*(?:\s*et\s+seq\.)?\s+of\s+the\s+(?:Maryland\s+Code,?\s+)?(?P<article3>(?:Business\s*Occupations\s*(?:&|and)\s*Professions|Housing\s*(?:&|and)\s*Community\s*Development|Alcoholic\s*Beverages\s*(?:&|and)\s*Cannabis|Courts\s*(?:&|and)\s*Judicial\s*Proceedings|State\s*Finance\s*(?:&|and)\s*Procurement|Corporations\s*(?:&|and)\s*Associations|State\s*Personnel\s*(?:&|and)\s*Pensions|Financial\s*Institutions|Correctional\s*Services|Labor\s*(?:&|and)\s*Employment|Economic\s*Development|Alcoholic\s*Beverages|Business\s*Regulation|Criminal\s*Procedure|Estates\s*(?:&|and)\s*Trusts|Health\s*Occupations|General\s*Provisions|Natural\s*Resources|State\s*Government|Public\s*Utilities|Health\s*\s*[-–]\s*\s*General|Local\s*Government|Commercial\s*Law|Human\s*Services|Health\s*General|Tax\s*\s*[-–]\s*\s*Property|Health\s*[-–]\s*General|Transportation|Public\s*Safety|Tax\s*\s*[-–]\s*\s*General|Real\s*Property|Criminal\s*Law|Tax\s*[-–]\s*Property|Election\s*Law|Tax\s*Property|Tax\s*[-–]\s*General|Agriculture|Environment|Tax\s*General|Family\s*Law|Education|Insurance|Land\s*Use))\s+Article`
- Maryland Constitution and Declaration of Rights: `Md\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+(?:-[A-I])?),?\s*§\s*(?P<section>\d+[A-Za-z]?)|Md\.\s*(?:Const\.\s*)?Decl(?:\.|aration)\s*of\s*R(?:ts|ights)\.?,?\s*art\.\s*(?P<dr>\d+)|Article\s+(?P<dr2>\d+)\s+of\s+the\s+(?:Maryland\s+)?Declaration\s+of\s+Rights|Article\s+(?P<article2>[IVXL]+(?:-[A-I])?),?\s+(?:Section|§)\s*(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+Maryland\s+Constitution`
- Maryland Rules: `(?:Md\.\s*Rules?|Maryland\s+Rules?(?:\s+of\s+Procedure)?)\s*(?P<rule>\d{1,2}-\s?\d{3}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,2}-\s?\d{3}(?:\.\d+)?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Maryland\s+Rules|MARPC\s*(?:Rule\s*)?(?P<marpc>\d\.\d+)|Md\.\s*Rule\s*(?P<marpc2>19-30\d\.\d+)`
- Code of Maryland Regulations (COMAR): `(?:COMAR|Md\.\s*Code\s*Regs\.)\s*(?P<title>\d{2}[A-Z]?)\.(?P<subtitle>\d{2})\.(?P<chapter>\d{2})(?:\.(?P<regulation>\d{2}(?:-\d+[A-Z]?)?))?`
- Maryland Register: `(?P<volume>\d{1,2})\s+Md\.\s*Reg\.\s*(?P<page>\d+)|(?P<volume2>\d{1,2}):(?P<issue>\d{1,2})\s+Md\.\s*R\.\s*(?P<page2>\d+)`
- Reported Maryland cases (Md. / Md. App.): `(?P<volume>\d{1,3})\s+Md\.(?:\s*(?P<app>App\.))?\s+(?P<page>\d{1,4})(?!\d)`
- Atlantic Reporter with Maryland parenthetical: `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Md\.(?:\s*(?:Ct\.\s*Spec\.\s*)?App\.)?)\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>\d{4})\)`
- Maryland appellate docket form (No. N, September Term, YYYY) - reported and unreported: `(?:(?:Misc\.|AG|Pet\.)\s*)?Nos?\.\s*(?P<number>\d{1,4})(?:\s*(?:,|and|&)\s*\d{1,4})*,?\s*Sept(?:ember|\.)?\s*Term,?\s*(?P<term>(?:19|20)\d\d)`
- Westlaw / Lexis unreported cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\((?P<court>Md\.(?:\s*(?:Ct\.\s*Spec\.\s*)?App\.)?)|Md\.\s*(?:(?P<lexapp>App\.)\s*)?LEXIS\s+(?P<lexis>\d+))`
- Certiorari dispositions: `cert\.\s*(?P<disp>denied|granted|dismissed)(?:\s+as\s+improvidently\s+granted)?,?\s*(?:(?P<volume>\d{1,3}|_+)\s+Md\.\s+(?P<page>\d{1,4}|_+)|No\.\s*(?P<number>\d+))`

Short forms → URL key:

Agriculture → `gag`; Agric. → `gag`; AG → `gag`; Alcoholic Beverages and Cannabis → `gab`; Alcoholic Beverages → `gab`; Alc. Bev. & Cannabis → `gab`; Alc. Bev. → `gab`; AB → `gab`; Alcoholic Beverages & Cannabis → `gab`; Business Occupations and Professions → `gbo`; Bus. Occ. & Prof. → `gbo`; BOP → `gbo`; BO → `gbo`; Business Occupations & Professions → `gbo`; Business Regulation → `gbr`; Bus. Reg. → `gbr`; BR → `gbr`; Commercial Law → `gcl`; Com. Law → `gcl`; CL → `gcl`; Corporations and Associations → `gca`; Corps. & Ass'ns → `gca`; Corps. & Ass’ns → `gca`; CA → `gca`; Corporations & Associations → `gca`; Correctional Services → `gcs`; Corr. Servs. → `gcs`; CS → `gcs`; Courts and Judicial Proceedings → `gcj`; Cts. & Jud. Proc. → `gcj`; CJP → `gcj`; CJ → `gcj`; Courts & Judicial Proceedings → `gcj`; Criminal Law → `gcr`; Crim. Law → `gcr`; CR → `gcr`; Criminal Procedure → `gcp`; Crim. Proc. → `gcp`; CP → `gcp`; Economic Development → `gec`; Econ. Dev. → `gec`; EC → `gec`; Education → `ged`; Educ. → `ged`; ED → `ged`; Election Law → `gel`; Elec. Law → `gel`; EL → `gel`; Environment → `gen`; Env't → `gen`; Envir. → `gen`; EN → `gen`; Estates and Trusts → `get`; Est. & Trusts → `get`; ET → `get`; Estates & Trusts → `get`; Family Law → `gfl`; Fam. Law → `gfl`; FL → `gfl`; Financial Institutions → `gfi`; Fin. Inst. → `gfi`; FI → `gfi`; General Provisions → `ggp`; Gen. Provis. → `ggp`; Gen. Prov. → `ggp`; GP → `ggp`; Health - General → `ghg`; Health-General → `ghg`; Health General → `ghg`; Health-Gen. → `ghg`; Health–Gen. → `ghg`; HG → `ghg`; Health Occupations → `gho`; Health Occ. → `gho`; HO → `gho`; Housing and Community Development → `ghs`; Hous. & Cmty. Dev. → `ghs`; HCD → `ghs`; HS → `ghs`; Housing & Community Development → `ghs`; Human Services → `ghu`; Hum. Servs. → `ghu`; HU → `ghu`; Insurance → `gin`; Ins. → `gin`; IN → `gin`; Labor and Employment → `gle`; Lab. & Empl. → `gle`; LE → `gle`; Labor & Employment → `gle`; Land Use → `glu`; LU → `glu`; Local Government → `glg`; Local Gov't → `glg`; Local Gov’t → `glg`; LG → `glg`; Natural Resources → `gnr`; Nat. Res. → `gnr`; NR → `gnr`; Public Safety → `gps`; Pub. Safety → `gps`; PS → `gps`; Public Utilities → `gpu`; Pub. Util. → `gpu`; Pub. Utils. → `gpu`; PUA → `gpu`; PU → `gpu`; Real Property → `grp`; Real Prop. → `grp`; RP → `grp`; State Finance and Procurement → `gsf`; State Fin. & Proc. → `gsf`; SFP → `gsf`; SF → `gsf`; State Finance & Procurement → `gsf`; State Government → `gsg`; State Gov't → `gsg`; State Gov’t → `gsg`; SG → `gsg`; State Personnel and Pensions → `gsp`; State Pers. & Pens. → `gsp`; SPP → `gsp`; SP → `gsp`; State Personnel & Pensions → `gsp`; Tax - General → `gtg`; Tax-General → `gtg`; Tax General → `gtg`; Tax-Gen. → `gtg`; Tax–Gen. → `gtg`; TG → `gtg`; Tax - Property → `gtp`; Tax-Property → `gtp`; Tax Property → `gtp`; Tax-Prop. → `gtp`; Tax–Prop. → `gtp`; TP → `gtp`; Transportation → `gtr`; Transp. → `gtr`; TR → `gtr`

Court renaming: effective Dec. 14, 2022 the Court of Appeals of Maryland became the Supreme Court of Maryland and the Court of Special Appeals became the Appellate Court of Maryland (name change only; mdcourts.gov opinions page). Pre-2022 'Court of Appeals' = the HIGH court (reporter Md.), not an intermediate court; pre-2022 'Ct. Spec. App.' = today's Appellate Court (reporter Md. App.). mdcourts.gov URLs still use 'coa' and 'cosa'. Statutes: the Code is cited by ARTICLE name, never by title number: Bluebook 'Md. Code Ann., Cts. & Jud. Proc. § 5-101'; Maryland courts write 'Md. Code (1974, 2020 Repl. Vol.), § 5-101 of the Courts and Judicial Proceedings Article' or define a short form ('CJP § 5-101', 'CP § 8-301.1'). law_aliases maps every full name, Bluebook abbreviation and practitioner short form to the mgaleg article code (gcj, gcr, grp ...). Two- and three-letter short forms (CP, CR, CJ, RP, FL, ET, SG, IN, ED, CA, LE ...) are matched case-sensitively and only immediately before '§'; route them here only with Maryland context, because 'CP § ' or 'CA § ' also occur elsewhere (e.g. California). Bare article names shared with other states ('Real Property', 'Criminal Law', 'Insurance', 'Education', 'Family Law') must not route here without 'Md.'/'Maryland'/'Article' context. Section numbers are title-subtitle-section with hyphens, and some subtitles carry a letter (CJP § 3-2A-04, HG § 19-3B-01); the regex accepts a three-part number only when the middle part has a letter, so a range '§§ 10-1601–10-1611' yields 10-1601 (first section), never a fused number. Pages print sections with an EN DASH (§5–101); fetch_doc.py verify normalises dashes. Constitution: 'Md. Const. art. IV, § 14' → mgaleg article c4, section 14; Declaration of Rights 'Md. Const. Decl. of Rts. art. 24' / 'Article 24 of the Maryland Declaration of Rights' → c0, section 24; lettered articles XI-A … XI-I → c11A … c11I. Maryland Rules: 'Md. Rule 2-322(b)' (title-chapter+rule); Attorneys' Rules of Professional Conduct are Title 19 ('Md. Rule 19-301.7' = MARPC 1.7: Rule 1.x → 19-301.x, 2.x → 19-302.x … 8.x → 19-308.x). Bare 'Rule 2-322' must not route here without Maryland context. COMAR 'TT.SS.CC.RR' (title may carry a letter: 13A, 10A); Register Bluebook 'NN Md. Reg. PPP' and COMAR history form 'V:I Md. R. PPP' (volume:issue). Unreported Appellate Court opinions are cited by docket 'No. NNNN, Sept. Term, YYYY (Md. App. date)'; Md. Rule 1-104 lets those issued on or after July 1, 2023 be cited for persuasive value only. Maryland has no public-domain citation. Docket numbers: Supreme Court 'No. N, September Term, YYYY' (term year = the court's term, not the decision year; opinion PDFs sit under the FILING year); Appellate Court 'No. NNNN, September Term, YYYY' (4-digit, zero-padded in URLs). The docket form is shared by both courts and by other bodies using 'Term' dockets: route on it only with Maryland context. Westlaw cites route here only with a '(Md.' parenthetical. Examples marked with round reporter numbers (e.g. '300 A.3d 1 (Md. 2023)', '475 Md. 1') are form examples for the regex, not real citations. CourtListener ids 'md' and 'mdctspecapp' are from memory and unverified.

## A. Statutes / code

### `md-code-mgaleg` — Maryland General Assembly — Statutes Text (Annotated Code of Maryland, by article)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Department of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** All 36 articles of the Annotated Code plus the Constitution (articles c0 = Declaration of Rights, c1-c20). One section per page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article={article}&section={section}&enactments={true|false}`
  - Placeholders: article = three-letter code from the Statutes page table (gcj Courts and Judicial Proceedings, gcr Criminal Law, gcp Criminal Procedure, grp Real Property, ghg Health - General, gsg State Government, gtg Tax - General ... — see citation_map.law_aliases). section = the section number exactly as cited with ASCII hyphens (5-101, 3-2A-04, 8-301.1, 10-1601); no padding. enactments=false shows the law in effect January 1 of this year; enactments=true includes the last session's enactments (in effect October 1) — use true after October 1. A non-existent section returns HTTP 200 with the page heading 'File Not Found', not a 404.
  - Index: `https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes`
- **Automation:** WebFetch gated · shell ok · robots: none (404)
  - WebFetch of the built StatuteText URL returned PROVENANCE_REQUIRED (permission prompt unanswered); no search result surfaced a StatuteText URL, so WebFetch could not be tested on this route. The script route reads the full section (5-101: 8.4K chars of page, section text after the 'Statutes Text' heading).
- **Currency:** Statutes index page radio buttons only; no currency line on section pages — observed: "Yes (Show statutes in effect as of October 1st of this year)"
- **Official status:** No disclaimer or authentication statement on the StatuteText page. Md. Code Ann., State Gov't § 10-1601(d)(3) names DLS as official publisher of the Code, but UELMA (§ 10-1602) applies only to material designated official under § 10-1603; no designation shown on the page.
- **Hazard:** section headings use an en dash (§5–101): exact-match tools must normalise dashes
- **Hazard:** missing section returns 200 'File Not Found' rather than 404
- **Hazard:** enactments=false vs true changes which version is shown (Jan. 1 vs Oct. 1)
- **Hazard:** WebFetch needs per-URL approval for built URLs (gated)
- **Hazard:** page chrome (menus, open-data dialog) surrounds the section text
- **Probe:** Md. Code Ann., Cts. & Jud. Proc. § 5-101 → `https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcj&section=5-101&enactments=true` — expect: "A civil action at law shall be filed within three years"
- **Evidence (2026-10-16):** fetch_doc.py verify: VERIFIED exact 'A civil action at law shall be filed within three years from the date it accrues'. Also Crim. Law § 2-201 ('(a) A murder is in the first degree if it is'), Real Prop. § 8-401, Crim. Proc. § 4-101, Cts. & Jud. Proc. § 3-2A-04, State Gov't § 10-1601, Health-Gen. § 4-301 all body present; gcj 5-1010 → 'File Not Found'.
- **Notes:** Bulk: the same text is published as per-section and per-article PDFs (see md-code-mgaleg-pdf). The site's 'Open Legislative Data' CSV/JSON downloads cover bills only, not statute text.

### `md-code-mgaleg-pdf` — Maryland General Assembly — Statute_Web PDFs (per section and per article)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Department of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** Per-section PDFs and whole-article PDFs for every article and constitution article, in a folder per session year (2019RS … 2027RS observed). The 2027RS folder (files dated Aug.–Sept. 2026) reflects the law after the 2026 session; older folders are frozen snapshots (2024RS c0.pdf still shows Declaration of Rights Art. 48 'NOT IN EFFECT ** SUBJECT TO REFERENDUM NOVEMBER 2024').
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://mgaleg.maryland.gov/{YYYY}RS/Statute_Web/{article}/{section}.pdf  |  whole article: https://mgaleg.maryland.gov/{YYYY}RS/Statute_Web/{article}/{article}.pdf`
  - Placeholders: article = mgaleg code (gcj, grp, c0, c4 ...); section with ASCII hyphens (5-101). YYYY = the NEXT regular session year relative to the text you want: after the 2026 session use 2027RS (Last-Modified Sept. 2026); 2026RS holds text as of Dec. 2025. Check Last-Modified via fetch_doc.py info and prefer the newest folder that exists.
  - Index: `https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: none (404)
  - WebFetch read the 9-page 2024RS c0.pdf (search-result URL) completely. Whole-article PDFs are far beyond the WebFetch window (gcj.pdf 818 pp, 1,728,658 chars) — use the script route or per-section PDFs.
- **Currency:** folder name and HTTP Last-Modified only; nothing inside the PDF — observed: "2027RS/Statute_Web/gcj/gcj.pdf Last-Modified Tue, 01 Sep 2026"
- **Official status:** No authentication statement in the PDFs; see md-code-mgaleg.
- **Hazard:** folder year must be chosen deliberately; old folders are stale snapshots
- **Hazard:** whole-article PDFs exceed the WebFetch window
- **Hazard:** no currency statement inside the PDF
- **Probe:** Md. Code Ann., Cts. & Jud. Proc. § 5-101 → `https://mgaleg.maryland.gov/2027RS/Statute_Web/gcj/5-101.pdf` — expect: "A civil action at law shall be filed within three years"
- **Evidence (2026-10-16):** fetch_doc.py: 2026RS/gcj/5-101.pdf 1 p, body 'A civil action at law shall be filed within three years'; 2027RS/gcj/5-101.pdf 1 p (Last-Modified 01 Sep 2026); 2027RS/grp/8-401.pdf 9 pp; 2027RS/gcj/gcj.pdf 818 pp; 2027RS/c0/c0.pdf 9 pp. WebFetch 2024RS/c0/c0.pdf: Art. 24 'That no man ought to be taken or imprisoned or', not truncated.

### `md-code-justia` — Justia — Maryland Code (2025)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Maryland Code editions incl. 2023, 2024, 2025 (and older years back to 2005); unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/maryland/{article-slug}/title-{title}/subtitle-{subtitle}/section-{section}/`
  - Placeholders: article-slug = article name lower-case hyphenated (courts-and-judicial-proceedings, real-property, criminal-law). title = part before the first hyphen of the section; subtitle = the digit(s)/letters that lead the second part (§ 5-101 → title-5/subtitle-1; § 8-401 → title-8/subtitle-4); lettered subtitles (3-2A-04) untested. section verbatim with hyphens. Year-specific: insert /{year}/ after /maryland/.
  - Index: `https://law.justia.com/codes/maryland/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: fetch_doc.py reports law.justia.com answers robots.txt with a bot check
  - Built section URLs went through WebFetch without a permission prompt.
- **Currency:** page header and Universal Citation line — observed: "2025 Maryland Code; 'MD Courts and Judicial Proceedings Code § 5-101 (2025)'"
- **Official status:** Third-party compilation; edition label '2025 Maryland Code' / '2025 Maryland Statutes'.
- **Hazard:** edition lags the official text (2025 edition; 2026 session changes missing)
- **Hazard:** shell blocked by bot challenge
- **Hazard:** subtitle slug for lettered subtitles not verified
- **Probe:** Md. Code Ann., Cts. & Jud. Proc. § 5-101 → `https://law.justia.com/codes/maryland/courts-and-judicial-proceedings/title-5/subtitle-1/section-5-101/` — expect: "A civil action at law shall be filed within three"
- **Evidence (2026-10-16):** WebFetch: YES, 'A civil action at law shall be filed within three', '2025 Maryland Code', not truncated. Second: /real-property/title-8/subtitle-4/section-8-401/ YES '(a) Whenever the tenant or tenants fail to pay the', '2025 Maryland Statutes'.

## B. Constitution

### `md-constitution-mgaleg` — Maryland Constitution and Declaration of Rights (mgaleg Statutes Text)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Department of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** Declaration of Rights (c0) and Articles I-XX (c1 … c20, incl. XI-A … XI-I as c11A … c11I); one section per page.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article={c_code}&section={section}&enactments=true`
  - Placeholders: Declaration of Rights article N → article=c0&section=N. Constitution art. IV, § 14 → article=c4&section=14 (Roman → Arabic, letter suffix kept upper-case: XI-A → c11A). Article X (repealed) has no code in the table. Whole-article PDF: https://mgaleg.maryland.gov/{YYYY}RS/Statute_Web/c0/c0.pdf (see md-code-mgaleg-pdf).
  - Index: `https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes`
- **Automation:** WebFetch gated · shell ok · robots: none (404)
  - Same host and behaviour as md-code-mgaleg.
- **Currency:** none on the page
- **Official status:** State Gov't § 10-1601(d)(1) names DLS official publisher of the Constitution; no UELMA designation or authentication statement on the page.
- **Hazard:** Roman-to-Arabic article mapping needed
- **Hazard:** built URLs gated for WebFetch
- **Probe:** Md. Const. Decl. of Rts. art. 24 → `https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=c0&section=24&enactments=false` — expect: "That no man ought to be taken or imprisoned or disseized"
- **Evidence (2026-10-16):** fetch_doc.py: 'Article - Declaration of Rights … §24. That no man ought to be taken or imprisoned or disseized'. Second: c4 § 14 'The Supreme Court of Maryland shall be composed of seven justices'.

### `md-constitution-msa` — Maryland Manual — Constitution of Maryland (Maryland State Archives)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland State Archives · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole Constitution, one page per article with amendment notes; 'with Amendments through Two Thousand and Twenty-Four'.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://msa.maryland.gov/msa/mdmanual/43const/html/{page}.html`
  - Placeholders: page = 00dec (Declaration of Rights); other articles appear to follow NNartR (04art4 = Article IV) — only 00dec and 04art4 were seen; confirm from https://msa.maryland.gov/msa/mdmanual/43const/html/const.html.
  - Index: `https://msa.maryland.gov/msa/mdmanual/43const/html/const.html`
  - Navigation: const.html → article page
- **Automation:** WebFetch ok · shell http-error · robots: not read
  - fetch_doc.py gets HTTP 200 (22,611 bytes) but its text extractor returns 0 characters (the page's HTML is malformed: <head> never closed), so grep/verify cannot work on this host. WebFetch reads it fine.
- **Currency:** page header and footer — observed: "with Amendments through Two Thousand and Twenty-Four; Copyright April 25, 2025"
- **Official status:** Reference copy in the Maryland Manual; DLS, not the Archives, is the statutory official publisher (State Gov't § 10-1601(d)(1)).
- **Hazard:** script extractor returns empty text
- **Hazard:** reference copy, not the official publisher
- **Probe:** Md. Const. Decl. of Rts. art. 24 → `https://www.msa.maryland.gov/msa/mdmanual/43const/html/00dec.html` — expect: "That no man ought to be taken or imprisoned or"
- **Evidence (2026-10-16):** WebFetch: YES, Art. 24 'That no man ought to be taken or imprisoned or'; 'with Amendments through Two Thousand and Twenty-Four'; complete through Art. 48. fetch_doc.py: 200, chars=0.
- **Notes:** Use as WebFetch second source for the Constitution, since mgaleg built URLs are gated for WebFetch.

### `md-constitution-justia` — Justia — Maryland Constitution

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Declaration of Rights on /00dec.html; other articles on sibling pages.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Declaration of Rights page is /constitution/maryland/00dec.html; other article slugs not verified.
  - Index: `https://law.justia.com/constitution/maryland/`
  - Navigation: index → article page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
- **Currency:** disclaimer — observed: "This Constitution may not be the most recent version."
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** possibly stale
- **Hazard:** shell blocked
- **Probe:** Md. Const. Decl. of Rts. art. 24 → `https://law.justia.com/constitution/maryland/00dec.html` — expect: "That no man ought to be taken or imprisoned or"
- **Evidence (2026-10-16):** WebFetch: YES, 'That no man ought to be taken or imprisoned or'; last article visible Art. 47 (official text has Art. 48 — Justia copy appears stale).
- **Notes:** Justia ends at Art. 47 while mgaleg/MSA include Art. 48 (2024 amendment): prefer tier 1.

## C. Court rules

### `md-rules-orders` — Rules Orders and Rules Committee Reports (amendments to the Maryland Rules)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Maryland / Standing Committee on Rules of Practice and Procedure · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules Orders and Reports listed on /rules/ruleschanges (228th Report, 2026, back through earlier reports); older orders under /sites/default/files/import/rules/rodocs/.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.mdcourts.gov/sites/default/files/rules/order/ro{N}th.pdf`
  - Placeholders: N = Rules Committee report number (ro227th.pdf); file names vary (ro228th_0.pdf, rorule16-310.pdf) — take the link from the index.
  - Index: `https://www.mdcourts.gov/rules/ruleschanges`
  - Navigation: ruleschanges → 'Rules Order' link for the report → PDF; search the PDF for the rule number
- **Automation:** WebFetch untested · shell ok · robots: mdcourts.gov: User-agent * disallows /core/, /profiles/, /admin/, /search/, /user/* and README files; /rules and /sites/default/files allowed
  - WebFetch not tried (stopped after a 429). Orders are long (ro227th.pdf 173 pp, 226K chars).
- **Currency:** ruleschanges index (report and order dates) — observed: "228th Report … Rules Order 06/04/2026"
- **Official status:** Court orders adopting amendments; they set out only the amended rules, not a consolidated text.
- **Hazard:** amendment text only (underline/strike-through formatting lost in text extraction)
- **Hazard:** file names irregular
- **Hazard:** long PDFs
- **Probe:** 227th Rules Order (amending Md. Rule 2-305 et al.) → `https://www.mdcourts.gov/sites/default/files/rules/order/ro227th.pdf` — expect: "IN THE SUPREME COURT OF MARYLAND RULES ORDER"
- **Evidence (2026-10-16):** fetch_doc.py: application/pdf 173 pp, 226,155 chars; begins 'IN THE SUPREME COURT OF MARYLAND RULES ORDER'; lists amendments to Rules 2-305 … 20-504.

### `md-rules-westlaw` — Maryland Rules of Procedure (Westlaw government site)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Court of Maryland, hosted by Thomson Reuters Westlaw · text: **link-only** · official: unknown
- **Coverage:** Maryland Rules Titles 1-20 (only free full-text source).
- **Access:** `link-only` · format html
  - Index: `https://govt.westlaw.com/mdc/Index?bhcp=1&transitionType=Default&contextData=(sc.Default)`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: fetch_doc.py: govt.westlaw.com answers robots.txt with a bot check
  - WebFetch of the link taken from mdcourts.gov/rules returned PROVENANCE_REQUIRED (not attempted further). Other records (CA, NY) record WebFetch SITE_BLOCKED on govt.westlaw.com.
- **Currency:** not reachable
- **Official status:** State Gov't § 10-1601(d)(4) names the Supreme Court official publisher of the Maryland Rules; the Rules Committee page says 'The Maryland Rules are available through Westlaw.'
- **Hazard:** host refuses automated access
- **Hazard:** no tier-2 copy exists
- **Probe:** Md. Rule 2-322(b) → `https://govt.westlaw.com/mdc/Index?bhcp=1&transitionType=Default&contextData=(sc.Default)`
- **Evidence (2026-10-16):** fetch_doc.py: 'REFUSED: govt.westlaw.com answers robots.txt with a bot check (challenge)'. Not retried by any route.
- **Notes:** Rule text can only be linked, not quoted, unless it appears in a Rules Order (md-rules-orders) or is quoted in an opinion.

## D. Administrative code

### `md-comar-regs` — Library of Maryland Regulations — COMAR (regs.maryland.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Division of State Documents (Open Law Library platform) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All COMAR titles; one regulation per page; chapter pages list regulations. Old dsd.maryland.gov/regulations/Pages/{cite}.aspx URLs redirect here.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://regs.maryland.gov/us/md/exec/comar/{title}.{subtitle}.{chapter}.{regulation}`
  - Placeholders: Use the COMAR number verbatim: 26.08.02.03, 13A.03.02.01, 26.08.02.03-2 (title letters upper-case, two-digit parts). Drop the regulation for the chapter table of contents (/26.08.02); /comar/{title} is the title index. Subsection letters (01B(2)) are on the regulation page.
  - Index: `https://regs.maryland.gov/us/md/exec/comar`
- **Automation:** WebFetch untested · shell ok · robots: regs.maryland.gov: User-agent * Disallow /_* (Cloudflare-managed block also disallows meta-externalagent); dsd.maryland.gov: disallows /_vti_bin/, /_layouts/, /_catalogs/
  - No search result surfaced a regs.maryland.gov URL, so WebFetch was not tried. Footer: 'Please do not scrape. Instead, bulk download' — single-page lookups are fine; for anything bulk use the GitHub repositories.
- **Currency:** home page paragraph — observed: "is current as of October 12, 2026"
- **Official status:** Home page: 'The text appearing here is not the official text'; only text obtained directly from DSD is official (https://regs.maryland.gov/).
- **Hazard:** unofficial text (DSD print/PDF is official)
- **Hazard:** publisher asks not to scrape; bulk via GitHub
- **Hazard:** very long regulations (26.08.02.03-2 is 173K chars)
- **Probe:** COMAR 26.08.02.03 → `https://regs.maryland.gov/us/md/exec/comar/26.08.02.03` — expect: "Surface water quality criteria shall apply"
- **Evidence (2026-10-16):** fetch_doc.py: '.03 Surface Water Quality Criteria. A. Applicability. (1) Surface water quality criteria shall apply'. Second: 13A.03.02.01 '.01 Scope. A. This chapter sets out the enrollment, credit'; 10.09.10.01 Definitions present.
- **Notes:** Licence: CC BY-NC-SA 4.0, becoming CC0 180 days after publication. Bulk: github.com/maryland-dsd/law-xml-codified (and -cc0), law-html (and -cc0).

### `md-comar-lii` — Cornell LII — Maryland Code of Regulations

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** COMAR per regulation with Md. R. history notes.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/maryland/COMAR-{title}-{subtitle}-{chapter}-{regulation}`
  - Placeholders: Dots become hyphens: COMAR 26.08.02.03 → COMAR-26-08-02-03. Chapter browse: /regulations/maryland/title-{title}/subtitle-{subtitle}/chapter-{title}.{subtitle}.{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/maryland`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - WebFetch read the chapter page (search URL) but a following WebFetch of /COMAR-08-03-01-01 returned HTTP 429 (rate limited) — respect the crawl delay.
- **Currency:** Notes section — observed: "State regulations are updated quarterly; Notes '(31:13 Md. R. 995)'"
- **Official status:** 'State regulations are updated quarterly; we currently have two versions available.'
- **Hazard:** quarterly lag
- **Hazard:** HTTP 429 when fetched in quick succession
- **Probe:** COMAR 26.08.02.03 → `https://www.law.cornell.edu/regulations/maryland/COMAR-26-08-02-03` — expect: "Surface water quality criteria shall apply"
- **Evidence (2026-10-16):** fetch_doc.py: body 'A. Applicability. (1) Surface water quality criteria shall apply'; Notes through '(31:13 Md. R. 995)'; Last-Modified 02 Aug 2025. WebFetch: chapter-08.03.01 page OK (TOC only); COMAR-08-03-01-01 → 429.

## D. Administrative register

### `md-register-dsd` — Maryland Register Online (Division of State Documents)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Division of State Documents, Office of the Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Only the 15 most recent biweekly issues (on 2026-10-16: Vol. 53 Issue 7, Apr. 3, 2026 to Issue 21, Oct. 16, 2026). Older issues 404.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://dsd.maryland.gov/MDRIssues/{volume}{issue:02d}/Assembled.aspx`
  - Placeholders: Vol. 53 Issue 20 → 5320. Register page numbers appear only in the issue's table of contents, not in the body text, so a 'NN Md. Reg. PPP' cite must be located through the TOC entry whose page range covers PPP. Issues older than the 15-issue window are not free (404).
  - Index: `https://dsd.maryland.gov/Pages/MDRegister.aspx`
- **Automation:** WebFetch untested · shell ok · robots: Disallow /_vti_bin/, /_layouts/, /_catalogs/ only
  - Search results still list older Assembled.aspx URLs (5110, 5021) that now 404. Issues are ~290K chars: beyond the WebFetch window.
- **Currency:** issue header — observed: "Issue Date: October 2, 2026 Volume 53 • Issue 20 • Pages 975 — 1030"
- **Official status:** Issue text: 'The Maryland Register is an official State publication'; the online HTML carries a DSD certification paragraph but no UELMA authentication statement.
- **Hazard:** rolling 15-issue window
- **Hazard:** no page markers in body
- **Hazard:** long pages exceed WebFetch window
- **Probe:** 53 Md. Reg. 975 (Oct. 2, 2026) → `https://dsd.maryland.gov/MDRIssues/5320/Assembled.aspx` — expect: "Volume 53 • Issue 20 • Pages 975"
- **Evidence (2026-10-16):** fetch_doc.py: 292,854 chars, 'Issue Date: October 2, 2026 Volume 53 • Issue 20 • Pages 975 — 1030'; /5306, /5301, /5110 → 404.
- **Notes:** regs.maryland.gov/us/md/exec/register lists Vol. 52-53 but its issue pages say Register publishing 'was not yet supported' (see absent).

## E. Case law

### `md-opinions-reported` — Maryland Appellate Court Opinions (reported) — mdcourts.gov

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Judiciary · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court of Maryland (formerly Court of Appeals) and Appellate Court of Maryland (formerly Court of Special Appeals) reported opinions, filing years 1995-2026; includes per curiam orders, attorney-grievance and bar orders.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.mdcourts.gov/data/opinions/{coa|cosa}/{filing_year}/{docket_file}.pdf`
  - Placeholders: Index (plain GET): https://www.mdcourts.gov/cgi-bin/indexlist.pl?court={coa|cosa|both}&year={YYYY|all}&order={bydate|bycase|bycite|byjudge|bytitle}&submit=Submit — rows give docket/term, Md./Md. App. cite (or 'slip.op'), filing date, judge, parties, and the PDF link. File names: Supreme Court No. N, Sept. Term 20TT → {N}a{TT}.pdf (5a24, 7a23); suffixes for other dockets: ag = attorney grievance (33a24ag), pc = per curiam order (5a24mpc), o = order (30a22o). Appellate Court No. NNNN, Sept. Term 20TT → {NNNN:04d}s{TT}.pdf (1991s23, 0311s24). The folder is the FILING year, not the term (Syed v. Lee, No. 7, Sept. Term 2023, filed 2024 → /coa/2024/7a23.pdf). If the filing year is unknown, use the index with order=bycite or bytitle.
  - Index: `https://www.mdcourts.gov/opinions/opinions`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * — disallows /core/, /profiles/, /admin/, /search/, /user/*, /media/oembed and README files; /cgi-bin/indexlist.pl and /data/opinions allowed
  - WebFetch not tried on this host (stopped after a 429 elsewhere). Long opinions (Syed v. Lee: 187 pp, 375K chars) exceed the WebFetch window; use the script route.
- **Currency:** index page timestamp line — observed: "2024 Index Listing of Supreme Court of Maryland Opinions Sat Oct 17 02:29:29 EDT 2026"
- **Official status:** mdcourts.gov/opinions/opinions: opinions posted on or after July 1, 2018 are the official and authentic text under UELMA; earlier postings defer to the bound Md. / Md. App. reports. PDFs carry 'Pursuant to the Maryland Uniform Electronic Legal Materials Act … this document is authentic.'
- **Hazard:** slip pagination only — PDFs do not carry Md. / Md. App. page numbers (Hollins PDF has no '489 Md.')
- **Hazard:** folder = filing year, not term year
- **Hazard:** docket suffixes (ag, pc, mpc, o)
- **Hazard:** very long opinions exceed WebFetch window
- **Hazard:** URLs still say coa/cosa after the 2022 renaming
- **Probe:** Hollins v. State, 489 Md. 296 (2024) (No. 5, Sept. Term 2024) → `https://www.mdcourts.gov/data/opinions/coa/2024/5a24.pdf` — expect: "Isiah A. Hollins v. State of Maryland, No. 5, September Term, 2024"
- **Evidence (2026-10-16):** indexlist.pl coa 2024 (GET) → row '5/24 489 Md. 296 2024-12-23 Killough Hollins v. State' linking /data/opinions/coa/2024/5a24.pdf; PDF 23 pp, headnote 'Isiah A. Hollins v. State of Maryland, No. 5, September Term, 2024', UELMA authentication line, no Md. page cite. Second: cosa 2025 → /data/opinions/cosa/2025/1991s23.pdf 17 pp 'Midaro Investments 2021, LLC v. Ari Gerzowski'. coa 1995 and cosa 2016 indexes list Md./Md. App. cites.
- **Notes:** The index's order=bycite listing maps an official cite (e.g. 231 Md. App. 398) to its PDF.

### `md-opinions-unreported` — Unreported Opinions of the Appellate Court of Maryland — mdcourts.gov

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full text for opinions filed May 1, 2015 to date; before that, references only (copies from the Clerk).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.mdcourts.gov/sites/default/files/unreported-opinions/{NNNN:04d}s{TT}.pdf`
  - Placeholders: Monthly list: https://www.mdcourts.gov/appellate/unreportedopinions/list/{YYYYMM} (filing month) — rows: court, filed date, docket, term, judge, appellant, appellee, with the PDF link. Recent files: /sites/default/files/unreported-opinions/{NNNN}s{TT}.pdf (seen for lists 2020-2026); older lists use a year folder: /sites/default/files/unreported-opinions/2016/1063s15.pdf. Take the link from the monthly list rather than guessing.
  - Index: `https://www.mdcourts.gov/appellate/unreportedopinions`
  - Navigation: main directory → month (filing date) → docket link → PDF
- **Automation:** WebFetch untested · shell ok · robots: see md-opinions-reported
- **Currency:** monthly list (latest month) — observed: "Appellate Court of Maryland 09-30-2026 0279 25 Shaw"
- **Official status:** UELMA covers 'a reported decision' (State Gov't § 10-1601(c)(7)); unreported opinions are outside it. Each PDF is marked 'UNREPORTED'.
- **Hazard:** need the filing month to find the list
- **Hazard:** file path varies (year folder for older files)
- **Hazard:** no lookup by party name except by scanning monthly lists
- **Hazard:** citation limits: Md. Rule 1-104 (persuasive only, issued on/after July 1, 2023)
- **Probe:** Farmer v. State, No. 2330, Sept. Term, 2024 (Md. App. Sept. 30, 2026) → `https://www.mdcourts.gov/sites/default/files/unreported-opinions/2330s24.pdf` — expect: "This is an unreported opinion. This opinion may not be cited as precedent"
- **Evidence (2026-10-16):** list/202609 row 'Appellate Court of Maryland 09-30-2026 2330 24 Blomquist Farmer, Maurice State' → 2330s24.pdf, 15 pp: 'UNREPORTED* IN THE APPELLATE COURT OF MARYLAND No. 2330 September Term, 2024'. list/201605 links /2016/1063s15.pdf.

### `md-cases-justia` — Justia — Maryland case law

- **Status:** REPORTED 2026-10-16 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Maryland Supreme Court / Court of Appeals and Appellate Court / Court of Special Appeals opinions (ranges not checked).
- **Access:** `index-anchored` · format html
  - Placeholders: Not verified. Expected year listings under https://law.justia.com/cases/maryland/.
  - Index: `https://law.justia.com/cases/maryland/`
  - Navigation: court → year listing → case page (unverified)
- **Automation:** WebFetch untested · shell blocked-challenge · robots: unreadable (bot check)
  - WebFetch budget not spent here after a 429 elsewhere.
- **Currency:** not checked
- **Official status:** Third-party; not checked this run.
- **Hazard:** shell blocked
- **Hazard:** slug pattern unverified
- **Probe:** Hollins v. State, 489 Md. 296 (2024) → `https://law.justia.com/cases/maryland/`
- **Evidence (2026-10-16):** Not probed. fetch_doc.py check on law.justia.com: REFUSED (bot check). Justia Maryland codes/constitution pages were WebFetch-readable this run.

## F. Subsequent history

### `md-cert-petitions` — Supreme Court of Maryland — Petitions for Writ of Certiorari (monthly grant/deny lists)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Maryland Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Monthly lists 2003-2026: current lists 2023-2026 under /scm/petitions/, archive 2003-2022 under /scm/petitionsarchive (links point to /scm/petitions/ or /coappeals/petitions/ month pages).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.mdcourts.gov/scm/petitions/{YYYYMM}petitions`
  - Placeholders: 2023-2026 months: /scm/petitions/{YYYYMM}petitions. Archive months use either /scm/petitions/{YYYYMM}petitions or /coappeals/petitions/{YYYYMM}petitions (e.g. 202010, 201010) — take the link from /scm/petitionsarchive. Granted entries give caption and new 'No. N, September Term, YYYY' with the questions presented; Denied/Dismissed entries give only caption and 'Pet. No. N' (older: 'Pet. Docket No.'), not the Appellate Court docket.
  - Index: `https://www.mdcourts.gov/scm/petitions`
  - Navigation: petitions index (2023-2026) or petitionsarchive (2003-2022) → month → find the caption
- **Automation:** WebFetch untested · shell ok · robots: see md-opinions-reported
- **Currency:** petitions index (latest month listed) — observed: "2026 September"
- **Official status:** Clerk's informational lists; the dispositions themselves are court orders.
- **Hazard:** found by party name only — denials do not cite the decision below
- **Hazard:** mixed /scm/ and /coappeals/ archive paths
- **Hazard:** month = disposition month, which is not derivable from the decision below
- **Probe:** Manson v. Britto, Pet. No. 207 (Md. Sept. 16, 2026) (cert. denied) → `https://www.mdcourts.gov/scm/petitions/202609petitions` — expect: "Denied/Dismissed September 16, 2026 Manson v. Britto - Pet. No. 207"
- **Evidence (2026-10-16):** fetch_doc.py: 'PETITIONS FOR WRIT OF CERTIORARI September Term, 2026 Denied/Dismissed September 16, 2026 Manson v. Britto - Pet. No. 207'; Granted 'Maria Volpe, et al. v. Christine Hough, et al. – No. 28'. Archive /coappeals/petitions/201010petitions: 'Granted October 25, 2010 State of Maryland v. Anissa Maddox'.
- **Notes:** Cert grants later appear as Supreme Court opinions in md-opinions-reported (opinion caption names the court below). The Supreme Court index rows tagged 'PC Order' are per curiam dispositions.

## Not available (do not look for these again)

- **court_rules** — Free full text of the Maryland Rules on a non-Westlaw host (tier 1 or tier 2): mdcourts.gov/rules says 'The Maryland Rules are available through Westlaw'; search found no LII, Justia or public.law copy (only non-vetted third parties). (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions and the index use only docket/term and Md./Md. App. cites; none seen. (2026-10-16)
- **case_law** — Official reporter (Md. / Md. App.) pagination in free opinion PDFs: Hollins (489 Md. 296) PDF on mdcourts.gov has slip pagination only; the index shows the Md. cite but the PDF does not. (2026-10-16)
- **case_law** — mdcourts.gov opinions filed before 1995; unreported opinion text before May 1, 2015: Year selector ends at 1995; unreported page: 'For opinions filed prior to May 1, 2015, only a reference to the decision is available.' (2026-10-16)
- **admin_register** — Maryland Register issues older than the latest 15, and Register text on regs.maryland.gov: dsd.maryland.gov MDRIssues 5306/5301/5110 → 404; regs.maryland.gov/us/md/exec/register/53/20: 'Register publishing was not yet supported'. (2026-10-16)

## Corpus candidates (maintainers)

- `md-code-mgaleg-pdf` — Whole-article PDFs (gcj 818 pp, 1.73M chars) far exceed the WebFetch window; one PDF per article (36 articles + constitution c0-c20). · bulk: https://mgaleg.maryland.gov/{YYYY}RS/Statute_Web/{article}/{article}.pdf
- `md-comar-regs` — Official bulk XML available; long regulations (26.08.02.03-2: 173K chars). · bulk: https://github.com/maryland-dsd/law-xml-codified

## Open questions

- WebFetch was stopped after an HTTP 429 (LII) per the brief; WebFetch on mdcourts.gov, regs.maryland.gov and dsd.maryland.gov is untested, and mgaleg StatuteText built URLs were gated (PROVENANCE_REQUIRED).
- Which Statute_Web folder (2026RS vs 2027RS) the StatuteText HTML page draws from is not established; compare Last-Modified/content when a section changed in the 2026 session.
- Session laws (Laws of Maryland chapters on mgaleg) not probed.
- Justia Maryland case-law URL pattern and coverage not probed (md-cases-justia reported only).
- Justia statute slug for lettered subtitles (e.g. CJP § 3-2A-04) not tested.
- MSA Constitution article page names beyond 00dec and 04art4 not confirmed.
- CourtListener court ids (md, mdctspecapp) unverified.

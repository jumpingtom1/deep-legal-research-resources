# Louisiana (LA) — free legal sources

_Generated from `data/la.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: legis.la.gov serves every law as a small Law.aspx?d={id} page (unofficial per its disclaimer). The five codes (Civil, Civil Procedure, Criminal Procedure, Evidence, Children's) have GET table-of-contents pages that map article → id, but the Revised Statutes and Constitution TOCs are POST-only, so R.S. ids must be found by web search or read from Justia (constructible, 2025 edition, WebFetch only). Court rules: the Uniform Rules of the Courts of Appeal are an official PDF on fifthcircuit.org; Supreme Court and District Court rules sit on lasc.org, a Blazor app neither tool can read. Admin code: the official LAC (per-part files) and 2026 Register editions are .docx files that fetch_doc.py reads; Cornell LII has a constructible per-section LAC but lags (Aug 2025). Case law: lasc.org is unreadable, so Supreme Court opinions come from Justia (court news-release PDFs on cases.justia.com, script-readable); the Second Circuit has GET year listings (2009–), the Fifth Circuit lists recent PDFs, and the First, Third and Fourth Circuits need JavaScript or POST — use Justia. Writ dispositions (subsequent history) have no readable free source.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Louisiana | `la (unverified)` | La. | So. 3d, So. 2d, So., La. | YYYY-TT-NNNNN (La. M/D/YY), e.g. 2022-K-01824 (La. 12/8/23); older dockets 1998-601 / 2006-2346 |
| Louisiana Court of Appeal, First Circuit | `lactapp (unverified)` | La. App. 1 Cir. | So. 3d, So. 2d | YYYY-NNNN or YYYY CA NNNN (La. App. 1 Cir. M/D/YY) |
| Louisiana Court of Appeal, Second Circuit | `lactapp (unverified)` | La. App. 2 Cir. | So. 3d, So. 2d | NN,NNN (La. App. 2 Cir. M/D/YY), e.g. 56,618 (La. App. 2 Cir. 12/17/25) |
| Louisiana Court of Appeal, Third Circuit | `lactapp (unverified)` | La. App. 3 Cir. | So. 3d, So. 2d | YY-NNN (La. App. 3 Cir. M/D/YY) |
| Louisiana Court of Appeal, Fourth Circuit | `lactapp (unverified)` | La. App. 4 Cir. | So. 3d, So. 2d | YYYY-NNNN (La. App. 4 Cir. M/D/YY) |
| Louisiana Court of Appeal, Fifth Circuit | `lactapp (unverified)` | La. App. 5 Cir. | So. 3d, So. 2d | YY-NNN (La. App. 5 Cir. M/D/YY), e.g. 2022-32 / 26-CA-27 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Louisiana Revised Statutes | `La. R.S. 9:2800`; `La. Rev. Stat. Ann. § 9:2800`; `La. Rev. Stat. § 13:5106(B)(1)`; `LSA-R.S. 14:30.1`; `La.R.S. 9:2800.16`; `Louisiana Revised Statutes 9:2800`; `Section 2800 of Title 9 of the Louisiana Revised Statutes` | `la-rs-legis` → `la-codes-justia` |
| Louisiana Revised Statutes (bare "R.S. 9:2800") *(only once this jurisdiction is known)* | `R.S. 9:2800`; `R.S. 14:30.1`; `R.S. 49:953`; `section 2800.6 of Title 9 of the Revised Statutes`; `Section 2800 of Title 9 of the Revised Statutes` | `la-rs-legis` → `la-codes-justia` |
| Louisiana Civil Code | `La. Civ. Code art. 2315`; `La. Civ. Code Ann. art. 2317.1`; `La. C.C. art. 2315`; `LSA-C.C. art. 1953`; `Louisiana Civil Code article 2315`; `Article 2315 of the Louisiana Civil Code`; `Art. 2315, La. C.C.` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Civil Code (bare "Civil Code article") *(only once this jurisdiction is known)* | `Civil Code article 2315`; `Civil Code Article 2317`; `C.C. art. 2317.1`; `Article 2315 of the Civil Code` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Civil Procedure | `La. Code Civ. Proc. art. 966`; `La. Code Civ. Proc. Ann. art. 966(A)(3)`; `La. C.C.P. art. 966`; `LSA-C.C.P. art. 1915`; `Louisiana Code of Civil Procedure article 966`; `Article 966 of the Louisiana Code of Civil Procedure`; `Art. 2166, La. C.C.P.` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Civil Procedure (bare "C.C.P. art.") *(only once this jurisdiction is known)* | `C.C.P. art. 966`; `Code of Civil Procedure article 966`; `Article 966 of the Code of Civil Procedure` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Criminal Procedure | `La. Code Crim. Proc. art. 894`; `La. Code Crim. Proc. Ann. art. 930.8`; `La. C.Cr.P. art. 894`; `LSA-C.Cr.P. art. 701`; `Louisiana Code of Criminal Procedure article 894`; `Article 894 of the Louisiana Code of Criminal Procedure` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Criminal Procedure (bare) *(only once this jurisdiction is known)* | `C.Cr.P. art. 894`; `Code of Criminal Procedure article 894` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Evidence | `La. Code Evid. art. 702`; `La. Code Evid. Ann. art. 404(B)`; `La. C.E. art. 702`; `LSA-C.E. art. 404(B)`; `Louisiana Code of Evidence article 702`; `Article 702 of the Louisiana Code of Evidence`; `Louisiana Code of Evidence Article 412.2` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Code of Evidence (bare) *(only once this jurisdiction is known)* | `C.E. art. 702`; `Code of Evidence article 702` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Children's Code | `La. Ch.C. art. 101`; `La. Child. Code art. 603`; `La. Ch. Code Ann. art. 1015`; `LSA-Ch.C. art. 101`; `Louisiana Children's Code article 1015` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Children's Code (bare) *(only once this jurisdiction is known)* | `Ch.C. art. 101`; `Children's Code article 603` | `la-codes-legis` → `la-codes-justia` |
| Louisiana Constitution of 1974 | `La. Const. art. I, § 22`; `La. Const. Art. 5, § 10(B)`; `La. Const. of 1974, art. I, § 22`; `La. Const. art. VII, § 14(A)`; `Article I, Section 22 of the Louisiana Constitution` | `la-const-legis` → `la-const-senate-pdf` → `la-const-justia` |
| Louisiana Supreme Court Rules | `La. Sup. Ct. R. X, § 1(a)`; `La. S. Ct. R. VII, § 11`; `Louisiana Supreme Court Rule XIX` | `la-rules-supreme` |
| Louisiana Supreme Court Rules (bare Roman-numbered) *(only once this jurisdiction is known)* | `Supreme Court Rule X, § 5`; `Supreme Court Rule XIX` | `la-rules-supreme` |
| Rules for Louisiana District Courts | `La. Dist. Ct. R. 9.5`; `La. Dist. Ct. Rule 10.1`; `Rule 9.5 of the Rules for Louisiana District Courts`; `Rule 9.10 of the Louisiana District Court Rules` | `la-rules-district` |
| District Court Rules (bare) *(only once this jurisdiction is known)* | `District Court Rule 9.5` | `la-rules-district` |
| Uniform Rules of Louisiana Courts of Appeal | `Uniform Rules of Louisiana Courts of Appeal, Rule 2-18.1`; `La. Unif. R. Ct. App. 2-16.1`; `Rule 2-12.4 of the Uniform Rules of Louisiana Courts of Appeal`; `Uniform Rules, Louisiana Courts of Appeal, Rule 4-3` | `la-rules-urca` |
| Uniform Rules, Courts of Appeal (bare) *(only once this jurisdiction is known)* | `Uniform Rules—Courts of Appeal, Rule 2-18.1`; `Rule 4-3`; `Rule 2-12.4` | `la-rules-urca` |
| Louisiana Administrative Code | `LAC 33:III.501`; `LAC 28:CXV.1103`; `LAC 46:LIII.2511`; `La. Admin. Code tit. 33, § III-501`; `La. Admin. Code tit. 33, pt. III, § 501` | `la-lac-doa` → `la-lac-lii` |
| Louisiana Register ("LR vol:page") *(only once this jurisdiction is known)* | `LR 13:741 (December 1987)`; `LR 51:69` | `la-register-doa` |
| Louisiana public-domain (docket + court/date) citations | `2022-K-01824 (La. 12/8/23)`; `2019-00123 (La. 5/7/19)`; `Cat's Meow v. City of New Orleans, 1998-601, p. 15 (La.10/20/98), 720 So.2d 1186`; `State v. Pinion, 2006-2346 (La. 10/26/07), 968 So.2d 131`; `State v. Sagastume, 2022-32, p. 4 (La. App. 5 Cir. 11/16/22), 353 So.3d 318`; `2020-0456 (La. App. 1 Cir. 3/11/21)`; `56,618 (La. App. 2 Cir. 12/23/25)`; `25-467 (La. App. 3 Cir. 3/27/26)`; `2024-0123 (La. App. 4 Cir. 6/5/24)`; `2026 CW 0629 (La. App. 1 Cir. 8/28/26)` | `la-sc-justia` → `la-sc-lasc` → `la-ca-justia` → `la-ca2-la2nd` → `la-ca5-fifthcircuit` → `la-ca1-lafcca` → `la-ca3-la3circuit` → `la-ca4-la4th` |
| Southern Reporter with Louisiana court parenthetical | `State v. Vanderpool, 493 So.2d 574 (La. 1986)`; `968 So. 2d 131 (La. 2007)`; `353 So. 3d 318 (La. App. 5 Cir. 2022)`; `123 So. 3d 456 (La. App. 1st Cir. 2013)` | `la-sc-justia` → `la-ca-justia` |
| Westlaw cites with Louisiana parenthetical | `2024 WL 123456 (La. App. 1 Cir. 3/1/24)`; `2019 WL 2041234 (La. 5/7/19)` | `la-sc-justia` → `la-ca-justia` |
| Louisiana docket numbers (bare) *(only once this jurisdiction is known)* | `2022-K-01824`; `2026CW0629`; `No. 57,066-CA`; `No. 26-CA-27`; `2025-C-01318` | `la-sc-justia` → `la-ca-justia` → `la-ca2-la2nd` → `la-ca5-fifthcircuit` |
| Southern Reporter (bare) *(only once this jurisdiction is known)* | `720 So. 2d 1186`; `353 So.3d 318` | `la-sc-justia` → `la-ca-justia` |
| Louisiana Supreme Court writ dispositions | `writ denied, 2021-01234 (La. 1/12/22), 330 So. 3d 1234`; `writ granted, 2023-00456 (La. 6/7/23)`; `writ not considered, 2019-01922 (La. 2/10/20)`; `writs denied, 2015-1234 (La. 9/25/15)` | `la-subsequent-lasc` → `la-sc-justia` |
| Writ disposition (bare) *(only once this jurisdiction is known)* | `writ denied`; `writs granted`; `writ not considered` | `la-subsequent-lasc` → `la-sc-justia` |

Regexes (case-insensitive):

- Louisiana Revised Statutes: `(?:\bLa\.?\s*R\.\s*S\.|\bLSA[\s\-–]*R\.\s*S\.|\bLa\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?|Louisiana\s+Revised\s+Statutes(?:\s+of\s+1950)?)\s*(?:§+\s*)?(?P<title>\d{1,2}):(?P<section>\d+(?:\.\d+)?)(?!\d)|(?:Section|§)\s*(?P<section2>\d+(?:\.\d+)?)\s+of\s+Title\s+(?P<title2>\d{1,2})\s+of\s+the\s+Louisiana\s+Revised\s+Statutes`
- Louisiana Revised Statutes (bare "R.S. 9:2800"): `(?<![\w.])R\.\s*S\.\s*(?P<title>\d{1,2}):(?P<section>\d+(?:\.\d+)?)(?!\d)|(?:Section|§)\s*(?P<section2>\d+(?:\.\d+)?)\s+of\s+Title\s+(?P<title2>\d{1,2})\s+of\s+the\s+Revised\s+Statutes`
- Louisiana Civil Code: `(?:\bLa\.\s*Civ(?:il)?\.?\s*Code(?:\s*Ann\.)?|\bLa\.\s*C\.\s*C\.|\bLSA[\s\-–]*C\.\s*C\.|Louisiana\s+Civil\s+Code)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s+of\s+the\s+Louisiana\s+Civil\s+Code|Arts?\.\s*(?P<article3>\d+(?:\.\d+)?),\s*La\.\s*C\.\s*C\.(?!\s*[PR])`
- Louisiana Civil Code (bare "Civil Code article"): `(?:\bCiv(?:il)?\.?\s*Code|(?<![\w.])C\.\s*C\.(?!\s*P))\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s+of\s+the\s+Civil\s+Code`
- Louisiana Code of Civil Procedure: `(?:\bLa\.\s*Code\s*(?:of\s*)?Civ(?:il)?\.?\s*Proc(?:edure)?\.?(?:\s*Ann\.)?|\bLa\.\s*C\.\s*C\.\s*P\.|\bLSA[\s\-–]*C\.\s*C\.\s*P\.|Louisiana\s+Code\s+of\s+Civil\s+Procedure)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s*(?:,|\s+of\s+the)\s*(?:La\.\s*C\.\s*C\.\s*P\.|Louisiana\s+Code\s+of\s+Civil\s+Procedure)`
- Louisiana Code of Civil Procedure (bare "C.C.P. art."): `(?:(?<![\w.])C\.\s*C\.\s*P\.|Code\s+of\s+Civil\s+Procedure|Code\s*Civ\.?\s*Proc\.?)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s+of\s+the\s+Code\s+of\s+Civil\s+Procedure`
- Louisiana Code of Criminal Procedure: `(?:\bLa\.\s*Code\s*(?:of\s*)?Crim(?:inal)?\.?\s*Proc(?:edure)?\.?(?:\s*Ann\.)?|\bLa\.\s*C\.\s*Cr\.\s*P\.|\bLSA[\s\-–]*C\.\s*Cr\.\s*P\.|Louisiana\s+Code\s+of\s+Criminal\s+Procedure)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s*(?:,|\s+of\s+the)\s*(?:La\.\s*C\.\s*Cr\.\s*P\.|Louisiana\s+Code\s+of\s+Criminal\s+Procedure)`
- Louisiana Code of Criminal Procedure (bare): `(?:(?<![\w.])C\.\s*Cr\.\s*P\.|Code\s+of\s+Criminal\s+Procedure)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)`
- Louisiana Code of Evidence: `(?:\bLa\.\s*Code\s*(?:of\s*)?Evid(?:ence)?\.?(?:\s*Ann\.)?|\bLa\.\s*C\.\s*E\.|\bLSA[\s\-–]*C\.\s*E\.|Louisiana\s+Code\s+of\s+Evidence)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)|Art(?:icle|\.)\s*(?P<article2>\d+(?:\.\d+)?)\s*(?:,|\s+of\s+the)\s*(?:La\.\s*C\.\s*E\.|Louisiana\s+Code\s+of\s+Evidence)`
- Louisiana Code of Evidence (bare): `(?:(?<![\w.])C\.\s*E\.|Code\s+of\s+Evidence)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)`
- Louisiana Children's Code: `(?:\bLa\.\s*Ch(?:ild(?:ren'?s)?)?\.?\s*C(?:ode)?\.?(?:\s*Ann\.)?|\bLSA[\s\-–]*Ch\.\s*C\.|Louisiana\s+Children'?s\s+Code)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)`
- Louisiana Children's Code (bare): `(?:(?<![\w.])Ch\.\s*C\.|Children'?s\s+Code)\s*,?\s*(?:arts?\.|articles?)\s*(?P<article>\d+(?:\.\d+)?)`
- Louisiana Constitution of 1974: `\bLa\.\s*Const\.(?:\s*of\s*1974)?,?\s*arts?\.\s*(?P<article>[IVXL]+|\d{1,2}),?\s*§+\s*(?P<section>\d+(?:\.\d+)?)|Article\s+(?P<article2>[IVXL]+|\d{1,2}),?\s+Section\s+(?P<section2>\d+(?:\.\d+)?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+(?:Louisiana\s+Constitution|Constitution\s+of\s+Louisiana)`
- Louisiana Supreme Court Rules: `(?:\bLa\.\s*S(?:up(?:reme)?)?\.?\s*Ct\.?\s*R(?:ule)?\.?|Louisiana\s+Supreme\s+Court\s+Rules?)\s*(?P<rule>[IVXL]+)\b(?:,?\s*§\s*(?P<section>\d+(?:\.\d+)?))?`
- Louisiana Supreme Court Rules (bare Roman-numbered): `Supreme\s+Court\s+Rule\s+(?P<rule>[IVXL]+)\b(?:,?\s*§\s*(?P<section>\d+(?:\.\d+)?))?`
- Rules for Louisiana District Courts: `\bLa\.\s*Dist\.?\s*Ct\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)\s+of\s+the\s+(?:Rules\s+for\s+Louisiana\s+District\s+Courts|Louisiana\s+District\s+Court\s+Rules)`
- District Court Rules (bare): `District\s+Court\s+Rules?\s+(?P<rule>\d+(?:\.\d+)?)`
- Uniform Rules of Louisiana Courts of Appeal: `(?:\bLa\.\s*Unif\.\s*R\.\s*Ct\.?\s*App\.?|Uniform\s+Rules?(?:\s+of|,)?\s+Louisiana\s+Courts?\s+of\s+Appeals?,?\s*Rule)\s*(?P<rule>\d-\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d-\d+(?:\.\d+)?)\s+of\s+the\s+Uniform\s+Rules\s+of\s+(?:the\s+)?Louisiana\s+Courts\s+of\s+Appeal`
- Uniform Rules, Courts of Appeal (bare): `(?:Uniform\s+Rules?\s*(?:—|–|-|,)?\s*(?:of\s+(?:the\s+)?)?Courts?\s+of\s+Appeals?,?\s*Rule\s*(?P<rule>\d-\d+(?:\.\d+)?))|\bRule\s+(?P<rule2>[1-7]-\d+(?:\.\d+)?)\b`
- Louisiana Administrative Code: `\bLAC\s*(?P<title>\d{1,2}):(?P<part>[IVXLC]+)\.(?P<section>\d+(?:\.\d+)?)|\bLa\.\s*Admin\.\s*Code\s*tit\.\s*(?P<title2>\d{1,2}),?\s*(?:pt\.\s*(?P<part2>[IVXLC]+),?\s*§+\s*(?P<section2>\d+)|§+\s*(?P<part3>[IVXLC]+)-(?P<section3>\d+))`
- Louisiana Register ("LR vol:page"): `\bLR\s+(?P<volume>\d{1,2}):(?P<page>\d{1,5})`
- Louisiana public-domain (docket + court/date) citations: `(?P<docket>\b\d{2,4}-(?:[A-Z]{1,3}-)?\d{1,5}|\b\d{2},\d{3}(?:-[A-Z]{2,3})?|\b\d{4}\s*[A-Z]{1,3}\s*\d{3,4})\s*,?\s*(?:p\.\s*\d+\s*,?\s*)?\(La\.\s*(?:App\.\s*(?P<circuit>[1-5])(?:st|nd|rd|th)?\s*Cir\.\s*)?(?P<date>\d{1,2}/\d{1,2}/\d{2,4})\)`
- Southern Reporter with Louisiana court parenthetical: `(?P<volume>\d{1,4})\s+So\.\s*(?:(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>La\.(?:\s*App\.(?:\s*[1-5](?:st|nd|rd|th)?\s*Cir\.)?)?)\s*(?P<year>\d{4})\)`
- Westlaw cites with Louisiana parenthetical: `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(La\.`
- Louisiana docket numbers (bare): `\b(?:19|20)\d\d-[A-Z]{1,2}-\d{4,5}\b|\b(?:19|20)\d\d\s?[A-Z]{2}\s?\d{4}\b|\b\d{2},\d{3}-[A-Z]{2,3}\b|\b\d{2}-[A-Z]{1,2}-\d{1,4}\b`
- Southern Reporter (bare): `(?P<volume>\d{1,4})\s+So\.\s*(?:(?P<series>[23])d)?\s+(?P<page>\d{1,5})`
- Louisiana Supreme Court writ dispositions: `\bwrits?\s+(?P<disposition>denied|granted(?:\s+in\s+part)?|not\s+considered|dismissed)[^()]{0,40}?,\s*(?P<docket>\d{2,4}-(?:[A-Z]{1,3}-)?\d{1,5})\s*\(La\.\s*(?P<date>\d{1,2}/\d{1,2}/\d{2,4})\)`
- Writ disposition (bare): `\bwrits?\s+(?:denied|granted|not\s+considered)\b`

Short forms → URL key:

La. R.S. → `RS`; La.R.S. → `RS`; LSA-R.S. → `RS`; R.S. → `RS`; La. Rev. Stat. → `RS`; La. Rev. Stat. Ann. → `RS`; Louisiana Revised Statutes → `RS`; La. Civ. Code → `CC`; La. Civ. Code Ann. → `CC`; La. C.C. → `CC`; LSA-C.C. → `CC`; C.C. → `CC`; Civil Code → `CC`; La. Code Civ. Proc. → `CCP`; La. Code Civ. Proc. Ann. → `CCP`; La. C.C.P. → `CCP`; LSA-C.C.P. → `CCP`; C.C.P. → `CCP`; Code of Civil Procedure → `CCP`; La. Code Crim. Proc. → `CCRP`; La. Code Crim. Proc. Ann. → `CCRP`; La. C.Cr.P. → `CCRP`; LSA-C.Cr.P. → `CCRP`; C.Cr.P. → `CCRP`; Code of Criminal Procedure → `CCRP`; La. Code Evid. → `CE`; La. Code Evid. Ann. → `CE`; La. C.E. → `CE`; LSA-C.E. → `CE`; C.E. → `CE`; Code of Evidence → `CE`; La. Ch.C. → `CHC`; La. Child. Code → `CHC`; La. Ch. Code Ann. → `CHC`; LSA-Ch.C. → `CHC`; Ch.C. → `CHC`; Children's Code → `CHC`; La. Const. → `CONST`; La. Const. of 1974 → `CONST`

Civil-law jurisdiction: the Civil Code, Code of Civil Procedure, Code of Criminal Procedure, Code of Evidence and Children's Code are cited by ARTICLE ('art.'), never by section; the Revised Statutes are cited title:section ('La. R.S. 9:2800', no § in Louisiana style; Bluebook 'La. Rev. Stat. Ann. § 9:2800'). law_aliases map each code abbreviation to the legis.la.gov TOC folder key. GUARD: Texas, California and other states also have a 'Civil Code', 'Code of Civil Procedure' and 'Code of Criminal Procedure' (Texas cites 'art.' too); bare 'Civil Code article', 'C.C.P. art.', 'Code of Criminal Procedure article', 'C.E. art.' and bare 'R.S. 9:2800' are context_required and route here only with a Louisiana marker (La./LSA-/Louisiana/'(La.' court parenthetical) elsewhere in the query. Louisiana has used a public-domain/vendor-neutral form since 1994 (La. Sup. Ct. Gen. Admin. Rules Part G § 8, from memory): docket number + court + exact date in parentheses, e.g. '2022-K-01824 (La. 12/8/23)', '2022-32 (La. App. 5 Cir. 11/16/22)', '56,618 (La. App. 2 Cir. …)'; the '(La.' / '(La. App. N Cir.' parenthetical is what makes it distinctive. Docket formats differ by court: Supreme Court YYYY-TT-NNNNN (older YYYY-NNNN); 1st Cir. YYYY CA/CW/KA NNNN; 2nd Cir. NN,NNN-CA; 3rd Cir. YY-NNN; 4th Cir. YYYY-CA-NNNN; 5th Cir. YY-CA-NNN. Bare dockets, bare So. 2d/So. 3d (Southern Reporter is shared with AL, FL, MS) and bare 'writ denied' are context_required. Subsequent history in Louisiana is almost always a Supreme Court WRIT disposition ('writ denied, 2021-01234 (La. 1/12/22), 330 So. 3d 1234'), not 'review denied'/'cert. denied'. Court rules: Supreme Court Rules use Roman numerals (Rule X, § 5); District Court Rules decimals (9.5); Uniform Rules of the Courts of Appeal 'N-N.N' (2-18.1). LAC citations use title:part(Roman).section ('LAC 33:III.501'); the Louisiana Register is cited 'LR vol:page'. CourtListener ids are from memory and unverified; CourtListener uses one id ('lactapp') for all five circuits, so filter by circuit in the parenthetical. Prose 'Section N of Title T of the Revised Statutes' without 'Louisiana' is in the context_required bare-R.S. pattern (independent check 2026-10-17).

## A. Statutes / code

### `la-codes-legis` — Louisiana Laws — Civil Code, Code of Civil Procedure, Code of Criminal Procedure, Code of Evidence, Children's Code (legis.la.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana State Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current text of the five codes, one article per Law.aspx page, with amendment history (Acts) at the foot.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://legis.la.gov/legis/Law.aspx?d={doc_id}`
  - Placeholders: doc_id is an internal numeric document id, NOT derivable from the article number (CC 2315 → 109369, CC 1 → 108528, CE 702 → 72506, CCP 966 → 112309, C.Cr.P. 894 → 112888, Ch.C. 101 → 72534). Each code has one GET table-of-contents page listing every article with its Law.aspx?d= link, labelled '{KEY} {article}' (e.g. 'CC 2315', 'CCP 966', 'CCRP 894', 'CE 702', 'CHC 101'). TOC folder ids: CC=67, CCP=68, CCRP=69, CE=70, CHC=71 (also CONST=72 and RS=75 — but those two TOCs are ASP.NET postback-only; see la-rs-legis / la-const-legis). LawPrint.aspx?d={doc_id} is a print view with the same body.
  - Index: `https://legis.la.gov/legis/Laws_Toc.aspx?folder={folder}&level=Parent`
  - Navigation: Laws_Toc.aspx?folder={67|68|69|70|71}&level=Parent → link whose text is exactly '{KEY} {article}' (fetch_doc.py links URL '^CC 2315$' --regex) → Law.aspx?d={id} holds the article body. The Civil Code TOC is one ~867K-character page (5,034 links): use fetch_doc.py links with a filter, not the fetch tool.
- **Automation:** WebFetch ok · shell ok · robots: none (404 on legis.la.gov and www.legis.la.gov)
  - Law.aspx pages are small (1.6–10K chars) so neither tool truncates. The Civil Code TOC (~867K chars) far exceeds the fetch tool's window; resolve article→id with the script. WebFetch was tested only on a search-result URL (it worked); built Law.aspx URLs may need per-URL approval, so the script is primary. legis.la.gov and www.legis.la.gov serve the same pages; 'Legis'/'legis' path case is ignored.
- **Currency:** LawSearch.aspx page header (not on Law.aspx pages); lags the article pages — use the Acts history at the foot of each page — observed: "Laws have been updated through the 2025 First Extraordinary Session."
- **Official status:** LawSearch.aspx 'Disclaimer': provisions 'have not been edited for publication and are not official or authoritative' (https://legis.la.gov/legis/LawSearch.aspx).
- **Hazard:** document id not derivable from the article number (TOC hop required)
- **Hazard:** Civil Code TOC page ~867K characters — far beyond the fetch tool window
- **Hazard:** no currency line on the article pages themselves
- **Hazard:** site disclaims official/authoritative status
- **Hazard:** LawSearch 'updated through the 2025 First Extraordinary Session' line understates currency: pages already carry Acts 2026 history (e.g. RS 14:30.1)
- **Probe:** La. Civ. Code art. 2315 → `https://legis.la.gov/legis/Law.aspx?d=109369` — expect: "Every act whatever of man that causes damage to another"
- **Evidence (2026-10-17):** Script: CC TOC folder=67 link 'CC 2315' → d=109369; body 'Art. 2315. Liability for acts causing damages A. Every act whatever of man'. Also CE 702 (d=72506) 'A witness who is qualified as an expert'; CCP 966 (d=112309) 'A party may move for a summary judgment'; C.Cr.P. 894 (d=112888) body present. | Independent check 2026-10-17: Script verify exact: 'Every act whatever of man that causes damage to another' (2,540 chars); second citation La. Code Crim. Proc. art. 930.8 ok
- **Notes:** Folder TOCs for CC/CCP/CCRP/CE/CHC are plain GET pages with direct Law.aspx links; this is the deterministic route for the codes.

### `la-rs-legis` — Louisiana Revised Statutes (legis.la.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana State Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current Revised Statutes (Titles 1–56), one section per Law.aspx page, with Acts history.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format html
  - Pattern: `https://legis.la.gov/legis/Law.aspx?d={doc_id}`
  - Placeholders: doc_id is an internal numeric id not derivable from title:section (9:2800 → 107250, 9:2800.16 → 408378, 9:1590 → 106718, 9:229 → 107045). Page heading reads 'RS {title}:{section}'. The RS title TOC (folder=75) and the 'View a Specific Law' box on LawSearch.aspx (law body RS + Title + Section) are ASP.NET POST postbacks — no GET URL reaches a section. Justia's 2006 edition uses the same ids (law.justia.com/codes/louisiana/2006/123/107250.html = RS 9:2800) but only for sections that existed in 2006.
  - Index: `https://legis.la.gov/legis/LawSearch.aspx`
  - Navigation: Find the id with a web search for the page heading: site:legis.la.gov "RS 9:2800" (exact heading form 'RS {title}:{section}'), or the section catchline + 'Law.aspx'; confirm the 'RS t:s' heading on the fetched page. If no id is found, use la-codes-justia (constructible) instead. Never guess ids.
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - Search-result Law.aspx URLs pass the fetch tool; built ones may be gated, so prefer the script. A bare site: search for 'RS 9:2800' returned wrong sections; adding the catchline found it.
- **Currency:** LawSearch.aspx page header (not on Law.aspx pages); lags the article pages — use the Acts history at the foot of each page — observed: "Laws have been updated through the 2025 First Extraordinary Session."
- **Official status:** LawSearch.aspx 'Disclaimer': provisions 'have not been edited for publication and are not official or authoritative' (https://legis.la.gov/legis/LawSearch.aspx).
- **Hazard:** no GET route from citation to page (POST-only TOC and lookup form)
- **Hazard:** web-search discovery is unreliable — always confirm the 'RS t:s' heading
- **Hazard:** no currency line on section pages
- **Hazard:** LawSearch 'updated through the 2025 First Extraordinary Session' line understates currency: pages already carry Acts 2026 history (e.g. RS 14:30.1)
- **Hazard:** duplicate live ids for one section: RS 14:30.1 is at d=150048 and d=78398 (same text, differently formatted Acts history; only 150048 shows eff. dates) — prefer the id whose history lists effective dates and matches LawPrint, and always confirm the 'RS t:s' heading
- **Probe:** La. R.S. 9:2800 → `https://legis.la.gov/Legis/Law.aspx?d=107250` — expect: "A public entity is responsible under Civil Code Article 2317"
- **Evidence (2026-10-17):** Script and WebFetch: heading 'RS 9:2800', body 'A. A public entity is responsible under Civil Code Article'; not truncated (4,605 chars). Also LawPrint.aspx?d=107250 same body; RS 9:1590 (d=106718) body present. | Independent check 2026-10-17: Script verify exact: 'A public entity is responsible under Civil Code Article 2317' (4,605 chars); second citation La. R.S. 14:30.1 ok
- **Notes:** Ask the skill maintainers whether a script that drives the LawSearch POST form (ddlLawBodies=RS, tbFirstNumber, tbSecondNumber) is acceptable; it would make RS deterministic.

### `la-codes-justia` — Justia — Louisiana Laws (Revised Statutes and codes, 2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Revised Statutes, Children's Code, Civil Code, Code of Civil Procedure, Code of Criminal Procedure, Code of Evidence; editions 2006, 2009, 2011–2025. No constitution in this tree.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/louisiana/{body}/{item}/`
  - Placeholders: RS: body='revised-statutes/title-{title}', item='rs-{title}-{section}' (La. R.S. 9:2800 → /revised-statutes/title-9/rs-9-2800/). Codes: body ∈ civil-code, code-of-civil-procedure, code-of-criminal-procedure, code-of-evidence, children-s-code; item='article-{article}' (CC 2315 → /civil-code/article-2315/; CE 702 → /code-of-evidence/article-702/). Unversioned URL = 2025 edition; insert /{year}/ after /louisiana/ for older editions. Decimal points become hyphens: La. R.S. 14:30.1 → /revised-statutes/title-14/rs-14-30-1/ (verified); presumably CC 2317.1 → /civil-code/article-2317-1/ (untested).
  - Index: `https://law.justia.com/codes/louisiana/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com refused the script with a bot challenge on robots.txt (host off for the day, 2026-10-17)
  - Built Justia URLs went through WebFetch without an approval prompt. Use WebFetch only.
- **Currency:** edition label in page header/breadcrumb — observed: "2025 Louisiana Laws"
- **Official status:** Third-party compilation; editions labelled by year ('2025 Louisiana Laws').
- **Hazard:** lags the official site by up to a year
- **Hazard:** shell blocked by bot challenge
- **Probe:** La. Civ. Code art. 2315 → `https://law.justia.com/codes/louisiana/civil-code/article-2315/` — expect: "Every act whatever of man that causes damage to another"
- **Evidence (2026-10-17):** WebFetch: CC 2315 body present, '2025 Louisiana Laws'; RS 9:2800 at /revised-statutes/title-9/rs-9-2800/ ('A public entity is responsible under Civil Code Article 2317'); CE 702 at /code-of-evidence/article-702/ body present. | Independent check 2026-10-17: WebFetch: 'Every act whatever of man that causes damage to another'; '2025 Louisiana Laws'; not truncated; second citation La. R.S. 14:30.1 ok
- **Notes:** Constructible fallback for Revised Statutes when no legis.la.gov id can be found.

## B. Constitution

### `la-const-legis` — Louisiana Constitution of 1974 (legis.la.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana State Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1974 as amended, one section per Law.aspx page; amendments table PDF at /LegisDocs/ConstAmend/Constitution_Amendments_Table.pdf.
- **Read via (in order):** **script**
- **Access:** `search-only` · format html
  - Pattern: `https://legis.la.gov/legis/Law.aspx?d={doc_id}`
  - Placeholders: Page heading 'CONST {article} {section}' (Arabic article number), e.g. 'CONST 1 22' = Art. I, § 22 → d=206288. The constitution TOC (folder=72) lists ARTICLE 1–14 as POST postbacks only.
  - Index: `https://legis.la.gov/legis/Laws_Toc.aspx?folder=72&level=Parent`
  - Navigation: Web search: legis.la.gov Law.aspx "CONST 1 22" (or the section catchline) → confirm heading. Otherwise read la-const-senate-pdf or la-const-justia.
- **Automation:** WebFetch untested · shell ok · robots: none (404)
- **Currency:** LawSearch.aspx page header (not on Law.aspx pages); lags the article pages — use the Acts history at the foot of each page — observed: "Laws have been updated through the 2025 First Extraordinary Session."
- **Official status:** LawSearch.aspx 'Disclaimer': provisions 'have not been edited for publication and are not official or authoritative' (https://legis.la.gov/legis/LawSearch.aspx).
- **Hazard:** section ids not derivable; TOC is postback-only
- **Hazard:** LawSearch 'updated through the 2025 First Extraordinary Session' line understates currency: pages already carry Acts 2026 history (e.g. RS 14:30.1)
- **Probe:** La. Const. art. I, § 22 → `https://legis.la.gov/legis/Law.aspx?d=206288` — expect: "All courts shall be open, and every person shall have an adequate remedy"
- **Evidence (2026-10-17):** Script: heading 'CONST 1 22', '§22. Access to Courts Section 22. All courts shall be open'. | Independent check 2026-10-17: Script verify exact: 'All courts shall be open, and every person shall have an adequate remedy'; second citation La. Const. art. V, § 10 ok

### `la-const-senate-pdf` — Louisiana Constitution of 1974 — Senate compilation (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana State Senate · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution, 108 pages, as amended through calendar year 2023 (dated January 8, 2024). An older 133-page edition (2019) sits at /Documents/Constitution/constitution.pdf.
- **Read via (in order):** **script**
- **Access:** `link-only` · format pdf
  - Placeholders: single PDF
  - Index: `https://senate.la.gov/Documents/LAConstitution.pdf`
  - Navigation: fetch_doc.py grep the PDF for 'Section {n}.' near the article heading
- **Automation:** WebFetch untested · shell ok · robots: User-agent:* Allow:/ Disallow: /private/
  - 683K characters of extracted text — beyond the fetch tool window. Two-column layout: layout extraction interleaves the columns, so verify short quotes only or use the raw (reading-order) text.
- **Currency:** cover page — observed: "(As amended through calendar year 2023)"
- **Official status:** Cover: 'Compiled from the Louisiana Senate Statutory Database'; no authentication statement.
- **Hazard:** two-column layout interleaves text in extraction
- **Hazard:** does not include amendments adopted after 2023 (stale vs legis.la.gov)
- **Hazard:** far exceeds fetch tool window
- **Probe:** La. Const. art. I, § 22 → `https://senate.la.gov/Documents/LAConstitution.pdf` — expect: "All courts shall be open, and every"
- **Evidence (2026-10-17):** Script: PDF 108 pp, last-modified 30 Jan 2024; cover 'Louisiana Constitution of 1974 … January 8, 2024'; grep found Art. I § 22 on page 15 (columns interleaved). | Independent check 2026-10-17: Script grep p.15 'Section 22. All courts shall be open, and every' (columns interleaved); cover '(As amended through calendar year 2023)'
- **Notes:** Corpus candidate only after a newer edition is published; check for post-2023 amendments on legis.la.gov first.

### `la-const-justia` — Justia — Louisiana Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1974, one page per article.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/louisiana/Article{article_arabic}.html`
  - Placeholders: article as Arabic numeral (Art. I → Article1.html, Art. V → Article5.html); sections are anchors on the article page.
  - Index: `https://law.justia.com/constitution/louisiana/`
  - Navigation: index is TOC only
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot challenge)
- **Currency:** page disclaimer — observed: "This Constitution may not be the most recent version."
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** edition undated; may predate recent amendments
- **Hazard:** shell blocked
- **Probe:** La. Const. art. I, § 22 → `https://law.justia.com/constitution/louisiana/Article1.html` — expect: "All courts shall be open, and every person shall have an adequate"
- **Evidence (2026-10-17):** WebFetch: Art. I § 22 body present, page complete through § 27; index page is TOC only. | Independent check 2026-10-17: WebFetch: 'All courts shall be open, and every person shall have'; disclaimer 'may not be the most recent version'; second citation La. Const. art. V, § 10 ok

## C. Court rules

### `la-rules-district` — Rules for Louisiana District Courts (lasc.org)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of Louisiana · text: **link-only** · official: unknown
- **Coverage:** Rules for Louisiana District Courts (Titles I–IV) and appendices — per memory.
- **Access:** `link-only` · format html
  - Index: `https://www.lasc.org/`
  - Navigation: unknown (Blazor app)
- **Automation:** WebFetch fail · shell http-error · robots: none (Blazor shell served for /robots.txt)
  - Script: 200 with 0 extractable characters on every path (content rendered over SignalR). WebFetch (independent check 2026-10-17) returned promptly with only base/viewport metadata — empty Blazor shell; an earlier WebFetch timed out on the approval prompt.
- **Currency:** none observed
- **Official status:** Not reached (lasc.org Blazor app).
- **Hazard:** JavaScript app
- **Probe:** La. Dist. Ct. R. 9.5 → `https://www.lasc.org/`
- **Evidence (2026-10-17):** Not reachable as text; web search surfaced only a non-vetted third-party copy (courtrules.net, not used). | Independent check 2026-10-17: WebFetch www.lasc.org: no visible text, only base/viewport metadata (shared fetch for 4 lasc rows)

### `la-rules-supreme` — Louisiana Supreme Court Rules (lasc.org)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of Louisiana · text: **link-only** · official: unknown
- **Coverage:** Rules I–XXXIX of the Supreme Court (writ applications Rule X, etc.) — per memory.
- **Access:** `link-only` · format html
  - Index: `https://www.lasc.org/`
  - Navigation: unknown: every lasc.org path returns the same empty Blazor shell to a plain GET
- **Automation:** WebFetch fail · shell http-error · robots: none: /robots.txt returns the empty Blazor HTML shell (200), no rules
  - Script: 200 with 0 extractable characters on every path (content rendered over SignalR). WebFetch (independent check 2026-10-17) returned promptly with only base/viewport metadata — empty Blazor shell; an earlier WebFetch timed out on the approval prompt.
- **Currency:** none observed
- **Official status:** Not reached: lasc.org is a Blazor Server app.
- **Hazard:** JavaScript (Blazor Server) app — no text for either tool
- **Probe:** La. Sup. Ct. R. X, § 5 → `https://www.lasc.org/`
- **Evidence (2026-10-17):** Script: lasc.org home 200 text/html, 0 extractable chars (Blazor prerender markers only). No rules URL found by web search. | Independent check 2026-10-17: WebFetch www.lasc.org: no visible text, only base/viewport metadata

### `la-rules-urca` — Uniform Rules of Louisiana Courts of Appeal (PDF, Fifth Circuit posting)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana Courts of Appeal (posted by the Fifth Circuit Court of Appeal) · text: **fetch-and-quote** · official: official
- **Coverage:** Complete Uniform Rules, amendments effective July 1, 2026; 32 pages.
- **Read via (in order):** **script**
- **Access:** `link-only` · format pdf
  - Placeholders: single PDF; file name carries the effective date and changes with each amendment
  - Index: `https://www.fifthcircuit.org/uniform.aspx`
  - Navigation: uniform.aspx → take the link whose text begins 'Download the Uniform Rules of Louisiana Courts of Appeal (PDF)' (URCA_eff{MMDDYYYY}.pdf); IGNORE the second link titled 'Uniform Rules of Louisiana Courts of Appeal' → 2023RevisedUniformRules.pdf (stale 2023 copy); confirm the '(As amended, with amendments effective as of …)' title line. Rules are headed 'Rule N-N.' with subsections 'N-N.N.'; grep may hit a cross-reference first (Rule 4-3 body is the second match, p. 26).
- **Automation:** WebFetch untested · shell ok · robots: only 'User-agent: amazon-QBusiness' Disallow: / — no rule for us
  - 75K characters: probably inside the fetch tool window, untested. PDF file name changes with each amendment — re-find it from uniform.aspx.
- **Currency:** PDF title line — observed: "(As amended, with amendments effective as of July 1, 2026)"
- **Official status:** Rule 1-1.1 says the rules are promulgated by posting a copy to the five Courts of Appeal websites (https://www.fifthcircuit.org/pdf/URCA_eff07012026.pdf p. 1).
- **Hazard:** file name changes per amendment
- **Hazard:** uniform.aspx also links a stale 2023 copy (2023RevisedUniformRules.pdf)
- **Probe:** Uniform Rules of Louisiana Courts of Appeal, Rule 2-18.1 → `https://www.fifthcircuit.org/pdf/URCA_eff07012026.pdf` — expect: "An application for rehearing shall state with particularity contentions of the applicant"
- **Evidence (2026-10-17):** Script: 32 pp, last-modified 13 Jul 2026; Rule 2-18.1 'An application for rehearing shall state with particularity' on p. 22. | Independent check 2026-10-17: Script verify exact Rule 2-18.1 p.22; title '(As amended, with amendments effective as of July 1, 2026)'; second citation Uniform Rules, Courts of Appeal, Rule 4-3 ok
- **Notes:** Each circuit also posts local rules (e.g. https://www.la2nd.org/local-rules-of-court/, https://www.fifthcircuit.org/localrules.aspx); not probed.

## D. Administrative code

### `la-lac-doa` — Louisiana Administrative Code (Office of the State Register)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Division of Administration, Office of the State Register · text: **fetch-and-quote** · official: unknown
- **Coverage:** Every LAC title as a whole-title (or volume) Word .docx file; per-title 'Last Amended Date' table.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format docx
  - Placeholders: Files live at /media/{random-slug}/{TT}[vNN[-NN]].docx (e.g. 31.docx, 33v03.docx); the slug is random, so take the link from the index.
  - Index: `https://www.doa.la.gov/doa/osr/louisiana-administrative-code/`
  - Navigation: fetch_doc.py links <index> .docx (157 links) → link text 'Title {t}:{Roman part}, …' for split titles (e.g. 'Title 33:III, Environmental Quality: Air' → 33v03.docx) or 'Title {t}, …' for unsplit titles — map by link text, not file name (33v03, 46v01, 01v01-03) → fetch_doc.py grep/section on the .docx with '§{section}\. '. The string 'LAC 33:III.501' never appears; sections are headed '§501. Scope and Applicability'. Each part file opens with a table of contents, so the FIRST hit is the TOC (33:III §501 at offset 1459) — take the second / heading-anchored match (body at offset ~197015).
  - Read via: fetch_doc.py (reads .docx)
- **Automation:** WebFetch fail · shell ok · robots: none (404)
  - fetch_doc.py extracts the .docx as one page (no page numbers); whole-part files are large (33v03.docx ≈ 1.98M chars). WebFetch returns '[binary data]'.
- **Currency:** index page table 'LAC Title / Last Amended Date' plus the .docx Last-Modified header — observed: "Title 4, Administration August 2026; 33v03.docx last-modified 28 Apr 2026"
- **Official status:** Page says LAC is published under R.S. 49:953 et seq. and certified copies come from the LAC editor; online files carry no authentication statement.
- **Hazard:** Word .docx only — no HTML or PDF
- **Hazard:** random media slugs: take links from the index
- **Hazard:** part files open with a TOC: first grep hit is the TOC entry
- **Hazard:** no page numbers in extraction
- **Hazard:** citation string 'LAC t:p.s' never appears in the file
- **Probe:** LAC 33:III.501 → `https://www.doa.la.gov/media/q4eanemv/33v03.docx` — expect: "The provisions of this Chapter apply to the owner and operator"
- **Evidence (2026-10-17):** Script: index 43,708 chars with title list and last-amended table; 31.docx downloaded (last-modified 30 Jan 2026); WebFetch on .docx: '[binary data]' (script now extracts .docx). | Independent check 2026-10-17: Script: index grep 'current through the last amended date'; 33v03.docx now extracts 1,976,234 chars; second citation LAC 33:III.501 ok
- **Notes:** Tier-1 route for LAC text; la-lac-lii is the fallback.

### `la-lac-lii` — Cornell LII — Louisiana Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute (Cornell) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All LAC titles, per-section pages with LR history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/louisiana/La-Admin-Code-tit-{title}-SS-{part_roman}-{section}`
  - Placeholders: LAC {title}:{part}.{section} → tit-{title}-SS-{part}-{section} with the part in upper-case Roman (LAC 33:III.501 → La-Admin-Code-tit-33-SS-III-501; LAC 28:I.101 → La-Admin-Code-tit-28-SS-I-101). Index: /regulations/louisiana/title-{title}/part-{part}/chapter-{n}.
  - Index: `https://www.law.cornell.edu/regulations/louisiana`
- **Automation:** WebFetch untested · shell ok · robots: permits; crawl-delay 10
  - Chapter index pages show section ranges (e.g. 'Chapter 5 - Permit Procedures (§ III-501 to III-551)').
- **Currency:** page foot — observed: "State regulations are updated quarterly"
- **Official status:** Third-party; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag behind the Register
- **Hazard:** decimal sections untested
- **Hazard:** pages last updated ~Aug 2025 (33:III.501, 33:V.109) despite 'updated quarterly' — over a year behind the official .docx (Apr 2026)
- **Probe:** LAC 33:III.501 → `https://www.law.cornell.edu/regulations/louisiana/La-Admin-Code-tit-33-SS-III-501` — expect: "The provisions of this Chapter apply to the owner and operator"
- **Evidence (2026-10-17):** Script: 'A. Applicability. The provisions of this Chapter apply to the owner and operator'; history notes through 'LR 5169 (1/1/2025)'. Second URL LAC 28:I.101 → 200 (2,736 chars). | Independent check 2026-10-17: Script verify exact 'The provisions of this Chapter apply to the owner and operator'; 'State regulations are updated quarterly'; second citation LAC 33:V.109 ok

## D. Administrative register

### `la-register-doa` — Louisiana Register (Office of the State Register)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Division of Administration, Office of the State Register · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly editions of the current year (January–October 2026 listed) as .docx; older years not linked from the page.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format docx
  - Placeholders: media/{slug}/{YYMM}.docx (2610.docx = October 2026); slug random.
  - Index: `https://www.doa.la.gov/doa/osr/louisiana-register/`
  - Navigation: LR 52:{page} → the newest edition's CUMULATIVE INDEX at its end ('Pages Issue 1-194 January 195-329 February …') gives the issue → that '{Month} Edition' .docx → its opening CONTENTS list (entries end with start page numbers) → grep the item heading. Extraction has no page breaks, so a page number cannot be read directly. Only 2026 (LR 52) editions are linked.
  - Read via: fetch_doc.py (reads .docx)
- **Automation:** WebFetch fail · shell ok · robots: none (404)
  - 2603.docx extracts ~748K chars as one page; WebFetch returns binary data.
- **Currency:** edition list — observed: "October Edition (2610.docx)"
- **Official status:** No authentication statement on the listing.
- **Hazard:** .docx only
- **Hazard:** no page breaks in extraction — locate pages via cumulative index and CONTENTS
- **Hazard:** only 2026 (LR 52) editions online here; earlier volumes not found
- **Probe:** LR 52:336 (March 2026) → `https://www.doa.la.gov/media/wscpjapv/2603.docx` — expect: "LR 52:336 (March 2026)"
- **Evidence (2026-10-17):** Script: listing has January–October Edition links (2601.docx … 2610.docx) and an upcoming-publication .xlsm. | Independent check 2026-10-17: Script: listing has 10 '{Month} Edition' links 2601-2610.docx; 2603.docx extracts 748,092 chars; second citation LR 52:336 (March 2026) ok
- **Notes:** LR volume = year − 1974 (LR 13 = 1987, LR 51 = 2025), from history notes.

## E. Case law

### `la-ca1-lafcca` — Louisiana First Circuit Court of Appeal — decisions

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Louisiana Court of Appeal, First Circuit · text: **link-only** · official: official
- **Coverage:** Year pages 2008–2026.
- **Access:** `link-only` · format html
  - Index: `https://www.la-fcca.org/decisions`
  - Navigation: decisions → year page (cms/One.aspx?portalId=161585&pageId=…) — the year page body is a JavaScript file manager ('Loading...') with no links in the HTML.
- **Automation:** WebFetch untested · shell http-error · robots: Disallow /Search/, /WebApi/, /WebServices/, /portal/svc/ for *; some CivicLive pages redirect to cdnsm5-hosted2.civiclive.com, which answers robots.txt with a bot check (refused)
  - Year pages fetch (200) but list nothing without JavaScript; the data services sit under robots-disallowed paths. Do not call them.
- **Currency:** none
- **Official status:** Court's own CivicLive site (la-fcca.org → lafcca.hosted2.civiclive.com).
- **Hazard:** JS-loaded file listing
- **Hazard:** data endpoints robots-disallowed
- **Hazard:** some subpages redirect to a bot-checked CDN host
- **Probe:** First Circuit 2026 decisions → `https://lafcca.hosted2.civiclive.com/decisions/o_p_i_n_i_o_n_s_2026`
- **Evidence (2026-10-17):** Script: page 200, 2,865 chars, body 'OPINIONS 2026 … Loading...'; no decision links.
- **Notes:** Use la-ca-justia (1991–2026) for First Circuit decisions.

### `la-ca2-la2nd` — Louisiana Second Circuit Court of Appeal — opinions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana Court of Appeal, Second Circuit · text: **fetch-and-quote** · official: official
- **Coverage:** 2009–2026 (opinion_year=2008 and earlier return no rows).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Listing: /opinions/?opinion_year={YYYY} (plain GET; default = current year). Rows: date, case number (57,066-CA), name, judge, disposition, parish, published/not. PDF: /wp-content/uploads/{upload YYYY}/{MM}/{docket digits}{type lower}.pdf (57,066-CA → 57066ca.pdf) — the upload folder is not the decision date (2010 opinions sit in /2022/09/), so take the link from the listing.
  - Index: `https://www.la2nd.org/opinions/?opinion_year={year}`
  - Navigation: year listing → row for the case number → Download link (PDF).
- **Automation:** WebFetch untested · shell ok · robots: Disallow /wp-admin/ only
  - Year listings are 30–70K characters.
- **Currency:** listing — observed: "latest 10/14/2026 57,066-CA"
- **Official status:** Court's own site; PDFs are the court's slip opinions.
- **Hazard:** upload folder ≠ decision date
- **Hazard:** slip pagination only
- **Probe:** No. 57,066-CA (La. App. 2 Cir. 10/14/26) → `https://www.la2nd.org/wp-content/uploads/2026/10/57066ca.pdf` — expect: "Judgment rendered October 14, 2026."
- **Evidence (2026-10-17):** Script: listing 2025 780 links, 2010 1,005 links; PDF 13 pp begins 'Judgment rendered October 14, 2026. Application for rehearing'. | Independent check 2026-10-17: Script verify exact 'Judgment rendered October 14, 2026.' (13 pp); second citation J. Calhoun One, L.L.C. v. Jeems Bayou Production Corp., No. 55,997-CA (La. App. 2 Cir. 12/18/24) ok
- **Notes:** Writ ('-CW'/'-KW') dispositions are in the same listing.

### `la-ca3-la3circuit` — Louisiana Third Circuit Court of Appeal — opinion search

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Louisiana Court of Appeal, Third Circuit · text: **link-only** · official: official
- **Coverage:** Published opinions (date range not determined).
- **Access:** `link-only` · format html
  - Index: `https://www.la3circuit.org/Cases/Opinions.aspx`
  - Navigation: Opinion calendar and 'Smart Search' (case number like 25-467, title, month, date) are ASP.NET postbacks — no GET URL found.
- **Automation:** WebFetch untested · shell http-error · robots: none (robots.txt returns the 404 HTML page)
  - Search page reads (10,650 chars) but results need POST.
- **Currency:** none
- **Official status:** Court's own site.
- **Hazard:** POST-only search
- **Probe:** Third Circuit opinions → `https://www.la3circuit.org/Cases/Opinions.aspx`
- **Evidence (2026-10-17):** Script: search page 200; calendar dates are __doPostBack('SelectOpinionDate','2026-10-14') links.
- **Notes:** Use la-ca-justia.

### `la-ca4-la4th` — Louisiana Fourth Circuit Court of Appeal — case/opinion search

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Louisiana Court of Appeal, Fourth Circuit · text: **link-only** · official: official
- **Coverage:** Search case years 1992–2026.
- **Access:** `link-only` · format html
  - Index: `https://www.la4th.org/Search.aspx`
  - Navigation: Opinion search by case number, month/year, date or litigant — ASP.NET postbacks only.
- **Automation:** WebFetch untested · shell http-error · robots: none (404)
  - Home page links a few news PDFs (/opinion/News/NNN.pdf), not opinions.
- **Currency:** none
- **Official status:** Court's own site.
- **Hazard:** POST-only search
- **Probe:** Fourth Circuit opinions → `https://www.la4th.org/Search.aspx`
- **Evidence (2026-10-17):** Script: Search.aspx 200 (12,159 chars); search buttons are WebForm_DoPostBack.
- **Notes:** Use la-ca-justia.

### `la-ca5-fifthcircuit` — Louisiana Fifth Circuit Court of Appeal — recent decisions and writ dispositions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Louisiana Court of Appeal, Fifth Circuit · text: **fetch-and-quote** · official: official
- **Coverage:** Home page lists recent opinions and writ dispositions as PDFs; older ones via POST-only Decision Search.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: PDFs at /dmzdocs/{OI/PO|RE|WI/Writ Disposition}/{YYYY}/{GUID}.pdf — GUID names; percent-encode the space ('Writ%20Disposition').
  - Index: `https://www.fifthcircuit.org/`
  - Navigation: home page 'Case # / Case Title' list → PDF. The dmzdocs PDF links have NO anchor text ('(no text)' in fetch_doc.py links), so a links filter on the case number fails: list the /dmzdocs/ links in page order and pair them with the case numbers from grep '2\d-[A-Z]{1,2}-\d+' on the home page (same order; checked 26-C-483, 26-KH-460), then confirm 'No. {docket}' on PDF page 1. One case can have several PDFs (26-CA-27: opinion OI/PO and rehearing RE). searchopinions.aspx (case year + number) is a POST form.
- **Automation:** WebFetch untested · shell ok · robots: only amazon-QBusiness disallowed
  - fetch_doc.py rejects a raw space in the URL — encode it as %20.
- **Currency:** home page list — observed: "26-C-483 … October 16, 2026"
- **Official status:** Court's own site.
- **Hazard:** GUID file names
- **Hazard:** only recent decisions reachable by GET
- **Hazard:** space in writ path
- **Hazard:** PDF links carry no anchor text — pair by order, confirm docket in the PDF
- **Probe:** No. 26-CA-27 (La. App. 5 Cir.) → `https://www.fifthcircuit.org/dmzdocs/OI/PO/2026/3BEA2644-D02C-48BF-953E-91C9B93E8536.pdf` — expect: "Fifth Circuit Court of Appeal State of Louisiana No. 26-CA-27"
- **Evidence (2026-10-17):** Script: 8 pp, last-modified 23 Sep 2026; writ disposition 26-C-483 PDF (3 pp) also read. | Independent check 2026-10-17: Script verify 'No. 26-CA-27' p.1; home list 'Case # Case Title 26-CA-27'; second citation No. 26-KH-460 (La. App. 5 Cir.) writ disposition ok

### `la-sc-lasc` — Supreme Court of Louisiana — opinions and news releases (lasc.org)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of Louisiana · text: **link-only** · official: official
- **Coverage:** Opinions announced by numbered news release ('NEWS RELEASE #054 … opinions handed down'), per Justia-hosted copies.
- **Access:** `link-only` · format html
  - Index: `https://www.lasc.org/`
  - Navigation: unknown — Blazor Server app; use la-sc-justia, whose PDFs are the court's own news-release PDFs.
- **Automation:** WebFetch fail · shell http-error · robots: none (Blazor shell served for /robots.txt)
  - Script: 200 with 0 extractable characters on every path (content rendered over SignalR). WebFetch (independent check 2026-10-17) returned promptly with only base/viewport metadata — empty Blazor shell; an earlier WebFetch timed out on the approval prompt.
- **Currency:** none observed
- **Official status:** Court's own site (per memory); not reachable as text.
- **Hazard:** JavaScript (Blazor Server) app
- **Probe:** 2022-K-01824 (La. 12/8/23) → `https://www.lasc.org/`
- **Evidence (2026-10-17):** Script: lasc.org /, /Opinions, /Actions, /News_Releases all 200 with 0 extractable characters. | Independent check 2026-10-17: WebFetch www.lasc.org: no visible text, only base/viewport metadata

### `la-ca-justia` — Justia — Louisiana Courts of Appeal (First–Fifth Circuits)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** First Circuit 1991–2026 (others not checked); per-court year listings.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/louisiana/{court}/{year}/{docket_slug}.html`
  - Placeholders: court ∈ first-circuit-court-of-appeal, second-circuit-court-of-appeal, third-circuit-court-of-appeal, fourth-circuit-court-of-appeal, fifth-circuit-court-of-appeal. First Circuit docket slug = docket lower case without spaces (2026 CW 0629 → 2026cw0629). Second Circuit slug = docket with the comma turned into a hyphen, type suffix kept, lower case (56,618-KA → 56-618-ka; /second-circuit-court-of-appeal/2025/56-618-ka.html, PDF …/second-circuit-court-of-appeal/2025-56-618-ka.pdf, verified). Third–Fifth Circuit slugs untested — use the year listing. PDF: https://cases.justia.com/louisiana/{court}/{year}-{docket_slug}.pdf
  - Index: `https://law.justia.com/cases/louisiana/{court}/{year}/`
  - Navigation: year listing → case page → Download PDF
  - Read via: cases.justia.com PDFs via fetch_doc.py
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com unreadable (challenge)
  - Some case pages carry no text (writ actions), only the PDF; some PDFs are image scans with no text layer (2026cw0629.pdf: 2 pages, 1 character).
- **Currency:** year listing — observed: "First Circuit latest August 28, 2026"
- **Official status:** Third-party.
- **Hazard:** writ-action PDFs may be image-only scans (OCR needed)
- **Hazard:** case page may lack body text
- **Probe:** Collins v. Greater True Love Baptist Church, 2026 CW 0629 (La. App. 1 Cir. 8/28/26) → `https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2026/2026cw0629.html`
- **Evidence (2026-10-17):** WebFetch: listing 1991–2026; case page has no body text, links PDF; script read the PDF: 2 pages, 1 character (scan). | Independent check 2026-10-17: WebFetch: 2026cw0629 page has no body, PDF link only (as recorded); second citation State v. Taylor, 56,618-KA (La. App. 2 Cir. 12/23/25) ok

### `la-sc-justia` — Justia — Louisiana Supreme Court decisions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 1885–2026 by year (2026: 27 entries, Mar 6–Jul 31 2026 at probe — incomplete vs. the court's output).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/louisiana/supreme-court/{year}/{docket_lower}.html`
  - Placeholders: year = year DECIDED, not the docket year (2025-C-01318 decided 2026 → /2026/2025-c-01318.html); docket in lower case with hyphens as printed (2022-K-01824 → 2022-k-01824.html). PDF: https://cases.justia.com/louisiana/supreme-court/{year}-{docket_lower}.pdf (works without the ?ts= suffix — verified). Older dockets (pre-2019, e.g. 2006-2346) not tested.
  - Index: `https://law.justia.com/cases/louisiana/supreme-court/{year}/`
  - Navigation: year listing → case page → 'Download PDF' (cases.justia.com).
  - Read via: cases.justia.com PDFs read by fetch_doc.py (ok); the case page itself is WebFetch-only
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com unreadable (challenge); cases.justia.com fetched by the script without refusal
  - Case pages carry the opinion text; the PDF (court news release + opinion, slip pagination) reads fully with fetch_doc.py.
- **Currency:** year listing — observed: "latest entry July 31, 2026"
- **Official status:** Third-party; the downloadable PDF is the court's own news-release PDF with slip pagination.
- **Hazard:** no So. 3d pagination — slip pages only
- **Hazard:** listing incomplete (writ actions and per curiams may be missing)
- **Hazard:** law.justia.com shell-blocked
- **Hazard:** listing lags the court by months (2026 listing still ended July 31, 2026 on 2026-10-17)
- **Probe:** State v. Sagastume, 2022-K-01824 (La. 12/8/23) → `https://law.justia.com/cases/louisiana/supreme-court/2023/2022-k-01824.html` — expect: "We granted the State's application to consider whether defendant's claim that the"
- **Evidence (2026-10-17):** WebFetch: body present; PDF via script 11 pp, begins 'FOR IMMEDIATE NEWS RELEASE NEWS RELEASE #054 FROM: CLERK OF SUPREME COURT'. | Independent check 2026-10-17: WebFetch: 'We granted the State's application to consider whether defendant's claim that the'; second citation Cousain v. Smitty's Supply, Inc., 2025-C-01318 (La. 6/29/26) ok

## F. Subsequent history

### `la-subsequent-lasc` — Supreme Court of Louisiana — writ grants and denials

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of Louisiana · text: **link-only** · official: official
- **Coverage:** Writ dispositions (granted / denied / not considered) announced by date.
- **Access:** `link-only` · format html
  - Index: `https://www.lasc.org/`
  - Navigation: unknown (Blazor app). From the court-of-appeal decision, the history is normally found only in later citing opinions ('writ denied, YYYY-NNNNN (La. M/D/YY)') or by the Supreme Court docket number.
- **Automation:** WebFetch fail · shell http-error · robots: none (Blazor shell)
  - Script: 200 with 0 extractable characters on every path (content rendered over SignalR). WebFetch (independent check 2026-10-17) returned promptly with only base/viewport metadata — empty Blazor shell; an earlier WebFetch timed out on the approval prompt.
- **Currency:** none
- **Official status:** Court's own news releases / actions (per memory); not reachable.
- **Hazard:** JavaScript app
- **Hazard:** writ denials are not on Justia's Supreme Court listing
- **Probe:** writ denied, 2021-01234 (La. 1/12/22) → `https://www.lasc.org/`
- **Evidence (2026-10-17):** lasc.org returns empty Blazor shell; Justia 2026 Supreme Court listing (27 entries) has no writ-action lists. | Independent check 2026-10-17: WebFetch www.lasc.org: no visible text, only base/viewport metadata

## Not available (do not look for these again)

- **statutes** — Official bulk download / API for Louisiana laws: LawSearch.aspx and LawsOther.aspx offer no XML/JSON/zip; only per-law HTML pages and a POST search. (2026-10-17)
- **statutes** — GET route from a Revised Statutes or Constitution citation to its page: RS (folder=75) and Constitution (folder=72) TOCs and the 'View a Specific Law' box are ASP.NET POST postbacks. (2026-10-17)
- **statutes** — public.law / Cornell LII editions of Louisiana statutes: From memory: public.law covers other states; LII has only the LAC (title list fetched). Not separately probed. (2026-10-17)
- **case_law** — Free official So. 3d pagination: Court PDFs (2nd Cir., 5th Cir., Supreme Court via Justia) carry slip pagination only; So. 2d/3d are West reporters. (2026-10-17)
- **subsequent_history** — Writ dispositions on Justia's Supreme Court listing: WebFetch of /cases/louisiana/supreme-court/2026/: 27 case captions, no writ-action lists. (2026-10-17)

## Corpus candidates (maintainers)

- `la-rules-urca` — Official single-PDF rule set (32 pp, 75K chars); file name changes per amendment, so a frozen ingested copy plus currency probe helps.
- `la-const-senate-pdf` — Whole constitution in one PDF (683K chars) — beyond the fetch tool; but two-column layout and 2023 currency make it a weak base (official per-section HTML exists on legis.la.gov).
- `la-lac-doa` — Official LAC as whole-part .docx files (up to ~2M chars) — script-readable but huge and TOC-first; ingest per section would speed lookup. · bulk: per-title .docx downloads from the index

## Open questions

- lasc.org (Supreme Court opinions, news releases, writ actions, Supreme Court Rules, District Court Rules) is a Blazor Server app: neither tool gets text, and WebFetch returns an empty shell (one earlier call timed out on approval). Need a real lasc.org opinion/rules PDF URL (a human browser session) to test whether static PDFs are served.
- First Circuit (CivicLive) decision listings load by JavaScript from robots-disallowed /portal/svc/ paths — is there any static listing?
- Third and Fourth Circuit opinion searches are POST-only; GET variants were not found.
- Louisiana Register archive for years before 2026 not found on the OSR page.
- Justia slug forms for the 2nd–5th Circuits and for pre-2019 Supreme Court dockets untested.
- CourtListener ids 'la' and 'lactapp' unverified.
- legis.la.gov has duplicate live ids for some sections (RS 14:30.1: d=150048 and d=78398) — which is canonical, and do ids change on amendment?

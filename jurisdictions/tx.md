# Texas (TX) — free legal sources

_Generated from `data/tx.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and Constitution: statutes.capitol.texas.gov is now an Angular app that gives the fetch tool an empty shell. The chapter files behind it, at tcss.legis.texas.gov/resources/{CODE}/htm/{CODE}.{chapter}.htm, are constructible from any Texas citation and readable by both the fetch tool and fetch_doc.py; official per-code bulk zips and PDFs also exist. Court rules (TRCP, TRAP, TRE, TDRPC) are long PDFs on txcourts.gov that the fetch tool truncates (corpus candidates). Case law: search.txcourts.gov (TAMES: all court of appeals and CCA opinions, dockets, petition dispositions) is closed by robots.txt (Disallow: /); Supreme Court opinions and weekly orders lists (Oct. 2014 on) and Business Court opinions (2024 on, public-domain cites like 2026 Tex. Bus. 72) are on www.txcourts.gov/media; Justia is the only allowed route to court of appeals and CCA opinion text. Admin Code: the SOS viewer is a JavaScript app with no readable text; Cornell LII is the working fallback; Texas Register issue PDFs are on sos.state.tx.us.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Texas | `tex (unverified)` | Tex. | S.W.3d, S.W.2d, S.W., Tex. | — |
| Texas Court of Criminal Appeals | `texcrimapp (unverified)` | Tex. Crim. App. | S.W.3d, S.W.2d, S.W., Tex. Crim. | — |
| Texas Courts of Appeals (First through Fifteenth Districts) | `texapp (unverified)` | Tex. App.—{city} [{n}th Dist.] | S.W.3d, S.W.2d | — |
| Business Court of Texas | `— (unverified)` | Tex. Bus. Ct. | S.W.3d | YYYY Tex. Bus. N (e.g. '2026 Tex. Bus. 72 (8th Div.)'); pinpoint by paragraph ¶N, not page |
| Special Court of Review (Texas) | `texreview (unverified)` | Tex. Spec. Ct. Rev. | S.W.3d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Texas codes | `Tex. Civ. Prac. & Rem. Code Ann. § 16.003`; `Tex. Penal Code § 19.02`; `Tex. Penal Code Ann. § 19.02(b)(1)`; `Tex. Code Crim. Proc. Ann. art. 38.23`; `Tex. Gov't Code § 552.325`; `Tex. Fam. Code Ann. § 153.002`; `Tex. Bus. Orgs. Code § 21.223`; `Texas Penal Code section 19.02`; `section 16.003 of the Civil Practice and Remedies Code`; `Section 19.02 of the Texas Penal Code`; `article 38.23 of the Code of Criminal Procedure`; `CPRC § 16.003`; `Tex. Civ. Prac. & Rem. Code §§ 16.003-.004` | `tx-statutes-tcss` → `tx-statutes-justia` → `tx-statutes-publiclaw` |
| Vernon's Texas Civil Statutes (uncodified articles) | `Tex. Rev. Civ. Stat. Ann. art. 4413(37)`; `Tex. Rev. Civ. Stat. art. 6243e` | `tx-statutes-tcss` → `tx-statutes-justia` |
| Texas Constitution | `Tex. Const. art. I, § 19`; `Tex. Const. art. V, § 1`; `Tex. Const. art. 1, § 19`; `Article I, Section 19 of the Texas Constitution`; `article I, section 13 of the Texas Constitution` | `tx-constitution-tcss` → `tx-constitution-justia` |
| Texas Rules of Civil Procedure | `Tex. R. Civ. P. 91a`; `Tex. R. Civ. P. 91a.1`; `TRCP 166a(c)`; `Rule 91a of the Texas Rules of Civil Procedure`; `Texas Rule of Civil Procedure 13` | `tx-rules-civil` |
| Texas Rules of Appellate Procedure | `Tex. R. App. P. 47.7`; `TRAP 33.1(a)`; `Rule 47.7 of the Texas Rules of Appellate Procedure`; `Texas Rule of Appellate Procedure 56.2` | `tx-rules-appellate` |
| Texas Rules of Evidence | `Tex. R. Evid. 702`; `TRE 403`; `Rule 803(6) of the Texas Rules of Evidence`; `Texas Rule of Evidence 401` | `tx-rules-evidence` |
| Texas Disciplinary Rules of Professional Conduct | `Tex. Disciplinary Rules Prof'l Conduct R. 1.06`; `TDRPC 1.05`; `Rule 3.03 of the Texas Disciplinary Rules of Professional Conduct` | `tx-rules-disciplinary` |
| Texas Rules of Judicial Administration | `Tex. R. Jud. Admin. 6.1`; `Rule 13 of the Texas Rules of Judicial Administration` | `tx-rules-judicial-admin` |
| Texas Administrative Code | `16 Tex. Admin. Code § 3.1`; `16 TAC § 3.1`; `30 T.A.C. § 330.3`; `16 Tex. Admin. Code § 3.1(a)(1)` | `tx-tac-lii` → `tx-tac-sos` |
| Texas Register | `51 Tex. Reg. 7113`; `50 TexReg 835`; `51 Tex. Reg. 7091 (Oct. 16, 2026)` | `tx-register-sos` |
| Reported Texas cases (South Western Reporter) with Texas court and subsequent-history parenthetical | `Smith v. Jones, 712 S.W.3d 100 (Tex. 2026)`; `Doe v. Roe, 700 S.W.3d 1, 5 (Tex. App.—Dallas 2024, pet. denied)`; `Smith v. Jones, 123 S.W.3d 456, 460 (Tex. App.—Houston [14th Dist.] 2003, no pet.)`; `State v. Doe, 600 S.W.3d 10 (Tex. Crim. App. 2020)`; `Doe v. State, 555 S.W.3d 777 (Tex. App.—Fort Worth 2018, pet. ref'd)`; `Roe v. Roe, 900 S.W.2d 100 (Tex. App.—Austin 1995, writ denied)`; `Roe v. Doe, 650 S.W.3d 20 (Tex. App.—Corpus Christi–Edinburg 2022, no pet.)`; `State v. Roe, 729 S.W.3d 400 (Tex. App.—15th Dist. 2025, pet. granted)` | `tx-scotx-orders-opinions` → `tx-cases-justia` → `tx-cases-tames` |
| Texas memorandum / unpublished opinions by docket number (courts of appeals, CCA, Supreme Court) | `No. 05-23-00999-CV, 2024 WL 1000001, at *2 (Tex. App.—Dallas Aug. 21, 2024, pet. denied) (mem. op.)`; `No. 14-22-00856-CV (Tex. App.—Houston [14th Dist.] Feb. 6, 2025, pet. denied)`; `No. 01-19-00999-CR (Tex. App.—Houston [1st Dist.] 2020, pet. ref'd) (mem. op., not designated for publication)`; `PD-0643-25`; `WR-97,760-01`; `AP-77,122`; `No. 24-0205 (Tex. May 29, 2026)` | `tx-cases-justia` → `tx-scotx-orders-opinions` → `tx-cases-tames` |
| Business Court of Texas public-domain citation and cause number | `Crain v. Northern, 2026 Tex. Bus. 72 (8th Div.)`; `2026 Tex. Bus. 73, ¶ 12`; `Cause No. 25-BC08A-0014`; `26-BC03A-0010` | `tx-business-court-opinions` |
| Westlaw / Lexis cites to Texas courts | `2024 WL 1000001 (Tex. App.—Dallas Aug. 21, 2024, pet. denied)`; `2020 Tex. App. LEXIS 1234`; `2019 Tex. Crim. App. LEXIS 55`; `2026 Tex. LEXIS 400` | `tx-cases-justia` → `tx-scotx-orders-opinions` |

Regexes (case-insensitive):

- Texas codes: `Tex(?:as|\.)\s+(?P<code>(?:(?:[A-Z&][\w.'’&]*|and|of)\s+){0,5}?Code|Code\s+(?:of\s+)?Crim(?:inal|\.)\s*Proc(?:edure|\.)?|Crim(?:inal|\.)\s*Proc(?:edure|\.)?\s+Code)(?:\s+Ann(?:otated|\.))?(?:\s*\([^)]*\))?,?\s*(?:§§?|[Ss]ec(?:tions?|s?\.)|[Aa]rt(?:icles?|s?\.))\s*(?P<section>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)+)|(?:[Ss]ection|[Aa]rticle|§)\s*(?P<section2>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)+)(?:\([a-zA-Z0-9]+\))*,?\s+of\s+(?:the\s+)?(?:Texas\s+(?P<code2>(?:(?:[A-Z&][\w.'’&]*|and)\s+){1,5}Code|Code\s+of\s+Criminal\s+Procedure)|(?P<code3>Civil\s+Practice\s+(?:and|&)\s+Remedies\s+Code|Code\s+of\s+Criminal\s+Procedure|Business\s+Organizations\s+Code|Parks\s+(?:and|&)\s+Wildlife\s+Code|Special\s+District\s+Local\s+Laws\s+Code|Alcoholic\s+Beverage\s+Code|Occupations\s+Code|Human\s+Resources\s+Code|Business\s+(?:and|&)\s+Commerce\s+Code|Estates\s+Code))|(?P<code4>T?CPRC)\s*§+\s*(?P<section4>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)+)`
- Vernon's Texas Civil Statutes (uncodified articles): `Tex\.\s*Rev\.\s*Civ\.\s*Stat\.(?:\s*Ann\.)?\s*art\.\s*(?P<article>\d+[a-z]?(?:\(\d+\))?(?:[-.]\d+)?)`
- Texas Constitution: `Tex(?:as|\.)\s*Const(?:itution|\.)\s*,?\s*art(?:icle|\.)?\s*(?P<article>[IVXL]+|\d{1,2}),?\s*(?:§|[Ss]ec(?:tion|\.)?)\s*(?P<section>\d+[a-z]?(?:-[a-z])?)|[Aa]rticle\s+(?P<article2>[IVXL]+|\d{1,2}),?\s+[Ss]ection\s+(?P<section2>\d+[a-z]?(?:-[a-z])?)\s+of\s+the\s+Texas\s+Constitution`
- Texas Rules of Civil Procedure: `(?:Tex\.\s*R\.\s*Civ\.\s*P(?:roc)?\.|T\.?R\.?C\.?P\.?|Texas\s+Rules?\s+of\s+Civil\s+Procedure)\s*(?P<rule>\d+[a-z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[a-z]?(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Texas\s+Rules\s+of\s+Civil\s+Procedure`
- Texas Rules of Appellate Procedure: `(?:Tex\.\s*R\.\s*App\.\s*P(?:roc)?\.|T\.?R\.?A\.?P\.?|Texas\s+Rules?\s+of\s+Appellate\s+Procedure)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Texas\s+Rules\s+of\s+Appellate\s+Procedure`
- Texas Rules of Evidence: `(?:Tex\.\s*R\.\s*Evid\.|T\.?R\.?E\.?(?=\s*\d{3})|Texas\s+Rules?\s+of\s+Evidence)\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Texas\s+Rules\s+of\s+Evidence`
- Texas Disciplinary Rules of Professional Conduct: `(?:Tex\.\s*Disciplinary\s*R(?:ules|\.)\s*Prof'?l\s*Conduct\s*(?:R\.)?|TDRPC|Texas\s+Disciplinary\s+Rules?\s+of\s+Professional\s+Conduct)\s*(?P<rule>\d\.\d{2})|Rule\s+(?P<rule2>\d\.\d{2})(?:\([a-z0-9]+\))*\s+of\s+the\s+Texas\s+Disciplinary\s+Rules\s+of\s+Professional\s+Conduct`
- Texas Rules of Judicial Administration: `Tex\.\s*R\.\s*Jud\.\s*Admin\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)\s+of\s+the\s+Texas\s+Rules\s+of\s+Judicial\s+Administration`
- Texas Administrative Code: `(?P<title>\d{1,2})\s+(?:Tex\.\s*Admin\.\s*Code|T\.?A\.?C\.?)\s*(?:§+|[Ss]ec(?:tion|\.)?|R(?:ule|\.))?\s*(?P<chapter>\d+[A-Z]?)\.(?P<section>\d+[a-z]?)`
- Texas Register: `(?P<volume>\d{1,2})\s+Tex\.?\s*Reg\.?\s+(?P<page>\d{1,5})`
- Reported Texas cases (South Western Reporter) with Texas court and subsequent-history parenthetical: `(?P<volume>\d{1,4})\s+S\.\s*W\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)*\s*\((?P<court>Tex\.(?:\s*Crim\.\s*App\.|\s*App\.\s*(?:[—–]|-{1,2})?\s*(?P<coa>[A-Z][A-Za-z .–-]*?(?:\s*\[\d+(?:st|nd|rd|th)\s+Dist\.\])?|\d+(?:st|nd|rd|th)\s+Dist\.)|\s*Bus\.\s*Ct\.|\s*Comm'n\s*App\.)?)\s*(?P<date>(?:[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s+)?(?P<year>\d{4}))(?:,\s*(?P<history>[^)]+))?\)`
- Texas memorandum / unpublished opinions by docket number (courts of appeals, CCA, Supreme Court): `(?P<coa_docket>(?P<district>0[1-9]|1[0-5])-(?P<yy>\d{2})-(?P<seq>\d{5})-(?P<kind>CV|CR))|(?P<cca_docket>(?P<cca_type>PD|WR|AP)-\d{1,2},?\d{3}(?:-\d{2})?)|No\.\s*(?P<sc_docket>\d{2}-\d{4})(?=[^)]{0,40}\(Tex\.\s+[A-Z])`
- Business Court of Texas public-domain citation and cause number: `(?P<year>20\d{2})\s+Tex\.\s*Bus\.\s+(?P<number>\d{1,4})|(?P<cause>\d{2}-BC\d{2}[A-Z]-\d{4})`
- Westlaw / Lexis cites to Texas courts: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Tex\.|Tex\.\s*(?:(?P<lexcourt>App\.|Crim\.\s*App\.)\s*)?LEXIS\s+(?P<lexis>\d+))`

Short forms → URL key:

Agric. Code → `AG`; Agriculture Code → `AG`; Alco. Bev. Code → `AL`; Alcoholic Beverage Code → `AL`; Bus. & Com. Code → `BC`; Bus. and Com. Code → `BC`; Business & Commerce Code → `BC`; Business and Commerce Code → `BC`; Bus. Orgs. Code → `BO`; Business Organizations Code → `BO`; BOC → `BO`; Civ. Prac. & Rem. Code → `CP`; Civ. Prac. and Rem. Code → `CP`; Civil Practice and Remedies Code → `CP`; Civil Practice & Remedies Code → `CP`; CPRC → `CP`; TCPRC → `CP`; Code Crim. Proc. → `CR`; Crim. Proc. Code → `CR`; Code of Criminal Procedure → `CR`; Tex. Code Crim. Proc. → `CR`; Educ. Code → `ED`; Education Code → `ED`; Elec. Code → `EL`; Election Code → `EL`; Est. Code → `ES`; Estates Code → `ES`; Fam. Code → `FA`; Family Code → `FA`; Fin. Code → `FI`; Finance Code → `FI`; Gov't Code → `GV`; Gov’t Code → `GV`; Govt. Code → `GV`; Government Code → `GV`; Health & Safety Code → `HS`; Health and Safety Code → `HS`; Hum. Res. Code → `HR`; Human Resources Code → `HR`; Ins. Code → `IN`; Insurance Code → `IN`; Lab. Code → `LA`; Labor Code → `LA`; Loc. Gov't Code → `LG`; Loc. Gov’t Code → `LG`; Local Government Code → `LG`; Nat. Res. Code → `NR`; Natural Resources Code → `NR`; Occ. Code → `OC`; Occupations Code → `OC`; Parks & Wild. Code → `PW`; Parks and Wildlife Code → `PW`; Parks & Wildlife Code → `PW`; Penal Code → `PE`; Prob. Code → `PB`; Probate Code → `PB`; Prop. Code → `PR`; Property Code → `PR`; Spec. Dist. Local Laws Code → `SD`; Special District Local Laws Code → `SD`; Tax Code → `TX`; Transp. Code → `TN`; Transportation Code → `TN`; Util. Code → `UT`; Utilities Code → `UT`; Water Code → `WA`; Auxiliary Water Laws → `WL`; Rev. Civ. Stat. → `CV`; Vernon's Civil Statutes → `CV`; Vernon's Tex. Civ. Stat. → `CV`; Tex. Const. → `CN`; Texas Constitution → `CN`; Insurance Code - Not Codified → `I1`

Statute citations: Bluebook 'Tex. Civ. Prac. & Rem. Code Ann. § 16.003 (West 20xx)'; Texas Greenbook (Texas Rules of Form) drops 'Ann.' and the publisher. Every Texas code section number is {chapter}.{section-within-chapter}, so the chapter is the part before the first dot (§ 16.003 → ch. 16; § 552.325 → ch. 552; art. 38.23 → ch. 38; § 2001.038 → ch. 2001; CCP chapters can carry letters: ch. 2A). The Code of Criminal Procedure uses 'art.' not '§'; it was partly recodified effective Jan. 1, 2025 (Acts 2023, H.B. 4504), so pre-2025 article numbers in older opinions may not exist in the current chapter file. 'Prob. Code' (PB) is repealed (replaced by the Estates Code, 2014) — the site no longer lists it in StatuteCodes.json; treat a Probate Code cite as historical. Guard against other states: bare 'Penal Code', 'Government Code', 'Family Code', 'Probate Code', 'Insurance Code', 'Labor Code', 'Education Code', 'Water Code', 'Property Code' route here ONLY with a 'Tex.'/'Texas' prefix — California has Penal Code § 187 and dotted sections like Penal Code § 12022.53, and 'Code of Civil Procedure § 425.16' is California, not Texas. Prose forms without 'Texas' route here only for Texas-unique code names (Civil Practice and Remedies, Code of Criminal Procedure, Business Organizations, Parks and Wildlife, Special District Local Laws, Alcoholic Beverage, Occupations, Human Resources, Business and Commerce, Estates). Bare 'CCP' is ambiguous (California Code of Civil Procedure) and is not routed. A range '§§ 16.003-.004' or '§§ 16.003–16.004' is a span: take the first section only (the regex stops at the hyphen). Bare 'Rule 91a' / 'Rule 47.7' route here only in a Texas context; 'TRE'/'TRAP'/'TRCP' acronyms are Texas-specific. Case citations: Texas cites carry the subsequent-history parenthetical inside the court/date parenthetical. Civil (Sept. 1, 1997 onward, petition for review to the Supreme Court): 'pet. denied', 'pet. granted', 'pet. dism'd', 'pet. dism'd w.o.j.', 'pet. abated', 'pet. filed', 'no pet.' (time expired, none filed), 'no pet. h.' (no history yet). Civil before Sept. 1, 1997 (application for writ of error): 'writ ref'd' (= Supreme Court precedent), 'writ ref'd n.r.e.', 'writ denied', 'writ dism'd w.o.j.', 'writ dism'd by agr.', 'no writ'. Criminal (petition for discretionary review to the Court of Criminal Appeals): 'pet. ref'd', 'pet. granted', 'pet. dism'd', 'untimely pet.', 'no pet.'; 'PDR' is a docket term, not a citation form. Civil petition history → tx-subsequent-scotx-orders (weekly orders lists name the COA docket); criminal 'pet. ref'd' is published only in TAMES (blocked) — cite it as reported, unconfirmed. Courts of appeals: 'Tex. App.—Houston [1st Dist.]', '[14th Dist.]', 'Tex. App.—Dallas', 'Tex. App.—Austin', 'Tex. App.—San Antonio', 'Tex. App.—Fort Worth', 'Tex. App.—Amarillo', 'Tex. App.—El Paso', 'Tex. App.—Beaumont', 'Tex. App.—Waco', 'Tex. App.—Eastland', 'Tex. App.—Tyler', 'Tex. App.—Texarkana', 'Tex. App.—Corpus Christi–Edinburg' (formerly 'Corpus Christi'); the Fifteenth Court of Appeals (statewide, from Sept. 1, 2024) is cited 'Tex. App.—15th Dist.' (form per orders lists; Greenbook form unverified). COA docket NN-YY-NNNNN-CV/CR: the first two digits are the district (01-15). Unpublished/memorandum opinions: civil memorandum opinions are precedential (TRAP 47.7(b)); criminal opinions marked 'do not publish' / 'not designated for publication' have no precedential value (TRAP 47.7(a)). Supreme Court docket 'No. YY-NNNN' collides with many courts' docket shapes — route only with a '(Tex.' parenthetical. Business Court cites are public-domain ('2026 Tex. Bus. 72 (8th Div.)'), paragraph-pinpointed. The Supreme Court and CCA have no vendor-neutral citation. CourtListener ids (tex, texcrimapp, texapp, texreview) are from memory and unverified; no id known for the Business Court.

## A. Statutes / code

### `tx-session-laws-lrl` — Legislative Reference Library of Texas — session laws and bill history

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Legislative Reference Library of Texas · text: **link-only** · official: unknown
- **Coverage:** General and Special Laws of Texas (session laws), statute history.
- **Access:** `link-only` · format html
  - Index: `https://lrl.texas.gov/`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: Disallow: / for anthropic-ai, Claude-Web and ClaudeBot (also GPTBot, CCBot, PerplexityBot …); '*' disallows only /lrlstaff, /cfide
  - The host names Anthropic's agents explicitly, so it is treated as refusing this skill's tools. Not fetched by any route.
- **Currency:** not checked
- **Official status:** Not fetched.
- **Hazard:** robots.txt refuses Anthropic user agents
- **Probe:**  → `https://lrl.texas.gov/robots.txt`
- **Evidence (2026-10-16):** robots.txt (curl, 200): 'User-agent: ClaudeBot / Disallow: /', same for anthropic-ai and Claude-Web.
- **Notes:** Session-law chapter numbers ('Acts 2023, 88th Leg., R.S., ch. 765') appear in the history notes of tx-statutes-tcss files; enrolled bill text is on capitol.texas.gov (Texas Legislature Online), not probed.

### `tx-statutes-capitol-app` — Texas Constitution and Statutes web app (statutes.capitol.texas.gov)

- **Status:** VERIFIED [!] 2026-10-16 (research) · **Tier 1** · Texas Legislative Council · text: **link-only** · official: unknown
- **Coverage:** Human-facing viewer for the same files; link target only.
- **Access:** `link-only` · format html
  - Pattern: `https://statutes.capitol.texas.gov/Docs/{CODE}/htm/{CODE}.{chapter}.htm#{section}`
  - Placeholders: Human link form used throughout Texas opinions and agency sites; it serves the Angular shell, which loads the text client-side from tcss.legis.texas.gov/resources. For reading, rewrite 'https://statutes.capitol.texas.gov/Docs/' → 'https://tcss.legis.texas.gov/resources/'.
  - Index: `https://statutes.capitol.texas.gov/`
- **Automation:** WebFetch fail · shell http-error · robots: none (robots.txt path returns the app's HTML)
  - Every path (incl. /robots.txt and /Docs/CP/htm/CP.16.htm) returns the same 1,402-character shell (identical sha256). Shell value is http-error by convention: HTTP 200 but no document text.
- **Currency:** Site Information panel (rendered by JavaScript; same text as tx-statutes-tcss)
- **Official status:** Same publisher as tx-statutes-tcss; no official-status statement found.
- **Hazard:** JavaScript-only app: no statute text reaches the fetch tool or the script
- **Probe:** Tex. Civ. Prac. & Rem. Code § 16.003 → `https://statutes.capitol.texas.gov/Docs/CP/htm/CP.16.htm#16.003`
- **Evidence (2026-10-16):** WebFetch: NOT PRESENT, 'only navigation and an app shell'. fetch_doc.py: 200, 1,402 chars, same sha256 for /robots.txt, /Docs/CP/htm/CP.16.htm and /Docs/PE/htm/PE.19.htm.
- **Notes:** Recorded so the skill rewrites these links rather than reporting the statute missing.

### `tx-statutes-tcss` — Texas Constitution and Statutes — chapter files (tcss.legis.texas.gov/resources)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Texas Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** All Texas codes, Vernon's Civil Statutes (CV), Auxiliary Water Laws (WL), uncodified Insurance Code (I1), and the Constitution; one HTML/PDF/DOCX file per chapter; historical versions 2004 onward via the 'Statutes by Date' API.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://tcss.legis.texas.gov/resources/{CODE}/htm/{CODE}.{chapter}.htm#{section}`
  - Placeholders: CODE = two-letter key from law_aliases (CP, PE, CR, GV, FA, BC, BO, …; list at https://statutes.capitol.texas.gov/assets/StatuteCodes.json). chapter = the part of the section number before the first dot, unpadded, letters kept (16.003 → CP.16; 19.02 → PE.19; art. 38.23 → CR.38; 552.325 → GV.552; 2001.038 → GV.2001; CR.2A exists). Sections are anchored <a name="16.003"> on the chapter page (the fetch tool ignores the #fragment; search the page for 'Sec. 16.003.' or 'Art. 38.23.'). Same file as PDF: /resources/{CODE}/pdf/{CODE}.{chapter}.pdf; Word: /resources/{CODE}/word/{CODE}.{chapter}.docx. There are NO per-section files for statutes (/CP/htm/CP.16/16.003.htm → 404). Hierarchy (title/subtitle/subchapter) is printed at the top of each chapter file — use it to build tx-statutes-justia URLs.
  - Index: `https://statutes.capitol.texas.gov/assets/StatuteCodes.json`
- **Automation:** WebFetch ok · shell ok · robots: none (tcss.legis.texas.gov/robots.txt → 404)
  - The fetch tool reads the whole of small and medium chapters (CP.16, 55K chars; PE.19). Large chapters are cut off and offset does NOT reach the rest: GV.552 (346K chars by script) — WebFetch reported only ~103K chars, ending at § 552.113; offset=100000 returned a fragment, § 552.325 NOT PRESENT. Use fetch_doc.py for any chapter over ~90K chars (e.g. GV.552, TX.151 434K, HS.481 295K, FA.153 215K, CR.38 155K), or the chapter PDF.
- **Currency:** Not on chapter files. Site-wide message from https://tcss.legis.texas.gov/api/GetProperty/StatutesCurrentMsg (shown in the app's Site Information panel) — observed: "current through the 89th 2nd Called Legislative Session, 2025"
- **Official status:** No official/unofficial or authentication statement found on the site's information panel or in the app text (statutes.capitol.texas.gov); Texas has no UELMA authentication statement on these files.
- **Hazard:** statutes.capitol.texas.gov (the address everyone cites, incl. old /Docs/CP/htm/CP.16.htm links) is a JavaScript app: the fetch tool and fetch_doc.py get only a code list. Rewrite to tcss.legis.texas.gov/resources/… instead.
- **Hazard:** large chapter files exceed the fetch tool's window and offsets do not recover the tail (GV.552 § 552.325 unreachable) — use fetch_doc.py
- **Hazard:** #section anchors are ignored by the fetch tool
- **Hazard:** no currency line in the files themselves
- **Hazard:** CCP recodification (eff. 1/1/2025) moved many articles; old article numbers may be absent
- **Hazard:** text includes future-effective versions: some sections appear twice ('Text of section effective on …') — check effective-date notes
- **Probe:** Tex. Civ. Prac. & Rem. Code § 16.003 → `https://tcss.legis.texas.gov/resources/CP/htm/CP.16.htm` — expect: "Except as provided by Sections 16.010, 16.0031, and 16.0045, a"
- **Evidence (2026-10-16):** WebFetch: § 16.003 YES 'Except as provided by Sections 16.010, 16.0031, and 16.0045, a'; complete through § 16.073. Second code: PE.19 § 19.02(b) YES 'A person commits an offense if the person: (1) intentionally'. fetch_doc.py verify OK on both; CR.38 art. 38.23 and GV.552 § 552.325 found by script grep. Large-chapter test: GV.552 § 552.325 NOT PRESENT in WebFetch even with offset.
- **Notes:** Bulk: per-code zips at https://tcss.legis.texas.gov/resources/Zips/{CODE}.htm.zip (also .pdf.zip, .doc.zip; CP.htm.zip 655,256 bytes, HTTP 200) and whole-code PDFs at /resources/SDocs/{CODENAME}.pdf (e.g. CIVILPRACTICEANDREMEDIESCODE.pdf, 1.8 MB) — list in https://statutes.capitol.texas.gov/assets/StatuteCodeDownloads.json (paths there are relative to /resources). Note /Zips/… without /resources → 404. API base https://tcss.legis.texas.gov/api/ (GetProperty/{name}, StatutesByDate/GetCodes/{yyyy-mm-dd}, DocViewer/GetDocument/…).

### `tx-statutes-justia` — Justia — Texas Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Texas codes, editions incl. 2023, 2024, 2025 ('View All Versions'); unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/texas/{code-slug}/title-{title}/[subtitle-{subtitle_letter}/]chapter-{chapter}/[subchapter-{subchapter_letter}/]section-{section_hyphenated}/`
  - Placeholders: code-slug = full code name lower-case hyphenated (civil-practice-and-remedies-code, penal-code). section dots → hyphens (16.003 → section-16-003; 19.02 → section-19-02). title/subtitle/subchapter are NOT in the citation: read them from the header of the official chapter file (tx-statutes-tcss: 'TITLE 2 … SUBTITLE B … SUBCHAPTER A') and lower-case the letters. Subtitle and subchapter segments are omitted where the code has none (penal-code/title-5/chapter-19/section-19-02/).
  - Index: `https://law.justia.com/codes/texas/`
  - Navigation: official chapter file header → title/subtitle/subchapter → Justia section URL
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge to the script)
  - fetch_doc.py: REFUSED (robots.txt challenge) for law.justia.com. WebFetch only.
- **Currency:** page header; Universal Citation line — observed: "2025 Texas Statutes; 'TX Civ Prac & Rem Code § 16.003 (2025)'"
- **Official status:** Third-party compilation; edition labelled by year.
- **Hazard:** 2025 edition may not reflect 89th Leg. called-session changes
- **Hazard:** hierarchy segments must be learned from the official file
- **Hazard:** shell blocked by Cloudflare
- **Probe:** Tex. Civ. Prac. & Rem. Code § 16.003 → `https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-2/subtitle-b/chapter-16/subchapter-a/section-16-003/` — expect: "Except as provided by Sections 16.010, 16.0031, and 16.0045, a"
- **Evidence (2026-10-16):** WebFetch: body YES; '2025 Texas Statutes'; 'TX Civ Prac & Rem Code § 16.003 (2025)'. Second code: /codes/texas/penal-code/title-5/chapter-19/section-19-02/ YES, '(b) A person commits an offense if the person: (1) intentionally'; editions 2023, 2024 also listed.

### `tx-statutes-publiclaw` — public.law — Texas Statutes

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Texas codes, one page per section; text as of May 2025 (before the 89th Leg. 2025 changes took effect).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://texas.public.law/statutes/tex._{code_slug}_section_{section}`
  - Placeholders: code_slug = public.law's abbreviation, lower-case with underscores: civ._practice_and_remedies_code, penal_code (others unverified — confirm from https://texas.public.law/statutes). section verbatim with dots (16.003, 19.02).
  - Index: `https://texas.public.law/statutes`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — disallows /admin, /api, /data, /demo, /images, /users; /statutes allowed
- **Currency:** index page header ('Updated …'); section page 'Up to date / Verified:' badge — observed: "index: 'Texas Statutes Updated May 26, 2025'; section: 'Verified: May 26, 2025'"
- **Official status:** No official-status statement; footer points to the Legislature as source and says 'Trust but verify.'
- **Hazard:** STALE: index still says Updated May 26, 2025 on 2026-10-16 — misses 89th Leg. (2025) R.S. and called-session amendments; the green 'Up to date' badge is misleading
- **Hazard:** inserts section titles into cross-references ('Sections 16.010 (Misappropriation of Trade Secrets), …'), so quotes will not match the official text verbatim
- **Probe:** Tex. Civ. Prac. & Rem. Code § 16.003 → `https://texas.public.law/statutes/tex._civ._practice_and_remedies_code_section_16.003` — expect: "Except as provided by Sections 16.010 (Misappropriation of Trade Secrets)"
- **Evidence (2026-10-16):** WebFetch: body YES; 'Up to date', 'Verified: May 26, 2025'. fetch_doc.py: 200, last-modified 11 May 2025; index 'Texas Statutes Updated May 26, 2025'. Second code: tex._penal_code_section_19.02 '(b) A person commits an offense if the person'.
- **Notes:** Last resort only; prefer tx-statutes-justia, and quote only from tx-statutes-tcss.

## B. Constitution

### `tx-constitution-tcss` — Texas Constitution — article and section files (tcss.legis.texas.gov/resources/CN)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Texas Legislative Council · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1876 as amended; one file per article, plus one file per section.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://tcss.legis.texas.gov/resources/CN/htm/CN.{article}/CN.{article}.{section}.htm`
  - Placeholders: article = Arabic numeral (art. I → 1, art. V → 5, art. XVI → 16). Per-section file: /CN/htm/CN.{article}/CN.{article}.{section}.htm (CN.1/CN.1.19.htm, CN.5/CN.5.1.htm, both HTTP 200). Whole article: /CN/htm/CN.{article}.htm with anchors name="{article}.{section}" (1.19). Lettered sections keep the letter (e.g. art. 3 § 49-g → 49-g; unverified).
  - Index: `https://tcss.legis.texas.gov/resources/CN/htm/CN.1.htm`
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - Per-section files are tiny (CN.1.19.htm 339 chars of text) — the best quote target. Article files fit the fetch tool (CN.1 ~29K chars).
- **Currency:** Not in files; site message https://tcss.legis.texas.gov/api/GetProperty/StatutesCurrentMsg — observed: "current through the amendments approved by voters in November 2025"
- **Official status:** No official-status statement found.
- **Hazard:** Roman article numbers in citations must be converted to Arabic
- **Hazard:** statutes.capitol.texas.gov/Docs/CN/… links are the JS shell — rewrite as for statutes
- **Probe:** Tex. Const. art. I, § 19 → `https://tcss.legis.texas.gov/resources/CN/htm/CN.1.htm` — expect: "No citizen of this State shall be deprived of life"
- **Evidence (2026-10-16):** WebFetch: art. 1 § 19 YES 'No citizen of this State shall be deprived of life'; runs through Sec. 37, not truncated. fetch_doc.py: CN.1/CN.1.19.htm holds § 19 alone; second citation art. V § 1 in CN.5.htm 'The judicial power of this State shall be vested in one Supreme Court'.
- **Notes:** Whole-constitution PDF: https://tcss.legis.texas.gov/resources/SDocs/THETEXASCONSTITUTION.pdf (from StatuteCodeDownloads.json; not fetched).

### `tx-constitution-justia` — Justia — Texas Constitution

- **Status:** REPORTED 2026-10-16 · **Tier 2** · Justia · text: **link-only** · official: unofficial
- **Coverage:** Articles 1-17 index pages; article 1 index ends at Sec. 32 (official text runs to Sec. 37) — stale.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/constitution/texas/articles/cn{article:04d}00.html`
  - Placeholders: Article 1 → cn000100.html (only pattern observed). The article page is a section index without body text; per-section page URLs not determined.
  - Index: `https://law.justia.com/constitution/texas/`
  - Navigation: index → article page (section list only) → section link (not probed)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
- **Currency:** page disclaimer — observed: "This Constitution may not be the most recent version."
- **Official status:** Page disclaimer: 'This Constitution may not be the most recent version.'
- **Hazard:** stale: missing art. 1 §§ 33-37
- **Hazard:** article page has no section text
- **Probe:** Tex. Const. art. I, § 19 → `https://law.justia.com/constitution/texas/articles/cn000100.html`
- **Evidence (2026-10-16):** WebFetch: index lists articles with link /constitution/texas/articles/cn000100.html; that page: § 19 body NOT PRESENT (title only), section list ends at Sec. 32.
- **Notes:** Low value; tx-constitution-tcss per-section files make a second official fetch possible (article file + section file).

## C. Court rules

### `tx-rules-appellate` — Texas Rules of Appellate Procedure (PDF)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas and Court of Criminal Appeals / txcourts.gov · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full TRAP, 147 pages, ~642K characters, two-column layout.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/1463134/texas-rules-of-appellate-procedure-02062026.pdf`
  - Placeholders: media id and filename date change on re-issue; take from the rules index.
  - Index: `https://www.txcourts.gov/rules-forms/rules-standards/`
  - Navigation: rules index → 'Texas Rules of Appellate Procedure'
- **Automation:** WebFetch ok · shell ok · robots: allowed (see tx-rules-civil)
  - The fetch tool's window ends in Rule 14.3; Rule 47.7 NOT PRESENT. Two-column pages: fetch_doc.py layout text interleaves columns (Rule 47.7 grep hit mixes with Rule 47.6); its verify falls back to reading-order text and succeeded.
- **Currency:** PDF cover; rules index 'Last Amended' — observed: "Updated with Amendments Effective February 6, 2026"
- **Official status:** Rules index: 'most current version approved by the Supreme Court of Texas'.
- **Hazard:** fetch tool truncation after Rule 14
- **Hazard:** two-column layout scrambles extracted text — quote from reading-order text
- **Hazard:** media id changes on re-issue
- **Probe:** Tex. R. App. P. 9.4 → `https://www.txcourts.gov/media/1463134/texas-rules-of-appellate-procedure-02062026.pdf` — expect: "Except for the record, a document filed with an appellate court"
- **Evidence (2026-10-16):** WebFetch: Rule 9.4 YES 'Except for the record, a document filed with an appellate court, including'; Rule 47.7 NOT PRESENT; truncated at Rule 14.3. fetch_doc.py verify 9.4 OK (reading-order text); 147 pp.
- **Notes:** TRAP 47.7 governs citation of unpublished opinions; TRAP 53 (petition for review) and 66-79 (PDR) define the history notations.

### `tx-rules-civil` — Texas Rules of Civil Procedure (PDF)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas / Texas Judicial Branch (txcourts.gov) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full TRCP incl. comments, 369 pages, ~998K characters.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/1463426/texas-rules-of-civil-procedure.pdf`
  - Placeholders: The /media/{id}/ number changes with each amendment; take the current link from the rules index.
  - Index: `https://www.txcourts.gov/rules-forms/rules-standards/`
  - Navigation: rules index → 'Texas Rules of Civil Procedure' link
- **Automation:** WebFetch ok · shell ok · robots: www.txcourts.gov: User-agent * disallows system paths (/umbraco/, /data/, /scripts/ …) and a few named /media PDFs (bench book, forms); rules PDFs allowed. Commented-out '# Crawl-delay: 720'.
  - The fetch tool's window ends inside Rule 21(f)(7); Rule 91a (page 69, offset ~195K) NOT PRESENT. fetch_doc.py reads all 369 pages.
- **Currency:** rules index table 'Last Amended' column (not in the PDF) — observed: "Texas Rules of Civil Procedure — Last Amended October 1, 2026"
- **Official status:** Rules page says the listed rules 'are the most current version approved by the Supreme Court of Texas'; no official-text statement in the PDF.
- **Hazard:** fetch tool truncation: only Rules 1-21 reachable
- **Hazard:** media id changes on re-issue
- **Hazard:** table of contents lists every rule title — never treat a TOC hit as the rule text
- **Probe:** Tex. R. Civ. P. 13 → `https://www.txcourts.gov/media/1463426/texas-rules-of-civil-procedure.pdf` — expect: "The signatures of attorneys or parties constitute a certificate by"
- **Evidence (2026-10-16):** WebFetch: Rule 13 YES 'The signatures of attorneys or parties constitute a certificate by'; Rule 91a.1 NOT PRESENT; truncated in Rule 21(f)(7). fetch_doc.py: 369 pp, 998,155 chars; Rule 91a body at p. 69 ('91a.1 Motion and Grounds'); verify Rule 13 OK.
- **Notes:** Local rules, forms and standing orders: https://topics.txcourts.gov/ (OCA database, not probed).

### `tx-rules-disciplinary` — Texas Disciplinary Rules of Professional Conduct (PDF)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas / txcourts.gov · text: **fetch-and-quote** · official: unknown
- **Coverage:** TDRPC with comments, 118 pages, ~371K characters.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/1459244/texas-disciplinary-rules-of-professional-conduct-pdf.pdf`
  - Placeholders: media id changes on re-issue; take from the rules index.
  - Index: `https://www.txcourts.gov/rules-forms/rules-standards/`
  - Navigation: rules index → 'Texas Disciplinary Rules of Professional Conduct'
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - Not WebFetch-probed (budget). At ~371K chars expect the window to end in Rule 1.0x; Rule 1.06 sits at offset ~83.6K so it is probably inside window 1.
- **Currency:** PDF cover; rules index 'Last Amended' — observed: "(Effective March 7, 2025)"
- **Official status:** Rules index statement only.
- **Hazard:** fetch tool truncation expected (371K chars)
- **Probe:** Tex. Disciplinary Rules Prof'l Conduct R. 1.06(a) → `https://www.txcourts.gov/media/1459244/texas-disciplinary-rules-of-professional-conduct-pdf.pdf` — expect: "A lawyer shall not represent opposing parties to the same litigation."
- **Evidence (2026-10-16):** fetch_doc.py: 118 pp, 370,680 chars, cover '(Effective March 7, 2025)'; verify Rule 1.06(a) OK at p. 28. WebFetch not run.
- **Notes:** Bluebook cites these as reprinted in Tex. Gov't Code Ann., tit. 2, subtit. G, app. A.

### `tx-rules-evidence` — Texas Rules of Evidence (PDF)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas and Court of Criminal Appeals / txcourts.gov · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full TRE with comments, 62 pages, ~145K characters.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/1463074/texas-rules-of-evidence-updated-with-amendments-effective-07022026.pdf`
  - Placeholders: media id changes on re-issue; take from the rules index.
  - Index: `https://www.txcourts.gov/rules-forms/rules-standards/`
  - Navigation: rules index → 'Texas Rules of Evidence'
- **Automation:** WebFetch ok · shell ok · robots: allowed
  - The fetch tool's window reaches Rule 803(9) (cut mid-803(10)); Rules 803(10)-1009 need offset=100000 or fetch_doc.py.
- **Currency:** PDF cover; rules index — observed: "Effective July 2, 2026"
- **Official status:** Rules index statement only.
- **Hazard:** fetch tool truncation mid-Rule 803
- **Probe:** Tex. R. Evid. 401 → `https://www.txcourts.gov/media/1463074/texas-rules-of-evidence-updated-with-amendments-effective-07022026.pdf` — expect: "Evidence is relevant if: (a) it has any tendency to"
- **Evidence (2026-10-16):** WebFetch: Rule 401 YES; Rule 702 YES 'A witness who is qualified as an expert by knowledge,'; truncated in 803(10). fetch_doc.py: 62 pp, 144,658 chars; verify 401 OK.

### `tx-rules-judicial-admin` — Texas Rules of Judicial Administration (PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Texas / txcourts.gov · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules of Judicial Administration.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/1462861/texas-rules-of-judicial-administration-07012026.pdf`
  - Placeholders: media id changes on re-issue.
  - Index: `https://www.txcourts.gov/rules-forms/rules-standards/`
  - Navigation: rules index → 'Texas Rules of Judicial Administration'
- **Automation:** WebFetch untested · shell untested · robots: allowed
  - Link read from the rules index only.
- **Currency:** rules index 'Last Amended' — observed: "Last Amended July 1, 2026"
- **Official status:** Rules index statement only.
- **Probe:** Tex. R. Jud. Admin. 6.1 → `https://www.txcourts.gov/media/1462861/texas-rules-of-judicial-administration-07012026.pdf`
- **Evidence (2026-10-16):** Link and 'Last Amended July 1, 2026' read from the rules index (curl); document not fetched.
- **Notes:** Same index also lists the Code of Judicial Conduct (June 12, 2026), Rules of Disciplinary Procedure (Oct. 1, 2024), Judicial Bypass Rules, Statewide e-filing rules for criminal cases.

## D. Administrative code

### `tx-tac-sos` — Texas Administrative Code — Secretary of State 'Rules & Meetings' portal

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Texas Secretary of State, Texas Register Section · text: **link-only** · official: unknown
- **Coverage:** All TAC titles, current and historical rule versions (per SOS guide 'view-search-TAC.pdf', Last Revised December 2024).
- **Access:** `link-only` · format html
  - Placeholders: Appian portal; rules are reached by drop-down selection (Title, Part, Chapter, Subchapter, Rule), no stable per-rule URL found. The legacy viewer texreg.sos.state.tx.us/public/readtac$ext.TacPage?…&ti={title}&pt={part}&ch={chapter}&rl={rule} now returns a 'This Site Has Moved' redirect page.
  - Index: `https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=LANDING_PAGE`
- **Automation:** WebFetch fail · shell http-error · robots: texas-sos.appianportalsgov.com/robots.txt → 404 page (none). Legacy texreg.sos.state.tx.us robots: no '*' group; disallows only named bots (GPTBot, bingbot, Googlebot, …).
  - Portal returns an empty JavaScript shell: fetch_doc.py 0 characters; WebFetch 'no readable body content', title 'Rules & Meetings'.
- **Currency:** not visible to tools
- **Official status:** Official publisher of the TAC; no statement seen (portal renders no text to tools).
- **Hazard:** JavaScript-only portal; no text for the fetch tool or script
- **Hazard:** legacy texreg readtac URLs (still cited everywhere) only redirect
- **Probe:** 16 Tex. Admin. Code § 3.1 → `https://texreg.sos.state.tx.us/public/readtac$ext.TacPage?sl=R&app=9&p_dir=&p_rloc=&p_tloc=&p_ploc=&pg=1&p_tac=&ti=16&pt=1&ch=3&rl=1`
- **Evidence (2026-10-16):** Legacy URL (fetch_doc.py): 204 chars 'This Site Has Moved' → appianportalsgov.com rules-and-meetings. Portal: script 0 chars; WebFetch empty shell.
- **Notes:** Agency-request copies (pdf/docx/txt by email) are offered through the portal — not usable by the skill.

### `tx-tac-lii` — Cornell LII — Texas Administrative Code

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** TAC per-section pages with Texas Register source notes; two versions kept.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/texas/{title}-Tex-Admin-Code-SS-{chapter}-{section}`
  - Placeholders: TAC § {chapter}.{section} → '{chapter}-{section}' (16 TAC § 3.1 → 16-Tex-Admin-Code-SS-3-1). Part is not in the URL.
  - Index: `https://www.law.cornell.edu/regulations/texas`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed (per Delaware probe of the same host)
  - Respect the 10-second crawl delay.
- **Currency:** page header; source note at end — observed: "State regulations are updated quarterly; 'Amended … 50 TexReg 0835, eff. 2/18/2025'"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag — compare the latest TexReg note with tx-register-sos before quoting
- **Hazard:** only tier-2 text route for the TAC
- **Probe:** 16 Tex. Admin. Code § 3.1 → `https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-1` — expect: "Filing requirements. (1) Except as provided under subsection (e) of"
- **Evidence (2026-10-16):** WebFetch: body YES '(a) Filing requirements. (1) Except as provided under subsection (e) of'; 'State regulations are updated quarterly; we currently have two versions available.' fetch_doc.py: 200, last-modified 7 Aug 2025, verify OK.
- **Notes:** Only one title probed; a second-title probe is an open question.

## D. Administrative register

### `tx-register-sos` — Texas Register (Secretary of State) — weekly issue PDFs

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Texas Secretary of State, Texas Register Section · text: **fetch-and-quote** · official: official
- **Coverage:** PDF 'backview' covers a rolling ~12 months (Nov. 7, 2025 - Oct. 16, 2026 on the probe date); older issues in the HTML archive (/texreg/archive/index.shtml, not probed).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.sos.state.tx.us/texreg/pdf/backview/{MMDD}/{MMDD}is.pdf`
  - Placeholders: MMDD = issue date (Friday). The backview index lists each issue with its page range ('October 9, 2026 - Pages 6983-7090'): find the issue whose range contains the cited TexReg page. Section PDFs: {MMDD}prop.pdf (proposed), {MMDD}with.pdf, {MMDD}gov.pdf, {MMDD}ag.pdf, {MMDD}con.pdf (contents).
  - Index: `https://www.sos.state.tx.us/texreg/pdf/backview/index.shtml`
  - Navigation: backview index → issue whose page range covers the cite → {MMDD}is.pdf
- **Automation:** WebFetch ok · shell ok · robots: none (www.sos.state.tx.us/robots.txt is empty, HTTP 200)
  - The fetch tool reads only to 51 TexReg 7113 of a 7091-7200 issue (truncated); use fetch_doc.py (whole 112-page issue, 734K chars) or the smaller section PDFs.
- **Currency:** issue cover line — observed: "Volume 51 Number 42 October 16, 2026 Pages 7091 - 7200"
- **Official status:** The Texas Register is the State's official journal of agency rulemaking, published by the SOS (cover: 'a section of the Office of the Secretary of State'); no online-authentication statement.
- **Hazard:** MMDD folder names repeat every year — the backview holds one year only; older issues need the archive
- **Hazard:** fetch tool truncation ~20 pages into an issue
- **Hazard:** Texas Register search lives in the JS-only Appian portal
- **Probe:** 51 Tex. Reg. 7091 (Oct. 16, 2026) → `https://www.sos.state.tx.us/texreg/pdf/backview/1016/1016is.pdf` — expect: "Volume 51 Number 42 October 16, 2026 Pages 7091 - 7200"
- **Evidence (2026-10-16):** WebFetch: cover line matches; truncated after 51 TexReg 7113. fetch_doc.py: 112 pp, 734,516 chars, verify cover OK.

## E. Case law

### `tx-business-court-opinions` — Business Court of Texas — Opinions page and PDFs

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Business Court of Texas · text: **fetch-and-quote** · official: official
- **Coverage:** All Business Court opinions from 2024 Tex. Bus. 1 (court opened Sept. 1, 2024) to 2026 Tex. Bus. 73 (Oct. 12, 2026); one listing page, newest first.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/{id}/{cause-slug}-{case-slug}-{YYYY|YY}-tex-bus-{N}.pdf`
  - Placeholders: Filename embeds the cause number and citation (25-bc08a-0014-crain-v-northern-26-tex-bus-72.pdf) but the media id is not derivable: find the entry on the listing by 'YYYY Tex. Bus. N' or cause number, then follow 'Read the full opinion'. Corrected opinions get a new media id.
  - Index: `https://www.txcourts.gov/businesscourt/opinions/`
  - Navigation: listing → entry 'Name, YYYY Tex. Bus. N (Div.)' → 'Read the full opinion' PDF
- **Automation:** WebFetch ok · shell ok · robots: www.txcourts.gov — allowed
  - The fetch tool truncates the listing (reached back only to 2025 Tex. Bus. 23, June 18, 2025); fetch_doc.py reads the whole listing (141 /media links, back to 2024 Tex. Bus. 1).
- **Currency:** listing (newest entry) — observed: "FSTI v. PVS Minibulk, 2026 Tex. Bus. 73 (3d Div.) — October 12, 2026"
- **Official status:** The court assigns its own public-domain citation ('2026 Tex. Bus. 72') and paragraph numbers, which the listing says are its preferred citation format; the staff summaries on the listing are expressly not official.
- **Hazard:** listing truncates in the fetch tool
- **Hazard:** pinpoint by ¶, not page
- **Hazard:** corrected opinions re-posted under new media ids
- **Probe:** Crain v. Northern, 2026 Tex. Bus. 72 (8th Div.) → `https://www.txcourts.gov/media/1463443/25-bc08a-0014-crain-v-northern-26-tex-bus-72.pdf` — expect: "2026 Tex. Bus. 72"
- **Evidence (2026-10-16):** WebFetch listing: 'The Business Court prefers citations to paragraph numbers in its opinions, not page numbers.' fetch_doc.py PDF: 19 pp, header '2026 Tex. Bus. 72', 'Cause No. 25-BC08A-0014', '¶1 Before the Court is Defendant'.
- **Notes:** Appeals from the Business Court go to the Fifteenth Court of Appeals.

### `tx-cases-tames` — TAMES case search (search.txcourts.gov) — all appellate courts

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Texas Office of Court Administration · text: **link-only** · official: unofficial
- **Coverage:** Dockets, opinions, orders and briefs for the Supreme Court, Court of Criminal Appeals and the First through Fifteenth Courts of Appeals ('Released Orders & Opinions', 'Hand Downs').
- **Access:** `link-only` · format html
  - Pattern: `https://search.txcourts.gov/Case.aspx?cn={docket}&coa={court_code}`
  - Placeholders: court_code: cossup (Supreme Court), coscca (CCA), coa01…coa15 (courts of appeals). Recorded for linking only; never fetched.
  - Index: `https://search.txcourts.gov/`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-Agent: * / Disallow: /
  - fetch_doc.py: 'REFUSED: robots.txt on search.txcourts.gov disallows /CaseSearch.aspx?coa=cossup (rule: Disallow: /)'. WebFetch not attempted (robots refusal is respected for every tool).
- **Currency:** not fetched
- **Official status:** Docket system serving slip opinions and orders.
- **Hazard:** whole host disallowed by robots.txt
- **Hazard:** it is the only official host for court of appeals and CCA opinions and for CCA PDR dispositions
- **Probe:**  → `https://search.txcourts.gov/robots.txt`
- **Evidence (2026-10-16):** curl robots.txt 200: 'User-Agent: * Disallow: /'; fetch_doc.py REFUSED by robots.
- **Notes:** Court pages on www.txcourts.gov (e.g. /14thcoa/, /15thcoa/, /cca/) link 'Released Orders & Opinions' / 'Hand Downs' only to this host, so courts of appeals and CCA have no allowed tier-1 opinion route.

### `tx-scotx-orders-opinions` — Supreme Court of Texas — Orders & Opinions pages and opinion PDFs (txcourts.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas · text: **fetch-and-quote** · official: unofficial
- **Coverage:** One page per order/opinion release day from Oct. 2014 to date (year pages 2014-2026; /2013/ and earlier → 404). Each page lists orders on causes, petitions granted/denied, mandamus and habeas orders, and links each opinion, concurrence and dissent as a PDF.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/supreme/orders-opinions/{YYYY}/{month}/{month}-{D}-{YYYY}/`
  - Placeholders: month = full lower-case month name; D unpadded (may-29-2026). Release dates are irregular (usually Fridays, plus extra days): take them from the year page /supreme/orders-opinions/{YYYY}/. Opinion PDFs: /media/{id}/{docket without hyphen}{suffix}.pdf (240205.pdf; 240205c.pdf concurring; 240286d.pdf dissent) — the media id is not derivable; take it from the day page. Older pages may keep the hyphen (12-0657c1.pdf).
  - Index: `https://www.txcourts.gov/supreme/orders-opinions/`
  - Navigation: year page → release-day page → 'opinion of the Court' / 'concurring opinion' link (/media/…pdf). Print-friendly orders PDF on each day page (supreme-court-of-texas-orders-MM-DD-YYYY.pdf).
- **Automation:** WebFetch ok · shell ok · robots: www.txcourts.gov: '*' disallows system folders and a few named /media PDFs only; /supreme/ and opinion /media/ PDFs allowed
  - 'View Electronic Briefs' links on each page go to search.txcourts.gov (robots-blocked — do not follow).
- **Currency:** year page lists the latest release day — observed: "latest release-day page: October 16, 2026"
- **Official status:** Slip opinions with slip pagination; reported versions appear in S.W.3d (West).
- **Hazard:** slip pagination only — no S.W.3d page numbers
- **Hazard:** nothing before Oct. 2014 on txcourts.gov; older opinions only in TAMES (blocked) or Justia
- **Hazard:** no search: find by date or by docket within year pages
- **Probe:** Huffman Asset Mgmt., LLC v. Colter, No. 24-0205 (Tex. May 29, 2026) → `https://www.txcourts.gov/media/1462796/240205.pdf` — expect: "This residential-lease dispute involves an appeal from a no-answer default judgment"
- **Evidence (2026-10-16):** WebFetch: opinion YES, 15 pp, slip pagination, no S.W.3d cite for itself, not truncated. fetch_doc.py: 15 pp, 24,992 chars, verify OK. Day page May 29, 2026 lists 240205.pdf, 240205c.pdf, 240286.pdf/c/d, 241057.pdf. Older: June 12, 2015 page links /media/996482/130047.pdf.
- **Notes:** Opinions also posted for 2014-2026 per-day; earliest year page lists Oct.-Dec. 2014 days only.

### `tx-cases-justia` — Justia — Texas case law (Supreme Court, CCA, Courts of Appeals 1st-15th, Special Court of Review)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court year pages 1942, 1949-2026; Fourteenth Court of Appeals 1985-2026 (density not checked); Fifteenth Court of Appeals from Jan. 14, 2025; CCA 2026 includes AP/PD/WR dockets. No Business Court.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/texas/{court-slug}/{YYYY}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court | court-of-criminal-appeals | first-court-of-appeals … fifteenth-court-of-appeals | special-court-of-review. YYYY = decision year. docket-slug = docket lower-cased, commas → hyphens: '24-0205' → 24-0205; '05-23-00190-CV' → 05-23-00190-cv; 'PD-0643-25' → pd-0643-25; 'AP-77,122' → ap-77-122; 'WR-97,760-01' → wr-97-760-01. Several opinions on one docket get suffixes -0, -1 (concurrences/dissents); concurrences are NOT included on the main opinion page (24-0205.html omits Huddle, J., concurring). If the first guess fails, use the year listing /cases/texas/{court-slug}/{YYYY}/.
  - Index: `https://law.justia.com/cases/texas/`
  - Navigation: year listing lists every decision with docket and link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - fetch_doc.py: REFUSED (challenge). WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** the only allowed text route for court of appeals and CCA opinions
- **Hazard:** slip text, no S.W.3d pagination
- **Hazard:** -0/-1 suffix variants; separate opinions on separate pages
- **Hazard:** shell blocked
- **Probe:** Gonzalez v. Zubarik, No. 05-23-00190-CV (Tex. App.—Dallas Aug. 21, 2024) → `https://law.justia.com/cases/texas/fifth-court-of-appeals/2024/05-23-00190-cv.html` — expect: "This appeal arises from a dispute between homeowners regarding whether"
- **Evidence (2026-10-16):** WebFetch: 05-23-00190-CV YES, Aug. 21, 2024, complete, no S.W.3d cite. Also supreme-court/2026/24-0205.html YES (May 29, 2026); court-of-criminal-appeals/2026/ap-77-122.html YES, 'Do Not Publish'; fifteenth-court-of-appeals/2025/ listing (15-25-00116-cv.html, -0 concurrence).

## F. Subsequent history

### `tx-subsequent-cca-pdr-granted` — Court of Criminal Appeals — PDR Granted Issues list

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Texas Court of Criminal Appeals · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Pending granted PDRs only (alphabetical by appellant, PDR number, date granted, then issues). Refusals are NOT listed.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.txcourts.gov/media/{id}/pdrissues{MM-DD-YY}.pdf`
  - Placeholders: media id and date change with each update; take the 'PDR Issues' link from the index.
  - Index: `https://www.txcourts.gov/cca/issues-granted/`
  - Navigation: Issues Granted page → 'PDR Issues' PDF
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - Found by party name only (appellant surname); PDR numbers are CCA numbers (PD-NNNN-YY written as 'YY-NNNN').
- **Currency:** PDF title line — observed: "NO ISSUES GRANTED OCTOBER 15, 2026"
- **Official status:** Court staff list; 'wording of the issues is taken verbatim from the parties' petitions'.
- **Hazard:** grants only; party-name lookup only
- **Probe:** PDR granted list → `https://www.txcourts.gov/media/1462832/pdrissues10-15-26.pdf` — expect: "PDR GRANTED ISSUES"
- **Evidence (2026-10-16):** fetch_doc.py: 14 pp, 35,203 chars; 'PDR GRANTED ISSUES', 'ALPHABETICAL LISTING WITHOUT ISSUES', rows like '26-0257 AGUIRRE, ERIK 09/03/26'. WebFetch not run.

### `tx-subsequent-scotx-orders` — Supreme Court of Texas weekly orders — petitions for review granted/denied

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Texas · text: **fetch-and-quote** · official: official
- **Coverage:** Oct. 2014 to date. Every petition entry gives SC docket, parties, county, court of appeals district and the COA docket, reporter cite and judgment date, e.g. '(05-23-00190-CV, ___ SW3d ___, 08-21-24)'. Also mandamus, habeas, rehearing dispositions.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.txcourts.gov/supreme/orders-opinions/{YYYY}/{month}/{month}-{D}-{YYYY}/`
  - Placeholders: No search. Petition for review must be filed within 45 days of the COA judgment (TRAP 53.7) and is usually decided 3-12 months later: scan the release-day pages after the COA judgment date for the COA docket number (NN-YY-NNNNN-CV) — it appears verbatim on the page. WebSearch with the quoted COA docket and site:txcourts.gov did not find it (2026-10-16 test returned unrelated pages).
  - Index: `https://www.txcourts.gov/supreme/orders-opinions/`
  - Navigation: year page → each release-day page after the COA judgment → search page text for the COA docket under 'PETITIONS FOR REVIEW ARE DENIED' / 'GRANTED'
- **Automation:** WebFetch ok · shell ok · robots: allowed
  - A script could crawl the ~60 day pages per year once and index COA docket → disposition (see script_candidates).
- **Currency:** year page — observed: "latest release-day page: October 16, 2026"
- **Official status:** The Court's own orders lists ('Orders Pronounced'), also as print-friendly PDF.
- **Hazard:** no docket search; linear scan of day pages
- **Hazard:** denials before Oct. 2014 not on txcourts.gov
- **Hazard:** criminal cases never appear here (CCA handles PDRs)
- **Probe:** Gonzalez v. Zubarik, No. 05-23-00190-CV (Tex. App.—Dallas 2024) → pet. denied, No. 24-0824 (Tex. May 29, 2026) → `https://www.txcourts.gov/supreme/orders-opinions/2026/may/may-29-2026/` — expect: "05-23-00190-CV"
- **Evidence (2026-10-16):** WebFetch: under 'THE FOLLOWING PETITIONS FOR REVIEW ARE DENIED': 24-0289 (02-22-00347-CV …), 24-0824 (05-23-00190-CV, ___ SW3d ___, 08-21-24), 25-0202 (14-22-00856-CV …). fetch_doc.py verify '05-23-00190-CV' OK.
- **Notes:** Same page shows 'pet. granted' dispositions (e.g. 26-0110 from the 15th COA, 15-25-00116-CV, 729 SW3d 483).

### `tx-subsequent-tames` — TAMES case pages — petition/PDR status for every appellate case

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Texas Office of Court Administration · text: **link-only** · official: unofficial
- **Coverage:** COA case page shows 'Petition for Review' / 'PDR' events and the higher-court case; CCA hand-down lists record 'PDR refused'.
- **Access:** `link-only` · format html
  - Pattern: `https://search.txcourts.gov/Case.aspx?cn={coa_docket}&coa=coa{NN}`
  - Placeholders: Link only; never fetched.
  - Index: `https://search.txcourts.gov/`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: User-Agent: * / Disallow: /
  - Criminal 'pet. ref'd' history therefore cannot be confirmed from an allowed source; report it as stated in the citing opinion.
- **Currency:** not fetched
- **Official status:** Docket system.
- **Hazard:** robots-blocked
- **Probe:**  → `https://search.txcourts.gov/robots.txt`
- **Evidence (2026-10-16):** robots.txt 'User-Agent: * Disallow: /'.

## Not available (do not look for these again)

- **case_law** — Allowed tier-1 source for Texas Courts of Appeals and Court of Criminal Appeals opinions: www.txcourts.gov court pages (/14thcoa/, /15thcoa/, /cca/) link opinions only to search.txcourts.gov, whose robots.txt disallows everything; no other official host found. Justia (tier 2) is the only allowed text route. (2026-10-16)
- **case_law** — Supreme Court of Texas orders/opinions pages before October 2014 on txcourts.gov: /supreme/orders-opinions/ lists years 2014-2026; /2013/, /2012/, /2010/, /2008/, /2005/, /2000/ return 404; 2014 page has Oct.-Dec. only. (2026-10-16)
- **case_law** — Free official reporter (S.W.3d) pagination: Supreme Court and COA slip opinions carry slip pagination only; orders lists print '___ SW3d ___' for unreported pages. S.W.3d is a West reporter; Texas has no official state reporter since 1962 (Tex.) / 1963 (Tex. Crim.) (per memory). (2026-10-16)
- **case_law** — Public-domain citation for the Supreme Court, CCA and courts of appeals: Only the Business Court uses one ('YYYY Tex. Bus. N'); other opinions and orders lists use docket numbers and S.W.3d. (2026-10-16)
- **subsequent_history** — Allowed source for CCA petition-for-discretionary-review refusals ('pet. ref'd'): CCA hand-downs are only on search.txcourts.gov (robots-blocked); the txcourts.gov 'Issues Granted' PDF lists grants only. (2026-10-16)
- **statutes** — Cornell LII Texas statutes: Not looked for beyond the brief's leads; LII is known to host only the TAC for Texas (unverified). (2026-10-16)

## Corpus candidates (maintainers)

- `tx-rules-civil` — 369 pp / ~998K chars; the fetch tool stops in Rule 21 of ~800 rules (Rule 91a unreachable).
- `tx-rules-appellate` — 147 pp / ~642K chars; the fetch tool stops at Rule 14.3 (Rule 47.7 unreachable).
- `tx-rules-evidence` — 62 pp / ~145K chars; the fetch tool stops mid-Rule 803(10).
- `tx-rules-disciplinary` — 118 pp / ~371K chars; exceeds the fetch window.
- `tx-statutes-tcss` — Large chapters (GV.552 346K, TX.151 434K, HS.481 295K, FA.153 215K, CR.38 155K chars) are cut off by the fetch tool and offsets do not reach later sections. · bulk: https://tcss.legis.texas.gov/resources/Zips/{CODE}.htm.zip (per code; also .pdf.zip, .doc.zip; whole-code PDF /resources/SDocs/{CODENAME}.pdf) — index https://statutes.capitol.texas.gov/assets/StatuteCodeDownloads.json

## Open questions

- Official status of tcss.legis.texas.gov text: no statement found in the app; whether Texas has adopted UELMA authentication for the statutes was not checked.
- Texas Administrative Code: no stable per-rule URL on the SOS Appian portal; whether the portal has a public API behind it was not investigated. Only one LII title probed (16 TAC § 3.1).
- Texas Register issues older than the rolling one-year PDF backview (HTML archive /texreg/archive/) not probed.
- TDRPC and PDR-issues PDFs not WebFetch-probed; Texas Rules of Judicial Administration not fetched (reported).
- Justia per-section Texas Constitution URLs not determined; Justia COA year listings show 1985 onward but actual density for 1985-2002 not checked.
- Greenbook (Texas Rules of Form) citation form for the Fifteenth Court of Appeals and the Business Court not confirmed from a primary source; the regex accepts 'Tex. App.—15th Dist.' as used in Supreme Court orders lists.
- CourtListener ids (tex, texcrimapp, texapp, texreview) unverified; Business Court id unknown.
- Session laws: capitol.texas.gov (Texas Legislature Online, robots allows /) enrolled-bill route not probed; LRL is closed to Anthropic agents by robots.txt.

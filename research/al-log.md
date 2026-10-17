# Alabama (al) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt status reads and downloads of the ALISON / admin-code / portal **JavaScript bundles** (public, robots-permitted static files) to find the apps' API endpoints — no refusal was worked around. WebFetch calls: 17 (of ~55): 3 refused by the session (2 provenance gate, 1 proxy URL-length limit), 2 CLIENT_ERROR on wrong Justia slugs. WebSearch: 4.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://alison.legislature.state.al.us/ | script check; curl robots | robots permits; /robots.txt = 200 text/html (app page, no rules) |
| https://alisondb.legislature.state.al.us/alison/CodeOfAlabama/1975/6-5-410.htm | script check ×3; curl | FETCH ERROR: proxy 502 "Tunnel connection failed" (host gone) |
| https://admincode.legislature.state.al.us/ | script check; curl robots | permits; robots.txt = app HTML |
| https://judicial.alabama.gov/ | script check; curl robots | permits; robots.txt 404 |
| https://acis.alabama.gov/ | script check | permits (robots 301) |
| https://publicportal.alappeals.gov/ | script check; curl | permits; robots.txt = app HTML |
| https://publicportal-api.alappeals.gov/ | script check; curl | permits; robots.txt 404 JSON "No static resource robots.txt" |
| https://law.justia.com/codes/alabama/ | script check | REFUSED: robots.txt answered with a bot check |
| https://www.law.cornell.edu/regulations/alabama | script check | permits; crawl-delay 10 |
| https://alabama.public.law/ | script check ×2; curl | FETCH ERROR: proxy 502 on robots.txt |
| https://arc-sos.state.al.us/ | script check | REFUSED: Disallow: / (not used) |
| https://www.sos.alabama.gov/ | script check | permits (not used further) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://alison.legislature.state.al.us/ | script links | 87 links; "Code of Alabama" → /code-of-alabama; "Acts" → /acts |
| https://alison.legislature.state.al.us/code-of-alabama | script info/read | html 1,822 chars, navigation only (Next.js shell) |
| https://alison.legislature.state.al.us/code-of-alabama?section=6-5-410 | script grep; curl | 0 matches; page config names NEXT_PUBLIC_FE_GRAPHQL_URL …/graphql |
| /_next/static/chunks/*.js | curl | queries codesOfAlabama, codeOfAlabamaScaffold, constitutionItem, constitutionTitles, instruments |
| WebSearch "alison…/code-of-alabama" section | WS | no per-section URLs |
| https://alison.legislature.state.al.us/code-of-alabama | WF | PROVENANCE_REQUIRED (gate; not a site refusal) |
| …/graphql?query={codesOfAlabama(where:{type:{eq:Section},displayId:{eq:"6-5-410"}})…} | script read | JSON 2,018 chars; "Section 6-5-410 Wrongful Act, Omission, or Negligence Causing Death." body (a)–(e) |
| same, 13A-6-2 / 40-1-1 / 6-2-38 | script read+grep | body + history ("(Acts 1977, No. 607, p. 812, §2005; …") each |
| …/graphql?query={scaffold: codeOfAlabamaScaffold} | script read | 1,154,719 chars hierarchy (codeId/parentId/displayId) |
| …/graphql codeId 2507 | script | "Article 23 Death." sectionRange "§6-5-410 to §6-5-411" |
| …/graphql instruments actNbr 2016-29 | script | SB22, Regular Session 2016, enrolledFileUrl …/2016RS/PrintFiles/SB22-Enr.pdf |
| https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2016RS/PrintFiles/SB22-Enr.pdf | script read | PDF 5 pp; "1 SB22 2 171578-3 3 By Senator Whatley" |
| https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2021RS/PrintFiles/212714-2.pdf | script info | PDF 1 p, 616 chars (from search) |
| WebSearch "law.justia.com codes alabama title 6 section 6-5-410" | WS | year-edition URLs; /codes/alabama/2024 |
| https://law.justia.com/codes/alabama/2024 | WF | "2024 Code of Alabama"; "These codes may not be the most recent version."; newer /2025/ |
| https://law.justia.com/codes/alabama/title-6/chapter-5/ | WF (built, not gated) | "2025 Code of Alabama"; articles by name only, no section ranges |
| https://law.justia.com/codes/alabama/title-6/chapter-5/article-23/section-6-5-410/ | WF | YES; "A personal representative may commence an action and recover such damages"; not truncated |
| https://law.justia.com/codes/alabama/title-13a/chapter-6/article-1/section-13a-6-2/ | WF | YES; "(a) A person commits the crime of murder if he"; 2025 |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| …/graphql?query={constitutionItems(where:{isContentNode:{eq:true}}){data{displayId title}}} | script | 112,360 chars; "Section 1 Equality and Rights of Men." … decimals 3.01, 6.01 |
| …/graphql constitutionItem displayId "13" | script | "That all courts shall be open; and that every person…" |
| …/graphql constitutionItem displayId "111.08" | script | "Implementation Date of Laws Providing for Conduct of the General Election." |
| …/graphql {constitutionTitles} | script | "Article I Declaration of Rights †§1 to §36.06" |
| https://law.justia.com/constitution/alabama/ | WF | heading "Alabama Constitution"; no version; Section 13 = CA-245544.html; truncated 100K/108K |
| https://law.justia.com/constitution/alabama/CA-245544.html | WF | YES; "That all courts shall be open; and that every person," |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://judicial.alabama.gov/ | script links | "Rules of Court" → /library/rulesofcourt |
| https://judicial.alabama.gov/library/rulesofcourt | script links | set pages CivilProcedure, RulesEV, AppellateProcedure, CriminalProcedure, JuvenileProcedure, RulesBarConduct, RulesJudicialAdm, SmallClaimsRules |
| set pages (7) | script links | per-rule PDFs docs/library/rules/cv12.pdf, CV28.pdf, ev702.pdf, cond4_1.pdf, cr4_1.pdf, jv1.pdf, crcr18.pdf, JA20B.pdf |
| https://judicial.alabama.gov/docs/library/rules/cv12.pdf | script verify | VERIFIED "failure to state a claim upon which relief can be granted"; 7 pp |
| …/cv28.pdf (lower-case of CV28) | script | 4 pp "Alabama Rules of Civil Procedure V. DEPOSITIONS AND DISCOVERY" |
| …/ev702.pdf | script | 6 pp; "[Amended 11-29-2011, eff. 1-1-2012.] Advisory Committee's Notes" |
| …/cond1_7.pdf, …/cr32_1.pdf, …/ap39.pdf | script | rule text; "Rule 32. Post-conviction remedies."; ap39 19 pp |
| https://judicial.alabama.gov/docs/library/rules/cv12.pdf | WF | YES; "A defendant shall serve an answer within thirty (30) days"; amendment note; not truncated |

## D — Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://admincode.legislature.state.al.us/ | script info/links; curl bundle | html 0 chars (Angular/React shell); 0 links; GraphQL client with persisted queries |
| https://admincode.legislature.state.al.us/api/graphql?query={document(number:"335-6-1-.01")…} | script | {"errors":[{"message":"PersistedQueryOnly"}]} — not pursued |
| WebSearch admincode … 335-6-1 / pdf chapter rule | WS ×2 | /api/chapter/335-1-A, /api/rule/335-1-A-F9, /api/aam/2026-08, file.admincode…/UpdatedMonthly/… |
| https://admincode.legislature.state.al.us/api/chapter/335-6-1 | script | PDF 8 pp "Chapter 335-6-1" |
| https://admincode.legislature.state.al.us/api/rule/335-6-1-.01 | script | PDF 2 pp; definitions; "Author: David Ludder Statutory Authority" |
| …/api/rule/420-5-10-.01, …/api/rule/290-3-1-.01 | script | PDF 7 pp / 1 p |
| …/api/chapter/482-1-1, …/api/rule/810-3-1-.01 | script | HTTP 404 (no such chapter/rule) |
| https://admincode.legislature.state.al.us/api/chapter/335-1-A | WF | YES (Appendix A forms index); "Revised 4/14/24" |
| https://admincode.legislature.state.al.us/api/aam/2026-08 | script | PDF 65 pp, 119,551 chars; "VOLUME XLIV, ISSUE NO. 11 August 31, 2026" |
| https://admincode.legislature.state.al.us/api/aam/2026-09 | script | PDF 60 pp, Issue No. 12 |
| https://file.admincode.legislature.state.al.us/UpdatedMonthly/AAM-FEB-16/AAM-FEB-16.htm | script | permits; html 8,547 chars |
| https://www.law.cornell.edu/regulations/alabama/Ala-Admin-Code-r-335-6-1-.01 | script grep | body present; Notes "Amended: October 10, 1984." |
| https://www.law.cornell.edu/regulations/alabama/Ala-Admin-Code-r-420-5-10-.01 | script | html 18,012 chars |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://judicial.alabama.gov/Appellate/SupremeCourt (+ CivilAppeals, CriminalAppeals) | script links | "Decisions and Opinions Released After May 19, 2023" → portal; court UUIDs 68f021c4…, 1da1a297…, b82b30d5… |
| https://publicportal.alappeals.gov/ ; /properties.js | script info; curl | html 0 chars; apiRoot https://publicportal-api.alappeals.gov |
| https://publicportal-api.alappeals.gov/courts/cms/publications?courtID=…&page=0&size=… | script | JSON; SC 155 lists, CL 173, CR 156; latest "…Release List - October 16, 2026" |
| …/courts/68f021c4…/cms/publication/cff1fc0c… (Sept 4, 2026) | script | items with decision, title, documents |
| …/courts/68f021c4…/cms/publication/45450f03… (Aug 21, 2026) | script | Opinion documents, e.g. SC-2026-0199 |
| …/courts/68f021c4…/cms/case/C2B8B5A5…/docketentrydocuments/38D82535… | script | Opinion.pdf 14 pp; "Rel: August 21, 2026 … SUPREME COURT OF ALABAMA … SC-2026-0199" |
| …/courts/1da1a297…/cms/case/76A85AD2…/docketentrydocuments/8AD0DBA5… | script | CL-2026-0261 Opinion 16 pp, "Rel: October 16, 2026" |
| …/courts/b82b30d5…/cms/publication/ca20e16b… | script | CR-RELEASE-2026-10-16, "Application for Rehearing Overruled." |
| …/courts/68f021c4…/cms/cases/search?caseNumber=SC-2026-0199 (also SC-2022-0474, 1200113) | script | caseInstanceUUID, title |
| …/courts/cms/cases?caseHeader.caseNumber=SC-2026-0199 | script | 1 result (caseNumber= / searchTerm= ignored) |
| …/cms/cases/c2b8b5a5…/docketentries?size=100 | script | 27 entries incl. "Decision - Reversed and Remanded." |
| publicportal.alappeals.gov/portal/search/publication/results?criteria=… | WF | PROXY_REJECTED: URL exceeds maximum fetchable length |
| …/courts/cms/publications?courtID=68f021c4…&page=0&size=2… | WF | PROVENANCE_REQUIRED (gate) |
| https://judicial.alabama.gov/decision/supremecourtdecisions | script read/links | 255,520 chars; 151 acis displaydocs links, Jan 3, 2020 – May 19, 2023 |
| https://acis.alabama.gov/displaydocs2.cfm?no=10613&event=6MD0V6TYR | script | PDF 4 pp "SUPREME COURT OF ALABAMA DECISIONS ANNOUNCED ON FRIDAY, MAY 19, 2023" |
| https://law.justia.com/cases/alabama/supreme-court/2026/ | WF | 3 latest (Sept 25, 2026), e.g. sc-2025-0242-0.html |
| https://law.justia.com/cases/alabama/supreme-court/2026/sc-2026-0563.html | WF | YES "In this wrongful-death case, Adam Bauman and Beth Bauman, as"; slip pp 1-10; PDF link |
| https://law.justia.com/cases/alabama/court-of-criminal-appeals/2026/ | WF | CLIENT_ERROR (wrong slug) |
| https://law.justia.com/cases/alabama/court-of-civil-appeals/2026/ | WF | CLIENT_ERROR (wrong slug) |
| WebSearch "law.justia.com cases alabama court-of-civil-appeals 2026" | WS | no Justia listing URL |
| https://law.justia.com/cases/alabama/ | WF | courts: supreme-court, court-of-appeals-civil, court-of-appeals-criminal, court-of-appeals |
| https://law.justia.com/cases/alabama/court-of-appeals-criminal/ | WF | years 1933–2026; latest cr-2023-0282.html (Aug 21, 2026) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| …/courts/68f021c4…/cms/publication/6db2874a… (SC-RELEASE-2026-09-11) | script | "Certiorari Pre Examination Decision - Writ Denied. No Opinion." items (SC-2026-0461, -0671 …) with Order documents; titles name lower court docket |
| https://acis.alabama.gov/displaydocs2.cfm?no=10613&event=6MD0V6TYR (May 19, 2023 list) | script | "Writ Denied. No Opinion." with "Civil Appeals: CL-2022-0762" |

## Build
`python3 scripts/build.py --check`: no output for al.json. `--cross`: 2 lines, both Georgia's bare-rule branch (`Rule\s+NNN-NN-NN-.NN`, not context_required) claiming AL examples "Rule 420-5-10-.01, Ala. Admin. Code" and "Rule 335-6-1-.01" — fix belongs in ga.json.

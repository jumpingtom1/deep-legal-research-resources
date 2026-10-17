# Rhode Island (ri) probe log

Date of all probes: 2026-10-17. Agent: research. Tools: `fetch_doc.py --research` (script), WebFetch (WF), WebSearch (WS).
Quoted page text is limited to 15 words per entry.

## A. Statutes

| URL | Tool | Result |
|---|---|---|
| https://webserver.rilegislature.gov/Statutes/TITLE9/9-1/9-1-14.htm | script info/read | 200 HTML 1,729 chars; "R.I. Gen. Laws § 9-1-14 ... Actions for words spoken shall be commenced"; History of Section; last-modified 2025-11-06 |
| https://webserver.rilegislature.gov/Statutes/TITLE9/9-1/INDEX.htm | script | 200, 4,539 chars, "Index of Sections" listing every section (no ranges) |
| https://webserver.rilegislature.gov/Statutes/TITLE11/11-41/11-41-1.htm | script | 200, 1,559 chars, R.I. Gen. Laws § 11-41-1 |
| https://webserver.rilegislature.gov/Statutes/TITLE9/INDEX.HTM | script read/links | 200, "Index of Chapters"; 40 chapter links (9-1, 9-1.1 ...) |
| https://webserver.rilegislature.gov/Statutes/ | script | 200, title list (TITLE 6A Uniform Commercial Code ...) |
| https://webserver.rilegislature.gov/Statutes/TITLE6A/6A-2/6A-2-725.htm | script grep | 200; "An action for breach of any contract for sale must be commenced within four (4) years" |
| https://webserver.rilegislature.gov/Statutes/TITLE42/42-35/42-35-15.htm | script grep | 200; "§ 42-35-15. Judicial review of contested cases." |
| https://webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-19.1.htm | script grep | 200, 10,904 chars; "§ 28-14-19.1. Misclassification of employees." |
| https://webserver.rilegislature.gov/robots.txt | script | HTTP 404 (no rules) |
| https://webserver.rilegislature.gov/Statutes/TITLE9/9-1/9-1-14.htm | WF | PROVENANCE_REQUIRED (permission prompt not answered) - gated |
| WS "Rhode Island General Laws rilegislature.gov statutes disclaimer ..." | WS | Statutes.html, Disclaimer.aspx, Justia editions |
| https://webserver.rilegislature.gov/Statutes/Statutes.html | WF | OK; "Search the 2026 General Laws"; "should not be relied upon as an official record"; "This information is provisional." Title links http://...//Statutes/TITLEn/INDEX.HTM |
| https://rilegislature.gov/Pages/Disclaimer.aspx | WF | OK; informational service only, provisional, refer to printed official publication |
| http://webserver.rilegislature.gov//Statutes/TITLE9/INDEX.HTM | WF | PROVENANCE_REQUIRED (gated) |
| WS "webserver.rilegislature.gov PublicLaws law24 ..." | WS | Lawrevision/laws2024.htm, plshort/pl2024nu.htm etc. |
| https://webserver.rilegislature.gov/PublicLaws/law24/law24001.htm | script | 200, 1,056 chars; "Chapter 001 2024 -- H 7068 Enacted 02/02/2024" |
| https://webserver.rilegislature.gov/PublicLaws/law24/law24.htm | script | network error: connection reset (not an index; ignored) |
| https://webserver.rilegislature.gov/PublicLaws/ | script | HTTP 404 |
| https://webserver.rilegislature.gov/Lawrevision/laws2024.htm | script links | 200; Chapter Number / Bill Number / Subject / Act / Resolution links |
| https://webserver.rilegislature.gov/Lawrevision/plshort/pl2024nu.htm | script links | 472 links to PublicLaws/law24/law24NNN.htm |
| https://webserver.rilegislature.gov/PublicLaws/law25/law25123.htm | script | 200, 9,692 chars; "Chapter 123 2025 -- S 0509 SUBSTITUTE A" |
| https://webserver.rilegislature.gov/Lawrevision/laws1995.htm | script | HTTP 404 |
| https://webserver.rilegislature.gov/PublicLaws/law95/law95001.htm | script | 200, 928 chars |
| https://law.justia.com/codes/rhode-island/title-9/chapter-9-1/section-9-1-14/ (and 6A-2-725) | script | REFUSED: law.justia.com robots.txt challenge, host off for the day |
| WS "law.justia.com codes rhode-island title-9 ..." | WS | title-9 page, yearly editions 2012-2025 |
| https://law.justia.com/codes/rhode-island/title-9/ | WF | OK; "2025 Rhode Island General Laws"; chapter-9-1, chapter-9-1-1, chapter-9-2 |
| https://law.justia.com/codes/rhode-island/title-9/chapter-9-1/section-9-1-14/ | WF | YES; "Actions for words spoken shall be commenced and sued within" |
| https://law.justia.com/codes/rhode-island/title-28/chapter-28-14/section-28-14-19-1/ | WF | YES; "The misclassification of a worker whether performing work as a" |
| https://rhode-island.public.law/ | script check/info | robots.txt unreachable: proxy "Tunnel connection failed: 502 Bad Gateway" |
| https://www.law.cornell.edu/states/rhode_island | script links | links out to rilin.state.ri.us (Constitution, Statutes) and courts.ri.gov; LII hosts RI regulations only |

## B. Constitution

| URL | Tool | Result |
|---|---|---|
| https://webserver.rilegislature.gov/RiConstitution/ | script links | 1 malformed link to rilegislature.gov/riconstitution/pages/default.aspx |
| https://www.rilegislature.gov/riconstitution/pages/default.aspx | script check/info/links | robots permits; links ConstFull.aspx, C01.aspx ... C15 |
| https://www.rilegislature.gov/robots.txt | script | 200; Disallow only /Special/comdoc/*.pdf and /senators/SenateComDocs/*.pdf |
| https://www.rilegislature.gov/riconstitution/Constitution/C01.aspx | script info/verify | 12,862 chars; VERIFIED "All free governments are instituted for the protection, safety, and happiness of the people." |
| https://www.rilegislature.gov/riconstitution/Constitution/C10.aspx | script verify | VERIFIED "The judicial power of this state shall be vested in one supreme court" |
| https://www.rilegislature.gov/riconstitution/Constitution/ConstFull.aspx | script | 70,612 chars; Article XV present at offset 69023 |
| https://www.rilegislature.gov/riconstitution/Constitution/C01.aspx | WF | PROVENANCE_REQUIRED (gated) |
| WS "law.justia.com constitution rhode-island" | WS | Justia constitution index; rilegislature ConstFull.aspx |
| https://rilegislature.gov/riconstitution/Constitution/ConstFull.aspx | WF | OK; Art. X § 1 "The judicial power of this state shall be vested in"; complete through Art. XV; no disclaimer |
| https://law.justia.com/constitution/rhode-island/ | WF | index only; links constintro.html, C01.html, C02.html; "may not be the most recent version" |
| https://law.justia.com/constitution/rhode-island/C01.html | WF | YES; "All free governments are instituted for the protection, safety, and" |

## E. Case law / F. Subsequent history

| URL | Tool | Result |
|---|---|---|
| https://www.courts.ri.gov/robots.txt | script | "User-agent: * Disallow: /*AllItems.aspx Disallow: /Lists/" |
| https://www.courts.ri.gov/Courts/SupremeCourt/Pages/Opinions%20and%20Orders%20Issued%20in%20Supreme%20Court%20Cases.aspx | script | HTTP 404 (old page, linked by LII) |
| WS "courts.ri.gov Supreme Court published opinions 2025 pdf" | WS | old Opinions-and-Orders page, oral argument calendar |
| https://www.courts.ri.gov/ | script links | Supreme Court Opinions search page, ood.aspx, court-rules.aspx |
| https://www.courts.ri.gov/Search/Pages/supreme-court-opinions.aspx | script | 4,739 chars; 10 default results linking /Opinions/Supreme-yy-n.pdf |
| https://www.courts.ri.gov/Search/Pages/supreme-court-opinions.aspx?k=Alicea | script | same 10 default results: GET query ignored |
| https://www.courts.ri.gov/Pages/ood.aspx | script | 10 recent links: /Published%20Orders/, /Opinions/EAP-, /Decisions/Superior-, /Decisions/District- |
| https://www.courts.ri.gov/Opinions/Supreme-23-43.pdf | script | PDF 28 pp, 44,310 chars; "No. 2023-43-C.A. ... State v. Lydia Alicea"; "subject to formal revision before publication in the Rhode Island Reporter" |
| https://www.courts.ri.gov/Courts/SupremeCourt/Pages/default.aspx | script links | Case Docket Search (publicportal), Case Summaries - Published Opinions |
| https://www.courts.ri.gov/Courts/SupremeCourt/Pages/published-opinions.aspx | script | 15,571 chars; summaries with dates/dockets, e.g. "7/30/2026 ... 2025-0247-Appeal"; links Supreme-25-247.pdf etc. |
| WS "courts.ri.gov Opinions Supreme 2012 OR 2014 ..." | WS | legacy Orders-(2012-2013).aspx, OpinionsOrders/pdf-files/08-37.pdf |
| .../Pages/Orders/Orders-(2012-2013).aspx; .../OpinionsOrders/Orders-(2009-2010).aspx; .../OpinionsOrders/pdf-files/08-37.pdf | script | all HTTP 404 |
| https://law.justia.com/cases/rhode-island/supreme-court | WF | years 1844-2026; 2026/23-251.html, 24-219.html, 25-247.html |
| https://law.justia.com/cases/rhode-island/supreme-court/2026/23-251.html | WF | YES; "The defendants, Brenda and Ernest Ricci (Mrs. Ricci and Mr. Ricci, respectively)"; No. 2023-251-Appeal; no A.3d |
| https://law.justia.com/cases/rhode-island/supreme-court/2015/ | WF | 14-199.html, 15-53.html, 14-145.html |
| https://www.courts.ri.gov/Opinions/Supreme-14-199.pdf, -14-145.pdf | script | HTTP 404 |
| https://www.courts.ri.gov/Opinions/Supreme-15-53.pdf | script | connection reset by peer (twice) |
| Supreme-{17..20}-{100..112}.pdf, Supreme-{19,20}-{1..45}.pdf, Supreme-21-{1..30}.pdf | script info | all non-200 (no hits) |
| https://www.courts.ri.gov/Published%20Orders/Supreme-26-268.pdf | script | PDF 3 pp; "No. 2026-268-M.P. In the Matter of Brian T. Dougan. ORDER" |
| WS "\"courts.ri.gov/Opinions/Supreme-\"" | WS | only legacy pages (stale index) |
| https://www.courts.ri.gov/Opinions/Supreme-21-34.pdf | script | PDF 78 pp, 128,829 chars; "No. 2021-34-C.A." (dissent) |
| https://www.courts.ri.gov/Opinions/Supreme-23-43.pdf | WF | PROVENANCE_REQUIRED (gated) |
| https://www.courts.ri.gov/Decisions/Superior-PC-2025-3316.pdf | script | PDF 9 pp; "(FILED: October 6, 2026) ... C.A. No. PC-2025-03316 ... DECISION" |
| https://www.courts.ri.gov/Decisions/District-AA26-48.pdf | script | PDF 12 pp; "A.A. No. 2026 - 48" |
| https://www.courts.ri.gov/Opinions/EAP-2026-11.pdf | script | Ethics Advisory Panel Op. 2026-11 |
| https://www.courts.ri.gov/Courts/SuperiorCourt/Pages/default.aspx | script links | no separate decisions list |
| https://publicportal.courts.ri.gov/PublicPortal | script check/info | robots permits; REFUSED HTTP 403 |
| https://publicportal.courts.ri.gov/PublicPortal | WF | landing page; "JavaScript must be enabled in order for you to use this application." |
| https://law.justia.com/rhode-island | WF | Supreme Court, Superior Court case lists; regulations on regulations.justia.com (not a vetted tier-2 host) |
| https://law.justia.com/cases/rhode-island/superior-court/ | WF | years 2000-2026; 2026/24-515.html, 25-187.html, 25-361.html |
| https://law.justia.com/cases/rhode-island/superior-court/2026/25-187.html | WF | YES; "Before the Court is Michael W. Miller and Karen A. Miller's"; NC-2025-0187 |
| https://www.courts.ri.gov/Decisions/Superior-NC-2025-0187.pdf | script | PDF 9 pp, 16,446 chars |
| https://www.courts.ri.gov/Decisions/Superior-NC-2025-187.pdf | script | HTTP 404 |

## C. Court rules

| URL | Tool | Result |
|---|---|---|
| https://www.courts.ri.gov/Legal-Resources/Pages/court-rules.aspx | script links | Supreme/Superior/Family/District/WCC/Traffic rule pages; RulesOfEvidence.pdf |
| https://www.courts.ri.gov/Legal-Resources/Pages/Supreme-Court-Rules.aspx | script links | Supreme-Rules-Article1..10.pdf (Article IV = Article4-2.pdf) |
| https://www.courts.ri.gov/Legal-Resources/Pages/Superior-Court-Rules.aspx | script links | Civil, Criminal, Practice, Arbitration PDFs |
| .../superiorcourt/Documents/SuperiorCourtRulesOfCivilProcedure.pdf | script | 101 pp, 274,066 chars; footer "Page 2 of 101 February 2024"; '56. Summary Judgment' at page 80 |
| .../SupremeCourt/Documents/Supreme-Rules-Article1.pdf | script | 40 pp, 110,459 chars; "Revised February 17, 2026" |
| .../Legal-Resources/Documents/RulesOfEvidence.pdf | script verify | 26 pp, 70,330 chars; VERIFIED "These rules may be known and cited as the Rhode Island Rules of Evidence" |
| .../superiorcourt/Documents/SuperiorCourtRulesOfCriminalProcedure.pdf | script | 47 pp, 135,035 chars |
| .../SupremeCourt/Documents/Supreme-Rules-Article5.pdf | script | 160 pp, 449,497 chars |
| WS "Rhode Island Superior Court Rules of Civil Procedure pdf courts.ri.gov" | WS | courts.ri.gov (no www) civil rules PDF |
| https://courts.ri.gov/Courts/superiorcourt/Documents/SuperiorCourtRulesOfCivilProcedure.pdf | WF | Rule 56 NOT PRESENT; text stops mid Rule 26(b)(4)(A), "Page 38 of 101 February 2024" |
| Family-Court-Rules.aspx, District-Court-Rules.aspx | script links | RulesOfDomesticRelationsProcedure.pdf etc.; District_Civil_Rules.pdf etc. |
| .../familycourt/Documents/RulesOfDomesticRelationsProcedure.pdf | script | 81 pp, 218,250 chars |
| .../districtcourt/Documents/District_Civil_Rules.pdf | script | 76 pp, 205,067 chars |
| .../superiorcourt/Documents/SuperiorCourtRulesOfPractice.pdf | script | 9 pp, 23,846 chars |

## D. Administrative code and register

| URL | Tool | Result |
|---|---|---|
| https://rules.sos.ri.gov/robots.txt | script | HTTP 404 |
| https://rules.sos.ri.gov/ | script | admin login page only |
| WS "Rhode Island Code of Regulations RICR sos.ri.gov ..." | WS | rules.sos.ri.gov/regulations/Index/Proposed; regulations.justia.com (not vetted) |
| https://rules.sos.ri.gov/regulations/Index/Proposed | script | 365,775 chars, 296 links (Promulgations/part/...) |
| https://rules.sos.ri.gov/regulations/part/230-20-25-13 | script | 13,559 chars; "Senior Specifications (230-RICR-20-25-13) ACTIVE RULE"; "official Final Regulation" = Download link |
| https://rules.sos.ri.gov/regulations/part/250-150-05-3 | script | resolves, "250-RICR-150-05-3 ACTIVE RULE" |
| https://rules.sos.ri.gov/regulations/part/216-40-05-1 | script verify | 79,260 chars; VERIFIED "Licensure and Discipline of Physicians" |
| https://rules.sos.ri.gov/regulations/part/110-00-00-1 | script | no RICR heading matched (not pursued) |
| https://risos-apa-production-public.s3.amazonaws.com/DBR/REG_12051_20211217110227.pdf | script | PDF 4 pp; "230-RICR-20-25-13 TITLE 230 – DEPARTMENT OF BUSINESS REGULATION" |
| https://www.sos.ri.gov/divisions/open-government-center/rules-and-regulations | script | RICR, building/fire code, historic rules, guide, notifications; no register |
| https://rules.sos.ri.gov/Promulgations/part/100-50-00-2 | script | "100-RICR-50-00-2 PROPOSED RULE"; type of filing Amendment |
| https://www.law.cornell.edu/regulations/rhode-island | script links | title-100 ... index |
| https://www.law.cornell.edu/regulations/rhode-island/230-RICR-20-25-13 | script | 5,119 chars; generic index page, no part text |
| .../title-230, .../chapter-20, .../subchapter-25, .../part-13 | script links | section links 230-RICR-20-25-13.1 ... |
| https://www.law.cornell.edu/regulations/rhode-island/230-RICR-20-25-13.2 | script verify | VERIFIED "This Part shall apply to any solicitation, sale or purchase of" |
| https://www.law.cornell.edu/regulations/rhode-island/216-RICR-40-05-1.1 | script verify | VERIFIED "Authority" |
| https://www.law.cornell.edu/robots.txt | script | User-agent * Crawl-delay 10 |

## Build checks

- `python3 scripts/build.py --check`: no ERROR/WARN for ri.json.
- `python3 scripts/build.py --cross`: first run reported `CROSS dc: 'Rule 59(e) of the Superior Court Rules of Civil Procedure' also matches ri`. D.C. has the same rule-set title, so the RI prose form without "Rhode Island" was split into a `context_required` pattern (RI examples kept unchanged). Second run: no CROSS line naming ri.

WebFetch calls used: 23 (5 gated / PROVENANCE_REQUIRED). No quota failures.

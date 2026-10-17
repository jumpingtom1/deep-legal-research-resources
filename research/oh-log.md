# Ohio (oh) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `python3 scripts/fetch_doc.py --research` (or its `lsnet.get` with the same robots/challenge checks); "curl" = plain curl of robots.txt only; "POST" = one-off Python urllib POST to the public ROD search form (robots allows /rod/; no block involved); "WF" = WebFetch. About 27 WebFetch calls used. No CourtListener tools used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://codes.ohio.gov/robots.txt | curl | 200 text/plain, 26 bytes, Last-Modified 2021-04-01; whole body is one line `User-agent: * Disallow: /` (no newline) |
| same | script `check` on section-2305.10 | "allowlisted; robots.txt permits" (parser sees no Disallow rule) |
| https://www.supremecourt.ohio.gov/robots.txt | curl | 200; `User-agent: *` Disallow /cms/, /Content/ODCMB/; Sitemap /site-xml/ |
| https://supremecourt.ohio.gov/robots.txt | curl | 301 → www |
| https://registerofohio.state.oh.us/robots.txt (and www.) | curl | TLS: "unable to get local issuer certificate" |
| https://www.legislature.ohio.gov/robots.txt | curl | TLS: "unable to get local issuer certificate" |
| https://search-prod.lis.state.oh.us/robots.txt | curl | 404 "SOLAR API - Page Not Found" |
| law.justia.com | script | REFUSED (robots.txt challenge, recorded earlier today) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://codes.ohio.gov/ohio-revised-code/section-2305.10 | script info/read | 200 html 9,151 chars; "Section 2305.10 \| Bodily injury or injury to personal property."; "Effective: August 3, 2006" |
| same | WF (first try) | PROVENANCE_REQUIRED — approval not answered |
| WebSearch "codes.ohio.gov ohio-revised-code section-2305.10 bodily injury" | search | returned the section URL and an authenticated-PDF URL |
| same section URL | WF (after search) | YES "(A) Except as provided in division (C) or (E) of"; not truncated |
| https://codes.ohio.gov/ohio-revised-code/section-2903.01 | script grep | "No person shall purposely, and with prior calculation and design" |
| …/assets/laws/revised-code/authenticated/23/2305/2305.10/8-3-2006/2305.10-8-3-2006.pdf | script | PDF 3 pp, 8,133 chars; body present |
| https://codes.ohio.gov/ohio-revised-code/chapter-2305 | script | html 233,376 chars (full chapter text) |
| https://codes.ohio.gov/ohio-revised-code/title-23 | script | chapter list only, no section ranges |
| https://codes.ohio.gov/ohio-revised-code | script | title list |
| https://codes.ohio.gov/ohio-revised-code/section-1.42 | script | "Section 1.42 \| Common, technical or particular terms." |
| https://codes.ohio.gov/orc/2305.10 | script | redirected to /ohio-revised-code/section-2305.10 |
| https://codes.ohio.gov/disclaimer | script | 404 |
| https://codes.ohio.gov/about | script | UELMA: LSC's electronic Revised Code and Administrative Code "are official publications" |
| WebSearch "Ohio Revised Code bulk download XML … API" | search | only page URLs; no bulk |
| WebSearch "law.justia.com codes ohio title-23 chapter-2305 …" | search | edition/title URLs |
| https://law.justia.com/codes/ohio/2025 | WF | editions 2025, 2024, 2023 + "View All Versions"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/ohio/title-23/ | WF | chapter links, no section ranges |
| https://law.justia.com/codes/ohio/title-23/chapter-2305/ | WF | section hrefs …/section-2305-10/, …/section-2305-11/ |
| https://law.justia.com/codes/ohio/title-23/chapter-2305/section-2305-10/ | WF | YES "Except as provided in division (C) or (E) of this"; "OH Rev Code § 2305.10 (2025)" |
| https://law.justia.com/codes/ohio/title-29/chapter-2903/section-2903-01/ | WF (built) | YES "(A) No person shall purposely, and with prior calculation and design," |
| https://law.justia.com/codes/ohio/title-23/chapter-2305/section-2305-10/ | script | REFUSED (Cloudflare) |
| https://search-prod.lis.state.oh.us/api/v2/general_assembly_129/legislation/sb202/05_EN/pdf | script | PDF 5 pp "sb202_05_EN.pdf"; "AN ACT To enact section 2305.402 of the Revised Code" |
| same | WF | "(Substitute Senate Bill Number 202)"; Approved/Effective lines blank |
| …/general_assembly_126/legislation/sb17/05_EN/pdf | script | PDF 77 pp |
| …/general_assembly_135/legislation/hb33/07_EN/pdf | script | 404 |
| …/general_assembly_135/legislation/hb33 | script | JSON 266,882 chars, version array |
| …/general_assembly_129/legislation/sb202 | script | JSON 35,001 chars; fields apn, version_id, formatted_version, effective_date |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://codes.ohio.gov/ohio-constitution/section-1.16 | script | "All courts shall be open, and every person, for an injury"; "Effective: January 1, 1913" |
| https://codes.ohio.gov/ohio-constitution/section-4.2 | script | "(A) The Supreme Court shall, until otherwise provided by law, consist of seven judges" |
| https://codes.ohio.gov/ohio-constitution/section-1.10a | script | "Article I, Section 10a \| Rights of victims of crime" |
| https://codes.ohio.gov/ohio-constitution | script | article list (I–XIX, schedules) |
| https://law.justia.com/constitution/ohio/ | WF | index only; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/ohio/article-i/ | WF | section links only, e.g. /article-i/section-16/ |
| https://law.justia.com/constitution/ohio/article-i/section-16/ | WF | YES "All courts shall be open, and every person, for an" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.supremecourt.ohio.gov/laws-court-rules/ (and …/rules-of-practice-and-procedure/) | script | 404 (lead was wrong) |
| WebSearch "supremecourt.ohio.gov Ohio Rules of Civil Procedure PDF …" | search | /docs/LegalResources/Rules/civil/CivilProcedure.pdf; /laws-rules/ohio-rules-of-court |
| https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court | script | 58,342 chars; rule-set links + "Amended Effective Date" table (Civ. July 1, 2026; Evid. July 1, 2025; Gov.Bar Sept. 6, 2026; Sup.R. Aug. 6, 2026; Prof.Cond. Jan. 1, 2026; Prac. May 1, 2025) |
| …/Rules/civil/CivilProcedure.pdf | script | 927 pp, 2,137,404 chars; "RULE 12." at 160,622; 12(B) at 162,269 |
| same | WF | 12(B) NOT PRESENT; text stops after Rule 5, "[Content truncated due to length...]" |
| …/Rules/evidence/evidence.pdf | script | 102 pp, 185,608 chars; "RULE 702. Testimony by Experts." at 98,861 |
| same | WF (built) | PROVENANCE_REQUIRED — not retried |
| …/Rules/appellate/AppellateProcedure.pdf | script | 83 pp, 182,195 chars; "Rule 26. Application for Reconsideration" at 146,619 |
| …/Rules/criminal/CriminalProcedure.pdf | script | 193 pp, 374,255 chars; "RULE 11.1." at 77,826 |
| …/Rules/govbar/govbar.pdf | script | 276 pp, 715,862 chars; "RULE V. DISCIPLINARY PROCEDURE" at 102,791 |
| …/Rules/superintendence/Superintendence.pdf | script | 536 pp, 780,009 chars; "Rule 44 was renumbered to Rule 11.09" (2026 restructuring) |
| …/Rules/ProfConduct/profConductRules.pdf | script | 207 pp, 537,206 chars; "RULE 1.7: CONFLICT OF INTEREST: CURRENT CLIENTS" at 111,437 |
| …/Rules/practice/rulesofpractice.pdf | script | 128 pp, 254,512 chars; TOC "Rule 7.01. Institution of Jurisdictional Appeal" |
| …/Rules/reporting/Report.pdf | script | 8 pp; Rep.Op.R. 2.5 numbered paragraphs; 3.4 appellate opinions after May 1, 2002 citable |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://codes.ohio.gov/ohio-administrative-code/rule-3701-17-01 | script | 12,038 chars; "Effective: July 17, 2025"; "Promulgated Under: 119.03" |
| same (after WebSearch listed it) | WF | YES "As used in rules 3701-17-01 to 3701-17-26 of the Administrative"; "Last updated July 17, 2025 at 7:45 AM" |
| https://codes.ohio.gov/ohio-administrative-code/rule-4123-5-01 | script | "The administrator of workers' compensation may reorganize the work" |
| https://codes.ohio.gov/ohio-administrative-code/rule-4901:1-10-01 | script | "Rule 4901:1-10-01 \| Definitions." |
| https://codes.ohio.gov/ohio-administrative-code/chapter-3701-17 | script | chapter text |
| …/assets/laws/administrative-code/authenticated/3701/0/17/3701-17-01_20250717.pdf | script | PDF 7 pp |
| https://www.law.cornell.edu/regulations/ohio/Ohio-Admin-Code-3701-17-01 | script + WF | body present; Notes "Effective: 1/1/2018"; "updated quarterly; we currently have two versions available" |
| https://www.law.cornell.edu/regulations/ohio/Ohio-Admin-Code-4123-5-01 | script | "may reorganize the work of the bureau"; "Effective: 12/12/2019" |
| WebSearch "Register of Ohio … rule filings search" | search | /rules/search, jsessionid hearing URLs |
| https://www.registerofohio.state.oh.us/rules/search | WF | search form (Agency #, Division #, Chapter #, Rule # …); no filing links |
| https://registerofohio.state.oh.us/ | script | FETCH ERROR: TLS certificate chain does not verify |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| …/rod/docs/pdf/0/2023/2023-Ohio-1234.pdf and /8/2023/… | script | 404 (lead number not a real document in those folders) |
| WebSearch "supremecourt.ohio.gov rod docs pdf 0 2023 …" | search | several /rod/docs/pdf/0/2023/… URLs |
| …/rod/docs/pdf/0/2023/2023-Ohio-3042.pdf | script | Case Announcements 8/30/2023, lists Harris v. Hilderbrand 2023-Ohio-3005 |
| …/rod/docs/pdf/0/2023/2023-Ohio-3005.pdf | script | 12 pp; "[Cite as Harris v. Hilderbrand, 172 Ohio St.3d 471, 2023-Ohio-3005.]"; {¶ N}; slip pages |
| same | WF (built) | PROVENANCE_REQUIRED — not retried |
| …/rod/docs/pdf/7/2022/2022-Ohio-1555.pdf | script | 19 pp |
| …/rod/docs/pdf/8/2022/2022-Ohio-2039.pdf | script | 43 pp |
| …/rod/docs/pdf/0/2022/2022-Ohio-1555.pdf | script | 404 (wrong court folder) |
| …/rod/docs/pdf/{2,1,11,8}/2026/2026-Ohio-{1580,1178,3514,1870}.pdf | script | all 200 PDFs; 1580 "SECOND APPELLATE DISTRICT MONTGOMERY COUNTY" |
| …/rod/docs/pdf/0/1995/1995-Ohio-166.pdf | script | PDF 1 p |
| …/rod/docs/pdf/0/2023/2023-Ohio-3741.pdf | WF | Case Announcements; official-version list with "171 Ohio St.3d 278" |
| …/rod/docs/pdf/0/2024/2024-Ohio-989.pdf | WF | announcements, complete, 3 pp |
| …/rod/docs/pdf/0/2024/2024-Ohio-2967.pdf | WF | announcements #2, complete |
| …/rod/docs/pdf/0/2018/2018-Ohio-1429.pdf | WF | announcements #2, complete |
| https://www.supremecourt.ohio.gov/rod/docs/ | script | ASP.NET form (POST); court codes 0–13, 98–100; years 1992–2026; default listing 582 rows newest first |
| …/rod/docs/?ctl00$MainContent$tbWebCiteYear=2022&…Number=1555&…btnSubmit=Submit | script GET | ignored — default listing returned |
| same + __VIEWSTATE in query | script GET | 404 |
| ROD search WebCite 2022/1555 | POST | 1 row: Harris v. Hilderbrand, 21 JE 0013, Jefferson, 2022-Ohio-1555 |
| ROD search Case No. 2022-0784 (court 0) | POST | 1 row → 2023-Ohio-3005, 172 Ohio St.3d 471 |
| ROD search Citation "172 Ohio St.3d 471" | POST | 1 row → 2023-Ohio-3005 |
| ROD search court 0, year 1995 | POST | 516 rows (1995-Ohio-166 = 74 Ohio St.3d 186) |
| ROD search all districts 1993 / 1997 / 1999 / 2000 / 2001 / 2002 | POST | 0 / 0 / 234 / 597 / 1000 (cap) / 1000 (cap) |
| ROD search court 13 (Court of Claims) 2025 | POST | 163 rows (2025-Ohio-5905) |
| https://law.justia.com/cases/ohio/ | WF | 15 Ohio collections (Supreme, 12 districts, Claims, Common Pleas) |
| https://law.justia.com/cases/ohio/supreme-court-of-ohio/2023/ | WF | Harris → /2023/2022-0784.html |
| https://law.justia.com/cases/ohio/supreme-court-of-ohio/2023/2022-0784.html | WF | YES {¶ 1}–{¶ 34}, complete |
| https://law.justia.com/cases/ohio/seventh-district-court-of-appeals/2022/21-je-0013.html | WF (built) | YES "[Cite as Harris v. Hilderbrand, 2022-Ohio-1555.]" |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| ROD search court 0, text "\"discretionary appeals not accepted\"" 2026 | POST | 0 rows |
| ROD search court 0, text "Case Announcements" 2026 | POST | 329 rows; 2026-Ohio-3977 "Appeals not accepted for review" |
| …/rod/docs/pdf/0/2026/2026-Ohio-3977.pdf | script | 10 pp; "APPEALS NOT ACCEPTED FOR REVIEW … Lewis v. BMW of Westlake. Cuyahoga App. No. 115771, 2026-Ohio-1870." |
| ROD search court 0, text "\"2026-Ohio-1870\"" | POST | 2 rows: 2026-Ohio-3977, 2026-Ohio-3073 |
| ROD search court 0, text "\"2022-Ohio-1555\"" | POST | 3 rows: 2023-Ohio-3005, 2023-Ohio-3042, 2022-Ohio-3135 (appeals accepted) |
| …/rod/docs/pdf/0/2024/2024-Ohio-989.pdf | script grep | "DISCRETIONARY\|ACCEPTED\|declin": 0 matches (official-versions announcement) |
| …/rod/docs/pdf/0/2026/2026-Ohio-3997.pdf | script | "SLIP OPINIONS REPLACED BY OHIO OFFICIAL REPORTS VERSIONS AS OF OCTOBER 12, 2026" |
| https://www.supremecourt.ohio.gov/clerk/ecms/#/caseinfo/2022/0784 | script | html, 0 chars text (Ember SPA) |
| …/clerk/ecms/scripts/dist/site.min.js?ver=3 | script | route /caseinfo/:caseyear/:casenumber; ajaxCall("Ajax.ashx") actions CaseSearch (paramPriorCaseNumber) etc.; X-CSRF-TOKEN header; not called |

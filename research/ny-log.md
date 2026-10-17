# New York (ny) — probe log, 2026-10-16

All probes were run on 2026-10-16 by the research agent. Tools: WF = WebFetch, SH = curl from the workspace shell, WS = WebSearch (discovery only). Quoted page text is limited to 15 words per entry.

## Statutes / Constitution
| # | URL | Tool | Result |
|---|---|---|---|
| 1 | https://www.nysenate.gov/legislation/laws/CVP/3211 | WF | YES; "Rule 3211. Motion to dismiss. (a) Motion to dismiss cause"; "Viewing most recent revision (from 2022-05-13)"; complete; no disclaimer |
| 2 | same | SH | 200, server cloudflare, no cf-mitigated; 42,930 bytes; contains "Motion to dismiss cause of action." |
| 3 | https://www.nysenate.gov/robots.txt | SH | 200; Disallow /search/, /admin/, /core/, /profiles/ …; /legislation not disallowed |
| 4 | https://legislation.nysenate.gov/robots.txt | SH | 200; "User-agent: *" only |
| 5 | https://legislation.nysenate.gov/api/3/laws/CVP/3211 | SH | 401 JSON "A valid API key is needed to fulfill this request." errorCode 701 |
| 6 | https://legislation.nysenate.gov/api/3/laws?view=json | SH | 401 same |
| 7 | https://www.nysenate.gov/legislation/laws/CONSOLIDATED | SH | 200; 94 law IDs scraped (table in ny.json) |
| 8 | …/laws/all | SH | 200 (no law-ID listing) |
| 9 | …/laws/COURTACTS, RULES, MISC, UNCONSOLIDATED | SH | 200; RULES → CMA/CMS; MISC → CNS=Constitution; COURTACTS listing not parsed (JS); UNCONSOLIDATED 33 links |
| 10 | …/laws/CTC, FCT, CCA, NYC, UJC, UCT, SCP | SH | all 200 |
| 11 | …/laws/GOB/5-701; CNS/A1S11; PEN/155.05; EXC/296 | SH | 200; revisions 2014-09-22, 2025-01-10, 2024-07-26, 2026-06-05; EXC/296 119,730 bytes |
| 12 | …/laws/FCT/1012; SCP/2103; CCA/202 | SH | 200; revisions 2021-04-09, 2014-09-22, 2023-07-07 |
| 13 | …/laws/CVP/3211?date=2016-08-05 | SH | 200, still "Viewing most recent revision (from 2022-05-13)", so the history parameter is ignored (the history form is POST) |
| 14 | CVP/3211 HTML regex for "official", "disclaim" | SH | no disclaimer found |
| 15 | https://www.nysenate.gov/legislation/laws/GOB/5-701 | WF | YES; "§ 5-701. Agreements required to be in writing. a. Every"; revision 2014-09-22 |
| 16 | https://www.nysenate.gov/legislation/laws/CNS/A1S11 | WF | YES; "a. No person shall be denied the equal protection of"; revision 2025-01-10 |
| 17 | https://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO: | WF | ROBOTS_DISALLOWED |
| 18 | https://public.leginfo.state.ny.us/robots.txt | SH | curl (35) Connection reset by peer |
| 19 | https://www.nyassembly.gov/robots.txt, https://nyassembly.gov/leg/ | SH | 200 Apache (not pursued further) |
| 20 | https://newyork.public.law/robots.txt | SH | 200; Disallow /admin /api /data /demo /images /users |
| 21 | https://newyork.public.law/laws | SH | 200; "Updated October 10, 2026" |
| 22 | …/laws/n.y._civil_practice_law_and_rules_section_3211; …general_obligations_law_section_5-701; …penal_law_section_155.05 | SH | 200 each; source line cites nysenate.gov CVP/3211; "Verified: Oct. 10, 2026 Last modified: May 13, 2022" |
| 23 | https://newyork.public.law/laws/n.y._general_obligations_law_section_5-701 | WF | YES; "Every agreement, promise or undertaking is void, unless it or"; "Verified: Oct. 10, 2026" |
| 24 | https://newyork.public.law/laws | WF | "Updated September 26, 2026" (differs from the shell, suggesting a WebFetch cache); no Constitution or NYCRR |
| 25 | https://law.justia.com/robots.txt | SH | 403 cf-mitigated: challenge |
| 26 | https://law.justia.com/codes/new-york/cvp/article-32/3211/ | WF | CLIENT_ERROR (wrong slug; correct one is r3211) |
| 27 | https://law.justia.com/codes/new-york/ | WF | editions 2025 back to 2006 (no 2011) |
| 28 | https://law.justia.com/codes/new-york/2025/ | WF | CVP → /codes/new-york/cvp/ ; GOB → /codes/new-york/gob/ |
| 29 | https://law.justia.com/codes/new-york/cvp/ | WF | "2025 New York Laws"; "These codes may not be the most recent version." |
| 30 | https://law.justia.com/codes/new-york/cvp/article-32/ | WF | r3211, r3212 hrefs |
| 31 | https://law.justia.com/codes/new-york/cvp/article-32/r3211/ | WF | YES; "Rule 3211. Motion to dismiss. (a) Motion to dismiss cause"; complete |
| 32 | same | SH | 403 cf-mitigated: challenge |
| 33 | WS "dos.ny.gov New York State Constitution pdf" | WS | found constitution-january-1-2026.pdf |
| 34 | https://dos.ny.gov/system/files/documents/2025/12/constitution-january-1-2026.pdf | WF | "As revised, including amendments effective January 1, 2026"; art I §11 present; truncated in art V §1 |
| 35 | https://dos.ny.gov/new-york-state-constitution | WF / SH | CLIENT_ERROR / 403 |
| 36 | https://dos.ny.gov/robots.txt | SH | 200 "User-agent: *" with Drupal defaults |

## Court rules / Admin
| # | URL | Tool | Result |
|---|---|---|---|
| 37 | https://www.nycourts.gov/robots.txt | SH | 403 cf-mitigated: challenge (nycourts.gov without www returns 302 to www) |
| 38 | same | WF | User-agent *; Disallow /core/ /profiles/ /admin/ /search/ /user/login/; /reporter and /rules allowed |
| 39 | https://www.nycourts.gov/rules/trialcourts/202.shtml | WF (×2) | index only, with no 202 body; links to /rules/part-202-uniform-civil-rules-supreme-court-and-county-court and Parts 200-221 |
| 40 | https://www.nycourts.gov/rules/trialcourts/index.shtml | WF | CLIENT_ERROR |
| 41 | https://www.nycourts.gov/rules/part-202-uniform-civil-rules-supreme-court-and-county-court | WF | YES 202.1-202.9-a; 202.7 "There shall be compliance with the procedures prescribed in the"; 134,417 chars, cut at 100k; 202.8-g [Repealed]; no currency |
| 42 | https://www.nycourts.gov/rules | WF | "No results found matching your search criteria." (JS menu) |
| 43 | WS Part 1250/500/1200 | WS | found jointappellate page, RPC PDF, Part1250 PDF on justicetraining.nycourts.gov |
| 44 | https://www.nycourts.gov/legacypdfs/rules/jointappellate/NY Rules of Prof Conduct.pdf | WF | Part 1200 confirmed; "effective April 1, 2009"; 1.7(a) "Except as provided in paragraph (b), a lawyer shall not"; truncated |
| 45 | https://nycourts.gov/rules/jointappellate | WF | joint orders list only; no rule text; latest entry 2022 |
| 46 | WS Court of Appeals Part 500 | WS | found 500rules.htm, 500rules10.htm |
| 47 | https://www.nycourts.gov/CTAPPs/500rules10.htm | WF | YES; "On its own motion, the Court may examine its subject"; "Effective: May 8, 2024" |
| 48 | https://nycourts.gov/ctapps/500rules.htm | WF | TOC with anchors #10, #22; "Effective: December 10, 2025" |
| 49 | https://www.nycourts.gov/ctapps/500rules.htm | SH | 403 cf-mitigated: challenge |
| 50 | https://www.law.cornell.edu/robots.txt | SH | 200 nginx; Crawl-delay: 10 |
| 51 | https://www.law.cornell.edu/regulations/new-york/22-NYCRR-202.8-g | WF | YES; "Upon any motion for summary judgment, other than a motion"; repealed eff. 7/7/2025 |
| 52 | https://www.law.cornell.edu/regulations/new-york/22-NYCRR-1250.1 | WF | YES; "Unless the context requires otherwise, as used in this Part"; "updated quarterly" |
| 53 | https://www.law.cornell.edu/regulations/new-york/12-NYCRR-23-1.7 | WF | YES; "(a) Overhead hazards. (1) Every place where persons are required" |
| 54 | https://www.law.cornell.edu/regulations/new-york/22-NYCRR-202.70 | WF | NO; returned the title TOC (soft 404) |
| 55 | https://govt.westlaw.com/nycrr/ | WF | SITE_BLOCKED "Access to this website has been blocked" |
| 56 | https://govt.westlaw.com/robots.txt | SH | 403 |
| 57 | https://dos.ny.gov/state-register | WF | latest "The October 14, 2026/Vol. XLVIII, Issue 41"; archive 2015-2026; DAR "the official compiler … (NYCRR)" |
| 58 | https://dos.ny.gov/october-14-2026vol-xlviii-issue-41 | WF | CLIENT_ERROR |

## Case law / subsequent history
| # | URL | Tool | Result |
|---|---|---|---|
| 59 | https://nycourts.gov/reporter/3dseries/2023/2023_04822.htm | SH | 302 to www, then www returns 403 challenge |
| 60 | https://www.nycourts.gov/reporter/3dseries/2023/2023_04822.htm | WF | Mejia v Linares, AD1 9/28/2023; [219 AD3d 1251]; "As corrected through Wednesday, November 8, 2023"; complete |
| 61 | https://www.nycourts.gov/reporter/3dseries/2024/2024_50001.htm | WF | People v Bowman, Webster Town Ct; 81 Misc 3d 1223(A); "will not be published in the printed Official Reports" |
| 62 | https://www.nycourts.gov/reporter/slipidx/slipidxmain.shtml | WF | 404 page |
| 63 | https://www.nycourts.gov/reporter/ | WF | current indexes per court; motions lists; bound volumes "starting with 1999"; Westlaw Official Reports link |
| 64 | https://www.nycourts.gov/reporter/bound-volumes.shtml | WF | series headings only; no PDF links visible |
| 65 | https://www.nycourts.gov/reporter/Decisions.shtml | WF | coverage statements: CoA decisions "Coverage begins in October 2003." etc. |
| 66 | https://www.nycourts.gov/reporter/current/index/aidxtable_1.shtml | WF | Oct 2026 by date; Title/Judge/Docket No./Slip Op columns; links to current/3dseries/…shtml |
| 67 | https://www.nycourts.gov/reporter/current/index/mots_coa_list.shtml | WF | CoA motions by date; links current/motions/2026/2026_772xx.shtml |
| 68 | https://www.nycourts.gov/reporter/current/motions/2026/2026_77266.shtml | WF | "Motion for reargument of motion for leave to appeal denied."; Motion No 2026-201 |
| 69 | https://www.nycourts.gov/reporter/motindex/coa-motions-archive.shtml | WF | year headings 2003-2026, no visible links |
| 70 | https://www.nycourts.gov/reporter/3dseries/2026/2026_05997.htm | WF | 404 ERROR PAGE (current-month decision) |
| 71 | WS nycourts reporter motions 2023 | WS | /reporter/motions/2023/2023_7xxxx.htm URLs |
| 72 | https://www.nycourts.gov/reporter/motions/2023/2023_73590.htm | WF | AD2 "Motion No: 2023-07520"; "ORDERED that the motion is denied."; (U), Index No. given |
| 73 | https://www.nycourts.gov/reporter/current/3dseries/2026/2026_05997.shtml | WF | BFAM v Glory Health, AD1 10/15/2026; "uncorrected and subject to revision"; complete |
| 74 | WS CoA leave denied 2024 | WS | /reporter/motions/2024/2024_7xxxx.htm |
| 75 | https://www.nycourts.gov/reporter/motions/2024/2024_74436.htm | WF | Brown v Annucci, CoA; "Motion No: 2024-250"; "Motion for leave to appeal denied." |
| 76 | https://www.nycourts.gov/reporter/current/index/ad1-decisions-archive.shtml | WF | year headings 2003-2026, no visible links |
| 77 | WS slipidx aidxtable | WS | slipidx/{idx}_{year}_{month}.shtml and motindex/mots_at2_09-2022.shtml patterns |
| 78 | https://www.nycourts.gov/reporter/slipidx/aidxtable_1_2023_september.shtml | WF | OK; Mejia row: Index No. 806442/21, Appeal No. 653, Case No. 2022-03158, 2023_04822 |
| 79 | https://www.nycourts.gov/reporter/slipidx/cidxtable_2023_october.shtml | WF | OK; Nemeth v K-Tooling docket 48, 2023_05349 |
| 80 | https://www.nycourts.gov/reporter/motindex/mots_coa_09-2024.shtml | WF | OK; rows Title / Motion No. 2024-363 / 2024 NY Slip Op 74646 |
| 81 | https://www.nycourts.gov/reporter/3dseries/2023/2023_05349.htm | WF | [40 NY3d 405]; [*1]-[*5] plus {**40 NY3d at 407}; "As corrected through Wednesday, January 17, 2024"; complete |
| 82 | same | SH | 403 cf-mitigated: challenge |
| 83 | https://www.nycourts.gov/ctapps/Decisions/2023/Oct23/48opn23-Decision.pdf | WF | Nemeth slip; "On this appeal we must determine whether, under CPLR 203"; slip pagination only |
| 84 | https://www.nycourts.gov/ctapps/decisions.htm | WF | monthly pages 2025-2026 |
| 85 | https://www.nycourts.gov/ctapps/Decisions/2025/Oct25/October25.html | WF | 70opn25-Decision.pdf, 67opn25-Decision.pdf, DecisionList102325.pdf |
| 86 | https://iapps.courts.state.ny.us/lawReporting/Search | WF | ROBOTS_DISALLOWED |
| 87 | https://iapps.courts.state.ny.us/robots.txt | SH | 403 cf-mitigated: challenge |
| 88 | https://www.nycourts.gov/reporter/pdfs/2023/2023_34927.pdf | WF | People v Gibbs, Sup Ct Westchester, 2023 NY Slip Op 34927(U); slip page markers only; "not selected for official publication" |
| 89 | https://www.nycourts.gov/reporter/3dseries/2026/2026_00100.htm | WF | People v Rodriguez AD1; [245 AD3d 484]; "As corrected through Wednesday, March 11, 2026" |
| 90 | https://law.justia.com/cases/new-york/court-of-appeals/2023/ | WF | listing; /2023/94.html; disclaimer "may not be the official published versions" |
| 91 | https://law.justia.com/cases/new-york/appellate-division-first-department/2023/ | WF | "Opinions 1 - 500 of 1784"; slugs from docket identifiers |

Not retried (per instructions): govt.westlaw.com/nyofficial, which was SITE_BLOCKED on 2026-10-05.

Totals: about 50 WebFetch calls, 6 WebSearch calls, and about 40 shell requests.

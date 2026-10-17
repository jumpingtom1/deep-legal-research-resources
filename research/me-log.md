# Maine (me) probe log, 2026-10-17

All probes run on 2026-10-17 by `research`. Tools: WF = WebFetch; FD = `scripts/fetch_doc.py --research` (check/info/read/grep/links/verify); SH = curl, used only to read the JavaScript/HTML assets of the Revisor's single-page app on legislature.maine.gov (robots.txt allows the path); WS = WebSearch (discovery only). Quoted page text is 15 words or fewer per entry.

WebFetch: 20 calls. Built URLs hit permission prompts that timed out (gated) three times. One call failed with "You've hit your session limit" (quota, not a site refusal); WebFetch resumed after the coordinator reported the limit had reset.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://legislature.maine.gov/robots.txt | FD | 200; User-agent * Disallow /bills/default_ps.asp, /bills/search_ps.asp, /LawMakerWeb (+ /legis/ variants) |
| https://mainelegislature.org/robots.txt | FD | same file |
| https://www.courts.maine.gov/robots.txt | FD | 404 |
| https://courts.maine.gov/robots.txt | FD | 404 |
| https://lldc.mainelegislature.org/robots.txt | FD | 404 |
| https://www.maine.gov/sos/cec/rules/ | FD check | REFUSED: "www.maine.gov answers robots.txt with a bot check" |
| https://www.maine.gov/robots.txt | FD | REFUSED (host off for the day) |
| https://law.justia.com/codes/maine/ | FD check | REFUSED: robots.txt bot check |
| https://www.law.cornell.edu/states/maine | FD check | OK; crawl-delay 10 s |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| https://legislature.maine.gov/statutes/14/title14sec752.html | FD | 200, 2,212 chars; "All civil actions shall be commenced within 6 years after" |
| same | FD verify | VERIFIED "All civil actions shall be commenced within 6 years after the cause of action accrues" |
| https://legislature.maine.gov/statutes/5/title5sec4572.html | FD | 200; "§4572. Unlawful employment discrimination" |
| …/11/title11sec2-314.html; …/39-A/title39-Asec201.html; …/14/title14sec752-C.html; …/17-A/title17-Asec207.html | FD | all 200 with section headings |
| …/17-A/title17-Asec207.html | FD verify | VERIFIED "A person is guilty of assault if" |
| …/14/title14sec9999.html | FD | HTTP 404 |
| section page links | FD links | §752 PDF (.pdf), MS-Word (.docx), Ch. 205 Contents, Title 14 Contents |
| https://legislature.maine.gov/statutes/14/title14ch0sec0.html | FD | chapter list with ranges "Chapter 205: LIMITATION OF ACTIONS §751 - §871" |
| https://legislature.maine.gov/statutes/homepage.html | FD | "is current through October 1, 2026, and is subject to change without notice" |
| https://legislature.maine.gov/statutes/14/title14sec752.pdf | FD | 1 p.; "has not been officially certified by the Secretary of State" |
| https://legislature.maine.gov/statutes/14/title14ch0sec0.pdf | FD | 404; title PDF is /statutes/14/title14.pdf, chapter /title14ch205.pdf (from links) |
| https://legislature.maine.gov/statutes/14/title14sec752.html (built) | WF | permission prompt timed out (gated) |
| https://legislature.maine.gov/ros/maine-constitution-statutes-and-law/9574 | WF | link list (Constitution /const/, Statutes, Session Laws); disclaimer "at the user's own risk" |
| same | FD links | Maine Constitution → https://legislature.maine.gov/const/ |
| https://legislature.maine.gov/statutes/ | WF | "reflects changes made through the Second Regular Session of the 132nd Maine Legislature" |
| https://legislature.maine.gov/statutes/14/title14ch0sec0.html | WF | YES ranges; Ch. 205 "§751 - §871" |
| https://legislature.maine.gov/statutes/14/title14ch205sec0.html | WF | §752 body NOT PRESENT (links only) |
| https://legislature.maine.gov/statutes/14/title14sec752.html (from chapter page) | WF | YES "All civil actions shall be commenced within 6 years after"; "Data for this page extracted on 10/05/2026"; not truncated |
| https://law.justia.com/codes/maine/ | WF | latest "2025 Maine Revised Statutes" |
| https://law.justia.com/codes/maine/title-14/chapter-205/section-752/ | WF | YES; "2025 Maine Revised Statutes"; breadcrumb incl. Part 2, Subchapter 1 |
| https://law.justia.com/codes/maine/title-17-a/chapter-9/section-207/ | WF | YES "A person is guilty of assault if: A. The person"; canonical URL has /part-2/ |

### Session laws
| URL | Tool | Result |
|---|---|---|
| https://legislature.maine.gov/ros/LawsOfMaine/ | FD | 64 chars "Law Information Application Loading..." (JavaScript app) |
| same + App/main.js, App/viewmodels/shell.js, chapters.js, services/dataservice.js | SH | Durandal app; routes Law/Const/Info; data via breeze/Law/get* |
| …/ros/LawsOfMaine/breeze/Law/getSessions?LegislatureTerm=131 | FD | JSON R1, S1, R2 |
| …/breeze/Law/getLawTypes?LegislatureTerm=131&SessionId=R1 | FD | ACTPUB 1-20, ACTPS 1-1, RESLV 1-5 (partial) |
| …/breeze/Law/getLawGroup?…sessionId=R1&lawType=ACTPUB&startingChapter=1&endingChapter=1 | FD | JSON, ch. 1 "Winter Energy Relief Payment Program" |
| same with chapter 405; sessionId=1R | FD | [] |
| …/breeze/Law/getLegislatures | FD | JSON from 112th Legislature (1985) |
| WS "Laws of Maine 2023 Public Law chapter PDF" | WS | old LOM123rd .asp pages |
| https://legislature.maine.gov/ros/directory-session-laws-of-maine/12023 | FD links | LawsOfMaine app, PDF editions, individual files 1996-2010 |
| https://legislature.maine.gov/ros/pdf-editions-of-published-session-laws-and-other-materials/12024 | FD links | 124th-125th volume PDFs (/ros/LOM/LOM125th/125R1/LOM125R1Vol1.pdf …) |
| https://lldc.mainelegislature.org/Open/ ; /Open/Laws/ ; /Open/Laws/2023/ | FD links | directory listings; 2023 has 922 files, 2023_PL_c001 … c684 |
| https://lldc.mainelegislature.org/Open/Laws/2023/2023_PL_c405.pdf | FD | 27 pp., 174,408 chars; "CHAPTER 405" p. 3 |
| https://lldc.mainelegislature.org/Open/Laws/2023/2023_PL_c679.pdf | FD | 54 pp., 351,218 chars; "CHAPTER 679" |
| https://lldc.mainelegislature.org/Open/Laws/2025/2025_PL_c001.pdf | FD | 3 pp.; cover "LAWS OF THE STATE OF MAINE" |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| WS "Maine Constitution Article I Section 6-A legislature.maine.gov" | WS | lldc /Open/Const/Versions/ PDFs |
| https://lldc.mainelegislature.org/Open/Const/Versions/ | FD links | 1825 … MeConst_2013.pdf, MeConst_2024_Amd.pdf |
| https://lldc.mainelegislature.org/Open/Const/Versions/MeConst_2024_Amd.pdf | FD | 75 pp., scanned with OCR, "Codification of 2024 with Supplemental Amendments" |
| https://legislature.maine.gov/const/ | FD | redirects to ros/LawsOfMaine/#Const (JS shell) |
| https://legislature.maine.gov/ros/LawsOfMaine/App/views/constitution.html | FD | 177,724 chars; "(Includes CR 2023, c. 1 and CR 2023, c. 2)"; last-modified Feb 5, 2024 |
| same | FD links | "Download PDF file" → https://legislature.maine.gov/doc/10674 |
| https://legislature.maine.gov/doc/10674 | FD | PDF 50 pp., 134,452 chars; same heading |
| doc/10674 and constitution.html | FD verify | art. I § 6-A "No person shall be deprived of life, liberty or property without due process of law" VERIFIED; § 5 "The people shall be secure in their persons, houses, papers and possessions" VERIFIED |
| https://legislature.maine.gov/legis/ros/meconlaw.htm | FD | HTTP 503 |
| https://law.justia.com/constitution/maine | WF | index only, NOT PRESENT; "This Constitution may not be the most recent version." |
| same | WF | Article I → consar1.html; Article VI → consar6.html |
| https://law.justia.com/constitution/maine/consar1.html | WF | YES § 6-A "No person shall be deprived of life, liberty or property"; complete to § 24 |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.courts.maine.gov/rules/index.html | FD links | amendment orders (2026 Me. Rules 01-04 …) and rule-set PDFs under /rules/text/ |
| https://www.courts.maine.gov/rules/text/mr_civ_p_only_2026-06-01.pdf | FD | 286 pp., 639,810 chars; "Includes amendments effective June 1, 2026"; Rule 12(b) p. 46 |
| same | WF | permission prompt timed out (gated) |
| https://www.courts.maine.gov/rules/rules-civil.html | FD links | per-rule annotated PDFs /rules/text/MRCivPPlus/… |
| https://www.courts.maine.gov/rules/text/mru_crim_p_only_2026-10-01.pdf | FD | 128 pp., 275,427 chars; "Including amendments effective October 1, 2026"; Rule 11 p. 39 |
| https://www.courts.maine.gov/rules/text/mr_evid_only_2018-06-29.pdf | FD | 60 pp., 99,142 chars; "Includes amendment effective August 1, 2018"; Rule 401 p. 13 |
| https://www.courts.maine.gov/rules/text/mr_app_p_only_2024-11-01.pdf | FD | 68 pp., 139,884 chars; "Includes amendments effective November 1, 2024" |
| https://www.courts.maine.gov/rules/text/mr_prof_conduct_only_2023-09-28.pdf | FD | 67 pp., 145,567 chars; Rule 1.7 p. 22 |
| https://www.courts.maine.gov/rules/text/mr_evid_plus_2018-06-29.pdf | FD | 200 pp., 412,390 chars |

## D: Administrative code and register
| URL | Tool | Result |
|---|---|---|
| WS "Code of Maine Rules Secretary of State …" | WS | www.maine.gov/sos/rulemaking/agency-rules…; also www11.maine.gov and apps.web.maine.gov (alternate hostnames, not used) |
| http://www.maine.gov/sos/cec/rules/rules.html | WF | permission prompt timed out (gated) |
| https://www.maine.gov/sos/rulemaking/agency-rules | WF | "There was an error while fetching." |
| https://www.maine.gov/sos/rulemaking/agency-rules/department-administrative-financial-services-rules | WF | "There was an error while fetching." |
| https://www.law.cornell.edu/regulations/maine | FD links | departments 1 … 28 |
| …/regulations/maine/department-26 ; …/division-239 ; …/chapter-2 | FD links | chapters with section ranges; § 239-2-1 → /regulations/maine/26-239-C-M-R-ch-2-SS-1 |
| https://www.law.cornell.edu/regulations/maine/26-239-C-M-R-ch-2-SS-1 | FD | body "A. The State, after assessing all of the facts in the case"; "updated quarterly" |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| WS "Maine Supreme Judicial Court opinions 2024 ME" | WS | courts.maine.gov year pages; Justia year listing |
| https://courts.maine.gov/courts/sjc/lawcourt/2024/index.html | FD | rows "2024 ME 84 / State of Maine v. Ramel L. Sheppard / December 31, 2024"; Atlantic Reporter official statement |
| same | FD links | /lawcourt/2024/24me084.pdf … |
| same | WF | 2024 ME 84 → 24me084.pdf; official-version sentence quoted |
| https://courts.maine.gov/courts/sjc/lawcourt/2024/24me084.pdf | FD | 56 pp., 85,868 chars; "Decision: 2024 ME 84 Docket: And-23-68" |
| same | WF | YES "[¶1] Ramel L. Sheppard appeals from a judgment of conviction"; complete |
| https://courts.maine.gov/courts/sjc/opinions.html | FD links | 2026 opinions (26me102 … ; 26me075re.pdf, 26me075or.pdf); year pages 2017-2025; memdec.html |
| https://courts.maine.gov/courts/sjc/lawcourt/2017/index.html | FD links | 272 links; 17me239.pdf |
| https://courts.maine.gov/courts/sjc/lawcourt/2017/17me239.pdf | FD | 20 pp.; "Decision: 2017 ME 239 Docket: Cum-17-54" |
| …/lawcourt/2010/index.html; …/2006/index.html; …/2010/10me001.pdf; …/2006/06me001.pdf | FD | all HTTP 404 |
| https://law.justia.com/cases/maine/supreme-court/2024/ | WF | slugs 2024-me-82, -83, -84 |
| https://law.justia.com/cases/maine/supreme-court/2024/2024-me-84.html | WF | YES; [¶1]-[¶87]; complete |
| https://law.justia.com/cases/maine/supreme-court/2010/2010-me-1.html (built) | WF | "There was an error while fetching." |
| https://law.justia.com/cases/maine/supreme-court/ | WF | years 1838-2026 |
| https://law.justia.com/cases/maine/supreme-court/2010/ | WF | slugs 10me119da.html, 10me120da.html, 10me121wi.html |
| https://law.justia.com/cases/maine/supreme-court/2010/10me120da.html | WF | YES; 2010 ME 120, Cum-10-120; [¶1]-[¶8]; complete |
| https://lldc.mainelegislature.org/Open/SJC/ ; …/Maine%20Reports/ | FD links | 001ME.pdf … 161ME.pdf |
| https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/161ME.pdf | FD | 742 pp., 1,372,042 chars; "JANUARY 1, 1965 to DECEMBER 31, 1965"; PDF p. 40 head "28 STATE OF MAINE vs. VILES, SR. [161" |
| https://lldc.mainelegislature.org/Open/SJC/Maine%20Reports/150ME.pdf | FD | 554 pp.; PDF p. 30 head "18 BELFAST, IN EQ. VS. GOODWILL FARM" |
| https://www.courts.maine.gov/courts/bcd/index.html | FD links | Orders and Decisions → /courts/bcd/orders.html |
| https://www.courts.maine.gov/courts/bcd/orders.html | FD | "page is no longer being updated"; 559 links; newest rows seen 2016 |
| …/bcd/ap-orders/AP-09-06/AP-09-06%20Decision%20and%20Order%205.21.09.pdf | FD | 5 pp., 4 chars extracted (image scan) |

## F: Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://courts.maine.gov/courts/sjc/memdec.html | FD | 30,496 chars; "listed on this page for approximately 60-90 days"; row "Yor-26-37 Mem 26-139 … Affirmed" |
| same | FD links | no PDF links |

## G: Citation map
`python3 scripts/build.py --check`: no output, exit 0. `python3 scripts/build.py --cross`: 10 lines, all of them other states' patterns claiming Maine examples (Maine patterns claim nothing):
- nj / Pamphlet Laws claims 'P.L. 2023, ch. 405', 'P.L. 2021, ch. 647, § B-19', 'P. & S.L. 2023, ch. 5' (the bare P.L. form is context_required on the Maine side)
- mt / Montana Rules (Civ. P., Evid., App. P., Prof. Conduct) claim the Maine 'M.R. …' forms
- co / Colorado Rules of Criminal Procedure claims 'M.R.U. Crim. P. 11' and 'Me. R. Unified Crim. P. 16(a)'

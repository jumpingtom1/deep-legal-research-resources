# Vermont (vt) probe log, 2026-10-17

All probes were run on 2026-10-17 by `research`. Tools: WF = WebFetch; FD = `scripts/fetch_doc.py --research` (check/info/read/grep/links/verify); SH = curl, used only to read robots.txt files and form/script field names on pages whose robots.txt allows the path; WS = WebSearch (discovery only). Quoted page text is 15 words or fewer per entry. 16 WebFetch calls in total (one gated on its permission prompt). No CourtListener tool was used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://legislature.vermont.gov/statutes/section/12/023/00512 | FD check | OK; robots permits; crawl-delay 30.0s |
| https://legislature.vermont.gov/robots.txt | SH | `User-agent: *`, Crawl-delay 30; Disallow /bill/loadBillDetailedStatus/, /bill/loadBillRollCalls/, /bill/loadBillRollCallDetails/, /bill/loadBillsIntroduced/ |
| https://www.vermontjudiciary.org/opinions-decisions | FD check | OK; redirects to www.vtcourts.gov/opinions-decisions |
| https://www.vtcourts.gov/robots.txt | SH | Drupal default: Disallow /admin/, /search/, /user/*, /node/add/, /media/oembed …; /opinions-decisions, /media/{id}, /sites/default/files allowed |
| https://law.justia.com/codes/vermont/ | FD check | REFUSED: "law.justia.com answers robots.txt with a bot check (challenge)" |
| https://www.law.cornell.edu/states/vermont | FD check | OK; crawl-delay 10.0s |
| https://sos.vermont.gov/ ; https://secure.vermont.gov/SOS/rules/ ; https://outside.vermont.gov/ | FD check | OK (robots permits) |
| https://secure.vermont.gov/robots.txt | SH | `Disallow: /UAT/` only |
| https://www.lexisnexis.com/hottopics/vtstatutesconstctrules/ ; …/codeofvtrules/ | FD check | OK (robots permits) |
| https://advance.lexis.com/container?config=00JABlZjg3… | FD check | OK (robots permits) |
| https://www.public.law/ | FD grep "Vermont" | 0 matches |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| https://legislature.vermont.gov/statutes/section/12/023/00512 | FD info/grep/verify | 200 html, 7,100 chars; "(Cite as: 12 V.S.A. § 512)"; VERIFIED "Actions for the following causes shall be commenced within three years" @5117; banner "now include the actions of the 2026 session"; "unofficial copy of the Vermont Statutes Annotated" |
| https://legislature.vermont.gov/statutes/ | FD links | title links /statutes/title/01 … /03APPENDIX, /09A, /11A; "Developers" → /docs/api/v1/index.html; Lexis links for statutes/rules |
| https://legislature.vermont.gov/statutes/title/12 | FD links/grep | chapter links /statutes/chapter/12/NNN; rows show ranges "Contains: §§ 1 - 5", "§§ 61 - 65" |
| https://legislature.vermont.gov/statutes/chapter/09/063 | FD links | per-section links /section/09/063/02451, 02451a, 02453 … |
| https://legislature.vermont.gov/statutes/section/09/063/02453 | FD grep | 7,987 chars; "(a) Unfair methods of competition in commerce and unfair" |
| https://legislature.vermont.gov/statutes/section/13/053/02301 | FD grep | 6,798 chars; "Murder committed by means of poison, or by lying in wait" |
| https://legislature.vermont.gov/statutes/section/09/062/02453 (wrong chapter) | FD grep | 200, 6,161 chars, empty shell "(Cite as: V.S.A. )" |
| https://legislature.vermont.gov/statutes/fullchapter/12/023 | FD info/grep | 33,857 chars; § 512 and § 521 text present |
| https://legislature.vermont.gov/statutes/title/09A ; /chapter/09A/002 | FD links | "Article 002A : Leases"; § 2-101 → /section/09A/002/00101 |
| https://legislature.vermont.gov/statutes/section/09A/002/00101 | FD grep | "(Cite as: 9A V.S.A. § 2-101)" body present |
| https://legislature.vermont.gov/statutes/title/11A ; /chapter/11A/008 | FD links | § 8.30 → /section/11A/008/00008.30 |
| https://legislature.vermont.gov/statutes/section/11A/008/00008.30 | FD grep | "(a) A director shall discharge his or her duties as a director" |
| https://legislature.vermont.gov/statutes/section/09/063/02453 | WF | ERROR: permission request not answered in time (gated, built URL); not retried |
| WS "legislature.vermont.gov statutes section 12 V.S.A. 512" | WS | returned /statutes/section/12/027/01131, 12/025/00811 … |
| https://legislature.vermont.gov/statutes/section/12/027/01131 | WF | repealed §§ 1131-1132 note only; "unofficial copy" note; 2026-session banner; not truncated |
| https://legislature.vermont.gov/docs/api/v1/index.html | FD read | 885 chars; API key required ("contact the Vermont Legislature at IT@leg.state.vt.us") |
| https://legislature.vermont.gov/bill/acts/2026 | FD/SH | list loaded by script from bill/loadBillActs/2026/regular |
| https://legislature.vermont.gov/bill/loadBillActs/2026/regular | FD read | JSON 96,387 chars; ActNo, BillNumber, ActLink "Documents/2026/Docs/ACTS/ACT001/ACT001 As Enacted.pdf" |
| https://legislature.vermont.gov/Documents/2026/Docs/ACTS/ACT153/ACT153%20As%20Enacted.pdf | FD info/verify | PDF 33 pp., 49,898 chars; "No. 153. An act relating to miscellaneous amendments to laws relating to motor vehicles" |
| https://legislature.vermont.gov/Documents/2024/Docs/ACTS/ACT181/ACT181%20As%20Enacted.pdf | FD info | PDF 171 pp., 270,360 chars; "An act relating to community resilience and biodiversity" |
| WS "law.justia.com codes vermont title 12 chapter 23 section 512" | WS | /codes/vermont/title-12/ and year editions |
| https://law.justia.com/codes/vermont/title-12/ | WF | "2025 Vermont Statutes"; chapter links /title-12/chapter-1/ …; "Contains: §§ 461 - 595" for ch. 23 |
| https://law.justia.com/codes/vermont/title-12/chapter-23/ | WF | § 512 link /title-12/chapter-23/section-512/; subchapter not linked |
| https://law.justia.com/codes/vermont/title-12/chapter-23/section-512/ | WF | YES "Actions for the following causes shall be commenced within three"; "2025 Vermont Statutes"; "12 VT Stats § 512" |
| https://law.justia.com/codes/vermont/title-9/chapter-63/section-2453/ | WF | YES "(a) Unfair methods of competition in commerce and unfair or"; "2025 Vermont Statutes" |
| https://www.lexisnexis.com/hottopics/vtstatutesconstctrules/ | FD info | 302 → advance.lexis.com container; html, 0 chars |
| same | WF | redirect reported to advance.lexis.com |
| https://advance.lexis.com/container?config=00JABlZjg3NDE5OS1mMmJlLTQ3MWMtYjAxYy1lYjc3NmM1ZTljOGUKAFBvZENhdGFsb2cij1bfBuS6Ez3oYHkLGCJ1 | WF | "The page content provided is empty." |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| https://legislature.vermont.gov/statutes/constitution-of-the-state-of-vermont | FD info/grep/verify | 57,836 chars; heading "AMENDED THROUGH MARCH 31, 2021"; Article 22 "[Personal reproductive liberty]" @13650; ch. II "§ 28. [Courts of justice]" @28714; art. 11 VERIFIED @10279 |
| same | WF | art. 11 YES "That the people have a right to hold themselves, their"; § 76 YES; not truncated |
| https://law.justia.com/constitution/vermont/ | WF | art. 11 YES; Article 22 NOT PRESENT; "This Constitution may not be the most recent version."; § 20 cut mid-word |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.vtcourts.gov/attorneys/rules | FD links | full rules linked only to advance.lexis.com ("LexisNexis - Vermont Statutes, Court Rules and Administrative Code"); /attorneys/rules/proposed, /promulgated |
| https://www.vtcourts.gov/attorneys/rules/promulgated | FD links | PROMULGATED-VRCrP32.1--STAMPED.pdf, VRCP55(a), VRCP79(a), VRFP9(c), VRE615 … |
| https://www.vtcourts.gov/PROMULGATEDVRCP55aSTAMPED | FD info/read/verify | → /sites/default/files/documents/PROMULGATED-VRCP55%28a%29--STAMPED.pdf, 1 p., 3,233 chars; "OCTOBER TERM, 2026"; "Promulgation Order Amending Rule 55(a) of the Vermont Rules of Civil Procedure" |
| WS "Vermont Rules of Civil Procedure" full text Rule 12 (site: vtcourts.gov / justia / cornell) | WS | only non-permitted third parties (rulesofcivilprocedure.com, state-rules.com, courtrules.net); not fetched |

## D: Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://www.law.cornell.edu/states/vermont | FD links | statutes → legislature.vermont.gov; "Code of Vermont Rules (LII)"; "Code of Vermont Rules (state website)" → lexisnexis.com/hottopics/codeofvtrules/ |
| https://www.law.cornell.edu/regulations/vermont | FD links | agency-01 … agency-26 |
| https://www.law.cornell.edu/regulations/vermont/agency-13 ; …/subagency-140 ; …/chapter-001 | FD links | rule link /regulations/vermont/13-001-Code-Vt-R-13-140-001-X |
| https://www.law.cornell.edu/regulations/vermont/13-001-Code-Vt-R-13-140-001-X | FD info/grep/verify | 123,545 chars; "Permissible Exposure Limit" VERIFIED @17521; Notes "EFFECTIVE DATE: February 15, 1992 (Secretary of State Rule Log # 92-4)" |
| same | WF | YES "Section 1 General Provisions 1.1 Purpose These regulations, as authorized"; truncated at 100K before Notes |
| https://sos.vermont.gov/secretary-of-state-services/apa-rules/ | FD links | Notices of Rulemaking → secure.vermont.gov/SOS/rules/index.php; "Code of Vermont Rules" → lexisnexis; CVR 04-000-001 → advance.lexis.com; Rule on Rulemaking PDF on outside.vermont.gov |
| https://secure.vermont.gov/SOS/rules/ ; index.php | FD info/read | 11,366 chars; "Proposed Rules Postings"; "29 Rules Found"; 26P032 "Home Health Services." Oct 07, 2026 |
| https://secure.vermont.gov/SOS/rules/rssFeed.php | FD info / SH | RSS 2.0, 27,624 chars; items "Rule:26P001" |
| https://secure.vermont.gov/SOS/rules/search.php | FD links | 14 links; form page |
| https://www.lexisnexis.com/hottopics/codeofvtrules/ | FD check | robots OK; not fetched separately (same Lexis container type as above) |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| https://www.vtcourts.gov/opinions-decisions | FD links / SH | facets court_division_opinions_library_ 1 Civil, 2 Criminal, 3 Environmental, 4 Family, 6 Probate, 7 Supreme; document_type 92/93/94/96; GET fields search_api_fulltext, facet_from_date, facet_to_date |
| …/opinions-decisions?f%5B0%5D=court_division_opinions_library_%3A7 | FD read | Supreme rows: "State v. Edward Skinner 10/09/2026 Supreme Court 25-AP-364" … |
| …?search_api_fulltext=25-AP-345&f%5B0%5D=court_division_opinions_library_%3A7 | FD links | 1 row → /media/20708 |
| same | WF | 1 result: Ford v. Polomsky, 10/02/2026, 25-AP-345, /media/20708 |
| https://www.vtcourts.gov/media/20708 → /sites/default/files/documents/op25-345.pdf | FD info/read/verify | PDF 19 pp., 44,329 chars; "2026 VT 44"; "No. 25-AP-345"; VERIFIED "Plaintiff appeals a civil division order dismissing his claim" @1363; notice "subject to motions for reargument under V.R.A.P. 40" |
| https://www.vtcourts.gov/sites/default/files/documents/op25-345.pdf | WF | YES; "2026 VT 44"; ¶ 1 "WAPLES, J. Plaintiff appeals a civil division order dismissing his"; complete to ¶ 38 |
| https://www.vtcourts.gov/media/20681 | FD info | → eo26-329.bail_.pdf, 3 pp. |
| …?search_api_fulltext=25-AP-364 → /media/20731 | FD links/read | eo25-364.pdf, 4 pp.; "ENTRY ORDER"; "Decisions of a three-justice panel are not to be considered as precedent" |
| /media/20706 | FD info | op25-448.pdf, 18 pp. |
| …Supreme + document_type 94 | FD links | /media/20709, 20708, 20707, 20706 … |
| date ranges 1990-2003, 2004-2008, 2010 with document_type 94 | FD links | 0 rows (Opinion type tag absent on older items) |
| Supreme facet, year 1998 / 2001 | FD links | 0 rows |
| year 2003 / 2005 | FD links | 1 / 4 rows (In re Blais; In re Dempsey) |
| years 2006-2019 | FD links | full first page (25 rows) each |
| 2008 row → eo2008-164.pdf | FD read | "Solsaa v. Solsaa" "2008 VT 138" |
| 2015-2016 opinions → op15-376_3.pdf | FD read/grep | "2016 VT 102"; cites "In re All Metals Recycling Inc., 2014 VT 101, ¶ 6, 197 Vt. 481, 107 A.3d 895" |
| ?search_api_fulltext=2015-376 | FD links | 1 row → /media/10311 |
| ?search_api_fulltext=%222026%20VT%2044%22 | FD links | 25+ rows (not a unique match) |
| ?search_api_fulltext=Polomsky | FD links | /media/20708 (Supreme) and /media/19500 ("ford v polomsky") |
| /media/20757 (Civil facet row) | FD read | "northfield savings v bell shafritz 26-cv-4158 10-9-26.pdf", 13 pp.; OCR "7ermont Superior Court"; "Case No. 26-CV-04158" |
| WS "law.justia.com cases vermont supreme-court 2025 VT" | WS | /cases/vermont/supreme-court/2023/ and vtcourts /media links |
| https://law.justia.com/cases/vermont/supreme-court/2023/ | WF | rows 22-ap-324.html, 23-ap-177.html, 23-ap-003.html, 23-ap-062.html |
| https://law.justia.com/cases/vermont/supreme-court/2023/23-ap-003.html | WF | YES full opinion; "2023 VT 64"; PDF cases.justia.com/vermont/supreme-court/2023-23-ap-003.pdf |
| https://law.justia.com/cases/vermont/supreme-court/ | WF | years 1950-2026; /supreme-court/YEAR/ |

## F: Subsequent history
| URL | Tool | Result |
|---|---|---|
| ?search_api_fulltext=Polomsky | FD links | trial entry /media/19500 and appeal /media/20708 |
| /media/19500 | FD read | "ford v polomsky battles 25-cv-1449 9-24-25.pdf"; "Lamoille Unit … Case No. 25-CV-01449"; "ENTRY REGARDING MOTIONS" |
| ?search_api_fulltext=25-CV-01449 | FD links | 0 rows |
| ?search_api_fulltext=22-CR-12116 (trial docket in eo25-364) | FD links | 0 rows |
| op25-345.pdf caption | FD read | "On Appeal from Superior Court, Lamoille Unit, Civil Division"; "Benjamin Battles, J." |

## Notes
- WebFetch quota was not hit. The one gated call (built statute URL) was not retried; the row was verified with FD and with a search-sourced WebFetch.
- `build.py --check`: no ERROR/WARN lines. `build.py --cross`: 0 matches.

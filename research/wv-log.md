# West Virginia (wv) probe log — 2026-10-17

Tools: WF = WebFetch; FD = `python3 scripts/fetch_doc.py --research` (info/read/grep/links/check); WS = WebSearch (discovery only). All entries dated 2026-10-17. About 17 WebFetch calls were made; the 17th hit the WebFetch proxy's HTTP 429 rate limit, after which WebFetch was stopped (per brief) and the remaining rows were verified by FD only. Field names of courtswv.gov filter forms were read from FD's cached HTML of pages already fetched.

## A. Statutes

| URL | Tool | Result |
|---|---|---|
| https://code.wvlegislature.gov/55-7-8a/ | FD info/grep | 200 html 13,029 chars; heading "§55-7-8a. Actions which survive; limitations" at offset 6714; body "(a) In addition to the causes of action which survive" |
| https://code.wvlegislature.gov/61-2-1/ | FD | 200 html 11,681 chars; body "Murder by poison, lying in wait, imprisonment, starving" |
| https://code.wvlegislature.gov/robots.txt | FD check / read | check: "robots.txt permits"; read: Connection reset by peer (after retry) |
| https://code.wvlegislature.gov/55-7/ | FD links/grep | article TOC: section links (/55-7-8A/ upper-case), headings only, 13,738 chars |
| https://code.wvlegislature.gov/ | FD links | chapter 1 article links; /pdf/1/ chapter PDF link; footer "updated regularly as new legislation takes effect" |
| https://code.wvlegislature.gov/pdf/55/ | FD info/read | application/pdf 436 pp, 656,691 chars; footer "October 17, 2026 Page 1 of 436"; "§55-1-1. When writing required." |
| https://code.wvlegislature.gov/55-7-8a/ | WF | YES; "(a) In addition to the causes of action which survive"; "Copyright © 2026 West Virginia Code"; not truncated |
| https://law.justia.com/codes/west-virginia/chapter-61/article-2/section-61-2-1/ | WF | YES; "Murder by poison, lying in wait, imprisonment, starving, or by"; "2025 West Virginia Code"; "WV Code § 61-2-1 (2025)" |
| same | FD info | REFUSED: law.justia.com refused automated access earlier (robots.txt challenge) |
| https://www.wvlegislature.gov/robots.txt | FD read | 462 chars; "User-agent: *" … "Disallow: /WVCODE/" (also /apps/, /media/, /js/ …) |
| https://www.wvlegislature.gov/WVCODE/WV_CON.cfm | FD info | REFUSED: robots.txt disallows /WVCODE/WV_CON.cfm (rule: Disallow: /WVCODE/) |
| https://www.wvlegislature.gov/ | FD links | links: WEST VIRGINIA CODE → code.wvlegislature.gov; ACTS → /Educational/publications.cfm#acts; WV CONSTITUTION → home.wvlegislature.gov/constitution-of-west-virginia/; Legacy WV Code → /wvcodeentire.htm |
| https://www.wvlegislature.gov/wvcodeentire.htm | FD links | 33,907 links; section links to code.wvlegislature.gov/1-1-4/ … |
| https://www.wvlegislature.gov/Educational/publications.cfm | FD links | Acts PDFs /legisdocs/publications/acts/Acts_2025_Vol_1.pdf … Acts_1863.pdf |
| https://www.wvlegislature.gov/legisdocs/publications/acts/Acts_2023.pdf | FD info | HTTP 404 (recent years split into volumes) |
| https://www.wvlegislature.gov/legisdocs/publications/acts/Acts_2025_Vol_1.pdf | FD info/grep | pdf 1,088 pp, 2,009,624 chars, Last-Modified 14 Mar 2026; p. 37 "2025 CHAPTER 1 (H. B. 3272" |
| https://www.public.law/ | FD grep "West Virginia" | 0 matches |
| https://www.law.cornell.edu/states/west_virginia | FD links | links out to courtswv.gov, apps.sos.wv.gov; LII hosts /regulations/west-virginia only |

## B. Constitution

| URL | Tool | Result |
|---|---|---|
| WS "West Virginia Constitution article III section 10 site:wvlegislature.gov" | WS | returned code.wvlegislature.gov/west-virginia-constitution |
| https://code.wvlegislature.gov/west-virginia-constitution | FD info/grep | 277,437 chars; "As Ratified in 1872 and Subsequently Amended"; Art. III §10 at 11,755; Art. VIII §1 at 106,557 |
| same | WF | Art. III §10 YES "No person shall be deprived of life, liberty, or property,"; Art. VIII NOT PRESENT; truncated in Art. VII §14; page 134,777 chars |
| https://home.wvlegislature.gov/constitution-of-west-virginia/ | FD info/grep | 211,905 chars; "ARTICLE VIII 8-1. Judicial power. The judicial power of the state" at 84,625 |
| https://law.justia.com/constitution/west-virginia/ | WF | §3-10 YES; single page; truncated in Art. VIII (8-13); 136,848 chars; no currency |

## C. Court rules

| URL | Tool | Result |
|---|---|---|
| https://www.courtswv.gov/robots.txt | FD read | Drupal default: Disallow /admin/, /search/, /search?, /user/*, /node/add/ … |
| https://www.courtswv.gov/legal-community/court-rules | FD links | rule-set pages (civil, criminal, evidence, appellate, trial court, RPC, family, magistrate, habeas, abuse/neglect, juvenile …); "Former West Virginia Rules of Civil Procedure" PDF |
| …/court-rules/rules-civil-procedure-contents | FD info/grep | 268,988 chars; Rule 12 body at 54,061; "Rule 56. Summary judgment. (a)" at 221,933; no currency line |
| same | WF (built URL) | PROVENANCE_REQUIRED (not answered) |
| WS "courtswv.gov West Virginia Rules of Civil Procedure contents Rule 12" | WS | returned the same URL |
| same | WF (search-sourced) | Rule 12(b) YES "Every defense to a claim for relief in any pleading"; 56(a) NOT PRESENT; truncated in Rule 23(f)(2); 127,744 chars |
| …/court-rules/rules-evidence-contents | FD | 101,132 chars; "Rule 702. Testimony by Expert Witnesses (a) If scientific" at 59,165 |
| …/court-rules/rules-appellate-procedure | FD | 180,778 chars; Rule 21 at 102,673; 21(e) "Memorandum decisions may be cited in any court" |
| …/court-rules/rules-criminal-procedure-contents | FD | 148,932 chars; "Rule 35. Correction or reduction of sentence" at 110,712 |
| …/court-rules/wv-trial-court-rules-contents | FD | 220,561 chars; "Rule 24.01. Generally" at 142,091 |
| …/court-rules/west-virginia-rules-professional-conduct | FD | 385,913 chars; "Rule 1.7 Conflict of Interest; Current Clients (a)" at 82,093 |

## D. Administrative code and register

| URL | Tool | Result |
|---|---|---|
| https://apps.sos.wv.gov/robots.txt | FD read | Disallow /adlaw/executivejournal/senateconfirmation/, /email/, /Templates/, business readpdf paths |
| https://apps.sos.wv.gov/adlaw/csr/rule.aspx?rule=110-15 | FD | versions table; Active 7/15/1993 "Consumer Sales And Service Tax And Use Tax" |
| https://apps.sos.wv.gov/adlaw/csr/ruleview.aspx?document=7820 | FD links | readfile.aspx?DocId=20946&Format=PDF / WORD / WP |
| https://apps.sos.wv.gov/adlaw/csr/readfile.aspx?DocId=20946&Format=PDF | FD info | pdf 249 pp, 248 chars (image scan) |
| …/csr/rule.aspx?rule=110-01H, 110-1H, 64-21, 78-03 | FD | 110-01H Active 4/28/2026; 110-1H empty; 64-21 Active 6/23/1997; 78-03 Active 6/28/2023 |
| …/csr/ruleview.aspx?document=18270 | FD | "Date Effective: 4/28/2026 Final File PDF"; DocId=58902 |
| …/csr/readfile.aspx?DocId=58902&Format=PDF | FD | pdf 11 pp, 32,214 chars; "NOTICE OF FINAL FILING AND ADOPTION OF A LEGISLATIVE RULE" |
| https://apps.sos.wv.gov/adlaw/csr/rule.aspx?rule=110-01H | WF (built) | PROVENANCE_REQUIRED |
| https://www.law.cornell.edu/regulations/west-virginia (+ /agency-110, /title-110, /series-110-01H) | FD links | index → W-Va-C-S-R-SS-110-1H-1 section links |
| https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-110-1H-1 | FD grep | 2,741 chars, LM 08 Aug 2025; "1.4. Effective Date. -- May 1, 1999"; "updated quarterly" |
| …/W-Va-C-S-R-SS-110-15-1 | FD grep | "1.1. Scope. -- These legislative regulations explain and clarify" |
| same (110-1H-1) | WF | PROXY_REJECTED HTTP 429 (WebFetch rate limit) — WebFetch stopped here |
| https://apps.sos.wv.gov/adlaw/register/ | FD info | HTTP 403 (wrong path); address refused for the day |
| WS "West Virginia State Register apps.sos.wv.gov adlaw register" | WS | real path /adlaw/registers |
| https://apps.sos.wv.gov/adlaw/registers | FD | 200, 5,345 chars; years 2003-2026; "Friday, August 21, 2026 XLIII (43) 33 View" |
| https://apps.sos.wv.gov/adlaw/registers/readpdf.aspx?did=40275 | FD info | pdf 74 pp, 73 chars (image-only) |

## E. Case law

| URL | Tool | Result |
|---|---|---|
| https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions | FD | current-term listing; "10/14/2026 25-835 In re M.M. JUV MD"; links pubfilesmnt/2026-10/25-858 Memorandum Decision.pdf |
| …/supreme-court-of-appeals/opinions/prior-terms | FD + cached HTML | GET form: combine, field_sca_opinion_year_value (1991-2026), _term_, field_case_type_sca_value, field_decision_type_sca_value; 1,797 pages |
| …/prior-terms?field_sca_opinion_year_value=2019&combine=AFL-CIO&… | FD links | 0 PDF links |
| …/prior-terms?combine=Morrison | FD | "Total Opinions: 7"; PDFs in pubfilesmnt/2023-11 and 2023-12 |
| …/prior-terms?field_sca_opinion_year_value=2024&field_case_type_sca_value=CIV-O | FD | rows incl. 22-765 SO → 2024-11/22-765-bunn-p.pdf |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2024-11/22-765-bunn-p.pdf | FD | pdf 46 pp, 82,086 chars; "September 2024 Term … No. 22-765"; no reporter cite |
| same | WF (page-link URL) | PROVENANCE_REQUIRED |
| WS "courtswv.gov supreme court of appeals opinions archived prior terms" | WS | prior-terms?page=1387 etc. |
| …/prior-terms?page=1387 | WF | rows "02/17/2006 32875 SER Games-Neely v. Sanders … SO"; filter form present |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2023-11/32783.pdf | WF | PROVENANCE_REQUIRED |
| …/intermediate-court-of-appeals/opinions | FD links | 25-ICA-369_MD.pdf etc. |
| …/intermediate-court-of-appeals/opinions/prior-terms | FD | 633,023 chars; "Total Opinions: 1398"; years 2022-2026 |
| …/prior-terms?combine=Battista | FD links | 2 rows (25-ICA-404_MemoD.pdf, 23-ICA-40.pdf) |
| …/prior-terms?field_sca_opinion_year_value=2023&field_decision_type_sca_value=SO | FD | 1,398 links (SCA field names ignored) |
| …/prior-terms?field_ica_opinion_year_value=2023&field_decision_type_value=SO | FD | 30 links incl. 2023-12/22-ICA-208 Opinion.pdf |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2023-12/22-ICA-208%20Opinion.pdf | FD | pdf 29 pp, 49,514 chars; "REVERSED AND REMANDED … Filed: December 8, 2023" |
| https://law.justia.com/cases/west-virginia/supreme-court/2024/22-765.html | WF | Armstead separate opinion only ("Although I concur with much of the majority's decision in") |
| https://law.justia.com/cases/west-virginia/intermediate-court-of-appeals/2023/22-ica-208.html | WF | CLIENT_ERROR (fetch error) |
| https://law.justia.com/cases/west-virginia/ | WF | two courts: supreme-court, intermediate-court-of-appeals |
| https://law.justia.com/cases/west-virginia/intermediate-court-of-appeals/2023/ | WF | 22-ICA-208 listed but unlinked; pattern …/2023/22-ica-243.html; "-0" suffixes |
| https://law.justia.com/cases/west-virginia/intermediate-court-of-appeals/2023/22-ica-243.html | WF | YES "SCARR, Judge: Petitioner, Mr. Jay Folse, appeals the October 13,"; complete |
| https://law.justia.com/cases/west-virginia/supreme-court/2024/ | WF | 22-765-0.html = Signed Opinion; 22-765.html = Separate |

## F. Subsequent history

| URL | Tool | Result |
|---|---|---|
| SCA prior-terms?combine=Ford%20Motor / combine=ICA | FD links | 10 rows each; combine=ICA returns ICA-appeal memorandum decisions |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2026-06/25-884%20Memorandum%20Decision.pdf | FD grep | 2 pp; "No. 25-884 (JCN: 2019025668) (ICA No. 25-ICA-78)" |
| SCA prior-terms?combine=25-ICA-78 | FD | "No Entries Found." |
| SCA prior-terms?combine=Gasvoda | FD | 25-884 MD (2026-06), 23-143 md (2024-08) |
| ICA prior-terms?combine=Gasvoda | FD | 25-ICA-78_MD.pdf (2025-10), 22-ICA-108md.pdf |
| https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/order-lists | FD links | 10 PDFs, e.g. OrderListJune262025.pdf |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2025-06/OrderListJune262025.pdf | FD | 3 pp, 4,496 chars; "No. 24-120 (Ohio CC-35-2022-C-26) Affirmed (5-0)" |
| WS "courtswv.gov pubfilesmnt opinion pdf …" | WS | order-list PDFs incl. 2024-11/2024-11-4 Order and Decision List.pdf |
| https://www.courtswv.gov/sites/default/pubfilesmnt/2024-11/2024-11-4%20Order%20and%20Decision%20List.pdf | WF | ICA list, Nov. 4, 2024; first entry 23-ICA-351 "Reversed and Remanded" (3-0) |

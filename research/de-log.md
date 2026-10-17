# Delaware (de) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "shell" = curl from this workspace via agent proxy; "WF" = WebFetch.

## Robots / host checks (shell)
| URL | Result |
|---|---|
| https://delcode.delaware.gov/robots.txt | 404 (IIS "File or directory not found") |
| https://courts.delaware.gov/robots.txt | 200; `User-agent: *`; Disallow ~10 specific `/opinions/download.aspx?ID=` ids (144670, 135640, 80280, 160340, 213920, 71240, 206330, 203680, 237150), `/Superior/pdf/admin_order_2015_1.pdf`, `/_declt`. First attempt: connection reset; retry OK |
| https://regulations.delaware.gov/robots.txt | 200 but returns SPA HTML ("Delaware Regulations"), no robots file |
| https://www.law.cornell.edu/robots.txt | 200; Crawl-delay: 10; disallows /search/, /user/, admin paths |
| https://law.justia.com/robots.txt | 403, `cf-mitigated: challenge`, server cloudflare |
| https://law.justia.com/codes/delaware/ | shell 403 cf challenge |
| https://legis.delaware.gov/robots.txt | 302 → /404 page |
| https://delaware.public.law/ , https://law.public.law/delaware | proxy CONNECT 502 |
| https://www.public.law/ | 200; lists CA, CO, FL, NV, NY, OR, TX only |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://delcode.delaware.gov/index.html | shell | 200; notice: "considered an official version of the State of Delaware statutory code"; "includes all acts enacted as of September 10, 2026" … "85 Del. Laws, c. 518"; UELMA authenticated PDFs |
| …/title6/c018/index.html | shell | 200, navigation only: links sc01..sc12, no section ids |
| …/title6/c018/sc01/index.html | WF | YES § 18-101 "As used in this chapter unless the context otherwise requires"; § 18-111 present; complete to § 18-113; no currency |
| …/title5/c009/index.html | shell | 200 nav only |
| …/title5/c009/sc02/index.html | WF | YES § 952 "Unless the agreement governing a revolving credit plan otherwise provides"; complete §§ 941–956 |
| …/title8/c001/index.html | shell | sc01..sc18 links (Arabic two-digit) |
| …/title8/c001/sc04/index.html | WF | YES § 141 "The business and affairs of every corporation organized under this"; § 145 present; ends § 147, not truncated |
| …/title10/index.html | shell | chapter links c001…c081…c089 (3-digit padding) |
| …/title10/c081/index.html | shell+WF | no sc links; 46 Section divs; WF YES § 8106 "(a) No action to recover damages for trespass"; ends § 8146 |
| …/title6/index.html | shell | slugs incl. c002a, c004a, c000a, c012_1, c012a–d, c013a |
| …/title11/c005/sc02/index.html | shell | 254 KB; ids 601…792 |
| same | WF | § 601 YES; § 791 NOT PRESENT; "[Content truncated due to length...]" after § 776(c) |
| same, offset=100000 | WF | § 791 NOT PRESENT; last visible § 778 |
| …/title8/title8.pdf | shell | 200 application/pdf 1.0 MB |
| https://law.justia.com/codes/delaware/ | WF | editions 2025…2006; no currency statement |
| WebSearch "law.justia.com codes delaware title 8 chapter 1 section 141" | search | found title-8/chapter-1 URL forms |
| https://law.justia.com/codes/delaware/title-8/chapter-1/subchapter-iv/section-141/ | WF | YES "(a) The business and affairs of every corporation organized under"; "2025 Delaware Code"; "These codes may not be the most recent version." |
| …/title-6/chapter-18/subchapter-i/section-18-101/ | WF | YES; "6 DE Code § 18-101 (2025)" |
| …/title-10/chapter-81/section-8106/ | WF | YES (no subchapter segment) |
| …/title-11/chapter-5/subchapter-ii/section-791/ | WF | YES "A person is guilty of coercion when the person compels" |
| https://legis.delaware.gov/SessionLaws , …/Chapter?id=22385 | shell 200; WF | Chapter 141 (S.B. 105, 134th G.A.); body "AN ACT TO AMEND CHAPTER 27, TITLE 11 OF THE"; "Approved July 9, 1987"; volume link Chapters?volume=42 |
| https://www.law.cornell.edu/states/delaware | shell+WF | links out only; LII hosts only Admin Code |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://delcode.delaware.gov/constitution/index.html | WF | TOC only, body NOT PRESENT; "through July 1, 2025." |
| …/constitution/constitution-02.shtml | WF | Art. I; § 1 "Although it is the duty of all persons frequently to"; § 9 present; no currency |
| …/constitution-05.shtml | shell | 301 → constitution-05.html, 200 |
| …/constitution/constitution.pdf | shell | 200 application/pdf |
| https://law.justia.com/constitution/delaware/ | WF | single page, #art01 anchors; § 1 reads "all men" (stale); Art. XII "NOT CURRENTLY AVAILABLE"; 134K chars |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://courts.delaware.gov/rules/ | WF | list of rule sets with download.aspx?id= links and currency strings (ids below) |
| forms/download.aspx?id=174928 (Supreme) | shell | application/pdf "sc rules_as amended through 2-2-26.pdf", 67 pp |
| same | WF | Rule 14(g) YES "The following shall be the form of citations: (i) Reported"; Rule 42 NOT PRESENT; truncated in Rule 26(j) |
| id=160908 (Chancery) | shell | "full set of chancery rules (6.1.2026).pdf", 231 pp |
| same | WF | Rule 23.1 YES "(a) Pleading Requirements. The complaint in a derivative action must:"; Rule 174 NOT PRESENT; truncated |
| same, offset=100000 | WF | Rule 174 NOT PRESENT; window covers Rules 23.2–26 |
| id=304488 (Super. Civ.) | shell | "del_super_ct_civ_02052026.pdf", 117 pp |
| same | WF | Rule 12(b) YES "Every defense, in law or fact, to a claim for"; 56(c) NOT PRESENT; truncated at 16.1 |
| id=39388 (D.R.E.) | shell | "drewithmay2018amend.pdf", 75 pp |
| same | WF | Rule 401 YES "Evidence is relevant if: (a) it has any tendency to"; 702 NOT PRESENT; truncated at 614 |
| id=160568 (DLRPC) | shell | "lawyers' rules of professional conduct_as amended through 11-18-25.pdf", 390 pp; WF not run |
| Other ids from index (not fetched) | — | Super. Crim. 304498; Special Proc. 133058; Family Civil 39308, Criminal 39318; CCP Civil 176248, Criminal 174058; JP Civil 39328, Civ. Violations 81598, Criminal 39338; Disciplinary 160798; CLE 160618; Ct. on Judiciary 160518; Rapid Arbitration 160508; Judicial Conduct 39408; Supreme IOPs 117538 |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://regulations.delaware.gov/AdminCode/ (+ /title14/index.html, /register/) | shell | 200 text/html, identical 65,668-byte Angular shell |
| https://regulations.delaware.gov/main.e86913c3cd7c00bf.js | shell | bundle: endpoints AdminCode/titles, POST AdminCode/title, POST AdminCode/regulation, file/download/{id}, register/monthlyRegister |
| https://regulations.delaware.gov/config.json | shell | rpsApiDomain "https://regulations.delaware.gov/api/" |
| …/api/AdminCode/titles | shell | 200 JSON list of titles |
| POST …/api/AdminCode/title {"/AdminCode/title14"} | shell | 200 JSON, 248 regulation urls (/AdminCode/title14/101 …) |
| POST …/api/AdminCode/regulation {"/AdminCode/title14/101"} | shell | 200 JSON keys titleId, titleName, regulationName, pdfId, titleUrl, htmlBody |
| GET …/api/AdminCode/regulationNumber/14/101 and /692/101 | shell | 200 empty body |
| …/api/file/download/d3e6e76e-8b82-4f26-b6eb-a74d0b57c6fe | shell | application/pdf 9 pp "TITLE 14 EDUCATION DELAWARE ADMINISTRATIVE CODE" |
| same | WF | 1.1 YES "The purpose of this regulation is to outline the procedures,"; not truncated; no currency |
| https://regulations.delaware.gov/AdminCode/title14/101 | WF | NOT PRESENT (SPA head only) |
| …/api/register/monthlyRegister | shell | 200 JSON 107 KB, 30 volumes, latest "2026 October - Volume 30 Issue 4" |
| same | WF | JSON truncated, reached only Vol. 19 |
| …/api/register/regs-rss.xml | shell | 200 application/xml |
| …/api/file/download/458675cb-fefa-4292-b134-6487303cda9d | WF | "DELAWARE REGISTER OF REGULATIONS, VOL. 30, ISSUE 4, THURSDAY, OCTOBER 1, 2026"; truncated ~p. 209/239 |
| https://www.law.cornell.edu/regulations/delaware | WF | Admin Code index, 20 titles listed; no currency |
| …/regulations/delaware/title-14 | WF | parts 100, 200, 400…; "State regulations are updated quarterly; we currently have two versions available." |
| …/regulations/delaware/14-Del-Admin-Code-SS-101 | WF | top-level index, not 404, no text |
| …/regulations/delaware/title-14/100 | WF + shell | links /title-14/100/101 …; shell gives /14-Del-Admin-Code-SS-101-1.0 section links |
| …/regulations/delaware/14-Del-Admin-Code-SS-101-1.0 | WF | 1.1 YES; Notes "28 DE Reg. 220 (9/1/2024) (Final)" |

## E/F — Case law and subsequent history
| URL | Tool | Result |
|---|---|---|
| https://courts.delaware.gov/opinions/ , /index.aspx | shell | 200; ASP.NET form POST ./index.aspx; fields ctlOpinions1selAgencies/selperiods/selyears/txtsearchtext/selresults/hdnpageno; 25 rows |
| /opinions/index.aspx?ag=Supreme%20Court (and ?ag=…&searchtext=…) | shell | parameters ignored; same mixed-court listing |
| /opinions/index.aspx | WF | 25 newest rows with download.aspx?id= links; no coverage statement |
| POST search years (shell) | shell | Supreme: 1998 18 rows, 1999 2, 2000 445, 2025 506; Chancery: 1998 0, 1999 0, 2000 107, 2001 74, 2025 337; Superior: 2000 1 page, 2001 478, 2003 490, 2005 519; CCP: 2001 3, 2005 85; Family: 2005 0, 2008 0, 2012 1, 2015 3, 2025 45. Year options list 1983–2026; 1995/1997 requests returned current-year rows |
| POST Supreme 2026 "Moelis" | shell | 1 row id 390230, "340, 2024", "(Court of Chancery)", Traynor J., Opinion |
| POST All Courts 2026 "2023-0309" | shell | 0 rows (lower-court C.A. No. not searchable on appeal) |
| POST Supreme 2026 "340, 2024" | shell | fuzzy results (many dockets); "340" → 2 rows incl. 390230 |
| POST Chancery 2024 "Moelis" | shell | ids 360460 (02/23/2024) and 360010 (02/12/2024), C.A. No. 2023-0309-JTL |
| POST Chancery 2026 "2026-0508-JTL" | shell | 1 row id 402240 |
| /opinions/download.aspx?id=390230 | shell | application/pdf "340, 2024 final opinion.pdf", 45 pp; caption "IN THE SUPREME COURT OF THE STATE OF DELAWARE" |
| same | WF | body "TRAYNOR, Justice: In the Court of Chancery, a stockholder sought a declaratory judgment"; no A.3d cite; slip pagination; complete to fn. 111; "REVERSED" |
| /opinions/download.aspx?ID=390230 (upper-case) | shell | 200 |
| /opinions/download.aspx?id=402240 | shell | first try connection reset; retry 200 application/pdf "aprio memo op final.pdf", 30 pp; "LASTER, V.C." |
| /opinions/download.aspx?id=40140 | shell | 200 PDF 1 p, Supreme No. 563, 2000 order |
| https://law.justia.com/cases/delaware/ | WF | courts: supreme-court, court-of-chancery, superior-court, court-of-common-pleas, court-on-the-judiciary, court-of-errors-and-appeals; "The only appellate court in Delaware is the Delaware Supreme Court" |
| …/cases/delaware/supreme-court/ | WF | years 1793–2026, /supreme-court/{year}/ |
| …/cases/delaware/supreme-court/2026/ | WF | Moelis at /2026/340-2024.html |
| …/supreme-court/2026/340-2024.html | WF | body present, complete; AI-metadata disclaimer; PDF on cases.justia.com |
| …/cases/delaware/court-of-chancery/ | WF | years 1950–2026; slugs "2024-1085-ccb.html" and "c-a-no-2025-0475-paf.html" |
| …/court-of-chancery/2024/c-a-no-2023-0309-jtl.html | WF | West Palm Beach v. Moelis, decided Feb. 12, 2024; body "Section 141(a) of the Delaware General Corporation Law" |
| https://courts.delaware.gov/rss/opinions.aspx | shell | 200 text/html (not a feed; not pursued) |

## Notes
- WebFetch calls used: ~37. No CourtListener tools used.
- Supreme Court Rule 14(g) (from the shell pdftotext of id=174928) gives Delaware's citation forms; recorded in citation_map.notes.

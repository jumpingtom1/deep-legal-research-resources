# Florida (fl) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt reads only (no content fetched around any refusal). WebFetch calls used: 33 (of ~55). WebSearch: 5.

## Robots / host checks (curl of robots.txt; script check)
| URL | Result |
|---|---|
| https://www.leg.state.fl.us/robots.txt | 200; `User-agent: *` Disallow /employees/ only; Drifter, SemrushBot fully disallowed |
| https://www.flsenate.gov/robots.txt | 200; Disallow /api/, /API/, admin/tracker paths; Allow /Laws/; `Crawl-delay: 10` |
| https://florida.public.law/robots.txt | 200; Disallow /admin /api /data /demo /images /users |
| https://law.justia.com/robots.txt | 403 Cloudflare "Just a moment..."; script REFUSED (robots challenge) |
| https://www.flrules.org/robots.txt | 301 → flrules.org/robots.txt → curl got Cloudflare challenge page; script robots check returned ok (no rules) |
| https://supremecourt.flcourts.gov/robots.txt | 200; `User-agent: * Disallow: /`; Allow only named search bots |
| https://www.flcourts.gov/robots.txt, https://1dca.flcourts.gov/robots.txt, https://flcourts-media.flcourts.gov/robots.txt | same "Disallow: /" for * |
| https://2dca…6dca.flcourts.gov/robots.txt | "# Disallow all" / `User-agent: * Disallow: /` |
| https://acis.flcourts.gov/robots.txt | 200 text/html — the SPA index.html (no robots file) |
| https://www.floridabar.org/robots.txt, https://www-media.floridabar.org/robots.txt | 403 "Attention Required! \| Cloudflare"; script REFUSED (bot check) |
| https://www.law.cornell.edu/robots.txt | 200; Crawl-delay: 10 |
| https://library.law.fsu.edu/robots.txt | 404 (Apache) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0768/Sections/0768.81.html | script | html 9,490 chars; "The 2026 Florida Statutes"; "768.81 Comparative fault.— (1) DEFINITIONS" |
| http://www.leg.state.fl.us/…0768.81.html (same) | WF | YES "(1) DEFINITIONS.—As used in this section, the term"; "The 2026 Florida Statutes"; not truncated; no disclaimer |
| …URL=0000-0099/0090/Sections/0090.803.html | script | 2026; "The provision of s. 90.802 to the contrary notwithstanding" |
| …URL=1000-1099/1001/Sections/1001.42.html | script | 51,064 chars; "1001.42 Powers and duties of district school board" |
| …URL=0700-0799/0768/0768.html (whole chapter) | script | 217,351 chars |
| …App_mode=Display_Statute&StatuteYear=2023&URL=0700-0799/0768/Sections/0768.81.html | script | "The 2023 Florida Statutes (including Special Session C)" |
| …URL=0000-0099/0090/0090ContentsIndex.html | script | section list 90.801-90.805 |
| …App_mode=Display_Index&Title_Request=XLV | script | ranges shown: "Part I: GENERAL PROVISIONS (ss. 768.041-768.405)" |
| https://www.leg.state.fl.us/index.cfm?Mode=Statutes%20Download&Submenu=7&Tab=statutes | script+curl | only FLLawDL2026.zip Windows installer ("Advanced Legislative Search & Browse") |
| https://www.flsenate.gov/Laws/Statutes/2025/768.81 | script | 15,273 chars |
| https://www.flsenate.gov/Laws/Statutes/2025/57.105 | WF | YES "Upon the court's initiative or motion of any party, the"; "2025 Florida Statutes"; disclaimer "information on this system is unverified" |
| https://www.flsenate.gov/Laws/Statutes/2026/90.803 | script | "2026 Florida Statutes … Section 803", body present |
| https://www.flsenate.gov/Laws/Statutes | script | footer disclaimer as above |
| https://www.flsenate.gov/Laws/Statutes/2026/768.81 | script | REFUSED: HTTP 429 (after ~8 requests; crawl-delay 10) |
| https://florida.public.law/statutes/fla._stat._768.81 | script | body present; source "flsenate.gov/Laws/Statutes/2024/0768.81 (accessed Aug. 7, 2025)" |
| https://florida.public.law/statutes/fla._stat._90.803 | script | body present; same 2024 source |
| https://florida.public.law/ , /statutes | script | home last-modified Aug 7 2025; title list |
| https://florida.public.law/statutes/fla._stat._57.105 | WF | YES; "Current through Fall 2025"; "(accessed Aug. 7, 2025)" |
| https://law.justia.com/codes/florida/title-xlv/chapter-768/part-ii/section-768-81/ | WF | YES; "2025 Florida Statutes"; "FL Stat § 768.81 (2025)" |
| same | script | REFUSED (Justia robots challenge) |
| https://law.justia.com/codes/florida/title-vii/chapter-90/section-90-803/ | WF | YES "The provision of s. 90.802 to the contrary notwithstanding, the"; 2025 |
| https://laws.flrules.org/2023/15 | script | pdf 21 pp, 55,995 chars; "CHAPTER 2023-15 … House Bill No. 837" |
| https://laws.flrules.org/files/Ch_2023-015.pdf | script | same sha256 |
| https://laws.flrules.org/2025/2 | script | pdf 5 pp |
| https://laws.flrules.org/2023/15 | WF | YES; "Approved by the Governor March 24, 2023."; not truncated |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.flsenate.gov/Laws/Constitution | script | 419,692 chars; anchors A1, A1S01…; Art. VII § 6 reached |
| same | WF | Art. I § 9 YES "No person shall be deprived of life, liberty or property"; Art. V § 3(b)(3) NOT PRESENT; text 133,252; ends Art. IV § 9 |
| same, offset=100000 | WF | Art. V § 3(b)(3) YES "May review any decision of a district court of appeal"; ends Art. V § 13 |
| https://www.leg.state.fl.us/index.cfm?Mode=Constitution&Submenu=3&Tab=statutes | script+curl | anchors #A1…#A12, #A1S01…; "expressly and directly conflicts" at offset 103,924 |
| same | WF | Art. I § 9 YES; Art. V § 3(b)(3) NOT PRESENT; text 136,480; ends Art. IV § 13 |
| https://law.justia.com/constitution/florida/ | WF | Art. I § 9 YES; one page, #A01S01 anchors; truncated mid Art. V § 10; text 132,664 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.floridabar.org/rules/florida-rules-of-court/ | script | REFUSED (Cloudflare bot check on robots.txt) |
| same | WF | CLIENT_ERROR "There was an error while fetching." |
| WebSearch "Florida Rules of Civil Procedure pdf floridabar.org uploads 2026" | search | Civil 10-01-26, 06-19-25, 04-01-24; Appellate 09-01-26; Small Claims 7-1-2026 |
| https://www-media.floridabar.org/uploads/2026/01/Civil-Procedure-Rules-Updated-1-1-2026.pdf | script check | REFUSED (Cloudflare) |
| https://www-media.floridabar.org/uploads/2026/10/Civil-Procedure-Rules-10-01-26.pdf | WF | Rule 1.510 NOT PRESENT; "current through 2026 WL 2603472"; truncated in Rule 1.190(f) |
| same, offset=100000 | WF | 1.510 NOT PRESENT; only Rule 1.200 visible |
| https://www-media.floridabar.org/uploads/2026/09/Appellate-Court-Rules-09-01-26.pdf | WF | 9.030 YES "The supreme court shall review, by appeal: (i) final orders"; "current through 434 So.3d 978"; ends after 9.110; text 112,114 |
| WebSearch criminal / general practice PDFs | search | Criminal 7-13-2026-2.pdf; Gen. Prac. & Jud. Admin. 7-1-2026.pdf |
| https://www-media.floridabar.org/uploads/2026/08/2026_01-JUL-Criminal-Procedure-Rules-7-13-2026-2.pdf | WF | 3.191 NOT PRESENT; last body 3.130(d); header "July 13, 2026"; text 114,916 |
| https://supremecourt.flcourts.gov/case-information/opinions | WF | ROBOTS_DISALLOWED |
| https://supremecourt.flcourts.gov/ | script | REFUSED robots "Disallow: /" |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.flrules.org/gateway/ruleNo.asp?id=61G15-19.001 | script | 9,889 chars; "Rule Title: Grounds for Disciplinary Proceedings"; "Effective Date: 8/20/2026" |
| same | WF | body NOT in page; VIEW_RULE href readFile.asp?sid=0&tid=31199582&type=1&file=61G15-19.001.doc; no challenge |
| https://flrules.org/gateway/readFile.asp?sid=0&tid=31199582&type=1&file=61G15-19.001.doc | script | 33,272 bytes OLE Word binary |
| same | WF | "[binary data]", NO |
| https://www.flrules.org/gateway/readFile.asp?sid=0&tid=0&type=1&file=61G15-19.001.doc | script | 800-char Dept. of State boilerplate (wrong tid) |
| https://www.flrules.org/gateway/View_notice.asp?id=31199582 | script | notice metadata, "RULE EFFECTIVE DATE: 8/20/2026" |
| https://www.flrules.org/gateway/notice_Files.asp?ID=31199582 | script | Word binary |
| https://www.flrules.org/gateway/ChapterHome.asp?Chapter=61G15-19 | script | 2,959 chars html |
| https://www.flrules.org/gateway/ruleNo.asp?id=62-302.530 | script | "Effective Date: 11/25/2025" |
| https://www.flrules.org/Faw/FAWIssues.asp | script | HTTP 500 |
| WebSearch "flrules.org Florida Administrative Register issue" | search | bigDoc/Default.asp?Year=, View_Faw.asp?IID= |
| https://flrules.org/bigDoc/Default.asp?Year=2026 | script | "2026 Issues (202) 2025 Issues (252)"; "January 2, 2026 - Vol/No 52/01" |
| https://flrules.org/BigDoc/View_Faw.asp?IID=4546 | script | issue Dec 23, 2025; sections |
| same | WF | Entire Issue href GotoLink.asp?Goto=BigDocFAW&Para=2025/51247/51247doc.pdf |
| https://flrules.org/gateway/GotoLink.asp?Goto=BigDocFAW&Para=2025/51247/51247doc.pdf | script | → /Faw/FAWDocuments/FAWVOLUMEFOLDERS2025/51247/51247doc.pdf; pdf 27 pp, 165,321 chars; "Florida Administrative Register Volume 51, Number 247" |
| https://www.law.cornell.edu/regulations/florida | script | FAC department list |
| https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-61G15-19-001 | script | body "(1) Pursuant to Section 471.033(2), F.S."; history ends "4/19/2023" |
| same | WF | YES; "effective 4/19/2023"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-62-302-530 | script | page present |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WebSearch "supremecourt.flcourts.gov content download opinion pdf SC2023" | search | FSU library archive, Justia |
| WebSearch flcourts opinions search | search | no usable official URL |
| https://1dca.flcourts.gov/ | WF | ROBOTS_DISALLOWED |
| https://acis.flcourts.gov/ | WF | "this application doesn't work properly without JavaScript enabled" |
| same | script | 200, html, 0 chars |
| https://acis.flcourts.gov/assets/index-06f12c8e.js | curl | 1.16 MB bundle; apiRoot "/api/v1"; route "/altcha/challenge" (not called) |
| https://library.law.fsu.edu/Digital-Collections/flsupct/dockets/SC22-0378/SC22-0378.html | script+curl | "Citation: 379 So.3d 1080"; links op-sc22-0378.pdf, briefs |
| https://library.law.fsu.edu/Digital-Collections/flsupct/dockets/SC22-0378/op-sc22-0378.pdf | script | pdf 39 pp, 49,996 chars; "No. SC2022-0378 … November 16, 2023 PER CURIAM." |
| same | WF | YES "Markeith Demangzlo Loyd was charged with and convicted of first-degree murder"; slip "- 2 -"; complete |
| …/flsupct/index.html; dockets/SC2024.html, SC2025.html, SC2026.html, SC19.html, SC05.html; SC24/SC25/SC26.html | curl | year listings exist for SC99-SC23 and SC2024-SC2026 (SC24.html etc. 404); folder forms SC19-0087, sc05-13 |
| …/dockets/SC25-0016/SC25-0016.html | curl | "In Re: Amendments to Florida Rules of Juvenile Procedure"; "Not for Commercial Use" |
| WebSearch "law.justia.com cases florida fourth-district-court-of-appeal 2024" | search | slugs; cases.justia.com PDFs |
| https://law.justia.com/cases/florida/fourth-district-court-of-appeal/2025/4d2024-0558.html | WF | YES; PCA "PER CURIAM. Affirmed."; Apr. 24, 2025 |
| https://law.justia.com/cases/florida/supreme-court/2023/sc2022-0378.html | WF | YES "PER CURIAM. Markeith Demangzlo Loyd was charged…"; complete |
| https://law.justia.com/cases/florida/ | WF | supreme-court, district-courts-of-appeal |
| https://law.justia.com/cases/florida/sixth-district-court-of-appeal/2025/ | WF | "Opinions 1 - 500 of 1182"; 6d23-3822.html … |
| https://law.justia.com/cases/florida/supreme-court/ | WF | 1848-2026; "sourced from individual state court sites" |
| https://law.justia.com/cases/florida/district-courts-of-appeal/ | WF | 1957-2026; first/second DCA slugs |

## F — Subsequent history
No fetchable source records orders declining Supreme Court review: flcourts.gov robots-disallowed; ACIS JS-only with an altcha route. Justia/FSU hold opinions only (party-name search). Recorded `reported` rows and an `absent` entry.

## WebFetch tally
33 calls: statutes 5, constitution 4, rules 5, admin 4 (+1 FAR), case law 11, misc 3. No quota/rate failures from WebFetch; flsenate.gov gave the script one HTTP 429.

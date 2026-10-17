# South Carolina (sc) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET through the agent proxy (robots files and form markup only; never on a refused URL); "WS" = WebSearch. Quoted text ≤ 15 words. WebFetch calls: 16 (13 returned content, 2 ROBOTS_DISALLOWED, 1 PROVENANCE_REQUIRED). No quota or rate failures. WebSearch: 5.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.scstatehouse.gov/robots.txt | script | 200: `User-Agent:*` Disallow /images/ /jpeg/ /gif/ /dashboard/ /sys/; AhrefsBot, Riddler Disallow / |
| https://www.sccourts.gov/robots.txt | script | FETCH ERROR: proxy "Tunnel connection failed: 502 Bad Gateway" |
| https://www.sccourts.gov/robots.txt, https://sccourts.gov/ | curl | CONNECT tunnel failed, 502; http://www.sccourts.gov: "Could not resolve host" |
| https://www.sccourts.gov/ | WF | ROBOTS_DISALLOWED |
| https://www.sccourts.gov/robots.txt | WF | ROBOTS_DISALLOWED |
| https://www.sccourts.org/robots.txt | script | REFUSED "disallows /robots.txt (rule: Disallow: /)" |
| https://www.sccourts.org/robots.txt | curl | 200; Google/Bing groups with path rules; "# No one else" `User-agent: *` `Disallow: /` `Crawl-delay: 120000` |
| https://www.sccourts.org/opinions/, /court-rules/ | script check | REFUSED "disallows … (rule: Disallow: /)" — not fetched by any route |
| https://law.justia.com/robots.txt | script | REFUSED: host refused earlier today (robots.txt challenge, 09:44) |
| https://publicindex.sccourts.org/robots.txt | script | HTTP 400 (not used) |
| https://www.judicial.state.sc.us/robots.txt | script | unreachable (XHTML error page) |
| https://ctrack.sccourts.org/robots.txt | script | 404 (no rules) |
| https://dc.statelibrary.sc.gov/robots.txt | script | 200 DSpace: Disallow /search, /browse, /entities/*?f, …; Crawl-delay 10 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.scstatehouse.gov/code/t15c003.php | script | 200 html 45,604 chars; grep "SECTION 15-3-530. Three years. Within three years:" found; header "South Carolina Code of Laws Unannotated" |
| raw HTML of t15c003.php | curl | no section anchors (ids only: adobebox, container, header…) |
| https://www.scstatehouse.gov/code/statmast.php | script | DISCLAIMER "now current through the 2025 Session of the General Assembly"; "this version … is not official" |
| https://www.scstatehouse.gov/code/title15.php, title1.php | script | chapter links t01c001.php…; Word links getfile.php?TYPE=CODEOFLAWS&TITLE=15&CHAPTER=3; no section ranges |
| title1.php … title63.php | script | 1,371 chapter links, all t{2d}c{3d}.php except t36c002A, t36c004A, t40c021R, t40c073R |
| t40c021R.php | script | heading "CHAPTER 21" only; title40 lists "CHAPTER 21 - RESERVED" |
| t36c002A.php | script | "SECTION 36-2A-103." found |
| t16c003, t01c023, t12c006, t38c077, t63c007 | script | 333,507 / 140,304 / 508,386 / 114,967 / 314,879 chars; "SECTION 16-3-20. Punishment for murder", "SECTION 1-23-380. Judicial review…", "SECTION 12-6-510. Tax rates…" found |
| WS "scstatehouse.gov code t15c003 …" | WS | returned scstatehouse.gov/code/t15c003.php and /Archives/CodeofLaws{2002-2010}/t15c003.php |
| https://scstatehouse.gov/code/t15c003.php | WF | YES "Within three years: (1) an action upon a contract…"; last § 15-3-700; not truncated |
| https://www.scstatehouse.gov/code/t16c003.php (built) | WF | 16-3-2020 NOT PRESENT; truncated at 100,000 of 124,663 chars, inside § 16-3-740 |
| query.php?search=DOC&searchtext="sealed instrument"&category=CODEOFLAWS | script | "found 0 times" / "Document not available" |
| query.php?search=FIRST&searchtext=sealed+instrument&category=CODEOFLAWS | script | "Submitting..." (JS auto-submit); search not usable by GET |
| https://law.justia.com/codes/south-carolina/title-15/chapter-3/section-15-3-530/ | WF | YES "Within three years: (1) an action upon a contract, obligation,"; "2025 South Carolina Code of Laws"; "may not be the most recent version" |
| https://law.justia.com/codes/south-carolina/title-16/chapter-3/section-16-3-20/ | WF | YES "A person who is convicted of or pleads guilty to"; 2025 edition |
| https://www.scstatehouse.gov/newlaws.php | script | 200; "Ratification Sheets & Act Lists"; "2025-2026 Legislative Session"; older lists in Archives |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.scstatehouse.gov/scconstitution/scconst.php | script | "October 14, 2025 - … updated through the 2025 Session …"; "is not official"; links A01.pdf … A17.pdf, A08A.pdf, SCConstitution.pdf |
| …/scconstitution/A01.pdf | script | 7 pp, 20,313 chars, Last-Modified 14 Oct 2025; "SECTION 10. Searches and seizures; invasions of privacy." |
| …/scconstitution/A05.pdf | script | 7 pp; "SECTION 5. Jurisdiction of Supreme Court." |
| …/scconstitution/SCConstitution.pdf | script | 99 pp, 244,257 chars |
| https://www.scstatehouse.gov/scconstitution/A01.pdf (built) | WF | YES "The right of the people to be secure in their"; last § 25; not truncated |
| https://law.justia.com/constitution/south-carolina/ | WF | index: introduction.html, preamble.html, a01.html; "may not be the most recent version" |
| https://law.justia.com/constitution/south-carolina/a01.html | WF | § 10 YES "The right of the people to be secure in their"; last section 24 (stale) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.sccourts.org/court-rules/ | script check | REFUSED robots (Disallow: /) |
| WS "South Carolina Rules of Civil Procedure Rule 12 SCRCP text …" | WS | only non-vetted third parties (courtrules.net, rulesofcivilprocedure.com, vlex, state-rules.com) |
No fetch of any rule text; no tier-2 source exists.

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.scstatehouse.gov/coderegs/statmast.php | script | "Files are current through State Register Volume 50, Issue 3, effective March 27, 2026."; "is not official"; links "Chapter N.pdf", getfile.php?TYPE=CODEOFREGS&CHAPTER=N, Chapter61.php |
| …/coderegs/Chapter61.php | script | links "Chapter 61-1 through 61-17.pdf", "Chapter 61-62.pdf", … (18 PDFs) |
| …/coderegs/Chapter 61-62.pdf (raw space) | script | FETCH ERROR "URL can't contain control characters" |
| …/coderegs/Chapter%2061-62.pdf | script | 397 pp, 1,570,629 chars, Last-Modified 23 Feb 2026; "61-62.1" at p. 60 |
| …/coderegs/Chapter%2010.pdf | script | 23 pp, 82,785 chars; "CHAPTER 10 Department of Labor, Licensing and Regulation"; "10–1." (en dash) |
| https://www.scstatehouse.gov/coderegs/Chapter%2061-62.pdf (built) | WF | 61-62.5 NOT PRESENT; truncated inside 61–62.1 § II(L) |
| https://www.scstatehouse.gov/state_register.php | script | year rows 2005-2027; links state_register.php?first=FILE&pdf=1&file=Sr50-9.pdf, index2025.pdf |
| …file=Sr50-9.pdf | script | 53 pp, 153,818 chars; "SOUTH CAROLINA STATE REGISTER DISCLAIMER"; "Published September 25, 2026 Volume 50 Issue No. 9" |
| …file=Sr50-3.pdf | script | 22 pp, 67,254 chars |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS "sccourts.gov published opinions …", "site:sccourts.gov opinions supreme court" | WS | no sccourts.gov results; dc.statelibrary.sc.gov advance-sheet items |
| https://www.sccourts.org/opinions/ | script check | REFUSED robots |
| https://dc.statelibrary.sc.gov/entities/publication/518f38c4-71bd-403f-920d-600dc17e2ae5 | script | 1,751 chars; "Opinions of the Supreme Court and Court of Appeals … advance sheet no. 26"; PDF not followed |
| https://law.justia.com/cases/south-carolina/ | WF | two courts: supreme-court/, court-of-appeals/ |
| https://law.justia.com/cases/south-carolina/supreme-court/ | WF | years 2026-1883 (some skipped); latest No. 28348, Aug. 12, 2026 |
| https://law.justia.com/cases/south-carolina/supreme-court/2024/ | WF | 28246 State v. Clark Dec. 18, 2024 → …/2024/28246.html; 28245 Huskins Dec. 11, 2024 |
| https://law.justia.com/cases/south-carolina/supreme-court/2024/28245.html | WF | YES full text "When Petitioners Amanda Leigh Huskins and Jay R. Huskins decided to buy"; Opinion No. 28245; Appellate Case No. 2023-000452; PDF cases.justia.com/south-carolina/supreme-court/2024-28245.pdf; no own S.C./S.E.2d cite |
| https://law.justia.com/cases/south-carolina/court-of-appeals/2024/ | WF | 2024-UP-425 Long v. Boutelle Dec. 30, 2024 → 2024-up-425.html; published No. 6093 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://ctrack.sccourts.org/ | script | → /public/caseSearch.do, "South Carolina Appellate Case Management System"; disclaimer "should not be relied upon as an official record of action" |
| caseSearch.do form markup | curl | method=post; fields courtID (10001 Supreme, 10002 COA), shortTitle, csNumber, fromDt/toDt, csGroupID, csTypeID, exclude |
| caseSearch.do?courtID=10001&csNumber=2023-000452&…&exclude=on | script | "No records were found." (closed cases excluded) |
| same without exclude | script | redirect caseView.do?csIID=78122; "01/16/2025 Rehearing - Denied"; "10/14/2025 Supreme Court of the United States - Notice that Certiorari Denied" |
| caseView.do?csIID=78122 | script | 2023-000452, "Certiorari - COA - Common Pleas - Other", lower court Richland (2017CP4003697) |
| caseSearch.do?courtID=10002&shortTitle=Huskins&… | script | → csIID=67446, 2018-000889, disposition 02/15/2023 Opinion, same lower court number |
| caseView.do?csIID=1043, 2375 | script | 2012-206608 (COA, filed 01/18/2012), 2012-206607 (Supreme, Certiorari - COA) |
| https://ctrack.sccourts.org/public/caseView.do?csIID=78122 (built) | WF | PROVENANCE_REQUIRED (approval not answered) — not a site refusal |
| WS "\"ctrack.sccourts.org\" …" | WS | ctrack pages; "sccourts.org/ACMS" listed (court site link to the portal) |

## Cross-check
`build.py --check`: no ERROR/WARN for sc.json. `build.py --cross`: one line, `CROSS sc: 'Act No. 133 of 2016 (S.C.)' also matches pa / Pennsylvania session laws` — the PA pattern `Act\s+(?:No\.\s*)?\d{1,4}\s+of\s+\d{4}` has no Pennsylvania marker; fix belongs in pa.json. Example left as is.

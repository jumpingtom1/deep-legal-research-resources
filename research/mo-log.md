# Missouri (mo) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt reads only (no refusal worked around). WebFetch calls: 25 (of ~55); 2 refused by the session's URL-provenance gate (unanswered permission prompt, not a site refusal). WebSearch: 12.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://revisor.mo.gov/robots.txt | curl | HTML "Object Moved" redirect to Home.aspx: no robots rules |
| https://www.courts.mo.gov/robots.txt | curl | `User-agent: *` Disallow /cnet/ /casenet/ /ecf/ /fv/ /bench/ /page.jsp?id=236; comment bans data scrapers |
| https://www2.courts.mo.gov/page.jsp?id=198912 | script | FETCH ERROR: TLS chain does not verify (hostname mismatch); curl robots: exit 60 |
| https://www.sos.mo.gov/robots.txt | curl | Cloudflare "Just a moment..." page |
| https://www.sos.mo.gov/adrules/csr/current/10csr/10csr | script check | "allowlisted; robots.txt permits"; pages fetched 200 |
| https://law.justia.com/… | script | REFUSED: robots.txt bot challenge earlier today; host off for the day |
| https://www.law.cornell.edu/regulations/missouri | script | OK |
| https://missouri.public.law/ | script | FETCH ERROR: proxy 502 on robots.txt |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://revisor.mo.gov/main/OneSection.aspx?section=516.120 | script info/read | 200, 10,599 chars; "516.120. What actions within five years. — Within five years:" |
| https://revisor.mo.gov/main/OneSection.aspx?section=537.765 | script | 200, 7,117 chars; "Contributory fault, as a complete bar to plaintiff's recovery" |
| https://revisor.mo.gov/main/OneSection.aspx?section=537.765 | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://revisor.mo.gov/main/Home.aspx | script grep | "statutes posted on this website are uncertified and unofficial"; "2025 Cumulative Supplement … is available" |
| https://revisor.mo.gov/main/Help.aspx | script grep | "Programmatically slow down malicious access" (2019 change log) |
| https://revisor.mo.gov/main/Info.aspx | script grep | print order forms, Appendices/Tables PDFs; no bulk data |
| https://revisor.mo.gov/main/MultiEnact.aspx | script links | PageSelect.aspx?section=56.067&bid=2011 / bid=36193 |
| https://revisor.mo.gov/main/OneSection.aspx?section=56.067 | script grep | "Effective - 28 Aug 2014, 2 histories"; "All versions" table |
| https://revisor.mo.gov/main/DwnLD.aspx?section=56.067&bid=2011&nid=0&idx=1 | script info | html, 0 chars |
| WebSearch "revisor.mo.gov OneSection.aspx section 516.120" | WS | only old Justia / unrelated hits |
| WebSearch "law.justia.com codes missouri section 516.120 2024…" | WS | /codes/missouri/2025/ etc. |
| https://law.justia.com/codes/missouri/2025/ | WF | titles with section ranges; "These codes may not be the most recent version." |
| https://law.justia.com/codes/missouri/title-xxxv/chapter-516/section-516-120/ | WF (built, not gated) | YES; "Within five years: (1) All actions upon contracts, obligations or"; "2025 Missouri Revised Statutes" |
| https://law.justia.com/codes/missouri/title-xxxvi/chapter-537/section-537-765/ | WF | YES; "Contributory fault, as a complete bar to plaintiff's recovery in" |
| https://law.justia.com/codes/missouri/title-xxxv/ | WF | chapters listed without section ranges |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://revisor.mo.gov/main/Home.aspx?constit=y | script links | per-section links PageSelect.aspx?section=I    10&bid=…&constit=y (4-space padding) |
| https://revisor.mo.gov/main/ViewChapter.aspx?chapter=I&constit=y | script grep | 138,558 chars; "I Section 10. Due process of law." |
| https://revisor.mo.gov/main/ViewChapter.aspx?chapter=V&constit=y | script grep | 107,365 chars; "V Section 10. Transfer of cases from court of appeals" |
| https://revisor.mo.gov/main/OneSection.aspx?section=I%20%20%20%2010&constit=y | script grep | 28,795 chars; "That no person shall be deprived of life, liberty or property" |
| https://revisor.mo.gov/main/OneSection.aspx?section=V%20%20%20%2010&constit=y | script grep | 6,842 chars; "Effective - 02 Sep 1976" |
| https://law.justia.com/constitution/missouri/article-i/section-10/ | WF | YES; "That no person shall be deprived of life, liberty or" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WebSearch "courts.mo.gov Supreme Court Rules Rule 55.27 page" | WS | page.jsp?id=58122 (index) and others |
| https://www.courts.mo.gov/page.jsp?id=58122 | script | REFUSED: HTTP 403 |
| https://www.courts.mo.gov/page.jsp?id=58122 | WF ×2 | loads; categories only; "not considered official documents"; no hrefs visible |
| WebSearch "\"55.27\" \"Defenses and Objections - How Presented\"…" | WS | page.jsp?id=199658; ClerkHandbooksP2RulesOnly.nsf docs |
| WebSearch "courts.mo.gov \"Rule 4-1.7\"…" | WS | page.jsp?id=198912 |
| https://www.courts.mo.gov/page.jsp?id=199658 | WF | YES Rule 55.27; "Every defense, in law or fact, to a claim in"; "Most Recently Effective: January 01, 2012" |
| https://www.courts.mo.gov/page.jsp?id=198912 | WF | YES Rule 4-1.7; "(a) Except as provided in Rule 4-1.7(b), a lawyer shall"; July 01, 2007 |
| https://www.courts.mo.gov/courts/ClerkHandbooksP2RulesOnly.nsf/c0c6ffa99df4993f86256ba50057dcb8/a9fdabe676220f8986256ca600521544 | script | 200, 6,571 chars; 55.27 text; Revised/Effective January 1, 2012 |
| …/c0c6ffa99df4993f86256ba50057dcb8/55.27?OpenDocument (and 4-1.7, 84.04) | script | HTTP 404 (key URLs not supported) |
| …/c0c6ffa99df4993f86256ba50057dcb8?OpenView&StartKey=55.27&Count=5 | script | categorized view; category expand links only |
| …?SearchView&Query=55.27 | script links | 55.27 first hit |
| …?SearchView&Query=%2284.04%22 / %224-1.7%22&Count=100 | script links | 84.04 doc; "4- 1. 7" doc d06710dff1830d2686256ca600521205 |
| …/988c5b6f0d74867086256ca6005215c9?OpenDocument | script | 84.04 "Briefs - Contents"; Revised/Effective January 1, 2018 |
| …?SearchView&Query=%222024%22 etc. | script | latest effective date seen: September 3, 2024 (16.07 repeal) |
| WebSearch "courts.mo.gov page.jsp \"84.04\" \"Briefs - Contents\"" | WS | no per-rule page found |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.sos.mo.gov/adrules/csr/current/10csr/10csr | script info/links | 200; Chapter links …/10csr/10c10-6.pdf, 10c20-7a.pdf |
| https://www.sos.mo.gov/adrules/csr/current/10csr/10csr | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://www.sos.mo.gov/CMSImages/AdRules/csr/current/10csr/10c10-6.pdf | script | PDF 164 pp, 1,275,288 chars; "10 CSR 10-6.060 Construction Permits Required"; footer "(6/30/26)" |
| https://www.sos.mo.gov/cmsimages/adrules/csr/current/20csr/20c2150-2.pdf | script | PDF 28 pp; "20 CSR 2150-2.001 Definitions"; footer "(5/31/26)" |
| https://www.law.cornell.edu/regulations/missouri/10-CSR-10-6-060 | script | 90,554 chars; "PURPOSE: This rule defines sources required to obtain permits"; Last-Modified Aug 2025 |
| https://www.law.cornell.edu/regulations/missouri/20-CSR-2150-2-001 | script | 8,932 chars; "PURPOSE: This rule defines terms used in Chapter 334, RSMo" |
| https://www.sos.mo.gov/adrules/moreg/moreg | script links | latest issue link /adrules/moreg/2026/v51/n20; year pages 2007-2025 |
| https://www.sos.mo.gov/adrules/moreg/2026 | script links | sidebar links only |
| https://www.sos.mo.gov/adrules/moreg/2026/v51/n20 | script links | "Volume 51, Number 20 (Pages 1313-1404)" -> v51n20.pdf |
| https://www.sos.mo.gov/CMSImages/AdRules/moreg/2026/v51n20Oct15/v51n20.pdf | script | PDF 92 pp, 671,011 chars; "Volume 51, Number 20 October 15, 2026 Pages 1313–1404" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WebSearch (3 queries) for courts.mo.gov opinions | WS | SUP/index.nsf minutes docs; page.jsp?id=103681; file.jsp ids |
| https://www.courts.mo.gov/page.jsp?id=103681 | script | REFUSED: HTTP 403 |
| https://www.courts.mo.gov/page.jsp?id=103681 | WF | ED "Pending Cases & Decisions" description; no listings |
| https://www.courts.mo.gov/page.jsp?id=1944 | WF ×2 | "Appellate Opinions … Opinions and Minutes"; no hrefs visible |
| https://www.courts.mo.gov/page.jsp?id=12086&dist=Opinions%20Supreme&date=all | WF | CLIENT_ERROR "error while fetching" |
| https://www.courts.mo.gov/file.jsp?id=236410 | script | REFUSED: HTTP 403 |
| https://www.courts.mo.gov/file.jsp?id=236410 | WF | CLIENT_ERROR "error while fetching" |
| https://www.courts.mo.gov/file.jsp?id=236411 | WF | CLIENT_ERROR "error while fetching" |
| WebSearch "law.justia.com cases missouri court-of-appeals 2024 opinion" | WS | year listings |
| https://law.justia.com/cases/missouri/court-of-appeals/2024/ | WF | "Opinions 1 - 500 of 621"; …/2024/ed112690.html |
| https://law.justia.com/cases/missouri/court-of-appeals/2024/ed112690.html | WF | YES; "Mary Beth Fryman sued The Board of Regents"; slip pagination |
| https://law.justia.com/cases/missouri/supreme-court/2026/sc101233.html | WF (built) | YES; "In his sole point on appeal, Harris contends the circuit court" |
| https://law.justia.com/cases/missouri/supreme-court/ | WF | years 1852-2026 |
| https://law.Justia.com/cases/missouri/court-of-appeals/ | WF | years 1891-2026 |
| https://law.justia.com/cases/missouri/court-of-appeals/2026/sd39269.html | WF (built) | CLIENT_ERROR (year likely wrong; not retried) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.courts.mo.gov/SUP/index.nsf/cfc8c4b5bc15cb158625661d0073593c/b3132bb9f649b0c186258e1f004c9e11 | script | Minutes of June 23, 2026; SC101233 -> file.jsp?id=236410 |
| https://www.courts.mo.gov/SUP/index.nsf/cfc8c4b5bc15cb158625661d0073593c?OpenView | script links | "Minutes of September 29, 2026" newest |
| …?OpenView&Start=1&Count=1000 | script links | 643 minutes; oldest "Minutes of May 26, 1998" |
| …/a984ebacb282c9d786258e810054d46d?OpenDocument | script | "application for transfer from the Missouri Court of Appeals, ED113496, denied" |
| …?SearchView&Query=ED112690 / ED113496 | script | no hits (search form only) |
| WebSearch "\"courts.mo.gov/file.jsp?id=\" opinion … Western District" | WS | page.jsp?id=2557; file.jsp?id=214050 |
| https://www.courts.mo.gov/file.jsp?id=214050 | WF | Motion Rulings report, WD, Oct 29, 2024 |
| https://www.courts.mo.gov/page.jsp?id=2557 | WF | "Missouri Court of Appeals – Western District Minutes"; Post-Opinion Motion Rulings list |

## G — Citation map
Built from memory and the pages above (RSMo style "section 516.120, RSMo 2016"; dotted subsections 537.765.3; "(Mo. banc YYYY)", "(Mo. App. E.D. YYYY)"; dockets SC/ED/WD/SD). `build.py --check`: no ERROR/WARN for mo.json. `build.py --cross`: no line involving mo (one unrelated sc/pa line).

## Fix pass (2026-10-17, from research/mo-verify.json)
Applied the independent check: 11 rows marked `by: independent`, with second citations appended. mo-coa-minutes downgraded to `reported`: its index exposes no file.jsp links to WebFetch and is stale (June 24, 2025). mo-sc-minutes: the view omits some sessions; the June 23, 2026 minutes document was reached via WebSearch and is not in the view. Hazard added and evidence corrected; the count is 641. mo-csr-sos: navigation now filters links by file name. mo-register-sos: past-year pages do list issue PDFs. Regex: added R.S.Mo., V.A.M.S., "section X of the Revised Statutes of Missouri" and "Missouri Rule(s) of Professional Conduct". No new fetches. `--check` and `--cross` are clean.

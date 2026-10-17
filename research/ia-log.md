# Iowa (ia) probe log — 2026-10-17

All probes by `research` on 2026-10-17. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET through the agent proxy, used only for robots files and one look at a listing page's form markup, never on a refused URL. Quoted text is 15 words or fewer. WebFetch calls: 21 (19 returned content, 2 PROVENANCE_REQUIRED on built iowacourts.gov URLs, not retried). No quota or rate failures.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.legis.iowa.gov/robots.txt | curl | 200; `*` Disallow /chambers/ only |
| https://www.iowacourts.gov/robots.txt | curl | 200; `*` Crawl-delay: 30; empty Disallow |
| https://rules.iowa.gov/robots.txt | curl | 404 (IIS) |
| https://www.iowacourts.state.ia.us/robots.txt | curl | 302 → /ESAWebApp/robots.txt; script `check` says robots permits |
| https://law.justia.com/codes/iowa/title-xv/chapter-614/section-614-1/ | script | REFUSED: "law.justia.com refused automated access earlier (robots.txt challenge)" |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.legis.iowa.gov/docs/code/614.1.pdf | script | PDF 3 pp., 10,777 chars; "Actions may be brought within the times limited"; footer "Iowa Code 2026, Section 614.1 (30, 0)" |
| …/docs/code/2026/614.1.pdf | script | same sha256 as undated |
| …/docs/code/2025/614.1.pdf | script | PDF 3 pp., last-modified 21 Nov 2024 |
| …/docs/code/707.2.pdf | script | 1 p.; "707.2 Murder in the first degree." |
| …/docs/code/321J.2.pdf | script | 4 pp.; footer "Iowa Code 2026, Section 321J.2 (37, 2)" |
| …/docs/code/614.pdf | script | chapter PDF 17 pp., 68,530 chars |
| https://www.legis.iowa.gov:443/docs/code/2023/614.1.pdf | WF | YES; footer "Iowa Code 2023, Section 614.1 (27, 0)"; not truncated |
| https://www.legis.iowa.gov:443/docs/code/2021/614.pdf | WF | full chapter to 614.38; "Iowa Code 2021, Chapter 614 (30, 2)" |
| https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter=614&year=2026 | script links | 89 links; per-section PDF/RTF (614.4A.pdf) |
| …/law/iowaCode/chapters?title=XV&year=2026 | script links | 725 links (chapter list) |
| https://www.legis.iowa.gov/law/iowaCode | script grep | "Official Version - PDF format: Vol I…"; "Unofficial Version - PDF and RTF formats" |
| https://www.legis.iowa.gov/law/statutory | script links | Vol I-VIII → /docs/publications/ICV/1594653-1594660.pdf |
| https://www.legis.iowa.gov/law/officialAndUnofficialEditions | script read | UELMA, Iowa Code ch. 2B; authentication since January 9, 2020 |
| https://www.legis.iowa.gov/docs/publications/ICV/1594658.pdf | script | 1,581 pp., 6,414,052 chars, last-modified 22 Dec 2025 |
| https://www.legis.iowa.gov/law/hyperlinkDownloads | script grep | Word template only; no bulk data |
| https://www.legis.iowa.gov/docs/publications/iactc/91.2/CH1150.pdf | script | "CHAPTER 1150 CIVIL ACTIONS"; S.F. 512 |
| …/iactc/87.1/CH0064.pdf, …/87.1/CH64.pdf | script | both 200, same file; "CHAPTER 64 IMPROVEMENTS TO REAL PROPERTY" |
| https://www.legis.iowa.gov/law/statutory/acts/actsChapter | script links | 403 links; 91.2/CH1001.pdf … |
| https://law.justia.com/codes/iowa/2016/title-xv/ | WF | "There Is a Newer Version"; editions 2025, 2024, 2023, 2016 |
| https://law.justia.com/codes/iowa/title-xv/ | WF | "2025 Iowa Code Title XV"; chapter links, no section ranges |
| https://law.justia.com/codes/iowa/title-xv/chapter-614/ | WF | section links incl. section-614-4a |
| …/title-xv/chapter-614/section-614-1/ | WF | YES; "IA Code § 614.1 (2025)" |
| …/title-xvi/chapter-707/section-707-2/ | WF (built URL, passed) | YES "A person commits murder in the first degree when the" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.legis.iowa.gov/law/statutory/constitution | script | "codified Iowa Constitution is an official legal publication"; links ICP/1518288.pdf |
| https://www.legis.iowa.gov/docs/publications/ICP/1518288.pdf | script | 27 pp., 105,512 chars; art. I § 8 present; Amendment 51 (2024) |
| same | WF | art. XII § 1 present; last body art. XII § 2; not truncated |
| https://law.justia.com/constitution/iowa/article-i/ | WF | section titles only; links section-8, section-1a |
| https://law.justia.com/constitution/iowa/article-i/section-1a/ | WF | YES "The right of the people to keep and bear arms" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.legis.iowa.gov/law/courtRules | script links | → /law/courtRules/courtRulesListings |
| …/law/courtRules/courtRulesListings | script | "Iowa Court Rules - September 2026"; "(Official Edition)"; dated links 09-30-2026.chapter.N.pdf |
| …/docs/ACO/CR/LINC/09-30-2026.chapter.{1,5,6,32}.pdf | script info | 424,571 / 78,862 / 199,325 / 406,602 chars |
| …/docs/ACO/CourtRulesChapter/{1,5,32}.pdf | script | sha256 identical to dated files |
| …/docs/ACO/CR/LINC/chapter.1.pdf | script | redirects to /docs/ACO/CourtRulesChapter/1.pdf |
| …/docs/ACO/CourtRules/1.421.pdf, 5.702.pdf | script | HTTP 404 (no per-rule files) |
| …/09-30-2026.FullCourtRules.pdf | script | 1,271 pp., 2,846,576 chars |
| CourtRulesChapter/5.pdf, 1.pdf, 6.pdf, 32.pdf | script grep | Rule 5.702, 1.421, 6.1103, 32:1.7 body headings found |
| …/09-30-2026.chapter.5.pdf | WF | YES 5.702; ends at Rule 5.1103; header "December 2022 EVIDENCE Ch 5, p.1" |
| …/09-30-2026.chapter.1.pdf | WF | Rule 1.981 NOT PRESENT; stops at Rule 1.308; "[Content truncated due to length...]" |

## D — Administrative code and bulletin
| URL | Tool | Result |
|---|---|---|
| https://www.legis.iowa.gov/law/administrativeRules | script links | IAC agencies, bulletin listing, rules.iowa.gov via /leaving |
| …/law/administrativeRules/agencies | script | "Iowa Administrative Code - 10/14/2026 (Official Edition)" |
| …/law/administrativeRules/chapters?agency=641 | script links | 10-14-2026.641.1.pdf … |
| …/docs/iac/chapter/10-14-2026.641.1.pdf and /641.1.pdf | script | identical sha256; 16 pp.; header "IAC 6/10/26 Public Health[641]" |
| …/docs/iac/rule/641.1.1.pdf | script | 2 pp.; "641—1.1(139A) Definitions." |
| …/docs/iac/chapter/10-14-2026.701.400.pdf | script | 295-char stub (chapter heading only) |
| …/docs/iac/chapter/567.61.pdf | script | 24 pp.; "CHAPTER 61 WATER QUALITY STANDARDS"; "IAC 2/5/25" |
| …/docs/aco/bulletin/10-14-2026.pdf | script | 235 pp., 818,460 chars; "VOLUME XLIX NUMBER 8 October 14, 2026" |
| …/docs/aco/bulletin/09-30-2026.pdf | script | 423 pp. |
| …/docs/aco/arc/0647D.pdf | script | 2 pp.; "ARC 0647D EDUCATION DEPARTMENT[281] Notice of Intended Action" |
| https://rules.iowa.gov/ | script | navigation ("Track Proposed Rules"); no rule text |
| https://www.law.cornell.edu/regulations/iowa | script links | agency list |
| …/regulations/iowa/agency-641/chapter-1 | script links | "Rule 641-1.1 - Definitions" → Iowa-Code-r-641-1.1 |
| …/regulations/iowa/Iowa-Code-r-641-1.1 | script | 8,018 chars; last-modified 01 Aug 2025; "ARC 8070C, IAB 6/12/24" |
| …/regulations/iowa/Iowa-Code-r-567-61.3 | script | 28,937 chars |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.iowacourts.gov/iowa-courts/supreme-court/supreme-court-opinions/ | script links | case/25-1183 → /courtcases/26518/embed/SupremeCourtOpinion |
| …/supreme-court-opinions/case/25-1183 | script | links briefs and "PDF of the Opinion" |
| https://www.iowacourts.gov/courtcases/26518/embed/SupremeCourtOpinion | script | 17 pp.; "Submitted September 9, 2026—Filed October 16, 2026" |
| …/court-of-appeals/court-of-appeals-court-opinions | script links, curl | latest day only ("Filed Oct 07, 2026"); only form is site search |
| https://www.iowacourts.gov/courtcases/27223/embed/CourtAppealsOpinion | script | 9 pp.; "No. 24-1358 Filed October 7, 2026" |
| …/supreme-court-opinions/archive/2021/3 | WF | 3 cases with links; "Page 1 of 2"; next /archive/2021/3/page/2 |
| …/court-of-appeals-court-opinions/archive/2021/3 | script links | case/19-0058 → /courtcases/12478/… |
| …/supreme-court-opinions/archive/2018/3 | script links | case/16-1684; irregular slug case/161218 |
| …/opinions-archive/opinions-archive-2013/ | script | case names and dockets as text; no per-opinion links found |
| https://www.iowacourts.gov/courtcases/8953/embed/SupremeCourtOpinion | WF | PROVENANCE_REQUIRED (not retried) |
| same | script | 19 pp.; "Filed March 26, 2021 Amended June 1, 2021" |
| …/supreme-court-opinions/case/18-2239 | WF | PROVENANCE_REQUIRED (not retried) |
| https://law.justia.com/cases/iowa/ | WF | Supreme Court and Court of Appeals links |
| https://law.justia.com/cases/iowa/court-of-appeals/ | WF | years 1977–2026; newest Oct. 7, 2026 (24-1358) |
| https://law.justia.com/cases/iowa/supreme-court/ | WF | years 1859–2026; newest shown June 30, 2026 (25-0443) |
| https://law.justia.com/cases/iowa/supreme-court/2021/ | WF | 18-2239.html; entries show dockets and dates |
| …/supreme-court/2021/18-2239.html | WF | YES; full opinion; no N.W.2d cite |
| …/court-of-appeals/2021/19-0058.html | WF (built URL, passed) | YES; "Filed March 17, 2021" |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.iowacourts.gov/announcements/supreme-court-issues-further-review-orders | script | 2018 announcement; links /iowa-courts/supreme-court/further-review-orders/ |
| https://www.iowacourts.gov/iowa-courts/supreme-court/further-review-orders/ | script | "further review status since our last report"; Granted 25-0461, 25-0562, 25-1345; Denied from 24-1440 |
| https://www.iowacourts.gov/courtcases/11098/embed/SupremeCourtOpinion | script | "On review from the Iowa Court of Appeals"; "COURT OF APPEALS DECISION VACATED" |
| …/court-of-appeals-court-opinions/case/19-1674 | script links | Application for Further Review; Resistance; COA and Supreme Court opinion PDFs |
| https://www.iowacourts.state.ia.us/ESAWebApp/SelectFrame | script | 90-char frameset "This page uses frames" |
| https://www.iowacourts.gov/iowa-courts/court-of-appeals/published-cases/ | script links | navigation links only |

## Searches (discovery only)
- "legis.iowa.gov docs code 614.1.pdf limitations of actions" → year-specific code PDFs
- "law.justia.com codes iowa title XV chapter 614 section 614.1" → Justia 2016 title page
- "law.justia.com constitution iowa article I section 8" → Justia article-i
- "\"legis.iowa.gov/docs/ACO/CourtRulesChapter\"" → listing TOCs, /DOCS/ACO/CR/LINC/chapter.633.pdf form
- "law.justia.com cases iowa supreme-court 2021 opinion" → iowacourts monthly archives
- "iowacourts.gov supreme court further review…" → further-review announcement
- "law.justia.com cases iowa court-of-appeals 2025 html" → Justia COA 2015 listing

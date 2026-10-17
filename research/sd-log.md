# South Dakota (sd) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "script" = `python3 scripts/fetch_doc.py --research` (obeys robots, bot checks, rate limits); "WF" = WebFetch. Quoted page text is 15 words or fewer per entry.

## Robots / host checks (script)
| URL | Result |
|---|---|
| https://sdlegislature.gov/robots.txt | 200; `User-agent: *`; Disallow only /Edge-logo.svg, /Firefox-logo., /chrome-logo.svg, /Unsupported.js, /pdfviewer, /PDFViewer; sitemaps /api/Documents/Index/Sitemap.xml, /Statutes.xml, /Rules.xml |
| https://mylrc.sdlegislature.gov/robots.txt | 200; `User-agent: *` `Disallow:` (empty) |
| https://ujs.sd.gov/robots.txt | 200; `User-agent: *` `Allow: /` |
| https://law.justia.com/robots.txt | REFUSED: "refused automated access earlier (robots.txt challenge, 2026-10-17T14:42:45)"; host off for the day |
| https://www.law.cornell.edu/robots.txt | 200 (cached); `User-agent: *`, Crawl-delay: 10 |
| https://sdsos.gov/robots.txt | 200; rules are `Disallow: /` blocks for named agents (uptimerobot, seekportbot, …) — not pursued |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://sdlegislature.gov/Statutes/22-18-1 | script | 200, 123 chars: "Your browser is not supported" (Vue app shell) |
| https://sdlegislature.gov/Statutes/19-15-9 (from WebSearch) | WF | NO — browser-unsupported message / app shell only |
| https://sdlegislature.gov/api/Statutes/22-18-1.html | script | 200, 1,843 chars; "A person is guilty of simple assault, a Class 1 misdemeanor"; Source note ends "SL 2021, ch 92, § 1" |
| https://sdlegislature.gov/api/Statutes/Statute/22-18-1 | script | 200 JSON (parents, Previous/Next, CatchLine, Html) |
| https://sdlegislature.gov/Statutes.xml | script | sitemap index → Statutes.1.xml, Statutes.2.xml (lastmod 2026-09-03) |
| https://sdlegislature.gov/Statutes.1.xml | script | 2,638,796 chars; lists /Constitution/… and /Statutes/… URLs incl. /Statutes/15-6-56(a) |
| https://sdlegislature.gov/api/Statutes/15-6-56.html | script | 200, 0 chars (bare rule number empty) |
| https://sdlegislature.gov/api/Statutes/53-1-1.html | script | 191 chars; "A contract is an agreement to do or not to do" |
| same | WF (built URL, no prompt) | YES, "A contract is an agreement to do or not to"; no currency; complete |
| https://sdlegislature.gov/api/Statutes/19-19-702.html | script | 922 chars; "A witness who is qualified as an expert by knowledge" |
| https://sdlegislature.gov/api/Statutes/22-18.html | script | 3,290 chars; chapter TOC "CHAPTER 22-18 ASSAULTS AND PERSONAL INJURIES" |
| https://sdlegislature.gov/api/Statutes/32-23-1.html | script | 1,413 chars; "No person may drive or be in actual physical control" |
| https://sdlegislature.gov/api/Statutes/15-6.html | script | 17,518 chars; grep finds 15-6-56(a)…(g), 15-6-12(a)…; links `Statutes?Statute=15-6-56(c)` |
| https://sdlegislature.gov/api/Statutes/15-6-56(c).html | script | 2,550 chars; "Unless different periods are fixed or permitted by order of the court" |
| https://sdlegislature.gov/api/Statutes/15-6-12(b).html | script | 1,804 chars; "Every defense, in law or fact, to a claim for relief" |
| https://sdlegislature.gov/api/Statutes/22.html | script | 2,084 chars; title TOC, chapters without section ranges |
| https://sdlegislature.gov/api/Statutes/22-18.html?all=true | script | 21,832 chars; all chapter sections |
| https://sdlegislature.gov/js/app.84949f1c.js, /js/chunk-10b1f980.d5c86bd7.js | script | SPA bundle; endpoints read: /api/Statutes/Statute/, /api/Statutes/Constitution/, /api/Statutes/LastStatuesEffectiveDate, /api/Rules/, /api/SessionLaws/… |
| https://sdlegislature.gov/api/Statutes/LastStatuesEffectiveDate | script | `"2026-09-03T00:00:00-05:00"` |
| https://sdlegislature.gov/api/Statutes/2-16.html, 2-16-12.html, 2-16-13.html, 2-16-13.1.html | script | 2-16-13 "Publications constituting official code"; official code = printed revised volumes; 2-16-13.1 excludes appendices incl. Rules of Professional Conduct |
| https://sdlegislature.gov/api/Sessions | script | JSON; SessionId 44 = 2021, 70 = 2025, 71 = 2026 |
| https://sdlegislature.gov/api/SessionLaws/ChapterToId/92?SessionId=44 | script | `7285` |
| https://sdlegislature.gov/api/SessionLaws/71 | script | 94,209 chars JSON list of 2026 chapters |
| https://sdlegislature.gov/api/SessionLaws/SessionLaw/7285 | script | 2,496 chars; "An Act to increase the enhanced penalty for the crime of simple assault." |
| WebSearch "law.justia.com codes south-dakota title-22 chapter-18 section 22-18-1" | search | Justia year editions 2011–2021 |
| https://law.justia.com/codes/south-dakota/2021/ | WF | editions 2025, 2024, 2023, 2021; "There Is a Newer Version"; Title 22 URL /2021/title-22/ |
| https://law.justia.com/codes/south-dakota/title-22/chapter-18/section-22-18-1/ | WF | YES "A person is guilty of simple assault, a Class 1"; "2025 South Dakota Codified Laws"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/south-dakota/title-15/chapter-6/section-15-6-56-c/ | WF | CLIENT_ERROR "error while fetching" (unpadded chapter) |
| https://law.justia.com/codes/south-dakota/title-15/chapter-6/ | WF | CLIENT_ERROR |
| https://law.justia.com/codes/south-dakota/title-53/chapter-1/section-53-1-1/ | WF | CLIENT_ERROR |
| https://law.justia.com/codes/south-dakota/2025/ | WF | heading "2025 South Dakota Codified Laws"; Title 15 → /codes/south-dakota/title-15/ |
| https://law.justia.com/codes/south-dakota/title-15/ | WF | Chapter 06 → /title-15/chapter-06/; no section ranges in labels |
| https://law.justia.com/codes/south-dakota/title-15/chapter-06/ | WF | links /section-15-6-56-c/, /section-15-6-12-b/; subsections listed individually |
| https://law.justia.com/codes/south-dakota/title-15/chapter-06/section-15-6-56-c/ | WF | YES "Unless different periods are fixed or permitted by order of"; "2025 South Dakota Codified Laws" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://sdlegislature.gov/api/Statutes/Constitution.html | script | 404 |
| https://sdlegislature.gov/api/Constitution/6-2(.html) | script | 123 chars, SPA "Your browser is not supported" |
| https://sdlegislature.gov/api/Statutes/Constitution/6-2 | script | 200 JSON, key "0N-6-2", CatchLine "Due process--Right to work."; Html field whitespace only |
| https://sdlegislature.gov/api/Statutes/0N-6-2.html (+?all=true), 0N-6.html, 0N.html | script | 200, 0 chars |
| https://sdlegislature.gov/api/Statutes/Constitution | script | 6,292 chars JSON article list (0N-Preamble, 0N-1 …) |
| https://sdlegislature.gov/api/Statutes/Constitution/6 | script | JSON, Html empty |
| WebSearch "South Dakota Constitution full text PDF sdlegislature.gov article VI section 2…" | search | found /api/Statutes/Constitution/0N-6.html, sdsos.gov PDFs |
| https://sdlegislature.gov/api/Statutes/Constitution/0N-6.html, 0N-6-2.html (+?all=true) | script | 200, 10,567 / 1,788 bytes, but 0 chars extracted; raw bytes start with doubled `<HTML><HEAD>` and hold the text |
| https://sdlegislature.gov/api/Statutes/Constitution/0N-6-2.html | WF | YES "No person shall be deprived of life, liberty or property"; history "Amendment proposed by SL 1945, ch 315"; complete |
| https://sdlegislature.gov/api/Statutes/Constitution/0N-5-1.html | WF | YES "The judicial power of the state is vested in a" |
| https://sdsos.gov/2025 South Dakota Constitution 20250919.pdf | script | HTTP 404 |
| https://www.sdsos.gov/2023SouthDakotaConstitution20220124.pdf | script | HTTP 404 |
| https://law.justia.com/constitution/south-dakota/ | WF | article pages, e.g. /article-6/; "Constitution may not be the most recent version." |
| https://law.justia.com/constitution/south-dakota/article-6/ | WF | section 2 body NOT PRESENT (headings only); section URL /article-6/section-2/ |
| https://law.justia.com/constitution/south-dakota/article-6/section-2/ | WF | YES "No person shall be deprived of life, liberty or property" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://sdlegislature.gov/api/Statutes/15-26A-60.html | script | 3,866 chars; "15-26A-60. Brief of appellant--Contents." |
| https://sdlegislature.gov/api/Statutes/23A-8-3.html | script | 991 chars; "(Rule 12(b)) Defenses and objections raised by motion" |
| https://sdlegislature.gov/api/Statutes/15-26A.html | script | TOC incl. 15-26A-69.1 "Citation of official opinions of the Supreme Court" |
| https://sdlegislature.gov/api/Statutes/15-26A-69.1.html | script | 1,649 chars; on/after Jan. 1, 1996: year, "S.D.", clerk number; pinpoint by paragraph |
| https://sdlegislature.gov/api/Statutes/15-26A-87.1.html | script | summary dispositions "shall not be cited or relied upon as authority" |
| https://sdlegislature.gov/api/Statutes/16-18.html | script | 4,304 chars; last link Statute=16-18-A |
| https://sdlegislature.gov/api/Statutes/16-18-A.html | script | 119,723 chars; grep "Rule 1.7. Conflict of Interest: Current Clients" at offset 28,649 |
| same | WF | truncated: 100,000 of 118,646 chars; last body Rule 7.2(d); Rule 8.4 NOT PRESENT |
| https://ujs.sd.gov/supreme-court/published-rules/ | script | page text "0 of 0", "No Results Found" (default view) |
| https://ujs.sd.gov/supreme-court/published-rules/?year=2025&archive=true | script links | 10 PDFs; "ADOPTION OF NEW RULES AT SDCL 16-3-5.3" → /media/4rxprw2v/scrule_rsrc_20250305135006.pdf |
| https://ujs.sd.gov/supreme-court/published-rules/?archive=true | script links | rule2608.pdf, correctedrule2606.pdf … |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://sdlegislature.gov/api/Rules/Rule/20:10:01:01.html | script | 573 chars; "20:10:01:01. Sessions of commission." |
| https://sdlegislature.gov/api/Rules/Rule/20:10:01.html | script | 4,149 chars; "CHAPTER 20:10:01 GENERAL RULES OF PRACTICE" |
| https://sdlegislature.gov/api/Rules/Rule/67:16:01:01.html | script | 4,869 chars; "Terms used in this article mean:" |
| same | WF (built URL, no prompt) | YES "Terms used in this article mean: (1) "Allowable costs," expenses"; source "44 SDR 94, effective December 4, 2017." |
| https://sdlegislature.gov/api/Rules/Rule/74:51:01:01.html | script | 11,684 chars; "Terms defined in SDCL 34A-2-2, have the same meaning" |
| https://sdlegislature.gov/api/Rules/20:10:01 | script | 70,073 chars JSON (RuleNumber, Html) |
| https://sdlegislature.gov/api/Documents/DocumentType?Type=53 | script | 36.8M chars JSON of "Guest Register" attachments — wrong type, not used |
| https://sdlegislature.gov/api/Documents/DocumentTypesRSS?Type=50 | script | 161,207 chars RSS "Register"; items https://mylrc.sdlegislature.gov/api/Documents/{id}.pdf |
| https://mylrc.sdlegislature.gov/api/Documents/210727.pdf (id from JS bundle) | script | pdftotext failed (exit 1) |
| https://mylrc.sdlegislature.gov/api/Documents/308375.pdf | script | PDF 3 pp, 8,568 chars; "SOUTH DAKOTA REGISTER Published weekly by the Legislative Research Council"; "Volume 53 … October 13, 2026" |
| https://www.law.cornell.edu/states/south_dakota | script links | links out to sdlegislature.gov and ujs.sd.gov (old .aspx URLs); /regulations/south-dakota |
| https://www.law.cornell.edu/regulations/south-dakota (→ title-67 → article-67-16 → chapter-67-16-01) | script links | ARSD-67-16-01-01 |
| https://www.law.cornell.edu/regulations/south-dakota/ARSD-67-16-01-01 | script | 6,176 chars; "Terms used in this article mean: (1) "Allowable costs," those expenses"; Last-Modified Aug 6 2025 |
| https://www.law.cornell.edu/regulations/south-dakota/ARSD-74-51-01-01 | script verify | NOT VERIFIED for LRC wording; LII reads "Words and phrases defined in SDCL 34A-2-2" (older text) |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://ujs.sd.gov/ | script | 14,476 chars, nav |
| https://ujs.sd.gov/Supreme_Court/opinions.aspx | script | redirect → /supreme-court/opinions/ |
| https://ujs.sd.gov/supreme-court/opinions/ | script | text extractor drops listing table; raw HTML: "Showing 1-10 of 29", "10/7/2026 BIALOTA v. LAKOTA LAKES, LLC, 2026 S.D. 52"; form GET fields keywords, year (2006–2026), archive |
| same | script links | 10 PDFs /media/{random}/{docket}.pdf; paging ?archive=false&page=N; RSS ?rss=1 |
| https://ujs.sd.gov/supreme-court/opinions/?keywords=Lucero&year=2026 | script links | 1: "STATE v. LUCERO, 2026 S.D. 48" → /media/xw4fesw2/31307.pdf |
| …/opinions/?keywords=&year=2010&archive=true | script links | 10, "[Archive] STATE V. REED, 2010 S.D. 105" → /media/sg0ntxzo/25626.pdf |
| …/opinions/?year=2006&archive=true | script links | "KRAFT V. MEADE CO., 2006 SD 113"; "Showing 1-10 of 113" |
| …/opinions/?archive=true&year= | script links | 2026 archived items |
| …/opinions/?keywords=31307 | script links | 0 (docket not searchable) |
| …/opinions/?keywords=2010+S.D.+105&archive=true | script links | unfiltered 2026 rows (citation not searchable) |
| …/opinions/?keywords=Reed&year=2010&archive=true | script links | 2: 2010 S.D. 105, 2010 SD 66 |
| …/opinions/?keywords=Reed&archive=true | script | "Showing 1-4 of 4" |
| …/opinions/?year=1996&archive=true | script links | 0 |
| https://ujs.sd.gov/media/xw4fesw2/31307.pdf | script | PDF 8 pp, 13,176 chars; "#31307-a-SPM 2026 S.D. 48"; "[¶1.] Jeremy Lucero pled guilty to possession of" |
| same | WF | PROVENANCE_REQUIRED (permission not answered) |
| https://ujs.sd.gov/media/sg0ntxzo/25626.pdf | script | PDF 10 pp, 18,079 chars; "[¶1.] Stanley Reed (Reed) filed a petition for writ of habeas" |
| https://ujs.sd.gov/supreme-court/opinions/ | WF | PROVENANCE_REQUIRED |
| WebSearch "ujs.sd.gov supreme court opinion 2025 S.D. pdf" | search | https://ujs.sd.gov/supreme-court/opinions, ?page=N, summary-dispositions |
| https://ujs.sd.gov/supreme-court/opinions (from search) | WF | rows "BIALOTA v. LAKOTA LAKES, LLC, 2026 S.D. 52" → /media/zhkot2me/31286.pdf; year filter 2026–2006 |
| https://ujs.sd.gov/media/zhkot2me/31286.pdf | WF | PROVENANCE_REQUIRED |
| same | script | PDF 13 pp, 24,160 chars; "[¶1.] Emily Bialota brought a quiet title action" |
| https://ujs.sd.gov/supreme-court/summary-dispositions/ | script links | "Interest of E.L.W., H.L.W., H.L.W." → /media/hvflyt3r/31521oadacomp.pdf; "Showing 1-10 of 33"; year filter 2022–2026 |
| https://ujs.sd.gov/cases-and-records/court-records-search/ | script | nav page; ecourts.sd.gov links to Account/Login.aspx |
| WebSearch "law.justia.com cases south-dakota supreme-court 2025" | search | UJS term-of-court pages only |
| https://law.justia.com/cases/south-dakota/supreme-court/2026/31307.html | WF | YES State v. Lucero, 2026 S.D. 48; "Jeremy Lucero pled guilty to possession of a controlled substance,"; through ¶15 |
| https://law.justia.com/cases/south-dakota/supreme-court/2010/25626.html | WF | YES State v. Reed, 2010 S.D. 105; "Stanley Reed (Reed) filed a petition for writ of habeas" |
| https://law.justia.com/cases/south-dakota/supreme-court/ | WF | years 2026 (46 opinions) back to 1894 (1 opinion); then 1899, 1908 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| WebSearch 'supremecourt.gov docket "Supreme Court of South Dakota" petition denied 2025' | search | 25-7600, 24A614, 25-276, 24-1081, 25A1 |
| https://www.supremecourt.gov/docket/docketfiles/html/public/25-7600.html | script grep | "Lower Ct: Supreme Court of South Dakota"; "Case Numbers: (31006, 31007)"; "Oct 05 2026 Petition DENIED." |
| …/24A614.html | script grep | "Lower Ct: Supreme Court of South Dakota"; "Case Numbers: (30448-a-SRJ)" |
| …/25-276.html, 24-1081.html, 25A1.html | script grep | lower courts 8th Cir. / 4th Cir. — not SD |

## Notes
- WebFetch calls used: 25 (3 PROVENANCE_REQUIRED, 3 CLIENT_ERROR on Justia built URLs). No quota or rate failures.
- `build.py --check`: clean for sd.json. `--cross`: SD-only harness (all SD examples vs all other regexes, and all other examples vs SD's non-context regexes) found 0 hits; the full `--cross` run takes several minutes on the shared data set.

# Colorado (co) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET/HEAD from this workspace (robots files, link lists, HEAD on zips; never used after a refusal). Quoted text is 15 words or fewer. WebFetch calls: 44 of about 55. Ten were not sent because the session's permission prompt timed out ("PROVENANCE_REQUIRED … not answered in time"). That is a gate in this session, not a refusal by the site, so these hosts are recorded as `untested` for WebFetch. There were no quota or rate failures.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://leg.colorado.gov/robots.txt | script | 200; `*` disallows /admin/, /rails/ …, **/laws/session-laws/*/download**, /bill_files/*/download; Allow / |
| https://content.leg.colorado.gov/robots.txt | curl | 200; Drupal default (/core/, /profiles/ …) |
| https://olls.info/robots.txt | curl | 200; `*` Disallow /crs-archive/ only |
| https://colorado.public.law/robots.txt | curl | 200; disallows /admin, /api, /data, /demo, /images, /users |
| https://www.coloradojudicial.gov/robots.txt | curl | 200; Drupal default |
| https://research.coloradojudicial.gov/robots.txt | curl | 404 "Cannot GET /robots.txt" |
| https://www.sos.state.co.us/robots.txt | curl | 200; `*` disallows /CCR/KeywordSearch.do, /CCR/Rule.do, /CCR/NumericalSubDocList.do, /apps/, /biz/… |
| https://advance.lexis.com/container?config=0123JAAy… | script check | OK, robots permits |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| https://leg.colorado.gov/colorado-revised-statutes (→ /laws/colorado-revised-statutes) | script, curl | 200, 4,009 chars; "access the Colorado Revised Statutes hosted by LexisNexis"; link lexisnexis.com/hottopics/colorado |
| https://leg.colorado.gov/agencies/office-legislative-legal-services/2025-crs-titles-download | script | 404 |
| https://content.leg.colorado.gov/agencies/office-of-legislative-legal-services | curl | 200; links to revisor page and Lexis hottopics |
| https://content.leg.colorado.gov/agencies/office-legislative-legal-services/revisor-statutes | script, curl | 200; gray-book PDFs only |
| http://www.lexisnexis.com/hottopics/colorado/ | script | 200 → advance.lexis.com, kind=html chars=0 (JS shell) |
| https://advance.lexis.com/container?config=0123JAAy… | WF | "web page content you provided is empty" |
| https://colorado.public.law/statutes/crs_13-80-102 | script | 200, 6,688 chars, body present; Source crs2024-title-13.pdf |
| https://colorado.public.law/statutes/crs_18-1-105 | script | 404 |
| https://colorado.public.law/statutes | script | 200; "Current through Fall 2025" |
| https://{leg,content.leg}.colorado.gov/sites/default/files/images/olls/crs2025-title-13.pdf | curl HEAD | 301 → content.leg…, then 404 |
| …/images/olls/crs2024-title-13.pdf | curl HEAD | 301 → content.leg.colorado.gov, 200 application/pdf |
| WebSearch "crs2025-title" | WebSearch | found 2025 and **2026** CRS titles download pages |
| https://content.leg.colorado.gov/agencies/office-legislative-legal-services/2026-crs-titles-download | curl, script | 200; links olls.info/crs/crs2026-title-{00..44}.{htm,pdf,docx}, index, 3 zips; "Current with the changes made by amendments, additions, and repeals…" |
| same | WF | same links and currency line; "no explicit official or unofficial disclaimer" |
| https://olls.info/crs/crs2026-title-13.htm | script | 200 html, 4,639,324 chars, last-modified 2 Oct 2026; verify "…must be commenced within two years" VERIFIED; § shown as U+FFFD (windows-1252) |
| https://olls.info/crs/crs2026-title-13.pdf | script | 1,769 pp, 5,794,576 chars; same quote VERIFIED p. 1436; p. 1 header "Colorado Revised Statutes 2026"; TOC shows article section ranges |
| https://olls.info/crs/crs2026-title-18.htm | script | grep "18-3-102. Murder in the first degree. (1)" 1 match |
| https://olls.info/crs/crs2026-title-25.5.pdf | script | 765 pp |
| https://olls.info/crs/crs2026-title-24.pdf | script | 4,892 pp, 13.7M chars; art. 71.5 = UELMA (L. 2012, HB 12-1209) |
| olls.info/crs/crs2026-{htm,pdf,docx}.zip | curl HEAD | 200 application/zip; 37.3 MB / 184.3 MB / 47.9 MB |
| https://olls.info/crs/crs2026-title-13.pdf, -13.htm, -00.pdf | WF | not sent (permission prompt timed out) |
| https://colorado.public.law/statutes/crs_13-80-102 | WF | not sent (permission prompt timed out) |
| https://colorado.public.law/statutes/crs_13-51-101 | WF | YES "This article shall be known and may be cited as"; "Current through Fall 2025" |
| https://colorado.public.law/statutes/crs_18-3-102 | script | verify "After deliberation and with the intent to cause the death…" VERIFIED |
| https://law.justia.com/codes/colorado/title-13/ | WF | "2025 Colorado Revised Statutes"; divisions with article ranges, no section ranges |
| …/title-13/limitation-of-actions/article-80/part-1/section-13-80-102/ | WF | fetch error (wrong level) |
| …/title-13/limitation-of-actions/ | WF | Article 80 link (§§ 13-80-101 - 13-80-105.5) |
| …/title-13/limitation-of-actions/article-80/ | WF | section links, no part level; 13-80-102.5 → section-13-80-102-5 |
| …/article-80/section-13-80-102/ | WF | YES "The following civil actions, regardless of the theory upon which"; not truncated |
| https://law.justia.com/codes/colorado/title-18/article-3/part-1/section-18-3-102/ | WF | YES "A person commits the crime of murder in the first" |
| same Justia URL | script | REFUSED (law.justia.com robots/challenge) |
| https://leg.colorado.gov/laws/session-laws | curl | 200; links /laws/session-laws/HB26-1001/8/download … (robots-disallowed; not fetched) |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| https://leg.colorado.gov/laws/colorado-appellate-court-opinions | script | "Pursuant to 13-2-122 C.R.S., every opinion … is published online"; link research.coloradojudicial.gov |
| https://research.coloradojudicial.gov/ | curl, script | 200, vLex SPA shell, 0 chars of text |
| https://research.coloradojudicial.gov/search?q=Jargowsky | curl, script | 404 |
| https://research.coloradojudicial.gov/ | WF | not sent (permission prompt timed out) |
| https://www.coloradojudicial.gov/ | script | 200, 10,384 chars (cached page) |
| https://www.coloradojudicial.gov/supreme-court/case-announcements, /supreme-court, /court-appeals | curl, script | 403 "160.79.106.128 has been banned up to Sat, 17 Oct 2026 16:31:12"; script REFUSED for the day |
| https://www.coloradojudicial.gov/es/node/47 | WF | "Supreme Court Case Announcements"; weekly PDFs; year facet 2021-2026; ?page=N |
| https://www.coloradojudicial.gov/supreme-court/opinions | WF | not sent (permission prompt timed out) |
| https://www.coloradojudicial.gov/sites/default/files/2026-09/9.28.26.pdf | WF | "COLORADO SUPREME COURT CASE ANNOUNCEMENTS"; cert denials, e.g. 26SC380 / COA 23CA1830 |
| https://www.coloradojudicial.gov/sites/default/files/2026-09/09-03-26.pdf | WF | COA announcements, "2026 COA 66" 24CA1018; "NOT PUBLISHED PURSUANT TO C.A.R. 35(e)"; 15 pp; no URLs |
| https://www.coloradojudicial.gov/sites/default/files/2025-06/06.30.25.pdf | WF | list only; "2025 CO 47" 24SA148; "Click on the public domain citation to view the opinion" |
| https://www.coloradojudicial.gov/node/18098 | WF | one file link (10.12.26.pdf); no opinion list |
| https://cl.cobar.org/features/colorados-unpublished-opinion-database/ | WF | discovery only: research.coloradojudicial.gov covers opinions "dating back to 1864", unpublished COA included |
| https://law.justia.com/cases/colorado/supreme-court/2025/ | WF | docket slugs (24sa276.html, 25sc679.html, 24sc207-0.html) |
| https://law.justia.com/cases/colorado/supreme-court/2025/23sc847.html | WF | full text ¶¶ 1-59, "2025 CO 63" |
| https://law.justia.com/cases/colorado/court-of-appeals/2026/24ca1018.html | WF | full text ¶¶ 1-69, "2026 COA 66" |
| https://law.justia.com/cases/colorado/court-of-appeals/2026/ | WF | "Opinions 1 - 500 of 1049"; includes 23CA0715 (unpublished) |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| https://leg.colorado.gov/laws/colorado-constitution | script | "Access the Colorado Constitution hosted by LexisNexis" |
| https://olls.info/crs/crs2026-title-00.pdf | script | 1,578 pp; art. II § 25 quote VERIFIED p. 566 |
| https://olls.info/crs/crs2026-title-00.htm | script | 4,643,814 chars; TOC "CONSTITUTION OF THE STATE OF COLORADO" |
| https://law.justia.com/constitution/colorado/ | WF | index only, art. II § 25 NOT PRESENT; links cnart1.html, cnart2.html |
| https://law.justia.com/constitution/colorado/cnart2.html | WF | YES "No person shall be deprived of life, liberty or property," |
| https://colorado.public.law/constitution | script | 404 |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://colorado.public.law/court_rules, /rules, /regulations | script | 404 |
| https://www.coloradojudicial.gov/sites/default/files/2026-04/Rule%20Change%202026%2811%29.pdf | WF | "RULE CHANGE 2026(11)", C.R.C.P. 1 and 16.2; "effective immediately" |
| https://coloradojudicial.gov/media/12394 | WF | "RULE CHANGE 2015(05)"; C.R.C.P. 12(b) present; truncated in Rule 37(a)(4) |
| https://www.coloradojudicial.gov/node/1512 | WF | "RULE CHANGE 2014-12" (Crim. P. 49.5); PDF link only |
| https://www.coloradojudicial.gov/node/1677 | WF | "RULE CHANGE 2012-13"; no Lexis links |

## D: Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://www.sos.state.co.us/CCR/Welcome.do, /CCR/NumericalDeptList.do, NumericalCCRDocList.do | script, curl | HTTP 500 "Service Unavailable" page |
| https://www.coloradosos.gov/CCR/Welcome.do | curl | HTTP 500 same |
| https://www.sos.state.co.us/CCR/Welcome.do | WF | not sent (permission prompt timed out) |
| https://coloradosos.gov/pubs/CCR/FAQs.html | WF | SOS "publishes the official Code and Register online"; Register on 10th and 25th |
| https://www.coloradosos.gov/CCR/NumericalDeptList.do, /CCR/RegisterHome.do | WF | not sent (permission prompt timed out) |
| https://www.sos.state.co.us/CCR/NumericalAgencyList.do?deptID=11 | WF | "Official Publication of the State Administrative Rules (24-4-103(11)"; no link URLs |
| https://www.law.cornell.edu/regulations/colorado | script, curl | 200; department list; drilled to 8-CCR-1505-1-{n} |
| https://www.law.cornell.edu/regulations/colorado/8-CCR-1505-1-2 | script | 20,297 chars; body present; last note "47 CR 19, October 10, 2024"; last-modified 31 Jul 2025 |
| same | WF | YES "An applicant may submit a properly executed voter registration form" |
| https://www.law.cornell.edu/regulations/colorado/1-CCR-101-1 | script | returns top index (same hash), not 404 |

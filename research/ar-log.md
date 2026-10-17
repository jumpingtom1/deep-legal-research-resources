# Arkansas (ar) probe log — 2026-10-17

Tools: S = `scripts/fetch_doc.py --research`, W = WebFetch, WS = WebSearch. All dates 2026-10-17.

## Robots
| URL | Tool | Result |
|---|---|---|
| https://www.arkleg.state.ar.us/robots.txt | S | 200; `User-agent: * Allow: /`; ChatGPT agents disallowed |
| https://codeofarrules.arkansas.gov/robots.txt | S | 200; same file as arkleg |
| https://opinions.arcourts.gov/robots.txt | S | 200; * disallows 4 specific item/document URLs; BUbiNG `/` |
| https://www.arcourts.gov/robots.txt | S | 200; Drupal default (admin, search, user paths) |
| https://www.sos.arkansas.gov/robots.txt | S | 200; * Crawl-delay 5; `Disallow: /rules_and_regs/` |
| https://advance.lexis.com/robots.txt | S | 404 |
| https://www.lexisnexis.com/robots.txt | S | 200 (cached); nothing covering /hottopics/ |
| https://law.justia.com/codes/arkansas/ | S | REFUSED: host off for the day (robots.txt challenge seen earlier) |

## A — statutes
| URL | Tool | Result |
|---|---|---|
| https://arkleg.state.ar.us/ | S | 200, 17,723 chars; raw HTML links "Arkansas Code and Constitution of 1874" → lexisnexis.com/hottopics/arcode/ |
| http://www.lexisnexis.com/hottopics/arcode/ | S | redirect to advance.lexis.com/container?config=00JAA3ZT…; kind=html chars=0 |
| https://law.justia.com/codes/arkansas/ | W | editions 2010–2025 listed; no currency statement |
| https://law.justia.com/codes/arkansas/2025/ | W | title links (undated /title-N/); "These codes may not be the most recent version." |
| https://law.justia.com/codes/arkansas/title-16/ | W | 7 subtitles, "2025 Arkansas Code", no chapter ranges |
| …/title-16/subtitle-5/ | W | chapter links, no section ranges |
| …/subtitle-5/chapter-56/ | W | subchapter 1 "§§ 16-56-101 to 16-56-130", subchapter 2 |
| …/chapter-56/subchapter-1/section-16-56-105/ | W | YES "The following actions shall be commenced within three (3) years"; not truncated |
| https://law.justia.com/codes/arkansas/title-5/subtitle-2/chapter-10/subchapter-1/section-5-10-102/ | W | YES "(a) A person commits murder in the first degree if:" |
| https://arkleg.state.ar.us/Acts/SearchByRange | S | 200; PDF links /Acts/FTPDocument?path=%2FACTS%2F2026F%2FPublic%2F&file=N.pdf |
| …/Acts/FTPDocument?…2026F…file=1.pdf | S | redirect → /Home/FTPDocument?path=%2FACTS%2F2026F%2FPublic%2FACT1.pdf; pdf 4 pp |
| …ACTS%2F2025R…ACT100.pdf | S | pdf 2 pp, "Regular Session, 2025 SENATE BILL 146" |
| …ACTS%2F2021R…ACT276.pdf | S | pdf 3 pp, "Act 276 of the Regular Session" |

## B — constitution
| URL | Tool | Result |
|---|---|---|
| WS "Arkansas Constitution of 1874 PDF sos.arkansas.gov" | WS | ssl-sos-site.ark.org/uploads/education/ArkansasConstitution1874.pdf |
| https://www.sos.arkansas.gov/uploads/education/ArkansasConstitution1874.pdf | S | HTTP 404 |
| https://www.sos.arkansas.gov/education/arkansas-constitution | S | HTTP 404 |
| https://ssl-sos-site.ark.org/uploads/education/ArkansasConstitution1874.pdf | S | robots unreachable: proxy CONNECT 502 (twice) |
| same | W | YES art. 2 § 13 "Every person is entitled to a certain remedy in the"; 125,699 chars, truncated at Art. 5 § 30 |
| https://www.sos.arkansas.gov/education/students-educators | S | 200, no constitution link |
| https://law.justia.com/constitution/arkansas/article-2/ | W | index only (NOT PRESENT); "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/arkansas/article-2/section-13/ | W | YES "Every person is entitled to a certain remedy in the" |

## C — court rules
| URL | Tool | Result |
|---|---|---|
| https://www.arcourts.gov/ | S | 200; "Court Rules" → opinions.arcourts.gov/ark/cr/en/nav_date.do |
| https://opinions.arcourts.gov/ark/cr/en/nav_date.do?iframe=true | S | 200; 23 rule sets (Civ. P. 16712, Evid. 1876, App. P.–Civ. 1885, App. P.–Crim. 1884, Sup. Ct. & Ct. App. 1871 …) |
| …/ark/cr/en/item/16712/index.do?iframe=true | S | 200, 808 chars; "Rule Current To 10/01/2026" |
| …/ark/cr/en/item/1876/index.do?iframe=true | S | "Rule Current To 06/04/2026" |
| …/ark/cr/en/16712/1/document.do | S | REFUSED HTTP 403 |
| same | W | gated: permission prompt timed out |
| WS "opinions.arcourts.gov cr 1876 document.do…" | WS | …/ark/cr/en/1876/1/document.do |
| https://opinions.arcourts.gov/ark/cr/en/1876/1/document.do | W | YES Rule 702 "If scientific, technical, or other specialized knowledge will assist the"; Rules 101–1102, not truncated |

## D — admin code and register
| URL | Tool | Result |
|---|---|---|
| https://codeofarrules.arkansas.gov/ | S | 200; footer: official version under § 25-15-218; "Last Updated: 10/12/2026 5:18:46 AM" |
| /Rules/RuleQuickSearch?titleNumber=2&… (all params) | S | redirect to title page |
| /Rules/RuleQuickSearch? title 2/20 + partNumber=1 | S | redirect to part pages |
| /Rules/RuleQuickSearch? with sectionNumber (101, 1-101, with/without part, subpart, chapter I) | S | "No rule found with the options entered" (6 variants) |
| NEXT walk title 2 → chapter 269 → … sectionID=54466 | S | "2 CAR § 1-101. Purpose." with body |
| …titleID=20…sectionID=18899 | S | "20 CAR § 1-101. Duties of State Registrar of Vital Records generally." |
| same | W | gated: permission prompt timed out |
| https://www.sos.arkansas.gov/rules-regulations/ | S | links: rules_and_regs search, CAR, bulk, Register |
| http://www.sos.arkansas.gov/rules_and_regs/index.php/rules/search/new | S check | REFUSED robots (Disallow: /rules_and_regs/) |
| https://www.sos.arkansas.gov/rules-regulations/bulk-data-download | S | INA subscription, $10 minimum per download |
| https://www.sos.arkansas.gov/rules-regulations/arkansas-register/ | S | monthly links 2025–2026 |
| http://www.sos.arkansas.gov/uploads/September_2026_Register_Report.pdf | S | pdf 4 pp "Volume 51 Number 9 September 2026" |
| https://www.sos.arkansas.gov/uploads/rulesRegs/Arkansas%20Register/2011/August11Reg/0811.pdf | S | pdf 10 pp "Volume XXXV, Number 2 August 2011" |
| same | W | error: session usage limit (quota, not a site refusal) |

## E — case law
| URL | Tool | Result |
|---|---|---|
| https://opinions.arcourts.gov/ | S | REFUSED HTTP 403 |
| https://opinions.arcourts.gov/ark/en/nav.do | S | 200, menu only; collections supremecourt, cr, ao |
| same | W | gated |
| …/ark/supremecourt/en/nav_date.do | S | 200, menu only (no listing) |
| …/ark/supremecourt/en/nav_date.do?iframe=true | S | 200; 50 links, latest 2026-10-15 |
| …/ark/supremecourt/en/{1837,1900,1950,2024}/nav_date.do?iframe=true | S | 200; 1837 lists 13 items (Hawkins vs. Carrington) |
| …/ark/supremecourt/en/2024/nav_date.do (no iframe) | S | menu only |
| …/ark/courtofappeals/en/nav_date.do?iframe=true | S | REFUSED 403 |
| …/ark/courtofappeals/en/2021/nav_date.do?iframe=true | S | REFUSED 403 |
| …/ark/supremecourt/en/264176/1/document.do | S | REFUSED 403 |
| same (from WS) | W | YES 304 Ark. 32 (1990), "Tom GLAZE, Justice. This is an appeal from the trial" |
| …/ark/supremecourt/en/524692/1/document.do | S | REFUSED 403 |
| …/ark/supremecourt/en/item/524692/index.do | S | 200, menu only |
| …/ark/courtofappeals/en/491562/1/document.do (WS) | W | CoA proceedings list Jan. 20, 2021 (no opinion) |
| …/courtofappeals/en/487231/1/document.do (WS) | W | CoA proceedings list Oct. 21, 2020 |
| …/courtofappeals/en/521918/1/document.do (WS) | W | CoA proceedings list May 10, 2023 |
| …/courtofappeals/en/item/491539/index.do | W | gated |
| …/courtofappeals/en/item/491539/index.do?iframe=true | S | 200, 23,436 chars; "Neutral Citation 2021 Ark. App. 21", CR-20-170; quote VERIFIED |
| …/supremecourt/en/item/523216/index.do?iframe=true | S | "2024 Ark. 181", CV-24-373, 12/12/2024 |
| …/ark/en/d/s/index.do?cont=&ref=2019+Ark.+123&… (no iframe) | S | 200, menu only |
| …/ark/supremecourt/en/d/s/index.do?… | S | 404 |
| …/ark/en/d/s/index.do?…ref=…&iframe=true (3 variants) | S | REFUSED 403 |
| …/ark/en/d/s/index.do?cont=%222019+Ark.+123%22&iframe=true | S | REFUSED 403 |
| …/ark/en/d/s/index.do?cont=Barrett&iframe=true | S | 200, 25 results |
| …/ark/en/d/s/index.do?cont=%22CR-20-170%22&iframe=true | S | 200, 4 results (opinion + 3 proceedings lists) |
| https://law.justia.com/cases/arkansas/ | W | Supreme Court and Court of Appeals links |
| https://law.justia.com/cases/arkansas/court-of-appeals/ | W | years 1979–2026 |
| https://law.justia.com/cases/arkansas/court-of-appeals/2026/cr-25-323.html | W | YES "Aechia Armstrong appeals from a Benton County Circuit Court sentencing"; 2026 Ark. App. 374 |
| https://cases.justia.com/arkansas/court-of-appeals/2026-cr-25-323.pdf?ts=1787757053 | S verify | VERIFIED |

## F — subsequent history
| URL | Tool | Result |
|---|---|---|
| …/ark/supremecourt/en/item/494454/index.do?iframe=true | S | "PROCEEDINGS OF MARCH 18, 2021 … REVIEWS DENIED … CR-20-170. Josh M. Barrett" |

## Notes
- WebFetch calls: 23 (5 gated, 1 quota error). After the quota error I made no more WebFetch calls.
- Bash was unavailable for a while (classifier timeout); work resumed after the coordinator's notice.
- `--check`: clean. `--cross`: one line: 'Arkansas Supreme Court Rule 5-2' matches the ks "Kansas Supreme Court Rules" pattern. That pattern needs the fix; the example stays.

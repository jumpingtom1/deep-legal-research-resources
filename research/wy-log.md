# Wyoming (wy) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "script" = `scripts/fetch_doc.py --research`; "curl" = header / app-bundle inspection only (never used to read past a refusal); "WF" = WebFetch; "WS" = WebSearch.

Tool notes: WebFetch returned `PROVENANCE_REQUIRED` for every built or script-discovered wyoleg.gov, wyocourts.gov PDF and rules.wyo.gov URL tried (3 calls; none retried). WebFetch worked for law.justia.com (including a built article URL) and for the wyocourts.gov opinions page (search-result URL). 12 WebFetch calls used. curl to www.wyocourts.gov got HTTP 403 "Access denied: Automated access detected" (x-blocked-by: Fruition-Cloud-Bot-Protection); stopped using curl on that host. fetch_doc.py was served normally.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://wyoleg.gov/robots.txt, https://www.wyoleg.gov/robots.txt | script | HTTP 404 (no rules) |
| https://www.wyocourts.gov/robots.txt | script | 563 chars; `*` disallows /app/uploads/protected/, /protected-files/, /search, /*search*, /*?*query*, /*?*keyword*; Allow / |
| https://rules.wyo.gov/robots.txt | script | HTTP 404 |
| https://sos.wyo.gov/robots.txt | script | Disallow /_mm/, /_notes/, election WYCF docs only |
| https://documents.wyocourts.gov/robots.txt | script | proxy 502 Tunnel connection failed |
| https://ctefiling.wyocourts.gov/robots.txt | script | 200, 0 chars (app shell) |
| https://cases.justia.com/robots.txt | script | `Disallow: /static/pdf-js/web/` only |
| https://law.justia.com/… | script | REFUSED: robots.txt challenge (refusal cached earlier today) |
| https://wyoming.public.law/ | script | proxy 502 Tunnel connection failed |
| https://www.wyocourts.gov/legal-research-resources/wyoming-research-and-resources/ | script | REFUSED: robots `Disallow: /*search*` matches "research" |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WS "wyoleg.gov statutes title pdf compress" | WS | Justia years, wyoleg.gov/2011/Session Laws.pdf |
| https://www.wyoleg.gov/ | script | html, 0 chars (Angular shell) |
| https://wyoleg.gov/StateStatutes/StatutesDownload | script links | 0 links (shell) |
| https://www.wyoleg.gov/ , main-*.js, chunk-DZMBzqM2.js, chunk-CQXRRUwh.js | curl (bundle inspection) | statutes links compress/Title01-42.pdf, Title97.pdf = Constitution; NXT gateway; currency "as they exist as of July 1, 2026"; disclaimer "not the official record" |
| https://wyoleg.gov/statutes/compress/title01.pdf (and /Statutes/ case) | script info | pdf 366 pp, 730,731 chars; Last-Modified 8 May 2026 |
| …/Title01.pdf | script grep "1-3-105. " | 1 match p. 35, "(a) Civil actions other than for the recovery of real property" |
| …/Title01.pdf | script read | "TITLE 1 - CODE OF CIVIL PROCEDURE" |
| …/Title06.pdf | script grep "6-2-101. " | p. 14 "Whoever purposely and with premeditated malice" |
| https://wyoleg.gov/statutes/compress/Title01.pdf | WF | PROVENANCE_REQUIRED |
| https://wyoleg.gov/NXT/gateway.dll?f=templates&fn=default.htm | script | 466 chars search-form labels, 0 links |
| https://wyoleg.gov/2011/Session%20Laws.pdf | script | pdf 624 pp, 1,570,300 chars; "1 HB0061 OMNIBUS WATER BILL-PLANNING" |
| https://wyoleg.gov/{2024,2025,2026}/Session%20Laws.pdf | script | html 0 chars (soft 404: app shell) |
| WS "Wyoming Statutes 1-3-105 … law.justia.com" | WS | Justia 2013 / chapter pages |
| https://law.justia.com/codes/wyoming/title-1/chapter-3/ | WF | "2025 Wyoming Statutes"; section links only, no body |
| https://law.justia.com/codes/wyoming/title-1/chapter-3/section-1-3-105/ | WF | YES "(a) Civil actions other than for the recovery of real"; "WY Stat § 1-3-105 (2025)" |
| https://law.justia.com/codes/wyoming/title-6/chapter-2/article-1/section-6-2-101/ | WF | YES "(a) Whoever purposely and with premeditated malice, or in the" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://wyoleg.gov/statutes/compress/Title97.pdf | script | pdf 81 pp, 166,570 chars; "TITLE 97 - WYOMING CONSTITUTION"; Art. 1 § 8 "All courts shall be open" p. 2 |
| same | script grep "Article 5, Section 2 Supreme court" | p. 25 "The supreme court shall have general appellate jurisdiction" |
| https://law.justia.com/constitution/wyoming/ | WF | YES Art. 1 § 8; one page; no edition; 136,973 chars (read 0-100,000) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.wyocourts.gov/court-rules/ | script links | ~45 rule-set pages |
| …/court-rules/wyoming-rules-of-{appellate-procedure,civil-procedure,evidence,criminal-procedure}/ | script links | "Download Rule" PDF links under /app/uploads/ |
| …/app/uploads/2025/01/WY-Rules-of-Civ.-Procedure-Eff.-9-21-26.pdf | script | 228 pp, 1,162,284 chars; "Rule 56. Summary Judgment. (a)" p. 169 |
| …/app/uploads/2025/01/WYOMING-RULES-OF-EVIDENCE-1.pdf | script | 26 pp, 92,805 chars; Rule 702 two versions p. 10; verify "Rule 1008." VERIFIED p. 25 |
| same | WF | PROVENANCE_REQUIRED |
| …/app/uploads/2025/01/WRAP-eff-Dec-1.pdf | script | 125 pp, 552,805 chars; "Rule 9.08. Petition for Rehearing." p. 66 |
| …/app/uploads/2026/06/WRCrP-with-bond-schedule.pdf | script | 190 pp, 761,741 chars; "Rule 35. Correction or Reduction of Sentence." p. 93 |
| …/court-rules/uniform-rules-for-district-courts-of-the-state-of-wyoming-2/ | script links | …/2026/06/Uniform-Rules-for-District-Courts-of-Wyomingeff-August-2026.pdf |
| that PDF | script | 23 pp, 115,304 chars; "Rule 802" p. 16 |
| …/court-rules/rules-of-professional-conduct-for-attorneys-at-law/ → …/2026/06/WY-Rules-Prof-Conduct-Eff.-9-21-26.pdf | script info | 140 pp, 569,634 chars |
| https://www.wyocourts.gov/app/uploads/2025/01/wrap_2015040900-1.pdf (from WS) | script | 38 pp; order amending W.R.A.P. (not an opinion) |

## D — Administrative code / register
| URL | Tool | Result |
|---|---|---|
| https://rules.wyo.gov/ | script | 7,650 chars; SOS "repository for rules"; indexing by agency, program, chapter, effective date |
| https://rules.wyo.gov/ | WF | PROVENANCE_REQUIRED |
| https://rules.wyo.gov/Search.aspx?mode=7 | script | 5,221 chars; "ADMINISTRATIVE RULES (CODE)"; postback form, no rule links |
| https://rules.wyo.gov/Help/Public/index.html | script links | Help & Manual frames only |
| WS "rules.wyo.gov DownloadFile.aspx …" | WS | only wyoleg.gov/arules/2012/rules/ARRyy-nnnP.pdf (LSO rule review) |
| https://www.law.cornell.edu/regulations/wyoming | script | 4,643 chars, agency list |
| …/agency-053 → subagency-0021 → chapter-1 | script links | sections …/chapter-1/053-1-Wyo-Code-R-SSSS-1-1 … 1-6 |
| …/053-1-Wyo-Code-R-SSSS-1-1 | script | "053-1 Wyo. Code R. §§ 1-1 - Authority"; "These rules, regulations and fee schedules are adopted by the"; "Amended, Eff. 8/24/2017" |
| …/agency-020/subagency-0002/chapter-2 | script links | flat links …/regulations/wyoming/020-2-Wyo-Code-R-SSSS-2-1 |
| …/020-2-Wyo-Code-R-SSSS-2-1 | script | "020-2 Wyo. Code R. §§ 2-1 - Introduction to Ambient Standards" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS "wyocourts.gov supreme court opinions 2024 WY" | WS | wyocourts.gov/wy-supreme-court-opinions/, Justia 2024 |
| https://www.wyocourts.gov/wy-supreme-court-opinions/ | script | 7,739 chars; "published prior to 2006 are not available"; table headers, no rows; 81 links, none to opinions |
| same | WF | headers only, NO rows; JS list |
| same | curl | HTTP 403 bot protection (stopped) |
| https://www.wyocourts.gov/wp-json/ | script | WordPress route index; custom route /api/v1/dynamictable |
| https://www.wyocourts.gov/wp-json/api/v1/dynamictable | script | HTTP 400 |
| https://www.wyocourts.gov/supreme-court-opinion-summaries/ | script links | no opinion links |
| https://www.wyocourts.gov/supreme-court/ | script links | "Public Docket" → ctefiling.wyocourts.gov/portal/home |
| WS for opinion PDF hosts (3 queries) | WS | no official opinion PDF URL found |
| https://law.justia.com/cases/wyoming/supreme-court/2024/ | WF | s-24-0162.html (2024 WY 139), s-24-0004.html (2024 WY 138) … |
| https://law.justia.com/cases/wyoming/supreme-court/2024/s-24-0004.html | WF | body to ¶101 then truncated (112,583 chars); PDF link cases.justia.com/…/2024-s-24-0004.pdf?ts=… |
| https://cases.justia.com/wyoming/supreme-court/2024-s-24-0004.pdf?ts=1734711128 | script | 41 pp, 119,181 chars; "2024 WY 138 OCTOBER TERM, A.D. 2024" |
| https://cases.justia.com/wyoming/supreme-court/2024-s-24-0162.pdf | script | 4 pp; "2024 WY 139" |
| https://law.justia.com/cases/wyoming/supreme-court/ | WF | years 1870-2026 |
| https://law.justia.com/cases/wyoming/supreme-court/2006/ | WF | numeric ids: 448386.html = 2006 WY 160, 149 P.3d 702, docket 06-20 |
| https://law.justia.com/cases/wyoming/supreme-court/2006/448386.html | WF | YES full body ¶1-¶26, "Appellant, Christopher Rader (Rader), a bar patron, filed a complaint" |
| https://www.wyocourts.gov/chancery-court-orders-and-decisions/ | script | 8,048 chars; database "pursuant to Wyo. Stat. Ann. § 5-13-104(f)"; 0 decision links |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://ctefiling.wyocourts.gov/portal/home | script | 0 chars (JS app) |
| WRAP PDF (above) | script | Rule 9.08 rehearing petition within 15 days |

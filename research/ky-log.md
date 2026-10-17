# Kentucky (ky) probe log: 2026-10-17

All probes were run on 2026-10-17 by `research`. "WF" = WebFetch, "script" = `scripts/fetch_doc.py --research`, "curl" = robots.txt reads only (no refusal was worked around). WebFetch calls: 13 of about 55. Four were refused by the session's URL-provenance gate (an unanswered permission prompt, not a site refusal). WebSearch calls: 5.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://apps.legislature.ky.gov/robots.txt | curl | 404 IIS "File or directory not found": no rules |
| https://legislature.ky.gov/robots.txt | curl | 403 Azure Front Door HTML "The request is blocked." (plain curl UA) |
| https://www.kycourts.gov/robots.txt | curl | 403 "The request is blocked." to plain curl. One diagnostic re-request with a browser UA got 200; contents not used. |
| https://www.kycourts.gov/x, https://legislature.ky.gov/x | script check | "allowlisted; robots.txt permits"; pages then fetched 200 by script |
| https://opinions.kycourts.net/robots.txt | curl | connection reset |
| https://appellatepublic.kycourts.net/ | script check | "robots.txt permits" |
| https://law.justia.com/robots.txt | curl | 403 Cloudflare "Just a moment..." |
| https://ky.public.law/robots.txt | curl | proxy 502 CONNECT failed (not probed further) |
| https://www.law.cornell.edu/robots.txt | curl | 200; `User-agent: *` Crawl-delay 10 |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| https://apps.legislature.ky.gov/law/statutes/ | script info/grep/links | 200 html 42,632 chars; "Includes enactments through the 2026 Regular Session"; 839 links |
| https://apps.legislature.ky.gov/law/statutes/ | WF | PROVENANCE_REQUIRED (gated; not retried) |
| …/statutes/chapter.aspx?id=39261 (ch. 413) | script | 200 html 8,517 chars; "The KRS database was last updated on 10/17/2026"; ".140 Actions to be brought within one year." -> statute.aspx?id=58050 |
| …/statutes/statute.aspx?id=58050 | script info/read/grep | PDF 2 pp, 5,536 chars; "413.140 Actions to be brought within one year."; "Effective: July 15, 2026 History:" |
| …/statutes/statute.aspx?id=58050 | WF | PROVENANCE_REQUIRED (gated) |
| …/statutes/chapter.aspx?id=38914 (ch. 342) | script links | ".0011 Definitions for chapter." -> id=56771 |
| …/statutes/statute.aspx?id=56771 | script | PDF 8 pp, 27,132 chars; "342.0011 Definitions for chapter." |
| https://apps.legislature.ky.gov/LAW/STATUTES/statute.aspx?id=50197 (from WebSearch) | WF | KRS 304.20-450 repeal stub; "Repealed 2020 Ky. Acts ch. 47, sec. 5" |
| …/statutes/chapter.aspx?id=39283 (ch. 422A) | script links | ".0702 Renumbered as KRE 702." |
| …/statutes/statute.aspx?id=18198 | script | PDF 33 chars "422A.0702 Renumbered as KRE 702." |
| https://legislature.ky.gov/Law/Statutes/Pages/default.aspx | script grep | "an unofficial posting of the Kentucky Revised Statutes"; KRS 61.874 commercial-use bar |
| https://legislature.ky.gov/Law/Statutes/Pages/KRSEDS.aspx | script grep | "Under KRS 7.138(2), only texts from the official version or a certified version" |
| https://law.justia.com/codes/kentucky/2012/chapter-57/57.320/ (from WebSearch) | WF | newer version -> /codes/kentucky/chapter-57/section-57-320/; years 2025, 2024, 2023, 2012 |
| https://law.justia.com/codes/kentucky/chapter-57/section-57-320/ | WF | YES "The state law librarian, under direction of the Supreme Court"; "2025 Kentucky Revised Statutes" |
| https://law.justia.com/codes/kentucky/chapter-413/section-413-140/ (built) | WF | YES "The following actions shall be commenced within one (1) year" |
| https://legislature.ky.gov/Law/Pages/KyActs.aspx | script links | sessions 26RS…22SS…; /law/acts/24RS/index.html |
| …/law/acts/24RS/index.html, acts_table_by_chapter.html | script links | chapter 1 -> /law/acts/24RS/documents/0001.pdf |
| …/law/acts/24RS/documents/0001.pdf | script | PDF 1 p "CHAPTER 1 ( HB 161 ) AN ACT" |
| …/law/acts/23RS/documents/0005.pdf (built) | script | PDF 2 pp "CHAPTER 5 ( SB 72" |
| https://apps.legislature.ky.gov/law/acts/19RS/ | script links | nav links only (no index.html at that path) |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| https://legislature.ky.gov/Law/Constitution/Pages/default.aspx | script | HTTP 404 |
| https://apps.legislature.ky.gov/law/constitution | script | 200 html 36,907 chars; "(Includes Amendments Ratified On or Before November 5, 2024)"; Section 1 -> rsn=3, 115 -> rsn=131 |
| …/Law/Constitution/Constitution/ViewConstitution?rsn=131 | script | PDF 1 p 838 chars "Section 115 Right of appeal -- Procedure." |
| https://law.justia.com/constitution/kentucky/ | WF | index YES; Sections 115-116 grouped at list1.html#Appellate; "may not be the most recent version" |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.kycourts.gov/courts/supreme-court/Pages/default.aspx | script links | "Supreme Court Rules & Procedures (Westlaw)" -> govt.westlaw.com/kyrules |
| https://www.kycourts.gov/Courts/Pages/Rules-of-Practice.aspx | script links | only "West's Rules & Procedures" (Westlaw) |
| https://govt.westlaw.com/kyrules/Index?… | script | REFUSED "robots.txt challenge, 2026-10-17T09:38:19"; not retried |
| https://www.kycourts.gov/Courts/Court-of-Appeals/Pages/default.aspx | script links | "Rules of Appellate Procedure" -> Supreme Court Orders/202249.pdf; "Searchable Opinions" -> opinions.kycourts.net/dtsearch.html |
| …/Supreme Court Orders/202249.pdf | script | PDF 89 pp 205,517 chars; "Order Creating Rules of Appellate Procedure" |
| https://kycourts.gov:443/…/202249.pdf (from WebSearch) | WF | truncated mid RAP 32(E)(1)(b); "RAP 41 NOT PRESENT"; Order 2022-49 eff. Jan. 1, 2023 |
| …/Supreme Court Orders/202332.pdf | script | 2 pp "Guidelines for Submission and Review of Proposed Rule Amendments" |
| …/Supreme Court Orders/202601.pdf | script; WF (from WebSearch) | 12 pp; "effective April 1, 2026"; WF complete, RAP 2 "(A) Filing the Notice of Appeal." |
| https://www.kycourts.gov/Courts/Supreme-Court/Pages/Administrative-Orders.aspx | script links | 618 links; "Amending Supreme Court Rule 2.112 … 2026-36 Order" -> 202636.pdf |
| WebSearch "kycourts.gov Rules of Civil Procedure PDF …" | WS | only Westlaw store / third-party rule sites; one kycourts order PDF |

## D: Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://apps.legislature.ky.gov/law/kar/titles.htm | script links | -> /law/kar/titles/201 (titles are 3-digit: /titles/001) |
| …/kar/titles/201, …/201/009 | script links | "Regulation 260 — Professional standards …" -> /titles/201/009/260/ |
| …/kar/titles/201/009/260/ | script | html 59,500 chars; "ALTERNATE VIEW This is how this document appeared before it was engrossed."; Download PDF docs/1885 |
| …/kar/downloads/docs/1885/document.engrossed.pdf | script | 8 pp 30,012 chars; ends "47 Ky.R. 374, 944; eff. 11-19-2020." |
| …/kar/titles/401/005/005/ (built) | script | html 164,689 chars; text appears twice |
| …/kar/titles/013/002/020/ (built) | script | 200; "13 KAR 2:020.Guidelines for admission"; /titles/13/002/020/ -> 404 |
| …/kar/titles/401/005/005E/ (built) | script | 404 |
| …/kar/downloads/docs/845/document.engrossed.pdf (from WebSearch) | WF; script | both: 103 KAR 008:141 placeholder "Not available" |
| https://legislature.ky.gov/Law/kar/Pages/default.aspx | script grep | "Unofficial WWW Version"; "updated approximately once a month" |
| https://legislature.ky.gov/Law/kar/Pages/KarFaqs.aspx | script grep | no official-status statement |
| https://legislature.ky.gov/Law/kar/Pages/Registers.aspx | script links | 53Ky_R_2026-27/01_July.pdf … 04_Oct.pdf |
| …/kar/registers/53Ky_R_2026-27/04_Oct.pdf | script | 242 pp 2,211,430 chars; "VOLUME 53, NUMBER 4 … OCTOBER 1, 2026" |
| https://www.law.cornell.edu/regulations/kentucky | script | 200, last-modified 2025-08-02 |
| …/regulations/kentucky/201-KAR-9-260, 401-KAR-5-005 | script | 32,166 / 87,808 chars; "Section 1. Applicability."; "State regulations are updated quarterly" |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| http://opinions.kycourts.net/dtsearch.html | script | FETCH ERROR: TLS chain does not verify |
| http://opinions.kycourts.net/dtsearch.html | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://appellatepublic.kycourts.net/ | script; curl (page source) | 200, html 0 chars (Vue shell "publicaccess"); properties.js apiRoot "/api/api/v1" |
| https://appellatepublic.kycourts.net/api/api/v1/searches/types | script | HTTP 500 |
| https://www.kycourts.gov/Pages/sitemap.aspx | script links | no opinion-search link besides judicial ethics |
| https://www.kycourts.gov/Courts/Court-of-Appeals/Pages/Court-of-Appeals-Minutes.aspx | script links | apps.kycourts.net/Appeals/Minutes/MNT01092026.pdf … MNT10092026.pdf |
| https://apps.kycourts.net/Appeals/Minutes/MNT01092026.pdf | script | 8 pp; "2024-CA-1103-MR … NOT TO BE PUBLISHED OPINION AFFIRMING" |
| https://law.justia.com/cases/kentucky/supreme-court/2000/ (from WebSearch) | WF | listing YES; docket + date per case |
| https://law.justia.com/cases/kentucky/ | WF | Supreme Court and Court of Appeals links |
| https://law.justia.com/cases/kentucky/court-of-appeals/ | WF | years 1894-2026 |
| https://law.justia.com/cases/kentucky/supreme-court/ | WF | years 1976-2026 |
| https://law.justia.com/cases/kentucky/court-of-appeals/2026/2024-ca-0287-mr.html | WF | full text YES; "TO BE PUBLISHED"; Aug. 28, 2026; PDF link cases.justia.com |
| https://law.justia.com/cases/kentucky/court-of-appeals/2026/2024-ca-0287-mr.html | script | REFUSED (robots.txt challenge; host off for the day) |
| https://cases.justia.com/kentucky/court-of-appeals/2026-2024-ca-0287-mr.pdf?ts=1787925814 | script | PDF 48 pp 79,135 chars; "RENDERED: AUGUST 28, 2026; 10:00 A.M. TO BE PUBLISHED" |
| WebSearch "opinions.kycourts.net …", "appellatepublic.kycourts.net …" (x3) | WS | no direct opinion-PDF URLs on court hosts |

## F: Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.kycourts.gov/Courts/Supreme-Court/Pages/Supreme-Court-Minutes.aspx | script links | MNT012026.pdf … MNT092026.pdf; archive back to MNT01222009.pdf |
| https://apps.kycourts.net/Supreme/Minutes/MNT092026.pdf | script grep | 17 pp; "ORDER GRANTING DISCRETIONARY REVIEW (ORAL ARGUMENT) - September 16, 2026"; "ORDER DENYING DISCRETIONARY REVIEW"; 0 matches for "-CA-" dockets |

## Build
- `python3 scripts/build.py --check`: exit 0, no ERROR or WARN lines.
- `python3 scripts/build.py --cross`: "0 cross-jurisdiction match(es)".

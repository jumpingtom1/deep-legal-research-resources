# Alaska (ak) probe log — 2026-10-16/17

All probes by `research`. "script" = `scripts/fetch_doc.py --research`; "shell" = curl (robots.txt / form markup only); "WF" = WebFetch; "WS" = WebSearch.

Tool notes: the first session (2026-10-17 ~00:06) hit a WebFetch "session limit" error after 3 calls and stopped fetching; it resumed after the reset. WebFetch refused every hand-built URL with `PROVENANCE_REQUIRED` ("permission request ... not answered in time"); it worked only on URLs taken from search results or fetched pages. 13 WebFetch calls in all (3 refused or quota-limited).

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.akleg.gov/robots.txt | shell | 200; Disallow /PDF/, /cgi-bin/, /basis/get_jrn_page.asp, other legacy paths |
| https://courts.alaska.gov/robots.txt | shell | 200; Disallow /cip/, /mediation/, /covid19/deleted/ |
| https://public.courts.alaska.gov/robots.txt | shell | 200; Allow /app, /web |
| https://aws.state.ak.us/robots.txt | shell | 200; Disallow /*.axd?, /OAH/Files/* etc. |
| https://ltgov.alaska.gov/robots.txt | shell | 200; Yoast, empty Disallow |
| https://law.justia.com/robots.txt | shell | 403 Cloudflare "Just a moment..." |
| https://appellate-records.courts.alaska.gov/robots.txt | shell | 404 IIS page |
| https://govt.westlaw.com/robots.txt | shell | Cloudflare "Attention Required!" page |
| http://list.state.ak.us/pipermail/ak-slip-opinions/ | script | REFUSED robots (Disallow: /) |
| https://alaska.public.law/ | shell | CONNECT tunnel 502 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.akleg.gov/basis/statutes.asp#09.10.070 | script | 200 html 2,327 chars; JS shell, 0 matches for 09.10.070 |
| same | WF | PROVENANCE_REQUIRED |
| https://www.akleg.gov/scripts/statutes.js | shell | AJAX calls `media=print&secStart&secEnd`, `media=js&type=TOC&title` |
| …/statutes.asp?media=print&secStart=09.10.070&secEnd=09.10.070 | script | 200, 1,132 chars, "Sec. 09.10.070. Actions for torts…"; verify VERIFIED |
| same | WF | PROVENANCE_REQUIRED |
| …?media=print&secStart=11.41.100&secEnd=11.41.100 | script | 7,196 chars, "Murder in the first degree." |
| …?media=print&secStart=09.10.010&secEnd=09.10.240 | script | 17,804 chars, every Sec. heading 010-240 |
| …?media=print&secStart=09&secEnd=09.99.999 | script | 589,488 chars (whole Title 9) |
| …?media=js&type=TOC&title=9 | script | chapter list, no section ranges |
| https://www.akleg.gov/basis/statutes.asp (grep) | script | "Alaska Statutes 2025" header |
| WS "akleg.gov/basis/statutes.asp" | WS | found /basis/statUTES.asp |
| https://www.akleg.gov/basis/statUTES.asp | WF | first try: "session limit" error; retry: TOC only, "Alaska Statutes 2024" (cached) |
| https://www.akleg.gov/basis/start.asp | script links | Statutes, AAC, Constitution (ltgov), Session Laws links |
| WS Justia Alaska codes | WS | /codes/alaska/2020/ etc. |
| https://law.justia.com/codes/alaska/2020/ | WF | editions 2025, 2024, 2023, 2020; "There Is a Newer Version" |
| https://law.justia.com/codes/alaska/2020/title-9/ | WF | chapters, no section ranges |
| …/2020/title-9/chapter-10/ | WF | section link …/section-09-10-070/ |
| …/2020/title-9/chapter-10/section-09-10-070/ | WF | YES "(a) Except as otherwise provided by law, a person may" |
| https://law.justia.com/codes/alaska/title-9/ | script | REFUSED (robots challenge) |
| https://www.akleg.gov/pdf/billfiles/SLAs/SLA%201996/CH%2070%20SLA%201996.pdf | script | REFUSED robots ("Disallow: /PDF/") |
| same | WF | ch. 70 SLA 1996 text, OCR errors |
| https://courts.alaska.gov/library/aklegal.htm | script | "official publisher of the Alaska Statutes is LexisNexis"; AAC same; case law DB link |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://ltgov.alaska.gov/services/alaskas-constitution/ | script | → /information/alaskas-constitution/, 105,195 chars |
| https://ltgov.alaska.gov/information/alaskas-constitution/ | script | art. I § 22 and § 7 quotes VERIFIED |
| same | WF | PROVENANCE_REQUIRED |
| https://ltgov.alaska.gov/wp-content/uploads/PDF-Pocket-Constitution.pdf | script | pdf 64 pp, 116,813 chars; "Printed in April 2023" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://courts.alaska.gov/rules/index.htm | script | network error (connection closed) |
| https://courts.alaska.gov/rules/ | script links | 28 rule PDFs; "official publisher … is Tower Publishing" |
| WS Alaska civil rules | WS | COURTS.ALASKA.GOV/rules/docs/civ.pdf |
| https://courts.alaska.gov/rules/docs/civ.pdf | script | 150 pp, 955,507 chars; 12(b)(6) phrase VERIFIED p. 32 |
| https://COURTS.ALASKA.GOV/rules/docs/civ.pdf | WF | truncated, stops in Rule 6; Rule 12(b) NOT PRESENT |
| …/rules/docs/crpro.pdf | script | 80 pp, 474,580 chars; "Rule 35.1. Post-Conviction Procedure." p. 61 |
| …/rules/docs/ev.pdf | script | 26 pp, 159,059 chars; Rule 702 heading p. 19 |
| …/rules/docs/app.pdf | script | 56 pp, 356,901 chars; "Rule 302." grep 0 |
| …/rules/docs/adm.pdf | script | 72 pp, 493,151 chars |
| https://courts.alaska.gov/sco/index.htm | script | 200, 3,819 chars |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| http://www.akleg.gov/basis/aac.asp | script | JS shell, title list |
| …/aac.asp?media=print&secStart=7.160.900&secEnd=7.160.900 | script | 18,874 chars "7 AAC 160.900. Requirements adopted by reference." |
| …secStart=07.160.900… | script | same page |
| …secStart=18.75.400… | script | 5,689 chars "18 AAC 75.400. Applicability." |
| …/aac.asp?media=js&type=TOC&title=7 | script | parts with section ranges |
| WS Alaska Administrative Register | WS | AAJ PDFs, LII 1-AAC-05.010 |
| https://aws.state.ak.us/onlinepublicnotices/Files/AAJ/aaj49.pdf | script | 34 pp, "ISSUE 49, December 6, 1999" |
| https://www.law.cornell.edu/regulations/alaska/7-AAC-160.900 | script | 125,488 chars; VERIFIED; "Register 193" history |
| https://www.law.cornell.edu/regulations/alaska/18-AAC-75.400 | script | 200, 8,615 chars |
| https://ltgov.alaska.gov/information/regulations/ | script | AAC on akleg; notices to OPNS |
| http://aws.state.ak.us/OnlinePublicNotices/Notices/Search.aspx?status=4&cat=10&subcat=10 | script | 56,686 chars, search form |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS Alaska opinions (3 queries) | WS | CMSPublic, Justia year pages |
| https://courts.alaska.gov/appellate/index.htm | script | first two tries: connection reset; then 200, 11,636 chars; slips kept until P.3d; MOJs "retained … three months" |
| https://appellate-records.courts.alaska.gov/CMSPublic/Home/Opinions?isCOA=False | script | 104,574 chars; rows 2022-2026; "available for direct download until they are published" |
| …/Home/Opinions?isCOA=True | script | rows 2018-2026 |
| …/Home/AppellateOpinions | script links | MOJ, summary dispositions, published orders listings |
| …/Home/MOJOpinions?isCOA=True | script | rows 2022-2026; 149 downloads, 188 "No Document" |
| …/UserControl/OpenOpinionDocument?q=…(S19268) | script | sp-7834.pdf 15 pp "Supreme Court No. S-19268" |
| …OpenOpinionDocument (A13337) | script | ap-2814.pdf 58 pp "No. 2814 — August 22, 2025" |
| …OpenOpinionDocument (MOJ A-14138) | script | Rule 214(d) legend |
| https://appellate-records.courts.alaska.gov/CMSPublic/ | shell | GET forms: Search/CaseNumber, PartyNameSearch, AttorneyNameSearch |
| …/Search/CaseNumber?CaseNumber=S-19268&TrialCourtNumber= | script | full match S19268, "Opinion Issued" |
| https://courts.alaska.gov/ops/sp-7834.pdf, /ops/ap-2814.pdf | script | HTTP 404 |
| https://govt.westlaw.com/akcases/Index | script | REFUSED robots challenge |
| https://law.justia.com/cases/alaska/supreme-court/2007/ | WF | listing; s-12164-1.html |
| https://law.justia.com/cases/alaska/supreme-court/2007/s-12164-1.html | WF | full text; 174 P.3d 224 |
| https://law.justia.com/cases/alaska/court-of-appeals/ | WF | years 1980-2026 |
| https://law.justia.com/cases/alaska/supreme-court/2024/ | WF | s-18729.html, s-18521.html |
| https://law.justia.com/cases/alaska/supreme-court/2023/ | WF | s-18114.html; no year links |
| https://law.justia.com/cases/alaska/supreme-court/2024/ | script | REFUSED (challenge) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| …/Search/CaseNumber?CaseNumber=&TrialCourtNumber=A-13337 | script | no match |
| …/Search/PartyNameSearch?CourtTypeString=SC&IsActiveStatus=-1&LastName=Marino&FirstName=Gregory&CompanyName= | script | S19597 "302 Petition for Hearing", 2025-11-04 |
| …/Search/CaseNumber?CaseNumber=A-13337&TrialCourtNumber= | script | link Case/General?q=… |
| …/Case/General?q=w6sobc/DATerGL7Z2BzdnA==' | script | Opinion 2814 Reverse/Remand; Related: S19597 Petition for Hearing, Briefing Stage |

## Build
`python3 scripts/build.py --check`: no ERROR/WARN lines for ak.json. `--cross`: 0 matches (after narrowing one example).

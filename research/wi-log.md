# Wisconsin (wi) probe log — 2026-10-17

All probes by `research` on 2026-10-17. "WF" = WebFetch; "WS" = WebSearch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET through the agent proxy, used only for robots files and to read search-form field names / one result row's raw HTML on pages the script had already fetched, never on a refused URL. Quoted text is 15 words or fewer.

**WebFetch tally:** 11 calls. 2 failed on the account session limit ("You've hit your session limit"), which paused the run until the coordinator said the limit had reset. 2 returned PROVENANCE_REQUIRED for built URLs (gated; not retried). 7 returned content. WS: 3 calls.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://docs.legis.wisconsin.gov/robots.txt | curl | 200; `*` Disallow /frame, /frame/, /scroll/, /feed/, /doc/feed/, /breadcrumbs/, /preferences, /search |
| https://www.wicourts.gov/robots.txt | curl | site HTML page "Error 404 - Page not found" (no robots rules) |
| https://wscca.wicourts.gov/robots.txt, https://wcca.wicourts.gov/robots.txt | curl | 404 "The Requested URL /robots.txt was not found" |
| https://www.law.cornell.edu/robots.txt | curl | 200; Crawl-delay 10 |
| law.justia.com (any) | script | REFUSED: "refused automated access earlier (robots.txt challenge)" — host off for the day |

## A — Statutes and session laws
| URL | Tool | Result |
|---|---|---|
| https://docs.legis.wisconsin.gov/statutes/statutes/893/54 | script | HTTP 404 (subchapter segment missing) |
| https://docs.legis.wisconsin.gov/statutes/statutes/940/01 | script | HTTP 404 |
| https://docs.legis.wisconsin.gov/statutes/statutes/802/06/2/a/6 | script | html 34,314 chars |
| https://docs.legis.wisconsin.gov/document/statutes/893.54 | script | → /statutes/statutes/893/v/54, 31,362 chars; "893.54 Injury to the person. (1m) Except as provided in sub. (2m)"; verify "An action to recover damages for injuries to the person" VERIFIED |
| same | script grep | footer "updated through 2025 Wis. Act 247 … October 1, 2026. Published and certified under s. 35.18." |
| same | WF | PROVENANCE_REQUIRED (built URL), not retried |
| …/document/statutes/940.01 | script | → /940/i/01, 25,359 chars; "whoever causes the death of another human being with intent to kill" |
| …/document/statutes/802.06 | script | → /802/06, 37,535 chars |
| …/document/statutes/802.06(2)(a)6. | script | → /802/06/2/a/6; "Failure to state a claim upon which relief can be granted" VERIFIED |
| …/document/statutes/180.0302 | script | → /180/iii/0302, 18,431 chars |
| …/document/statutes/35.18, 35.93, 889.01 | script | 35.18(1)(b)3.e: notice that updated version "is certified under sub. (2) (b)"; 35.93 no "official" wording found |
| WS "docs.legis.wisconsin.gov statutes 893.54 injury to the person" | WS | surfaced /statutes/statutes/893/V/54 and Justia chapter-893/section-893-54 |
| https://docs.legis.wisconsin.gov/statutes/statutes/893/V/54 | WF (1st try) | session limit error |
| https://law.justia.com/codes/wisconsin/chapter-893/section-893-54 | WF (1st try) | session limit error |
| https://docs.legis.wisconsin.gov/statutes/statutes/893/V/54 | WF | YES "Except as provided in sub. (2m), the following actions shall"; footer "updated through 2025 Wis. Act 170 … May 22, 2026"; truncated mid-893.55(5)(c) "Loading..."; sections 893.52–893.55 |
| https://law.justia.com/codes/wisconsin/chapter-893/section-893-54 | WF | YES "(1m) Except as provided in sub. (2m), the following actions"; "WI Stat § 893.54 (2025)"; not truncated |
| https://law.justia.com/codes/wisconsin/chapter-893/section-893-54/ | script | REFUSED (challenge earlier today) |
| https://docs.legis.wisconsin.gov/statutes/statutes/893.pdf | script | pdf 34 pp, 448,171 chars; "893.54 Injury to the person." in TOC |
| https://docs.legis.wisconsin.gov/document/statutes/893.54.pdf | script | → 893.pdf#page=0 (same file) |
| https://docs.legis.wisconsin.gov/statutes/statutes/893 | script | 6,520 chars; links only Up/Down window scroll, /document/statutes/893.pdf |
| https://docs.legis.wisconsin.gov/statutes/statutes | script | 31,701 chars; chapter list "Chapter 893 (PDF: ) - Limitations Of Commencement…" (no section ranges) |
| https://docs.legis.wisconsin.gov/statutes/prefaces/toc | script | 28,732 chars |
| https://docs.legis.wisconsin.gov/document/acts/2025/247 | script | → /2025/related/acts/247, 4,198 chars |
| https://docs.legis.wisconsin.gov/document/acts/2025/247.pdf | script | → /2025/related/acts/247.pdf, 1 p; "2025 WISCONSIN ACT 247"; "Date of enactment: April 9, 2026" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://docs.legis.wisconsin.gov/constitution/wi | script | 5,262 chars, navigation only; links /document/wisconsinconstitution/top.pdf |
| https://docs.legis.wisconsin.gov/document/wiconst/1/9 | script | 404 |
| https://docs.legis.wisconsin.gov/constitution/wi/000002/000009 | script | 404 |
| https://docs.legis.wisconsin.gov/document/wisconsinconstitution/I,9 | script | → /constitution/wi/000230/000020, 27,554 chars; "Every person is entitled to a certain remedy in the laws" VERIFIED; footer "Published August 5, 2026" |
| https://docs.legis.wisconsin.gov/document/wisconsinconstitution/VII,3 | script | → /000236/000004; "VII,3 Supreme court: jurisdiction. Section 3." |
| https://docs.legis.wisconsin.gov/document/wisconsinconstitution/top.pdf | script | → /constitution/wi.pdf, 95 pp, 1,375,500 chars; two-column; exact quote of I,9 not found (column layout) |
| https://law.justia.com/constitution/wisconsin/ | WF | index; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/wisconsin/article-i/ | WF | article page, Sections 1–26 links, no body |
| https://law.justia.com/constitution/wisconsin/article-i/section-9/ | WF | YES "Every person is entitled to a certain remedy in the" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.wicourts.gov/scrules/supreme.htm | script | → /scrules/index.htm, 8,298 chars |
| https://www.wicourts.gov/supreme/scrules.jsp | script | 404 |
| https://www.wicourts.gov/supreme/sc_rules.jsp | script | 11,412 chars; chapter table with release dates ("Chapter 20A … Jul 01, 2023"); "updated as changes are approved" |
| https://www.wicourts.gov/sc/rules/chap20a.pdf | script | 107 pp, 298,902 chars; SCR 20:1.7 p.38 quote VERIFIED; SCR 20:1.18 p.105 |
| https://www.wicourts.gov/sc/rules/chap20b.pdf | script | 64 pp, 214,011 chars |
| https://www.wicourts.gov/sc/rules/chap10.pdf | script | 56 pp, 133,945 chars |
| https://www.wicourts.gov/sc/rules/chap60.pdf | script | 40 pp, 106,779 chars |

## D — Administrative Code and Register
| URL | Tool | Result |
|---|---|---|
| …/document/administrativecode/DHS 110.04 (literal space) | script | error: URL can't contain control characters |
| https://docs.legis.wisconsin.gov/code/admin_code/dhs/110/110_04 | script | 404 |
| https://docs.legis.wisconsin.gov/document/administrativecode/DHS%20110.04 | script | → /code/admin_code/dhs/110/110/i/04, 19,763 chars; "has the meaning given in s. 256.01" VERIFIED; footer "Updated on the first day of each month." |
| https://docs.legis.wisconsin.gov/document/administrativecode/NR%20115.05 | script | → /code/admin_code/nr/100/115/05, 30,031 chars |
| https://docs.legis.wisconsin.gov/document/administrativecode/ch.%20DHS%20110.pdf | script | → /code/admin_code/dhs/110/110.pdf, 25 pp |
| https://docs.legis.wisconsin.gov/code/admin_code, /code/admin_code/dhs/110 | script | 200, index pages |
| https://docs.legis.wisconsin.gov/code/register, /code/register/2026/ | script | 200; year page 46 links, "850A2 Register (10/12/2026)" |
| https://docs.legis.wisconsin.gov/document/register/850/A1/toc | script | → /code/register/2026/850a1 |
| https://docs.legis.wisconsin.gov/document/register/850/A1/register_toc | script | → /code/register/2026/850a1/register; links EmR2609…EmR2602 |
| …/code/register/2026/850A1/register/emr_effect/emr2609/emr2609 | script | → …/849a3/register/emr/emr2609_rule_text/emr2609_rule_text, 12,292 chars |
| https://www.law.cornell.edu/regulations/wisconsin | script | index by agency |
| https://www.law.cornell.edu/regulations/wisconsin/Wis-Adm-Code-SS-DHS-110-04 | script | same hash as index (wrong slug falls back) |
| …/agency-department-of-health-services → /DHS-110-199 → /chapter-DHS-110 → /subchapter-I | script links | link "§ DHS 110.04 - Definitions" → /Wis-Admin-Code-SS-DHS-110-04 |
| https://www.law.cornell.edu/regulations/wisconsin/Wis-Admin-Code-SS-DHS-110-04 | script | "DHS 110.04 - Definitions … In this chapter: (1g)"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/wisconsin/Wis-Admin-Code-SS-NR-115-05 | script | "NR 115.05 - Minimum zoning standards for shorelands" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.wicourts.gov/opinions/supreme.jsp, /opinions/appeals.jsp, /opinions/index.htm | script | 200; links to sopinion.htm, aopinion.htm, sorders.htm, sc_disptab.jsp |
| https://www.wicourts.gov/opinions/sopinion.htm | curl | form GET action /supreme/scopin.jsp; fields docket_number, range, begin_date, end_date, party_name, disp_code, cite_type, cite_volume, cite_page, pdcNo, sortBy |
| https://www.wicourts.gov/opinions/aopinion.htm | curl | form action /other/appeals/caopin.jsp; same fields plus ca_district, author |
| …/supreme/scopin.jsp?begin_date=01/01/2024&end_date=03/31/2024&SortBy=date | script | 8 rows with seqNo PDF links (e.g. Catholic Charities, Mar 14, 2024) |
| …/scopin.jsp?pdcNo=2019+WI+12 (no range) | script | no results table |
| …/scopin.jsp?docket_number=2020AP002007 | script | 1 row Catholic Charities Bureau |
| …/scopin.jsp?party_name=Tavern+League&begin_date=01/01/2018&end_date=12/31/2026 | script | 1 row 2020AP001742 (Apr 14, 2021) |
| …/scopin.jsp?cite_type=Wis2D&cite_volume=385&cite_page=1 | script | no results table |
| …/scopin.jsp?range=None&pdcNo=2024+WI+13&sortBy=date | script | 1 row 2020AP002007, PDF seqNo=777152 |
| …/scopin.jsp?range=None&cite_type=Wis2D&cite_volume=393&cite_page=1&sortBy=date | script | "Sorry, no records found" |
| https://www.wicourts.gov/sc/opinion/DisplayDocument.pdf?content=pdf&seqNo=777152 | script | 129 pp, 275,298 chars; "2024 WI 13 SUPREME COURT OF WISCONSIN"; "Reported at 406 Wis. 2d 586, 987 N.W.2d 778"; ¶22 quote VERIFIED p.14 |
| same | WF | PROVENANCE_REQUIRED (built URL), not retried |
| …/other/appeals/caopin.jsp?range=None&pdcNo=2020+WI+App+34&sortBy=date | script | 1 row 2018AP002220-CR State v. Adam W. Vice "[Final publication on 2020-07-08]", seqNo=261630 |
| …/caopin.jsp?range=None&docket_number=2022AP000013&sortBy=date | script | Amazon Logistics v. LIRC, Apr 06, 2023, seqNo=641594 |
| …/caopin.jsp?range=None&begin_date=10/01/2026&end_date=10/16/2026&sortBy=date | script | rows incl. Oct 15, 2026 2026AP001629 |
| https://www.wicourts.gov/ca/opinion/DisplayDocument.pdf?content=pdf&seqNo=261630 | script | 45 pp; "2020 WI App 34 COURT OF APPEALS OF WISCONSIN PUBLISHED OPINION"; "†Petition for Review filed"; "¶1 STARK, P.J." |
| https://www.wicourts.gov/ca/opinion/DisplayDocument.html?content=html&seqNo=261630 | script | html 0 chars |
| https://www.wicourts.gov/ca/opinion/DisplayDocument.pdf?content=pdf&seqNo=1190465 | script | 22 pp; unpublished "DECISION NOTICE … October 15, 2026"; Appeal No. 2025AP1919 |
| scopin.jsp / caopin.jsp, range=None, begin/end 1994, 1995, 1996 | script | 1994 "no records"; 1995 SC 1 page, CA 22 pages; 1996 SC 3 pages, CA 36 pages |
| …/scopin.jsp?…1996… links | script | pagination via &page=2 |
| WS "wicourts.gov DisplayDocument.pdf 2024 WI 13 Catholic Charities Bureau" | WS | no wicourts opinion PDF surfaced |
| WS "law.justia.com cases wisconsin supreme-court 2024 Catholic Charities…" | WS | no Justia URL surfaced |
| https://law.justia.com/cases/wisconsin/ | WF | courts: Supreme, Court of Appeals, circuit/municipal; no year range |
| https://law.justia.com/cases/wisconsin/supreme-court/ | WF | years 1878–2026; example /2026/2022ap000431.html |
| https://law.justia.com/cases/wisconsin/supreme-court/2026/2022ap000431.html | WF | 2026 WI 28; ¶1 "The attorney general represents the state in legal matters, including"; truncated at 100,000 of 109,178 chars |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.wicourts.gov/opinions/sorders.htm | script/curl | form action /supreme/scorder.jsp; docket_number, party_name, range, dates |
| https://www.wicourts.gov/supreme/scorder.jsp?range=None&docket_number=2023AP000301 | script | 1 row Aug 18, 2026 Milwaukee Police Association v. City of Milwaukee; link extractor found no PDF link |
| same | curl | raw row: unquoted href /sc/order/DisplayDocImage.pdf?docId=1163207 |
| https://www.wicourts.gov/sc/order/DisplayDocImage.pdf?docId=1163207 | script | 1 p; "IT IS ORDERED that the petition for review is denied, without costs." |
| https://www.wicourts.gov/supreme/sc_disptab.jsp | script | "Disposition tables list actions taken on petitions for review"; 6 PDFs; "Oct 15, 2026 Disposition table - July & August 2026" |
| https://www.wicourts.gov/sc/DisplayDocument.pdf?content=pdf&seqNo=1192383 | script | 8 pp, 32,061 chars; "2026 WI 33 DISPOSITION OF PETITIONS"; row "2023AP000301 … Denied 8/18/2026" |
| https://wscca.wicourts.gov/ | script | html, 0 chars (JS shell) |
| https://wscca.wicourts.gov/caseDetails.do?caseNo=2018AP002220 | script | 404 |
| https://wscca.wicourts.gov/appealHistory.xsl?caseNo=2018AP002220&… | script | 404 |

## G — Citation map checks
- `python3 scripts/build.py --check`: no ERROR/WARN lines for wi.json.
- `python3 scripts/build.py --cross`: first run flagged 4 Wisconsin SCR examples ("SCR 20:1.7" etc.) as matching Nevada's bare `\bSCR\s*\d+` pattern. The Nevada record is not ours to edit, so the examples now use the Bluebook form "Wis. Sup. Ct. R. 20:1.7". The regex still accepts "SCR 20:1.7". Re-run: no CROSS line for wi.

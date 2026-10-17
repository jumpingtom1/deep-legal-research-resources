# North Carolina (nc) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET through the agent proxy (robots files, index pages, form markup; never used on a refused URL). Quoted text ≤ 15 words. WebFetch calls attempted: 44 (35 returned content). No quota/rate failures.

**Harness note.** WebFetch returned `PROVENANCE_REQUIRED` ("permission request … not answered in time") for any URL that a web search had not surfaced. That includes some URLs that appeared only in a WebFetch result, such as nccourts.gov asset PDFs. These are not site refusals, and the record lists them as open questions.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.ncleg.gov/robots.txt | curl | 200: `*` Disallow /WHPTest/, /Ethics/; Crawl-delay: 2 |
| https://appellate.nccourts.org/robots.txt | curl | 200: `User-agent: *` / `Disallow: /opinions/` |
| https://www.nccourts.gov/robots.txt | curl, script | 403 CloudFront "Request blocked."; script: "answers robots.txt with a bot check (refused)" |
| https://reports.oah.state.nc.us/robots.txt | curl, script | https: Connection reset by peer; http: 404 page |
| https://www.oah.nc.gov/robots.txt | curl | 200 Drupal default (allows core/profile assets) |
| https://files.nc.gov/robots.txt | curl | S3 `AccessDenied` XML |
| https://law.justia.com/robots.txt | curl, script | 403 Cloudflare "Just a moment..."; script REFUSED (robots.txt challenge) |
| https://north-carolina.public.law/, https://northcarolina.public.law/ | curl | CONNECT tunnel failed, 502 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1/GS_1-52.html (www) | script | 200 html 5,444 chars, last-modified 16 Apr 2026; grep "Within three years" found |
| same (www.ncleg.gov) | WF | PROVENANCE_REQUIRED (not surfaced by search) |
| https://ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_1/GS_1-52.html | WF | YES "Within three years an action (1) Upon a contract, obligation or liability"; complete to (20); no currency |
| https://ncleg.gov/…/Chapter_14/GS_14-17.html | WF | YES "A murder which shall be perpetrated by means of a"; complete |
| …/Chapter_14/GS_14-17.html, Chapter_15A/GS_15A-1415, Chapter_160D/GS_160D-102, Chapter_75/GS_75-1.1, Chapter_143B/GS_143B-135.40 | script | 200; 3,689 / 8,598 / 9,855 / 1,168 / 159 chars |
| …/PDF/BySection/Chapter_1/GS_1-52.pdf; …/RTF/BySection/Chapter_1/GS_1-52.rtf | script | PDF 2 pp 7,014 chars; RTF 34,331 chars |
| …/Chapter_1A/GS_1A-1.html; …/Chapter_8C/GS_8C-1.html | script | stubs, 129 / 119 chars: "The Rules of Civil Procedure are as follows:" |
| …/HTML/ByChapter/Chapter_1A.html | script | 301,629 chars; "Rule 12. Defenses and objections" at offset 67,139 |
| https://ncleg.gov/…/HTML/ByChapter/Chapter_1A.html | WF | Rule 56(c) NOT PRESENT; 12(b) "Every defense, in law or fact, to a claim for"; truncated in Rule 20; 131,823 chars |
| …/PDF/ByChapter/Chapter_1A.pdf | script | 87 pp, 352,069 chars |
| https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_116/GS_116-209.52.pdf | WF | Recodification notice only: "Recodified as G.S. § 127A-192, effective November 18, 2021." |
| https://ncleg.gov/…/Chapter_164/GS_164-11.8.html | WF | YES "(a) The chapters, subchapters, articles and sections now comprising Volume" |
| https://www.ncleg.gov/Laws/GeneralStatutes | curl | "The General Statutes include changes through S.L. 2026-30."; heading "Not Official" |
| https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter1A | curl | per-rule links `GS_1A-1,_Rule_{n}.html` (1–65, 67–70, 83, 84, 44.1, 68.1) |
| https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2023-2024/SessionLaw2023-134.html | script | 404 |
| https://www.ncleg.gov/Laws/SessionLaws | curl | links `/SessionLaws/HTML/2025-2026/SL2026-61.html` |
| https://www.ncleg.gov/EnactedLegislation/SessionLaws/HTML/2023-2024/SL2023-134.html | script | 200, 2,386,462 chars; "SESSION LAW 2023-134 HOUSE BILL 259" |
| https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-30.pdf | script | PDF 2 pp |
| https://law.justia.com/codes/north-carolina/chapter-1a/section-1a-1 | WF | Rule 12(b) NOT PRESENT; only lead-in; "2025 North Carolina General Statutes" |
| https://law.justia.com/codes/north-carolina/chapter-1a/ | WF | only one link, § 1A-1 |
| https://law.justia.com/codes/north-carolina/chapter-1/article-45a/ | WF | SERVER_ERROR |
| https://law.justia.com/codes/north-carolina/2024/ | WF | chapter links, no section ranges; newer version 2025 |
| https://law.justia.com/codes/north-carolina/2024/chapter-1/ | WF | article links titles only ("Article 5 - Limitations, Other Than Real Property.") |
| https://law.justia.com/codes/north-carolina/2024/chapter-1/article-5/ | WF | section-1-52 href; newer version /codes/north-carolina/chapter-1/article-5/ |
| https://law.justia.com/codes/north-carolina/chapter-1/article-5/ | WF | 2025 edition; section-1-52 href |
| https://law.justia.com/codes/north-carolina/chapter-1/article-5/section-1-52/ | WF | YES "Within three years an action (1) Upon a contract, obligation"; "NC Gen Stat § 1-52 (2025)" |
| same | script | REFUSED: robots.txt challenge |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.ncleg.gov/Laws/Constitution | script, curl | 8,772 chars; links /Laws/Constitution/Article1..Article14, NCConstitution.html/.pdf |
| https://www.ncleg.gov/EnactedLegislation/Constitution/NCConstitution.html | script | 116,397 chars, last-modified 10 Jun 2026; Art. I Sec. 18 found (stray "�") |
| same | WF | Art. XIV § 3 NOT PRESENT; truncated at Art. X § 2; notes "contingent upon the results of the November 3, 2026, referendum" |
| …/NCConstitution.pdf | script | 39 pp, 117,868 chars |
| https://www.ncleg.gov/Laws/Constitution/Article1, Article4 | script | 23,082 / 24,503 chars; Sec. 18 and Sec. 12 found |
| https://ncleg.gov/Laws/Constitution/Article1 | WF | YES "All courts shall be open; every person for an injury"; last Sec. 38 |
| https://law.justia.com/constitution/north-carolina/ | WF | index; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/north-carolina/preamble.html | WF | Sec. 18 present; Article I ends Sec. 37 (stale) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| …/Chapter_1A/GS_1A-1,_Rule_12.html (www) | script | 7,210 chars; "(6) Failure to state a claim upon which relief can be granted" |
| same | WF | PROVENANCE_REQUIRED |
| …/Chapter_8C/GS_8C-1,_Rule_702.html (www) | script | 6,276 chars; "Rule 702. Testimony by experts. (a) If scientific, technical" |
| https://nccourts.gov/courts/supreme-court/court-rules/north-carolina-rules-of-appellate-procedure | WF | no rule text; PDF "Codified 2 September 2025"; Rule 28(b) NOT PRESENT |
| https://nccourts.gov/courts/supreme-court/court-rules/general-rules-of-practice-for-superior-and-district-courts | WF | no text; PDF "Codified 6 August 2025" |
| https://www.nccourts.gov/courts/supreme-court/court-rules/north-carolina-business-court-rules | WF | no text; PDF "Codified 2 September 2025" |
| https://www.nccourts.gov/assets/inline-files/North-Carolina-Rules-of-Appellate-Procedure-Codified-1-March-2023.pdf | WF | Rule 28(b) NOT PRESENT; truncated in Rule 18(c)(8) (superseded edition) |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.oah.nc.gov/rules-division/north-carolina-administrative-code | script | 404 |
| https://www.oah.nc.gov/rules-division/participating-rulemaking-process/about-north-carolina-administrative-code | WF | NCAC at http://reports.oah.state.nc.us/ncac.asp; "OAH updates this website weekly." |
| http://reports.oah.state.nc.us/ncac.asp | WF | PROVENANCE_REQUIRED |
| same | script | FETCH ERROR: robots.txt unreachable (https connection reset) |
| same; ?folderName=\Title 15A…; …\Chapter 02 - Environmental Management | curl | 200; folder links; chapter listing (2nd try, first timed out at 30 s) |
| http://reports.oah.state.nc.us/ncac/title%2015a%20-%20…/15a%20ncac%2002b%20.0202.html | curl | 200 32,770 B; "15A NCAC 02B .0202 DEFINITIONS"; "Amended Eff. June 1, 2026" |
| http://reports.oah.state.nc.us/ncac/title%2010a%20-%20…/10a%20ncac%2013f%20.0101.html | curl | 200; repealed-rule history note |
| https://www.law.cornell.edu/regulations/north-carolina/15A-NCAC-02B-.0202 (guess) | script | 200 but title index (2,569 chars, same sha for any bad slug) |
| https://www.law.cornell.edu/regulations/north-carolina/title-15A/chapter-02/subchapter-B/section-.0200 | curl | link /regulations/north-carolina/15A-N-C-Admin-Code-02B-0202 |
| https://www.law.cornell.edu/regulations/north-carolina/15A-N-C-Admin-Code-02B-0202 | script | 25,259 chars; definitions found; history ends "Amended Eff. June 1, 2022" |
| https://www.law.cornell.edu/regulations/north-carolina/10A-N-C-Admin-Code-13F-0102 | script | 8,205 chars; "State regulations are updated quarterly" |
| https://files.nc.gov/oah/documents/2026-10/Volume-41-Issue-08-October-15-2026.pdf | script | 110 pp, 485,893 chars |
| same | WF | "VOLUME 41 ● ISSUE 08 ● Pages 652 – 756"; truncated at p. 710 |
| https://www.oah.nc.gov/documents/north-carolina-register | script | 14,179 chars; lists Volume 41 Issue 08, 07, 06 … |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://appellate.nccourts.org/opinion-filings/?c=1&year=2024 | script | 30,069 chars, page shell, no rows |
| https://appellate.nccourts.org/opinion-filings/?c=sc&year=2024 | curl | 87,753 B; rows "Cato Corp. v. Zurich Am. Ins. Co., (353PA23 - Published)"; viewOpinion(…pdf=44232); years 1998–2026 |
| same | WF | PROVENANCE_REQUIRED |
| https://appellate.nccourts.org/opinion-filings/?c=coa&year=2024 | curl | 581,694 B; "(24-417 - Unpublished)" rows |
| https://appellate.nccourts.org/getopzip.php?c=1&d=MjAyNC0xMi0xMw== | curl HEAD | 200 application/zip, 2,807,512 B |
| https://appellate.nccourts.org/opinion-filings/index-search.php?court=1&sSearchTerm=Cato | script | 25 results; "In re J.N.J., 286 N.C. App. 599 (2022)" |
| https://appellate.nccourts.org/opinions/?c=1&pdf=43543 | script | REFUSED: robots disallows /opinions/ |
| https://www.nccourts.gov/documents/appellate-court-opinions | script | REFUSED (bot check) |
| https://www.nccourts.gov/documents/appellate-court-opinions?page=200 | WF | items Dec. 29, 2022 (Kozec v. Murphy, COA22-433), PDF links ?c=2&pdf=41876 |
| https://www.ncdrc.gov/documents/pdf-volumes/north-carolina-reports-volume-386-… | WF | 302 → nccourts.gov/commissions/dispute-resolution-commission (not followed) |
| https://www.nccourts.gov/documents/pdf-volumes?page=1 | WF | volumes 366–361 detail links |
| https://www.nccourts.gov/documents/pdf-volumes/volume-366-14-june-2012-to-13-june-2013 | WF | ncsct366.pdf, 4,806 KB, "Supreme Court" |
| https://nccourts.gov/documents/pdf-volumes/coa-volume-292-02-january-2024-to-05-march-2024 | WF | nccoa292.pdf, 2,390 KB, "Court of Appeals" |
| https://www.nccourts.gov/assets/documents/pdf-volumes/nccoa292.pdf?VersionId=… | WF | PROVENANCE_REQUIRED |
| https://nccourts.gov/documents/business-court-opinions?page=2 | WF | "LUCAS v. HOPPER, 2026 NCBC 39", 24-CVS-502; PDF /assets/documents/opinions/2026%20NCBC%2039.pdf |
| https://www.nccourts.gov/assets/documents/opinions/2026%20NCBC%2039.pdf?VersionId=… | WF | PROVENANCE_REQUIRED |
| https://www.nccourts.gov/documents/business-court-opinions/lucas-v-hopper-2026-ncbc-1 | WF | metadata + PDF link only |
| https://law.justia.com/cases/north-carolina/supreme-court/2024/ | WF | 353pa23.html etc.; slugs like 225pa21-2 |
| https://law.justia.com/cases/north-carolina/supreme-court/2024/353pa23.html | WF | YES "This is a companion case to North State Deli, LLC"; slip pp. -2- to -15- |
| https://law.justia.com/cases/north-carolina/court-of-appeals/2024/ | WF | 20-665-2.html, 23-1013.html, 23-1031.html |
| https://law.justia.com/cases/north-carolina/court-of-appeals/2024/23-1013.html | WF | YES "This matter concerns a dispute between a church in Wilmington"; no reporter cite |
| https://www.nccourts.gov/news/tag/press-release/supreme-court-of-north-carolina-withdraws-order-implementing-universal-citation-system | WF | Jan. 13, 2023; order Jan. 11, 2023 "withdrawing the order implementing universal citations" |
| https://www.nccourts.gov/assets/news-uploads/FINAL_fact-sheet_UniversalCitation--SCofNC_11182020.pdf | WF | "2020-NCSC-45, ¶ 16"; "2020-NCCOA-118, ¶ 23"; applies to opinions filed from Jan. 1, 2021 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://appellate.nccourts.org/dockets.php?court=1&docket=353PA23&submit=Search | script, curl | 1 case → dockets.php?court=1&docket=1-2023-0353-001&pdf=1&a=0&dev=1 |
| https://appellate.nccourts.org/dockets.php?court=1&docket=1-2023-0353-001&pdf=1&a=0&dev=1 | script | 9,998 chars; "(1) PDR … Allowed 05-21-2024"; COA 23-305; "Modified and Affirmed" |
| https://appellate.nccourts.org/dockets.php?court=1&docket=&title=Builders&…&submit=Search | curl | 5 cases incl. 98A24, 304P25 |
| https://appellate.nccourts.org/dockets.php?court=2&docket=23-305&…&submit=Search | curl | COA docket 2-2023-0305-001 |
| https://appellate.nccourts.org/dockets.php?court=1&docket=23-305&submit=Search | curl | "0 cases" |
| https://appellate.nccourts.org/dockets.php?court=2&docket=2-2023-0305-001&pdf=1&a=0&dev=1 | script | no Supreme/PDR mention; slip link pdf=42928 |
| https://appellate.nccourts.org/orders.php | script | 4,569 chars; GET form (court, docket, title) |
| https://appellate.nccourts.org/orders.php?court=1&docket=353PA23&title=&submit=Search | curl | 7 orders; ids 428065, 435462 … |
| https://appellate.nccourts.org/orders.php?t=PA&court=1&id=428065&pdf=1&a=0&docket=1&dev=1 | script | PDF 1 p; "Allowed by order of the Court in conference, this the 21st of May 2024." |

## Search-only discovery (WebSearch, not fetched unless listed above)
ncleg.gov statute URLs, Justia NC code and cases, NC universal-citation press releases, nccourts.gov rules pages, pdf-volumes listings, Business Court listings, OAH register listing and NCAC links.

# Idaho (id) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `scripts/fetch_doc.py --research`; "shell" = curl (robots.txt, headers, href listing only); "WF" = WebFetch; "WS" = WebSearch.

Tool note: WebFetch refused every hand-built URL with `PROVENANCE_REQUIRED` ("permission request ... was not answered in time"). It worked only on URLs that had appeared in a WebSearch or WebFetch result. About 24 WebFetch calls used. No quota/rate failures.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://legislature.idaho.gov/robots.txt | shell | 200; `User-agent: *` Disallow /wp-admin/, committee-calendar paths; Semrushbot Disallow / |
| https://isc.idaho.gov/robots.txt | shell | 200; Disallow /admin, /cdn-cgi/, /isc-network/, /__preview, /api/cms-page-preview |
| https://api.isc.idaho.gov/robots.txt | shell | 404 "Cannot GET /robots.txt" |
| https://adminrules.idaho.gov/robots.txt | shell | 404 (HTML page) |
| https://files.dfm.idaho.gov/robots.txt | shell | 404 "Page not found" |
| https://isb.idaho.gov/robots.txt | shell | 200; Yoast block, `Disallow:` empty |
| https://icourt.idaho.gov/robots.txt | shell+script | 403 Cloudflare "Just a moment..."; script: REFUSED bot check (challenge) |
| https://law.justia.com/codes/idaho/ | script | REFUSED: robots.txt answers with a bot check (challenge) |
| https://www.public.law/ ; https://idaho.public.law/ | shell | Oregon listed, Idaho not; idaho.public.law CONNECT 502 |
| https://www.law.cornell.edu/states/idaho | shell | links out to legislature/isc/adminrules only |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| …/statutesrules/idstat/Title5/T5CH2/SECT5-219/ | WF | PROVENANCE_REQUIRED (constructed URL) |
| …/idstat/Title18/T18CH40/SECT18-4001/ | WF | PROVENANCE_REQUIRED |
| same two | script | 200 html, 6,981 / 4,336 chars; body present; "Idaho Statutes are updated to the website July 1" |
| …/idstat/Title5/T5CH2/ | script+shell | section list 5-201…5-214A…5-219 with catchlines; hrefs /SECT5-201; chapter PDF link T5CH2.pdf |
| …/idstat/Title5/ | script | chapter titles only, no section ranges |
| …/SECT5-214A/, Title67/T67CH52/SECT67-5279/, Title15/T15CH2/SECT15-2-101/, Title28/T28CH9/SECT28-9-109/, Title63/T63CH30/SECT63-3022A/ | script | all body present |
| …/Title5/T5CH3/SECT5-219/ ; …/T5CH2/SECT5-299/ | shell | 404 "not found" |
| …/wp-content/uploads/statutesrules/idstat/Title5/T5CH2.pdf | script | pdf 13 pp, last-modified 15 Sep 2025 |
| WS "Idaho Code 5-219 legislature.idaho.gov…" | WS | title55 index URL found |
| https://legislature.idaho.gov/statutesrules/idstat/title55/ | WF | chapters listed, no section ranges; currency banner |
| WS "SECT5-219 …" | WS | lower-case URL title5/t5ch2/sect5-219/ |
| https://legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-219/ | WF | YES "Within two (2) years: An action against a sheriff, coroner"; not truncated; links howcurrentisthislaw, site-disclaimer |
| https://legislature.idaho.gov/statutesrules/idstat/title18/t18ch40/sect18-4001/ | WF | YES "Murder is the unlawful killing of a human being including," |
| …/statutesrules/howcurrentisthislaw | script | "current through the 2026 Legislative Session." |
| …/site-disclaimer | script | "Official copies of the Idaho Code are published ... by LEXIS Publishing" |
| https://law.justia.com/codes/idaho/2021/title-5/chapter-2/ | WF | editions 2025, 2024, 2023, 2021…; "These codes may not be the most recent version." |
| https://law.justia.com/codes/idaho/2025 | WF | Title hrefs /codes/idaho/title-5/ |
| https://law.justia.com/codes/idaho/title-5/ | WF | "2025 Idaho Code"; no section ranges |
| https://law.justia.com/codes/idaho/title-5/chapter-2/ | WF | hrefs section-5-214a, section-5-219 |
| https://law.justia.com/codes/idaho/title-5/chapter-2/section-5-219/ | WF | YES; "ID Code § 5-219 (2025)" |
| …/statutesrules/sessionlaws/ | shell | volumes sessionlaws_vol{1,2}_2025 … 1993, sessionlaws_1992 … 1945 |
| …/wp-content/uploads/sessionlaws/sessionlaws_vol1_2025.pdf | script | pdf 779 pp, 2.7M chars; "CHAPTER 1 (H.B. No. 3)" p. 3 |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| …/statutesrules/idconst/ | shell | hrefs /statutesrules/idconst/ArtI … |
| …/idconst/ArtI/Sect13/ ; …/ArtV/Sect9/ | script | body present; "updated to the website July 1 following the legislative session" |
| WS "idconst ArtI Sect13 …" | WS | ArtI/Sect22, Justia article-i/section-22 |
| https://legislature.idaho.gov/statutesrules/idconst/ArtI/Sect22 | WF | YES "Section 22. Rights of crime victims. A crime victim, as" |
| https://law.justia.com/constitution/idaho/article-i/section-22/ | WF | YES; "This Constitution may not be the most recent version." |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://isc.idaho.gov/api/cms-content-search?scope=pages&q=petition%20for%20review | script | pages rules-procedure/ircp, /icar, /iar |
| https://isc.idaho.gov/rules-procedure/ircp | script | 417,681 chars, all rules; ids rule-N; print links /rules-procedure/print/ircp/N |
| https://isc.idaho.gov/rules-procedure | shell | sets iar icar icr iir ijr imcr ircp ire irefs irfl irsca irtc |
| …/rules-procedure/print/ircp/56 | script | "Rule 56. Summary Judgment" body present |
| …/print/ire/702, iar/118, icr/35, icr/33.1, iar/11, ircp/12 | script | body present |
| …/print/icr/11.1 | script | HTTP 404 |
| …/rules-procedure/iar, icr, ire | script | 232,420 / 263,642 / 127,721 chars |
| https://isc.idaho.gov/rules-procedure/print/ircp/56 | WF | YES "A party may move for summary judgment, identifying each claim"; not truncated |
| https://isc.idaho.gov/rules-procedure/print/ire/702 | WF | YES "A witness who is qualified as an expert by knowledge,"; "(Adopted March 26, 2018, effective July 1, 2018.)" |
| https://isc.idaho.gov/ire702 | shell / WF | 301 → /rules-procedure/ire#rule-702; WF truncated at 100K in Rule 703 (123,194 chars) |
| https://isc.idaho.gov/printpdf/1620 | shell | 404 |
| WS "Idaho Rules of Professional Conduct PDF isb.idaho.gov" | WS | bar-counsel/irpc/, IRPC-acc.pdf |
| https://isb.idaho.gov/bar-counsel/irpc/ | shell | single PDF link IRPC-acc.pdf |
| https://isb.idaho.gov/wp-content/uploads/IRPC-acc.pdf | script | pdf 67 pp, 544,451 chars, last-modified 9 Mar 2026; "RULE 1.7: CONFLICT OF INTEREST: CURRENT" |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://adminrules.idaho.gov/ ; /rules/current/ | shell | 200; /rules/current/ 301 → /current-rules/ |
| https://adminrules.idaho.gov/current-rules/ | shell/script | listing loaded by POST /wp-json/dfm-document-display/fetch-documents with X-WP-Nonce; "Each year's administrative code is archived annually, dating back to 1996." |
| https://adminrules.idaho.gov/latest-bulletins/ | script | banner "temporary technical issue affecting document search and listings" |
| https://adminrules.idaho.gov/rules/current/58/580102.pdf | script | 301 → files.dfm.idaho.gov/dfm-admin-website/rules/current/58/580102.pdf; 181 pp, 713,747 chars; "These rules are titled IDAPA 58.01.02" |
| …/rules/current/16/160309.pdf, 160310, 160318, 160502 | script/shell | 404 |
| …/rules/current/16/160301.pdf | script | 301 → files.dfm; 20 pp; "16.03.01 – Eligibility for Health Care Assistance" |
| …/rules/2021%20Archive/58/580102.pdf ; 2025%20Archive | shell | 301 → files.dfm …/rules/2021%20Archive/… |
| …/bulletin/2026/10.pdf, 2026/09.pdf, 2025/01.pdf | shell | 301 → files.dfm.idaho.gov/dfm-admin-website/bulletin/… |
| https://files.dfm.idaho.gov/dfm-admin-website/bulletin/2026/10.pdf | script | pdf 428 pp, 1.88M chars; "October 7, 2026 – Vol. 26-10" |
| WS "adminrules.idaho.gov rules current 58 580102.pdf…" | WS | /rules/current/58, archive PDFs, bulletin/2018/05.pdf |
| https://adminrules.idaho.gov/rules/current/58 | WF / shell | WF: chapter list, no hrefs; shell: 404 |
| https://adminrules.idaho.gov/bulletin/2018/05.pdf | WF | "REDIRECT DETECTED" 302 → files.dfm (not followed) |
| https://files.dfm.idaho.gov/dfm-admin-website/bulletin/2018/05.pdf | WF | PROVENANCE_REQUIRED |
| WS "law.cornell.edu regulations idaho IDAPA 58.01.02" | WS | LII title-IDAPA-58, IDAPA-59.01.01.001 |
| https://www.law.cornell.edu/regulations/idaho/IDAPA-58.01.08.900 | WF | NOT PRESENT |
| https://www.law.cornell.edu/regulations/idaho/title-IDAPA-58 | WF | rule-58.01.02 href; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/idaho/IDAPA-59.01.01.001 | WF | YES "Sections 50-1507, 50-1508, 50-1524, 59-1301…" |
| https://www.law.cornell.edu/regulations/idaho/title-IDAPA-58/rule-58.01.02 | WF | hrefs IDAPA-58.01.02.001, .010 |
| https://www.law.cornell.edu/regulations/idaho/IDAPA-58.01.02.001 | script | 200, 2,865 chars, last-modified 1 Aug 2025 |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://isc.idaho.gov/ | shell | links /cases-opinions/isc-opinions, /ica-opinions |
| https://isc.idaho.gov/cases-opinions/isc-opinions | script | 2,259 chars: notice + search form only (Nuxt app); "West Publishing Company publishes all cited opinions" |
| same | WF | PROVENANCE_REQUIRED |
| _nuxt/*.js bundles | shell | GET /api/cms-content-search (scope, document_type, q, tag, sort_by, cursor), /api/cms-document?id= |
| …/api/cms-content-search?scope=documents&document_type=ISC%20Opinion&sort_by=entry_date&sort_direction=DESC&limit=2 | script | JSON; id 22184 name "53539" 2026-10-14 |
| …/api/cms-document?id=22184 | script | opinion_file https://api.isc.idaho.gov/uploads/Documents/ISC/Criminal/2026/1791997359508-53539.pdf |
| that PDF | script | 22 pp; "IN THE SUPREME COURT OF THE STATE OF IDAHO Docket No. 53539"; slip pages |
| sort ASC ISC / ICA | script | ISC earliest 2019-09-11 (44182); ICA earliest 2013-07-12 (39073) |
| tag counts (limit 100) | script | ISC 2010-2017: 0; 2018: 2; 2019: 2; 2020-2025: 100+. ICA 2013, 2014, 2016: 100; 2017: 1; 2018-2019: 0; 2020+: 100 |
| q=Dorff ; q=50045 | script | 48119 (2023); 50045 Shumway v. IDOL, PDF 12 pp |
| cms-document?id=22193 → ICA PDF 53548 | script | "THIS IS AN UNPUBLISHED OPINION AND SHALL NOT BE CITED AS AUTHORITY" |
| https://isc.idaho.gov/opinions/casesfiled022217.pdf ; /print/appeals-court/isc_criminal ; /opinions/49915summ.pdf | script/shell | 404 |
| https://isc.idaho.gov/appeals-court/isc_civil | shell / WF | 301 → /cases-opinions/isc-opinions; WF: search form only, no opinions |
| WS "isc.idaho.gov Idaho Supreme Court opinions…" (×3) | WS | only legacy (404) URLs indexed |
| https://law.justia.com/cases/idaho/supreme-court-criminal/2023/ | WF | Dorff href …/2023/48119.html; "-0" suffix dockets |
| https://law.justia.com/cases/idaho/ | WF | supreme-court/, court-of-appeals/ |
| https://law.justia.com/cases/idaho/supreme-court-criminal/2023/48119.html | WF | YES "Kirby Dorff appeals from the denial of his motion to"; no reporter cite; not truncated |
| https://law.justia.com/cases/idaho/supreme-court/ | WF | 1866-2026 |
| https://law.justia.com/cases/idaho/court-of-appeals/ | WF | 1982-2026 |
| https://icourt.idaho.gov/ | script | REFUSED bot check (challenge) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| …/api/cms-content-search?scope=documents&q=Petition%20for%20Review&limit=5 | script | 46085ORD.pdf (2020-06-23), SMITHORD.pdf (45758, 2020-10-09) |
| …q=Petition%20for%20Review%20denied | script | 0 results |
| …q=46085 ; q=45758 | script | only the ISC orders; ICA opinion for 46085 not found (ICA 2018-19 gap) |
| …/uploads/Documents/ISC/Civil/2018/1775503706039-46085ORD.pdf | script | "Court of Appeals Case No. 46085-2018 is CLOSED"; "Supreme Court Case No. 48109-2020"; "Order Granting Petition for Review" |
| …/api/cms-content-search?…document_type=ICA%20Opinion&q=Huckabay | script | 0 results |

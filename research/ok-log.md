# Oklahoma (ok) probe log — 2026-10-17 (research)

Tools: S = `scripts/fetch_doc.py --research`, W = WebFetch, WS = WebSearch, C = curl (robots.txt only).

## OSCN (oscn.net)
| # | URL | Tool | Result |
|---|---|---|---|
| 1 | oscn.net/applications/oscn/DeliverDocument.asp?CiteID=69145 | S check | OK, robots permits (cached as 'ok, no rules') |
| 2 | oscn.net/applications/oscn/index.asp?ftdb=STOKST12&level=1 | S info/read/links | 200 html 89,393 chars; 'Title 12. Civil Procedure'; complete to § 3408; § 95 -> CiteID=439150, § 2012 -> 94873, § 2702 -> 94951 |
| 3 | DeliverDocument.asp?CiteID=439150 (12 O.S. § 95) | S | 15,447 chars; 'A. Civil actions other than for the recovery of real property'; Historical Data then Citationizer table |
| 4 | DeliverDocument.asp?CiteID=94873 (12 O.S. § 2012) | S | 38,320 chars; 'B. HOW PRESENTED. Every defense, in law or fact' |
| 5 | index.asp?ftdb=STOKST23&level=1 | S | **444-char page: 'Why am I seeing this? ... verify they are human'** (10:31:47); not detected as a wall by fetch_doc.py |
| 6 | index.asp?ftdb=STOKST21&level=1 | S links | § 701.7 -> CiteID=69297 |
| 7 | DeliverDocument.asp?CiteID=69297 (21 O.S. § 701.7) | S | 39,947 chars; 'Cite as: 21 O.S. § 701.7 (OSCN 2026)'. Script use of oscn.net stopped here |
| 8 | index.asp?ftdb=STOKST12&level=1 | W | PROVENANCE_REQUIRED (gated, not answered) |
| 9 | index.asp?level=1&ftdb=STOKCN&year= (from oklahoma.gov/libraries page) | W | ROBOTS_DISALLOWED |
| 10 | /robots.txt | W | ROBOTS_DISALLOWED |
| 11 | /robots.txt | C | HTML 'OSCN Turnstile' Cloudflare Turnstile form, 'verify they are human' |
| 12 | index.asp?ftdb=STOKST74&level=1 (from opers.ok.gov) | W | ROBOTS_DISALLOWED |

## Oklahoma Legislature
| 13 | oklegislature.gov/OK_Statutes/CompleteTitles/os12.pdf | S | REFUSED robots (Disallow: /*.pdf$) |
| 14 | oklegislature.gov/osstatuestitle.html?title=12, .../os12.rtf | S check | REFUSED robots (Disallow: /) |

## Justia (law.justia.com) — script: REFUSED (robots.txt bot check, host off for the day)
| 15 | law.justia.com/codes/oklahoma/title-12/section-12-95 | W | YES 'A. Civil actions other than for the recovery of real property'; '2025 Oklahoma Statutes' |
| 16 | .../title-21/section-21-701-7/ (built) | W | YES 'A person commits murder in the first degree when that' |
| 17 | .../title-12/section-12-2012/ (built) | W | YES B: 'Every defense, in law or fact, to a claim for' |
| 18 | .../codes/oklahoma/title-5/ | W | no appendix / rules entries |
| 19 | .../constitution/oklahoma/II-7.html | W | YES 'No person shall be deprived of life, liberty, or property,' |
| 20 | .../constitution/oklahoma/V-46.html (built) | W | YES 'The Legislature shall not, except as otherwise provided in this' |
| 21 | .../cases/oklahoma/supreme-court/2024/ | W | 81 entries, 2024 OK 1-83, slugs docket or citation |
| 22 | .../supreme-court/2024/121610.html | W | YES 'The State of Oklahoma moved to terminate Father's (Parker) parental rights.' ¶ numbers |
| 23 | .../cases/oklahoma/court-of-appeals-civil/ | W | years 1950-2026 |
| 24 | .../cases/oklahoma/ | W | 5 courts listed |
| 25 | .../court-of-appeals-criminal/ | W | years 1900-2026 |
| 26 | .../court-of-appeals-criminal/2024/ | W | 33 entries; Jimenez v. State 2024 OK CR 33 |
| 27 | .../court-of-appeals-criminal/2024/c-2023-951.html | W | YES 'On January 9, 2023, Petitioner, Luis Jimenez, entered a semi-blind plea' |
| 28 | .../court-of-appeals-civil/2024/ | W | 26 entries; decided 2024 but cited 2025 OK CIV APP N |
| 29 | .../court-of-appeals-civil/2024/121092.html | W | YES; 'Mandate Issued: 03/27/2025'; no cert note |
| 30 | law.justia.com/codes/oklahoma/title-12/section-12-95/ | S info | REFUSED (law.justia.com off for the day) |

## Oklahoma Senate
| 31 | oksenate.gov/sites/default/files/2019-12/oc2.pdf | S | PDF 13 pp; 'SECTION II-7 Due process of law.' |
| 32 | oksenate.gov/sites/default/files/2019-12/oc5.pdf | S | PDF 19 pp; 'SECTION V-46 Local and special laws' |
| 33 | oksenate.gov/sites/default/files/2022-01/AllOKConstitutionArticles.pdf | S | PDF 231 pp, 691,110 chars, LM 4 Jan 2022; II-7 at p.14, V-46 at p.41 |
| 34 | oksenate.gov/oklahoma-constitution, /constitution | S | 404 |
| 35 | accessible.oksenate.gov/search-statutes-constitution | S | 404 |

## Administrative code / register
| 36 | rules.ok.gov/ | S | REFUSED: robots.txt answered with a bot check |
| 37 | https://rules.ok.gov/ | W | PROVENANCE_REQUIRED |
| 38 | opers.ok.gov/statues-administrative-rules | W | links rules.ok.gov and OSCN title indexes |
| 39 | https://rules.ok.gov (from opers page) | W | PROVENANCE_REQUIRED (earlier request unanswered) |
| 40 | law.cornell.edu/regulations/oklahoma/Okla-Admin-Code-SS-310-667-1-1 (guess) | S | 200 but state title list (wrong slug) |
| 41 | .../regulations/oklahoma/title-310 -> chapter-667 -> subchapter-1 | S links | '§ 310:667-1-1 - Purpose' -> OAC-310-667-1-1 |
| 42 | .../regulations/oklahoma/OAC-310-667-1-1 | S | 2,512 chars; editorial note only; Notes 'Volume 39, Issue 24' |
| 43 | .../regulations/oklahoma/OAC-165-10-3-1 | S | 12,620 chars; '(1) Except as provided in (I) of this Section' |
| 44 | oklahoma.public.law/statutes/okla._stat._tit._12_sec._95 | S | FETCH ERROR: robots.txt unreachable (proxy 502) |

## Other
| 45 | oklahoma.gov/libraries/law-legislative-reference/library-laws-and-regulations.html | W | one oscn.net link (STOKCN) |
| 46 | okbar.org/ec/conduct/ | W | no ORPC text or links |

WebSearch: 7 queries (OSCN statute URLs; oklegislature titles; rules.ok.gov; Oklahoma Register; Justia 2024 cases; Justia constitution; ORPC PDF).
WebFetch calls: 23.

## Fix pass 2026-10-17 (from research/ok-verify.json)
- The OSCN rows are now blocked-robots: the independent check got fetch_doc.py REFUSED with robots 'User-agent: * Disallow: /'. The earlier Turnstile wall is kept as history.
- Justia: added the hazard and fallback for 2025 version-index pages that have no text (47 O.S. § 11-902, 10A O.S. § 1-1-105): use the linked 2024 edition and disclose it.
- Justia constitution: lettered-section slugs now tested (X-9A.html). Added hazards for case-name typos in Justia headers and for pages marked 'NOT RELEASED FOR PUBLICATION'.
- Regex: added the prose form '§ N of Title T of the Oklahoma Statutes', the trailing-marker form 'Rule 1.191, Okla. Sup. Ct. R.', and the West 'Okl.St.Ann.' form to the Pleading/Evidence Code pattern.
- No new fetches in this pass.

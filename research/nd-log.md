# North Dakota (nd) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "script" = `scripts/fetch_doc.py --research`; "WF" = WebFetch; "WS" = WebSearch.

Tool notes: WebFetch returned `PROVENANCE_REQUIRED` ("permission request ... not answered in time") for every built ndlegis.gov URL, the ndlegis.gov home page, and ndcourts.gov opinion/docket pages, even ones linked from a fetched page. URLs that came straight from search results went through. About 24 WebFetch calls used. No quota/rate failures.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.ndlegis.gov/robots.txt | script | 200 (redirect to ndlegis.gov); Drupal default: Disallow /core/, /admin/, /search/, /user/*, /survey/; /cencode/, /constit/, /information/acdata/, /admcode/ not covered |
| https://www.ndcourts.gov/robots.txt | script | served custom error page (customerrorpage?aspxerrorpath=/robots.txt), no rules = no robots file |
| https://www.ndcourts.gov/supreme-court/opinions?page=52 (and 2 more) | script | REFUSED: HTTP 403 (Cloudflare challenge); host off for the day |
| https://law.justia.com/robots.txt | script | REFUSED: robots.txt challenge (refusal cached from 14:42 today) |
| https://www.law.cornell.edu/robots.txt | script | 200; `User-agent: *` Crawl-delay 10; /regulations/ not disallowed |
| https://northdakota.public.law/robots.txt | script | proxy 502 Tunnel connection failed |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.ndlegis.gov/cencode/t12-1c32.pdf | script | PDF 22 pp, 96,133 chars; "CHAPTER 12.1-32 PENALTIES AND SENTENCING"; "12.1-32-01. Classification of offenses - Penalties." |
| https://www.ndlegis.gov/cencode/t28c01.pdf | script | PDF 10 pp, 36,801 chars; grep "28-01-16. Actions having six-year limitations." + body |
| https://www.ndlegis.gov/cencode/t10c19-1.pdf | script | PDF 95 pp, 394,274 chars; "10-19.1-150. Secretary of state - Forms" at p. 94 |
| https://www.ndlegis.gov/general-info/north-dakota-century-code | script | HTTP 404 (guessed path) |
| https://www.ndlegis.gov/cencode/t01.html | script links | chapter links t01c01.pdf and "Sections" t01c01.html |
| https://www.ndlegis.gov/cencode/t12-1.html | script links | t12-1c01.pdf … |
| https://www.ndlegis.gov/cencode/t28c01.html | script links | sections link t28c01.pdf#nameddest=28-01-01 … |
| https://ndlegis.gov/general-information/north-dakota-century-code/index.html | script | 3,598,176 chars; "is the official version of the North Dakota Century Code"; "07/01/25 UPDATE: All statutory changes approved by the 69th Legislative Assembly"; lists every section (28-01-16 at offset 1,560,456); links t04-1c01.pdf#nameddest=4p1-01-01, t04c02-1.pdf |
| https://www.ndlegis.gov/cencode/t28c01.pdf | WF | PROVENANCE_REQUIRED |
| https://www.ndlegis.gov/cencode/t10c19-1.pdf | WF | PROVENANCE_REQUIRED |
| https://www.ndlegis.gov/ | WF | PROVENANCE_REQUIRED |
| WS "ndlegis.gov cencode chapter 28-01 limitations pdf"; WS "\"cencode\" \"t28c01.pdf\""; WS "North Dakota Century Code 12.1-32-01 ndlegis.gov" | WS | no cencode PDF URLs; gave https://ndlegis.gov/general-information/north-dakota-century-code |
| https://ndlegis.gov/general-information/north-dakota-century-code | WF | official-version sentence and 07/01/25 UPDATE quoted; no hrefs; truncated at "6-01-17.1 Application fees" |
| https://law.justia.com/codes/north-dakota/title-28/chapter-28-01/section-28-01-16/ | WF | CLIENT_ERROR "There was an error while fetching." |
| WS "law.justia.com codes north-dakota title-28 …" | WS | /codes/north-dakota/2021/title-28/ and year editions |
| https://law.justia.com/codes/north-dakota/2021/title-28/ | WF | "2021 North Dakota Century Code Title 28"; newer 2025 link /codes/north-dakota/title-28/ |
| https://law.justia.com/codes/north-dakota/title-28/ | WF | "2025 North Dakota Century Code Title 28 - Judicial Procedure, Civil"; chapter href /title-28/chapter-28-01/ |
| https://law.justia.com/codes/north-dakota/title-28/chapter-28-01/ | WF | full text of 28-01-01 to 28-01-48 on chapter page; section headings not links |
| https://law.justia.com/codes/north-dakota/title-12-1/chapter-12-1-32/ | WF | YES "Offenses are divided into seven classes, which are denominated and"; through 12.1-32-16; not truncated |
| https://ndlegis.gov/research-and-archives/session-laws | script links | per-year pages 2015-2026 |
| https://ndlegis.gov/assembly/69-2025/regular/session-laws | script | REFUSED HTTP 403 (single URL, wrong path) |
| https://ndlegis.gov/assembly/69-2025/regular/2025-session-laws | script links | "2025 Session Laws - Full Book (PDF)" sl2025.pdf; "Chapter Categories" |
| https://ndlegis.gov/assembly/69-2025/regular/2025-session-laws/chapter-categories | script links | documents/appro.pdf, gnlpr.pdf, agric.pdf … |
| https://ndlegis.gov/assembly/69-2025/session-laws/documents/gnlpr.pdf | script | PDF 18 pp; "HOUSE BILL NO. 1031 … AN ACT to amend and reenact section 1-01-49" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://ndlegis.gov/constitution | script | "contains the current provisions of the state constitution"; links constit/preamble.pdf, a01.pdf … a14 |
| https://ndlegis.gov/constit/a01.pdf | script | 5 pp; "Section 9. All courts shall be open, and every man for any injury" ; last-modified 2016-12-08 |
| https://ndlegis.gov/constit/a06.pdf | script | 2 pp; "Section 2. The supreme court shall be the highest court of the state." |
| https://law.justia.com/constitution/north-dakota/ | WF | index only; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/north-dakota/article-i/ | WF | NOT PRESENT (section index) |
| https://law.justia.com/constitution/north-dakota/article-i/section-9/ | WF | YES "All courts shall be open, and every man for any injury done" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WS "ndcourts.gov legal-resources rules ndrcivp rule 56 …" | WS | /legal-resources/rules/ndrcivp/56, /56-1, /56-2 |
| https://www.ndcourts.gov/legal-resources/rules/ndrcivp/56 | WF | YES "A party claiming relief may move, with or without supporting declarations, for"; "Effective Date: 3/1/2021"; not truncated |
| https://ndcourts.gov/legal-resources/rules/ndrcivp | WF | rule links /ndrcivp/1 …; sets ndsupctadminr, ndrappp, ndrcivp, ndrcrimp, ndrct; no full-set PDF |
| WS "… ndrev 702 …" | WS | /ndrev/402-1, /ndrev/802, /ndrcrimp/26-2 |
| https://www.ndcourts.gov/legal-resources/rules/ndrev/802 | WF | YES "Hearsay is not admissible unless any of the following provides otherwise"; "Effective Date: 3/1/2014" |
| https://www.ndcourts.gov/legal-resources/rules | WF | PROVENANCE_REQUIRED |
| WS "… ndrct 3.2 …" | WS | /ndrct/3-2, /ndrct/3-2-3, /ndrappp/27, /local/east-central/1-1 |
| WS "… Rules of Professional Conduct 1.7" | WS | /legal-resources/rules/ndrprofconduct, /ndrlawyerdiscipl/1-2 |

## D — Administrative code and supplements
| URL | Tool | Result |
|---|---|---|
| https://ndlegis.gov/agency-rules/north-dakota-administrative-code/index.html | script | 294,369 chars; "Administrative Code is updated with quarterly changes"; links acdata/pdf/2-01-01.pdf, 4.5-02.1-01.pdf, 4-07-20.1.pdf |
| https://ndlegis.gov/information/acdata/pdf/43-02-03.pdf | script | 82 pp, 293,996 chars; "43-02-03-01. Definitions. The terms used throughout this chapter" |
| https://ndlegis.gov/information/acdata/pdf/75-02-02.pdf | script | 30 pp; table lists 75-02-02-09 Nursing Facility Level of Care |
| https://ndlegis.gov/administrative-rules-supplements | script | "Supplement 401 (October 2026)" … links admcode/arc202610401.pdf … |
| https://ndlegis.gov/admcode/arc202610401.pdf | script | 181 pp, 549,686 chars; "OCTOBER 2026 … ARTICLE 33-41 TATTOO AND BODY ART" |
| https://www.law.cornell.edu/regulations/north-dakota | script | title list (title-2 … title-4.5) |
| …/regulations/north-dakota/title-43 → /article-43-02 → /chapter-43-02-03 | script links | "(§ 43-02-03-01 to 43-02-03-101)"; section links N-D-A-C-43-02-03-01 |
| https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-43-02-03-01 | script | body "The terms used throughout this chapter have the same meaning"; Notes "Amended by Administrative Rules Supplement 2016-362" |
| https://www.law.cornell.edu/regulations/north-dakota/N-D-A-C-75-02-02-09 | script | "N.D. Admin Code 75-02-02-09 - Nursing facility level of care" |
| https://www.law.cornell.edu/states/north_dakota | script links | links out to legis.nd.gov, ndcourts.gov; LII hosts only the Administrative Code |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS "ndcourts.gov supreme-court opinion 2023 ND" | WS | listing pages ?page=52 … and news posts |
| https://www.ndcourts.gov/supreme-court/opinions?page=52 | WF | "2023 ND 171 Berger, et al. v. Sellers … Docket No. 20220322 … 9/28/2023"; no hrefs in text |
| https://www.ndcourts.gov/news/north-dakota/north-dakota-supreme-court/opinions/new-opinion-feb-23 | WF | Queen v. Martel, 2023 ND 32, docket link /supreme-court/Dockets/20220121 |
| https://www.ndcourts.gov/supreme-court/Dockets/20220121 | WF | PROVENANCE_REQUIRED |
| https://www.ndcourts.gov/supreme-court/opinions | WF | "681 - 690 of 12446 results"; no official-status statement |
| https://www.ndcourts.gov/supreme-court/opinion/2023ND32 | WF | PROVENANCE_REQUIRED |
| WS "\"ndcourts.gov/supreme-court/opinion/\"" (extended) | WS | news posts, /supreme-court/docket-search |
| https://www.ndcourts.gov/news/north-dakota/north-dakota-supreme-court/opinions/new-opinions-may-7-2026 | WF | 2026 ND 91-99 with links /supreme-court/opinions/2108xx (2026 ND 97 → 210815) |
| https://www.ndcourts.gov/supreme-court/docket-search | WF | "You do not need to register to search public appellate records"; system live April 8, 2024 |
| https://www.ndcourts.gov/supreme-court/opinions/210815 | WF | PROVENANCE_REQUIRED |
| WS "\"2026 ND 97\" Bismarck v. Herrera" | WS | rss?term=44641 and third-party sites |
| https://www.ndcourts.gov/rss?term=44641 | WF | "North Dakota Related Courts" feed (federal news); not ND opinions |
| https://www.ndcourts.gov/supreme-court/opinions?page=596 | WF | "State v. Guy, 2002 ND 19"; "Page 596 of 1,214"; 12,137 results |
| WS "\"ND App\" North Dakota Court of Appeals …" | WS | no ndcourts Court of Appeals listing found |
| https://law.justia.com/cases/north-dakota/supreme-court/2023/ | WF | Queen v. Martel → /2023/20220121.html; slug = docket; suffix -0 on shared dockets |
| https://law.justia.com/cases/north-dakota/supreme-court/2023/20220121.html | WF | YES "Lee Queen appealed from a judgment awarding him and Kimber Martel equal residential responsibility"; [¶1]-[¶5]; complete |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| WS "supremecourt.gov docket \"Supreme Court of North Dakota\" petition denied 2026" | WS | dockets 25-1349, 24A635, 26A210 |
| https://www.supremecourt.gov/docket/docketfiles/html/public/25-1349.html | script | "Lower Ct: Supreme Court of North Dakota"; "Case Numbers: (20250066)"; "Decision Date: March 4, 2026"; "Jun 17 2026 DISTRIBUTED for Conference of 9/28/2026." |
| https://www.supremecourt.gov/docket/docketfiles/html/public/24A635.html | script | "Lower Ct: Supreme Court of North Dakota"; "Case Numbers: (20240022)" |
| https://www.supremecourt.gov/docket/docketfiles/html/public/26A210.html | script | lower court is a U.S. Court of Appeals (not ND) |

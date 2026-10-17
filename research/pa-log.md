# Pennsylvania (pa) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `python3 scripts/fetch_doc.py --research` (obeys robots.txt and bot checks); "curl" = plain curl of robots.txt only; "WF" = WebFetch. About 28 WebFetch calls used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.palegis.us/robots.txt | curl (default UA) | 403, LDPC "403 Forbidden" HTML page |
| same | script (lsnet, project UA) | 200; only a `UserWay/Scanner` group (Disallow /cfdocs/, /legislation/bills/*); no `*` group → script treats all paths as allowed |
| https://www.legis.state.pa.us/robots.txt | curl | 403 (IIS 403.0) |
| https://www.pacodeandbulletin.gov/robots.txt | curl | 200; `User-agent: *` / `Disallow: /` (also GPTBot, Amazonbot etc. disallowed) |
| https://www.pacourts.us/robots.txt | curl | 404 (IIS "File or directory not found") |
| https://ujsportal.pacourts.us/robots.txt | curl | 404 (error page) |
| https://www.law.cornell.edu/robots.txt | (from DE run) | Crawl-delay 10; /regulations allowed |
| law.justia.com | script | REFUSED (Cloudflare challenge on robots.txt) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.palegis.us/statutes/consolidated | script | 200 html 21,787 chars; Title 0 (Constitution) … 79, each with History / HTML / PDF / Word links; no currency string |
| …/view-statute?txtType=HTM&ttl=42&div=0&chapter=55&section=24&subsctn=0 | script | 200 but 1,647 chars of nav only — text loads in an iframe (`loadIframe(...)`) |
| …/view-statute?iFrame=true&txtType=HTM&ttl=42&div=00.&chpt=55&sctn=24&subsctn=0 | script | 2,277 chars; "§ 5524. Two year limitation." "The following actions and proceedings must be commenced within two years"; history + cross refs |
| same | WF | ERROR ROBOTS_DISALLOWED |
| …/view-statute?txtType=HTM&ttl=18&div=00.&chpt=25&sctn=2&subsctn=0 | WF | ERROR ROBOTS_DISALLOWED |
| iFrame ttl=18 chpt=25 sctn=2 | script | "§ 2502. Murder." |
| iFrame ttl=13 div=0 chpt=27 sctn=25 | script | "could not be found" (Title 13 needs division) |
| iFrame ttl=13 div=2 chpt=27 sctn=25 (also div=02.) | script | "§ 2725. Statute of limitations in contracts for sale." |
| iFrame ttl=13 div=9 chpt=91 sctn=2 | script | "§ 9102. Definitions and index of definitions." |
| iFrame ttl=42 chpt=55 sctn=24.1 | script | not found |
| iFrame ttl=42 chpt=55 sctn=24 subsctn=1 | script | "§ 5524.1. Limitation and application for asbestos claims (Unconstitutional)." |
| iFrame ttl=42 chpt=1 sctn=2 (and sctn=02) | script | "§ 102. Definitions." |
| iFrame ttl=75 chpt=38 sctn=2; ttl=15 chpt=17 sctn=2; ttl=20 chpt=21 sctn=1; ttl=18 chpt=63 sctn=1 | script | §§ 3802, 1702, 2101, 6301 present |
| iFrame ttl=42 chpt=62A sctn=1 | script | "§ 62A01. Scope of chapter." |
| iFrame ttl=23 chpt=33 sctn=1 | script | chapter contents + "§ 3301. Grounds for divorce." |
| iFrame ttl=42 chpt=55 (no sctn) | script | whole chapter, 81,301 chars |
| …/view-statute?txtType=PDF&ttl=42 | script | PDF "Title 42.pdf", 845 pp, 2,607,722 chars; no currency line |
| https://www.palegis.us/statutes/consolidated/history?ttl_id=42 | script | 89,470 chars; latest entries "Amended Jul. 20, 2026, P.L.436, No.36" |
| https://www.palegis.us/legal | script | "presented AS IS without warranty"; "not intended to replace official versions" |
| https://www.palegis.us/data | script | bulk = Bill History XML zips (1969–), RSS, member data; no statute bulk |
| https://www.legis.state.pa.us/cfdocs/legis/LI/consCheck.cfm?txtType=HTM&ttl=42&div=0&chpt=55&sctn=24&subsctn=0 | script | redirected to palegis.us view-statute (…&chapter=55&section=24), 1,647-char nav shell |
| https://www.palegis.us/statutes/unconsolidated | script | browse by Act Year (1700s–2026) and by name (letter pages JS-filled) |
| …/unconsolidated/browse-by-name?letter=U | script | letter list only; names not in static HTML |
| …/unconsolidated/law-information?sessYr=1968&sessInd=0&actNum=387 | script | "Act No. 387 of 1968 UNFAIR TRADE PRACTICES AND CONSUMER PROTECTION LAW"; sections 1…10; PDF/HTML/Word links |
| …/unconsolidated/law-information/view-statute?txtType=HTM&SessYr=1968&ActNum=0387.&SessInd=0 | script | 1,683-char shell (iframe) |
| same + iFrame=true | script | 67,617 chars; "Section 2. Definitions.--As used in this act." ; no "P.S." cites in text |
| WebSearch "palegis.us statutes unconsolidated … 1968 Act 387" | search | no palegis hit; led to guessing law-information URL, then confirmed by fetch |
| https://law.justia.com/codes/pennsylvania/title-42/chapter-55/section-5524/ | WF | YES "The following actions and proceedings must be commenced within two"; "2025 Pennsylvania Consolidated & Unconsolidated Statutes"; "42 PA Cons Stat § 5524 (2025)" |
| https://law.justia.com/codes/pennsylvania/title-13/chapter-27/section-2725/ | WF | YES "(a) General rule.--An action for breach of any contract for"; 2025 edition (no division segment) |
| https://law.justia.com/codes/pennsylvania/ | WF | editions 2025…2010 (no 2011, 2013); no P.S. section |
| WebSearch "law.justia.com codes pennsylvania title 73 201-2" | search | only Pa.C.S. title pages |
| https://law.justia.com/codes/pennsylvania/title-73/ | WF | "Title 73 - TOWNSHIPS" (Pa.C.S. placeholder, "has not been implemented"); no Purdon's text |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| …/view-statute?iFrame=true&txtType=HTM&ttl=0&div=00.&chpt=1&sctn=11&subsctn=0 | script | "§ 11. Courts to be open; suits against the Commonwealth." "All courts shall be open; and every man for an injury" |
| iFrame ttl=0 chpt=5 sctn=10 | script | "§ 10. Judicial administration." |
| …/view-statute?txtType=PDF&ttl=0 | script | "The Constitution of Pennsylvania.pdf", 82 pp, 244,320 chars |
| https://law.justia.com/constitution/pennsylvania/ | WF | YES Art. I § 11 "All courts shall be open; and every man for an"; 139,081 chars, truncated at Art. V schedule; anchors #article1..#article11 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.palegis.us/statutes/pacode | script | PA Code title list linking to pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/{NNN}/{NNN}toc.html (incl. 201, 204, 207, 210, 225, 231, 234, 237, 246) |
| https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/231/chapter1000/s1035.2.html | script | REFUSED robots (Disallow: /) |
| same | WF | ERROR ROBOTS_DISALLOWED |
| https://www.law.cornell.edu/regulations/pennsylvania | script | titles 1…70, 101, 104, 107, 201, 204, 207, 210, 225, 231, 234, 237, 246 |
| …/title-231 → /part-I → /chapter-1000 → /subchapter-F | script | rule links of form /231-Pa-Code-r-1091 |
| /231-Pa-Code-SS-1035-2, /231-Pa-Code-Rule-1035-2, /231-Pa-Code-r-1035-2, /210-Pa-Code-SS-126 … | script | unknown slugs return the 2,879-char top index (same sha), not 404 |
| /231-Pa-Code-r-1035.2 | script | body + Notes "231 Pa. Code r. 1035.2 … 46 Pa.B. 3797" |
| same | WF | YES "After the relevant pleadings are closed, but within such time"; "State regulations are updated quarterly"; 46 Pa.B. 3797 |
| /210-Pa-Code-r-126 | WF | YES "(a) When citing authority, a party should direct the court's"; (b) "filed after May 1, 2019"; 49 Pa.B. 1335 |
| /225-Pa-Code-r-803 | script | body ends "regardless of whether the declarant is available as a witness:"; Notes 51 Pa.B. 7438 |
| /234-Pa-Code-r-600 | script | NO BODY: Notes say Rule 600 "rescinded October 1, 2012, effective 7/1/2013" — LII shows the rescinded old rule, not the replacement Rule 600 |
| /204-Pa-Code-r-81.4-1.7 | script | slug unknown → top index |
| https://www.law.cornell.edu/regulations/pennsylvania (headers) | script | last-modified Wed, 06 Aug 2025 |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| pacodeandbulletin.gov (all paths) | robots | `User-agent: *` Disallow: / — Code and Bulletin both blocked to script and WF |
| /regulations/pennsylvania/25-Pa-Code-SS-93.4 (dot) | script | top index (wrong slug) |
| /25-Pa-Code-SS-93-4, /55-Pa-Code-SS-187-26, /37-Pa-Code-SS-79-1 | script | bodies + Notes present (dot → hyphen for agency sections) |
| /25-Pa-Code-SS-93-4 | WF | YES "(a) Statewide water uses. Except when otherwise specified in law"; latest 30 Pa.B. 6059 |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.pacourts.us/courts/supreme-court/court-opinions | script | 58,472 chars; recent postings with PDF links /assets/opinions/Supreme/out/…; posting types incl. "Petitions for Allowance of Appeal"; Year select 1998–2026; Coveo/JS search form |
| https://www.pacourts.us/Themes/AOPC/assets/js/aopc.app.min.js | script (lsnet raw) | builds GET /api/opinion?month=&year=&courtType=&captionText=&authorName=&courtDocketNumber=&keywords=&postTypes=&publicationType=&sortDirection=&pageNumber= ; also startDate/endDate |
| /api/opinion?month=10&year=2026&courtType=Supreme&captionText=Roberts | script | JSON TotalItems 1: "Commonwealth v. Roberts, T., Pet. - No. 391 MAL 2026", paa |
| /api/opinion?month=10&year=2026&courtType=Superior&courtDocketNumber=1996%20EDA%202025 | script | parameter ignored: 132 items returned |
| /api/opinion?month=10&year=2026&courtType=Superior&captionText=1996%20EDA%202025 | script + WF | 1 item "Com. v. Ly, C.\r\nNo. 1996 EDA 2025", Memorandum, Non-Precedential |
| /api/opinion?month=10&year=2026&courtType=Superior&captionText=Cuong | script | 0 (captions abbreviate first names) |
| /api/opinion?month=&year=1998&courtType={Supreme,Superior,Commonwealth} | script | 137 / 142 / 187 items; month=1&year=1998 → 0 |
| /api/opinion?month=9&year=2026&courtType=Supreme&postTypes=mo | script | 2 items, Carr v. FCB 22 & 23 WAP 2025 |
| /assets/opinions/Superior/out/J-S20031-26m - 106963858377968335.pdf | script | 20 pp; "NON-PRECEDENTIAL DECISION - SEE SUPERIOR COURT O.P. 65.37"; No. 1996 EDA 2025 |
| /assets/opinions/Superior/out/J-S36002-26o - 106963096377907878.pdf | script + WF | 29 pp; "2026 PA Super 231"; In re D.E., No. 910 MDA 2026; WF complete to "Judgment Entered"; slip pages "- 2 -" |
| /assets/opinions/Supreme/out/J-27A-2026mo - 106920311373500212.pdf | WF | YES "JUSTICE MUNDY DECIDED: SEPTEMBER 10, 2026 The question raised in"; complete; no A.3d cite for itself |
| /assets/opinions/Commonwealth/out/987CD24_9-29-26.pdf | script + WF | 11 pp; "OPINION BY JUDGE McCULLOUGH FILED: September 29, 2026"; no neutral cite; complete |
| /assets/opinions/Superior/out/a45036.pdf (1998 file) | script | PDF 8 pp, last-modified 15 Jan 1999 |
| https://www.pacourts.us/courts/superior-court/court-opinions | WF | YES listing with captions, dockets, PDF links |
| /courts/{superior,commonwealth}-court/court-opinions | script | listings; RSS links /Rss/Opinions/{Court}/ |
| /Rss/Opinions/Supreme/, /Superior/, /Commonwealth/ | script | RSS 200, ~21–25K chars, dated 16 Oct 2026 |
| https://ujsportal.pacourts.us/CaseSearch | script | 200, 458K chars; POST form (DocketNumber, AppellateCourtName …) |
| https://ujsportal.pacourts.us/Report/PacDocketSheet?docketNumber=1996%20EDA%202025 | script | REFUSED HTTP 401 |
| https://law.justia.com/cases/pennsylvania/supreme-court/2026/ | WF | listing; slugs "22-wap-2025.html"; only supreme-court slug in nav |
| …/supreme-court/2026/22-wap-2025.html | WF | YES "The question raised in this discretionary appeal is whether the"; complete |
| …/superior-court/2026/ | WF | listing (2,271 results), memoranda included; slug "2753-eda-2024.html" |
| …/superior-court/2026/2753-eda-2024.html | WF | YES; "2026 PA Super 211"; complete |
| …/commonwealth-court/2026/ | WF | listing 611 opinions, first 500 shown; slug "358-m-d-2025.html" |
| …/commonwealth-court/2026/987-c-d-2024.html | WF | YES "Shahbaz Ather (Appellant) appeals from the March" |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| /assets/opinions/Supreme/out/391MAL2026 - 106963546377949705.pdf | script | 1 p; "Petition for Allowance of Appeal … is DENIED."; no Superior Court docket or date |
| /api/opinion?month=&year=2025&courtType=Supreme&captionText=Carr | script | "Patrick J. Carr, et al., Pet. v. FCB - No. 98 WAL 2025 (Granted)", paa |
| /api/opinion?…&captionText=First%20Commonwealth | script | 0 (caption abbreviates respondent to "FCB") |
| /assets/opinions/Supreme/out/98WAL2025 - 106510072326969493.pdf | script + WF | GRANTED order, 16 Sept. 2025; names neither Superior docket nor date |

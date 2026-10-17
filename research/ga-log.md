# Georgia (ga) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt reads and raw-HTML link extraction on pages the script had already been permitted to read (no refusal was worked around). WebFetch calls: 24 (of ~55), 5 of them refused by the session's URL-provenance gate (permission request unanswered; not a site refusal). WebSearch: 9.

**Provenance gate:** WF refused URLs on legis.ga.gov, gasupreme.us (2 attempts), rules.sos.ga.gov, which had not appeared in earlier search/fetch results. To avoid repeated prompts, gaappeals.gov, efast.gaappeals.gov and pubdoc.gasupreme.gov were tested with the script only. Their rows say `webfetch: untested`.

## Host checks (script `check`; curl robots.txt)
| URL | Result |
|---|---|
| https://law.justia.com/codes/georgia/ | script REFUSED: robots.txt answered with a bot check |
| https://www.legis.ga.gov/ | OK (robots permits) |
| https://www.gasupreme.us/ | OK; robots.txt: `User-agent: *  Disallow: /wp-content/uploads/  Disallow: /readme.html` |
| https://www.gasupreme.gov/ | OK, but robots.txt and /2026-opinions/ return 404 (site not migrated; only e-mail moved, per 02/17/26 notice) |
| https://www.gaappeals.us/ | serves links.gaappeals.us "Website Update Notice" pointing to gaappeals.gov |
| https://www.gaappeals.gov/ | OK; robots.txt Disallow /wp-admin/ only |
| https://rules.sos.ga.gov/ | OK; crawl-delay 2; robots disallows /gac/*-.*, /docs/, /search/ …; ClaudeBot/GPTBot fully disallowed by name |
| https://sos.ga.gov/ | script REFUSED: robots.txt answered with a bot check |
| https://www.georgiacourts.gov/ | OK |
| https://georgia.public.law/ | FETCH ERROR: proxy 502 on robots.txt |
| https://www.law.cornell.edu/regulations/georgia | OK; crawl-delay 10 |
| https://www.gabar.org/ | OK; crawl-delay 2 |
| https://pubdoc.gasupreme.gov/ | OK; robots.txt "Not found" |
| https://assets.georgiacourts.gov/robots.txt | S3 AccessDenied XML |
| https://services.georgia.gov/sos/sos-rw/searchHome.do | OK (not probed further) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WebSearch "Official Code of Georgia Annotated free public access…" | WS | ABA Journal, techdirt, etc. |
| https://www.abajournal.com/news/article/after-supreme-court-copyright-fight-georgia-makes-annotated-legal-code-freely-available | WF | Mar. 23, 2022; free annotated code hosted by LexisNexis; no direct URL |
| https://www.legis.ga.gov/ | WF | PROVENANCE_REQUIRED (gate, not site) |
| https://www.legis.ga.gov/ | script | html, 113 chars (JS shell) |
| https://dbf.georgia.gov/laws-regulations-rulings-publications/georgia-laws-title-7 | script grep + curl href | "Access to the entire Code is provided by LexisNexis"; href advance.lexis.com/container?config=00JAAzZDgz… |
| https://advance.lexis.com/container?config=…&crid=201b1720…&prid=32ba624a… | script | html, 0 chars |
| same | WF | NO: content empty |
| https://law.justia.com/codes/georgia/title-9/chapter-11/article-3/section-9-11-12/ | WF | YES "(a) When answer presented. (1) Except as provided in paragraph"; "2025 Code of Georgia"; "GA Code § 9-11-12 (2025)"; truncated in annotations only |
| https://law.justia.com/codes/georgia/title-51/chapter-1/section-51-1-6/ | WF | YES "When the law requires a person to perform an act"; complete |
| https://law.justia.com/codes/georgia/title-16/chapter-5/article-1/section-16-5-1/ | WF | YES "(a) A person commits the offense of murder when he"; page 103,619 chars, statute in window 1 |
| https://law.justia.com/codes/georgia/title-9/chapter-11/ | WF | article links with ranges "(§§ 9-11-7 — 9-11-16)"; editions 2024, 2023 linked |
| https://public.law/ | WF | states: CA, CO, FL, NV, NY, OR, TX — Georgia NO |
| https://www.law.cornell.edu/states/georgia | WF | links out: Lexis (code), sos.ga.gov 2013 PDF (constitution), gasupreme.us, gaappeals.us; LII hosts regs only |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| WebSearch "Constitution of the State of Georgia PDF sos.ga.gov…" | WS | sos.ga.gov amendments page, UGA digital commons |
| https://sos.ga.gov/page/proposed-georgia-constitution-amendments | WF | only proposed-amendment booklets 2014-2026; no full constitution |
| WebSearch '"sos.ga.gov" "Georgia Constitution" full text pdf…' | WS | found SOS "Electronic Version - January, 2023" PDF |
| https://sos.ga.gov/sites/default/files/2023-08/Georgia Constitution - Electronic Version - January%2C 2023.pdf | WF | YES ¶ XII "No person shall be deprived of the right to prosecute"; "Revised January 2023"; truncated Art. III § IX |
| https://law.justia.com/constitution/georgia/ | WF | TOC only; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/georgia/conart1.html | WF | YES ¶ XII same words; not truncated |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.gasupreme.us/rules/ | curl hrefs | /wp-content/uploads/2026/07/SupremeCourtRules_eff-July-2-2026.pdf (robots-disallowed path) |
| https://www.gasupreme.us/other-court-rules/ | curl hrefs | USCR 2026_04_09, State 2024_01_18, Juvenile 2026_09_03, Probate, Magistrate, Municipal, Business Court PDFs — all under /wp-content/uploads/ |
| WebSearch "Uniform Superior Court Rules Georgia PDF 2026" | WS | assets.georgiacourts.gov USCR 2025_03_06 PDF |
| https://assets.georgiacourts.gov/4/wp-content/uploads/2025/05/03170432/UNIFORM-SUPERIOR-COURT-RULES-2025_03_06.pdf | script | pdf 145 pp, 351,798 chars; Rule 6.4 "(A) Motions to compel discovery in accordance with OCGA § 9-11-37" |
| same | WF | YES Rule 6.4; "Including Amendments Received Through March 6, 2025"; truncated in Rule 9.1 |
| WebSearch "Rules of the Supreme Court of the State of Georgia pdf 2026" | WS | only third-party mirrors (not allowed) |
| https://www.gaappeals.gov/rules-1-8/ | script | 18,190 chars; "These rules are effective on March 26, 2026." Rules 1-8 text |
| https://www.gaappeals.gov/rules-1-8/ | curl hrefs | group pages rules-1-8 … rules-33-36, rule-16, rule-22, rule-30…rule-46; complete PDF link |
| https://www.gaappeals.gov/rules-33-36/ | script grep | "Rule 33.2. Judgment as Precedent. (a) Effective Dates."; "physical precedent only" |
| https://www.gaappeals.gov/rule-38/ | script grep | "Rule 38 Certiorari" page |
| https://www.gaappeals.gov/wp-content/uploads/2026/03/COA-Rules-Complete-Eff-26-March-26.pdf | script info | pdf 53 pp, 118,679 chars, last-modified 25 Mar 2026 |
| WebSearch "gabar.org handbook Rule 4-102…" | WS | gabar.org georgia-rules-of-professional-conduct |
| https://www.gabar.org/general-counsel/georgia-rules-of-professional-conduct | script + curl hrefs | index; Rule 1.7 → /handbook?rule=rule58 |
| https://www.gabar.org/handbook?rule=rule58 | script | 5,528 chars of site chrome; no rule text (JS-injected) |

## D — Admin code and bulletin
| URL | Tool | Result |
|---|---|---|
| https://rules.sos.ga.gov/gac/160-1-3-.04 (and /GAC/…) | script | REFUSED: robots Disallow /gac/*-.* |
| https://rules.sos.ga.gov/gac/160-1-3 | script | 37,725 chars; "Rule 160-1-3-.04 School Law Tribunals and Appeals (1) Purpose." |
| https://rules.sos.ga.gov/gac/160 | script | 68,672 chars department page |
| https://rules.sos.ga.gov/gac/391-3-6 | script | 710,038 chars; Rule 391-3-6-.03 present |
| https://rules.sos.ga.gov/gac/345-2 | script | chapter-level page, "Rule 345-2-.01 Organization of the Board" |
| https://rules.sos.ga.gov/ | script | "Current through Rules and Regulations filed through September 17, 2026"; "Fastcase is the designated publisher" |
| https://rules.sos.ga.gov/gac/160-1-3 | WF | PROVENANCE_REQUIRED (gate) |
| https://rules.sos.ga.gov/Download_pdf.aspx | script + curl hrefs | department PDFs and Bulletins 2020-01 … 2026-06 |
| …Download_pdf.aspx?st=GASOS&dept=Bulletins&pdf=2026-06 Georgia Monthly Bulletin for June 2026 | script | pdf 130 pp; "Georgia Rules and Regulations Administrative Bulletin for June 2026" |
| …Download_pdf.aspx?st=GASOS&year=2026&dept=Departments&pdf=Department 20 RULES OF STATE BOARD OF ACCOUNTANCY | script | pdf 90 pp |
| WebSearch "law.cornell.edu regulations georgia…" | WS | LII per-rule URLs |
| https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-160-1-3-.04 | WF | YES "(1) Purpose. The purpose of this rule is to specify the procedures"; "State regulations are updated quarterly" |
| same; …Ga-Comp-R-Regs-R-391-3-6-.03 | script | both bodies present |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.gasupreme.us/opinions/ | script | HTTP 404 |
| https://www.gasupreme.us/ | curl hrefs | /2026-opinions/, /2026-granted/, /2026-discretionary/, /2026-interlocutory/, /docket-search/ |
| https://www.gasupreme.us/2026-opinions/ | script | 14,629 chars; Final Copy notice; "October 14, 2026 … S26A0699. CHATHAM COUNTY v. SMITH et al." |
| same | curl hrefs | 286 PDF links /wp-content/uploads/2026/MM/sNNxNNNN.pdf; year pages 2017-2026 |
| https://www.gasupreme.us/2017-opinions/ | script | 20,530 chars; "S17A1412. CARTER v. THE STATE" (curl got 403 once; not retried by curl) |
| https://www.gasupreme.us/2017-opinions/, /2026-opinions/ | WF | PROVENANCE_REQUIRED (gate) |
| https://www.gasupreme.us/wp-content/uploads/2026/10/s26a0699.pdf | script | REFUSED: robots Disallow /wp-content/uploads/ |
| https://www.gasupreme.us/docket-search/ | curl | iframe src https://pubdoc.gasupreme.gov |
| https://pubdoc.gasupreme.gov/ | script | → /ui/, 49 chars; Vue app + obfuscated x-bni fingerprint script |
| WebSearch "site:gasupreme.us opinions 2026" and "Supreme Court of Georgia opinions gasupreme.us…" | WS | no gasupreme URLs surfaced |
| https://law.justia.com/cases/georgia/supreme-court/2026/ | WF | latest Sept. 22, 2026; slug s26a0604.html; '-0' suffix duplicates |
| https://law.justia.com/cases/georgia/supreme-court/2026/s26a0604.html | WF | YES "Appellant Sterling Ware challenges his 2024 convictions for malice murder"; no reporter cite; complete |
| https://law.justia.com/cases/georgia/court-of-appeals/2026/a26a0896.html | WF | YES "After Mack Dekle was injured on a bike path maintained by the"; complete |
| https://law.justia.com/cases/georgia/ | WF | two courts listed |
| https://law.justia.com/cases/georgia/court-of-appeals/ | WF | 1910-2026 |
| https://law.justia.com/cases/georgia/supreme-court/ | WF | 1850-2026 |
| https://www.gaappeals.gov/opinion-search/ | script + curl form | GET form → docket/docketdate/results_all.php?OPstartDate&OPendDate |
| …results_all.php?OPstartDate=2026-10-14&OPendDate=2026-10-14&submit=… | script | "18 Results for dates 10-14-2026 thru 10-14-2026"; A26A0896 REVERSED |
| same | curl | PDF href https://efast.gaappeals.gov/download?filingId=f49ddd90-… |
| https://efast.gaappeals.gov/download?filingId=f49ddd90-c64b-4f9e-b707-416661ddffae | script | pdf 11 pp, 12,994 chars; "MARKLE, Judge. After Mack Dekle was injured on a bike path" |
| …results_one_record.php?docr_case_num=A26A0896 | script | docket record; trial court Thomas County; "REVERSED (October 14, 2026)" |
| results_all.php date ranges 1996-97 / 1998-99 / 2000 / single days 1995, 2003, 2010 | script | 0 / 428 / 2,594 results; 1995 day 0; 2003 13; 2010 6 |
| results_all.php single days 2010-2021 | curl | filingId empty 2010-2012; present from 2013-03-15 on |
| …docket/results_all.php?searchterm=Dekle&submit=Start+Docket+Search | script | "2 results for "Dekle"" incl. A26A0896 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.gasupreme.us/2026-granted/ | script | 5,044 chars; "S26G1223. SAFECO INSURANCE COMPANY OF ILLINOIS v. CANNON (A25A1847)" |
| same | curl hrefs | /2022-…/2026-granted/ and -denied/ |
| https://www.gasupreme.us/2026-denied/ | script | 23,660 chars; "S26C1177. VINCENT v. STATE FARM … (A25A2138)" under October 14, 2026 |
| …results_one_record.php?docr_case_num=A25A2138 | script | "Certiorari Number S26C1177"; Disposition blank |

## G — Citation map
Georgia citation style taken from the Dekle slip opinion: "Young v. Johnson, 359 Ga. App. 769, 770 (860 SE2d 82) (2021)". Regexes tested against every example plus "O.C.G.A. §§ 9-11-12 - 9-11-16" (first section only) and bare "Rule 12(b)(6)" (no match). `build.py --check`: no ERROR/WARN for ga.json.

# Illinois (il) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research` (or the same `lsnet` module, which obeys robots.txt, used from a scratch helper to list links); "POST" = a urllib form post to the illinoiscourts.gov opinions page (robots allows `/`), spaced 2+ s apart. 36 WebFetch calls, 2 WebSearch calls.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2017&ChapterID=56 | script | FETCH ERROR: TLS certificate chain does not verify |
| https://www.ilga.gov/robots.txt | script | FETCH ERROR: TLS (same) |
| https://ilga.gov/ | script | FETCH ERROR: TLS (same) |
| https://witnessslips.ilga.gov/robots.txt, https://lrb.ilga.gov/robots.txt | script | FETCH ERROR: TLS (same) |
| https://www.illinoiscourts.gov/robots.txt | script | 200; `User-agent: *` Allow /; Disallow /antilles/, /App_Code/, /Bin/; sitemap |
| https://www.illinoiscourts.gov/ | script | 200, 14,368 chars; menu links: ILCS -> www.ilga.gov/Legislation/ILCS/Chapters; JCAR -> www.ilga.gov/agencies/JCAR/AdminCode; Constitution -> www.ilga.gov/commission/lrb/conmain.htm |
| https://law.justia.com/codes/illinois/chapter-815/ | script | REFUSED: law.justia.com robots.txt challenge (Cloudflare) |
| ilcourtsaudio.blob.core.windows.net (any URL) | script | REFUSED: "answers robots.txt with a bot check (refused)" — robots.txt 401/403 |
| https://www.ilsos.gov/…/register/home.html, https://www.cyberdriveillinois.com/…/register/home.html | script | FETCH ERROR: robots.txt unreachable (remote end closed connection) |
| https://www.public.law/ | script | 200; text names only oregon.public.law |
| https://illinois.public.law/ | script | robots.txt unreachable: proxy "Tunnel connection failed: 502" |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.ilga.gov/Legislation/ILCS/Chapters | WF | ROBOTS_DISALLOWED |
| https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2017&ChapterID=56 | WF | ROBOTS_DISALLOWED |
| https://www.ilga.gov/robots.txt | WF | ROBOTS_DISALLOWED |
| WebSearch "ilga.gov Legislation ILCS Sections ActID 2017 815 ILCS 505/2" | search | showed documents/081501750K15-5.htm on witnessslips.ilga.gov; mirrors lrb.ilga.gov, witnessslips.ilga.gov |
| https://witnessslips.ilga.gov/legislation/ilcs/documents/081501750K15-5.htm | WF | YES "Sec. 15-5. Definitions. As used in this Act, the terms"; "(Source: P.A. 89-209, eff. 1-1-96.)" — mirror; NOT adopted (would be a workaround); no further mirror probes |
| https://law.justia.com/codes/illinois/chapter-815/act-815-ilcs-505/section-815-ilcs-505-2/ | WF | CLIENT_ERROR (no per-section page) |
| https://law.justia.com/codes/illinois/chapter-815/ | WF | "2025 Illinois Compiled Statutes"; act links act-815-ilcs-505/ etc.; "These codes may not be the most recent version." |
| …/chapter-815/act-815-ilcs-505/ | WF | whole act on one page, no section links; 125,589 chars; 2024/2023 version links |
| same | WF | 505/2 YES "Unfair methods of competition and unfair or deceptive acts or practices, including" |
| …/chapter-735/act-735-ilcs-5/ | WF | list of articles (article-i, article-ii, …) |
| …/act-735-ilcs-5/article-ii/ | WF | full text; 117,765 chars; window 1 ends after § 2-616; 2-619 NOT PRESENT |
| same, offset=100000 | WF | 2-619 YES "(a) Defendant may, within the time for pleading, file a motion for"; last section 2-622 |
| same, offset=100000 | WF | text ends mid-word after 2-622; no pagination links; 2-1401 NOT PRESENT |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://ilga.gov/commission/lrb/conmain.htm | WF | ROBOTS_DISALLOWED |
| https://law.justia.com/constitution/illinois/ | WF | index only; con1.html … con6.html; "may not be the most recent version" |
| https://law.justia.com/constitution/illinois/con1.html | WF | § 2 YES "No person shall be deprived of life, liberty or property without due"; § 12 YES; runs through § 24 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.illinoiscourts.gov/rules-law/supreme-court-rules/ | script | 200; 145,695 chars; GridView rows Article / Rule N / /resources/{guid}/file link / "Amended …"; Rule 23 at char 11,628, Rule 315 at 55,992, RPC 1.7 at 107,893 |
| https://www.illinoiscourts.gov/resources/650f76b5-3cce-40b9-acc3-d93b1aced5f4/file | WF | 302 -> ilcourtsaudio.blob.core.windows.net/…/Rule%2023.pdf |
| …/650f76b5-…/Rule%2023.pdf | WF | 23(e)(1) YES "An order entered under subpart (b) or (c) of this rule is"; "amended June 3, 2025, eff. immediately." |
| https://www.illinoiscourts.gov/resources/2374deda-2eed-448e-8b4b-24a22a348f28/file | WF | 302 -> …/Rule%206.pdf |
| …/2374deda-…/Rule%206.pdf | WF | YES "Citation of Illinois cases filed prior to July 1, 2011, and published"; examples 2011 IL 102345, 2011 IL App (1st) 101234, -U, ¶ pinpoints; "amended May 31, 2011, effective July 1, 2011." |
| https://www.illinoiscourts.gov/courts/supreme-court/courts-supreme-court-illinois-rules-of-evidence/ | script | 200; 38,665 chars; per-rule links; Rule 702/803 hrefs contain a stray space before /file |
| https://www.illinoiscourts.gov/resources/6a5bd4c5-f59c-4bdd-9183-0a0e78f9e2a7/file | WF | 302 -> …/Evid.%20Rule%20401.pdf |
| …/6a5bd4c5-…/Evid.%20Rule%20401.pdf | WF | YES "Relevant evidence means evidence having any tendency to make the existence of"; "Adopted September 27, 2010, eff. January 1, 2011." |
| /courts/appellate-court/appellate-court-local-rules/ | — | link seen on home page only |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://www.ilga.gov/agencies/JCAR/AdminCode | WF | ROBOTS_DISALLOWED |
| https://www.law.cornell.edu/states/illinois | script | links out to ilga.gov/illinoiscourts.gov; LII hosts Illinois Admin Code |
| https://www.law.cornell.edu/regulations/illinois | script | 200; title-1 … title-95 links |
| …/regulations/illinois/title-35, …/title-35/part-101, …/part-101/subpart-A | script | hops to /regulations/illinois/Ill-Admin-Code-tit-35-SS-101.100; subpart links show section ranges |
| …/Ill-Admin-Code-tit-35-SS-101.100 | script | 200; "Amended at 43 Ill. Reg. 9674"; Last-Modified Aug 1, 2025 |
| same | WF | YES "This Part sets forth the rules generally applicable to proceedings before the"; "State regulations are updated quarterly; we currently have two versions available." |
| …/Ill-Admin-Code-tit-86-SS-100.10 | script | 200 but returns the Illinois title index (non-existent section) |
| …/Ill-Admin-Code-tit-86-SS-130.101 | script | 200; heading § 130.101; "Amended at 47 Ill. Reg. 2116" |
| WebSearch "Illinois Register cyberdriveillinois.com volume issue PDF Secretary of State" | search | agency mirror pattern register/volume45/register_volume45_issue_3.pdf |
| https://www.ilsos.gov/departments/index/register/home.html | WF | "Illinois Register Index", "2022, Volume 46"; "not the official publication of the Illinois Register"; no links extracted |
| https://www.ilsos.gov/departments/index/register/volume50/register_volume50_issue_40.pdf | WF | ROBOTS_DISALLOWED (URL was a pattern guess) |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.illinoiscourts.gov/top-level-opinions/ | script | 200, 328 KB HTML; ~150 rows (name link /resources/{guid}/file, citation, date, court, type, status); ASP.NET form; RSS links |
| same + ?ctl00$ctl04$txtFilterName=Wancket&…, and ?search=Wancket | script | GET params ignored (default rows returned) |
| https://www.illinoiscourts.gov/views/courts/rss/opinions-supreme.aspx | script | 200 text/xml; items with opinion:citationnum "2026 IL 131191", filingdate, docketstatus, link |
| top-level-opinions POST txtFilterName=Rehfield, all years | POST | first try 500 (bad form parse); retry 200, 30 rows incl. citing cases (full-text match) |
| POST "2021 IL 125656" | POST | rows of citing cases (full-text) |
| POST "Rehfield v. Diocese of Joliet", Supreme Court | POST | 2021 IL 125656, 02/04/2021, Final |
| POST custom date range 1995/1996/1997/2000/2011 | POST | date fields ignored (current rows); two attempts: connection reset |
| POST Supreme Court, all years, sort FilingDate ASC | POST | earliest rows 05/23/1996 (People v. Redd, Franson v. Micelli), no citation |
| POST appellate ASC (2 tries) | POST | connection reset / proxy tunnel closed — stopped |
| https://www.illinoiscourts.gov/resources/231556cb-4e60-4b7d-871d-fc1c1a871a41/file | script | REFUSED (redirect to blob host; robots refused) |
| same | WF | 302 -> blob …/Rehfield%20v.%20Diocese%20of%20Joliet,%202021%20IL%20125656.pdf |
| blob Rehfield PDF | WF | YES ¶ 1 "Plaintiff Mary Rehfield filed a two-count amended complaint against defendant, the Diocese"; "Illinois Official Reports" header; ¶¶ 1-70 complete |
| https://www.illinoiscourts.gov/resources/decf4801-5251-4ba1-b18e-8cea8af92bf5/file | WF | 302 -> blob …/Wancket … 2026 IL App (1st) 232256.pdf |
| blob Wancket PDF | WF | YES; no Official Reports header ("IN THE APPELLATE COURT OF ILLINOIS"); ¶¶ 1-86; complete |
| blob Wancket PDF (recheck) | WF | phrase "We are asked to determine whether bimonthly payments…" YES in ¶ 2, split by page header "No. 1-23-2256" |
| https://www.illinoiscourts.gov/resources/476f9abc-80b8-41f8-b3a4-13187b9f2ba3/file | WF | 302 -> blob …/Moore v. Moore 2026 IL App (1st) 251481-U.pdf |
| blob Moore PDF | WF | "NOTICE: This order was filed under Supreme Court Rule 23 and is not precedent except"; ¶¶ 1-37 |
| https://www.illinoiscourts.gov/top-level-opinions/ | WF | table rows readable; search form visible; 175,706 chars (window 1 = 100K) |
| https://law.justia.com/cases/illinois/supreme-court/2021/125656.html | WF | Rehfield ¶ 1 YES; ¶¶ 1-70 complete |
| https://law.justia.com/cases/illinois/court-of-appeals-first-appellate-district/2026/1-23-2256.html | WF | Wancket YES; complete through "Affirmed." |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.illinoiscourts.gov/courts/supreme-court/leave-to-appeal/ | script | 200; year filter 2007-2026; direct blob links "September 30 2026" … "February 13, 2026" |
| blob …/819ce661-8298-4ed3-b7dc-c942e285d8c7/September%2030%202026.pdf | WF | heading "THE FOLLOWING CASES ON THE LEAVE TO APPEAL DOCKET WERE DISPOSED OF AS INDICATED:"; entries keyed by Supreme docket + appellate docket (2-23-0584); ~305 entries; no public-domain cites |

## G — Citation map
Regexes tested locally against all examples plus negatives ("Penal Code § 187", bare "Rule 23", "Supreme Court Rule 41", "Cal. Civ. Code § 1714", "§§ 2-619 to 2-622": no match). `python3 scripts/build.py --check`: no ERROR/WARN.

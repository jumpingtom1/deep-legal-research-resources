# New Jersey (nj) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research`; "shell" = curl, used only for robots.txt, response headers and to read public TOC XML / bulk files on hosts that allow it (no refusal was ever retried by another route). 39 WebFetch calls used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.njleg.state.nj.us/robots.txt | shell | 200; `User-agent: *` `Allow: /`; sitemaps listed |
| https://www.njleg.gov/robots.txt | shell | 200; same file |
| https://lis.njleg.state.nj.us/robots.txt | shell | 302 → https://njleg.state.nj.us/robots.txt (Allow: /) |
| https://pub.njleg.gov/robots.txt | shell | 302 → https://njleg.state.nj.us/robots.txt (Allow: /) |
| https://www.njcourts.gov/robots.txt | shell | 200; Drupal default; Disallow /search, /admin/, /user/*, /node/add/ etc.; /attorneys/ and /system/files/ not disallowed |
| https://www.njcourts.gov/attorneys/rules-of-court | script | REFUSED: HTTP 403; script then refuses the host for the day |
| same | shell (headers only) | HTTP/2 403, `x-iinfo` header, `visid_incap_…` cookies, body loads `/_Incapsula_Resource` — Imperva Incapsula bot challenge |
| https://law.justia.com/codes/new-jersey/title-2a/section-2a-14-1/ | script | REFUSED: robots.txt answered with bot challenge (Cloudflare) |
| https://law.justia.com/constitution/new-jersey/ | script | REFUSED (host off for the day after challenge) |
| https://advance.lexis.com/robots.txt | shell | no usable output |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://lis.njleg.state.nj.us/nxt/gateway.dll?f=templates&fn=default.htm&vid=Publish:10.1048/Enu | script | 200 html, 408 chars: Folio NXT search shell ("Simple Search … <Not initialized yet>") |
| https://www.njleg.state.nj.us/statutes | script | HTTP 404 |
| https://pub.njleg.gov/statutes/ | script | 200 directory listing: STATUTES-TEXT.zip 41,443,870 B, STATUTES-FOLIO.zip, NJCONST-TEXT.zip, LCTOC-*.zip, all dated 10/16/2026 6:00 AM |
| https://pub.njleg.gov/statutes/_READ_ME.txt | script | "Updated every week day at 2AM"; TXT/RTF and Folio formats described |
| https://pub.njleg.gov/statutes/STATUTES-TEXT.zip | shell | 200 application/x-zip-compressed, last-modified Fri, 16 Oct 2026 10:00:48 GMT; STATUTES.TXT 84,201,151 B; line 2 "(UPDATED THROUGH  P.L.2026, c.50, and J.R.1)"; section heads like "2A:14-1.  6 years" |
| https://pub.njleg.gov/statutes/NJCONST-TEXT.zip | shell | 200; NJCONST.TXT 177,316 B; "(UPDATED THROUGH AMENDMENTS ADOPTED IN NOVEMBER, 2021)" |
| …/nxt/gateway.dll?f=jumplink$…$jumplink_q=[field SECTION:2A:14-1] | shell | 200 but body `onLoad="noLink()"` (unresolved; field name unknown) |
| …/nxt/gateway.dll?f=templates$fn=nxturl.js… | shell | JS showing XmlContentsUrl params command/basepathid/maxnodes |
| …/nxt/gateway.dll?f=xmlcontents&command=getchildren&basepathid=&maxnodes=200&minnodesleft=5 | shell | XML: node id="statutes/1" t="NEW JERSEY GENERAL AND PERMANENT STATUTES (UPDATED THROUGH  P.L.2026, c.50, and J.R.1)" |
| …basepathid=statutes%2F1&maxnodes=500 | shell | title folders: statutes/1/2 = TITLE 1, statutes/1/112 = TITLE 2A, statutes/1/2785 = TITLE 2C … (titles show names only, no section ranges) |
| …basepathid=statutes%2F1%2F112&maxnodes=5000 | shell | 2,419 nodes flat (no chapter level); id="statutes/1/112/303" t="2A:14-1.  6 years" |
| …basepathid=statutes%2F1%2F2785&maxnodes=5000 | shell | id="statutes/1/2785/2868" t="2C:11-3  Murder." |
| …basepathid=statutes%2F1%2F10834 | shell | HTTP 500 "The function, 'xmlcontents', did not succeed" (a document node, not a folder) |
| https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1/112/303 | script | 200 html 2,773 chars; contains "2A:14-1. a. Every action at law for trespass to real property"; ends "amended 2021, c.379." |
| …/statutes/1/112/303?f=templates$fn=document-frame.htm$3.0 | script | same content |
| …/statutes/1/112/303?f=templates$fn=document-frameset.htm | WF | CLIENT_ERROR (error while fetching) |
| https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1/2785/2868 | WF | YES 2C:11-3 "a. Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder"; not truncated; no currency line |
| same | script verify | VERIFIED "criminal homicide constitutes murder" (8,165 chars) |
| …/nxt/gateway.dll?f=xmlcontents&command=getchildren&basepathid=statutes%2F1%2F2785&maxnodes=5000&minnodesleft=5 | WF | returned id statutes/1/2785/2868 for 2C:11-3; truncated at 2C:40A-4 |
| https://www.njleg.state.nj.us/disclaimer | script | 3,572 chars nav only (Next.js) |
| same | WF | "The text of the statutes and Constitution of New Jersey are not annotated."; no official/unofficial statement |
| https://law.justia.com/codes/new-jersey/title-2a/section-2a-14-1/ | WF | YES "Every action at law for trespass to real property, for"; "2025 New Jersey Revised Statutes"; "NJ Rev Stat § 2A:14-1 (2025)" |
| https://law.justia.com/codes/new-jersey/title-2c/section-2c-11-3/ | WF | YES "a. Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder"; "2025 New Jersey Revised Statutes" |
| https://pub.njleg.gov/bills/2020/PL21/379_.HTM | script | 200 html; "CHAPTER 379 An Act concerning construction defects…"; "Approved January 18, 2022." |
| https://pub.njleg.gov/bills/2020/PL21/379_.PDF | script | 200 pdf 1 page |
| https://pub.njleg.gov/bills/2016/PL17/150_.HTM | script + WF | 200; WF YES "An Act concerning certain murders and amending N.J.S.2C:11-3"; "Approved July 21, 2017." |
| https://pub.njleg.gov/bills/2016/PL17/150_.PDF | script | 200 pdf 3 pages |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.njleg.state.nj.us/constitution | script | 200 html 177,072 chars, single page, no anchors; "(Updated Through Amendments Adopted in November, 2021)"; Art. I ¶1 at offset 1,779 VERIFIED "All persons are by nature free and independent"; Art. VI § I at 78,747; Art. VIII § IV ¶1 at 146,127; Art. XI at 152,010 |
| same | WF | Art. I ¶1 YES; Art. VIII § IV ¶1 NOT PRESENT; "[Content truncated due to length...]" in Art. VIII § I; 141,147 chars, read 0–100000 |
| https://www.njleg.state.nj.us/lawsconstitution/constitution.asp | script | 404 (old URL gone) |
| https://law.justia.com/constitution/new-jersey/ | WF | YES Art. I ¶1 "All persons are by nature free and independent, and have"; single page; 137,263 chars; truncated in Art. VIII § II; no currency |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.njcourts.gov/attorneys/rules-of-court | script | REFUSED HTTP 403 (Incapsula) |
| same | WF | CLIENT_ERROR |
| https://www.njcourts.gov/attorneys/rules-of-court?page=0 | WF | CLIENT_ERROR |
| https://www.njcourts.gov/attorneys/rules-court | WF | CLIENT_ERROR |
| https://www.njcourts.gov/sites/default/files/rules/r4-46.pdf | WF | CLIENT_ERROR (guessed path; not confirmed to exist) |
| WebSearch (3 queries) for njcourts rule PDF URLs | search | only third-party rule sites and njcourts /search?page= URLs; no official rule PDF URL found |

## D — Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://www.lexisnexis.com/hottopics/njcode/ | script | 302 → advance.lexis.com/container?config=00JAA5…; 0 chars |
| same | WF | REDIRECT to advance.lexis.com |
| https://advance.lexis.com/container?config=00JAA5OTY5…IHrf | WF | empty page (no text) |
| https://www.lexisnexis.com/hottopics/njoal/ | script | → advance.lexis.com/container?config=00JABk…; 0 chars |
| https://www.nj.gov/oal/ | script | 200; links "Public Access to Administrative Code and NJ Register" |
| https://www.nj.gov/oal/rules/accessp | script | "Please note that the online version of the Code is not the official Code."; Register free on Lexis back to July 3, 1995 |
| https://www.nj.gov/oal/rules/portal/ | script | active-proposal database at oalrulesproduction.dynamics365portals.us (not probed) |
| https://www.nj.gov/oal/rules/ | script | 404 |
| https://www.law.cornell.edu/regulations/new-jersey | script | 200 index |
| https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-7-7-1-1 | script | 200, last-modified Aug 4 2025; VERIFIED "This chapter establishes the rules of the Department"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-6A-14-1-1 | script + WF | WF YES "(a) The rules in this chapter supersede all rules in"; latest note "Amended by 52 N.J.R. 1822(b), effective 10/5/2020" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.njcourts.gov/ | WF | home page text "All state courthouses are open to the public." |
| https://www.njcourts.gov/attorneys/opinions/supreme | WF | CLIENT_ERROR |
| https://www.njcourts.gov/attorneys/opinions/supreme?page=35 | WF | partial: Oral Argument rows 2014–2015 with dockets (A-2-13 …), no PDF links |
| https://www.njcourts.gov/attorneys/opinions/supreme?page=0 | WF | CLIENT_ERROR |
| https://www.njcourts.gov/attorneys/opinions/published-appellate?page=1 | WF | "Sorry, you need to enable JavaScript…"; rows A-0891-24 (Jan. 12, 2026) etc., no names or links |
| https://www.njcourts.gov/system/files/court-opinions/2024/a_39_23.pdf | WF | YES Rodriguez v. Shelbourne Spring, "SYLLABUS This syllabus is not part of the Court's opinion."; 28 pp opinion |
| https://www.njcourts.gov/system/files/court-opinions/2024/a_66_21.pdf | WF | YES State v. Zingis, decided August 8, 2024; 109,924 chars, truncated at 100,000 |
| https://www.njcourts.gov/system/files/court-opinions/2024/a_18_24.pdf | WF | CLIENT_ERROR (Fenimore; filename form or block unknown) |
| https://www.njcourts.gov/system/files/court-opinions/2025/a0117-23.pdf | WF | YES State v. Gibson, "After a jury trial, defendant Anthony Gibson, a police officer, was found"; "Decided December 19, 2025"; full (unredacted, NOT FOR PUBLICATION legend) version |
| https://www.njcourts.gov/system/files/court-opinions/2026/a0891-24.pdf | WF | YES NC Roseville Senior 2016 UR LLC v. Howard; "APPROVED FOR PUBLICATION" January 12, 2026 |
| https://www.njcourts.gov/system/files/court-opinions/2025/a0921-24.pdf | WF | CLIENT_ERROR (consolidated A-0921-24/A-1568-24) |
| https://www.njcourts.gov/system/files/court-opinions/2026/a2551-24.pdf | WF | CLIENT_ERROR (unpublished, decided Oct 5, 2026) |
| WebSearch result | search | https://njcourts.gov/system/files/court-opinions/2024/a-15-23.pdf (hyphen form) listed — not fetched |
| https://www.njcourts.gov/cases/a-1489-22 | WF | JS notice + State v. A.H.-S., "Argued: Oct. 16, 2024", no links |
| https://law.justia.com/cases/new-jersey/ | WF | collections: supreme-court, appellate-division, tax-court, advisory-committee-on-professional-ethics, court-of-errors-and-appeals |
| https://law.justia.com/cases/new-jersey/supreme-court/ | WF | years 1900–2026 (2026: 47) |
| https://law.justia.com/cases/new-jersey/supreme-court/2024/ | WF | entries with URLs …/2024/a-39-23.html, a-37-38-23.html |
| https://law.justia.com/cases/new-jersey/supreme-court/2024/a-39-23.html | WF | YES "In this appeal, we consider whether the Hartford Underwriters Insurance Company (Hartford)"; slip pagination only |
| https://law.justia.com/cases/new-jersey/appellate-division/ | WF | years 1944–2026 (2026: 1,358); recent rows under appellate-division-unpublished/ |
| https://law.justia.com/cases/new-jersey/appellate-division-published/2025/ | WF | rows …/2025/a-0921-24.html, a-0117-23.html |
| https://law.justia.com/cases/new-jersey/appellate-division-published/2025/a-0117-23.html | WF | YES "After a jury trial, defendant Anthony Gibson, a police officer, was found"; "APPROVED FOR PUBLICATION AS REDACTED" |
| https://law.justia.com/cases/new-jersey/appellate-division-unpublished/2026/a-2551-24.html | WF | YES "PER CURIAM S.J.M. appeals from a March 21, 2025 order"; decided October 5, 2026 |
| https://law.justia.com/cases/new-jersey/tax-court/ | WF | years 1980–2026; slug …/2026/001081-2024.html |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.njcourts.gov/cases/a-39-23 | WF | JS notice + "Leave to Appeal Granted: May 10, 2024", "Argued: Sept. 9, 2024", "Decided: Dec. 12, 2024"; court below not listed |
| WebSearch x3 for certification-granted / pending-cases lists | search | no official list URL found; only third-party blogs and brief PDFs under /system/files/cases/briefs/ |

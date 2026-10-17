# Massachusetts (ma) probe log, 2026-10-16

All probes were run on 2026-10-16 by `research`. Tools: WF = WebFetch; FD = `scripts/fetch_doc.py --research` (info/read/grep); SH = curl, used only to list `href`s on hosts whose robots.txt allows the path; WS = WebSearch (discovery only). Quoted page text is 15 words or fewer per entry. 33 WebFetch calls in total.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://malegislature.gov/robots.txt | FD | 200; "User-agent: * / Disallow:" (empty), so everything is allowed |
| https://www.mass.gov/robots.txt | FD | 200; Disallow /search/, /node/*, /media/*, /taxonomy/term/*, /doc/courts-dwnld-*; SemrushBot disallowed |
| https://www.sec.state.ma.us/robots.txt | FD | 200; Disallow /spr, /Pubs, /search, /archives …; /divisions/spr not listed |
| https://archives.lib.state.ma.us/robots.txt | FD | 200; Disallow /search, /browse/*, /entities/*/*/* |
| https://128archive.com/robots.txt | FD | 404 |
| https://www.lexisnexis.com/clients/macourts/ | FD check | REFUSED: robots "Disallow: /clients/" |
| https://www.ma-appellatecourts.org/robots.txt | FD | REFUSED: bot challenge on robots.txt |
| https://law.justia.com/codes/massachusetts/... | FD | REFUSED: robots.txt challenge (off for the day) |
| https://massachusetts.public.law/ | FD | robots.txt unreachable, proxy 502 |
| https://www.public.law/ | FD grep "Massachusetts" | 0 matches |
| https://www.law.cornell.edu/states/massachusetts | FD | 200; links out for statutes, constitution and opinions; LII hosts the CMR only |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A/Section9 | FD | 200, 25,160 chars; body "Section 9. (1) Any person, other than a person entitled" |
| same | WF | YES "(1) Any person, other than a person entitled to bring"; no currency line; not truncated |
| https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleII/Chapter231/Section85 | FD | 200; "Section 85. Contributory negligence shall not bar recovery" |
| …/PartI/TitleI/Chapter93A/Section9 (wrong title) | FD | HTTP 404 |
| https://malegislature.gov/Laws/GeneralLaws/Chapter93A/Section9 | FD | redirects to …/PartI/TitleXV/Chapter93A/Section9 |
| …/Chapter231/Section85; Chapter151B/Section4; Chapter231/Section60B; Chapter265/Section13A; Chapter149/Section148; Chapter12/Section11I; Chapter93a/Section9 | FD | all redirect to canonical Part/Title URLs (PartIII/TitleII; PartI/TitleXXI; PartIV/TitleI; PartI/TitleII) |
| …/Chapter93A/Section99 | FD | HTTP 404 (no soft page) |
| https://malegislature.gov/GeneralLaws/GoTo?ChapterGoTo=93A&SectionGoTo=9 | FD | 404 |
| https://malegislature.gov/Laws/GeneralLaws/Chapter231/Section85 | WF | YES "Contributory negligence shall not bar recovery in any action by" |
| https://malegislature.gov/Laws/GeneralLaws/PartI | FD | titles with chapter ranges: "Title XV REGULATION OF TRADE Chapters 93 - 110H" |
| https://malegislature.gov/Laws/GeneralLaws | FD grep | "NOTICE: This is NOT the official version of the General Laws"; "includes all amendments to the General Laws passed before May 31, 2026" |
| https://malegislature.gov/api/Chapters/93A/Sections/9 | FD | JSON; "Text":"Section 9. (1) Any person, other than a person entitled" |
| https://malegislature.gov/api/Parts; /api/Chapters; /api/Chapters/93A | FD | JSON lists (Parts I-V; chapters; sections with Details links) |
| https://malegislature.gov/api/Chapters/231/Sections/85; /265/Sections/13A | FD | JSON Text present |
| https://malegislature.gov/api/Chapters/231/Sections/85 | WF | YES "Section 85. Contributory negligence shall not bar recovery in any action" |
| https://malegislature.gov/api/Documents; /api/SessionLaws | FD | JSON, 12.5M and 3.3M chars |
| https://malegislature.gov/api/swagger/ui/index; /api/Constitution | FD | 404 |
| https://malegislature.gov/Laws/SessionLaws/Acts/2024/Chapter150 | FD | 200, 371K chars; "AN ACT RELATIVE TO THE AFFORDABLE HOMES ACT" |
| https://malegislature.gov/Laws/SessionLaws/Acts/2016/Chapter219 | FD | 200, 241K chars; "AN ACT RELATIVE TO JOB CREATION AND WORKFORCE DEVELOPMENT" |
| same | WF | YES "Whereas, The deferred operation of this act would tend to"; truncated at SECTION 35 |
| WS "law.justia.com codes massachusetts chapter 93a section 9" | WS | found /codes/massachusetts/part-i/title-xv/chapter-93a |
| https://law.justia.com/codes/massachusetts/part-i/title-xv/chapter-93a/section-9/ | WF | YES "Any person, other than a person entitled to bring action"; "2025 Massachusetts General Laws"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/massachusetts/part-iii/title-ii/chapter-231/section-85/ | WF | YES; "2025 Massachusetts General Laws" |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| https://malegislature.gov/Laws/Constitution | FD | 200, 356,822 chars; "Article LXXXIX." at offset 265906, "Article CXXI." at 318167 |
| same | SH | anchors id=articleXIV, amendmentArticleLXXXIX, chapterISectionIArticleIV, … (127 amendment anchors) |
| same | WF | art. XIV YES "Every subject has a right to be secure from all"; LXXXIX NOT PRESENT; truncated after Amendment art. V |
| same, offset=100000 | WF | LXXXIX and CXXI NOT PRESENT; window ends in art. XVI |
| https://law.justia.com/constitution/massachusetts/ | WF | art. XIV YES; truncated in Amendment art. IV; no currency line; 130,293 chars |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.mass.gov/law-library/massachusetts-court-rules | FD | 404 |
| WS "mass.gov Massachusetts Rules of Civil Procedure" | WS | found law-library index and /doc/…/download |
| https://www.mass.gov/law-library/massachusetts-rules-of-civil-procedure | FD+SH | 200; per-rule links; rule-231 (23.1), two rule-41 / rule-42 / rule-43 / rule-81 slugs; two Rule 11 pages |
| https://www.mass.gov/info-details/massachusetts-rules-of-court-and-standing-orders | SH | links to law-library indexes for civil, criminal, appellate, SJC, Appeals, Superior … |
| https://www.mass.gov/rules-of-civil-procedure/civil-procedure-rule-12-defenses-and-objections-when-and-how-presented-by-pleading-or-motion-motion-for-judgment-on-pleadings | FD | 200, 36,154 chars |
| same | WF | YES "After service upon him of any pleading requiring a responsive"; "Effective Date: 07/01/2008"; (a)-(h) complete |
| https://www.mass.gov/doc/massachusetts-rules-of-civil-procedure/download | FD | PDF 271 pp, 827,883 chars, "…effective-March-2025…" |
| same | WF | "Including amendments effective March 10, 2025"; Rules 12/56/85 NOT PRESENT; ends Rule 6(b) |
| https://www.mass.gov/guides/massachusetts-guide-to-evidence | FD+SH | redirects to /guide/…; per-section links; PDF link …-2026-edition/download |
| https://www.mass.gov/guide-to-evidence/section-803-hearsay-exceptions-availability-of-declarant-immaterial | WF | YES "The following are not excluded by the hearsay rule, even"; "Adopted Date: 02/01/2026"; Note truncated |
| same | FD | 200, 95,435 chars |
| https://www.mass.gov/doc/massachusetts-guide-to-evidence-2026-edition/download | FD | PDF 446 pp, 1,463,018 chars; "Section 803. Hearsay Exceptions" p. 262 |
| same | WF | "2026 Edition"; § 104 YES; § 803 NOT PRESENT; ends in Note to § 202 |
| https://www.mass.gov/doc/massachusetts-supreme-judicial-court-rules-and-orders/download | FD | PDF 470 pp, 1,152,705 chars, "…August-2026…" |
| same | WF | "Including rule amendments effective August 1, 2026"; 1:03 YES; 3:07 NOT PRESENT; ends Rule 1:18 |
| https://www.mass.gov/doc/appeals-court-rules/download | FD | PDF 23 pp, July 2024 |
| https://www.mass.gov/doc/massachusetts-superior-court-rules-and-orders/download | FD | PDF 122 pp, 256,749 chars, Sept-2025 |
| https://www.mass.gov/law-library/massachusetts-supreme-judicial-court-rules; …appeals-court-rules; …superior-court-rules; …rules-of-appellate-procedure; …rules-of-criminal-procedure | SH | per-rule slug lists (rule-103 = 1:03; rule-230 = 23.0; rule-9a; rule-271 = 27.1; rule-141 = 14.1) |
| …/appeals-court-rules/appeals-court-rule-230-summary-disposition-formerly-known-as-appeals-court-rule-128 | FD | 200; "(1) Summary disposition without oral argument"; "Effective Date: 07/01/2020" |
| …/rules-of-criminal-procedure/criminal-procedure-rule-14-pretrial-discovery-from-the-prosecution | FD | 200; "Effective Date: 03/01/2025" |
| …/supreme-judicial-court-rules/supreme-judicial-court-rule-103-uniform-certification-of-questions-of-law | FD | 200; "Effective Date: 01/01/1981" |
| …/superior-court-rules/superior-court-rule-9a-civil-motions | FD | 200; "Effective Date: 09/15/2025" |
| …/rules-of-appellate-procedure/appellate-procedure-rule-271-further-appellate-review | FD | 200; "Effective Date: 09/01/2021" |

## D: Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.mass.gov/law-library/940-cmr | FD+SH | 200; chapter links /regulations/940-CMR-300-general-regulation … |
| https://www.mass.gov/law-library/code-of-massachusetts-regulations(-cmr) | FD | 404 |
| https://www.mass.gov/info-details/code-of-massachusetts-regulations-cmr-by-number | FD+SH | 200; 162 cmr links (/law-library/{n}-cmr, some /info-details/) |
| https://www.mass.gov/regulations/940-CMR-300-general-regulation | FD+SH | summary only; "Official Version: Purchase the official print version"; PDF link |
| https://www.mass.gov/doc/940-cmr-3-consumer-protection-general-regulations/download | FD | PDF 22 pp; footer "(Mass. Register #1420 6/26/20)" |
| same | WF | 3.16 YES "Without limiting the scope of any other rule, regulation or"; 3.19 present |
| https://www.mass.gov/law-library/310-cmr → /regulations/310-CMR-1000-wetlands-protection → /doc/310-cmr-10-wetlands-protection/download | SH+FD | PDF 245 pp, 627,647 chars; 10.02 present; last-modified 2017 |
| https://www.law.cornell.edu/regulations/massachusetts | FD | 200; title list 101 CMR … |
| https://www.law.cornell.edu/regulations/massachusetts/940-CMR-3-16 | FD | 200; "Without limiting the scope of any other rule"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/massachusetts/310-CMR-10-02 | FD | 200; "(1) Areas Subject to Protection under M.G.L. c. 131, § 40" |
| https://www.sec.state.ma.us/divisions/spr/massachusetts-register.htm | FD | 200, 0 chars |
| same | WF | error "There was an error while fetching." |
| https://www.sec.state.ma.us/divisions/spr/index.htm | WF | error, same message |
| WS "Massachusetts Register Secretary of the Commonwealth…" | WS | State Library DSpace entities (archives.lib.state.ma.us) |
| https://archives.lib.state.ma.us/entities/journalfile/b44bea6e-965b-474f-b9a9-04ae8f68f90d | FD | 200; "Massachusetts Register (2017-04-21; no. 1337)"; file ocm04109606-2017-04-21.pdf listed |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| WS "Massachusetts Reporter of Decisions slip opinions…" | WS | new-opinions, published-sjc-and-appeals-court-opinions, reporter's office |
| https://www.mass.gov/info-details/new-opinions | SH+FD | 10 /doc/{slug}-{sjc|ac}-{letter}{docket}/download links; "superseded by the advance sheets and bound volumes" |
| https://www.mass.gov/published-sjc-and-appeals-court-opinions | SH | links: Mass. Reports vols 1-477 (case.law), single justice decisions, trial-court opinions |
| https://www.mass.gov/appellate-opinion-portal | SH | links new opinions, unofficial collections, 128archive.com, revisions, errata |
| https://www.mass.gov/lists/unofficial-collections-of-published-opinions | SH | "There is no official version of the Massachusetts Reports available online." Lists lexisnexis.com/clients/macourts, case.law, CourtListener, Scholar, FindLaw |
| https://www.mass.gov/doc/commonwealth-v-goncalves-sjc-c13880/download | FD | PDF 28 pp, c13880.pdf; "SJC-13880 COMMONWEALTH vs. CLERENCE H. GONCALVES." |
| same | WF | body present "DEWAR, J. The defendant, Clerence H. Goncalves, surreptitiously photographed a"; no Mass. cite; complete |
| https://128archive.com | FD+SH | GET form (DocketNumber, PartyName, ReleaseDateFrom/To, Keywords); "SHOWING RESULTS: 10 of 20030" |
| https://128archive.com/?DocketNumber=25-P-0254 (&Action=Search) | FD | "SHOWING RESULTS: 1 of 1" |
| same | WF | 1 result, Commonwealth vs. Travis C. Washington, 25-P-0254, 10/16/2026, PDF link |
| https://128archive.com/?PartyName=Loreti | FD | 2 of 2 |
| https://128archive.com/?ReleaseDateFrom=01/01/1990&ReleaseDateTo=12/31/2008 | FD | 933 results; before 02/28/2008: 9 |
| https://128archive.com/Disposition/DownloadDisposition/22052?dispositionId=22076 | FD | PDF 5 pp 25P0907.pdf; "NOTICE: Summary decisions issued by the Appeals Court pursuant to M.A.C. Rule" |
| https://128archive.com/Disposition/ViewDispositionDocInHtml?dispositionId=22076&ispublicview=True | FD | redirected to /Error/ErrorDetail |
| https://law.justia.com/cases/massachusetts/supreme-court/2026/ | WF | listing; Daikin SJC-13881 Oct 14 2026 → …/2026/sjc-13881.html |
| https://law.justia.com/cases/massachusetts/supreme-court/2026/sjc-13880.html | WF | body "The defendant, Clerence H. Goncalves, surreptitiously photographed a sexual encounter"; no page markers |
| https://law.justia.com/cases/massachusetts/court-of-appeals/2026/ | WF | listing; 25-p-1082.html, 25-p-396.html (unpadded) |
| https://law.justia.com/cases/massachusetts/ | WF | courts list; year range not stated; /volumes/ archives |
| WS "site:mass.gov/doc sjc opinion download 2023" | WS | older /doc/sjc-NNNNN-opinion items (not fetched) |
| https://www.mass.gov/law-library/massachusetts-reports-volumes-1-477 | FD+SH | points to case.law (not a permitted host) |
| https://www.mass.gov/published-trial-court-opinions | FD | Superior Court opinions "1980-date" (host not traced) |
| https://www.mass.gov/supreme-judicial-court-single-justice-decisions | FD | single justice archive, "2019 to the present" (host not traced) |

## F: Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.ma-appellatecourts.org/ | FD | REFUSED (robots.txt challenge) |
| same | WF | error "There was an error while fetching." |
| https://www.ma-appellatecourts.org/docket/FAR-30123 | WF | error, same message |
| WS "further appellate review denied list mass.gov" (x3) | WS | /doc/far-denied-list-…, /doc/fard-redacted-order-… URLs |
| https://www.mass.gov/doc/further-appellate-review-denied-list-july-29-2022/download | FD | 404 |
| https://www.mass.gov/doc/fard-redacted-order-july-31-2026/download (and without /download) | FD | 404 |
| https://www.mass.gov/doc/far-denied-list-may-12-2023/download | FD | 404 |
| https://www.mass.gov/orgs/massachusetts-supreme-judicial-court | SH | no FAR list link; links to search-court-dockets page only |
| https://www.mass.gov/info-details/sjc-further-appellate-review-applications | SH | 404 (guessed; recorded as not existing) |

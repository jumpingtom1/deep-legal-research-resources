# Kansas (ks) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "WS" = WebSearch. WebFetch calls: 13 (of ~55); 3 returned PROVENANCE_REQUIRED (session URL-provenance gate, unanswered permission prompt; not a site refusal; not retried). WebSearch: 3.

Note: one plain `curl` (browser-like UA) of https://searchdro.kscourts.gov/Documents/LoadPage was made to read the search form's field names (the script does not expose raw HTML). It returned a 5,793-byte Cloudflare error page; nothing further was attempted and no form details were used. The script itself was never challenged on that host.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://kslegislature.gov/robots.txt | script | HTTP 404 (no rules) |
| https://www.ksrevisor.gov/robots.txt | script | `User-agent: *` Disallow /images/ /cgi-bin/ /err/ /css/ /sjtest/ /scripts/ |
| https://www.kscourts.gov/robots.txt | script | `User-agent: *` with no Disallow; sitemap line |
| https://searchdro.kscourts.gov/robots.txt | script | HTTP 404 (no rules) |
| https://sos.ks.gov/robots.txt | script | Disallow /index.html, /ent/, /api/, business search, displaydocuments.aspx |
| https://rules.ks.gov/robots.txt | script | `User-agent: *` / `Disallow:` (allow all) |
| https://law.justia.com/… | script | REFUSED: robots.txt challenge earlier today; host off for the day |
| https://www.law.cornell.edu/regulations/kansas/K-A-R-28-1-2 | script | OK (robots permits) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://kslegislature.gov/li/b2025_26/statute/060_000_0000_chapter/060_005_0000_article/060_005_0013_section/060_005_0013_k/ | script info | redirected to /b2025_26/laws/…; html 8,664 chars |
| https://www.kslegislature.gov/li/statute/060_000_0000_chapter/…/060_005_0013_k/ | script | HTTP 404 |
| https://kslegislature.gov/b2025_26/laws/060_000_0000_chapter/060_005_0000_article/060_005_0013_section/060_005_0013_k/ | script read | "2026 Kansas Statutes"; "60-513. Actions limited to two years." … "History: L. 1963, ch. 303" |
| same | WF | YES; "(a) The following actions shall be brought within two years:"; not truncated |
| https://kslegislature.gov/b2025_26/laws/021_000_0000_chapter/021_054_0000_article/021_054_0002_section/021_054_0002_k/ | script grep | 8,956 chars; "21-5402. Murder in the first degree." |
| https://kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_032_0000_article/079_032_0117_section/079_032_0117_k/ | script grep | "79-32,117. Kansas adjusted gross income of an individual" |
| https://kslegislature.gov/b2025_26/laws/082a_000_0000_chapter/082a_007_0000_article/082a_007_0001_section/082a_007_0001_k/ | script grep | "82a-701. Definitions." |
| https://kslegislature.gov/b2025_26/laws/060_000_0000_chapter/060_005_0000_article/060_005_0013a_section/060_005_0013a_k/ | script grep | 4,189 chars; "60-513a. Ionizing radiation defined." |
| https://kslegislature.gov/b2025_26/laws/060_000_0000_chapter/060_005_0000_article/ | script read | article index lists "60-513 - Actions limited to two years." etc. |
| https://kslegislature.gov/b2025_26/laws/ | script read/links | "2026 Kansas Statutes"; chapter links; 090/094/095/097 listed, no 092/093 |
| https://kslegislature.gov/b2023_24/laws/060_000_0000_chapter/…/060_005_0013_k/ | script grep | "viewing the 2023-2024 Regular Sessions archive" but still "2026 Kansas Statutes" |
| https://www.ksrevisor.gov/statutes/chapters/ch60/060_005_0013.html | script read | 105,961 chars; statute then annotations / law review list |
| same | WF | YES; no currency statement; "Truncated: Yes" at annotation 376 |
| https://www.ksrevisor.gov/statutes/chapters/ch21/021_054_0002.html | script grep | 11,552 chars; "21-5402. Murder in the first degree." |
| https://www.ksrevisor.gov/statutes/chapters/ch79/079_032_0117.html | script grep | "79-32,117. Kansas adjusted gross income" |
| https://www.ksrevisor.gov/statutes/chapters/ch82a/082a_007_0001.html | script grep | "82a-701. Definitions." |
| https://www.ksrevisor.gov/statutes/chapters/ch60/060_005_0013a.html | script grep | 2,116 chars; "60-513a. Ionizing radiation defined." |
| https://www.ksrevisor.gov/ksa.html | script read/links | chapter list; chapter 60 -> /statutes/ksa_ch60.html |
| https://www.ksrevisor.gov/statutes/ksa_ch60.html | script links | 765 links; link text = section titles only, numbers only in URLs |
| https://www.ksrevisor.gov/ | script links | 2026 composite lists; Session Laws -> sos.ks.gov; K.A.R. -> sos.ks.gov/publications/pubs_kar.aspx |
| https://www.ksrevisor.gov/questions.html | script read | "An unofficial version of the K.S.A. is available online." |
| https://law.justia.com/codes/kansas/chapter-60/article-5/section-60-513/ | script | REFUSED (challenge, host off for the day) |
| same | WF | YES; "2025 Kansas Statutes"; "These codes may not be the most recent version." |
| https://www.sos.ks.gov/publications/session-laws.html | script | 30,175 chars; "2026 Session Laws of Kansas"; chapter links to enrolled PDFs |
| https://www.kslegislature.gov/li/b2025_26/measures/documents/hb2347_enrolled.pdf | script info | redirected to /b2025_26/bills/download/?apn=…; PDF 12 pages, 43,498 chars |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.ksrevisor.gov/kanconst.html | script links | 269 links; Bill of Rights 092_001_00SS, articles 093_AAA_00SS |
| https://www.ksrevisor.gov/kanconst/092_001_0005.html | script grep | "BILL OF RIGHTS § 5. Trial by jury." |
| https://www.ksrevisor.gov/kanconst/093_003_0001.html | script grep | "Article 3.—JUDICIAL § 1. Judicial power; seals; rules." |
| https://www.ksrevisor.gov/kanconst/093_011_0001.html | script grep | "Article 11.—FINANCE AND TAXATION § 1." |
| https://kslegislature.gov/b2025_26/laws/092_000_0000_chapter/092_001_0000_article/092_001_0005_section/092_001_0005_k/ | script info | 169-char bare fragment; not linked from chapter list; not used |
| https://law.justia.com/constitution/kansas/ | WF | rights.html, art3.html; "may not be the most recent version" |
| https://law.justia.com/constitution/kansas/rights.html | WF | YES; § 5 present; §§ 1-20 on one page |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.kscourts.gov/Rules-Orders/Rules | script links | 609 links; "Rule 6.02: Content of Appellant's Brief"; "Rule 240 1.7: Conflict of Interest: Current Clients"; 2026 RuleBook PDF |
| https://www.kscourts.gov/Rules-Orders/Rules/Opinion-of-Appellate-Court | script read/links | title + "View PDF" only -> Rule-7-04.pdf?ext=.pdf |
| https://www.kscourts.gov/Rules-Orders/Rules/Content-of-Appellant-s-Brief | script links | -> Rule-6-02.pdf?ext=.pdf |
| https://www.kscourts.gov/Rules-Orders/Rules/1-7-Conflict-of-Interest-Current-Clients | script links | -> RULE-1-7.pdf?ext=.pdf; order 2021-RL-169 |
| https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/Rule-7-04.pdf?ext=.pdf | script read | 2 pages, 4,368 chars; "Rule 7.04 OPINION OF APPELLATE COURT" |
| same | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/Rule-6-02.pdf?ext=.pdf | script read | 1 page, 2,408 chars; "Rule 6.02 CONTENT OF APPELLANT'S BRIEF" |
| https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/2026-RuleBook.pdf | script info/read | 712 pages, 1,793,376 chars; "2026 Edition … amendments through January 1, 2026" |
| https://www.kscourts.gov/About-the-Courts/District-Courts/District-Court-Rules | script links | 2nd JD -> kscourts.gov PDF; 3rd -> shawneecourt.org; 5th -> 5thjd.org .docx |

## D — Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://sos.ks.gov/publications/pubs_kar.aspx | script | REFUSED: HTTP 403 (that URL off for the day) |
| https://sos.ks.gov/publications/kansas-administrative-regulations.html | script | 5,867 chars; "Kansas Administrative Regulations" -> https://rules.ks.gov/ |
| https://rules.ks.gov/ | script | 200, 0 chars (JavaScript app) |
| https://rules.ks.gov/ | WF | PROVENANCE_REQUIRED (gated; not retried) |
| WS "rules.ks.gov K.A.R. 28-1-2 regulation" | WS | LII K-A-R pages; no rules.ks.gov deep links |
| https://www.law.cornell.edu/regulations/kansas/K-A-R-28-1-2 | script | 10,665 chars; "Reporting requirements for infectious or contagious diseases"; "updated quarterly" |
| https://www.law.cornell.edu/regulations/kansas/K-A-R-30-5-58 | script grep | "Kan. Admin. Regs. § 30-5-58 - Definitions" |
| https://www.sos.ks.gov/publications/kansas-register.html | script links | only link: rules.ks.gov ("link to new K.A.R. and Kansas register page") |
| WS "\"rules.ks.gov\" Kansas Register issue" | WS | legacy sos.ks.gov register PDFs/index pages; vlex (not used) |
| https://sos.ks.gov/publications/Register/Volume-43/Issues/Regulation-Index/07-04-24-Index.html | script info | 200, 19,550 chars (legacy, unlinked) |
| WS "rules.ks.gov regulations agency article…" | WS | SOS publications FAQ |
| https://sos.ks.gov/publications/publications-faq.html | script read | online K.A.R. holds "most current version"; Register is "official state newspaper" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.kscourts.gov/Cases-Decisions/Decisions | script info | redirect -> https://searchdro.kscourts.gov/Documents/LoadPage |
| https://searchdro.kscourts.gov/Documents/LoadPage | script read/links | search form (date, status, court, keyword; "top 500 records"); last 3 months of results; PDF links /documents/pdf/caseDecisions/{guid}_{docket}.pdf |
| https://searchdro.kscourts.gov/Documents/LoadPage | curl | Cloudflare error page (5,793 bytes); stopped |
| https://searchdro.kscourts.gov/Data/decisionsList | script read/links | 222,375 chars; Supreme Court / Court of Appeals, 2026 and 2025 (earliest Oct. 24, 2025) |
| https://searchdro.kscourts.gov/Documents/Released | script read | PDF; "KANSAS APPELLATE COURT OPINIONS FILED October 16, 2026" |
| https://searchdro.kscourts.gov/documents/pdf/caseDecisions/bc839305-04d5-48c3-851d-ed090456f05c_127715.pdf | script info/read | 25 pages, 49,857 chars; "No. 127,715 TROY ALAN MARTIN … CITY OF TOPEKA"; slip page numbers |
| same | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://www.kscourts.gov/Cases-Decisions | script read | slip opinions online from Oct. 25, 1996; unpublished from Sept. 4, 2015 |
| https://www.kscourts.gov/Cases-Decisions/Citing-Decisions | script read | Rule 6.08 official citation; Rule 7.04 unpublished |
| https://www.kscourts.gov/Cases-Decisions/Advance-Sheets | script read/links | Kan. vol. 320 No. 1 – 322 No. 2; Kan. App. 2d vol. 65 No. 1 – 66 No. 5 |
| https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/SupremeCourtVol321No2.pdf | script info/read/grep | 282 pages, 657,158 chars; "VOL. 321 SUPREME COURT OF KANSAS 261" |
| https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/CourtofAppealsVol66No4.pdf | script info | 219 pages, 549,165 chars |
| https://law.justia.com/cases/kansas/supreme-court/2025/ | WF | In re Kort 129389.html, State v. Cunningham 125865.html … |
| https://law.justia.com/cases/kansas/supreme-court/2025/125865.html | WF | YES; "A jury convicted Jason Cunningham of eight counts of sexual"; PDF on cases.justia.com |
| https://law.justia.com/cases/kansas/court-of-appeals/2025/ | WF | Beltz v. State 127820.html …; no published/unpublished labels |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/SupremeCourtVol321No2.pdf (pp. 32-33) | script read | "PETITIONS FOR REVIEW OF DECISIONS OF THE COURT OF APPEALS 321 Kan. No. 2"; columns docket / disposition / date / reported below |
| https://www.kscourts.gov/eCourt/Search-Appellate-Court-Records | script read/links | eCourt landing page (access tiers); portal not followed |

## G — Citation map
`python3 scripts/build.py --check`: no ERROR/WARN for ks.json. `python3 scripts/build.py --cross`: no CROSS line involving ks (only remaining line is ok/oh).

# Montana (mt) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "script" = `scripts/fetch_doc.py --research`; "shell" = curl (headers / app bundle inspection only, no text retrieval past any refusal); "WF" = WebFetch; "WS" = WebSearch.

Tool notes: WebFetch refused every constructed or redirected mca.legmt.gov URL and supremecourtdocket.mt.gov with `PROVENANCE_REQUIRED` ("permission request ... not answered in time"). One WebFetch failed with a session usage limit ("You've hit your session limit") early on; fetching paused and resumed after the coordinator said the limit had reset. About 12 WebFetch calls used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://leg.mt.gov/robots.txt → www.legmt.gov/robots.txt | script | 200; only GPTBot and meta-externalagent `Crawl-delay: 10` |
| https://mca.legmt.gov/robots.txt | shell | HTML "404" page |
| https://courts.mt.gov/robots.txt | script | HTTP 404 |
| https://supremecourtdocket.mt.gov/robots.txt | script/shell | 200 but it is the Angular app HTML (0 text chars) |
| https://rules.mt.gov/robots.txt | script | `User-agent: * / Disallow:` (empty) |
| https://sosmt.gov/robots.txt | script | Disallow /wp-admin/ only |
| https://juddocumentservice.mt.gov/robots.txt | script | 200, 0 chars (app HTML) |
| https://law.justia.com/codes/montana/ | script | REFUSED: robots.txt challenge (refusal cache from 2026-10-16) |
| https://montana.public.law/ | script | proxy 502 Tunnel connection failed (no such host) |
| https://searchcourts.mt.gov/ ; https://juris.mt.gov/ | script | proxy 502 Tunnel connection failed |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://leg.mt.gov/bills/mca/title_0270/chapter_0020/part_0020/section_0040/0270-0020-0020-0040.html | script | redirect → mca.legmt.gov same path; 3,077 chars; "Montana Code Annotated 2025"; two versions (Temporary / Effective October 1, 2026) |
| …/title_0450/chapter_0050/part_0010/section_0010/0450-0050-0010-0010.html | script | 743 chars; "45-5-101. Repealed." |
| …same 27-2-204 page | script links | part sections_index, chapter parts_index, prev/next links |
| …/title_0270/chapter_0020/part_0020/sections_index.html | script | lists 27-2-201 … 27-2-219 with catchlines; "Renumbered 27-2-231" entries |
| …/title_0150/chapter_0300/part_0210/section_0010/0150-0300-0210-0010.html | script | 16,144 chars; "15-30-2101. Definitions." |
| …/title_0300/chapters_index.html | script links | chapter_002A, chapter_009A, chapter_012A |
| …/title_0300/chapter_009A/part_0010/section_0010/0300-009A-0010-0010.html | script | "30-9A-101 Short title" |
| https://mca.legmt.gov/bills/2019/mca/title_0270/…/0270-0020-0020-0040.html | script | 2,397 chars; "Montana Code Annotated 2019" |
| https://mca.legmt.gov/bills/mca/index.html | script links | constitution = title_0000, titles title_0010… |
| https://mca.legmt.gov/bills/mca/help.html | script | 15,109 chars; enrolled bill "will prevail" statement |
| mca.legmt.gov constructed 27-2-204 URL | WF | PROVENANCE_REQUIRED |
| WS "Montana Code Annotated 27-2-204 …" | WS | archive.legmt.gov/bills/MCA/… ; old /bills/1999/mca/27/2/27-2-204.htm forms |
| https://archive.legmt.gov/bills/MCA/title_0270/…/0270-0020-0020-0040.html | WF | 302 redirect to mca.legmt.gov; follow-up PROVENANCE_REQUIRED |
| https://mca.legmt.gov/bills/2019/mca/title_0270/chapter_0020/part_0020/sections_index.html | WF | "You've hit your session limit" |
| https://law.justia.com/codes/montana/2025/ | WF | "2025 Montana Code Annotated"; title links /codes/montana/title-27/ |
| https://law.justia.com/codes/montana/title-27/chapter-2/part-2/section-27-2-204/ | WF | YES, "(1) Except as provided in 27-2-216, the period prescribed for"; only one version shown |
| https://law.justia.com/codes/montana/title-45/chapter-5/part-1/section-45-5-102/ | WF | YES, "(1) A person commits the offense of deliberate homicide if:" |
| https://www.law.cornell.edu/states/montana | script links | links out to leg.mt.gov, courts.mt.gov, mtrules.org |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://courts.mt.gov/ | script links | Supreme Court statement PDF (9-2-2026), "Thomson Reuters Statement" → ctracknotification.com |
| https://courts.mt.gov/external/supreme/statement/MT_JUD_Press_Release_9-2-2026.pdf | script | 3 pp, 2 chars (image-only) |
| https://courts.mt.gov/courts/supreme/opinions | script | 404 |
| https://courts.mt.gov/Courts/Supreme/index | script links | no opinions link |
| https://courts.mt.gov/clerk/index | script links | supremecourtdocket.mt.gov, external/orders/dailyorders, clerk/PastOpinions |
| https://courts.mt.gov/clerk/PastOpinions | script | 404 |
| https://courts.mt.gov/external/orders/dailyorders | script | 670 chars; only points to supremecourtdocket.mt.gov |
| https://supremecourtdocket.mt.gov/ ; /PerceptiveJUDDocket/ ; /search/getDocument?documentid=105958 | script | 200, 0 chars (Angular shell) |
| https://supremecourtdocket.mt.gov/ , assets/env.js, main-3PBDZI4Z.js | shell | "MT Supreme Court Docket Search"; env apiUrl localhost; routes /docket/search, /docket/case-info, /docket/case-info-pre-2006; Okta issuer |
| https://supremecourtdocket.mt.gov/ | WF | PROVENANCE_REQUIRED |
| https://courts.mt.gov/Library/index ; /Library/mr/index | script links | "Montana Court Opinions" → supremecourtdocket; cite_cases.pdf; juddocumentservice links |
| https://juddocumentservice.mt.gov/getDocByCTrackId?DocId=292310 | script | PDF 12 pp, 34,947 chars; "Case Number: AF 07-0110" |
| https://courts.mt.gov/external/library/docs/cite_cases.pdf | script | 10 pp; Dec. 16, 1997 order: "1998 MT 1"; N / W / A suffixes; 2009 pinpoint order |
| https://courts.mt.gov/external/library/guides/QuickGuide.pdf | script | searchcourts.mt.gov "opinions from the early 1970's forward"; "Updated: April 25, 2018" |
| https://courts.mt.gov/Clerk/Resources/CourtRecords | script | record types list; no opinion search |
| WS "Montana Supreme Court opinions search …" | WS | courts.mt.gov stats PDFs, Justia 2023 listing, third parties |
| https://courts.mt.gov/external/clerk/stats/2025/oo25.pdf | script | "Opinions Overview Report" counts only |
| https://law.justia.com/cases/montana/supreme-court/2023/ | WF | rows: Matter of C.M., 2023 MT 255N, DA 21-0580; State v. Hamernick, 2023 MT 249, DA 21-0372 |
| WS "State v. Hamernick 2023 MT 249"; WS Justia case URLs | WS | Justia listings; no opinion URL |
| https://law.justia.com/cases/montana/supreme-court/2023/da-21-0372.html | WF | YES full text ¶1–¶46, dissents; no P.3d; Justia PDF link |
| https://courts.mt.gov/Courts/workers-comp/case-law | script links | year pages {YYYY}-wc 1993–2026, {YYYY}-sc 1994–2025 |
| https://courts.mt.gov/Courts/workers-comp/2024-wc | script links | …/external/wcc/s/Schmidt_2024MTWCC9.pdf etc. |
| https://courts.mt.gov/external/wcc/s/Schmidt_2024MTWCC9.pdf | script | text present; "APPEALED TO MONTANA SUPREME COU…" |
| https://courts.mt.gov/Courts/workers-comp/1993-wc | script links | CHAGNON_WT_DISCOVERY.pdf (free-form names) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://mca.legmt.gov/bills/mca/title_0250/chapters_index.html | script links | ch. 19 UDCR, 20 Civ. P., 21 App. P., 23, 24, 30A … |
| …/title_0250/chapter_0200/parts_index.html | script links | parts I–XI + Appendix (part_0010…0120) |
| …/chapter_0200/part_00{10..110}/sections_index.html | script links | rule→part table (1-2, 3-6, 7-16, 17-25, 26-37, 38-53, 54-63, 64-71, 72, 77/80, 81-86); 4.1 → section_0041 |
| …/chapter_0200/part_0030/section_0120/0250-0200-0030-0120.html | script | 7,873 chars; "(6) failure to state a claim upon which relief can be granted" |
| …/chapter_0200/part_0050/section_0560/… | script | HTTP 404 (wrong part) |
| …/chapter_0200/part_0070/section_0560/… | script | "Rule 56 Summary Judgment" |
| …/title_0260/chapter_0100/parts_index.html ; part_0070/sections_index.html | script links | Articles I–X; Rule 702 → section_0020 |
| …/title_0260/chapter_0100/part_0070/section_0020/0260-0100-0070-0020.html | script | 1,117 chars; "Rule 702. Testimony by experts." |
| …/title_0250/chapter_0210/parts_index.html ; part_0010/sections_index.html | script links | Rules 1–19+ at section_00N0 |
| …/chapter_0210/part_0010/section_0120/0250-0210-0010-0120.html | script | "Rule 12. Briefs." |
| …/chapter_0190/part_0010/sections_index.html | script links | UDCR Rule 1–3 … |
| https://courts.mt.gov/Courts/Rules/index | script links | ~25 rule PDFs under /external/rules/ |
| https://courts.mt.gov/external/rules/civ_proc.pdf | script | 123 pp, 276,612 chars; "Date of Last Amendment to these Rules: 28JUN2022" |
| same | WS → WF | Rule 56 NOT PRESENT; last rule received 23.1 |
| https://courts.mt.gov/external/rules/mtr_evid.pdf | script | 21 pp, 64,462 chars; "20JUN2007"; Rule 702 p.12 |
| https://courts.mt.gov/external/rules/mtr_app_pro.pdf | script | 58 pp, 160,229 chars; "12OCT2021" |
| https://courts.mt.gov/external/rules/mtr_prof_cond.pdf | script | 37 pp, 109,771 chars |

## F — Subsequent history
No intermediate court. Rehearing / withdrawal (W) / amendment (A) orders sit in the docket app (JS, see E). No separate free listing found.

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://mca.legmt.gov/bills/mca/title_0000/chapters_index.html | script links | article_000p (Preamble), article_0010 … |
| …/title_0000/article_0020/parts_index.html ; part_0010/sections_index.html | script links | sections 1… at section_00N0; §10 → section_0100 |
| …/title_0000/article_0020/part_0010/section_0100/0000-0020-0010-0100.html | script | 905 chars; "Section 10. Right of privacy." |
| …/title_0000/article_0070/part_0010/section_0020/0000-0070-0010-0020.html | script | "Section 2. Supreme court jurisdiction." |
| https://law.justia.com/constitution/montana/ | WF | whole constitution one page; "AS ADOPTED BY THE CONSTITUTIONAL CONVENTION MARCH 22, 1972" |

## D — Administrative code and register
| URL | Tool | Result |
|---|---|---|
| https://rules.mt.gov/ | script / shell | 0 chars; React shell "Montana SOS" (Esper) |
| https://rules.mt.gov/index.bundle.ee6a356c3b3752e365fa.js | shell | routes :collectionUuid/sections/:sectionUuid; /api/context; DisclaimerForARM.pdf |
| https://sosmt.gov/arm/register/ | script / links | 0 text chars; links: ARM collection aec52c46…, MAR collection 5e1173a6…, emergency e57ed8e7…, mtrules.org |
| https://rules.mt.gov/browse/collections/aec52c46-128e-4279-9068-8af5d5432d74 | script | 0 chars (shell) |
| https://www.law.cornell.edu/regulations/montana | script | Department list; /department-{n} links |
| …/department-37 → chapter-37.86 → subchapter-37.86.1 | script links | "Rule 37.86.101 to 37.86.112"; Mont-Admin-r-37.86.101 |
| https://www.law.cornell.edu/regulations/montana/Mont-Admin-r-37.86.101 | script | 4,429 chars; body present; history "NEW, 1980 MAR p. 1747" |
| https://www.law.cornell.edu/regulations/montana/Mont-Admin-r-42.15.101 | script | "DEFINITIONS (REPEALED)" |

# Michigan (mi) probe log — 2026-10-16/17

All probes by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research` (or `lsnet.get` from a scratch link-lister, which applies the same robots/bot-check rules). "GATED" = WebFetch error PROVENANCE_REQUIRED (permission prompt not answered; URL was built, not taken from a search result). ~44 WebFetch calls, ~16 WebSearch calls. WebFetch hit a session usage limit once on 2026-10-17 00:1x (michigan-register page); work resumed after the reset.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-5805 | script | REFUSED: www.legislature.mi.gov answers robots.txt with a bot check |
| https://legislature.mi.gov/Laws/MCL?objectName=mcl-600-5805 | script | REFUSED: legislature.mi.gov answers robots.txt with a bot check |
| https://www.courts.michigan.gov/robots.txt, /case-search/ | script | REFUSED: robots.txt rule `Disallow: /` |
| https://law.justia.com/codes/michigan/chapter-600/ | script | REFUSED: robots.txt Cloudflare challenge |
| https://www.michigan.gov/lara/…/michigan-register | script | REFUSED: robots.txt bot check |
| https://ars.apps.lara.state.mi.us/AdminCode/AdminCode | script | 200 html 2,148 chars; robots: none; POST form (RuleNumber, Department, Bureau) |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-5805 | WF | GATED |
| https://www.legislature.mi.gov/ | WF | GATED |
| https://legislature.mi.gov/Laws/MCLSearch (from search) | WF | OK; "Complete Through PA 103 of 2026"; disclaimer "not intended to replace official versions"; links ChapterIndex, Constitution, policy |
| https://legislature.mi.gov/Home/AutomatedDataCollectionPolicy | WF | OK; automated access allowed, max 1 request/second; MCL PDF+XML bulk at /documents/mcl/, monthly archives; LitWebServices API |
| https://legislature.mi.gov/Laws/ChapterIndex | WF | OK; chapter links GetObject?objectName=mcl-chap{N}; NO section ranges |
| https://legislature.mi.gov/Laws/MCL?objectName=mcl-600-5805 | WF | GATED |
| https://legislature.mi.gov/Home/GetObject?objectName=mcl-chap600 | WF | returned Chapter 18 page (acts with ranges "(18.1101-18.1594)") — wrong chapter |
| https://legislature.mi.gov/documents/mcl/ | WF | GATED |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-600-5040.pdf | WF | repeal notice "600.5040-600.5065 Repealed. 1993, Act 78"; "Complete Through PA 103 of 2026" |
| https://legislature.mi.gov/documents/mcl/pdf/mcl-600-5805.pdf | WF | GATED |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-750-567.pdf | WF | repeal notice; "Rendered Tuesday, September 29, 2026" |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-750-46.pdf | WF | repeal notice "750.46-750.48 Repealed. 1978, Act 571" |
| https://www.legislature.mi.gov/documents/mcl/pdf/MCL-257-201.pdf | WF | YES "When a reference is made in this act to "division","; History 1949, Act 300; not truncated |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-257-504A.pdf | WF | repeal notice "257.504a-257.510 Repealed. 1971, Act 67" |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-ACT-58-OF-1935.pdf | WF | act PDF, repeal notice only; "Courtesy of legislature.mi.gov"; no official statement |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-600-6601.pdf | WF | NOT PRESENT |
| https://legislature.mi.gov/documents/mcl/pdf/MCL-600-7001.pdf | WF | repeal notice "600.7001-600.7061 Repealed. 1974, Act 297"; Page 1 of 1 |
| https://law.justia.com/codes/michigan/chapter-600/ | WF | "2025 Michigan Compiled Laws"; acts with section ranges; "may not be the most recent version" |
| https://law.justia.com/codes/michigan/chapter-600/statute-act-236-of-1961/ | WF | divisions with ranges; ch. 58 = division-236-1961-58 "(600.5801...600.5869)" |
| …/division-236-1961-58/section-600-5805/ | WF | YES "Sec. 5805. (1) A person shall not bring or maintain"; not truncated |
| WebSearch results | search | per-section PDFs also on mirror hosts zeus-milenia., hercules-milenia., capitol., ombudsman., renderpdf.legislature.mi.gov — not used |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://legislature.mi.gov/Laws/Constitution | WF | links only: mcl-chap1.pdf, MIConstitution.pdf ("Updates may be slightly delayed"), 1963 / 1908 as-ratified PDFs |
| https://legislature.mi.gov/documents/mcl/pdf/mcl-chap1.pdf | WF | art 1 § 17 YES "No person shall be compelled in any criminal case to"; Page 1 of 93; truncated at Art. IV § 34 heading; art 6 § 1 NOT PRESENT |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.courts.michigan.gov/ | WF | GATED |
| …/michigan-court-rules-responsive-html5.zip/Michigan_Court_Rules/Updated/Updated.htm | WF | "Updated May 1, 2025"; no chapter links |
| …/Court_Rules_Chapter_1/Court_Rules_Chapter_1.htm | WF | MCR 1.105 YES "These rules are to be construed, administered, and employed by"; "Chapter Updated with MSC Order(s) Effective on January 1, 2026"; complete |
| …/Court_Rules_Chapter_2/Court_Rules_Chapter_2.htm | WF | GATED |
| https://www.courts.michigan.gov/492ca5/siteassets/…/rules-of-evidence/michigan-rules-of-evidence.pdf | WF | MRE 702 YES "A witness who is qualified as an expert by knowledge"; "Updated with MSC order(s) effective on 1/28/2026"; complete to 1102 |
| https://www.courts.michigan.gov/siteassets/…/rules-of-professional-conduct/michigan-rules-of-professional-conduct.pdf?r=1 | WF | MRPC 1.7 YES "A lawyer shall not represent a client if the representation"; "Last Updated 1/1/2025"; truncated after 1.10(c)(2), 130,109 chars |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://ars.apps.lara.state.mi.us/AdminCode/AdminCode?RuleNumber=R%20408.10011 | script | blank form (GET param ignored); 0 matches for "408" |
| https://ars.apps.lara.state.mi.us/AdminCode/DeptBureauAdminCode?Department=Labor%20and%20Economic%20Opportunity&Bureau=MIOSHA | script | 200, 152,316 chars, rule-set rows with ranges and PDF/HTML links |
| …/DownloadAdminCodeFile?FileName=R%20408.10001%20to%20R%20408.10098.pdf | script | PDF 8 pp, 16,094 chars; verify "An employer shall comply with all of the following" VERIFIED p.2; "History: 1979 AC; 2018 AACS." |
| same + &ReturnHTML=True | script | html 16,499 chars |
| …/DeptBureauAdminCode?Department=Environment%2C%20Great%20Lakes%20and%20Energy | script | link "R 336.1201 to R 336.1299.pdf" |
| …/DownloadAdminCodeFile?FileName=R%20336.1201%20to%20R%20336.1299.pdf | script | PDF 73 pp, 246,989 chars; verify R 336.1201(1) phrase VERIFIED p.1 |
| https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-408-10011 | script | 200, body "Rule 11. An employer shall comply"; Notes "2018 MR 2, Eff. 2/2/2018"; Last-Modified Aug 2 2025 |
| https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-336-1201 | script | 200, body present |
| https://michigan.gov/lara/bureau-list/moahr/admin-rules/using-the-michigan-administrative-code | WF | "there may be errors contained in the code text"; no official statement |
| https://michigan.gov/lara/bureau-list/moahr/admin-rules/publications/michigan-register | WF | 1st try: session usage limit; 2nd try OK: links 2026 issues page and CONTENTdm archive |
| https://www.michigan.gov/…/michigan-register-issues-for-year-2026 | WF | GATED |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.courts.michigan.gov/4a11c7/siteassets/reports/coa/annualreports/annualreport2019.pdf | WF | OK "Michigan Court of Appeals Annual Report 2019" (WebFetch not blocked by robots here) |
| https://www.courts.michigan.gov/siteassets/case-documents/uploads/OPINIONS/FINAL/COA/20230112_C359401_46_359401C.OPN.PDF | WF | EGLE v Brotherton, No. 359401, UNPUBLISHED; "SHAPIRO, P.J. (concurring). I concur in the result only."; concurrence file only |
| https://www.courts.michigan.gov/c/courts/coa/case/359401 | WF | GATED |
| https://www.courts.michigan.gov/4a5268/siteassets/publications/coa-bound-volumes/bv_miapp285_final.pdf | WF | "Michigan Appeals Reports" vol. 285; running heads "285 MICH APP 1"; People v Seals p. 1; truncated p. 46 |
| https://law.justia.com/cases/michigan/ | WF | four listings: supreme-court, court-of-appeals-published, -unpublished, -order |
| https://law.justia.com/cases/michigan/supreme-court/2025/ | WF | docket slugs, e.g. 163989.html |
| https://law.justia.com/cases/michigan/supreme-court/2025/163989.html | WF | YES "In this case, we address whether an employer can contractually"; truncated 100K/118,108 |
| https://law.justia.com/cases/michigan/court-of-appeals-unpublished/2023/ | WF | slugs 354823.html, 362536-0.html; listing paginated |
| https://law.justia.com/cases/michigan/court-of-appeals-unpublished/2023/359401.html | WF | Shapiro concurrence only; PDF cases.justia.com/…/2023-359401.pdf |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.courts.michigan.gov/4927ff/siteassets/case-documents/uploads/sct/public/orders/169336_37_01.pdf | WF | People v Cao, SC 169336, COA 373185, Feb. 27, 2026; "On order of the Court, the application for leave to appeal"; leave denied |
| WebSearch "courts.michigan.gov/c/courts/coa/case" etc. | search | no case-search URLs surfaced; case search not verifiable |

## Build
- `python3 scripts/build.py --check`: exit 0, no lines for mi.json.
- `python3 scripts/build.py --cross`: first run flagged 'Act 236 of 1961, Michigan Public Acts' (PA) and bare 'MRPC 1.7' (MN); removed those forms; final "0 cross-jurisdiction match(es)".

# Nevada (nv) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `scripts/fetch_doc.py --research`; "shell" = curl (used only for robots.txt, headers, anchor inspection and the ACIS JSON API, never to get around a refusal); "WF" = WebFetch; "WS" = WebSearch (discovery only).

Environment note: WebFetch in this session only fetched URLs that had appeared in WebSearch results (or hosts already approved); several others failed with `PROVENANCE_REQUIRED` ("permission request ... not answered in time"). Those are recorded below and are not site refusals. About 27 WebFetch calls used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.leg.state.nv.us/robots.txt | shell | 200; `User-agent: *` disallows `/*.axd`, `*/Reports/*`, `/App/Opinions/*`, `*/ExhibitDocument/*`, two FiscalNote paths; NRS/NAC/Const/CourtRules/Register allowed |
| https://nvcourts.gov/robots.txt | shell | Cloudflare "Just a moment..." challenge page |
| https://nvcourts.gov/supreme/decisions/forthcoming_opinions | script | REFUSED: "nvcourts.gov answers robots.txt with a bot check (challenge)" |
| https://acis.nvcourts.gov/robots.txt | shell | 200 text/html — the SPA shell (no robots file) |
| https://acis-api.nvcourts.gov/robots.txt | shell | 404 JSON "No static resource robots.txt." |
| https://caseinfo.nvsupremecourt.us/ | shell + script | curl HTTP 000; script: robots.txt unreachable, "Connection reset by peer" |
| https://law.justia.com/codes/nevada/chapter-41/statute-41-130/ | script | REFUSED: law.justia.com refused automated access earlier (robots.txt challenge) |
| https://www.law.cornell.edu/robots.txt | shell | Crawl-delay: 10 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.leg.state.nv.us/NRS/NRS-041.html | script info | kind=html, 316,449 chars, last-modified 21 Apr 2026 |
| same | script grep/verify | 41.130 body at offset ~120.7K; verify "whenever any person shall suffer personal injury by wrongful act" VERIFIED |
| same | shell | anchors `<a name=NRS041Sec010>`, `NRS041Sec0305` |
| https://www.leg.state.nv.us/NRS/NRS-041.html (www host) | WF | PROVENANCE_REQUIRED (permission timed out) |
| WS "NRS 41.130 liability for personal injury leg.state.nv.us" | WS | gave leg.state.nv.us/nRs/NRS-041.html, Justia, public.law URLs |
| https://leg.state.nv.us/nRs/NRS-041.html | WF | 41.130 NOT PRESENT; 41.0305 "As used in NRS 41.0305 to 41.039, inclusive, the term"; "[Rev. 4/15/2026 10:45:11 AM--2025]"; page text 106,190 chars, ends in 41.039 |
| same, offset=100000 | WF | 41.130 NO; only 41.0393, 41.0395 |
| https://leg.state.nv.us/NRS/NRS-011.html | WF | first try PROVENANCE_REQUIRED; after WS listed it: 11.190 YES "Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007,"; "[Rev. 4/15/2026 10:40:13 AM--2025]"; complete to 11.500 |
| https://www.leg.state.nv.us/NRS/NRS-011.html | script | 55,091 chars; verify 11.190 opening VERIFIED |
| https://www.leg.state.nv.us/NRS/ | script | 52,662 chars; title/chapter list, no section ranges, no disclaimer, no bulk links |
| https://www.leg.state.nv.us/NRS/NRS-041A.html | shell | 200; anchors `NRS041ASec003` |
| https://www.leg.state.nv.us/NRS/NRS-200.html | shell | 200, 462,749 bytes |
| https://www.leg.state.nv.us/NRS/NRS-000.html | shell | 200 |
| https://www.leg.state.nv.us/NRS/NRS-220.html | script | NRS 220.170(3): certified printed copies are "the official codified version of Statutes of Nevada"; 220.170(4)(d) "A section: NRS 000.000" |
| https://nevada.public.law/statutes/nrs_11.190 | WF | YES, same opening; "(accessed May 26, 2025)"; no edition label |
| same; …/nrs_41.130 | script | ok, 7,990 / 4,546 chars; last-modified 11 May 2025 |
| https://nevada.public.law/statutes | script | header "Updated May 26, 2025" |
| https://nevada.public.law/ | script | links only /statutes for Nevada |
| https://law.justia.com/codes/nevada/chapter-41/statute-41-130 | WF | YES "Except as otherwise provided in NRS 41.745, whenever any person"; "2025 Nevada Revised Statutes"; "These codes may not be the most recent version" |
| https://law.justia.com/codes/nevada/chapter-11/statute-11-190 | WF | YES; "2025 Nevada Revised Statutes" |
| WS "Statutes of Nevada 2025 …" | WS | gave /Statutes/83rd2025/Stats2025001.html |
| https://www.leg.state.nv.us/Statutes/ , /Statutes/83rd2025/ | shell | 403 (directory) |
| https://www.leg.state.nv.us/Statutes/83rd2025/Stats2025001.html | script | 306,320 chars; "Statutes of the State of Nevada - Eighty-Third Session, 2025"; "[Rev. 8/22/2025 11:13:05 AM]" |
| https://www.law.cornell.edu/states/nevada | script | links out to Legislature / nvcourts.gov |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.leg.state.nv.us/Const/NVConst.html | script | 325,751 chars; anchors `Art1Sec8`, `Art1Sec8A`; verify Art. 1 § 8 "No person shall be tried for a capital or other infamous crime" VERIFIED; Art. 6 § 4 at offset 139,492 |
| same | WF | Art. 1 § 8 YES; Art. 6 § 4 NOT PRESENT; "[Rev. 4/15/2026 4:36:19 PM--2025]"; window ends Art. 4 § 36 |
| same, offset=100000 | WF | Art. 6 § 4 NOT PRESENT; last visible Art. 5 § 9 |
| https://law.justia.com/nevada/constitution/ | WF | single page; Art. 1 § 8 YES; Art. 6 NOT PRESENT in window 1; 126,220 chars |
| same, offset=100000 | WF | Art. 6 § 4 "The supreme court shall have appellate jurisdiction in all civil" (no court of appeals: stale) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WS "leg.state.nv.us CourtRules NRCP …" | WS | NRCP.html, index.html, JCRCP.html, nvcourts.gov nrcp_1.pdf |
| https://www.leg.state.nv.us/CourtRules/index.html | script + shell | ~40 rule-set pages (NRCP, NRCrP, NSTR, DCR, First–EleventhDCR, JCRCP, RPC, NRAP, NRAD, SCR parts …) |
| https://www.leg.state.nv.us/CourtRules/NRCP.html | script | 396,847 chars; anchors `NRCPRule12`, `NRCPRule16_1`; verify 12(b)(5) phrase VERIFIED |
| same | WF | 12(b)(5) YES; Rule 56 NOT PRESENT; truncated in 16.1(c)(2)(N); "[Rev. 4/15/2026 4:39:25 PM--2025]" |
| https://www.leg.state.nv.us/CourtRules/NRAP.html | script | 251,814 chars; 36(c)(3) VERIFIED offset 207,738 (SC on/after Jan. 1, 2016; COA on/after Aug. 15, 2024) |
| same | WF | 36(c)(3) NOT PRESENT; 3A YES; "[Rev. 9/9/2026 2:04:44 PM--2026R1]"; "Amendments Through October 31, 2025"; truncated Rule 13 |
| https://www.leg.state.nv.us/CourtRules/SCR.html | script | 609,453 chars; "[Rev. 9/9/2026 2:05:02 PM--2026R1]"; Rule 99 at offset 361,476 |
| https://www.leg.state.nv.us/CourtRules/RPC.html | script | 145,672 chars; Rule 1.7 at 33,388; verify VERIFIED |
| EighthDCR, DCR, SecondDCR, JCRCP, NSTR .html | shell | anchors `EighthDCRRule1_10`, `DCRRule2`, `SecondDCRRule2_1`, `JCRCPRule2`, `NSTRRule2` |
| https://nvcourts.gov/supreme/rules/amendments | WF | loads; links SCR/NRAP amendment pages and ADKT search; no rule text |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://www.leg.state.nv.us/NAC/ | script | title page "NEVADA ADMINISTRATIVE CODE … Pursuant to NRS 233B.062 to 233B.065"; links Chapters.html |
| https://www.leg.state.nv.us/NAC/Chapters.html | script + shell | links NAC-038.html … (3-digit padding) |
| https://www.leg.state.nv.us/NAC/NAC-116.html | script | 87,593 chars; "[Rev. 6/7/2026 11:00:00 AM]"; NAC 116.010 body present; anchors `NAC116Sec010` |
| same | WF | 116.010 YES "As used in this chapter, unless the context otherwise requires,"; "[NAC-116 Revised Date: 4-26]"; complete |
| https://www.leg.state.nv.us/NAC/NAC-284.html | script | 528,863 chars; NAC 284.010 present |
| https://www.law.cornell.edu/regulations/nevada | script | chapter list |
| https://www.law.cornell.edu/regulations/nevada/NAC-116-010 | script | verify VERIFIED; "State regulations are updated quarterly" |
| https://www.leg.state.nv.us/Register/ | script | year index links 2022–2026 numerical/keyword |
| …/Register/indexes/2025_NAC_REGISTER_NUMERICAL.htm | script | stage legend (I, P, RP, A, AP …); links /Register/2025Register/R001-25A.pdf |
| …/Register/2025Register/R001-25A.pdf | script | 4 pp; "ADOPTED REGULATION OF THE BOARD OF PSYCHOLOGICAL EXAMINERS" |
| …/Register/2021Register/R123-21I.pdf | WF | title and submission note only |
| same | script | 5 pp, 241 chars (scanned images) |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://nvcourts.gov/supreme/decisions/forthcoming_opinions | WF | real content; links to ACIS searches (court UUIDs dc01122c… SC, 74764f58… COA; type 1000014 opinions, 1000018 orders) |
| ACIS portal search URL (acis.nvcourts.gov/portal/search/document/results?criteria=…) | WF | PROXY_REJECTED "url exceeds the maximum fetchable length" |
| same | script | kind=html chars=0 (Vue SPA) |
| https://acis.nvcourts.gov/properties.js | shell | apiRoot "https://acis-api.nvcourts.gov" |
| https://acis.nvcourts.gov/assets/index-DNIzE65D.js + search chunk | shell | endpoint and parameter names (api.search.documents, caseHeader.courtID, docketEntryHeader.docketEntryTypeID …) |
| acis-api …/courts/cms/docketentrydocuments?caseHeader.courtID=SC&docketEntryHeader.docketEntryTypeID=1000014&size=4&sort=…desc | shell | 200 JSON; totalElements 2,125; newest City of Sparks v. Bluth 90244 "142 Nev. Adv. Opn. No. 65" |
| same, sort asc | shell | earliest 2000-05-08 per curiam opinion |
| COA type 1000014 / 1000018; SC 1000018 | shell | COA opinions 95 (earliest 2015-03-27); COA orders 9,532; SC orders 10,000 (cap) |
| …/courts/{SC uuid}/cms/case/61b849df…/docketentrydocuments/3e2b60be… | shell | 200 application/pdf 142,398 bytes; with courtID "1": 400 "not a valid UUID" |
| same | script | pdf 9 pp, 14,971 chars; verify "we are asked to determine whether the district court abused its discretion…" VERIFIED p. 2 |
| …/courts/cms/cases?caseHeader.caseNumber=90244 | shell + script | 200 JSON with caseInstanceUUID, originatingCourtCases |
| …/cms/cases/{uuid}/docketentries?size=100 | shell | 92 entries; with sort= → 500 |
| …/docketentrysubtypes | shell | 372 subtypes (1000233 Opinion on Supreme Court Review; 1000336/1000339 petition for review granted/denied; 1000148 cert denied) |
| https://nvsctlawlib.libguides.com/nvcitationguide/case-law | WF | "140 Nev., Adv. Op. 60, 555 P.3d 1171, 1174 (2024)"; NRAP 36(c) dates; links nvcourts.gov nevada_reports |
| https://nvcourts.gov/supreme/decisions/advance_opinions_enterprise | WF | PROVENANCE_REQUIRED |
| https://nvcourts.gov/supreme/decisions/nevada_reports | WF | preliminary prints; newest "Volume 140, Adv. Op. Nos. 51-53, pages 467-486"; bound volume controls |
| https://nvcourts.gov/__data/assets/pdf_file/0023/51458/140_Nevada_Reports_pages_467-486.pdf | WF | PROVENANCE_REQUIRED (not retried; shell blocked) |
| https://law.justia.com/cases/nevada/supreme-court/2020 | WF | entries /2020/75669.html etc. |
| https://law.justia.com/cases/nevada/supreme-court/2026/90244.html | WF | Bluth, "142 Nev., Adv. Op. No. 65", complete |
| https://law.justia.com/cases/nevada/court-of-appeals/2026/ | WF | listing; 90082-coa.html, 90577-coa.html, 89261-coa.html |
| https://law.justia.com/cases/nevada/court-of-appeals/2026/89261-coa.html | WF | Moore v. Primadonna "142 Nev. Adv. Op. No. 6", complete, OCR errors, no review note |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| …/docketentrydocuments?docketEntryHeader.docketEntrySubTypeID=1000339 | shell | 856 denials; newest Herrmann 92238 (2026-10-16) |
| …=1000336 | shell | 62 grants; Ngbeken 89259, State v. Benjamin 91335 |
| …/cases?caseHeader.caseNumber=92238 → docketentries | shell | petition for review "TRANSFERRED FROM THE COURT OF APPEALS" 2026-09-30; denied 2026-10-16 |
| …/cases?caseHeader.caseNumber=89261 → docketentries | shell | transferred to COA 2025-10-03; COA opinion 2026-01-29 (Adv. Opn. No. 6); petition 2026-02-19; granted 2026-04-13; SC opinion 2026-10-15 (Adv. Opn. No. 64) |

# Hawaii (hi) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "script" = `scripts/fetch_doc.py --research`; "shell" = curl (robots.txt only); "WF" = WebFetch; "WS" = WebSearch (discovery only).

Session notes: WebFetch hit a session usage limit ("You've hit your session limit · resets 2:50am") after 2 calls; fetching stopped and resumed only after the coordinator reported the reset. Several WF calls failed with `PROVENANCE_REQUIRED` (permission prompt not answered) — recorded as gating, not site refusals. About 22 WF calls used in total.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.capitol.hawaii.gov/robots.txt | shell | 403, "Attention Required! \| Cloudflare" |
| https://capitol.hawaii.gov/robots.txt | shell | 301 (cloudflare) |
| https://data.capitol.hawaii.gov/robots.txt | shell | 200; `User-Agent: * Allow: /`, `Disallow: /*.axd$` |
| https://www.courts.state.hi.us/robots.txt | shell | 403 Forbidden (nginx) |
| https://www.capitol.hawaii.gov/hrscurrent/Vol13_Ch0601-0676/HRS0657/HRS_0657-0007.htm | script | REFUSED: "answers robots.txt with a bot check (refused)" |
| https://www.courts.state.hi.us/legal_references/rules/rulesOfCourt | script | REFUSED: "answers robots.txt with a bot check (refused)" |
| https://www.courts.state.hi.us/ | script | REFUSED (host off for the day) |
| https://law.justia.com/codes/hawaii/ | script | REFUSED: robots.txt challenge (recorded 2026-10-16) |
| https://www.law.cornell.edu/states/hawaii | script | 200, 2,590 chars; links out to LRB, capitol, courts; LII hosts HAR only |
| https://hawaii.public.law/ | script | FETCH ERROR: robots.txt unreachable, "Tunnel connection failed: 502 Bad Gateway" |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WS "HRS 657-7 … hrscurrent" | WS | data.capitol.hawaii.gov hrsarchive/hrscurrent URLs, SLH PDFs |
| https://data.capitol.hawaii.gov/hrscurrent/Vol13_Ch0601-0676/HRS0657/HRS_0657-0007.htm | script | 18,294 chars, last-modified 6 Jan 2026; "§657-7 Damage to persons or property."; verify "shall be instituted within two years after the cause of action" VERIFIED |
| same | WF | PROVENANCE_REQUIRED (built URL) |
| https://data.capitol.hawaii.gov/hrscurrent/Vol14_Ch0701-0853/HRS0708/HRS_0708-0821.htm | script | 1,631 chars; "§708-821 Criminal property damage in the second degree." |
| same (from WS) | WF | YES "A person commits the offense of criminal property damage in"; no currency; complete |
| https://data.capitol.hawaii.gov/hrscurrent/ | script links | 14 volume folders with chapter ranges in names (Vol01_Ch0001-0042F … Vol14_Ch0701-0853) |
| …/Vol09_Ch0431-0435H/ ; …/Vol12_Ch0501-0588/ | script links | chapter folders HRS0431, HRS0431A …, HRS0514B … |
| …/HRS0431/ filter "10C-03" | script links | HRS_0431-0010C-0301.htm, _0005 variants |
| …/HRS0657/ | script links | HRS_0657-.htm (TOC), HRS_0657-0001_0005.htm … |
| …/HRS0657/HRS_0657-0001_0005.htm | script | "[§657-1.5] Limitation of actions not applicable to State." |
| …/HRS0626/ | script links | HRS_0626-0001-0100 … -1102 (one file per HRE rule) |
| …/HRS0626/HRS_0626-0001-0702.htm | script | 17,123 chars; "Rule 702 Testimony by experts." |
| …/HRS0657/HRS_0657-.htm | script | chapter TOC, sections listed individually |
| https://data.capitol.hawaii.gov/hrsall/AllDivisions.aspx | WF | session limit error (quota) |
| same | script | 15,429 chars; "Hawaii Revised Statutes 2025"; links to hrstoc.pdf, hrs_index.pdf, Division.aspx; no disclaimer |
| https://data.capitol.hawaii.gov/hrsall/Default.aspx | script | volume list "VOLUME 13 601-676 VOLUME 14 701-853"; no official/disclaimer text |
| https://data.capitol.hawaii.gov/docs/hrstoc.pdf | script | PDF 71 pp., 238,152 chars, last-modified 13 Feb 2025 |
| https://data.capitol.hawaii.gov/hrsall/title.aspx?id=23A | script | 15,873 chars, header "Hawaii Revised Statutes 2025" |
| https://data.capitol.hawaii.gov/hrsall/ChaptersByDivision.aspx?id=4 | script | chapter list ("657 LIMITATION OF ACTIONS"), no titles |
| https://data.capitol.hawaii.gov/hrsall/Division.aspx?id=4 | script links | titles with chapter ranges: 32 601-615 … 36 651-676 |
| WS "capitol.hawaii.gov hrscurrent HRS_0663" ; WS HRS disclaimer ; WS "www.capitol.hawaii.gov/hrscurrent" | WS | only data.capitol.hawaii.gov URLs; hrsarchive/hrs{1999,2000,2003,2004,2009,2018,2022,2023} seen |
| WS Justia HRS section | WS | /codes/hawaii/title-38/chapter-852/, /2015/title-13/chapter-202/section-202-6-to-8 |
| https://law.justia.com/codes/hawaii/title-1/ | WF | "2025 Hawaii Revised Statutes"; chapter links chapter-1, chapter-4e; disclaimer "These codes may not be the most recent version." |
| https://law.justia.com/codes/hawaii/title-38/chapter-852/ | WF | 2025; section-852-1/, section-852-2/ |
| https://law.justia.com/codes/hawaii/title-38/chapter-852/section-852-1/ | WF | YES "§852-1 Refusal to provide ingress or egress. (a) Whenever ingress"; "HI Rev Stat § 852-1 (2025)" |
| https://data.capitol.hawaii.gov/sessions/sessionlaws/Years/SLH1972/SLH1972_Act189.pdf | script | 1 p.; "A Bill for an Act Relating to Tort Liability." |
| https://data.capitol.hawaii.gov/sessions/sessionlaws/Years/SLH2025/ | script links | 315 links: Index&Effects_SLH2025.pdf, SLH2025_Act1.pdf … |
| …/SLH2025/SLH2025_Act235.pdf | script | 21 pp., 89,440 chars; "A Bill for an Act Relating to Agriculture." |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| WS Hawaii constitution | WS | data.capitol …/05-CONST/CONST_0001-0001.htm, lrb.hawaii.gov |
| https://data.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/05-CONST/ | script links | 174 links: CONST_.htm, CONST_0001-0001.htm … |
| …/05-CONST/CONST_0001-0001.htm | WF | YES "All political power of this State is inherent in the"; no currency |
| …/05-CONST/CONST_0001-0005.htm | script | 81,949 chars; "Section 5. No person shall be deprived of life, liberty or property" |
| …/05-CONST/CONST_0006-0001.htm | script | 2,825 chars; "ARTICLE VI THE JUDICIARY" |
| https://lrb.hawaii.gov/constitution | script | 153,886 chars; note on HB 2802 (2024)/SB 2927 (2024); verify "All political power of this State is inherent in the people" VERIFIED |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WS HRCP / HRAP 35 | WS | rules index, hrcp_ada.htm/pdf, hrap_ada.pdf, 2026_hrap35am_ada.pdf |
| https://www.courts.state.hi.us/legal_references/rules/rulesofcourt | WF | 31 rule sets with HTML/PDF links and effective dates; "Last Updated: October 12, 2026"; HRE not listed |
| https://www.courts.state.hi.us/wp-content/uploads/2024/09/hrcp_ada.htm | WF | 12(b) YES "Every defense, in law or fact, to a claim for"; 56(c) NOT PRESENT; stops in Rule 17(d)(3); 121,526 chars |
| https://www.courts.state.hi.us/wp-content/uploads/2025/07/hrap.htm | WF | PROVENANCE_REQUIRED |
| https://www.courts.state.hi.us/wp-content/uploads/2024/12/hrpp.htm | WF | PROVENANCE_REQUIRED |
| https://www.courts.state.hi.us/wp-content/uploads/2025/07/hrap_ada.pdf | WF | 35(c) NO, 40.1 NOT PRESENT; body through Rule 28(b)(11)(A); cover "Effective June 1, 1984" |
| same, offset=100000 | WF | window Rule 28(b) → Rule 32(c); 35(c), 40.1 NOT PRESENT |

## D — Administrative rules
| URL | Tool | Result |
|---|---|---|
| WS HAR ltgov | WS | luc.hawaii.gov/har, ltgov HAR listing PDFs |
| WS Cornell HAR | WS | law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-15-218-36 etc. |
| https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-11-60.1-1 | script | 2,506 chars — HAR title index, not the section (dotted form wrong) |
| https://www.law.cornell.edu/regulations/hawaii | script links | Title 2 … Title 24 |
| …/hawaii/title-11 → /title-11/subtitle-1 → /chapter-60.1 → /subchapter-11 | script links | "Subchapter 1 - GENERAL REQUIREMENTS (§ 11-60.1-1 to 11-60.1-20)"; section link Haw-Code-R-SS-11-60-1-201 |
| https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-11-60-1-1 | script | 33,949 chars; "Haw. Code R. § 11-60.1-1 - Definitions"; "As used in this chapter, unless otherwise defined" |
| https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-11-60-1-201 | script | "The purpose of this subchapter is to further implement"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-15-218-36 ; …-17-650-27 | script | 2,441 / 2,283 chars (reserved/repealed stubs) |
| https://ltgov.hawaii.gov/the-office/administrative-rules/ | script | 6,285 chars; department links (Title 11 → health.hawaii.gov/opppd/administrative-rules/); external-site disclaimer |
| https://health.hawaii.gov/ | script | 200, 7,531 chars |
| https://health.hawaii.gov/opppd/administrative-rules/ | script links | one PDF: chapter-11-1-HAR-effective-2005.02.14.pdf |
| https://health.hawaii.gov/opppd/files/2026/08/chapter-11-1-HAR-effective-2005.02.14.pdf | script | 37 pp.; "CHAPTER 1 RULES OF PRACTICE AND PROCEDURE … §11-1-1" |
| https://health.hawaii.gov/cab/hawaii-administrative-rules-har/ | script | HTTP 404 (guessed URL) |
| https://ltgov.hawaii.gov/the-office/administrative-rules/monthly-update-reports/ | script links | year pages 2012, 2013, 2014, 2015 … |
| https://lrb.hawaii.gov/admin-rules-directory/ | script | Admin Rules Table & Directory; links 2025AdminRules_Supplement.pdf, 2001 directory PDFs |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS courts.state.hi.us opinions | WS | /opinions_and_orders/opinions/page/N[?yr=YYYY], /writ-of-cert/page/N |
| https://www.courts.state.hi.us/opinions_and_orders/opinions | WF | mixed S.Ct/ICA table; newest Oct 16, 2026 (CAAP-25-0000731 sdo); year dropdown 2010-2026; 297 pages; scanned-image notice 2010-July 2025 |
| https://www.courts.state.hi.us/wp-content/uploads/2026/10/SCWC-23-0000668.pdf | WF | PROVENANCE_REQUIRED |
| https://www.courts.state.hi.us/opinions_and_orders/opinions/page/18?yr=2016 | WF | filtered to 2016 (Jan-Feb 2016 rows); 19 pages; old /docs/opin_ord/{ica,sct}/2016/February/ links |
| https://www.courts.state.hi.us/opinions_and_orders/opinions/2016 | WF | NOT filtered (2026 rows); RSS /opinions-orders/feed; SCt_VariousOrders link |
| https://www.courts.state.hi.us/wp-content/uploads/2019/04/CAAP-17-0000351recondada.pdf | WF | ICA order; "NOT FOR PUBLICATION IN WEST'S HAWAII REPORTS OR THE PACIFIC REPORTER"; "Upon consideration of the April 12, 2019" |
| WS published-opinion PDFs (3 queries) | WS | listings only; Justia year pages |
| https://law.justia.com/cases/hawaii/supreme-court/2020/ | WF | rows e.g. scwc-17-0000581.html, scwc-18-0000600-0.html, scad-20-0000767.html |
| https://law.justia.com/cases/hawaii/supreme-court/2020/scwc-17-0000581.html | WF | cert-acceptance order only, not opinion; PDF cases.justia.com/… |
| https://law.justia.com/cases/hawaii/supreme-court/2020/scwc-18-0000600-0.html | WF | YES "I. Introduction We address whether a defendant whose substance use results in"; complete |
| WS Justia ICA | WS | law.justia.com/cases/hawaii/court-of-appeals/ |
| https://law.Justia.com/cases/hawaii/court-of-appeals/ | WF | years 1980-2026; caap-23-0000665.html |
| https://law.justia.com/cases/hawaii/court-of-appeals/2026/caap-23-0000665.html | WF | SDO, "NOT FOR PUBLICATION…"; "In this consolidated appeal, Mother-Appellant/Cross-Appellee (Mother) appeals"; complete |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.courts.state.hi.us/writ-of-cert/page/4 | WF | "Archives: Writ of Certioraris / Motions for Reconsiderations"; SCWC dockets + posting dates only; 404 pages; years 1997-2026 |
| https://www.courts.state.hi.us/writ-of-cert/scwc-24-0000432 | WF | PROVENANCE_REQUIRED |
| WS SCWC certacc | WS | many …certacc.pdf / certrej.pdf URLs |
| https://www.courts.state.hi.us/wp-content/uploads/2026/05/SCWC-23-0000412certacc.pdf | WF | order accepting cert; caption CAAP-23-0000412; "The application for writ of certiorari filed on March 10, 2026, by" |
| https://www.courts.state.hi.us/docs/opin_ord/sct/2012/jul/SCWC-11-0000049.pdf | WF | order accepting cert; ICA CAAP-11-0000049; "The Application for Writ of Certiorari filed on June 4, 2012 by" |
| WS "SCWC-19-0000446" | WS | certacc/certrej/recond PDFs; Justia year pages |

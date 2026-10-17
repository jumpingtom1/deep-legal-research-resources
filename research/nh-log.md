# New Hampshire (nh) probe log, 2026-10-17

All probes were run on 2026-10-17 by `research`. Tools: WF = WebFetch; FD = `scripts/fetch_doc.py --research`; WS = WebSearch (discovery only). Quoted page text is 15 words or fewer per entry. The WebFetch quota ran out once ("session limit · resets 2pm"); work resumed after the reset. 37 WebFetch calls in total, including 7 errors or gated calls.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.gencourt.state.nh.us/robots.txt | FD (x3) | FETCH ERROR: "Remote end closed connection without response" |
| https://gc.nh.gov/robots.txt | FD (x3, incl. after reset) | same, connection closed |
| https://www.courts.nh.gov/robots.txt | FD | REFUSED: bot check on robots.txt |
| https://courts.nh.gov/robots.txt | FD | REFUSED: bot check |
| https://www.courts.state.nh.us/robots.txt | FD | REFUSED: bot check |
| https://www.sos.nh.gov/robots.txt | FD | REFUSED: bot check |
| https://www.nh.gov/robots.txt | FD | REFUSED: bot check |
| https://law.justia.com/robots.txt | FD | REFUSED: robots.txt challenge earlier today; host off for the day |
| https://new-hampshire.public.law/robots.txt | FD | proxy 502 (Tunnel connection failed) |
| https://www.law.cornell.edu/robots.txt | FD | 200; User-agent * Crawl-delay 10; /regulations/ not disallowed |

## A: Statutes
| URL | Tool | Result |
|---|---|---|
| WS "gencourt.state.nh.us/rsa/html 358-A" | WS | found gc.nh.gov/rsa/html/nhtoc/NHTOC-LVI-567-A.htm |
| https://www.gencourt.state.nh.us/rsa/html/XXXI/358-A/358-A-2.htm | WF | PROVENANCE_REQUIRED (built URL, gated) |
| https://gc.nh.gov/rsa/html/nhtoc/NHTOC-LVI-567-A.htm | WF | TOC; links /rsa/html/LVI/567-A/567-A-1.htm …; no text; no currency line |
| https://gc.nh.gov/rsa/html/LVI/567-A/567-A-1.htm | WF | YES "A person who is aggrieved by a decree, order, appointment"; "Source. 1975, 395:11." |
| https://gc.nh.gov/rsa/html/XXXI/358-A/358-A-2.htm | WF | PROVENANCE_REQUIRED (gated) |
| https://gc.nh.gov/rsa/html/indexes/default.aspx | WF | first try: quota error; after reset: "current through the 2026 regular legislative session. Last updated: September 2026."; disclaimer "PROVIDED FOR INFORMATIONAL PURPOSES ONLY" |
| https://gc.nh.gov/rsa/html/nhtoc.htm | WF | titles with chapter ranges, "TITLE XXXI … (Includes Chapters 333 - 359-V)" |
| https://gc.nh.gov/rsa/html/NHTOC/NHTOC-XXXI.htm | WF | chapter links, e.g. NHTOC-XXXI-358-A.htm; no merged link |
| https://gc.nh.gov/rsa/html/NHTOC/NHTOC-XXXI-358-A.htm | WF | PROVENANCE_REQUIRED, although linked from the page above |
| https://gc.nh.gov/rsa/html/NHTOC/NHTOC-X-126-G.htm (from WS) | WF | section links X/126-G/126-G-1.htm …; merged 126-G-mrg.htm |
| https://gc.nh.gov/rsa/html/X/126-G/126-G-2.htm | WF | YES "In this chapter: I. "Area" means"; Source "1989, 255:2. 1995, 310:79" |
| https://gc.nh.gov/rsa/html/X/126-G/126-G-mrg.htm | WF | YES all of 126-G:1-5; not truncated |
| https://gc.nh.gov/rsa/html/LVI/567-A/567-A-1.htm | FD | FETCH ERROR (robots.txt unreachable, connection closed) |
| https://www.gc.nh.gov/dynamicdatadump (from WS) | WF | 13 .txt files: legislators, LSRs, docket, roll calls; no RSA text |
| WS "law.justia.com codes new-hampshire …" | WS | found /codes/new-hampshire/title-xliii/ |
| https://law.justia.com/codes/new-hampshire/title-xliii/ | WF | "2025 New Hampshire Revised Statutes"; chapter links chapter-457/, chapter-458/ … |
| https://law.justia.com/codes/new-hampshire/title-xliii/chapter-458/ | WF | section links section-458-1/ … |
| https://law.justia.com/codes/new-hampshire/title-xliii/chapter-458/section-458-2/ | WF | YES "If any doubt exists whether any marriage is void, or"; "These codes may not be the most recent version." |

## B: Constitution
| URL | Tool | Result |
|---|---|---|
| WS (3 queries) for an official constitution page | WS | only Justia and third parties |
| https://en.wikipedia.org/wiki/Constitution_of_New_Hampshire | WF | discovery only: official link https://www.nh.gov/glance/state-constitution |
| https://www.nh.gov/glance/state-constitution | WF | CLIENT_ERROR "There was an error while fetching." |
| same | FD links | REFUSED: bot check on robots.txt |
| https://law.justia.com/constitution/new-hampshire/ | WF | index; Art. 15 NOT PRESENT; links billofrights.html, formofgov.html |
| https://law.justia.com/constitution/new-hampshire/billofrights.html | WF | YES "No subject shall be held to answer for any crime,"; header "IN FORCE DECEMBER 1990" |

## C: Court rules
| URL | Tool | Result |
|---|---|---|
| https://courts.nh.gov/rules-superior-court-state-new-hampshire (from WS) | WF | CLIENT_ERROR "There was an error while fetching." |
| https://www.courts.state.nh.us/rules/index.htm | WF | rule-set names, no hrefs; "is not an official publication of the court rules" |
| https://courts.nh.gov/rules-evidence | WF | YES R. 403 "The court may exclude relevant evidence if its probative value is"; 110,415 chars; cut off at R. 902(4)(A) |
| https://courts.nh.gov/new-hampshire-rules-criminal-procedure | WF | YES R. 1 "These rules govern the procedure in circuit court-district division and"; 136,231 chars; cut off in R. 23 |
| https://www.courts.state.nh.us/rules/scr/index.htm | WF | TOC only; "Rule 7. Appeal from Trial Court Decision on the Merits."; no hrefs |
| same | FD links | REFUSED (host off for the day) |
| https://www.courts.nh.gov/rules-supreme-court-state-new-hampshire/note | WF | note only, "subject to revisions promulgated from time to time" |

## D: Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://gc.nh.gov/rules/about_rules/official_version.aspx | WF | "There is no official publisher of the complete New Hampshire Code of Administrative Rules"; web rules "NOT the official version" |
| https://gc.nh.gov/rules/about_rules/listagencies.aspx | WF | agency links /rules/state_agencies/{prefix}.html (env-a.html, ban.html; some mixed case) |
| https://www.gc.nh.gov/rules/state_agencies/ban.html | WF | TOC; chapter links ban100.html, ban500.html, ban700.html |
| https://gc.nh.gov/rules/state_agencies/ban100.html | WF | YES Ban 101.01 "The purpose of these rules is to describe the New Hampshire" |
| https://www.law.cornell.edu/regulations/new-hampshire | FD info | 200, 8,050 chars |
| …/title-Env/subtitle-Env-Ws/chapter-Env-Ws-300; …/title-Ban; …/title-Ban/chapter-Ban-100; …/part-Ban-101 | FD links | section link N-H-Admin-Code-SS-Ban-101.01 |
| https://www.law.cornell.edu/regulations/new-hampshire/N-H-Admin-Code-SS-Ban-101.01 | FD grep | 2,825 chars; "The purpose of these rules is to describe the New Hampshire banking department" |
| https://www.law.cornell.edu/regulations/new-hampshire/N-H-Admin-Code-SS-Env-Dw-702.01 | FD | 2,755 chars; "#9699, eff 5-1-10"; "Amended by Volume XXXVIII Number 50" |
| https://www.gc.nh.gov/rules/register/availability.aspx | WF | electronic-only since July 14, 2018; links default.aspx |
| https://www.gc.nh.gov/rules/register/default.aspx | WF | issues from 2000; "published weekly each Thursday"; No 34 Aug. 27, 2026 viewer link |
| https://www.gc.nh.gov/rules/register/viewer.aspx?fileName=F:\Websites\GCNHWeb\Rules\register\2026\No 34 August 27 2026.PDF | WF | YES "NEW HAMPSHIRE RULEMAKING REGISTER OFFICE OF LEGISLATIVE SERVICES ROOM 234," |

## E: Case law
| URL | Tool | Result |
|---|---|---|
| https://www.courts.state.nh.us/supreme/opinions/index.htm | WF | notice only; post-2024 opinions "listed … according to the neutral citation form"; no list |
| https://www.courts.nh.gov/news-and-media/supreme-court-announces-adoption-neutral-citation-form | WF | "will receive a citation of 2024 N.H. 1"; paragraph pinpoints; effective Jan. 1, 2024 |
| https://www.courts.nh.gov/taxonomy/term/1856?page=0 | WF | case orders: "2023-0175, State of New Hampshire v. Kevin M. Ruel"; no hrefs or dates |
| https://www.courts.nh.gov/our-courts/supreme-court/orders-and-opinions/opinions | WF | PROVENANCE_REQUIRED (built URL) |
| https://courts.nh.gov/search?page=28 | WF | site search, 11,715 results; PDF hrefs e.g. …/documents/2021-07/2020021torromeo.pdf; no query param seen |
| https://www.courts.nh.gov//sites/g/files/ehbemt471/files/documents/2021-07/2020021torromeo.pdf | WF | PROVENANCE_REQUIRED |
| https://law.justia.com/cases/new-hampshire/supreme-court/2023/ | WF | 61 cases; e.g. Brown v. Secretary of State, 2022-0629, Nov. 29, 2023 |
| https://law.justia.com/cases/new-hampshire/supreme-court/2023/2022-0629.html | WF | "DONOVAN, J. This case presents a question of first impression"; 122,410 chars, cut off; PDF cases.justia.com/…/2023-2022-0629.pdf |

## F: Subsequent history
| URL | Tool | Result |
|---|---|---|
| WS "Lower Ct: Supreme Court of New Hampshire" | WS | dockets 25-1390, 24A1016, 25A49, 25A908 … |
| https://www.supremecourt.gov/docket/docketfiles/html/public/25-1390.html | FD grep | "Lower Ct: Supreme Court of New Hampshire"; "(2025-0297)"; "Oct 05 2026 Petition DENIED." |
| …/24A1016.html; …/25A49.html; …/25A908.html | FD grep | NH lower court; case nos. 2024-0491, 2024-0369, 2025-0454; applications denied |

## Checks
- `python3 scripts/build.py --check`: exit 0, no ERROR/WARN lines.
- `python3 scripts/build.py --cross`: "0 cross-jurisdiction match(es)".

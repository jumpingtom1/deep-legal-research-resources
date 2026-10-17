# Connecticut (ct) probe log — 2026-10-17

Tools: WF = WebFetch; FD = `python3 scripts/fetch_doc.py --research`; WS = WebSearch (discovery only). All on 2026-10-17. Quoted text ≤ 15 words.

## A. Statutes

| URL | Tool | Result |
|---|---|---|
| https://www.cga.ct.gov/current/pub/chap_926.htm | FD info/grep | FETCH ERROR: "TLS certificate chain does not verify from this sandbox" |
| https://www.cga.ct.gov/current/pub/chap_926.htm | WF | PROVENANCE_REQUIRED (built URL, permission not answered) |
| https://www.cga.ct.gov/Current/Pub/titles.htm | WF | ROBOTS_DISALLOWED |
| https://prdext3.cga.ct.gov/2026/sup/chap_926.htm | WF | 200; only §§ 52-592, 52-593a (supplement); "revised to January 1, 2025" |
| https://cga.ct.gov/Current/pub/titles.htm | WF (x2) | OK: "Revised to January 1, 2025"; "2026 Supplement, revised to January 1, 2026"; chapter + section ranges per title |
| https://www.cga.ct.gov/robots.txt | WF | ROBOTS_DISALLOWED |
| https://cga.ct.gov/Current/pub/title_52.htm | WF | ROBOTS_DISALLOWED |
| https://www.cga.ct.gov/Current/pub/title_12.htm | WF | ROBOTS_DISALLOWED (search-result URL) |
| https://cga.ct.gov/Current/pub/title_01.htm | WF | ROBOTS_DISALLOWED (link from titles.htm) |
| https://www.cga.ct.gov/2025/pub/chap_883.htm | WF | ROBOTS_DISALLOWED (search-result URL) |
| https://cga.ct.gov/Current/pub/titles.htm, https://cga.ct.gov/robots.txt | FD | TLS certificate chain does not verify |
| https://prdext3.cga.ct.gov/2026/sup/chap_926.htm | FD info | 200, 8,637 chars (not used further: alternate server hostname) |
| https://prdext3.cga.ct.gov/robots.txt | FD read | "# robots.txt for https://www.cga.ct.gov"; Disallow /cgi-bin/, /asp/menu/, /html/, /images/, /js/ … ; nothing for /Current/pub/ |
| WS "prdext3.cga.ct.gov" site:ct.gov | WS | only indexed node URLs; no CGA page found linking prdext hosts → alternate-host rule: not used |
| https://law.justia.com/codes/connecticut/title-52/chapter-926/ | WF | heading "2024 Connecticut General Statutes"; links section-52-577/, section-52-584/ |
| https://law.justia.com/codes/connecticut/title-52/chapter-926/section-52-577/ | WF | YES "No action founded upon a tort shall be brought but"; "2025 Connecticut General Statutes"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/connecticut/title-42/chapter-735a/section-42-110b/ | WF | YES "No person shall engage in unfair methods of competition and" (built URL, not gated) |
| https://law.justia.com/codes/connecticut/title-52/ | WF | "Chapter 926 - Statute of Limitations (Secs. 52-573 to 52-598a)" |
| https://law.justia.com/constitution/connecticut/ | FD info | REFUSED: law.justia.com robots.txt challenge earlier today (host off) |

## B. Constitution

| URL | Tool | Result |
|---|---|---|
| https://portal.ct.gov/SOTS/Register-Manual/Section-I/Constitution-of-the-State-of-Connecticut | FD info/grep/verify | 200, 113,252 chars; art. I § 7 VERIFIED exact at offset 5219; last "Adopted November 30, 2022."; no 2023-2025 dates |
| same | WF | § 7 present; truncated at 100,000 of 114,066 chars (mid amendment Art. XXIX); canonical URL has "archived=true" |
| https://portal.ct.gov/robots.txt | FD read | "Allow: /"; Disallow /sitecore/* and beta paths |
| https://law.justia.com/constitution/connecticut | WF | § 7 present; one page, 112,710 chars, truncated at 100K |

## C. Court rules

| URL | Tool | Result |
|---|---|---|
| https://www.jud.ct.gov/robots.txt, https://www.jud.ct.gov/opinions.htm | FD | FETCH ERROR: SSLV3_ALERT_HANDSHAKE_FAILURE fetching robots.txt |
| https://jud.ct.gov/opinions.htm | FD check | same TLS handshake failure |
| https://www.jud.ct.gov/pub.htm | WF | Lists "Connecticut Practice Book", "Connecticut Code of Evidence, 2023 Edition"; hrefs NOT exposed |
| https://www.jud.ct.gov/Publications/PracticeBook/PB.pdf | WF | PROVENANCE_REQUIRED (built URL from memory) |
| https://jud.ct.gov/LawLib/LawLibNews/Posts/Post.aspx?Id=6154 | WF | Announces amendment to Code of Evidence § 7-3 eff. May 2, 2023; "NO URLS" |

## D. Admin code / register

| URL | Tool | Result |
|---|---|---|
| https://eregulations.ct.gov/robots.txt | FD | HTTP 404 (no rules) |
| https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_22aSubtitle_22a-174Section_22a-174-1/ | FD info/read/links | 200, 2,223 chars, navigation only ("Browse>List of Titles") |
| https://eregulations.ct.gov/eRegsPortal/Browse/RCSA | FD links | 2,211 chars, 0 title links (JavaScript app) |
| https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_20Subtitle_20-406Section_20-406-2-20-406-3 | WF | NOT PRESENT; navigation only |
| https://www.law.cornell.edu/regulations/connecticut/title-22a | WF | links /title-22a/1, /1a, /2a; "State regulations are updated quarterly; we currently have two versions available." |
| https://www.law.cornell.edu/regulations/connecticut/title-22a/174 | FD links | § 22a-174-1 → /regulations/connecticut/Regs-Conn-State-Agencies-SS-22a-174-1 |
| https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-22a-174-1 | FD grep/verify | 37,231 chars; "Except as may otherwise be provided" VERIFIED |
| https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-17b-262-1 | FD grep | "Conn. Agencies Regs. § 17b-262-1 Effective June 4, 1996" |

## E. Case law

| URL | Tool | Result |
|---|---|---|
| https://jud.ct.gov/external/supapp/archiveAROsup.htm | WF | archive from July 2000; year links 2000-2026; hrefs not shown |
| https://jud.ct.gov/external/supapp/archiveAROsup24.htm | WF | PROVENANCE_REQUIRED (built) |
| https://jud.ct.gov/external/supapp/aro.htm | WF | dated "Friday, January 16, 2026"; "subject to modification and technical correction prior to official publication"; no hrefs |
| https://jud.ct.gov/external/supapp/archiveAROsup04.htm | WF (x2) | "SC16446 - State v. Colon" under "Published in Connecticut Law Journal - 12/28/04"; asked for link targets → "NO URLS" |
| https://www.jud.ct.gov/lawjournal/Docs/Appellate/FullVolume/AP108.pdf | WF | "Official Connecticut Appellate Reports, Volume 108"; Cabral at p. 1; truncated at 100K of 112,939 |
| https://www.jud.ct.gov/lawJournal/CR/ConnecticutReports.aspx | WF | electronic from vol. 320; Vol. 353 segments, e.g. "10/07/2025 Connecticut Reports Vol.353 Pages 564 - 665"; no hrefs |
| https://jud.ct.gov/LawJournal/CR/ConnecticutReports.aspx | WF | "01/20/2026 Orders Vol.354 Pages 901 - 901"; no earlier-volume selector visible |
| https://www.jud.ct.gov/faq/lawjournal.htm | WF | Law Journals "published after June 13, 2017" online |
| https://www.jud.ct.gov/lawjournal/Docs/Appellate/2025/27/md233_8701.pdf | WF | "233 Conn. App. MEMORANDUM DECISIONS 903"; "CONNECTICUT LAW JOURNAL July 1, 2025" |
| https://law.justia.com/cases/connecticut/supreme-court/2023/ | WF | Alico, LLC v. Somers SC20748 → /2023/sc20748.html |
| https://law.justia.com/cases/connecticut/supreme-court/2023/sc20748.html | WF | full opinion; "General Statutes § 12-71 (f) (1)1 authorizes Connecticut towns to"; PDF cases.justia.com; no official cite |
| https://law.justia.com/cases/connecticut/court-of-appeals/ | WF | years 1983-2026 |
| https://law.justia.com/cases/connecticut/court-of-appeals/2024/ | WF | Unifoods v. Magallanes AC46166 → /2024/ac46166.html |
| https://law.justia.com/cases/connecticut/court-of-appeals/2024/ac46166.html | WF | full opinion "MOLL, J. The plaintiff, Unifoods, S.A. de C.V., appeals from"; header "0 Conn. App. 1" placeholder |
| https://law.justia.com/cases/connecticut/supreme-court/ | WF | years 1846-2026 |

## F. Subsequent history

| URL | Tool | Result |
|---|---|---|
| https://www.jud.ct.gov/lawjournal/Docs/CTReports/2025/27/ord352_8701.pdf | WF | "Certification Petition Denials, June 17, 2025"; State v. Overstreet, 232 Conn. App. 273 (AC 46253) denied; heads "ORDERS 910 352 Conn." |

## Budget

WebFetch calls: 41 (incl. 4 permission-gated / 7 robots refusals). No quota or rate failures.

## Build

- `build.py --check`: no ERROR/WARN for ct.json.
- `build.py --cross`: two remaining lines are North Carolina's statute pattern claiming Connecticut examples — `'C.G.S. § 52-190a'` (NC's `\bG\.S\.` matches inside "C.G.S.") and `'section 52-584 of the General Statutes'` (NC's prose alternative has optional "North Carolina"). Fix belongs in nc.json: `(?<![\w.])G\.S\.` and mark the bare prose form context_required. CT's own bare prose form is already context_required; examples left unchanged.

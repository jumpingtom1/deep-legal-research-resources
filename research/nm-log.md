# New Mexico (nm) probe log — 2026-10-17

All probes by `research`. "shell" = `scripts/fetch_doc.py --research` (obeys robots.txt, bot checks, 1.1 s/host). "WF" = WebFetch. "WS" = WebSearch.

Session notes:
- First pass (2026-10-17 ~00:05) stopped when WebFetch returned a session usage limit ("You've hit your session limit"); resumed after reset (~09:10).
- WebFetch on URLs I built (nmonesource.com, laws.nmonesource.com, srca.nm.gov) returned PROVENANCE_REQUIRED (permission prompt unanswered); not retried. WebFetch calls used: 16.
- nmonesource.com answered HTTP 403 to the shell on roughly half of requests, apparently at random (same URL shapes succeeded seconds earlier). fetch_doc.py marks each refused URL off for the day; none was retried.

## Host checks (shell)
| URL | Result |
|---|---|
| https://nmonesource.com/robots.txt | 200; `User-agent: BUbiNG` Disallow /; `*` disallows two /icm/ items only |
| https://laws.nmonesource.com/robots.txt | check: permits |
| https://www.nmcourts.gov/robots.txt, supremecourt.nmcourts.gov, coa.nmcourts.gov | 200, empty body (0 chars) |
| https://caselookup.nmcourts.gov/caselookup/ | FETCH ERROR: robots.txt unreachable after retry (connection closed) — not used |
| https://www.srca.nm.gov/nmac-home/ | check: robots permits |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WS "nmonesource.com nmos nmsa en item index.do 37-1-8" | WS | nmonesource /ti/, /nmsl/ document.do URLs; no NMSA item |
| WS "site:nmonesource.com nmsa document.do chapter 37" | WS | nmcompcomm scope-of-coverage URLs |
| https://nmonesource.com/nmos/en/nav.do | shell | 200, 117 chars: "Home Scope of Coverage Contact Us … Website last modified: 10/16/2026" (shell page) |
| https://nmonesource.com/nmos/nmsa/en/nav_date.do (and nmsc, nmca, nmra, nmsl, ti) | shell | 200, ~230 chars each, breadcrumb only; raw HTML shows iframe src `?iframe=true`; /nmos/nmc/ and /nmos/nmconst/ 404 |
| https://nmonesource.com/nmos/nmsa/en/nav_date.do?iframe=true | shell | chapter rows "Chapter 1 - Elections" → item/4351/index.do and 4351/1/document.do; 4 pages |
| https://nmonesource.com/nmos/nmsa/en/nav_date.do?page=2&iframe=true | shell | "Chapter 37 - Limitation of Actions…" → item 4366; ch. 41 → 4382 |
| https://nmonesource.com/nmos/nmsa/en/4366/1/document.do | shell | PDF 160 pp, 430,719 chars, filename 8-11-26_chapter-37-…-2026.pdf; "37-1-8. Actions against sureties on fiduciary bonds; injuries to person or reputation." at p. 51 |
| https://nmonesource.com/nmos/nmsa/en/4382/1/document.do | shell | PDF 322 pp, 874,366 chars; "41-4-4. Granting immunity from tort liability" p. 106 |
| https://www.nmcompcomm.us/scope-of-coverage-2/ | shell | 12,793 chars; "current through the Second Session of the Fifty-Seventh Legislature (2026)" |
| https://www.nmcompcomm.us/scope-of-coverage-2/ | WF | currency strings confirmed; no official/authenticated statement; ~300 nmonesource links incl. laws.nmonesource.com/w/nmos/Chapter-{X}-NMSA-1978 and unannotated ids |
| https://laws.nmonesource.com/w/nmos/Chapter-37-NMSA-1978 | shell | redirect → nmonesource.com/nmos/nmsa/en/item/4366/index.do |
| https://laws.nmonesource.com/w/nmos/Chapter-41-NMSA-1978 | shell | redirect → item/4382 |
| https://nmonesource.com/nmos/nmsa-unanno/en/nav_date.do?iframe=true | shell | chapter rows, ids 18502… |
| https://nmonesource.com/nmos/nmsa-unanno/en/nav_date.do?page=2&iframe=true | shell | REFUSED HTTP 403 |
| https://nmonesource.com/nmos/nmsa-unanno/en/18537/1/document.do | shell | REFUSED HTTP 403 |
| https://nmonesource.com/nmos/nmsl/en/18777/1/document.do | WF | (from WS) "2023 First Regular Session, Newly Enacted NMSA 1978 Section Numbers" table; PDF read |
| https://nmonesource.com/nmos/ti/en/15078/1/document.do | WF | session-limit error (quota), not a site refusal |
| WS "law.justia.com New Mexico Statutes 37-1-8 …" | WS | justia /codes/new-mexico/2019/chapter-37/article-1/section-37-1-8 |
| https://law.justia.com/codes/new-mexico/2019/chapter-37/article-1/section-37-1-8 | WF | YES "Actions must be brought against sureties on official bonds and"; "2019 New Mexico Statutes" |
| https://law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-8/ | WF | YES; "2025 New Mexico Statutes"; "NM Stat § 37-1-8 (2025)"; not truncated |
| https://law.justia.com/codes/new-mexico/chapter-41/article-4/section-41-4-4/ | WF | YES "A governmental entity and any public employee while acting within"; 2025 |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://nmonesource.com/nmos/nmsc/en/nav_date.do?iframe=true | shell | 5,850 chars; year links 1852–2026; "43 result(s)" 2026; links nav_alpha / nav_neu / nav_re |
| https://nmonesource.com/nmos/nmsc/en/2019/nav_date.do?iframe=true | shell | 25 rows, e.g. GandyDancer → item/454344 |
| https://nmonesource.com/nmos/nmsc/en/item/459534/index.do | shell | 256-char shell |
| https://nmonesource.com/nmos/nmsc/en/item/459534/index.do?iframe=true | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmsc/en/459534/1/document.do | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmsc/en/item/459534/index.do | WF | PROVENANCE_REQUIRED (unanswered) |
| WS "site:nmonesource.com nmsc 2019-NMSC-012"; WS "nmonesource.com/nmos/nmsc/en/item index.do opinion" | WS | no nmonesource opinion URLs |
| https://nmonesource.com/nmos/en/nav.do?iframe=true | shell | collection list: nmsc, nmca, oct, sum (AI summaries), nmsa, nmra, nmsa-unanno, nmra-unanno, historical, nmtlt, ag, c, secap, nmac, nmsl, forms, ti |
| https://nmonesource.com/nmos/nmca/en/2024/nav_date.do?iframe=true | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmca/en/nav_date.do?iframe=true | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmsc/en/nav_neu.do?iframe=true | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmsc/en/454344/1/document.do | shell | PDF 13 pp, 37,099 chars, 19sc-021_auth.pdf; "Opinion Number: 2019-NMSC-021", "No. S-1-SC-37201", "{1} The district court certified for interlocutory review…" |
| https://nmonesource.com/nmos/en/d/s/index.do?cont=&ref=2019-NMSC-021&d1=&d2=&p=&col=&or=date&iframe=true | shell | GET search OK: GandyDancer → nmsc item 454344 (+ AI summary row) |
| …?ref=2020-NMCA-034… | shell | State v. Jackson → nmca item 483661 |
| https://nmonesource.com/nmos/nmca/en/483661/1/document.do | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmca/en/item/483661/index.do | WF | PROVENANCE_REQUIRED |
| …?ref=2018-NMCA-064… | shell | Gandydancer (COA) → item 392375 |
| https://nmonesource.com/nmos/nmca/en/392375/1/document.do | shell | PDF 10 pp, 18ca-064_auth.pdf; "Certiorari Granted, October 15, 2018, No. S-1-SC-37201"; "Opinion Number: 2018-NMCA-064" |
| …?cont=%22S-1-SC-37201%22… and ?cont=S-1-SC-37201… | shell | REFUSED 403 (both) |
| …?ref=1997-NMSC-001… | shell | REFUSED 403 |
| https://supremecourt.nmcourts.gov/ | shell | links: Opinions, Rules & Forms, Case Lookup |
| https://supremecourt.nmcourts.gov/rules-forms-files/opinions/ | shell | "…New Mexico Compilation Commission website, which is the official legal publisher for the Supreme Court" → nmonesource link |
| WS "New Mexico Supreme Court opinions page nmcourts.gov …" | WS | irrelevant (CAP demo JSON) |
| https://coa.nmcourts.gov/ | shell | links Formal Opinions, Memorandum Opinions |
| https://coa.nmcourts.gov/opinions-oral-arguments/formal-opinions/ | shell | 1,634 links; "Filed in 2009"…"2026"; "Caution: These electronic slip opinions may contain computer-generated errors" |
| https://coa.nmcourts.gov/opinions-oral-arguments/memorandum-opinions/ | shell | 3,779 links; 2018–2026; sealed cases not posted |
| https://coa.nmcourts.gov/wp-content/uploads/sites/43/2026/01/January-29-2026-State-of-New-Mexico-v.-Bobby-Charles-Crawford-No.-A-1-CA-41857.pdf | shell | PDF 29 pp, 49,493 chars; "Opinion Number: __________"; line-numbered |
| https://coa.nmcourts.gov/wp-content/uploads/sites/43/2026/01/January-29-2026-Emil-Mottola-v.-Triad-National-Security-LLC-No.-A-1-CA-41722.pdf | shell | PDF 19 pp, 30,752 chars |
| https://law.justia.com/cases/new-mexico/supreme-court/2019/ | WF | GandyDancer → /2019/s-1-sc-37201.html; other rows s-1-sc-37077, s-1-sc-36537 |
| https://law.justia.com/cases/new-mexico/supreme-court/2019/s-1-sc-37201.html | WF | YES; {1}–{43}; "2019-NMSC-021" in header; not truncated |
| https://law.justia.com/cases/new-mexico/court-of-appeals/2020/ | WF | rows e.g. /2020/a-1-ca-39058.html "(Unpublished Opinion)"; no Jackson on page 1 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://nmonesource.com/nmos/nmra-unanno/en/nav_date.do?iframe=true | shell | Rule Set rows 18468 (Set 1) …; Set 11 → 18481, 12 → 18482, 16 → 18486 |
| https://nmonesource.com/nmos/nmra-unanno/en/18468/1/document.do | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmra-unanno/en/18481/1/document.do | shell | PDF 67 pp, 151,784 chars, 12-31-25_unannotated_rule-set-11…; "11-702. Testimony by expert witnesses." p. 40 |
| https://nmonesource.com/nmos/nmra-unanno/en/18482/1/document.do | shell | PDF 127 pp, 346,651 chars; "12-502. Certiorari from the Supreme Court to the Court of Appeals." p. 100; Rule 23-112 NMRA references |
| https://nmonesource.com/nmos/nmra-unanno/en/18486/1/document.do | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmra/en/nav_date.do?iframe=true | shell | REFUSED 403 |
| https://laws.nmonesource.com/w/nmos/Rule-Set-1-NMRA | shell | redirect → nmra item 5687 |
| https://laws.nmonesource.com/w/nmos/Rule-Set-1-NMRA | WF | PROVENANCE_REQUIRED |
| https://laws.nmonesource.com/w/nmos/Rule-Set-11-NMRA | shell | redirect → nmra item 5665 |
| https://nmonesource.com/nmos/nmra/en/5687/1/document.do | shell | REFUSED 403 |
| https://nmonesource.com/nmos/nmra/en/5665/1/document.do | shell | REFUSED 403 |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://nmonesource.com/nmos/c/en/nav_date.do?iframe=true | shell | "Constitution of New Mexico" item 5916; U.S. Constitution 5812 |
| https://nmonesource.com/nmos/c/en/5916/1/document.do | shell | PDF 1,422 pp, 4,024,971 chars, nm_const_2026.pdf; "Sec. 10. [Searches and seizures.]" p. 25; "Sec. 18. [Due process; equal protection; sex discrimination.]" p. 511 |
| https://law.justia.com/constitution/new-mexico/ | WF | index only (NOT PRESENT); articles I–XXII, XXIV; "may not be the most recent version" |
| https://law.justia.com/constitution/new-mexico/article-ii/ | WF | section list only (NOT PRESENT) |
| https://law.justia.com/constitution/new-mexico/article-ii/section-10/ | WF | YES "The people shall be secure in their persons, papers, homes"; no date |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.srca.nm.gov/ | shell | NMAC title links, NM Register link |
| https://www.srca.nm.gov/parts/title16/16.010.0008.html | shell | 6,764 chars; 16.10.8.1–16.10.8.8; Last-Modified 21 Apr 2025 |
| https://www.srca.nm.gov/parts/title01/01.024.0001.html | shell | 17,099 chars; "1.24.1.7 DEFINITIONS" |
| https://www.srca.nm.gov/parts/title16/16.010.0008.html | WF | PROVENANCE_REQUIRED |
| https://www.srca.nm.gov/nmac-home/ | shell | "The Official site of the New Mexico Administrative Code"; "Last Update: September 18, 2026" |
| https://www.srca.nm.gov/nmac-home/new-mexico-register/ | shell | issue links (Vol. XXXVII Issue 19, Oct. 6, 2026); archives 2001–2025 |
| https://www.srca.nm.gov/nmac-home/new-mexico-register/volume-xxxvii-issue-19/ | shell | "PDF Version of Entire Issue" → prod-rf-lambda.rtssaas.com …/xxxvii19c.pdf |
| https://prod-rf-lambda.rtssaas.com/PublicFiles/d89c47bd0d70402dba89b03a22bda6d1/efb63e06-9632-4c97-b6c7-a706777a9933/xxxvii19c.pdf | shell | PDF 42 pp, 231,267 chars; "The official publication for all official notices of rulemaking" |
| https://www.law.cornell.edu/regulations/new-mexico/N-M-Admin-Code-SS-21.16.9.1 | WF | (from WS) issuing-agency section present; "State regulations are updated quarterly" |

## Checks
- `python3 scripts/build.py --check`: exit 0, no ERROR/WARN.
- `python3 scripts/build.py --cross`: 0 cross-jurisdiction matches.

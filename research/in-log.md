# Indiana (in) probe log — 2026-10-17, by research

Tools: `S` = `python3 scripts/fetch_doc.py --research` (info/read/grep/links/check), `W` = WebFetch, `WS` = WebSearch, `C` = curl (only to read the public HTML/JS app shells on hosts with no refusal; no refusal was worked around).

| # | Tool | URL | Result |
|---|---|---|---|
| 1 | S | https://iga.in.gov/robots.txt | 200, kind=html, 0 chars, sha256 61d9d1265c828684 (the app shell; no rules) |
| 2 | S | https://iar.iga.in.gov/robots.txt | 200, 0 chars, sha256 f91bd4e755d1cdd9 (app shell; no rules) |
| 3 | S | https://www.in.gov/robots.txt | 200, "User-agent: *" + Sitemap only, no Disallow |
| 4 | S | https://rules.incourts.gov/robots.txt | HTTP 404 (no rules) |
| 5 | S | https://public.courts.in.gov/robots.txt | 200; Disallow /MYCASE/ca…, /Appellate, /Docket, /AppellateDocket, /*.pdf, … |
| 6 | S | https://law.justia.com/robots.txt | REFUSED: robots.txt challenge earlier today; host off for the day (script) |
| 7 | S | https://iga.in.gov/laws/2025/ic/titles/34 | 200, 0 chars, same shell sha as #1 |
| 8 | WS | iga.in.gov Indiana Code download PDF title 34 2025 | Justia results only |
| 9 | WS | "iga.in.gov/laws/2025/ic/titles" | no IGA pages |
| 10 | S | https://iga.in.gov/ (links) | 0 links |
| 11 | S | iga.in.gov /api/2025/ic/titles, /laws/2025/ic/titles/34/pdf, /ic/2025/Title_34.pdf, /static-documents/ic/2025/title34.pdf | all 0-char shell, same sha |
| 12 | C | https://iga.in.gov/ ; /static/js/main.0fd45481.js ; /asset-manifest.json ; /manifest.json | all return the same 691-byte HTML shell (server: AmazonS3) |
| 13 | W | https://iga.in.gov/laws/2025/ic/titles/34 | PROVENANCE_REQUIRED: permission timed out (gated built URL); not retried |
| 14 | WS | "iga.in.gov" "Indiana Code" title 34 pdf … (extended) | found https://iga.in.gov/laws/ic/downloads |
| 15 | W | https://iga.in.gov/laws/ic/downloads | JS shell: "You need to enable JavaScript to run this app." |
| 16 | WS | "iga.in.gov/static-documents" Indiana Code title pdf | nothing usable |
| 17 | W | https://law.justia.com/codes/indiana/2025/ | title list; "These codes may not be the most recent version." |
| 18 | W | https://law.justia.com/codes/indiana/title-34/ | heading "2025 Indiana Code Title 34. Civil Law and Procedure" |
| 19 | W | https://law.justia.com/codes/indiana/title-34/article-11/ | chapter-2 link |
| 20 | W | https://law.justia.com/codes/indiana/title-34/article-11/chapter-2/ | section links, no text |
| 21 | W | …/chapter-2/section-34-11-2-4/ | YES: "Sec. 4. (a) An action for: (1) injury to person"; not truncated |
| 22 | W | https://law.justia.com/codes/indiana/title-35/article-42/chapter-1/section-35-42-1-1/ | YES (built URL, not gated): "Sec. 1. A person who: (1) knowingly or intentionally kills"; 2025 |
| 23 | WS | Indiana Constitution full text official site in.gov | Justia art1, in.gov/history pages |
| 24 | S | https://www.in.gov/history/…/constitution-of-1851/ | 9,850 chars, index only; breadcrumb "Constitution of 1851 as originally written" |
| 25 | W | https://law.justia.com/constitution/indiana/art1.html | YES § 12: "All courts shall be open; and every person, for injury"; page through § 37 |
| 26 | S | https://rules.incourts.gov/ | 0 chars, 0 links (JS shell) |
| 27 | WS | rules.incourts.gov Trial Procedure Rule 12 current.htm | /Content/trial/rule1/current.htm, trial.pdf, default.htm |
| 28 | S | https://rules.incourts.gov/Content/trial/rule12/current.htm | 8,954 chars; "Effective July 1, 2026 (A) When presented." |
| 29 | S | https://rules.incourts.gov/Content/evidence/rule702/current.htm | 2,028 chars; "A witness who is qualified as an expert by knowledge" |
| 30 | S | https://rules.incourts.gov/Content/appellate/rule65/current.htm | 4,922 chars; "memorandum decision issued on or after January 1, 2023, may be cited" |
| 31 | S | https://rules.incourts.gov/Content/trial/default.htm (links) | 129 links; Rule 3.1 → /rule3-1/current.htm |
| 32 | S | https://rules.incourts.gov/Content/index.htm (links) | 31 links; set keys (trial, evidence, appellate, criminal, prof-conduct, admission-discipline, …) |
| 33 | S | /Content/{criminal,prof-conduct,admission-discipline}/default.htm | rule1-1…, preamble, rule1 … links |
| 34 | S | https://rules.incourts.gov/pdf/PDF%20-%20Trial/trial.pdf | pdf 216 pp, 462,254 chars; Last-Modified 31 Jul 2026 |
| 35 | S | https://rules.incourts.gov/Content/prof-conduct/rule1-7/current.htm | "Rule 1.7. Conflict of Interest: Current Clients Effective January 1, 2005" |
| 36 | S | https://rules.incourts.gov/Content/criminal/rule1-1/current.htm | "Rule 1.1. Scope of the Rules Effective January 1, 2024" |
| 37 | W | https://rules.incourts.gov/Content/trial/rule1/current.htm | YES: "Except as otherwise provided, these rules govern the procedure and"; "Effective January 1, 2026"; no disclaimer |
| 38 | S | default.htm PDF links for 6 sets; info on evidence/appellate/criminal/professional-conduct/admission-discipline PDFs | 50/116/36/170/194 pp |
| 39 | S | trial.pdf grep "Rule 12\. Defenses" | page 51, "Effective July 1, 2026" |
| 40 | S | https://www.in.gov/courts/appellate/opinions/ | HTTP 404 |
| 41 | WS | Indiana appellate opinions in.gov … | /courts/help/decisions/, transfer-YYYY-MMDD.pdf |
| 42 | S | https://www.in.gov/courts/help/decisions/ | help text: "250 most recent opinions"; collection "dates back to 2005" |
| 43 | S | https://public.courts.in.gov/decisions | 1,532 chars, Vue app shell; footer "not to be considered or used as an official court record" |
| 44 | C | https://public.courts.in.gov/decisions ; /Decisions/app/app.js | JS shows GET api/Search, api/Dropdown/{Court,County,Judge,CaseCategory} |
| 45 | S | https://public.courts.in.gov/Decisions/api/Search | JSON, 382,204 chars, newest 10/16/2026 26A-DC-00221 |
| 46 | S | …/Decisions/api/Document/Opinion?Id=m0gt7s1_… | pdf 29 pp, 54,398 chars, filename Opinion.pdf; slip pagination "Page 1 of 29" |
| 47 | S | …/Decisions/api/Dropdown/Court | Supreme 9510, Court of Appeals 9530, Tax Court 9550 |
| 48 | S | …/api/Search?caseParty=Walls&fromDate=10/01/2026&toDate=10/17/2026(&showMemorandum=true) | 1 row 26A-DC-00221 |
| 49 | S | …/api/Search?courtId=9530&fromDate=09/01/2026&toDate=09/05/2026 ± showMemorandum=true | 30 rows (23 mem.) vs 7 rows |
| 50 | S | …/api/Search?courtId=9510 years 2004, 2005-2008, 2011, 2014, 2017 | 2004: 0; 2005 earliest 6/23/2005; 2008: 101 rows |
| 51 | S | https://www.in.gov/judiciary/opinions/pdf/11250901.pdf | HTTP 404 (legacy archive gone) |
| 52 | S | https://www.in.gov/courts/clerk/files/transfer-2026-0213.pdf | pdf 2 pp, 6,104 chars; "25A-CR-338 Kamal Nour v. State of Indiana Appellant Denied" |
| 53 | S | https://www.in.gov/courts/clerk/ (links) | "Transfer Dispositions" → /courts/clerk/transfer |
| 54 | S | https://www.in.gov/courts/clerk/transfer/ | 64 links, weekly PDF+XLSX; archive 2026/2025/2024; "10/09/2026 21 0 21" |
| 55 | S check | https://public.courts.in.gov/mycase/Case/CaseSummary | REFUSED: robots Disallow: /MYCASE/ca |
| 56 | S check | https://public.courts.in.gov/mycase/ | OK (robots permits the app root) |
| 57 | S check | https://public.courts.in.gov/Appellate/ | REFUSED: robots Disallow: /Appellate |
| 58 | S | https://iar.iga.in.gov/ ; /code/current/410 | 0-char shell, same sha |
| 59 | S | http://iac.iga.in.gov/iac/ | FETCH ERROR: robots.txt unreachable, SSL UNEXPECTED_EOF |
| 60 | WS | iar.iga.in.gov Indiana Administrative Code title 410 article 1 pdf | regulations.justia.com (not tier 2) |
| 61 | S | https://www.law.cornell.edu/regulations/indiana (+ title-410, article-1, rule pages) | 10,737 chars; title list; rule slugs irregular |
| 62 | S | LII 410-IAC-1-1-1, 170-IAC-1-1.1-1, 312-IAC-9-2-2 | body present ("Sec. 1. Every child less than nineteen (19) years of age") |
| 63 | S | LII 410-IAC-1-1-1 grep currency | "State regulations are updated quarterly"; title caption mislabelled IURC |
| 64 | WS | "iar.iga.in.gov" register document IR pdf | agency copies of IR docs only |
| 65 | C | https://iar.iga.in.gov/ ; /static/js/main.a7e305e4.js | both return the HTML shell (735 bytes) |
| 66 | W | https://law.justia.com/cases/indiana/supreme-court/2025/ | YES list; 25s-cr-00349.html, 25s-pl-00103.html |
| 67 | W | https://law.justia.com/cases/indiana/supreme-court/2025/25s-pl-00103.html | full opinion "Massa, Justice. This case concerns application of the final judgment rule"; not truncated |

WebFetch calls: 13 (1 gated). No quota/rate failures.

`build.py --check`: exit 0, no ERROR/WARN for in.json. `build.py --cross`: no line starting `in:` or naming `in`.

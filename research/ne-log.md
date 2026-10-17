# Nebraska (ne) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt reads and one download of the rules.nebraska.gov app shell and its public JS bundle (robots allows all) to find API routes — no refusal was worked around. Some hrefs were read from fetch_doc.py's own cache because `fetch_doc.py links` crashes on nebraskajudicial.gov pages (malformed href `site:url-brief`). WebFetch calls: 19 (of ~55); 4 hit the provenance gate (built/linked URLs, not retried), 1 CLIENT_ERROR (wrong Justia slug). WebSearch: 5.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://nebraskalegislature.gov/robots.txt | curl | 200; `User-agent: *` Disallow /trans/search.php, two /bills/ search pages; Crawl-delay 3 |
| https://supremecourt.nebraska.gov/robots.txt | curl | 301 -> https://nebraskajudicial.gov/robots.txt: Drupal default (Disallow /core/ /admin/ /search/ /user/...) |
| https://sos.nebraska.gov/robots.txt | curl | Drupal default; /search/, /user/* disallowed |
| https://www.nebraska.gov/robots.txt | curl | Disallow /demo/billtrack/ /app-fsp/; Allow / |
| https://rules.nebraska.gov/robots.txt | curl | `User-agent: *` `Disallow:` (empty) |
| https://law.justia.com/codes/nebraska/ | script check | REFUSED: robots.txt answered with a bot check |
| https://nebraska.public.law/statutes | script check | FETCH ERROR: proxy 502 on robots.txt |
| https://www.law.cornell.edu/regulations/nebraska | script check | OK; robots permits; crawl-delay 10 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://nebraskalegislature.gov/laws/statutes.php?statute=25-207 | script | 200 html 26,651 chars; "25-207. Actions for trespass, conversion, other torts, and frauds; exceptions." |
| same | WF | PROVENANCE_REQUIRED (gated; not retried) |
| https://nebraskalegislature.gov/laws/statutes.php?statute=27-702 | script grep | "a witness qualified as an expert by knowledge, skill, experience" |
| https://nebraskalegislature.gov/laws/statutes.php?statute=77-2701.10 | script grep | "77-2701.10. Contractor or repairperson, defined." |
| https://nebraskalegislature.gov/laws/ucc.php?code=2-207 | script grep | "2-207. Additional terms in acceptance or confirmation." |
| https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=25 | script | 224,512 chars; flat list "View Statute 25-201 Civil actions; when commenced." |
| WebSearch "nebraskalegislature.gov statutes.php 25-207 …" | WS | browse-chapters.php?chapter=25; Justia year editions |
| https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=25 | WF | YES list; no article ranges; truncated at 25-1013 |
| https://nebraskalegislature.gov/laws/laws.php | script | Reissue/Supplement PDF list; "Supplement 2025", "Cumulative Supplement 2024" table |
| https://nebraskalegislature.gov/contact/disclaimer.php | script grep | "refer to the printed version of the appropriate official publication" |
| https://nebraskalegislature.gov/laws/browse-ucc.php | script (cache hrefs) | /laws/ucc.php?code=1-101 … |
| https://nebraskalegislature.gov/pdf/revisor/2016reissue_v2.pdf | script info | pdf 1,297 pages, 6,189,605 chars; Last-Modified Oct 3 2016 |
| https://law.justia.com/codes/nebraska/ | WF | "2025 Nebraska Revised Statutes" -> /codes/nebraska/2025/ |
| https://law.justia.com/codes/nebraska/chapter-25/section-25-207/ | WF | CLIENT_ERROR (wrong slug) |
| https://law.justia.com/codes/nebraska/2025/ | WF | chapter links /codes/nebraska/chapter-N/, no ranges |
| https://law.justia.com/codes/nebraska/chapter-25/ | WF | section link …/chapter-25/statute-25-207/ |
| https://law.justia.com/codes/nebraska/chapter-25/statute-25-207/ | WF | YES "The following actions can only be brought within four years:"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/nebraska/chapter-27/statute-27-702/ | WF | YES "If scientific, technical, or other specialized knowledge will assist the" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://nebraskalegislature.gov/laws/browse-constitution.php | script links | articles.php?article=I-1 …; VIII-1A, VIII-1B, VIII-2A |
| https://nebraskalegislature.gov/laws/articles.php?article=I-3 | script grep | "I-3. Due process of law; equal protection. No person shall be deprived" |
| https://nebraskalegislature.gov/laws/articles.php?article=V-2 | script grep | "The Supreme Court shall consist of seven judges" |
| https://nebraskalegislature.gov/FloorDocs/Current/PDF/Constitution/constitution.pdf | script | pdf 91 pages, 235,777 chars; "Certified by Secretary of State's Office … December 2, 2024" |
| https://law.justia.com/constitution/nebraska/ | WF | I-3 -> c0101003000.html; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/nebraska/c0101003000.html | WF | YES "No person shall be deprived of life, liberty, or property," |
| https://law.justia.com/constitution/nebraska/c0105002000.html | WF | Section V-2; "The Supreme Court shall consist of seven judges, one of whom" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WebSearch "nebraskajudicial.gov supreme court rules § 6-1112 pleadings" | WS | article-11 page, /book/export/html/9131 |
| https://nebraskajudicial.gov/supreme-court-rules/chapter-6-trial-courts/article-11-nebraska-court-rules-pleading-civil-cases | script | redirects to …-effective-january-1-2025; 19,039 chars TOC; `links` crashed (ValueError) |
| …/%C2%A7-6-1112-defenses-and-objections-when-and-how-presented-pleading-or-motion-motion-judgment-pleadings | script grep | "(6) failure to state a claim upon which relief can be granted" |
| https://nebraskajudicial.gov/book/export/html/9131 | script | 64,852 chars; "former rule 12 is now Neb. Ct. R. Pldg. § 6-1112"; "§ 6-1115 amended September 3, 2025." |
| https://nebraskajudicial.gov/book/export/html/9131 | WF | YES; complete through § 6-1116; "Effective January 1, 2025." |
| https://nebraskajudicial.gov/supreme-court-rules | script (cache hrefs) | chapter-1 … chapter-6 links |
| …/chapter-2-appeals, …/article-1-nebraska-court-rules-appellate-practice | script (cache hrefs) | § 2-109 link; export node 8671 |
| …/%C2%A7-2-109-briefs-constitutional-questions | script grep | "§ 2-109. Briefs; constitutional questions. … (A) Time for Filing." |
| https://nebraskajudicial.gov/book/export/html/8671 | script | 136,868 chars; § 2-109 at offset 83,781 |
| …/chapter-3-attorneys-and-practice-law/article-5-nebraska-rules-professional-conduct | script (cache hrefs) | group pages §§ 3-501.1-3-501.18; export node 8800 |
| https://nebraskajudicial.gov/book/export/html/8800 | script grep | 367,510 chars; "§ 3-501.7. Conflict of interest; current clients. (a) Except as provided" |

## D — Administrative code / register
| URL | Tool | Result |
|---|---|---|
| WebSearch "Nebraska Administrative Code … sos.nebraska.gov" | WS | nebraska.gov/nesos/rules-and-regs/regtrack, agency pages, regulations.justia.com (not tier 2) |
| https://sos.nebraska.gov/rules-and-regs | script | HTTP 404 |
| https://sos.nebraska.gov/ | script (cache hrefs) | rules.nebraska.gov, /browse-rules, /docket; legacy regsearch link |
| https://rules.nebraska.gov/browse-rules | script | html 0 chars (JS shell) |
| https://rules.nebraska.gov/browse-rules | curl | 803-byte shell, /static/js/main.5fa7e335.js |
| https://rules.nebraska.gov/static/js/main.5fa7e335.js | curl | 3.07 MB bundle; routes /api/agency/filtered, /api/title/GetByAgencyId, /api/chapter/GetByTitleId, /api/ChapterImage/GetByChapterId |
| https://rules.nebraska.gov/api/agency/filtered | script | REFUSED HTTP 401 (not retried) |
| https://www.nebraska.gov/rules-and-regs/regsearch/Rules/index.cgi | script | redirects to rules.nebraska.gov/browse-rules, 0 chars |
| https://nebraska.gov/nesos/rules-and-regs/regtrack/index.cgi | script | redirects to rules.nebraska.gov/, 0 chars |
| https://www.nebraska.gov/nesos/rules-and-regs/regtrack/proposals/2469.pdf | script | redirects to rules.nebraska.gov/, 0 chars |
| https://sos.nebraska.gov/regulations/overview-regulation-process | script | redirects to rules.nebraska.gov/about, 0 chars |
| WebSearch "Title 471 Nebraska Administrative Code chapter pdf …" | WS | regulations.justia.com, agency pages only |
| https://rules.nebraska.gov/browse-rules | WF | PROVENANCE_REQUIRED |
| https://www.law.cornell.edu/regulations/nebraska (+ /attorney-general/title-53/chapter-2) | script links | § 53-2-002 -> 53-Neb-Admin-Code-ch-2-SS-002 |
| https://www.law.cornell.edu/regulations/nebraska/53-Neb-Admin-Code-ch-2-SS-002 | script | 3,194 chars; "002.01 Petition Any person may petition an agency"; Last-Modified Aug 3 2025 |
| https://www.law.cornell.edu/regulations/nebraska/471-Neb-Admin-Code-ch-23-SS-007 | script | "[REPEALED] … Repealed effective 12/26/2021" |
| https://www.law.cornell.edu/regulations/nebraska/53-Neb-Admin-Code-SS-2-001 | script | 200 but Nebraska index page (bad slug falls back) |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WebSearch "nebraskajudicial.gov opinions Supreme Court Court of Appeals released" | WS | /courts/supreme-court/opinions, /courts/court-appeals/opinions |
| https://nebraskajudicial.gov/courts/supreme-court/opinions | script | 32,569 chars; "October 16, 2026 … S-25-084 322 Neb. 578"; links to www.nebraska.gov viewOpinion |
| same | WF | read, but paired dockets with wrong titles (table scrambled) |
| https://www.nebraska.gov/apps-courts-epub/public/viewOpinion?docId=N00013369PUB | script | pdf 45 pages, 102,805 chars; "Cite as 321 Neb. 841"; "Filed July 24, 2026. No. S-25-209." |
| same | WF | PROVENANCE_REQUIRED |
| https://www.nebraska.gov/apps-courts-epub/public/viewOpinion?docId=N00013529PUB | WF | PROVENANCE_REQUIRED |
| https://www.nebraska.gov/apps-courts-epub/public/supreme | script | 592,618 chars; bound vols "Vol. 1 (1871) through Vol. 274 (2012)"; search JS POSTs /public/search |
| https://www.nebraska.gov/apps-courts-epub/public/search?searchText=S-25-209 | script (GET) | 200; "State v. Raymond Evans 07/24/2026 S-25-209 321 Neb. 841" |
| https://www.nebraska.gov/apps-courts-epub/public/search?searchText=321%20Neb.%20841 | script (GET) | same hit |
| https://www.nebraska.gov/apps-courts-epub/public/search?searchText=A-25-197 | script (GET) | "Martinez v. Amerigreen, LLC 06/30/2026 A-25-197 34 Neb. App. 347" |
| https://nebraskajudicial.gov/courts/court-appeals/opinions | script | "October 13, 2026 … A-25-855 State v. Spencer"; memorandum PDF links |
| https://www.nebraska.gov/apps-courts-epub/public/viewOpinion?docId=N00013358PUB | script | pdf 12 pages; "Cite as 34 Neb. App. 384"; "No. A-25-413" |
| https://nebraskajudicial.gov/sites/default/files/memorandums/a25-855m.pdf | script | pdf 4 pages; "MEMORANDUM OPINION AND JUDGMENT ON APPEAL (Memorandum Web Opinion)" |
| https://nebraskajudicial.gov/sites/default/files/memorandums/NonWeblist10-13-26.pdf | script | "Memorandum Opinions NOT Selected for Posting"; subscription SCCALES |
| https://law.justia.com/cases/nebraska/supreme-court/2026/ | WF | "Nebraska Supreme Court Decisions 2026"; /2026/s-24-829.html … |
| https://law.justia.com/cases/nebraska/supreme-court/2026/s-25-209.html | WF | YES "Raymond Evans was convicted by a jury of first degree"; '- 841 -' markers; truncated at 100K |
| https://law.justia.com/cases/nebraska/court-of-appeals/2026/a-25-197.html | WF | YES "Cite as 34 Neb. App. 347"; complete |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.nebraska.gov/apps-courts-epub/public/viewPFR?docId=N00013533PUB | script | pdf 2 pages; "A-25-197: Martinez v. Amerigreen … further review denied on October 9, 2026." |
| https://nebraskajudicial.gov/courts/appellate-courts-offices/daily-minutes | script | "Daily minutes … are retained on this page for sixty days."; /sites/default/files/content-files/10-13-26-Minutes.pdf |

## Build
- `python3 scripts/build.py --check`: exit 0, no ERROR/WARN.
- `python3 scripts/build.py --cross`: one line, `CROSS ne: 'Neb. Evid. R. 702' also matches oh / Ohio Rules of Evidence` — Ohio's bare `\bEvid\.\s?R\.` alternative claims the Nebraska form; fix belongs in oh.json (e.g. a negative lookbehind for "Neb. "). Example left unchanged per brief.

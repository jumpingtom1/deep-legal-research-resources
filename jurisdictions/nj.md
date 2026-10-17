# New Jersey (NJ) — free legal sources

_Generated from `data/nj.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the Legislature's Folio NXT database (lis.njleg.state.nj.us) serves per-section text at bare gateway.dll/statutes/1/{title}/{node} URLs; node ids are found through its XML table of contents, and an official weekday-refreshed bulk text file (pub.njleg.gov/statutes) covers the whole code; Justia 2025 is a constructible tier-2 fallback. Constitution: one 177K-char Legislature page (WebFetch stops in Art. VIII). Court rules and N.J.R.E.: njcourts.gov is behind an Imperva Incapsula challenge — blocked for the script, index pages fail in WebFetch; no free tier-2 copy. N.J.A.C. and N.J. Register are on a JavaScript-only LexisNexis site (not official); LII serves N.J.A.C. sections (possibly stale). Case law: njcourts.gov opinion PDFs are constructible from docket + decision year and readable by WebFetch only; Justia (Supreme 1900–, App. Div. published/unpublished 1944–, Tax 1980–) is the locator. Certification denials are not free online.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of New Jersey | `nj (unverified)` | N.J. | N.J., A.3d, A.2d, A. | — |
| Superior Court of New Jersey, Appellate Division | `njsuperctappdiv (unverified)` | N.J. Super. Ct. App. Div. | N.J. Super., A.3d, A.2d | — |
| Superior Court of New Jersey, Law Division | `njsuperctlawdiv (unverified)` | N.J. Super. Ct. Law Div. | N.J. Super., A.3d, A.2d | — |
| Superior Court of New Jersey, Chancery Division | `njsuperctchdiv (unverified)` | N.J. Super. Ct. Ch. Div. | N.J. Super., A.3d, A.2d | — |
| Tax Court of New Jersey | `njtaxct (unverified)` | N.J. Tax Ct. | N.J. Tax | — |
| New Jersey Court of Errors and Appeals (to 1948) | `nj (unverified)` | N.J. Err. & App. | N.J.L., N.J. Eq., A. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| New Jersey Statutes (N.J.S.A.) | `N.J.S.A. 2A:14-1`; `N.J. Stat. Ann. § 2A:14-1`; `N.J.S. 2C:11-3`; `N.J.S.2C:11-4`; `N.J.S.A. 2A:14-1.1`; `N.J. Rev. Stat. § 2C:11-3`; `NJ Rev Stat § 2A:14-1 (2025)`; `section 2A:14-1 of the New Jersey Statutes`; `P.L.1993, c.30 (C.45:22A-47)`; `N.J.S.A. 52:14B-7.1`; `R.S.39:4-50`; `N.J. Stat. § 39:4-50`; `N.J.S.A. 10:5-12(d)` | `nj-statutes-njleg` → `nj-statutes-bulk` → `nj-statutes-justia` |
| Pamphlet Laws (session laws) | `P.L.2021, c.379`; `P.L. 2017, c. 150`; `L. 1951 (1st SS), c. 344`; `L.1961, c. 121` | `nj-session-laws-njleg` |
| New Jersey Constitution | `N.J. Const. art. I, ¶ 1`; `N.J. Const. art. VI, § 2, ¶ 3`; `N.J. Const. art. VIII, § 4, ¶ 1`; `Article I, Paragraph 7 of the New Jersey Constitution`; `N.J. Const. art. I, para. 5` | `nj-constitution-njleg` → `nj-constitution-justia` |
| Rules Governing the Courts of the State of New Jersey | `R. 4:46-2`; `R. 4:46-2(c)`; `Rule 1:36-3`; `R. 2:2-3(a)(1)`; `N.J. Ct. R. 3:22-4`; `Rule 4:6-2(e) of the New Jersey Court Rules`; `R. 4:5B-2` | `nj-rules-of-court` |
| Rules Governing the Courts (bare "Rule 1:1" form, no subrule) *(only once this jurisdiction is known)* | `Rule 1:4`; `R. 2:10` | `nj-rules-of-court` |
| New Jersey Rules of Evidence | `N.J.R.E. 803(c)(6)`; `N.J.R.E. 702`; `New Jersey Rule of Evidence 404(b)` | `nj-rules-evidence` |
| New Jersey Administrative Code | `N.J.A.C. 7:7-1.1`; `N.J. Admin. Code § 6A:14-1.1`; `N.J.A.C. 10:122D-2.4`; `N.J.A.C. 1:1-1` | `nj-admincode-lii` → `nj-admincode-lexis` |
| New Jersey Register | `52 N.J.R. 1822(b)`; `47 N.J.R. 1392(a)` | `nj-register-lexis` |
| Certification history (certif. denied / granted) | `certif. denied, 250 N.J. 123 (2022)`; `certif. granted, 255 N.J. 487 (2023)`; `certif. denied, ___ N.J. ___ (2025)`; `certif. denied, 244 N.J. 336 (2020)` | `nj-subsequent-history-njcourts` |
| Reported New Jersey cases (N.J., N.J. Super., N.J. Tax, old N.J.L./N.J. Eq.) | `257 N.J. 247 (2024)`; `475 N.J. Super. 123 (App. Div. 2023)`; `33 N.J. Tax 1 (Tax 2022)`; `135 N.J. Eq. 1 (E. & A. 1944)`; `320 A.3d 1 (N.J. 2024)`; `290 A.3d 1 (N.J. Super. Ct. App. Div. 2023)` | `nj-cases-justia` → `nj-opinions-njcourts` |
| Docket-number citations (Supreme A-N-YY; Appellate Division A-NNNN-YY, incl. unpublished) | `State v. Gibson, No. A-0117-23 (App. Div. Dec. 19, 2025)`; `No. A-2551-24 (App. Div. Oct. 5, 2026) (slip op. at 4)`; `A-39-23`; `A-37/38-23`; `A-0921-24/A-1568-24`; `State v. Smith, No. A-4318-14T1 (App. Div. Mar. 3, 2017)` | `nj-cases-justia` → `nj-opinions-njcourts` → `nj-case-pages-njcourts` |
| Westlaw / Lexis unreported NJ cites | `2024 WL 123456 (N.J. Super. Ct. App. Div. Mar. 1, 2024)`; `2023 N.J. Super. Unpub. LEXIS 1234`; `2022 N.J. Tax LEXIS 5` | `nj-cases-justia` → `nj-opinions-njcourts` |

Regexes (case-insensitive):

- New Jersey Statutes (N.J.S.A.): `(?:N\.?\s*J\.?\s*S\.?\s*A\.?|N\.\s*J\.\s*S\.|N\.\s*J\.\s*Stat\.?(?:\s*Ann\.?)?|(?<![A-Za-z.])R\.\s*S\.|N\.?\s*J\.?\s*Rev\.?\s*Stat\.?|New\s+Jersey\s+Statutes(?:\s+Annotated)?)\s*(?:§+\s*)?(?P<title>\d{1,2}[A-Z]?):(?P<chapter>\d+[A-Z]*)-(?P<section>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)*)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2}[A-Z]?):(?P<chapter2>\d+[A-Z]*)-(?P<section2>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)*)\s+of\s+the\s+(?:New\s+Jersey\s+Statutes|N\.\s*J\.\s*S\.\s*A\.|Revised\s+Statutes)|\(C\.\s*(?P<title3>\d{1,2}[A-Z]?):(?P<chapter3>\d+[A-Z]*)-(?P<section3>\d+[A-Za-z]?(?:\.\d+[A-Za-z]?)*)\)`
- Pamphlet Laws (session laws): `(?:P\.\s*L\.|\bL\.)\s*(?P<year>(?:18|19|20)\d\d)(?:\s*\([^)]*\))?,?\s*c(?:h)?\.\s*(?P<chapter>\d+)`
- New Jersey Constitution: `N\.\s*J\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*(?:§\s*(?P<section>\d+|[IVXL]+),?\s*)?(?:¶|para\.?)\s*(?P<paragraph>\d+)|Article\s+(?P<article2>[IVXL]+),?\s+(?:Section\s+(?P<section2>[IVXL]+|\d+),?\s+)?Paragraph\s+(?P<paragraph2>\d+)\s+of\s+the\s+New\s+Jersey\s+Constitution`
- Rules Governing the Courts of the State of New Jersey: `N\.\s*J\.\s*Ct\.\s*R\.\s*(?P<part>[1-8]):(?P<rule>\d+[A-Z]?)(?:-(?P<sub>\d+[A-Z]?(?:\.\d+)?))?|(?<!Ct\.\s)(?<!Ct\.)(?:\bR\.|\bRules?)\s*(?P<part2>[1-8]):(?P<rule2>\d+[A-Z]?)-(?P<sub2>\d+[A-Z]?(?:\.\d+)?)`
- Rules Governing the Courts (bare "Rule 1:1" form, no subrule): `(?:\bR\.|\bRules?|N\.\s*J\.\s*Ct\.\s*R\.)\s*(?P<part>[1-8]):(?P<rule>\d+[A-Z]?)(?:-(?P<sub>\d+[A-Z]?(?:\.\d+)?))?`
- New Jersey Rules of Evidence: `(?:N\.\s*J\.\s*R\.\s*E\.|New\s+Jersey\s+Rules?\s+of\s+Evidence)\s*(?P<rule>\d{3})`
- New Jersey Administrative Code: `(?:N\.\s*J\.\s*A\.\s*C\.|N\.\s*J\.\s*Admin\.?\s*Code)\s*(?:§+\s*)?(?P<title>\d{1,2}[A-Z]?):(?P<chapter>\d+[A-Z]*)(?:-(?P<subchapter>\d+[A-Z]?)(?:\.(?P<section>\d+[A-Z]?))?)?`
- New Jersey Register: `(?P<volume>\d{1,2})\s+N\.\s*J\.\s*R\.\s+(?P<page>\d+)(?:\((?P<item>[a-z])\))?`
- Certification history (certif. denied / granted): `certif\.\s*(?P<disposition>denied|granted|dismissed),?\s*(?:(?P<volume>\d{1,3})|_+)\s+N\.\s*J\.\s+(?:(?P<page>\d{1,4})|_+)`
- Reported New Jersey cases (N.J., N.J. Super., N.J. Tax, old N.J.L./N.J. Eq.): `(?<!\d)(?<!denied, )(?<!granted, )(?<!dismissed, )(?<!denied,)(?<!granted,)(?P<volume>\d{1,3})\s+N\.\s*J\.(?:\s*(?:(?P<series>Super|Eq|L|Misc)\.|(?P<tax>Tax)))?\s+(?P<page>\d{1,4})|(?P<avolume>\d{1,4})\s+A\.(?:\s*[23]d)?\s+(?P<apage>\d{1,5})\s*(?:,\s*\d+)?\s*\((?P<court>N\.\s*J\.[^)]*?)\s*(?P<year>\d{4})\)`
- Docket-number citations (Supreme A-N-YY; Appellate Division A-NNNN-YY, incl. unpublished): `(?:No\.\s*)?\bA-(?P<seq>\d{1,4})(?:/(?:A-)?\d{1,4})*-(?P<yy>\d{2})(?:T(?P<team>\d))?\b`
- Westlaw / Lexis unreported NJ cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(N\.\s*J\.|N\.\s*J\.\s*(?:(?P<lexcourt>Super\.(?:\s*Unpub\.)?|Tax)\s*)?LEXIS\s+(?P<lexis>\d+))`

Short forms → URL key:

N.J.S.A. → `NJSA`; N.J.S. → `NJSA`; N.J. Stat. Ann. → `NJSA`; N.J. Rev. Stat. → `NJSA`; NJ Rev Stat → `NJSA`; C. → `NJSA`; N.J.A.C. → `NJAC`; N.J. Admin. Code → `NJAC`; R. → `NJ-CT-R`; N.J. Ct. R. → `NJ-CT-R`; Rule → `NJ-CT-R`; N.J.R.E. → `NJRE`; N.J.R. → `NJR`; P.L. → `PL`

NJ statute cites use the colon-hyphen form title:chapter-section (2A:14-1, 2C:11-3, 52:14B-7.1); route a bare 'title:chapter-section' here only with an N.J.S.A./N.J.S./N.J. Stat. Ann./NJ Rev Stat prefix, a '(C.x:y-z)' compiled-statute cite, or explicit New Jersey context — 'N.J.S.' (no A) denotes a Title 2A/2B/2C/3B/12A/14A-type revised section and is the same code. N.J.S.A. ranges are written '2A:14-1 to -2' or '§§ 2A:14-1 to -3': take the first section. Court rules are cited 'R. 4:46-2' (part:rule-subrule); the colon form is NJ-specific, but bare 'Rule 12' or 'R. 56' (no colon) must not route here. 'P.L.2021, c.379' is a NJ chapter law; federal 'Pub. L. 111-148' / 'P.L. 111-148' has no comma-year-chapter and is excluded by the regex. 'N.J.R.' (Register) vs 'N.J.R.E.' (Evidence) differ by the trailing E and the volume-before form. Supreme Court dockets 'A-39-23' (term number-year) and Appellate Division dockets 'A-0117-23' (4-digit, zero-padded) share one regex; the digit count tells them apart. Unpublished Appellate Division opinions (R. 1:36-3) are cited by docket and date or WL/LEXIS; resolve them through Justia's appellate-division-unpublished year listing. 'certif. denied' cites point to N.J. Reports tables (commercial); no free official equivalent. CourtListener ids are from memory and unverified; pre-1948 Court of Errors and Appeals id uncertain. Fixes after the independent check: pre-2017 Appellate Division dockets carry a team suffix (A-4318-14T1) and now match; 'R.S.39:4-50' (Revised Statutes form) and 'N.J. Stat. §' route to statutes — 'R.S.' is guarded by a lookbehind so 'M.R.S.' (Maine) and similar prefixed forms do not route here, and it still requires the colon-hyphen section form. 'certif. denied/granted, V N.J. P' routes to subsequent history: that pattern is listed before reported cases, and the reported-case regex refuses an N.J. cite immediately preceded by 'denied, ' / 'granted, ' / 'dismissed, '.

## A. Statutes / code

### `nj-session-laws-njleg` — Pamphlet Laws (P.L.) chapter texts — Legislature bill archive

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Legislature, Office of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** Enacted chapter laws by two-year session; HTM and PDF per chapter (verified for P.L.2017 and P.L.2021).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://pub.njleg.gov/bills/{session}/PL{yy}/{chapter}_.HTM`
  - Placeholders: From 'P.L.{year}, c.{chapter}': yy = last two digits of year; session = first year of the two-year session = year if even, year − 1 if odd (P.L.2017 → 2016; P.L.2021 → 2020). Chapters signed in January of an even year before the new session opens may still sit under the earlier session (P.L.2021, c.379 was approved January 18, 2022 and is under 2020/PL21 because the folder follows the P.L. year). chapter unpadded. Even-year rule verified: P.L.2022, c.40 → /bills/2022/PL22/40_.HTM. Replace .HTM with .PDF for the PDF.
  - Index: `https://pub.njleg.gov/bills/`
- **Automation:** WebFetch ok · shell ok · robots: 302 → njleg.state.nj.us/robots.txt: Allow: /
  - HTM text has CR/LF and non-breaking spaces between words: fetch_doc grep with a literal multi-word phrase can return 0 matches — use fetch_doc verify (whitespace-normalised) or grep --regex with \s+.
- **Currency:** none stated
- **Official status:** Chapter-law text and PDF posted by the Legislature; no official/unofficial statement on the page.
- **Hazard:** NBSP/CRLF between words defeats literal grep — use verify or \s+ regex
- **Probe:** P.L.2017, c.150 → `https://pub.njleg.gov/bills/2016/PL17/150_.HTM` — expect: "An Act concerning certain murders and amending N.J.S.2C:11-3"
- **Evidence (2026-10-16):** WebFetch: 'An Act concerning certain murders and amending N.J.S.2C:11-3', 'Approved July 21, 2017.', complete. Second citation P.L.2021, c.379 at /bills/2020/PL21/379_.HTM: fetch_doc 'CHAPTER 379 An Act concerning construction defects', 'Approved January 18, 2022.' | Independent check 2026-10-16: WebFetch YES 'An Act concerning certain murders and amending N.J.S.2C:11-3'; 'Approved July 21, 2017.'; second citation P.L.2022, c.40 ok
- **Notes:** Statute section history notes cite chapter laws in this form (e.g. 'amended 2021, c.379').

### `nj-statutes-bulk` — New Jersey Statutes — official bulk text download (STATUTES-TEXT.zip)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Legislature, Office of Legislative Services · text: **link-only** · official: unknown
- **Coverage:** Entire unannotated statutes in one plain-text file (STATUTES.TXT, 84 MB) and RTF; also Folio infobase; Constitution (NJCONST-TEXT.zip) and Legislative Counsel TOC (LCTOC).
- **Access:** `index-anchored` · format zip (txt, rtf)
  - Pattern: `https://pub.njleg.gov/statutes/STATUTES-TEXT.zip`
  - Placeholders: Fixed file names in the directory listing. Inside STATUTES.TXT each section starts on a line beginning with the section number, e.g. '2A:14-1.  6 years' or '2C:11-3  Murder.' (period after the number is inconsistent).
  - Index: `https://pub.njleg.gov/statutes/`
  - Navigation: directory listing → STATUTES-TEXT.zip → STATUTES.TXT; search for a line starting with the section number.
- **Automation:** WebFetch fail · shell http-error · robots: pub.njleg.gov/robots.txt 302 → njleg.state.nj.us/robots.txt: Allow: /
  - binary zip; ingest only. fetch_doc.py does not unzip (it reads the 41 MB zip as html garbage) and WebFetch returns a client error; the directory listing and _READ_ME.txt are readable. Use as a maintainer corpus/ingest input, not a live read route.
- **Currency:** line 2 of STATUTES.TXT — observed: "(UPDATED THROUGH  P.L.2026, c.50, and J.R.1)"
- **Official status:** Same Legislature text as nj-statutes-njleg; _READ_ME.txt describes formats only, no official-status statement.
- **Hazard:** binary zip — not readable by fetch_doc.py or WebFetch; ingest only
- **Hazard:** very large file
- **Hazard:** section heading format varies (with/without trailing period)
- **Probe:** N.J.S.A. 2A:14-1 → `https://pub.njleg.gov/statutes/STATUTES-TEXT.zip` — expect: "2A:14-1.  6 years"
- **Evidence (2026-10-16):** Shell: 200 application/x-zip-compressed, 41,443,870 B, last-modified 16 Oct 2026; STATUTES.TXT line 3694 '2A:14-1.  6 years', line 3703 '2A:14-1.1.'; header 'UPDATED THROUGH  P.L.2026, c.50, and J.R.1'. fetch_doc read the directory listing and _READ_ME.txt. | Independent check 2026-10-16: WebFetch CLIENT_ERROR on zip; fetch_doc reads raw ZIP bytes, grep 'UPDATED THROUGH' 0 matches — live route unusable, kept as ingest input; second citation N.J.S.A. 10:5-12 failed via live routes
- **Notes:** Best bulk statute source in the pilot so far: a script can index every section from one file daily.

### `nj-statutes-njleg` — New Jersey Statutes (Unannotated) — Legislature's Folio NXT statutes database

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Legislature, Office of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** All titles of the Revised Statutes / N.J.S.A. as currently in force (Title 1 through Title 59 and Appendix A), one document per section.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1/{title_node}/{section_node}`
  - Placeholders: Node ids are sequential integers assigned when the Folio infobase is rebuilt (it is rebuilt every weekday), so they are NOT derivable from the citation and may shift; never store or guess them. Resolve per request: (1) GET https://lis.njleg.state.nj.us/nxt/gateway.dll?f=xmlcontents&command=getchildren&basepathid=statutes%2F1&maxnodes=500&minnodesleft=5 → XML <n id='statutes/1/NNN' t='TITLE 2A  ADMINISTRATION OF …'> (title names only, no section ranges); (2) GET the same URL with basepathid=statutes%2F1%2F{title_node}&maxnodes=5000 → flat list of every section in the title (no chapter level), each <n ct='text/xml' id='statutes/1/{title}/{node}' t='2A:14-1.  6 years'>; match the t attribute with the regex ^{title}:{chapter}-{section}\.?\s — the section number, an optional period, then whitespace — so 10:5-12 matches '10:5-12.  …' but NOT '10:5-12.1  …' (a looser 'followed by a period' rule returned 13 hits for 10:5-12); (3) GET https://lis.njleg.state.nj.us/nxt/gateway.dll/{id} (bare path, no query) for the section text. Verified: N.J.S.A. 2A:14-1 → statutes/1/112/303; N.J.S.A. 2C:11-3 → statutes/1/2785/2868 (2026-10-16). Third verified: N.J.S.A. 10:5-12 → Title 10 = statutes/1/7555, section node statutes/1/7555/7610.
  - Index: `https://lis.njleg.state.nj.us/nxt/gateway.dll?f=xmlcontents&command=getchildren&basepathid=statutes%2F1&maxnodes=500&minnodesleft=5`
  - Navigation: Use WebFetch for the xmlcontents steps: fetch_doc.py strips XML tags and attributes (it returns only 'getchildrenstatutes/1'), so ids and section titles are invisible to the script. xmlcontents root (title folders, e.g. statutes/1/112 = TITLE 2A, statutes/1/2785 = TITLE 2C, statutes/1/7555 = TITLE 10) → xmlcontents of the title folder (every section listed with its number in the t attribute) → document URL gateway.dll/{id} (readable by WebFetch or fetch_doc). The HTML front end (gateway.dll?f=templates&fn=default.htm&vid=Publish:10.1048/Enu) is a JavaScript search app — do not use it.
- **Automation:** WebFetch ok · shell ok · robots: lis.njleg.state.nj.us/robots.txt 302 → njleg.state.nj.us/robots.txt: User-agent * Allow: /
  - Use the bare document path: WebFetch of the same document with '?f=templates$fn=document-frameset.htm' returned a client error. TOC lookup needs WebFetch (fetch_doc strips XML attributes); WebFetch truncates large title lists (Title 2C cut at 2C:40A-4) — use a smaller maxnodes and command=getmore&start={last name}&direction=… or offset. A non-folder basepathid returns HTTP 500 'xmlcontents did not succeed'. Section documents themselves read fine with fetch_doc.
- **Currency:** none on section pages or in the xmlcontents output seen by the independent check; the bulk STATUTES.TXT header (pub.njleg.gov) carries an 'UPDATED THROUGH' line
- **Official status:** Legislature disclaimer (https://www.njleg.state.nj.us/disclaimer, read by WebFetch) says the statute and Constitution text are not annotated; it makes no official/unofficial statement. The TOC root is titled 'New Jersey Statutes (Unannotated)'. The annotated N.J.S.A. is a commercial publication. No UELMA authentication statement found.
- **Hazard:** node ids not derivable from citations and may shift on the weekday rebuild — resolve through xmlcontents each time
- **Hazard:** JavaScript front end (gateway.dll default.htm) shows only a search shell
- **Hazard:** no currency line on section pages
- **Hazard:** section-number matching must stop at whitespace: ^{t}:{c}-{s}\.?\s (10:5-12 vs 10:5-12.1 vs 2C:11-3a)
- **Hazard:** fetch_doc.py cannot see the xmlcontents ids/titles (attributes stripped) — TOC navigation is WebFetch-only
- **Probe:** N.J.S.A. 2C:11-3 → `https://lis.njleg.state.nj.us/nxt/gateway.dll/statutes/1/2785/2868` — expect: "Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder"
- **Evidence (2026-10-16):** WebFetch: 2C:11-3 body present ('a. Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder'), complete through subsection j. fetch_doc verify OK (8,165 chars). Second citation N.J.S.A. 2A:14-1 at /statutes/1/112/303: fetch_doc read 'Every action at law for trespass to real property', ends 'amended 2021, c.379.' | Independent check 2026-10-16: WebFetch YES 'Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder when'; complete; second citation N.J.S.A. 10:5-12 ok
- **Notes:** Node ids recorded here are evidence only, valid on 2026-10-16.

### `nj-statutes-justia` — Justia — New Jersey Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** N.J.S.A. by title and section; editions by year, unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/new-jersey/title-{title_lower}/section-{title_lower}-{chapter_lower}-{section}/`
  - Placeholders: title lower-cased (2A → 2a, 2C → 2c); section slug = title-chapter-section joined by hyphens, all lower-case (2A:14-1 → section-2a-14-1). No chapter segment in the path. Decimal sections: '.' → '-' (10:5-12.1 → /title-10/section-10-5-12-1/, verified). Year-specific: insert /{year}/ after /new-jersey/.
  - Index: `https://law.justia.com/codes/new-jersey/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a Cloudflare challenge
  - fetch_doc.py REFUSED (bot challenge). WebFetch only.
- **Currency:** page header and Universal Citation line — observed: "2025 New Jersey Revised Statutes; NJ Rev Stat § 2A:14-1 (2025)"
- **Official status:** Third-party compilation; page labels the edition '2025 New Jersey Revised Statutes'.
- **Hazard:** edition lags official text
- **Hazard:** shell blocked by Cloudflare
- **Probe:** N.J.S.A. 2A:14-1 → `https://law.justia.com/codes/new-jersey/title-2a/section-2a-14-1/` — expect: "Every action at law for trespass to real property, for"
- **Evidence (2026-10-16):** WebFetch: body present, '2025 New Jersey Revised Statutes', 'NJ Rev Stat § 2A:14-1 (2025)'. Second citation 2C:11-3 at /title-2c/section-2c-11-3/: 'a. Except as provided in N.J.S.2C:11-4, criminal homicide constitutes murder'. | Independent check 2026-10-16: YES '2A:14-1. a. Every action at law for trespass to real property'; 'NJ Rev Stat § 2A:14-1 (2025)'; second citation N.J.S.A. 10:5-12.1 ok

## B. Constitution

### `nj-constitution-njleg` — New Jersey State Constitution 1947 (Legislature)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Legislature, Office of Legislative Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** 1947 Constitution as amended, whole document on one page, with amendment notes after each article.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.njleg.state.nj.us/constitution`
  - Placeholders: Single page for the whole Constitution; no per-article anchors. Locate 'Article {roman}' then 'Section {roman}' then the paragraph number. Bulk alternative: https://pub.njleg.gov/statutes/NJCONST-TEXT.zip (NJCONST.TXT).
  - Index: `https://www.njleg.state.nj.us/constitution`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: Allow: /
  - WebFetch window 1 (0–100,000 of 141,147 chars) ends in Art. VIII § I; later provisions (e.g. Art. VIII § IV ¶ 1, Art. IX, Art. XI) need offset=100000 or fetch_doc.py, which reads the whole 177,072-char page.
- **Currency:** heading at top of page — observed: "(Updated Through Amendments Adopted in November, 2021)"
- **Official status:** Legislature disclaimer says the Constitution text is not annotated; no official-status statement.
- **Hazard:** WebFetch truncation after Art. VIII § I
- **Hazard:** no anchors
- **Hazard:** currency string may lag recent amendments
- **Probe:** N.J. Const. art. I, ¶ 1 → `https://www.njleg.state.nj.us/constitution` — expect: "All persons are by nature free and independent, and have"
- **Evidence (2026-10-16):** WebFetch: Art. I ¶ 1 YES; Art. VIII § IV ¶ 1 NOT PRESENT (truncated). fetch_doc: verify OK at offset 1,779; second citation Art. VI § I ¶ 1 'The judicial power shall be vested in a Supreme Court' at offset 78,747; Art. VIII § IV ¶ 1 at 146,127. | Independent check 2026-10-16: YES Art. I para 1; '(Updated Through Amendments Adopted in November, 2021)'; WebFetch truncated in Art. VIII § I; Art. IX para 1 at offset 148,621; second citation N.J. Const. art. IX, para. 1 ok

### `nj-constitution-justia` — Justia — New Jersey Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/new-jersey/`
  - Placeholders: single page, no article links
  - Index: `https://law.justia.com/constitution/new-jersey/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - 137,263 chars; WebFetch window 1 ends in Art. VIII § II; use offset=100000.
- **Currency:** none stated
- **Official status:** Third-party compilation; no currency statement.
- **Hazard:** WebFetch truncation
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Probe:** N.J. Const. art. I, ¶ 1 → `https://law.justia.com/constitution/new-jersey/` — expect: "All persons are by nature free and independent, and have"
- **Evidence (2026-10-16):** WebFetch: Art. I ¶ 1 body present; single page; truncated in Art. VIII § II; no currency statement. | Independent check 2026-10-16: YES Art. I para 1; no currency statement; window 1 ends at start of Art. VIII § II; second citation N.J. Const. art. IX, para. 1 (offset=100000) ok

## C. Court rules

### `nj-rules-evidence` — New Jersey Rules of Evidence (N.J.R.E.) — njcourts.gov

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · New Jersey Judiciary · text: **link-only** · official: unknown
- **Coverage:** N.J.R.E. 101–1103, adopted under the Evidence Act (N.J.S.A. 2A:84A).
- **Access:** `index-anchored` · format pdf
  - Placeholders: URL not established.
  - Index: `https://www.njcourts.gov/attorneys/rules-of-court`
  - Navigation: rules-of-court index → Rules of Evidence (reported, not observed)
- **Automation:** WebFetch fail · shell blocked-challenge · robots: see nj-rules-of-court
- **Currency:** not observed
- **Official status:** Not read (host blocked).
- **Hazard:** host blocked
- **Probe:** N.J.R.E. 803(c)(6) → `https://www.njcourts.gov/attorneys/rules-of-court`
- **Evidence (2026-10-16):** Same index as nj-rules-of-court: script 403 Incapsula, WebFetch client error. | Re-confirmed blocked 2026-10-16: WebFetch CLIENT_ERROR 'There was an error while fetching.'; fetch_doc REFUSED (403 Incapsula)

### `nj-rules-of-court` — Rules Governing the Courts of the State of New Jersey (Parts I–VIII, appendices) — njcourts.gov

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · New Jersey Judiciary (Supreme Court of New Jersey) · text: **link-only** · official: unknown
- **Coverage:** Part I (all courts), II (appellate), III (criminal), IV (civil), V (family), VI (tenancy), VII (municipal), VIII (tax); appendices incl. RPC; cited 'R. 4:46-2'.
- **Access:** `index-anchored` · format pdf
  - Placeholders: Per-part / per-rule PDF URLs not established; a guessed /sites/default/files/rules/r4-46.pdf failed. Do not guess.
  - Index: `https://www.njcourts.gov/attorneys/rules-of-court`
  - Navigation: rules-of-court index → part or rule link (not observed)
- **Automation:** WebFetch fail · shell blocked-challenge · robots: njcourts.gov robots.txt allows /attorneys/ and /system/files/ (disallows /search, /admin/, /user/…); the host itself answers the script with an Incapsula challenge (HTTP 403)
  - WebFetch CLIENT_ERROR on /attorneys/rules-of-court, ?page=0, and /attorneys/rules-court. Opinion PDFs on the same host DO work in WebFetch, so rule PDFs may too once their URLs are known.
- **Currency:** not observed
- **Official status:** Not read: every rules page on njcourts.gov errored or was refused (Imperva Incapsula).
- **Hazard:** Incapsula bot challenge on the shell
- **Hazard:** WebFetch errors on index pages
- **Hazard:** rule PDF URLs unknown
- **Probe:** R. 4:46-2 → `https://www.njcourts.gov/attorneys/rules-of-court`
- **Evidence (2026-10-16):** fetch_doc: 'REFUSED: www.njcourts.gov refused automated access: HTTP 403'; headers show Incapsula (x-iinfo, visid_incap cookie, /_Incapsula_Resource). WebFetch: 'There was an error while fetching.' on three index URLs. | Re-confirmed blocked 2026-10-16: WebFetch CLIENT_ERROR 'There was an error while fetching.'; fetch_doc REFUSED (403 Incapsula)
- **Notes:** No tier-2 host serves the NJ court rules (Justia, LII and public.law do not); other sites found by search are unvetted third parties.

## D. Administrative code

### `nj-admincode-lexis` — New Jersey Administrative Code — free public access (LexisNexis)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · LexisNexis under contract with the Office of Administrative Law · text: **link-only** · official: unofficial
- **Coverage:** Semi-monthly updated N.J.A.C. (per OAL).
- **Access:** `link-only` · format html
  - Index: `https://www.lexisnexis.com/hottopics/njcode/`
  - Navigation: 302 redirect to advance.lexis.com/container?config=… — a JavaScript application; no per-section URL usable by tools.
- **Automation:** WebFetch fail · shell http-error · robots: not determined
  - fetch_doc follows the 302 and gets HTTP 200 with 0 characters of text (JavaScript shell); WebFetch reports the redirect, then an empty page.
- **Currency:** not observable
- **Official status:** OAL page https://www.nj.gov/oal/rules/accessp: 'Please note that the online version of the Code is not the official Code.'
- **Hazard:** JavaScript-only application
- **Hazard:** not the official Code
- **Probe:** N.J.A.C. 7:7-1.1 → `https://advance.lexis.com/container?config=00JAA5OTY5MTdjZi1lMzYxLTQxNTEtOWFkNi0xMmU5ZTViODQ2M2MKAFBvZENhdGFsb2coFSYEAfv22IKqMT9DIHrf`
- **Evidence (2026-10-16):** WebFetch: empty page; fetch_doc: 200, 0 chars. Linked from nj.gov/oal as the public-access Code. | Independent check 2026-10-16: confirmed index 302 → advance.lexis.com container; page empty
- **Notes:** Link users here for the current Code; quote from nj-admincode-lii only with its currency caveat.

### `nj-admincode-lii` — Cornell LII — New Jersey Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** N.J.A.C. per section with history notes; pages last modified August 2025 (latest N.J.R. note seen 2020 on 6A:14-1.1).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-{title}-{chapter}-{subchapter}-{section}`
  - Placeholders: N.J.A.C. {title}:{chapter}-{subchapter}.{section} → replace ':' '-' '.' with hyphens, keep letter suffixes upper-case as cited (7:7-1.1 → N-J-A-C-7-7-1-1; 6A:14-1.1 → N-J-A-C-6A-14-1-1).
  - Index: `https://www.law.cornell.edu/regulations/new-jersey`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 10; disallows /search/ and admin paths (per DE log); /regulations/ allowed
  - A literal fetch_doc grep of a multi-word phrase can miss because of whitespace; fetch_doc verify passes.
- **Currency:** bottom of section page — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party compilation; 'State regulations are updated quarterly'.
- **Hazard:** possibly stale (Last-Modified Aug 2025)
- **Hazard:** no as-of date for the text
- **Probe:** N.J.A.C. 6A:14-1.1 → `https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-6A-14-1-1` — expect: "(a) The rules in this chapter supersede all rules in"
- **Evidence (2026-10-16):** WebFetch: body present, complete; note 'Amended by 52 N.J.R. 1822(b), effective 10/5/2020'. Second citation N.J.A.C. 7:7-1.1: fetch_doc verify 'This chapter establishes the rules of the Department' OK. | Independent check 2026-10-16: YES '(a) The rules in this chapter supersede all rules in effect'; 'updated quarterly'; 52 N.J.R. 1822(b); second citation N.J.A.C. 5:23-2.1 ok

## D. Administrative register

### `nj-register-lexis` — New Jersey Register — free public access (LexisNexis)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · LexisNexis under contract with the Office of Administrative Law · text: **link-only** · official: unknown
- **Coverage:** N.J.R. July 3, 1995 – current.
- **Access:** `link-only` · format html
  - Index: `https://www.lexisnexis.com/hottopics/njoal/`
  - Navigation: 302 redirect to advance.lexis.com JavaScript application.
- **Automation:** WebFetch fail · shell http-error · robots: not determined
  - fetch_doc: redirect to advance.lexis.com/container?config=00JABk…, 200 with 0 chars.
- **Currency:** not observable
- **Official status:** OAL accessp page: free online access to the Register from the current issue back to July 3, 1995; earlier issues (from Sept. 25, 1969) via the New Jersey State Library.
- **Hazard:** JavaScript-only application
- **Probe:** 52 N.J.R. 1822(b) → `https://www.lexisnexis.com/hottopics/njoal/`
- **Evidence (2026-10-16):** fetch_doc: 0 chars after redirect. OAL rulemaking portal (nj.gov/oal/rules/portal/) lists active proposals at oalrulesproduction.dynamics365portals.us (not probed). | Independent check 2026-10-16: WebFetch 302 → advance.lexis.com/container?config=00JABk… (JS app)
- **Notes:** OAL also posts rulemaking notices at https://www.nj.gov/oal/rules/proposals/ (script 200, not examined).

## E. Case law

### `nj-case-pages-njcourts` — New Jersey Courts — case pages (/cases/{docket})

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Judiciary · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court cases (grant, argument, decision dates, question presented) and some Appellate Division argued cases; briefs posted under /system/files/cases/briefs/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.njcourts.gov/cases/{docket_lower}`
  - Placeholders: docket lower-case, as cited with hyphens: A-39-23 → a-39-23; A-1489-22 → a-1489-22.
  - Index: `https://www.njcourts.gov/attorneys/opinions/supreme`
- **Automation:** WebFetch ok (partial) · shell blocked-challenge · robots: /cases/ not disallowed
  - WebFetch returns the page text below a 'Sorry, you need to enable JavaScript' notice; no document links come through.
- **Currency:** none stated
- **Official status:** Court-posted case summaries (argued/decided dates, questions presented).
- **Hazard:** JS notice; links missing
- **Hazard:** Decided date may be missing or lag (State v. Myers, A-4-25: no Decided date though Justia lists Aug. 17, 2026)
- **Hazard:** shell blocked
- **Probe:** Rodriguez v. Shelbourne Spring, LLC, A-39-23 → `https://www.njcourts.gov/cases/a-39-23` — expect: "Leave to Appeal Granted"
- **Evidence (2026-10-16):** WebFetch: 'Leave to Appeal Granted: May 10, 2024', 'Argued: Sept. 9, 2024', 'Decided: Dec. 12, 2024'. Second: /cases/a-1489-22 State v. A.H.-S., 'Argued: Oct. 16, 2024'. | Independent check 2026-10-16: 'Leave to Appeal Granted: May 10, 2024', 'Argued: Sept. 9, 2024', 'Decided: Dec. 12, 2024'; JS notice; second citation State v. Myers, A-4-25 ok
- **Notes:** Use as a pointer only; quote opinions from the PDF or Justia. Certification-granted pages name the Appellate Division docket ('Appellate Opinion A-2045-22' on A-4-25).

### `nj-opinions-njcourts` — New Jersey Courts — opinion PDFs (Supreme Court, Appellate Division, Tax Court, trial courts)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Appellate Division opinions confirmed for 2024–2026; earliest year not determined (listing pages unreadable). Appellate Division unpublished opinions, Tax Court and published trial-court opinions are reportedly posted in the same tree but were not confirmed.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Do NOT construct opinion PDF URLs. Observed filenames (evidence only): Supreme /2024/a_39_23.pdf, /2024/a_66_21.pdf; Appellate Division /2025/a0117-23.pdf, /2026/a0891-24.pdf. URLs built from these forms failed for 8 other opinions (a_18_24, a0921-24, a2551-24 at research; a_4_25, a-4-25, a3222-24, a1103-24, a_8_25 at the independent check) and failures cannot be told from host errors. Read an njcourts PDF only from a URL actually found on a page (e.g. a link surfaced by a search result or listing); otherwise read the Justia text.
  - Index: `https://law.justia.com/cases/new-jersey/`
  - Navigation: Locate the opinion on Justia (court → year listing → docket) or another listing; read the official PDF only if its exact njcourts URL was found; njcourts listing pages /attorneys/opinions/{supreme|published-appellate|…} are JavaScript/Incapsula-protected (WebFetch errors or returns dockets and dates without links).
- **Automation:** WebFetch ok (found PDF URLs only) · shell blocked-challenge · robots: Disallow /search (site search off-limits); /attorneys/ and /system/files/ allowed
  - Shell: Imperva Incapsula challenge (HTTP 403) — fetch_doc refuses the host for the day. WebFetch reads PDFs (converted to text) but fails on most HTML pages. Long opinions exceed the 100K window (Zingis 109,924 chars) — use offset=100000.
- **Currency:** none stated
- **Official status:** Slip opinions; Supreme Court PDFs open 'This syllabus is not part of the Court's opinion'; the official reports are N.J., N.J. Super. and N.J. Tax (commercial).
- **Hazard:** pattern not constructible: 8 URLs built from observed filename forms failed (research 3, independent check 5) while the recorded files load
- **Hazard:** slip pagination only — no N.J. / N.J. Super. page numbers
- **Hazard:** filename form varies (a_39_23 vs a-15-23); consolidated and unpublished forms unknown
- **Hazard:** shell blocked by Incapsula; WebFetch intermittent on HTML pages
- **Hazard:** the Appellate Division PDF may be the full unredacted slip opinion while the published version omits parts (Gibson: Justia text 'APPROVED FOR PUBLICATION AS REDACTED'; njcourts PDF carries the not-for-publication legend)
- **Hazard:** WebFetch truncation on long opinions
- **Probe:** Rodriguez v. Shelbourne Spring, LLC, A-39-23 (N.J. Dec. 12, 2024) → `https://www.njcourts.gov/system/files/court-opinions/2024/a_39_23.pdf` — expect: "SYLLABUS This syllabus is not part of the Court's opinion"
- **Evidence (2026-10-16):** WebFetch: Rodriguez (A-39-23, 089044) syllabus and opinion text present. Second Supreme: /2024/a_66_21.pdf State v. Zingis, decided August 8, 2024. Appellate: /2025/a0117-23.pdf 'After a jury trial, defendant Anthony Gibson, a police officer, was found'; /2026/a0891-24.pdf 'APPROVED FOR PUBLICATION' January 12, 2026. Failures: a_18_24, a0921-24, a2551-24 (client error). | Independent check 2026-10-16: probe YES (Rodriguez syllabus 'This syllabus is not part of the Court's opinion'); /2026/a0891-24.pdf re-confirmed; 5 freshly constructed URLs failed — row verified only for reading a found URL
- **Notes:** Public-domain citation: none. Unpublished Appellate Division opinions are cited by docket and date; R. 1:36-3 restricts citing them.

### `nj-cases-justia` — Justia — New Jersey case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1900–2026; Appellate Division 1944–2026 (published and unpublished collections); Tax Court 1980–2026; Court of Errors and Appeals; Advisory Committee on Professional Ethics.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/new-jersey/{court}/{decision_year}/{docket_slug}.html`
  - Placeholders: court = supreme-court | appellate-division-published | appellate-division-unpublished | tax-court (the umbrella appellate-division/ path lists years). docket_slug = docket lower-cased with '/' → '-' (A-39-23 → a-39-23; A-37/38-23 → a-37-38-23; A-0117-23 → a-0117-23; consolidated App. Div. uses the first docket, A-0921-24/A-1568-24 → a-0921-24). Tax Court slug = docket like 001081-2024. decision_year = year decided. If unsure, open the year listing /cases/new-jersey/{court}/{year}/ which lists names, dates, dockets and URLs.
  - Index: `https://law.justia.com/cases/new-jersey/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - PDF copies at cases.justia.com/new-jersey/{court}/{year}-{docket_slug}.pdf?ts=… (seen, not fetched).
- **Currency:** none stated
- **Official status:** Pages warn opinions 'may not be the official published versions'; some metadata/summaries AI-assisted.
- **Hazard:** slip pagination only
- **Hazard:** published App. Div. text may be the redacted version
- **Hazard:** AI-assisted metadata
- **Hazard:** shell blocked
- **Hazard:** the appellate-division-published/{year}/ listing also includes unpublished entries — take publication status from the URL segment and the opinion legend, not the listing
- **Probe:** Rodriguez v. Shelbourne Spring, LLC, A-39-23 (N.J. 2024) → `https://law.justia.com/cases/new-jersey/supreme-court/2024/a-39-23.html` — expect: "In this appeal, we consider whether the Hartford Underwriters Insurance Company (Hartford)"
- **Evidence (2026-10-16):** WebFetch: full opinion, slip pagination, not truncated. Also /appellate-division-published/2025/a-0117-23.html ('APPROVED FOR PUBLICATION AS REDACTED') and /appellate-division-unpublished/2026/a-2551-24.html ('PER CURIAM S.J.M. appeals from a March 21, 2025 order of the'). | Independent check 2026-10-16: YES 'In this appeal, we consider whether the Hartford Underwriters Insurance'; complete, slip pagination; second citation State v. Myers, A-4-25 (2026); Carbone, A-3222-24 (App. Div. 2026); State v. Mwangi, A-2889-24 (unpub.) ok
- **Notes:** Practical first stop for locating NJ opinions by year/name, because the njcourts listings are unreadable.

## F. Subsequent history

### `nj-subsequent-history-njcourts` — New Jersey Supreme Court — certification / leave-to-appeal grants on case pages and in opinions

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New Jersey Judiciary · text: **link-only** · official: unofficial
- **Coverage:** Grants only: Supreme Court case pages show 'Certification Granted' / 'Leave to Appeal Granted' dates, argument and decision dates; the opinion names the court below. Certification DENIALS are not posted as individual items (found only as tables in the N.J. Reports, commercial).
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format html
  - Pattern: `https://www.njcourts.gov/cases/{supreme_docket_lower}`
  - Placeholders: Only the Supreme Court's own A-{n}-{yy} docket opens the case page; the Appellate Division docket does not lead to it. To find review of an Appellate Division decision, search Justia's supreme-court year listings (and later years) by party name, then confirm the court below in the opinion caption ('On certification to the Superior Court, Appellate Division'); certification-granted case pages also name the Appellate Division docket.
  - Index: `https://law.justia.com/cases/new-jersey/supreme-court/`
  - Navigation: party name → Justia Supreme Court year listing → Supreme docket → njcourts /cases/{docket} for grant date, and the opinion PDF for the disposition
- **Automation:** WebFetch ok (partial) · shell blocked-challenge · robots: see nj-opinions-njcourts
- **Currency:** none stated
- **Official status:** Court-posted case pages and slip opinions.
- **Hazard:** party-name search only
- **Hazard:** denials of certification not findable free
- **Hazard:** njcourts HTML partially readable
- **Hazard:** case page may lack the Decided date (A-4-25)
- **Probe:** Rodriguez v. Shelbourne Spring, LLC, A-39-23 → `https://www.njcourts.gov/cases/a-39-23` — expect: "Leave to Appeal Granted: May 10, 2024"
- **Evidence (2026-10-16):** WebFetch: grant, argument and decision dates present; court below not listed on the page. | Independent check 2026-10-16: 'Leave to Appeal Granted: May 10, 2024'; argued/decided dates; second citation State v. Myers, A-4-25 (cert. from App. Div. A-2045-22) ok
- **Notes:** 'certif. denied, 250 N.J. 123 (2022)' points to an N.J. Reports page (commercial); no free official equivalent was found.

## Not available (do not look for these again)

- **statutes** — Cornell LII and public.law editions of the N.J. Statutes / Constitution: public.law lists only CA, CO, FL, NV, NY, OR, TX (DE pilot check, same day); LII hosts NJ regulations only. (2026-10-16)
- **court_rules** — Tier-2 copy of the NJ Rules of Court or N.J.R.E.: Justia, LII and public.law do not host them; search results were unvetted third-party sites only. (2026-10-16)
- **admin_code** — Official, tool-readable N.J.A.C. text: OAL: online Code 'is not the official Code'; the Lexis public-access site is a JavaScript app returning 0 characters. (2026-10-16)
- **case_law** — Free official reporter pagination (N.J., N.J. Super., N.J. Tax): njcourts and Justia texts carry slip pagination only. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: None in use; citations are to N.J./N.J. Super./A.3d or by docket number and date. (2026-10-16)
- **case_law** — Rutgers Law Library NJ opinion archive as a permitted source: Third party, not tier 1 or the vetted tier-2 list; not probed. (2026-10-16)
- **subsequent_history** — Free official list of certification denials: No njcourts list found by three searches; denials are tabulated in the commercial N.J. Reports. (2026-10-16)

## Corpus candidates (maintainers)

- `nj-constitution-njleg` — 177K-char single page; WebFetch stops in Art. VIII § I (Art. VIII § IV, IX, X, XI unreachable without offset). · bulk: https://pub.njleg.gov/statutes/NJCONST-TEXT.zip
- `nj-statutes-bulk` — Whole N.J.S.A. in one official 84 MB text file refreshed every weekday; ideal for a section-level corpus. · bulk: https://pub.njleg.gov/statutes/STATUTES-TEXT.zip

## Open questions

- Official URLs of the Rules of Court part/rule PDFs and N.J.R.E. on njcourts.gov (index pages unreadable; Incapsula).
- njcourts opinion PDF filenames for consolidated dockets, unpublished App. Div. opinions (a2551-24 failed), Tax Court and trial-court opinions; whether Supreme files use a_N_YY or a-N-YY consistently.
- Earliest year of opinions on njcourts.gov.
- Whether NXT node ids stay stable between weekday rebuilds.
- CourtListener ids (nj, njsuperctappdiv, njsuperctlawdiv, njsuperctchdiv, njtaxct) unverified.
- Whether the Legislature's statutes/Constitution are official (no statement found; UELMA status unknown).
- Whether any njcourts opinion PDF filename rule exists beyond the four observed files (5 fresh constructions failed in the independent check).
- A live (non-ingest) route to the bulk statutes zip: fetch_doc.py would need zip support.

# Mississippi (ms) probe log — 2026-10-17

All probes 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "WS" = WebSearch. No curl. WebFetch calls: 14 (5 PROVENANCE_REQUIRED approval-gate refusals on courts.ms.gov / sos.ms.gov / legislature.ms.gov, 1 session-limit error, 1 redirect notice). WebSearch: 4.

## Host checks
| URL | Tool | Result |
|---|---|---|
| https://www.legislature.ms.gov/ | script check | FETCH ERROR: TLS certificate chain does not verify |
| https://legislature.ms.gov/, https://billstatus.ls.state.ms.us/, http://billstatus.ls.state.ms.us/sessions.htm, https://www.ls.state.ms.us/ | script info | TLS error (all four) |
| https://www.legislature.ms.gov/ | WF | PROVENANCE_REQUIRED (approval gate, not site) |
| https://law.justia.com/codes/mississippi/ | script check | REFUSED: robots.txt answered with a bot check |
| https://courts.ms.gov/ | script check | robots permits |
| https://courts.ms.gov/robots.txt | script read | Disallow /appellatecourts/docket/, …/sendPDF.php, /search/, /scripts/ … |
| https://www.sos.ms.gov/, /adminsearch/ | script check | robots permits |
| https://www.sos.ms.gov/robots.txt | script read | Drupal defaults (/admin/, /search/, /user/…) |
| https://mississippi.public.law/ | script check | FETCH ERROR: proxy 502 on robots.txt |
| https://www.law.cornell.edu/regulations/mississippi | script check | permits; crawl-delay 10 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WS "Mississippi Code 1972 free access LexisNexis…" | WS | sos.ms.gov/node/147 |
| https://www.sos.ms.gov/node/147 | WF | "Mississippi Law" page; Code via LexisNexis, "the Code's official publisher"; constitution PDF link |
| https://www.lexisnexis.com/hottopics/mscode/ | script info/links | redirect → advance.lexis.com container; html chars=0; 0 links |
| same | WF | 302 to advance.lexis.com container (not followed) |
| WS "law.justia.com codes mississippi title 15…" | WS | year editions 2014-2024; /title-11/ |
| https://law.justia.com/codes/mississippi/title-11/ | WF | "2025 Mississippi Code 1972 Title 11"; chapter links with §§ ranges; ch. 9 "(Arts. 1 - 3)" |
| https://law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-49/ | WF (built) | YES "All actions for which no other period of limitation is"; not truncated |
| https://law.justia.com/codes/mississippi/title-97/chapter-3/section-97-3-19/ | WF (built) | YES "The killing of a human being without the authority of" |
| https://law.justia.com/codes/mississippi/title-11/chapter-9/ | WF | Article 1 (§§ 11-9-1 - 11-9-3), Article 3 (§§ 11-9-101 - 11-9-147) |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.sos.ms.gov/sites/default/files/publications/Mississippi_Constitution.pdf | script info/read/grep | PDF 193 pp, 368,794 chars; "ANNOTATED UPDATED MAY, 2022"; § 24 p. 16 "All courts shall be open"; § 14, § 273 present |
| same | WF | PROVENANCE_REQUIRED |
| https://law.justia.com/constitution/mississippi/ | WF ×2 | one page 120,868 chars; § 24 "All courts shall be open; and every person for an"; window 1 ends at § 157 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://courts.ms.gov/research/rules/rules.php | script links | links to all rule PDFs under /research/rules/msrulesofcourt/; local rule index pages |
| …/2026-07-01 Rules of Civil Procedure with Advisory Committee Notes (with Forms 6-8 attached).pdf | script info/grep | 231 pp; Rule 12(b)(6) p. 43; "RULE 56. SUMMARY JUDGMENT" p. 156 |
| …/2025-04-07 Restyled Rules of Evidence.pdf | script info/verify | 146 pp; VERIFIED Rule 702 text p. 86 |
| …/Rules of Appellate Procedure Current.pdf | script info/verify | 183 pp; VERIFIED Rule 17(a) heading p. 57 |
| …/Rules of Criminal Procedure Post-070123.pdf | script info/grep | 185 pp; "Rule 8.1 Definitions and Requirements." p. 39 |
| …/rules_of_professional_conduct.pdf | script info/verify | 143 pp; VERIFIED Rule 1.7(a) p. 29 |
| …/UCRCCC Post-070117.pdf | script info/grep | 25 pp; "may be cited as 'UCRCCC _.__.'"; Rule 4.01 |
| …/uniform_chancery_rules.pdf | script info/grep | 32 pp; "may be cited as UCCR"; RULE 1.10 p. 9 |

## D — Administrative code and bulletin
| URL | Tool | Result |
|---|---|---|
| https://www.sos.ms.gov/adminsearch/ , /adminsearch/default.aspx | script info | html chars=0 |
| https://www.sos.ms.gov/adminsearch/default.aspx | WF | PROVENANCE_REQUIRED |
| https://www.sos.ms.gov/regulation-enforcement/administrative-code | script links/read | iframe → adminsearch/default.aspx |
| …/administrative-code/administrative-bulletin | script read | iframe → default.aspx?current_page=Bulletin |
| https://www.sos.ms.gov/adminsearch/ACCode/00000300c.pdf | script info | (guessed id) PDF 2 pp "Title 2: Agriculture and Commerce Part 904" — not used as a route |
| WS "sos.ms.gov ACCode pdf Title 11…" / "sos.ms.gov/adminsearch/ACCode" | WS | LII and regulations.justia.com rule pages, MDAH archive |
| https://www.law.cornell.edu/regulations/mississippi/Miss-Admin-Code-11-8-31 | script read | navigation shell only (no rule) |
| …/regulations/mississippi/title-11 → /part-1 → /chapter-1 | script links | parts with chapter ranges; rule link 11-Miss-Code-R-SS-1-1-1 |
| https://www.law.cornell.edu/regulations/mississippi/11-Miss-Code-R-SS-1-1-1 | script grep | "11 Miss. Code. R. 1-1.1 - Delegations … The Commission delegates"; "updated quarterly" |
| https://www.law.cornell.edu/regulations/mississippi/11-Miss-Code-R-SS-1-6-1 | script grep (built) | "11 Miss. Code. R. 1-6.1 - General" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://courts.ms.gov/appellatecourts/sc/sc.php, scdecisions.php | script links/read | JS calendar "Hand Down Lists"; no list links |
| WS "courts.ms.gov images Opinions …" | WS | Images/HDList/SCT{MM-DD-YYYY}.html pattern; Justia year listings |
| https://courts.ms.gov/Images/HDList/SCT03-07-2019.html | WF | session usage limit error |
| https://courts.ms.gov/Images/HDList/SCT10-15-2026.html | script read/links | 7,139 chars; dockets, dispositions, links "..%5COpinions%5CCO196092.pdf" |
| same | WF | PROVENANCE_REQUIRED |
| SCT10-08-2026, COA10-13-2026, COA10-06-2026, SCT01-07-2010, COA01-05-2010, SCT01-06-2000 | script info | all html lists present |
| SCT01-08-1998 | script info | 190-char stub |
| SCT01-04-1996 | script info | network error (remote closed connection) |
| https://courts.ms.gov/Images/Opinions/CO196092.pdf | script read | 11 pp; "NO. 2025-CA-00269-SCT"; "¶1. Glenda Mayze’s knee was injured" |
| same | WF | PROVENANCE_REQUIRED |
| https://courts.ms.gov/Images/Opinions/CO195485.pdf | script read | "IN THE COURT OF APPEALS … NO. 2025-CA-00913-COA" |
| https://courts.ms.gov/appellatecourts/docket/sendPDF.php?f=700_779108.pdf&c=17875&a=N&s=2 | script info | REFUSED: robots disallows /appellatecourts/docket/sendPDF.php |
| https://law.justia.com/cases/mississippi/supreme-court/2021/ | WF | entries with dockets (2019-CT-01554-SCT …) |
| https://law.justia.com/cases/mississippi/supreme-court/2021/2020-ca-00293-sct.html | WF | YES "A Jones County jury returned a $4 million verdict"; ¶ to ¶81 |
| https://law.justia.com/cases/mississippi/court-of-appeals/2026/2025-ca-00913-coa.html | WF (built) | YES "Wiley Harrison appeals from a final judgment of the Lee County Chancery" |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| SCT10-15-2026, 10-08, 10-01, 09-24-2026 lists | script grep | cert dismissed/granted/denied entries under -CT-…-SCT dockets |
| https://courts.ms.gov/Images/HDList/SCT10-01-2026.html | script grep | "2024-CT-01022-SCT … Petition for Writ of Certiorari … is denied" |
| M.R.A.P. PDF | script verify | Rule 17(a) "Decisions of Court of Appeals Reviewable by Writ of Certiorari" |

# Tennessee (tn) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `scripts/fetch_doc.py --research`; "curl" = robots.txt reads only (no refusal worked around). WebFetch calls: 22 (of ~55), one refused by the session's URL-provenance gate (unanswered permission prompt, not a site refusal). WebSearch: 8.

## Host checks (script `check`; curl robots.txt)
| URL | Result |
|---|---|
| https://law.justia.com/codes/tennessee/ | script REFUSED: robots.txt answered with a bot check |
| https://www.tncourts.gov/ | script check "robots.txt permits", but curl robots.txt returns JS challenge (`function leastFactor(n)`); every page returns challenge (below) |
| https://sos.tn.gov/ | script REFUSED: bot check; curl robots.txt 403 CloudFront "Request blocked." |
| https://publications.tnsosfiles.com/ | script REFUSED: bot check; robots.txt 403 CloudFront "Request blocked." |
| https://sharetngov.tnsosfiles.com/ , https://tnsos.net/ | script REFUSED: bot check |
| https://www.capitol.tn.gov/ , https://wapp.capitol.tn.gov/ | script REFUSED: robots.txt `User-agent: *  Disallow: /` (Allow only for Googlebot, Bingbot, etc.) |
| http://www.capitol.tn.gov/about/docs/TN-Constitution.pdf | script REFUSED: Disallow: / |
| https://advance.lexis.com/ | OK (robots permits) |
| https://www.law.cornell.edu/regulations/tennessee | OK; crawl-delay 10 |
| https://tennessee.public.law/ | FETCH ERROR: proxy 502 on robots.txt |
| https://www.tn.gov/ | OK; but https://tn.gov/ (no www) REFUSED: bot check |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| WebSearch "Tennessee Code Annotated free public access LexisNexis…" | WS | store.lexisnexis.com, law.resource.org, tn.gov laws pages |
| https://tn.gov/generalservices/procurement/…/cpo-laws-central-procurement-office.html | script links | REFUSED: tn.gov bot check |
| https://www.tn.gov/commerce/fire/permit/licensing/fireworks/laws-rules/laws.html | script links "lexis" | 1 link: https://www.lexisnexis.com/hottopics/tncode/ |
| https://www.lexisnexis.com/hottopics/tncode/ | script info | redirect → advance.lexis.com/container?config=014CJAA5…; kind=html chars=0 |
| https://www.lexisnexis.com/hottopics/tncode/ | WF | 302 to advance.lexis.com container |
| https://advance.lexis.com/container?config=014CJAA5ZGVhZjA3NS02MmMzLTRlZWQtOGJjNC00YzQ1MmZlNzc2YWYKAFBvZENhdGFsb2e9zYpNUjTRaIWVfyrur9ud | WF | content empty (two horizontal rules only) |
| WebSearch "law.justia.com codes tennessee title-28 chapter-3 section 28-3-104" | WS | justia title/chapter and year-edition URLs |
| https://law.justia.com/codes/tennessee/title-28/chapter-3/ | WF | "2025 Tennessee Code"; parts listed by name only, no section ranges; disclaimer "These codes may not be the most recent version." |
| https://law.justia.com/codes/tennessee/title-28/chapter-3/part-1/section-28-3-104/ | WF (built URL, not gated) | YES; "(a) (1) Except as provided in subdivision (a)(2), the following"; not truncated |
| https://law.justia.com/codes/tennessee/title-39/chapter-17/part-13/section-39-17-1307/ | WF (built) | YES; "A person commits an offense who carries, with the intent"; year 2025 |
| WebSearch "publications.tnsosfiles.com acts 113 pub pc pdf Public Chapter" | WS | acts/107/pub/pc0582.pdf; sos.tn.gov/node/730 |
| https://publications.tnsosfiles.com/acts/107/pub/pc0582.pdf | WF | "PUBLIC CHAPTER NO. 582 SENATE BILL NO. 2183"; signatures; OCR garbled in places |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| WebSearch "Tennessee Constitution full text pdf sos.tn.gov OR capitol.tn.gov" | WS | sos.tn.gov/node/1487, law.justia.com/constitution/tennessee/ |
| https://sos.tn.gov/node/1487 | WF | not blocked; TSLA history of the 1796 constitution; no current text |
| https://www.law.cornell.edu/states/tennessee | script links | Constitution PDF link http://www.capitol.tn.gov/about/docs/TN-Constitution.pdf (robots-blocked) |
| https://law.justia.com/constitution/tennessee/article-i/ | WF | section links only; "This Constitution may not be the most recent version" |
| https://law.justia.com/constitution/tennessee/article-i/section-8/ | WF | YES; "That no man shall be taken or imprisoned, or disseized" |
| https://law.justia.com/constitution/tennessee/article-ii/section-24/ | WF (built) | YES; "No public money shall be expended except pursuant to appropriations" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.tncourts.gov/rules/rules-civil-procedure/1202 | script info/read | kind=html chars=138: "Please wait while we validate your browser" |
| WebSearch "tncourts.gov rules of civil procedure 12.02" | WS | tncourts.gov/node/3216 etc. |
| https://tncourts.gov/node/3216 | WF | CHALLENGE |
| https://www.law.cornell.edu/states/tennessee | script links | Court Rules → http://www.tncourts.gov/courts/rules (no LII copy) |

## D — Administrative code and register
| URL | Tool | Result |
|---|---|---|
| WebSearch "publications.tnsosfiles.com rules 1200-08-01 pdf" | WS | dated chapter PDFs; LII rule pages |
| https://publications.tnsosfiles.com/rules/1200/1200-08/1200-08-01.20220701.pdf | WF | "July, 2022 (Revised) 1 RULES OF THE TENNESSEE DEPARTMENT OF HEALTH"; rules TRANSFERRED to 0720-14; not truncated |
| WebSearch "sos.tn.gov effective rules … 0720-14" | WS | recently-effective page; LII title-0720 |
| https://sos.tn.gov/publications/services/recently-effective-rules-and-regulations | WF | list 3/5/2026 back to 1/28/2026; no hrefs exposed |
| WebSearch "sos.tn.gov effective-rules department chapter list" | WS | sos.tn.gov/rules-and-regulations; publications.tnsosfiles.com/rules/1330/1330.htm |
| https://publications.tnsosfiles.com/rules/0720/0720.htm | WF (built) | PROVENANCE_REQUIRED (gate; not retried) |
| https://publications.tnsosfiles.com/rules/1330/1330.htm | WF | "Rules of the Tennessee Board of Respiratory Care"; chapter 1330-01 listed; hrefs not exposed |
| https://sos.tn.gov/rules-and-regulations | WF | agency list "0020 Accountancy" …; "official compilation, Rules and Regulations of the State of Tennessee" |
| https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0720-14-01-.01 | script read | 5,850 chars: generic Tennessee index (nonexistent rule number falls back silently) |
| https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0780-01-01-.01 | script read | same generic index (same sha256) |
| https://www.law.cornell.edu/regulations/tennessee/title-0720 | script links | chapter-0720-14 → Tenn-Comp-R-Regs-0720-14-.01 |
| https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-0720-14-.01 | script grep | 35,920 chars; "(1) Abuse. The willful infliction of injury" |
| https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-1200-13-19-.01 | script grep/read | 5,349 chars; "This chapter governs all administrative hearings…"; Notes "Adopted effective May 6, 2015"; "State regulations are updated quarterly" |
| WebSearch "Tennessee Administrative Register sos.tn.gov rulemaking …" | WS | rules_filings PDFs; sos.tn.gov rulemaking guidelines |
| https://publications.tnsosfiles.com/rules_filings/04-09-24.pdf | WF | Notice of Rulemaking Hearing, 0400-30-39, filed April 11, 2024; 30 pages |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.tncourts.gov/courts/supreme-court/opinions | script info | chars=138 browser-validation challenge |
| https://law.justia.com/cases/tennessee/ | WF | 4 courts: supreme-court, court-of-appeals, court-of-criminal-appeals, workers-compensation |
| https://law.justia.com/cases/tennessee/supreme-court/2024/ | WF | "Tennessee Supreme Court Decisions 2024"; entries show docket + date; URL = lower-cased docket |
| https://law.justia.com/cases/tennessee/supreme-court/2024/w2021-00999-sc-r11-cv.html | WF | full opinion, footnotes, "- 13 -" page marker; no S.W.3d; PDF link cases.justia.com/…pdf?ts=1734727236 |
| https://cases.justia.com/tennessee/supreme-court/2024-w2021-00999-sc-r11-cv.pdf?ts=1734727236 | script info/grep | kind=pdf pages=13 chars=37216; "IN THE SUPREME COURT OF TENNESSEE AT JACKSON" (host not on vetted list; not used in a row) |
| https://law.justia.com/cases/tennessee/court-of-appeals/2025/ | WF | "Tennessee Court of Appeals Decisions 2025"; e2024-00871-coa-r3-pt … Dec. 30, 2025 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| WebSearch "tncourts.gov sites default files opinion pdf Tennessee Supreme Court 2025" | WS | ten "Discretionary Appeals List" PDFs (2025), irregular file names |
| https://www.tncourts.gov/sites/default/files/AppealsFileAttachments/Discretionary%20Appeals%20List%20-October-13-2025.pdf | script info | chars=138 challenge |
| same | WF | CHALLENGE "Please wait while we validate your browser" |
| https://tncourts.gov/ | script info | chars=138 challenge |

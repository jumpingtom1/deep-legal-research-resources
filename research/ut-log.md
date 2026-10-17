# Utah (ut) probe log — 2026-10-17

All probes were run on 2026-10-17 (some script probes at 00:05–00:11, before a usage-limit pause; the rest at 09:11–09:31) by `research`. Key: "script" = `scripts/fetch_doc.py --research`, "curl" = plain curl (robots.txt only), "WF" = WebFetch, "WS" = WebSearch.

Tool note: WebFetch returned `PROVENANCE_REQUIRED` ("permission request ... not answered in time") for le.utah.gov, legacy.utcourts.gov, www.utcourts.gov and adminrules.utah.gov URLs. Constructed law.justia.com URLs went through. 15 WebFetch calls were used, with no quota or rate failures.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://le.utah.gov/robots.txt | curl | 200; `User-agent: *` Crawl-delay 10; Disallow /templates/ /ASP/ /asp/ /includes/ /JSP/ /RSS/ |
| https://adminrules.utah.gov/robots.txt | curl | 404 (Next.js HTML) |
| https://www.utcourts.gov/robots.txt | curl | 406 Not Acceptable (WAF on curl UA) |
| https://legacy.utcourts.gov/robots.txt | curl | connection reset |
| https://www.utcourts.gov/robots.txt | script | 200, 23,203 chars; Disallow /opinions/*.pdf$, /opinions/supopin/, /appopin/, /mds/, /juv/, /resources/rules/comments/, /approved/, */search/* |
| https://legacy.utcourts.gov/robots.txt | script | 200, same rules |
| https://rules.utah.gov/robots.txt | curl | 200; Disallow /wp-admin/; Crawl-delay 10 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://le.utah.gov/xcode/Title78B/Chapter2/78B-2-S307.html | script | 200, 4,957 chars, navigation only (JS shell); raw HTML has `versionDefault="C78B-2-S307_2023050320230503"` |
| https://le.utah.gov/xcode/Title76/Chapter5/76-5-S203.html | script | same shell; versionDefault C76-5-S203_2026050620260506 |
| https://le.utah.gov/xcode/Title78B/Chapter2/78B-2-S307.html | WF | PROVENANCE_REQUIRED |
| …/Title78B/Chapter2/C78B-2-S307_2023050320230503.html | script | 2,222 chars; "An action may be brought within four years:"; "Effective 5/3/2023"; links .pdf/.rtf/.xml |
| …/Title76/Chapter5/C76-5-S203_2026050620260506.html | script | body present; "Effective 5/6/2026" |
| …/C78B-2-S307_2023050320230503.xml | script | 965 chars; "Amended by Chapter 185, 2023 General Session" |
| grep shell for versionDefault | script | 0 matches (script strips JS) |
| https://le.utah.gov/xcode/code.html | script | JS shell; versionDefault C_1800010118000101 |
| https://le.utah.gov/xcode/C_1800010118000101.html | script | title list (3…81, incl. 75E, 76 "Criminal Offenses"); links ?v= ids; no currency string |
| https://le.utah.gov/xcode/Title78B/C78B_1800010118000101.html | script | chapter links, e.g. 78B-2.html?v=C78B-2_1800010118000101 |
| …/Title78B/Chapter2/C78B-2_1800010118000101.html | script | 890 chars; parts listed; no section ranges |
| …/Title78B/Chapter2/C78B-2-P3_1800010118000101.html | script | sections with ?v= ids, e.g. S307 → C78B-2-S307_2023050320230503 |
| https://le.utah.gov/xcode/Title78B/C78B_1800010118000101.pdf | script | pdf 456 pp, 1,516,158 chars |
| https://le.utah.gov/documents/disclaimer.htm | script | "attempt to ensure … accurate and complete"; "as is" |
| https://legacy.utcourts.gov/statutes/?s=78B-2 | script | redirect page to le.utah.gov 78B-2.html |
| https://le.utah.gov/UtahCode/ChapterLookup.jsp?chap=185&sess=2023GS | script | → /~2023/bills/static/HB0388.html, 9,166 chars |
| https://le.utah.gov/~2023/bills/hbillenr/HB0030.pdf | script | pdf 214 pp |
| WS "le.utah.gov xcode 78B-2-307 …" | WS | syfert, Justia 2024 title-78b, legacy.utcourts statutes |
| WS "le.utah.gov xcode Title76 …" ; "law.justia.com codes utah title-78b …" | WS | no xcode URLs |
| https://law.justia.com/codes/utah/2024/title-78b/ | WF | "2024 Utah Code Title 78B - Judicial Code"; no section ranges; 2025 = unversioned |
| https://law.justia.com/codes/utah/title-78b/ | WF | "2025 Utah Code"; "These codes may not be the most recent version." |
| https://law.justia.com/codes/utah/title-78b/chapter-2/ | WF | Part 3 → /chapter-2/part-3/ |
| https://law.justia.com/codes/utah/title-78b/chapter-2/part-3/ | WF | /part-3/section-307/ |
| https://law.justia.com/codes/utah/title-78b/chapter-2/part-3/section-307/ | WF | YES "An action may be brought within four years: (1) after"; "UT Code § 78B-2-307 (2025)" |
| https://law.justia.com/codes/utah/title-76/chapter-5/part-2/section-203/ | WF | YES; "UT Code § 76-5-203 (2025)" |
| https://law.justia.com/codes/utah/title-78b/chapter-2/part-3/section-307/ | script | REFUSED: law.justia.com robots.txt challenge (off for the day) |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://le.utah.gov/xcode/constitution.html | script | JS shell; versionDefault UC_1800010118000101 |
| https://le.utah.gov/xcode/UC_1800010118000101.html | script | Article I → ArticleI/Article_I.html?v=UC_AI_1800010118000101 |
| https://le.utah.gov/xcode/ArticleI/UC_AI_1800010118000101.html | script | Section 11 ?v=UC_AI_S11_2020051220210101 |
| https://le.utah.gov/xcode/ArticleI/UC_AI_S11_2020051220210101.html | script | "All courts shall be open, and every person, for an injury"; Effective 1/1/2021 |
| https://le.utah.gov/xcode/ArticleVIII/UC_AVIII_1800010118000101.html | script | Section 3 ?v=UC_AVIII_S3_1800010118000101 |
| https://le.utah.gov/xcode/ArticleVIII/UC_AVIII_S3_1800010118000101.html | script | "The Supreme Court shall have original jurisdiction" |
| https://law.justia.com/constitution/utah/ | WF | TOC only; "This Constitution may not be the most recent version."; Art. I → CO_02.html |
| https://law.justia.com/constitution/utah/CO_02.html | WF | NOT PRESENT (section headings with links only) |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://legacy.utcourts.gov/rules/ | script | 4,906 chars; set links urcp, urcrp, urap, urjp, srpe, adr, ure, urbcp, ucja, scrp |
| https://legacy.utcourts.gov/rules/view.php?type=urcp&rule=12 | script | 8,347 chars; "Rule 12. Defenses and objections."; "Effective: 5/1/2024" |
| https://www.utcourts.gov/rules/view.php?type=urcp&rule=12 | script | redirects to legacy host, same text |
| https://legacy.utcourts.gov/rules/view.php?type=urcp&rule=12 | WF | PROVENANCE_REQUIRED |
| …view.php?type=ure&rule=702 | script | first try: connection reset; later: "Rule 702. Testimony by Experts."; Effective 11/1/2007 |
| …view.php?type=urcrp&rule=11 | script | "Rule 11. Pleas." |
| …view.php?type=urap&rule=24 | script | "Principal briefs must contain under appropriate headings"; Effective 11/1/2017 |
| …view.php?type=scrp&rule=3-1.07 | script | "Rule 3-1.7. Conflict of Interest: Current Clients."; previously UCJA 13-1.7 |
| …view.php?type=ucja&rule=4-202.02 | script | "Records Classification"; Effective 5/18/2026 |
| …view.php?type=urbcp&rule=1 | script | "Rule 1. General provisions." |
| https://legacy.utcourts.gov/rules/{scrp,ucja,ure,urcrp,urap}.php | script (links) | per-rule view.php links; scrp Rule 1.7 → rule=3-1.07 |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://adminrules.utah.gov/ | script | 877 chars of navigation; links /Code, rules.utah.gov bulletin |
| https://adminrules.utah.gov/Code | script | 873 chars; "Current Rules", "Agencies"; no rules |
| https://adminrules.utah.gov/Code | WF | PROVENANCE_REQUIRED |
| https://adminrules.utah.gov/public/rule/R414-1/Current%20Rules | script | HTTP 404 |
| WS "adminrules.utah.gov R414-1 …"; WS "\"adminrules.utah.gov/public\" rule R307-101" | WS | LII, Justia regs, rules.utah.gov bulletin pages; no adminrules per-rule URL |
| https://www.law.cornell.edu/regulations/utah | script | topic links |
| …/regulations/utah/health → title-R414 → rule-R414-1 | script | "Rule R414-1 … (§ R414-1-1 to R414-1-32)"; section link Utah-Admin-Code-R414-1-1 |
| https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R414-1-1 | script | 2,715 chars; "(1)(a) Title XIX of the Social Security Act"; "Bulletin Number 2025-05"; "updated quarterly" |
| https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R307-101-2 | script | "Except where specified in individual rules, definitions in" |
| https://rules.utah.gov/publications/utah-state-bulletin/ | script | 75,681 chars; "Vol. 2026, No. 20 (10/15/2026)" → wp-content/uploads/b20261015.pdf |
| https://rules.utah.gov/wp-content/uploads/b20261001.pdf | script | pdf 311 pp, 1,304,012 chars; "an official noticing publication of the executive branch" |
| https://rules.utah.gov/publicat/bulletin/2017/20170301/41321.htm | script | "DAR File No. 41321" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| WS "utcourts.gov Utah Supreme Court opinions 2024 UT pdf"; WS "site:utcourts.gov opinions supreme court \"2025 UT\"" | WS | cert petition PDFs under /content/dam/courts/sup/certs/petitions/ |
| https://www.utcourts.gov/en/opinions.html | script | HTTP 404 |
| https://www.utcourts.gov/opinions/ | script | → legacy.utcourts.gov/opinions/, 3,937 chars; year selectors 1997–2026 |
| https://legacy.utcourts.gov/opinions/supopin/ | script | REFUSED robots (Disallow: /opinions/supopin/) |
| https://legacy.utcourts.gov/rss/opinions/index.xml | script | 1,582 chars; items like "State v. Conde20261008_20241010_149.pdf" |
| https://legacy.utcourts.gov/opinions/streams/?court=sup | script | 200, 11,331 chars (oral-argument audio) |
| https://legacy.utcourts.gov/opinions/view.html?court=appopin&opinion=State%20v.%20Conde20261008_20241010_149.pdf | script | REFUSED robots (Disallow: /opinions/*.pdf$) |
| http://www.utcourts.gov/opinions/view.html?court=appopin&opinion=State v. Conde… | WF | PROVENANCE_REQUIRED |
| https://law.justia.com/cases/utah/supreme-court/2025/ | WF | listing; State v. Jennings 20230556 → /2025/20230556.html |
| https://law.justia.com/cases/utah/supreme-court/2025/20230556.html | WF | YES "Deon Andre Jennings is charged with the murder of Willie"; 2025 UT 59; ¶1–¶78 |
| https://law.justia.com/cases/utah/court-of-appeals-published/2025/ | WF | listing; State v. Leatham 20230824-CA → 20230824-ca.html |
| https://law.justia.com/cases/utah/court-of-appeals-published/2025/20230824-ca.html | WF | YES "A driver was stopped by officers and found to lack"; 2025 UT App 194 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.utcourts.gov/en/about/courts/sup/certs.html | script | HTTP 404 |
| https://www.utcourts.gov/content/dam/courts/sup/certs/petitions/2025cert_09-10.pdf | script | pdf 1 pp; "Reporting period: 9/01/2025 - 10/31/2025"; GRANTED State v. Lucke 20230428 |
| https://www.utcourts.gov/content/dam/courts/sup/certs/petitions/2024cert_07-08.pdf | script | "Reporting period: 07/01/2024 - 08/31/2024" |

## Build
- `python3 scripts/build.py --check`: no output, exit 0.
- `python3 scripts/build.py --cross`: the first run gave "CROSS ut: 'Utah Code section 76-5-203' also matches ga / Official Code of Georgia Annotated", because Georgia's case-insensitive "Code Section" pattern matches it. I changed the example to "Utah Code Ann. section 76-5-203" and recorded the collision in notes. The re-run gave 0 matches.

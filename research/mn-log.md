# Minnesota (mn) probe log — 2026-10-16/17

All probes by `research`, on 2026-10-16 (the environment clock rolled to 2026-10-17 while the record was being written). "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET through the agent proxy, used only for robots files, index-page link lists and headers, and never on a refused URL. Quoted text is 15 words or fewer. WebFetch calls attempted: 40 (31 returned content). No quota or rate failures.

**Harness note.** For URLs that no search had surfaced, WebFetch returned `PROVENANCE_REQUIRED` ("permission request … not answered in time"). That happened for revisor.mn.gov/statutes/cite/541.05, revisor.mn.gov/state_register/50/1/, mncourts.gov/robots.txt, mn.gov/law-library/search/opinions-archive.jsp and macsnc…/publicLogin.jsp. None was retried. These are not site refusals.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://www.revisor.mn.gov/robots.txt | curl | 200; `*` Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result |
| https://mncourts.gov/robots.txt, https://www.mncourts.gov/robots.txt | curl | 403 Cloudflare "Just a moment..." |
| https://mncourts.gov/ | script | REFUSED: "answers robots.txt with a bot check (challenge)" |
| https://mn.gov/robots.txt | curl | 200; Disallow /law-library-stat/archive/, /law-library-stat/briefs/; Visit-time 0000-1200; Request-rate 10 |
| https://mn.gov/law-library-stat/archive/supct/ | script | REFUSED: robots.txt disallows /law-library-stat/archive/ |
| https://law.justia.com/robots.txt | curl | 403 Cloudflare challenge |
| https://www.law.cornell.edu/robots.txt | curl | 200; Crawl-delay 10 |
| https://macsnc.courts.state.mn.us/robots.txt | curl | 200 "User-agent: * Allow: /" |
| mn.gov static archive, law-library search, macsnc, publicaccess | script check | allowlisted; robots permits |

## A — Statutes and session laws
| URL | Tool | Result |
|---|---|---|
| https://www.revisor.mn.gov/statutes/cite/541.05 | script | html 8,731 chars; "2025 Minnesota Statutes"; "Except where the Uniform Commercial Code otherwise prescribes" |
| …/statutes/cite/609.185 | script | 10,681 chars; "MURDER IN THE FIRST DEGREE. (a) Whoever does any of the following" |
| …/statutes/cite/336.2-725 | script | 8,747 chars; "An action for breach of any contract for sale must be commenced" |
| …/statutes/cite/541.05 | WF | PROVENANCE_REQUIRED (built URL) |
| https://www.revisor.mn.gov/statutes/?id=441.51 | WF, script | NOT PRESENT; repealed stub "[Repealed, 1984 c 543 s 69]" |
| https://www.revisor.mn.gov/statutes/?id=254.05 | WF | repeal note; "2025 Minnesota Statutes"; footer "Official Publication of the State of Minnesota" |
| https://www.revisor.mn.gov/statutes/?id=541.05 | curl -I | 301 → /statutes/cite/541.05 |
| https://www.revisor.mn.gov/statutes/2025/cite/609.185 | WF | YES "(a) Whoever does any of the following is guilty of"; complete |
| https://revisor.mn.gov/statutes/2023/cite/609.185/pdf | WF | served as web page; "MINNESOTA STATUTES 2023" |
| …/statutes/cite/541.05/pdf | script | PDF 1 p, 2,217 chars |
| …/statutes/cite/609/full | script | 1,061,273 chars |
| …/statutes/2024/cite/541.05 | script | 8,832 chars; "2024 Minnesota Statutes" |
| https://www.revisor.mn.gov/authenticate/ | curl | "Authenticated PDF copies … official electronic records under the Uniform Electronic Legal Material Act" |
| https://www.revisor.mn.gov/statutes/info | curl | "Two versions … are official": print edition and authenticated PDFs (§ 3E.04, subd. 2) |
| https://www.revisor.mn.gov/downloads/, /data/, /office/downloads | curl | 404 / 502 / 502 (no bulk download found) |
| https://www.revisor.mn.gov/laws/2024/0/127/ | script | 4,174,473 chars; "2024 Regular Session Chapter 127" |
| https://www.revisor.mn.gov/laws/2015/0/5/ | script | 389,733 chars |
| https://law.justia.com/codes/minnesota/ | WF | 29 editions, 2025 back to 1997 |
| https://law.justia.com/codes/minnesota/2025/ | WF ×2 | group links with ranges: "Chapters 540 - 552 — Civil Procedure", "Chapters 324 - 342", "Chapters 609 - 624" |
| https://law.justia.com/codes/minnesota/chapters-540-552/chapter-541/section-541-05/ | WF | YES; "MN Stat § 541.05 (2025)"; complete |
| https://law.justia.com/codes/minnesota/chapters-324-342/chapter-336/section-336-2-725/ | WF | YES "(1) An action for breach of any contract for sale"; "MN Stat § 336.2-725 (2025)" |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.revisor.mn.gov/constitution/ | script | 79,554 chars; anchors article_1, section_1_8; "Sec. 8. Redress of injuries or wrongs." |
| same | WF | YES "Every person is entitled to a certain remedy in the"; ends Art. XIV § 13; "Generally Revised November 5, 1974" |
| https://law.justia.com/constitution/minnesota/ | WF | index only; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/minnesota/Article1.html | WF | YES § 8; Art. I ends Sec. 17; no currency |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.revisor.mn.gov/court_rules/ | curl | sets ap, cp, cr, dc, ev, gp, ju, ms, pr, ra, sg, each with /pdf/ |
| …/court_rules/info/ | curl | "not intended to replace an official source"; official edition printed under § 3C.08 |
| …/court_rules/rule/{ev,cr,gp,aprcap,prcond,prprof,apspec,apflam}-toh/ | curl | per-rule links /court_rules/{set}/id/{n}/ and /{set}/subtype/{sub}/id/{n}/ |
| …/court_rules/cp/id/12/ | script | 14,832 chars; "Defendant shall serve an answer within 21 days" |
| …/court_rules/ev/id/702/ | script | 11,886 chars; "Rule 702.Testimony by Experts If scientific, technical" |
| …/court_rules/cr/id/15/ | script | 34,244 chars; "Rule 15.Guilty Plea Procedures 15.01 Felony Cases" |
| …/court_rules/gp/id/115/ | script | 29,993 chars; 115.03 found |
| …/court_rules/ap/subtype/rcap/id/103/ | script | 25,201 chars; "103.03 Appealable Judgments and Orders" |
| …/court_rules/ap/subtype/rcap/id/136/ | script | "nonprecedential opinions may be cited as persuasive authority"; amended eff. Aug. 1, 2020 |
| …/court_rules/pr/subtype/cond/id/1.7/ | script | 34,322 chars; "Rule 1.7 Conflict of Interest: Current Clients" |
| https://www.revisor.mn.gov/court_rules/ev/id/702 | WF | YES "If scientific, technical, or other specialized knowledge will assist the"; "(Amended effective September 1, 2006.)" |
| https://www.revisor.mn.gov/court_rules/rule/ev-702/ | WF | YES (alternate per-rule URL) |
| https://www.revisor.mn.gov/court_rules/ev/pdf | WF | truncated at Rule 609; 1101 NOT PRESENT; "With amendments received through July 1, 2019" |
| …/court_rules/{cp,ev,cr,ap,gp}/pdf/ | script | 174/70/259/142/341 pp; covers "through July 1, 2025" / "July 1, 2019" / "July 1, 2026" / "April 1, 2025" / "July 1, 2026" |

## D — Minnesota Rules and State Register
| URL | Tool | Result |
|---|---|---|
| https://www.revisor.mn.gov/rules/7050.0222/ | script | 139,178 chars |
| same | WF | YES subp. 1; truncated in subp. 3c item B; "[Content truncated due to length...]" |
| https://www.revisor.mn.gov/rules/1400.5100/ | script | 8,458 chars; "Published Electronically: August 6, 2013"; History "9 SR 2276; 15 SR 1595; 26 SR 391" |
| https://www.law.cornell.edu/regulations/minnesota | WF | YES; "Agency 101 - Abstracters Board" |
| https://www.law.cornell.edu/regulations/minnesota/Minn-R-1400-5100 | script | 4,069 chars; last-modified 3 Aug 2025 |
| https://www.law.cornell.edu/regulations/minnesota/Minn-R-7050-0222 | script | 99,488 chars |
| https://www.revisor.mn.gov/state_register/ | curl, WF | Vol. 51 "Jul, 2026 to Oct, 2026" 1-15; vols. 41 onward from the Minnesota Bookstore |
| https://www.revisor.mn.gov/state_register/50/ | curl | issue table (number, date, pages) |
| https://www.revisor.mn.gov/state_register/50/1/ | curl -I | 302 → https://mn.gov/admin/assets/SR50_01_tcm36-696254.pdf |
| same | script | PDF 24 pp, 83,257 chars; "Monday, July 7, 2025 Volume 50, Number 1" |
| same | WF | PROVENANCE_REQUIRED |
| https://www.revisor.mn.gov/state_register/39/pdf/ | script | 12 pp; "Title Index for Volume 39, #1-26" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://mncourts.gov/courtofappeals/recentopinions/nonprecedential-opinions | WF | 9 opinions filed Oct. 12, 2026 with PDF links; no archive |
| https://mncourts.gov/_media/migration/appellate/court-of-appeals/standard-opinions/12oct26/OPa260557-101226.pdf | WF | ROBOTS_DISALLOWED |
| https://mncourts.gov/_media/migration/appellate/supreme-court/standard-opinions/14oct26/ORA251802-100626.pdf | WF | ROBOTS_DISALLOWED |
| https://mncourts.gov/SupremeCourt/RecentOpinions.aspx | WF | overview; links to opinions, opinion sets, PFR orders; archive = law-library search |
| https://mncourts.gov/supremecourt/recentopinions/minnesota-supreme-court-opinion | WF | "RELEASED OCTOBER 14, 2026" "No Opinions Filed."; 3 disciplinary orders |
| https://mncourts.gov/supremecourt/recentopinions/opinion-sets | WF | one zip link (14oct26) |
| https://mncourts.gov/courtofappeals/recentopinions/precedential-opinions | WF | "No Precedential Opinions Filed." (Oct. 12, 2026) |
| https://mncourts.gov/PublicAccess/ | WF | links P-MACS and the law-library opinion archive |
| https://mn.gov/law-library/how-do-i-find/unpublished-opinions.jsp | WF | archive links; quotes 136.01 subd. 1(c) and § 480A.08 subd. 3 |
| https://mn.gov/law-library/search/opinions-archive.jsp | WF | PROVENANCE_REQUIRED |
| https://mn.gov/law-library/search/?v:sources=mn-law-library-opinions | WF ×2 | form; "Supreme Court opinions and orders from May 2, 1996 to present"; form attributes NOT VISIBLE |
| …search/?v:sources=mn-law-library-opinions&query=A23-1544 | WF | landing page, no results |
| …search/index.jsp?…&query=A23-1234, …&query=Honcik, …&query=Thigpen | script | redirected to validate.perfdrive.com "Please validate your request" (ShieldSquare CAPTCHA) |
| https://mn.gov/web/prod/static/lawlib/live/archive/cau13q4.html | WF | "October - December 2013 Unpublished and Order Opinions"; PDFs at ctapun/1312/ |
| https://www.mn.gov/web/prod/static/lawlib/live/archive/index.html | WF, script | coverage "May 2, 1996 - March 27, 2013"; relative links resolve to mn.gov/archive/… |
| https://mn.gov/web/prod/static/lawlib/live/archive/sctdate.html | script, curl | quarterly list to "January - March 2016"; a later curl got the CAPTCHA script (1,242 bytes) |
| https://mn.gov/web/prod/static/lawlib/live/archive/capdate.html | script | CAPTCHA redirect (validate.perfdrive.com) |
| https://mn.gov/web/prod/static/lawlib/live//archive/sct16q1.html | WF | latest Feb. 3, 2016; PFR list links (pfr01-27-2016.pdf) |
| https://mn.gov/web/prod/static/lawlib/live/archive/ctapun/1312/opa121997-123013.pdf | script | 23 pp, 41,143 chars; "This opinion will be unpublished and may not be cited" |
| https://law.justia.com/cases/minnesota/ | WF | supreme-court, court-of-appeals |
| https://law.justia.com/cases/minnesota/court-of-appeals/2026/ | WF | Oct. 5, 2026 entries; slugs a25-1318.html |
| https://law.justia.com/cases/minnesota/court-of-appeals/2026/a25-1783.html | WF | YES; nonprecedential notice; slip page numerals; complete |
| https://law.justia.com/cases/minnesota/supreme-court/2025/ | WF | Walsh v. City of Orono A25-0354 (Dec. 31, 2025) … |
| https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1544.html | WF | YES; "The penalty under Minnesota law for obtaining unemployment benefit overpayments"; no N.W.3d cite |
| https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1544.html | script | REFUSED (Justia robots challenge, host off for the day) |
| https://mncourts.gov/courtofappeals/recentopinions/nonprecedential-opinions | script | REFUSED (bot check) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://mncourts.gov/supremecourt/recentopinions/orders-on-petitions-for-further-review | WF | "FILED WEDNESDAY, SEPTEMBER 30, 2026"; Granted 1-5, Denied 8-38; unlinked text with dockets |
| https://mn.gov/web/prod/static/lawlib/live/archive/supct/2016/pfr01-27-2016.pdf | script | 1 p; "Benjamin Paul Adams – A14-1891 – Denied" |
| https://law.justia.com/cases/minnesota/court-of-appeals/2024/a23-1544.html | WF | Thigpen COA, July 29, 2024, nonprecedential; same docket as the Supreme Court decision |
| http://macsnc.courts.state.mn.us/ctrack/publicLogin.jsp | script | 0 chars of text |
| https://macsnc.courts.state.mn.us/ctrack/publicLogin.jsp | curl | 200; JavaScript bot-defence page (server volt-adc) instead of the form |
| same (http) | WF | PROVENANCE_REQUIRED |

## Searches (discovery only)
- "Minnesota Court of Appeals opinions archive mncourts.gov …": surfaced the static archive pages (/web/prod/static/lawlib/live/archive/cau…).
- "mncourts.gov 'Court of Appeals' opinions 'nonprecedential' …", "mncourts.gov supremecourt recentopinions …", "mncourts.gov _media … pdf 2025": found the listing URLs.
- "law.justia.com codes minnesota 2025 chapter 541 …", "revisor.mn.gov statutes cite 609.185 …", "revisor.mn.gov court_rules ev id 702 …", "revisor.mn.gov rules 7050.0222 …", "Minnesota Revisor … bulk download XML …" (none found), "'lawlib/live/archive' supreme court … 2015".

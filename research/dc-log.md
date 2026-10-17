# District of Columbia (dc) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `python3 scripts/fetch_doc.py --research`; "WF" = WebFetch; "WS" = WebSearch (discovery only). About 30 WebFetch calls used. CourtListener tools not used.

## Robots / host checks (script)
| URL | Result |
|---|---|
| https://code.dccouncil.gov/robots.txt | 200; Cloudflare-managed; `User-Agent: *` Allow / with "Content-signal: search=yes,ai-train=no"; Disallow for ClaudeBot, GPTBot, CCBot, Amazonbot, Bytespider, Google-Extended, meta-externalagent; `Disallow: /_*` |
| https://www.dcregs.dc.gov/robots.txt | 200; Cloudflare content-signal comments; no Disallow seen in the part read |
| https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments | REFUSED: "answers robots.txt with a bot check"; host off for the day |
| https://github.com/DCCouncil/law-xml | REFUSED: github.com robots bot check |
| https://law.justia.com/... | REFUSED (robots.txt challenge, recorded earlier in the day) |
| https://www.public.law/ | 200 (cached); no D.C. site listed |
| https://www.law.cornell.edu/states/dc | 200; links out to LexisNexis, dccourts.gov, dcregs.dc.gov |
| https://www.law.cornell.edu/regulations | 200; state list goes Delaware → Florida (no D.C.) |
| https://www.law.cornell.edu/states/district_of_columbia, /regulations/district-of-columbia | 404 |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://code.dccouncil.gov/us/dc/council/code/sections/16-1001 | script | html 4,935 chars; "For the purposes of this subchapter, the term:"; footer "Please do not scrape. Instead, bulk download the HTML or XML." |
| same | WF | PROVENANCE_REQUIRED (permission prompt not answered); not retried |
| https://code.dccouncil.gov/us/dc/council/code | WF (first try) | PROVENANCE_REQUIRED |
| …/sections/2-1402.11 | script | 22,009 chars |
| WS "code.dccouncil.gov § 16-1001 …", WS "code.dccouncil.gov/us/dc/council/code/sections" | WS | section URLs (2-552, 11-502, 47-861 …) |
| …/sections/2-552 | WF | YES "(a) The District of Columbia Office of Documents, established pursuant to"; no currency; not truncated |
| https://code.dccouncil.gov/us/dc/council/code | WF | "Current through" "Sept. 26, 2026"; "Law 26-187 effective Sept. 26, 2026"; no official statement; bulk links github.com/dccouncil/law-html, law-xml; title URLs /code/titles/1, /titles/27A |
| …/sections/11-502 | WF | YES "In addition to its jurisdiction as a United States district"; not truncated |
| …/sections/2-702 | script | body present (official mail) |
| …/code/titles/16 | script | chapters with ranges, e.g. "Chapter 10 … §§ 16-1001 – 16-1058" |
| WS UELMA D.C. | WS | found sections 2-651.04-.06, D.C. Law 21-251 |
| …/sections/2-651.02, 2-651.03, 2-651.04 | script | UELMA: applies to material first published electronically on/after July 1, 2017; designation + authentication duties |
| WS "DC Council official D.C. Code online …" | WS | dccouncil.gov 2016 post; dcist/slashdot 2018 GitHub stories |
| https://dccouncil.gov/easy-user-friendly-access-dc-code-now-official-website-feature/ | WF | July 13, 2016 post; beta site; no official-text designation |
| https://raw.githubusercontent.com/DCCouncil/law-xml/main/README.md | script | "raw, uncodified laws, along with the code as it appeared on March 10, 2016"; names law-xml-codified and law-html |
| …/law-xml/main/us/dc/council/code/titles/16/sections/16-1001.xml | script | 4,207 chars; old text ("Domestic Violence Unit"); grep "Family member" 0 matches → stale |
| …/law-xml-codified/main/…, …/law-html/main/… , READMEs | script | 404 |
| …/law-xml/master/…16-1001.xml | script | 404 |
| https://raw.githubusercontent.com/DCCouncil/law-html/master/us/dc/council/code/sections/16-1001.html | script | 4,935 chars; "Family member" 3 matches |
| https://raw.githubusercontent.com/DCCouncil/law-xml-codified/master/us/dc/council/code/titles/16/sections/16-1001.xml | script | 4,343 chars; "Family member" 3 matches |
| …/law-xml-codified/master/…/titles/2/sections/2-1402.11.xml | script | 21,818 chars; "Prohibitions." |
| …/law-xml-codified/master/us/dc/council/code/index.xml | script | template only ("Law {{ doc.num }}") |
| …/law-html/master/us/dc/council/code/index.html | script | "Current through Apr. 29, 2026 Last codified D.C. Law: Law 26-112" |
| https://code.dccouncil.gov/us/dc/council/laws/23-275 | script | 39,401 chars; "Intrafamily Offenses and Anti-Stalking Orders Amendment Act of 2020" |
| https://code.dccouncil.gov/us/dc/council/laws/docs/17-368.pdf | script | pdf, 8 pages |
| WS "law.justia.com codes district-of-columbia …" | WS | /codes/district-of-columbia/title-38, /2016/, /2019/ |
| https://law.justia.com/codes/district-of-columbia/title-38 | WF | "2025 District of Columbia Code"; chapters, no section ranges; "These codes may not be the most recent version." |
| …/title-38/chapter-1/ | WF | subchapter links (subchapter-i, subchapter-i-a, subchapter-ii); no ranges |
| …/title-38/chapter-1/subchapter-ii/ | WF | section links section-38-131 …; no body |
| …/subchapter-ii/section-38-131/ | WF | YES "The Chancellor of the District of Columbia Public Schools is"; not truncated |
| https://law.justia.com/codes/district-of-columbia/title-16/chapter-10/subchapter-i/section-16-1001/ (built) | WF | YES; (5A) Family member present; "2025 District of Columbia Code" |
| same | script | REFUSED (law.justia.com off for the day) |

## B — Constitution (Home Rule Act)
| URL | Tool | Result |
|---|---|---|
| https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02 | script | "(a) The Council shall have no authority to pass any act contrary" |
| https://code.dccouncil.gov/us/dc/council/code/titles/1/chapters/2 | script | subch. I–VII with ranges; "Subchapter IV. The District Charter. §§ 1-204.01 – 1-204.115" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| WS "dccourts.gov Superior Court Rules of Civil Procedure Rule 12 pdf …" | WS | compiled 2025 PDF; per-rule "Civil Rule 1. Scope and Purpose.pdf"; promulgation order 25-01 |
| https://www.dccourts.gov/sites/default/files/superior-rules/Superior-Court-Rules-of-Civil-Procedure-2025.pdf | WF ×2 | CLIENT_ERROR "There was an error while fetching." both times |
| https://www.dccourts.gov/sites/default/files/rules-superior-court/Civil%20Rule%201.%20Scope%20and%20Purpose.pdf | WF | YES "These rules govern the procedure in all civil actions and"; "COMMENT TO 2017 AMENDMENTS" |
| WS "dccourts.gov District of Columbia Court of Appeals Rules pdf Rule 28 …" | WS | DCCA_Complete_Rules.pdf (2024-06), DCCA-Rules-6-2022.pdf, 2020/2021 versions, per-rule Rule 28 PDF |
| https://dccourts.gov/sites/default/files/2024-06/DCCA_Complete_Rules.pdf | WF | Rule 28(a) YES "Brief of the Appellant (or Petitioner). The brief must contain,"; cover "Revised effective December 1, 2021"; window ends Rule 29(a)(6); Rule 40 NOT PRESENT; 123,307 chars |
| same, offset 100000 | WF | Rules 35, 40 present; ends mid-word in Rule 41(g) "A mandate is not issued in a disciplinary cas" |
| same (Rule 28(g) question) | WF | unpublished orders/opinions not citable except law of case, res judicata, collateral estoppel, same defendant/respondent; no 2007 cutoff |
| WS "dccourts.gov rules-superior-court Civil Rule 12 pdf" | WS | /superior-court/rules index URL |
| https://www.dccourts.gov/superior-court/rules | WF | 18 rule sets listed; per-rule titles; hrefs not exposed; no currency line |

## D — DCMR and D.C. Register
| URL | Tool | Result |
|---|---|---|
| https://www.dcregs.dc.gov/ | script | 23,516 chars; ASP.NET postback links |
| https://www.dcregs.dc.gov/Common/DCMR/TitleList.aspx | script | redirected to /ErrorPage.aspx |
| https://www.dcregs.dc.gov/Common/DCMR/ChapterList.aspx?TitleNum=14 | script | 42,124 chars |
| https://www.dcregs.dc.gov/Common/DCMR/RuleList.aspx?ChapterNum=14-3 | script | 19 sections 14-300…14-399 with effective dates; "View text" anchors carry DownloadFile GUIDs |
| same | WF | PROVENANCE_REQUIRED (gated) |
| https://www.dcregs.dc.gov/Common/DCMR/SectionList.aspx?SectionNumber=14-308 | script | metadata: "Most recent version of the final adopted rule codified in the D.C. Municipal Regulations"; Effective Date 1/1/1900; source note; text link is a postback |
| https://dcregs.dc.gov/Common/DCMR/RuleList.aspx?DownloadFile=F072555F-0000-C01C-9C51-075D1CDEADB6 | script | filename=14308.doc, 22,528 chars; grep finds "308.1 For purposes of this chapter, the term “security deposit”" |
| WS "dcregs.dc.gov DCMR RuleList/SectionList …" (×2) | WS | no dcregs URLs returned |
| https://www.dcregs.dc.gov/Common/NoticeDetail.aspx?NoticeId=N0047614 | script | 12,176 chars metadata; "Register Issue : 5/16/2014 Vol 61/21"; text link postback |
| https://www.dcregs.dc.gov/Common/DCR/Issues/IssueDetailPage.aspx?issueID=493 | script | "DISTRICT OF COLUMBIA REGISTER Vol.61 - No.21 May 16, 2014"; issue file postback; category links IssueCategoryList.aspx?CategoryID=…&IssueID=493 |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments | WF | PROVENANCE_REQUIRED |
| WS "dccourts.gov court of appeals opinions memorandum opinion and judgment search" | WS | listing ?page=47, ?page=107, node/1870 pages |
| https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments?page=47 | WF | listing Nov 2019–Jan 2020; "only lists online the names and case numbers of MOJs"; no hrefs |
| https://dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments?page=107 | WF | columns Appeal Number, Case, Date, Disposition, Judge; no hyperlinks |
| WS (several, incl. "matters-docs") | WS | /node/NNNNN pages; no opinion PDFs |
| https://www.dccourts.gov/node/16643 | WF | partial record (Upchurch v. DOES), no PDF link, no body |
| WS "This opinion is subject to formal revision … dccourts.gov" | WS | /sites/default/files/2018-12/14-CV-101.pdf |
| https://www.dccourts.gov/sites/default/files/2018-12/14-CV-101.pdf | WF | YES "These appeals present us with legal issues of first impression"; 150 A.3d 1213 noted; truncated at 100,000/116,785 |
| WS (extended) "site:dccourts.gov opinions … sites/default/files" | WS | listing URL with combine/field_date_value/field_date_value_1/field_type_value/order/sort/page params |
| …opinions-memorandum-of-judgments?combine=&…&page=7&sort=desc | WF | CLIENT_ERROR |
| WS "dccourts.gov sites default files 2026 …" | WS | calendars; SCOTUS 25-248 mandate PDF |
| WS (extended) "… 23-CV OR 24-CV OR 23-CF pdf" | WS | /sites/default/files/2026-05/Greer v US 23-CF-389.pdf; listing page=186 URL |
| https://www.dccourts.gov/sites/default/files/2026-05/Greer%20v%20US%2023-CF-389.pdf | WF | CLIENT_ERROR; second attempt blocked by the tool (recent failure) |
| https://www.dccourts.gov/index.php/court-of-appeals/opinions-memorandum-of-judgments?…page=186… | WF | CLIENT_ERROR |
| WS "dccourts.gov opinions-memorandum-of-judgments field_type_value opinion" | WS | ?field_type_value=All&page=69&order=field_date&sort=desc |
| that URL | WF | CLIENT_ERROR |
| https://newsroom.dccourts.gov/press-releases/dc-court-of-appeals-to-pilot-online-access-to-documents | WF | Nov. 10, 2020 release; briefs pilot only (not opinions) |
| https://law.justia.com/cases/district-of-columbia/ | WF | only "District of Columbia Court of Appeals Decisions" linked |
| https://law.justia.com/cases/district-of-columbia/court-of-appeals/ | WF | years 1923–2026 |
| …/court-of-appeals/2026/ | WF | newest rows Aug. 13, 2026; slugs = lower-case docket (24-cf-0191), suffixes -0/-1 |
| …/court-of-appeals/2026/24-cf-0191.html | WF | YES "Marquette Jordan was convicted of second-degree murder and two related"; complete; PDF at cases.justia.com |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.supremecourt.gov/docket/docketfiles/html/public/25-248.html | script | 15,277 chars; "Lower Ct: District of Columbia Court of Appeals"; "(23-FS-0589)"; Apr 20 2026 "Petition GRANTED. Judgment REVERSED and case REMANDED" |
| DCCA en banc orders | — | no list located; Rules 35/40 read in DCCA rules PDF |

## Notes
- WebFetch on dccourts.gov worked for 5 URLs, then returned CLIENT_ERROR on 5 (not a quota message, not a site refusal text). Recorded as intermittent; not retried beyond one attempt.
- No URL was fetched by any route after a refusal.

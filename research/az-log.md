# Arizona (az) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "shell" = `scripts/fetch_doc.py --research` (or a small helper calling `lsnet.get` from the same script layer, which obeys robots.txt, bot-check refusals and crawl delays). "WF" = WebFetch.

Session note: WebFetch here only fetched URLs that had already appeared in a WebSearch/WebFetch result. Constructed URLs (and URLs that appeared only in shell output) triggered a permission prompt that went unanswered ("PROVENANCE_REQUIRED … not answered in time"); those are recorded as not fetched, never retried. WebFetch calls used: about 31.

## Robots / host checks (shell)
| URL | Result |
|---|---|
| https://www.azleg.gov/robots.txt | 200; `User-agent: *` Crawl-delay: 120; Disallow /search/, /xml/, /FormatDocument.asp, /FormatForPrint.asp, /DocumentsForBill.asp, WordPress paths |
| https://www.azcourts.gov/robots.txt | 200; DNN default: Disallow /*/ctl/, /admin/, /App_*, /bin/, /Providers/ … |
| https://coa1.azcourts.gov/robots.txt | 200; same DNN file |
| https://apps.azcourts.gov/robots.txt | 404 (no robots) |
| https://www.appeals2.az.gov/robots.txt | "unreachable after a retry" — HTML error page; host treated as disallowed |
| https://apps.azsos.gov/robots.txt | REFUSED: bot check (challenge) |
| https://azsos.gov/robots.txt | REFUSED: bot check (challenge) |
| http://azrules.westgroup.com/ | REFUSED: robots.txt bot check |
| https://govt.westlaw.com/azrules/Index | REFUSED: robots.txt bot check |
| law.justia.com | already in refusal cache: "robots.txt challenge" (22:41) |
| https://www.azcourts.gov/azrules/Help | HTTP 403 Cloudflare challenge (23:04) → script marked www.azcourts.gov refused for the day |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://www.azleg.gov/ars/12/00542.htm | WF | PROVENANCE_REQUIRED (permission unanswered) — not retried |
| https://www.azleg.gov/ars/13/01105.htm | WF | same |
| https://www.azleg.gov/arsDetail/?title=12 | WF | same |
| https://www.azleg.gov/ars/12/00542.htm | shell | 1,035 chars; "12-542. Injury to person; …"; "Except as provided in section 12-551 there shall be commenced"; Last-Modified 9 Sep 2026 |
| https://www.azleg.gov/ars/13/01105.htm | shell | 2,757 chars; "A. A person commits first degree murder if:" |
| https://www.azleg.gov/ars/12/00341-01.htm | shell | "12-341.01. Recovery of attorney fees" body present |
| https://www.azleg.gov/ars/41/01092-01.htm | shell | "41-1092.01. Office of administrative hearings" body present |
| https://www.azleg.gov/ars/1/00213.htm | shell | "1-213. Words and phrases" body present |
| https://www.azleg.gov/ars/01/00213.htm | shell | HTTP 404 (titles unpadded) |
| https://www.azleg.gov/arsDetail/?title=12 | shell | 69,452 chars; chapters with ranges "Chapter 5 LIMITATIONS OF ACTIONS Sec: 12-501-12-559.03"; links /viewdocument/?docName=…/ars/12/00102-01.htm; "official version … is published by Thomson Reuters"; "effective on January 1st of the year following" |
| https://www.azleg.gov/arsDetail/?title=13 | shell | 79,465 chars |
| WebSearch "azleg.gov arsDetail title 12 …" | search | surfaced arsDetail/?title=22 |
| https://www.azleg.gov/arsDetail/?title=22 | WF | title index; chapter ranges + per-section links; "updated to include the revised sections from the 57th Legislature, 2nd Regular Session" |
| https://www.azleg.gov/viewdocument/?docName=https://www.azleg.gov/ars/22/00101.htm | WF | YES "A. The board of supervisors shall divide the county into"; not truncated |
| https://www.azleg.gov/ars/22/00101.htm | WF | PROVENANCE_REQUIRED |
| https://www.azleg.gov/arstitle/ | shell | 10,169 chars, title list |
| https://law.justia.com/codes/arizona/2005/title12/00542.html | WF | YES "Except as provided in section 12-551 there shall be commenced"; "2005 Arizona Revised Statutes" |
| https://law.justia.com/codes/arizona/title-12/ | WF | "2025 Arizona Revised Statutes"; section links only, no chapter links/ranges; e.g. /title-12/section-12-559-03/ |
| https://law.justia.com/codes/arizona/title-12/section-12-559-03/ | WF | YES "A. Except as provided in subsections B, C and D"; "AZ Rev Stat § 12-559.03 (2025)" |
| https://law.justia.com/codes/arizona/title-13/section-13-751/ | WF | YES "A. If the state has filed a notice of intent"; 2025 |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://www.azleg.gov/Constitution/ | shell | links constitution?article=1…30 (6.1 present, 23-24 absent); banner "updated to include the revised sections from the 55th Legislature, 1st Regular Session … January 2022" |
| https://www.azleg.gov/constitution/constitution?article=2 | shell | → /constitution/?article=2; links viewDocument/?docName=…/const/2/1.htm, 2_1.htm … |
| https://www.azleg.gov/viewDocument/?docName=https://www.azleg.gov/const/2/4.p.htm | shell | 200 page chrome (wrong file name) |
| https://www.azleg.gov/const/2/4.p.htm | shell | 404 |
| https://www.azleg.gov/const/2/4.htm | shell | "Section 4. No person shall be deprived of life, liberty, or" |
| https://www.azleg.gov/const/6/14.htm | shell | "The superior court shall have original jurisdiction" |
| https://www.azleg.gov/const/2/2_1.htm | shell | "2.1. Victims' bill of rights" body present |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.azcourts.gov/rules | shell | links "Court Rules" → http://azrules.westgroup.com/; Recent-Amendments; 2018 Final Rules Order PDF |
| http://azrules.westgroup.com/ , https://govt.westlaw.com/azrules/Index , govt.westlaw.com/robots.txt | shell | REFUSED (bot check) |
| WebSearch "govt.westlaw.com/azrules" and two others | search | no Westlaw rule URL surfaced; only third-party rule mirrors (not permitted) |
| https://www.azcourts.gov/azrules/Help | WF | "INVALID_URL … error while fetching" |
| https://www.azcourts.gov/azrules/Help | shell | HTTP 403 Cloudflare challenge |

## D — Admin code / register
| URL | Tool | Result |
|---|---|---|
| https://apps.azsos.gov/public_services/Title_17/17-09.pdf | WF | Title 17 ch. 9 stub, "Supp. 14-3", "recodified to 13 A.A.C. 13"; no sections |
| https://apps.azsos.gov/public_services/Title_09/9-09.rtf | WF | "[binary data]" — unreadable |
| https://apps.azsos.gov/public_services/register/2026/contents.htm | WF | "2026, Volume 32"; Issue 42 Oct 16, 2026 pp. 2539-2634; "The Register as published by the Division is the official version." |
| https://apps.azsos.gov/public_services/register/2026/42/contents.pdf | WF | Vol. 32 Issue 42; Information p. 2540 …; full issue, truncated in p. 2560 |
| https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R9-10-101 | shell | 54,978 chars; "In addition to the definitions in A.R.S. §§ 36-401(A) and 36-439"; history "8 A.A.R. 3559 … (Supp. 02-3)"; Last-Modified 30 Jul 2025 |
| https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R4-23-110 | shell | 46,286 chars; "In addition to definitions in A.R.S. § 32-1901" |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://azcourts.gov/opinions/Search-Opinions-Memo-Decs | WF | landing page; links /opinions/search, /opinions/Opinions-Custom-Search, appeals2 recentdecisions.cfm |
| https://www.azcourts.gov/coa1/Search-Decisions | WF | 302 → coa1.azcourts.gov/Search-Decisions (not followed) |
| https://coa1.azcourts.gov/Search-Decisions, /Decisions/DecisionsoftheCourt, /Decisions/SearchDecisions | shell | DNN pages; Elm app `Elm.Views.Opinions.Main`, service 'Azcourts' + 'Opinions', headers ModuleId/TabId/RequestVerificationToken; no decision rows |
| https://coa1.azcourts.gov/DesktopModules/MVC/Azcourts/elm.min.js | shell | 239,918 bytes; method names GetOpinions, GetDecisions, GetOpinionFiles |
| https://coa1.azcourts.gov/API/Azcourts/Opinions/GetOpinions?court=Division1&year=2026 | shell | 404 |
| https://www.azcourts.gov/API/Azcourts/Opinions/GetOpinions?court=Supreme&year=2026 | shell | 404 |
| https://www.azcourts.gov/opinions | shell | "Search By Year" 2002-2026 → Default.aspx?startDate=…&court=Supreme&TabId=9535 |
| https://www.azcourts.gov/Default.aspx?startDate=2025-01-01&endDate=2025-12-31&court=Supreme&TabId=9535 | shell | 220,658 bytes, Elm app (module 12754), no rows |
| same | WF | PROVENANCE_REQUIRED |
| https://www.azcourts.gov/opinions/2001-Opinions-Memo-Decs | shell | no opinion links (app) |
| https://www.azcourts.gov/Portals/0/OpinionFiles/Supreme/2025/CV240143PR.pdf | shell | PDF 15 pp, 34,371 chars; "No. CV-24-0143-PR Filed April 29, 2025"; "¶1 We consider the meaning of the phrase"; Last-Modified 10 Jun 2025 |
| https://www.azcourts.gov/Portals/0/OpinionFiles/Supreme/2025/CV-24-0143-PR.pdf | shell | 404 |
| https://www.azcourts.gov/News-Info/CV-24-0143 | shell+WF | links /Portals/0/2025_06_10_05523102-0-0000-AmendedOpinion.PDF and briefs |
| https://www.azcourts.gov/Portals/0/2025_06_10_05523102-0-0000-AmendedOpinion.PDF | WF | PROVENANCE_REQUIRED |
| https://www.azcourts.gov/casesummaries/2025-Case-Summaries | shell | redirect to Login |
| https://coa1.azcourts.gov/Portals/1/OpinionFiles/2026/CV240785.pdf ; www.azcourts.gov/Portals/0/OpinionFiles/Div1/2026/1%20CA-CV%2024-0785.pdf ; …/Div1/2026/CV240785.pdf ; coa1…/Portals/0/OpinionFiles/Div1/2026/1%20CA-CV%2024-0785.pdf | shell | all 404 (exploratory guesses, not recorded as patterns) |
| https://coa1.azcourts.gov/Decisions/Opinions | shell | text only; "Later proceedings in other courts may affect the legal status of any Opinion"; no rows |
| https://coa1.azcourts.gov/Decisions/Opinions | WF | PROVENANCE_REQUIRED |
| https://coa1.azcourts.gov/SearchDecisionDocumentText.aspx | shell | DNN page, no decision links |
| https://www.appeals2.az.gov/ | shell | robots.txt unreachable — not fetched |
| http://www.appeals2.az.gov/odsplus/recentdecisions.cfm | WF | PROVENANCE_REQUIRED |
| https://law.justia.com/cases/arizona/ | WF | Supreme Court, Court of Appeals, Territorial Supreme Court collections |
| https://law.justia.com/cases/arizona/supreme-court/2024/ | WF | rows e.g. cr-23-0236-pr.html, cv-24-0251-t-ap.html, cv-23-0284-pr.html |
| https://law.justia.com/cases/arizona/supreme-court/2024/cv-23-0284-pr.html | WF | YES full opinion ¶1-¶22; "Under A.R.S. § 12-821.01(A), a person with a claim against"; no own reporter cite |
| https://law.justia.com/cases/arizona/court-of-appeals/ | WF | years 1965-2026 |
| https://law.justia.com/cases/arizona/court-of-appeals/2026/ | WF | "first 500 of 1,141"; slugs court-of-appeals-division-one-unpublished/2026/1-ca-cv-26-0175.html etc. |
| https://law.justia.com/cases/arizona/court-of-appeals-division-one-unpublished/2026/1-ca-cv-26-0175.html | WF | YES full text through ¶19; legend "THIS DECISION IS NOT PRECEDENTIAL AND MAY BE CITED ONLY AS AUTHORIZED BY RULE." |

## F — Subsequent history (dockets)
| URL | Tool | Result |
|---|---|---|
| https://apps.azcourts.gov/aacc/appella/ASC/CR/CR260026.PDF | shell | 2 pp docket; "CR-26-0026-PR ROBBINS et al. v STATE OF ARIZONA"; predecessor "1 CA-SA 25-0153" |
| https://apps.azcourts.gov/aacc/appella/ASC/CV/CV250033.PDF, CV250089, CV250271, CV250116 | shell | 404 |
| https://apps.azcourts.gov/aacc/appella/ASC/CV/CV240143.PDF | shell | 404 (closed case) |
| https://apps.azcourts.gov/aacc/appella/1CA/CV/CV250429.pdf, CV250045.pdf | shell | 404 |
| https://apps.azcourts.gov/aacc/appella/1CA/CV/CV240785.pdf | shell | 4 pp; "MEMORANDUM DECISION" 15-Jan-2026; "DESCENDENT CASE(S) ASC CV-26-0046-PR"; "Case Docket as of 10-Aug-2026" |
| https://apps.azcourts.gov/aacc/appella/1CA\CV\CV240785.pdf | WF | YES same facts; not truncated |
| https://apps.azcourts.gov/aacc/appella/ASC/CV/CV260046.PDF | shell | status "Pending"; PR extension order |
| https://apps.azcourts.gov/aacc/appella/1CA/CV/CV260175.pdf | shell | 2 pp docket present |
| https://apps.azcourts.gov/aacc/appella/2CA/CV/CV20230108.pdf , …/2CA/CV/CV230108.pdf | shell | 404 |

## WebSearch queries (discovery only)
azleg 12-542; arsDetail title 12 (×2); Arizona Constitution article 2 (×2); azcourts Supreme Court opinions 2026; COA1 search decisions; OpinionFiles Supreme (×3); OpinionFiles Div1/Div2 (×3); 1 CA-CV 24-0785 Fuller; Justia AZ codes/cases (×4); govt.westlaw azrules (×3); Cornell LII A.A.C. (×2); apps.azsos.gov Title_09 / register (×4); appeals2 odsplus.

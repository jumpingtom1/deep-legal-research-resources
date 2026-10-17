# Maryland (md) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "script" = `python3 scripts/fetch_doc.py --research` (obeys robots.txt and bot checks); "WF" = WebFetch; "WS" = WebSearch. WebFetch calls used: 10 (2 gated, 1 rate-limited). WebFetch was stopped after an HTTP 429 per the brief, so several rows carry `webfetch: untested`.

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://mgaleg.maryland.gov/robots.txt | script | HTTP 404 (no robots file) |
| https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcj&section=5-101&enactments=false | script | 200 html 8,433 chars; "§5–101. A civil action at law shall be filed within three years" (en dash in heading) |
| same URL | WF | PROVENANCE_REQUIRED (permission prompt unanswered) → `gated` |
| …StatuteText?article=gcj&section=5-101&enactments=true | script | verify: VERIFIED exact (dash-normalised) |
| …StatuteText?article=gcr&section=2-201 | script | "(a) A murder is in the first degree if it is" |
| …StatuteText?article=grp&section=8-401 | script | 27,722 chars; "(a) Whenever the tenant or tenants fail to pay the rent" |
| …StatuteText?article=gcp&section=4-101 | script | "§4–101. (a) (1) In this section the following words" |
| …StatuteText?article=gcj&section=3-2A-04 | script | "§3–2A–04. (a) (1) (i) A person having a claim against" |
| …StatuteText?article=gcj&section=5-1010 | script | 200, heading "File Not Found" (no 404) |
| …StatuteText?article=gsg&section=10-1601 / 10-1602 | script | UELMA definitions: Code, Constitution official publisher = DLS; applies only to material "designated as official" |
| …StatuteText?article=ghg&section=4-301&enactments=true | script | verify VERIFIED "In this subtitle the following words have the meanings indicated" |
| https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes | script | 13,902 chars; article code table (gag … gtr, c0 … c20); "Show statutes in effect as of October 1st of this year" |
| https://mgaleg.maryland.gov/2026RS/Statute_Web/gcj/5-101.pdf | script | pdf 1 p, 360 chars, Last-Modified 20 Dec 2025 |
| https://mgaleg.maryland.gov/2026RS/Statute_Web/gcj/gcj.pdf | script | pdf 809 pp, 1,713,394 chars |
| https://mgaleg.maryland.gov/2027RS/Statute_Web/gcj/5-101.pdf | script | pdf 1 p, Last-Modified 01 Sep 2026 |
| https://mgaleg.maryland.gov/2027RS/Statute_Web/gcj/gcj.pdf | script | pdf 818 pp, 1,728,658 chars, Last-Modified 01 Sep 2026 |
| https://mgaleg.maryland.gov/2025RS/Statute_Web/gcj/5-101.pdf | script | pdf 1 p, Last-Modified 03 Jan 2025 |
| https://mgaleg.maryland.gov/2027RS/Statute_Web/grp/8-401.pdf; 2026RS same | script | 9 pp each; Last-Modified 24 Sep 2026 / 19 Dec 2025 |
| WS "mgaleg.maryland.gov StatuteText article gcj section 5-101" | WS | no StatuteText URL surfaced |
| WS "law.justia.com codes maryland courts-and-judicial-proceedings 5-101 2024" | WS | surfaced law.justia.com/codes/maryland/2024 and 2024RS gcj.pdf |
| https://law.justia.com/codes/maryland/2024 | WF | links …/2024/courts-and-judicial-proceedings/ etc.; "2024 Maryland Code"; editions 2023-2025 |
| https://law.justia.com/codes/maryland/courts-and-judicial-proceedings/title-5/subtitle-1/section-5-101/ | WF | YES "A civil action at law shall be filed within three"; "2025 Maryland Code" |
| https://law.justia.com/codes/maryland/real-property/title-8/subtitle-4/section-8-401/ | WF | YES "(a) Whenever the tenant or tenants fail to pay the"; "2025 Maryland Statutes" |
| law.justia.com (check) | script | REFUSED: robots.txt answered with a bot check |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.mdcourts.gov/robots.txt | script | 200; `User-agent: *` disallows /core/, /profiles/, /admin/, /search/, /user/*, README files |
| https://www.mdcourts.gov/opinions/opinions | script | 10,132 chars; renaming note (Dec. 14, 2022); UELMA "official and authentic" for postings on/after July 1, 2018; year radio 1995-2026 |
| https://www.mdcourts.gov/cgi-bin/indexlist.pl?court=coa&year=2024&order=bydate&submit=Submit | script | 200 GET works; "2024 Index Listing of Supreme Court of Maryland Opinions"; rows link /data/opinions/coa/2024/5a24.pdf etc. |
| https://www.mdcourts.gov/data/opinions/coa/2024/1a24.pdf | script | 404 (guess; no such file) |
| https://www.mdcourts.gov/data/opinions/coa/2024/5a24.pdf | script | pdf 23 pp; "Isiah A. Hollins v. State of Maryland, No. 5, September Term, 2024"; UELMA authentication line; no "489 Md." |
| https://www.mdcourts.gov/data/opinions/coa/2024/7a23.pdf | script | pdf 187 pp, 375,727 chars; "Adnan Syed v. Young Lee … No. 7, September Term, 2023" |
| …indexlist.pl?court=cosa&year=2025… | script | rows link /data/opinions/cosa/2025/1991s23.pdf, "slip.op" |
| https://www.mdcourts.gov/data/opinions/cosa/2025/1991s23.pdf | script | pdf 17 pp; "Midaro Investments 2021, LLC v. Ari Gerzowski, et al., Nos. 1991 and 1992" |
| …indexlist.pl?court=coa&year=1995… | script | "1995 Index Listing"; rows with 341 Md. cites; /data/opinions/coa/1995/34a95.pdf |
| …indexlist.pl?court=cosa&year=2016… | script | rows with "231 Md.App. 398" etc. |
| https://www.mdcourts.gov/appellate/unreportedopinions | script | 10,579 chars; "Unreported opinions filed from May 1, 2015 to present are available" |
| …/appellate/unreportedopinions/list/202609 | script | rows "09-30-2026 2330 24 Blomquist Farmer, Maurice State"; links /sites/default/files/unreported-opinions/2330s24.pdf |
| …/list/202001, 202301, 202401, 202501 | script | links /sites/default/files/unreported-opinions/{NNNN}s{TT}.pdf |
| …/list/201605 | script | links /sites/default/files/unreported-opinions/2016/1063s15.pdf (year folder) |
| https://www.mdcourts.gov/sites/default/files/unreported-opinions/2330s24.pdf | script | pdf 15 pp; "UNREPORTED* IN THE APPELLATE COURT OF MARYLAND No. 2330" |
| https://www.mdcourts.gov/appellate | script | 404 |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.mdcourts.gov/scm (and /coappeals → redirects to /scm) | script | link "Certiorari Petitions" → /scm/petitions |
| https://www.mdcourts.gov/scm/petitions | script | month links 202301-202609; "Archive of Petitions for Writ of Certiorari granted and denied, 2003-2022" |
| https://www.mdcourts.gov/scm/petitions/202609petitions | script | "Denied/Dismissed September 16, 2026 Manson v. Britto - Pet. No. 207"; grants with No. N, Sept. Term 2026 |
| https://www.mdcourts.gov/scm/petitions/200801petitions | script | 404 (guess) |
| https://www.mdcourts.gov/scm/petitionsarchive | script | month links mix /scm/petitions/ and /coappeals/petitions/ |
| https://www.mdcourts.gov/coappeals/petitions/201010petitions | script | 15,457 chars; "Granted October 25, 2010 State of Maryland v. Anissa Maddox" |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.mdcourts.gov/rules | script | "The Maryland Rules are available through Westlaw."; link govt.westlaw.com/mdc/Index… |
| https://www.mdcourts.gov/rules/rulesorders | script | 404 |
| https://govt.westlaw.com/mdc/Index?transitionType=Default&contextData=%28sc.Default%29 | script | REFUSED: host refused earlier (robots.txt challenge) |
| https://govt.westlaw.com/mdc/Index?bhcp=1&transitionType=Default&contextData=(sc.Default) | WF | PROVENANCE_REQUIRED; not retried |
| https://www.mdcourts.gov/rules/ruleschanges | script | "228th Report … Rules Order 06/04/2026"; links /sites/default/files/rules/order/ro227th.pdf etc. |
| https://www.mdcourts.gov/sites/default/files/rules/order/ro227th.pdf | script | pdf 173 pp, 226,155 chars; "IN THE SUPREME COURT OF MARYLAND RULES ORDER" |
| WS '"Maryland Rules" "Rule 2-322" … site:law.cornell.edu OR law.justia.com OR public.law' | WS | only non-vetted third parties and mdcourts rules-order PDFs; no tier-2 copy |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| …StatuteText?article=c0&section=24&enactments=false | script | "Article - Declaration of Rights … §24. That no man ought to be taken" |
| …StatuteText?article=c4&section=14&enactments=false | script | "§14. The Supreme Court of Maryland shall be composed of seven justices" |
| WS "law.justia.com constitution maryland declaration of rights article 24" | WS | surfaced justia 00dec.html, msa 00dec.html, mgaleg 2024RS c0.pdf |
| https://law.justia.com/constitution/maryland/00dec.html | WF | YES Art. 24; "This Constitution may not be the most recent version."; last article 47 |
| https://www.msa.maryland.gov/msa/mdmanual/43const/html/00dec.html | WF | YES Art. 24; "with Amendments through Two Thousand and Twenty-Four"; through Art. 48 |
| https://msa.maryland.gov/msa/mdmanual/43const/html/00dec.html, 04art4.html, const.html | script | 200 (22,611 bytes for 00dec) but extracted chars=0 |
| https://mgaleg.maryland.gov/2024RS/Statute_Web/c0/c0.pdf | WF | YES Art. 24; Art. 48 "NOT IN EFFECT ** SUBJECT TO REFERENDUM NOVEMBER 2024"; complete |
| https://mgaleg.maryland.gov/2027RS/Statute_Web/c0/c0.pdf | script | pdf 9 pp, Last-Modified 31 Aug 2026 |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://dsd.maryland.gov/regulations/Pages/26.08.02.03.aspx | script | redirected to https://regs.maryland.gov/us/md/exec/comar/26.08.02.03 |
| https://regs.maryland.gov/us/md/exec/comar/26.08.02.03 | script | 4,088 chars; ".03 Surface Water Quality Criteria. A. Applicability."; "Please do not scrape. Instead, bulk download" |
| https://regs.maryland.gov/ | script | "is current as of October 12, 2026"; "The text appearing here is not the official text"; GitHub bulk links |
| https://regs.maryland.gov/robots.txt | script | `User-agent: *` Disallow `/_*`; meta-externalagent disallowed |
| https://dsd.maryland.gov/robots.txt | script | Disallow /_vti_bin/, /_layouts/, /_catalogs/ |
| https://regs.maryland.gov/us/md/exec/comar/13A.03.02.01 | script | ".01 Scope. A. This chapter sets out the enrollment, credit" |
| https://regs.maryland.gov/us/md/exec/comar/10.09.10.01 | script | ".01 Definitions." 17,517 chars |
| https://regs.maryland.gov/us/md/exec/comar/26.08.02 | script | chapter TOC |
| https://regs.maryland.gov/us/md/exec/comar/26.08.02.03-2 | script | 173,427 chars |
| https://regs.maryland.gov/us/md/exec/register, /53, /53/20 | script | Vol. 52-53 listed; issue page: "Register publishing was not yet supported"; /53/53-20.pdf → 404 |
| https://dsd.maryland.gov/Pages/MDRegister.aspx | script | "The 15 most current issues are available for free"; links /MDRIssues/5307 … /5321/Assembled.aspx |
| https://dsd.maryland.gov/MDRIssues/5320/Assembled.aspx | script | 292,854 chars; "Volume 53 • Issue 20 • Pages 975 — 1030"; page numbers only in TOC |
| https://dsd.maryland.gov/MDRIssues/5306, 5301, 5110, 5021, 5101/Assembled.aspx | script | 404 |
| WS "regs.maryland.gov us/md/exec/comar …" | WS | surfaced LII chapter page and old MDRIssues URLs; no regs.maryland.gov URL |
| https://www.law.cornell.edu/regulations/maryland/COMAR-26-08-02-03 | script | body present; Notes "(31:13 Md. R. 995)"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/maryland/title-08/subtitle-03/chapter-08.03.01 | WF | TOC only; link /COMAR-08-03-01-01; "updated quarterly" |
| https://www.law.cornell.edu/regulations/maryland/COMAR-08-03-01-01 | WF | PROXY_REJECTED HTTP 429 (rate limited) → WebFetch stopped for the rest of the run |

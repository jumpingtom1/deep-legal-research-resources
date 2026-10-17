# New York (NY) — free legal sources

_Generated from `data/ny.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and the Constitution: NY Senate Open Legislation (nysenate.gov/legislation/laws/{LAWID}/{section}) is constructible, returns full section text to both WebFetch and shell, and shows a per-section revision date. It carries no official-status statement, and New York has no official online code. public.law and Justia (2025 edition) are tier-2 fallbacks. Case law: the Law Reporting Bureau slip-opinion reporter (nycourts.gov/reporter, coverage from 2003) is constructible from the NY Slip Op cite. Its corrected pages carry the official [AD3d/NY3d/Misc 3d] cite and *n page markers, and monthly listing pages give docket numbers. Court of Appeals leave dispositions are published as NY Slip Op 6xxxx-8xxxx motion decisions. Gaps: the Official Reports and the official NYCRR are on govt.westlaw.com (SITE_BLOCKED), so the NYCRR falls to Cornell LII. www.nycourts.gov, law.justia.com and iapps return a Cloudflare challenge to the shell, but WebFetch works on nycourts.gov.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| New York Court of Appeals | `ny (unverified)` | N.Y. | NY3d, NY2d, NY, N.E.3d, N.E.2d, N.Y.S.3d, N.Y.S.2d | YYYY NY Slip Op NNNNN (decisions 0xxxx; motions 6xxxx-8xxxx) |
| Supreme Court, Appellate Division (1st-4th Departments) | `nyappdiv (unverified)` | N.Y. App. Div. | AD3d, AD2d, AD, N.Y.S.3d, N.Y.S.2d | YYYY NY Slip Op NNNNN |
| Supreme Court, Appellate Term (1st, 2d Departments) | `nyappterm (unverified)` | N.Y. App. Term | Misc 3d, Misc 2d, N.Y.S.3d | YYYY NY Slip Op NNNNN or NNNNN(U) |
| Supreme Court (trial level, incl. Commercial Division) | `nysupct (unverified)` | N.Y. Sup. Ct. | Misc 3d, Misc 2d, N.Y.S.3d | YYYY NY Slip Op 5NNNN(U) (unreported, Misc 3d table cite NNNN(A)); 3NNNN(U) (eCourts-sourced, not selected for publication) |
| Other trial courts (Civil, Criminal, Family, Surrogate's, Court of Claims, City/District/Justice) | `nycivct | nycrimct | nyfamct | nysurct | nyclaimsct (unverified)` | N.Y. Civ. Ct. / N.Y. Crim. Ct. / N.Y. Fam. Ct. / N.Y. Sur. Ct. / N.Y. Ct. Cl. | Misc 3d, N.Y.S.3d | YYYY NY Slip Op NNNNN |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Consolidated Laws (Bluebook and NY Official style) | `N.Y. Gen. Oblig. Law § 5-701`; `General Obligations Law § 5-701`; `Penal Law § 155.05`; `Executive Law § 296`; `N.Y. Bus. Corp. Law § 626`; `Labor Law § 240(1)`; `section 1192 of the Vehicle and Traffic Law`; `Real Property Law § 235-b`; `N.Y. Real Prop. Law § 235-b` | `ny-laws-senate` → `ny-laws-publiclaw` → `ny-laws-justia` |
| CPLR (statute; law ID CVP) | `CPLR 3211(a)(7)`; `N.Y. C.P.L.R. 3211(a)(7)`; `CPLR R 3211`; `N.Y. C.P.L.R. 213 (McKinney)` | `ny-laws-senate` → `ny-laws-publiclaw` → `ny-laws-justia` |
| Court acts and short-form law names (CPL, RPAPL, EPTL, BCL, GOL, VTL, DRL, Fam. Ct. Act, SCPA …) | `CPL 440.10`; `N.Y. Crim. Proc. Law § 30.30`; `Family Ct Act § 1012`; `SCPA 2103`; `N.Y.C. Civ. Ct. Act § 202`; `RPAPL 1304`; `EPTL 5-1.1-A`; `N.Y. Fam. Ct. Act § 1028` | `ny-laws-senate` → `ny-laws-publiclaw` |
| New York Constitution | `N.Y. Const. art. I, § 11`; `NY Const, art I, § 6` | `ny-const-senate` → `ny-const-dos` |
| Court rules in 22 NYCRR (Uniform Rules, Court of Appeals, Appellate Division, Rules of Professional Conduct) | `22 NYCRR 202.8-g`; `22 N.Y.C.R.R. § 202.7`; `22 NYCRR 500.22`; `22 NYCRR 1250.1`; `Rules of Professional Conduct (22 NYCRR 1200.0) rule 1.7` | `ny-rules-ucr-nycourts` → `ny-rules-coa-500` → `ny-rules-rpc-1200` → `ny-nycrr-cornell` |
| NYCRR (agency regulations) | `12 NYCRR 23-1.7`; `12 N.Y.C.R.R. § 23-1.7(d)` | `ny-nycrr-cornell` |
| Public-domain slip opinion citation | `2023 NY Slip Op 04822`; `2024 NY Slip Op 50001(U)`; `2024 NY Slip Op 74436` | `ny-cases-lrb` → `ny-history-lrb-motions` → `ny-cases-justia` |
| Official Reports (NY Official style and Bluebook) | `40 NY3d 405`; `219 AD3d 1251`; `81 Misc 3d 1223(A)`; `40 N.Y.3d 405 (2023)`; `219 A.D.3d 1251 (1st Dep't 2023)` | `ny-cases-lrb` → `ny-cases-ctapps` → `ny-cases-justia` |
| Regional / West reporters | `196 N.Y.S.3d 1` | `ny-cases-lrb` → `ny-cases-justia` |
| Regional reporter N.E. (no court parenthetical) *(only once this jurisdiction is known)* | `216 N.E.3d 1` | `ny-cases-lrb` → `ny-cases-justia` |

Regexes (case-insensitive):

- Consolidated Laws (Bluebook and NY Official style): `(?<![A-Za-z])(?<!Ann\.,\s)(?<!Ann\.\s)(?<!Code\s)(?<![A-Z][a-z]\.\s)(?<![A-Z][a-z]{2}\.\s)(?<![A-Z][a-z]{3}\.\s)(?<![A-Z][a-z]{4}\.\s)(?:N\.?\s?Y\.?\s+)?(?P<law>Parks,\s+Recreation\s+(?:and|&)\s+Historic\s+Preservation|Racing,\s+Pari\-Mutuel\s+Wagering\s+(?:and|&)\s+Breeding|Soil\s+(?:and|&)\s+Water\s+Conservation\s+Districts|Real\s+Property\s+Actions\s+(?:and|&)\s+Proceedings|Volunteer\s+Ambulance\s+Workers'\s+Benefit|State\s+Administrative\s+Procedure\s+Act|Volunteer\s+Firefighters'\s+Benefit|Retirement\s+(?:and|&)\s+Social\s+Security|Alternative\s+County\s+Government|Printing\s+(?:and|&)\s+Public\s+Documents|Municipal\s+Housing\s+Authorities|Civil\s+Practice\s+Law\s+(?:and|&)\s+Rules|Statute\s+of\s+Local\s+Governments|Transportation\s+Corporations|Not\-for\-Profit\s+Corporation|Alcoholic\s+Beverage\s+Control|Estates,\s+Powers\s+(?:and|&)\s+Trusts|Rural\s+Electric\s+Cooperative|Environmental\s+Conservation|Limited\s+Liability\s+Company|Arts\s+(?:and|&)\s+Cultural\s+Affairs|Cooperative\s+Corporations|Eminent\s+Domain\s+Procedure|Agriculture\s+(?:and|&)\s+Markets|Private\s+Housing\s+Finance|Uniform\s+Commercial\s+Code|Religious\s+Corporations|Senate/Assembly\s+Rules|Workers'\s+Compensation|General\s+Construction|Est\.\s+Powers\s+\&\s+Trusts|General\s+Associations|Employers'\s+Liability|Business\s+Corporation|Economic\s+Development|Not\-for\-Profit\s+Corp\.|Vehicle\s+(?:and|&)\s+Traffic|Municipal\s+Home\s+Rule|General\s+Obligations|Second\s+Class\s+Cities|Debtor\s+(?:and|&)\s+Creditor|Criminal\s+Procedure|Financial\s+Services|Abandoned\s+Property|Public\s+Authorities|Domestic\s+Relations|Veterans'\s+Services|Multiple\s+Residence|Real\s+Property\s+Tax|Multiple\s+Dwelling|General\s+Municipal|Benevolent\s+Orders|Personal\s+Property|Real\s+Prop\.\s+Acts\.|General\s+Business|Public\s+Buildings|Alco\.\s+Bev\.\s+Cont\.|State\s+Technology|Public\s+Officers|Social\s+Services|Envtl\.\s+Conserv\.|Mental\s+Hygiene|Workers'\s+Comp\.|Ltd\.\s+Liab\.\s+Co\.|Public\s+Housing|Transportation|Real\s+Prop\.\s+Tax|Public\s+Service|Local\s+Finance|Rapid\s+Transit|Debt\.\s+\&\s+Cred\.|Real\s+Property|Civil\s+Service|State\s+Finance|Public\s+Health|Veh\.\s+\&\s+Traf\.|Public\s+Lands|Mult\.\s+Dwell\.|Constitution|Civil\s+Rights|General\s+City|Gen\.\s+Oblig\.|Civ\.\s+Rights|Mental\s+Hyg\.|Partnership|Crim\.\s+Proc\.|Pub\.\s+Health|Legislative|Civ\.\s+Serv\.|Bus\.\s+Corp\.|Fin\.\s+Serv\.|Soc\.\s+Serv\.|State\s+Fin\.|Navigation|Correction|Real\s+Prop\.|Insurance|Pub\.\s+Off\.|Education|Gen\.\s+Mun\.|Gen\.\s+Bus\.|Judiciary|Executive|Dom\.\s+Rel\.|Cannabis|Military|Election|Railroad|Village|Highway|Banking|Energy|Indian|P'ship|County|State|Elder|Canal|Exec\.|Labor|Elec\.|Educ\.|Penal|Ins\.|Lien|Town|Lab\.|Jud\.|Tax)\s+Law\s+(?:§+|sections?)\s*(?P<section>\d+[A-Za-z]?(?:[-.]\d+[A-Za-z]?)*)|(?:sec(?:tion|\.)s?|§§?)\s*(?P<section_p>\d+[A-Za-z]?(?:[-.]\d+[A-Za-z]?)*)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:New\s+York\s+)?(?P<law_p>Parks,\s+Recreation\s+(?:and|&)\s+Historic\s+Preservation|Racing,\s+Pari\-Mutuel\s+Wagering\s+(?:and|&)\s+Breeding|Soil\s+(?:and|&)\s+Water\s+Conservation\s+Districts|Real\s+Property\s+Actions\s+(?:and|&)\s+Proceedings|Volunteer\s+Ambulance\s+Workers'\s+Benefit|State\s+Administrative\s+Procedure\s+Act|Volunteer\s+Firefighters'\s+Benefit|Retirement\s+(?:and|&)\s+Social\s+Security|Alternative\s+County\s+Government|Printing\s+(?:and|&)\s+Public\s+Documents|Municipal\s+Housing\s+Authorities|Civil\s+Practice\s+Law\s+(?:and|&)\s+Rules|Statute\s+of\s+Local\s+Governments|Transportation\s+Corporations|Not\-for\-Profit\s+Corporation|Alcoholic\s+Beverage\s+Control|Estates,\s+Powers\s+(?:and|&)\s+Trusts|Rural\s+Electric\s+Cooperative|Environmental\s+Conservation|Limited\s+Liability\s+Company|Arts\s+(?:and|&)\s+Cultural\s+Affairs|Cooperative\s+Corporations|Eminent\s+Domain\s+Procedure|Agriculture\s+(?:and|&)\s+Markets|Private\s+Housing\s+Finance|Uniform\s+Commercial\s+Code|Religious\s+Corporations|Senate/Assembly\s+Rules|Workers'\s+Compensation|General\s+Construction|Est\.\s+Powers\s+\&\s+Trusts|General\s+Associations|Employers'\s+Liability|Business\s+Corporation|Economic\s+Development|Not\-for\-Profit\s+Corp\.|Vehicle\s+(?:and|&)\s+Traffic|Municipal\s+Home\s+Rule|General\s+Obligations|Second\s+Class\s+Cities|Debtor\s+(?:and|&)\s+Creditor|Criminal\s+Procedure|Financial\s+Services|Abandoned\s+Property|Public\s+Authorities|Domestic\s+Relations|Veterans'\s+Services|Multiple\s+Residence|Real\s+Property\s+Tax|Multiple\s+Dwelling|General\s+Municipal|Benevolent\s+Orders|Personal\s+Property|Real\s+Prop\.\s+Acts\.|General\s+Business|Public\s+Buildings|Alco\.\s+Bev\.\s+Cont\.|State\s+Technology|Public\s+Officers|Social\s+Services|Envtl\.\s+Conserv\.|Mental\s+Hygiene|Workers'\s+Comp\.|Ltd\.\s+Liab\.\s+Co\.|Public\s+Housing|Transportation|Real\s+Prop\.\s+Tax|Public\s+Service|Local\s+Finance|Rapid\s+Transit|Debt\.\s+\&\s+Cred\.|Real\s+Property|Civil\s+Service|State\s+Finance|Public\s+Health|Veh\.\s+\&\s+Traf\.|Public\s+Lands|Mult\.\s+Dwell\.|Constitution|Civil\s+Rights|General\s+City|Gen\.\s+Oblig\.|Civ\.\s+Rights|Mental\s+Hyg\.|Partnership|Crim\.\s+Proc\.|Pub\.\s+Health|Legislative|Civ\.\s+Serv\.|Bus\.\s+Corp\.|Fin\.\s+Serv\.|Soc\.\s+Serv\.|State\s+Fin\.|Navigation|Correction|Real\s+Prop\.|Insurance|Pub\.\s+Off\.|Education|Gen\.\s+Mun\.|Gen\.\s+Bus\.|Judiciary|Executive|Dom\.\s+Rel\.|Cannabis|Military|Election|Railroad|Village|Highway|Banking|Energy|Indian|P'ship|County|State|Elder|Canal|Exec\.|Labor|Elec\.|Educ\.|Penal|Ins\.|Lien|Town|Lab\.|Jud\.|Tax)\s+Law\b`
- CPLR (statute; law ID CVP): `(?:N\.Y\.\s+)?C\.?P\.?L\.?R\.?\s+(?:R(?:ule)?\.?\s+|§\s*)?(?P<section>\d{3,4}(?:-[a-z])?)`
- Court acts and short-form law names (CPL, RPAPL, EPTL, BCL, GOL, VTL, DRL, Fam. Ct. Act, SCPA …): `(?:N\.?\s?Y\.?\s+)?(?P<law>CPL|RPAPL|EPTL|BCL|GOL|VTL|DRL|RPTL|N-PCL|LLCL|Fam\.?\s+Ct\.?\s+Act|Crim\.?\s+Proc\.?\s+Law|Family\s+C(?:our)?t\.?\s+Act|SCPA|Surr\.?\s+Ct\.?\s+Proc\.?\s+Act|(?:N\.Y\.C\.\s+)?Civ\.?\s+Ct\.?\s+Act)\s+§?\s*(?P<section>\d+(?:[-.]\d+)*)`
- New York Constitution: `N\.?\s?Y\.?\s+Const\.?,?\s+art\.?\s+(?P<article>[IVXL]+|\d+),?\s+§\s*(?P<section>\d+(?:-[a-z])?)`
- Court rules in 22 NYCRR (Uniform Rules, Court of Appeals, Appellate Division, Rules of Professional Conduct): `22\s+N\.?\s?Y\.?\s?C\.?\s?R\.?\s?R\.?\s+(?:§\s*)?(?P<part>\d+)\.(?P<section>\d+(?:-[a-z])?)`
- NYCRR (agency regulations): `(?<!\d)(?P<title>(?!22\b)\d{1,2})\s+N\.?\s?Y\.?\s?C\.?\s?R\.?\s?R\.?\s+(?:§\s*)?(?P<section>[\d.\-a-z]+)`
- Public-domain slip opinion citation: `(?P<year>(?:19|20)\d{2})\s+N\.?\s?Y\.?\s+Slip\s+Op\.?\s+(?P<num>\d{5})(?P<u>\(U\))?`
- Official Reports (NY Official style and Bluebook): `(?P<vol>\d{1,3})\s+(?P<rep>N\.?Y\.?(?:2d|3d)?|A\.?D\.?(?:2d|3d)?|Misc\.?\s?(?:2d|3d)?)\s+(?P<page>\d{1,4})(?P<table>\(A\))?`
- Regional / West reporters: `(?P<vol>\d{1,3})\s+(?P<rep>N\.Y\.S\.(?:2d|3d)?)\s+(?P<page>\d{1,4})`
- Regional reporter N.E. (no court parenthetical): `(?P<vol>\d{1,3})\s+(?P<rep>N\.E\.(?:2d|3d)?)\s+(?P<page>\d{1,4})`

Short forms → URL key:

CPLR → `CVP`; Civ. Prac. L. & R. → `CVP`; CPL → `CPL`; Crim. Proc. Law → `CPL`; Penal Law → `PEN`; Penal → `PEN`; Gen. Oblig. Law → `GOB`; GOL → `GOB`; Gen. Bus. Law → `GBS`; GBL → `GBS`; Bus. Corp. Law → `BSC`; BCL → `BSC`; Ltd. Liab. Co. Law → `LLC`; LLCL → `LLC`; Not-for-Profit Corp. Law → `NPC`; N-PCL → `NPC`; P'ship Law → `PTR`; Partnership Law → `PTR`; Veh. & Traf. Law → `VAT`; VTL → `VAT`; Lab. Law → `LAB`; Labor Law → `LAB`; Exec. Law → `EXC`; Executive Law → `EXC`; Educ. Law → `EDN`; Ins. Law → `ISC`; Jud. Law → `JUD`; Judiciary Law → `JUD`; Dom. Rel. Law → `DOM`; DRL → `DOM`; Est. Powers & Trusts Law → `EPT`; EPTL → `EPT`; Real Prop. Law → `RPP`; RPL → `RPP`; Real Prop. Acts. Law → `RPA`; RPAPL → `RPA`; Real Prop. Tax Law → `RPT`; RPTL → `RPT`; Civ. Rights Law → `CVR`; Civil Rights Law → `CVR`; Civ. Serv. Law → `CVS`; Pub. Health Law → `PBH`; PHL → `PBH`; Soc. Serv. Law → `SOS`; Mental Hyg. Law → `MHY`; Debt. & Cred. Law → `DCD`; Gen. Mun. Law → `GMU`; Town Law → `TWN`; Tax Law → `TAX`; U.C.C. → `UCC`; UCC → `UCC`; Envtl. Conserv. Law → `ENV`; ECL → `ENV`; Pub. Off. Law → `PBO`; Public Officers Law → `PBO`; Elec. Law → `ELN`; Election Law → `ELN`; Mult. Dwell. Law → `MDW`; Alco. Bev. Cont. Law → `ABC`; State Fin. Law → `STF`; Fin. Serv. Law → `FIS`; Workers' Comp. Law → `WKC`; WCL → `WKC`; Unconsol. Laws → `(not in Senate CONSOLIDATED list — locate via index)`; Fam. Ct. Act → `FCT`; Family Court Act → `FCT`; SCPA → `SCP`; Surr. Ct. Proc. Act → `SCP`; N.Y.C. Civ. Ct. Act → `CCA`; CPLR (as Civ. Prac. Law) → `CVP`

There are two citation styles. The NY Official Reports style (Tanbook) omits periods (40 NY3d 405; CPLR 3211 [a] [7]; 22 NYCRR 202.8-g), while Bluebook uses periods (N.Y. C.P.L.R. 3211(a)(7) (McKinney); N.Y. Gen. Oblig. Law § 5-701). The Tanbook style manual is at nycourts.gov/reporter/Styman_Menu.shtml (reported, not fetched). Slip Op number ranges observed: 0xxxx are reported appellate and Court of Appeals decisions; 3xxxx(U) are eCourts-sourced trial orders shown as PDF and 'not selected for official publication'; 5xxxx(U) are unreported decisions with a Misc 3d NNNN(A) table cite; 6xxxx-8xxxx are motion decisions, both Court of Appeals leave motions and Appellate Division motions (the latter with (U)). The court IDs come from memory and were not checked against CourtListener. CourtListener groups the four Appellate Division departments under one id, so the department appears only in the citation parenthetical. The Senate law-ID table (94 Consolidated Laws plus court acts) is in ny-laws-senate.pattern_rules. Court acts (FCT, SCP, CCA, UDA, UJCA) and WKC are listed by the Senate outside the 94-law CONSOLIDATED table; their LAWIDs here are from the Senate's court-acts listing and should be confirmed on first use (open question). Precedence: the 22 NYCRR court-rules pattern wins over the general NYCRR pattern (the latter excludes title 22). The Consolidated Laws pattern accepts only the closed set of consolidated-law names (and their abbreviations from law_aliases) and refuses a preceding state abbreviation ('Md.', 'Tex.'), so other states' '… Law §' citations are not claimed.

## A. Statutes / code

### `ny-laws-assembly` — NY Assembly public LAWS of New York (LBDC)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · New York State Assembly / Legislative Bill Drafting Commission · text: **link-only** · official: unknown
- **Coverage:** Consolidated and unconsolidated laws (reported)
- **Access:** `link-only` · format html
  - Index: `https://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO:`
- **Automation:** WebFetch blocked · shell http-error · robots: Could not be read: shell got 'Connection reset by peer' (curl 35). WebFetch reported ROBOTS_DISALLOWED.
  - Not retried by another route.
- **Currency:** unknown
- **Official status:** Not reached.
- **Hazard:** Robots-disallowed for WebFetch
- **Probe:** index → `https://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO:` — expect: "LAWS OF NEW YORK index"
- **Evidence (2026-10-16):** WebFetch error_type ROBOTS_DISALLOWED; curl (35) Recv failure: Connection reset by peer. | Re-confirmed blocked 2026-10-16: WebFetch error_type ROBOTS_DISALLOWED
- **Notes:** Not usable as a second tier-1 statute source.

### `ny-laws-senate` — NYS Open Legislation: The Laws of New York (Consolidated Laws, court acts, Constitution)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York State Senate · text: **fetch-and-quote** · official: unknown
- **Coverage:** All 94 Consolidated Laws, the Unconsolidated Laws, the court acts (FCT, SCP, CCA, UCT, UJC, NYC Civil Court Act, CTC), the Constitution (CNS), and the Senate and Assembly Rules (CMS/CMA). Each section has historical revisions back to 2014-09-22.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.nysenate.gov/legislation/laws/{LAWID}/{section}`
  - Placeholders: {section} is the section number exactly as cited, with dashes and dots kept (5-701, 155.05, 3211, 1012). For the Constitution, LAWID=CNS and section=A{article arabic}S{section}, e.g. art I § 11 → CNS/A1S11 (verified). The LAWID table is the 3-letter codes scraped 2026-10-16 from https://www.nysenate.gov/legislation/laws/CONSOLIDATED: ABC Alcoholic Beverage Control; ABP Abandoned Property; ACA Arts & Cultural Affairs; ACG Alternative County Government; AGM Agriculture & Markets; BNK Banking; BSC Business Corporation; BVO Benevolent Orders; CAL Canal; CAN Cannabis; CCO Cooperative Corporations; CNT County; COM Economic Development; COR Correction; CPL Criminal Procedure; CVP Civil Practice Law & Rules; CVR Civil Rights; CVS Civil Service; DCD Debtor & Creditor; DOM Domestic Relations; EDN Education; EDP Eminent Domain Procedure; ELD Elder; ELN Election; EML Employers' Liability; ENG Energy; ENV Environmental Conservation; EPT Estates, Powers & Trusts; EXC Executive; FIS Financial Services; GAS General Associations; GBS General Business; GCN General Construction; GCT General City; GMU General Municipal; GOB General Obligations; HAY Highway; IND Indian; ISC Insurance; JUD Judiciary; LAB Labor; LEG Legislative; LFN Local Finance; LIE Lien; LLC Limited Liability Company; MDW Multiple Dwelling; MHA Municipal Housing Authorities; MHR Municipal Home Rule; MHY Mental Hygiene; MIL Military; MRE Multiple Residence; NAV Navigation; NPC Not-for-Profit Corporation; PAR Parks, Recreation & Historic Preservation; PBA Public Authorities; PBB Public Buildings; PBG Public Housing; PBH Public Health; PBL Public Lands; PBO Public Officers; PBS Public Service; PEN Penal; PEP Personal Property; PML Racing, Pari-Mutuel Wagering & Breeding; PPD Printing & Public Documents; PTR Partnership; PVH Private Housing Finance; RAT Rapid Transit; RCO Religious Corporations; REL Rural Electric Cooperative; RPA Real Property Actions & Proceedings; RPP Real Property; RPT Real Property Tax; RRD Railroad; RSS Retirement & Social Security; SAP State Administrative Procedure Act; SCC Second Class Cities; SLG Statute of Local Governments; SOS Social Services; STF State Finance; STL State; STT State Technology; SWC Soil & Water Conservation Districts; TAX Tax; TCP Transportation Corporations; TRA Transportation; TWN Town; UCC Uniform Commercial Code; VAT Vehicle & Traffic; VAW Volunteer Ambulance Workers' Benefit; VET Veterans' Services; VIL Village; VOL Volunteer Firefighters' Benefit; WKC Workers' Compensation. Court acts (each returned a section page by shell): FCT Family Court Act (FCT/1012), SCP Surrogate's Court Procedure Act (SCP/2103), CCA NYC Civil Court Act (CCA/202); UCT and UJC loaded as law pages but no section was probed. Other: CNS Constitution; CMS/CMA Senate/Assembly Rules. Law index: /legislation/laws/{LAWID}; article pages: /legislation/laws/{LAWID}/A{n}.
  - Index: `https://www.nysenate.gov/legislation/laws/CONSOLIDATED`
  - Navigation: For an unknown section number: law index → article → section links.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * disallows /search/, /admin/, /core/, /profiles/ and similar. /legislation/laws/ is not disallowed. No crawl-delay.
  - Served behind Cloudflare, but curl got HTTP 200 with no challenge (CVP/3211 = 42,930 bytes). Revision history is a POST form; a ?date= query parameter is ignored (it still showed the most recent revision), so historical text needs the form or the API.
- **Currency:** Above the section text, per section — observed: "Viewing most recent revision (from 2022-05-13)"
- **Official status:** The CVP/3211 page has no official or unofficial disclaimer, and a regex search of its HTML for 'official' and 'disclaim' turned up only statute text. No New York publisher states an official online code; the printed McKinney's/Gould codes remain the citation standard. Treat the text as authoritative-in-practice but not certified.
- **Hazard:** Revision date is the date of the last amendment, not a 'current through' date; there is no site-wide currency statement
- **Hazard:** Long sections (EXC/296 = 119,730 bytes HTML) may exceed WebFetch's 100k-character window; use offset
- **Hazard:** WebFetch summariser reported GOB 5-701 subdivision a as 'skipping items 4, 7, and 8' — those paragraphs were repealed; do not treat as truncation, but verify numbering against the second source
- **Hazard:** Historical revisions not reachable by GET URL
- **Probe:** CPLR 3211; also Gen. Oblig. Law § 5-701 → `https://www.nysenate.gov/legislation/laws/CVP/3211` — expect: "Rule 3211. Motion to dismiss. (a) Motion to dismiss cause"
- **Evidence (2026-10-16):** WebFetch CVP/3211: YES, full text through (h), 'Viewing most recent revision (from 2022-05-13)'. WebFetch GOB/5-701: YES, opens 'Every agreement, promise or undertaking is void', revision 2014-09-22. Shell 200 for PEN/155.05 (2024-07-26), EXC/296 (2026-06-05), FCT/1012, SCP/2103, CCA/202. | Independent check 2026-10-16: YES 'Rule 3211. Motion to dismiss. (a) Motion to dismiss cause'; 'Viewing most recent revision (from 2022-05-13)'; complete through (h); second citation N.Y. Veh. & Traf. Law § 1192 ok
- **Notes:** Preferred tier-1 source for both statute fetches. For the second fetch, use public.law (which states it sources this same nysenate.gov page, so it is not fully independent) or Justia.

### `ny-laws-senate-api` — NY Senate Open Legislation API v3 (laws)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · New York State Senate · text: **link-only** · official: unknown
- **Coverage:** Laws, bills, calendars; JSON
- **Access:** `constructible` · format json
  - Pattern: `https://legislation.nysenate.gov/api/3/laws/{LAWID}/{section}?key={APIKEY}`
  - Placeholders: Same LAWID table as ny-laws-senate. Requires a free API key, which this research did not obtain.
  - Index: `https://legislation.nysenate.gov/api/3/laws`
- **Automation:** WebFetch untested · shell http-error · robots: legislation.nysenate.gov/robots.txt: 'User-agent: *' with no disallow lines
  - Without a key: HTTP 401, JSON 'A valid API key is needed to fulfill this request.' (errorCode 701).
- **Currency:** unknown (not fetched with key)
- **Official status:** Same data as ny-laws-senate.
- **Hazard:** Needs an API key; the skill cannot use it unless a key is provisioned
- **Probe:** CPLR 3211 → `https://legislation.nysenate.gov/api/3/laws/CVP/3211` — expect: "JSON with section text"
- **Evidence (2026-10-16):** HTTP 401 errorCode 701 'A valid API key is needed' — endpoint exists, key required.
- **Notes:** Script candidate if a key is ever provisioned.

### `ny-laws-justia` — Justia — New York Laws (annual editions)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Annual snapshots: 2006, 2010, and 2012-2025. The latest is the 2025 edition.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Do not construct. The hierarchy varies by law: CPLR is /cvp/article-32/r3211/ ('r' prefix for CPLR rules); GOL is /gob/article-5/title-7/5-701/ (extra title level, no prefix). Law segment = Senate LAWID in lower case.
  - Index: `https://law.justia.com/codes/new-york/`
  - Navigation: /codes/new-york/{lawid}/ → article-N/ → title-N/ (where present) → section link from the list.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Not readable from the shell: robots.txt itself returned 403 cf-mitigated: challenge.
  - One WebFetch of a guessed section URL (/codes/new-york/cvp/article-32/3211/, without the 'r') returned CLIENT_ERROR. The 'r' prefix matters.
- **Currency:** Page heading — observed: "2025 New York Laws"
- **Official status:** The CVP index carries the disclaimer 'These codes may not be the most recent version.'
- **Hazard:** Annual edition lags; amendments after 2025 missing
- **Hazard:** Shell blocked by Cloudflare challenge
- **Probe:** CPLR 3211 → `https://law.justia.com/codes/new-york/cvp/article-32/r3211/` — expect: "A party may move for judgment dismissing one or more"
- **Evidence (2026-10-16):** WebFetch YES, complete through (h), '2025 New York Laws'. curl 403 cf-mitigated: challenge. | Independent check 2026-10-16: YES CPLR 3211 'A party may move for judgment dismissing one or more'; '2025 New York Laws'; second citation N.Y. Gen. Oblig. Law § 5-701 ok

### `ny-laws-publiclaw` — NewYork.Public.Law — Laws of New York

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Consolidated Laws including CPLR. Constitution and NYCRR not listed.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://newyork.public.law/laws/n.y._{law_slug}_section_{section}`
  - Placeholders: {law_slug} is the lower-case law name with spaces as underscores, plus '_law' where the name includes it. Verified slugs: civil_practice_law_and_rules (3211), general_obligations_law (5-701), penal_law (155.05). The index shows '&' forms (n.y._civil_practice_law_&_rules); both forms returned 200. For other laws, take the slug from the index https://newyork.public.law/laws, whose links follow /laws/n.y._{law_slug}.
  - Index: `https://newyork.public.law/laws`
  - Navigation: index → law → article → section
- **Automation:** WebFetch ok · shell ok · robots: Disallows /admin, /api, /data, /demo, /images and /users. /laws is allowed.
  - Cloudflare-fronted; curl got 200 with no challenge.
- **Currency:** Index header and a per-section 'Verified' / 'Last modified' line — observed: "Verified: Oct. 10, 2026 / Last modified: Sep. 22, 2014"
- **Official status:** Third-party republication. Each section names its source as the nysenate.gov URL, e.g. 'Source: Section 3211 … https://www.nysenate.gov/legislation/laws/CVP/3211'.
- **Hazard:** Copies nysenate.gov, so it is not an independent textual witness
- **Hazard:** The index 'Updated' date differed by route: WebFetch saw 'Updated September 26, 2026' and curl saw 'Updated October 10, 2026', so WebFetch may be serving a cached copy
- **Hazard:** The 'Verified: <date>' badge is per section page (Labor Law § 240 showed Sep. 26, 2026); read and disclose it from each page.
- **Probe:** N.Y. Gen. Oblig. Law § 5-701 → `https://newyork.public.law/laws/n.y._general_obligations_law_section_5-701` — expect: "Every agreement, promise or undertaking is void, unless it or"
- **Evidence (2026-10-16):** WebFetch YES, body complete, 'Verified: Oct. 10, 2026', 'Last modified: Sep. 22, 2014'. Shell 200 for CPLR 3211 (32,048 bytes), GOL 5-701, Penal 155.05. | Independent check 2026-10-16: YES 'Every agreement, promise or undertaking is void, unless it or'; Verified Oct. 10, 2026; Last modified Sep. 22, 2014; second citation Labor Law § 240 ok
- **Notes:** The 2026-10-05 skill note recorded 'Updated September 26, 2026'; that index date was still seen via WebFetch on 2026-10-16.

## B. Constitution

### `ny-const-dos` — New York State Constitution (Department of State PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York Department of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full constitution as amended
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format pdf
  - Placeholders: The file path is dated (system/files/documents/2025/12/…) and changes with each edition, so locate it via the DOS constitution page (dos.ny.gov/new-york-state-constitution), which WebFetch could not load (CLIENT_ERROR) and the shell got 403 for.
  - Index: `https://dos.ny.gov/system/files/documents/2025/12/constitution-january-1-2026.pdf`
  - Navigation: Single PDF
- **Automation:** WebFetch ok · shell untested · robots: dos.ny.gov/robots.txt: 'User-agent: *' with Drupal defaults
  - The DOS HTML landing page returned 403 to curl and CLIENT_ERROR to WebFetch.
- **Currency:** Cover — observed: "As revised, including amendments effective January 1, 2026"
- **Official status:** Department of State publication; no explicit official-text statement was observed in the portion read.
- **Hazard:** WebFetch truncates partway through Article V § 1; later articles are unreachable in one fetch
- **Probe:** N.Y. Const. art. I, § 11 → `https://dos.ny.gov/system/files/documents/2025/12/constitution-january-1-2026.pdf` — expect: "No person shall be denied the equal protection of the"
- **Evidence (2026-10-16):** WebFetch: art. I § 11 PRESENT; text truncated in art. V § 1. URL found by WebSearch. | Independent check 2026-10-16: YES art I § 11 present; 'As revised, including amendments effective January 1, 2026'; truncates in art V § 1
- **Notes:** Use as the second fetch for Articles I-IV only. For later articles, use ny-const-senate alone.

### `ny-const-senate` — New York State Constitution (Open Legislation law ID CNS)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York State Senate · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current constitution with section revision history
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.nysenate.gov/legislation/laws/CNS/A{article}S{section}`
  - Placeholders: Convert the Roman article number to Arabic: art I § 11 → A1S11. Lettered sections (e.g. art VI § 2-a) are untested; use the index https://www.nysenate.gov/legislation/laws/CNS.
  - Index: `https://www.nysenate.gov/legislation/laws/CNS`
  - Navigation: CNS → article → section
- **Automation:** WebFetch ok · shell ok · robots: See ny-laws-senate
- **Currency:** Above section text — observed: "Viewing most recent revision (from 2025-01-10)"
- **Official status:** Same as ny-laws-senate; no disclaimer.
- **Probe:** N.Y. Const. art. I, § 11 → `https://www.nysenate.gov/legislation/laws/CNS/A1S11` — expect: "a. No person shall be denied the equal protection of"
- **Evidence (2026-10-16):** WebFetch YES, complete through subsection b; revision 2025-01-10 (reflects the 2024 amendment). Shell 200, 33,554 bytes. | Independent check 2026-10-16: YES 'No person shall be denied the equal protection of the laws'; revision 2025-01-10; complete; second citation NY Const, art VI, § 3 ok

## C. Court rules

### `ny-rules-coa-500` — Rules of Practice of the Court of Appeals (22 NYCRR Part 500)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York Court of Appeals · text: **fetch-and-quote** · official: unknown
- **Coverage:** 22 NYCRR 500.1-500.27
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.nycourts.gov/ctapps/500rules.htm#{n}`
  - Placeholders: A single page holds all of Part 500, with anchors #{n} for 500.{n}. The fragment does not change what is fetched. A second copy at /CTAPPs/500rules10.htm also returned the full Part.
  - Index: `https://nycourts.gov/ctapps/500rules.htm`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: See ny-rules-ucr-nycourts
- **Currency:** page header — observed: "Effective: December 10, 2025"
- **Official status:** Court's own page; no explicit official statement.
- **Hazard:** An older copy at /CTAPPs/500rules10.htm carries 'Effective: May 8, 2024' — do not use it
- **Probe:** 22 NYCRR 500.10 → `https://www.nycourts.gov/ctapps/500rules.htm` — expect: "On its own motion, the Court may examine its subject"
- **Evidence (2026-10-16):** WebFetch 500rules10.htm YES (500.10 complete, 'Effective: May 8, 2024'); WebFetch 500rules.htm: TOC anchors #10, #22, 'Effective: December 10, 2025'. | Independent check 2026-10-16: YES 500rules10.htm '(a) On its own motion, the Court may examine'; 'Effective: May 8, 2024'; second citation 22 NYCRR 500.22 ok
- **Notes:** Body text was verified only on the older copy; the newer page was checked for its TOC and effective date. An independent run should confirm body text on /ctapps/500rules.htm.

### `ny-rules-rpc-1200` — New York Rules of Professional Conduct (22 NYCRR Part 1200) — PDF

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Appellate Divisions (joint rules), via NY Unified Court System · text: **fetch-and-quote** · official: unknown
- **Coverage:** Part 1200 Rules 1.0-8.5 (TOC to p. 37)
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format pdf
  - Placeholders: Single PDF; the path contains spaces (URL-encode them as %20).
  - Index: `https://www.nycourts.gov/legacypdfs/rules/jointappellate/NY Rules of Prof Conduct.pdf`
  - Navigation: Single PDF
- **Automation:** WebFetch ok · shell blocked-challenge · robots: See ny-rules-ucr-nycourts
- **Currency:** Cover — observed: "effective April 1, 2009 (no later amendment date seen)"
- **Official status:** Court-system PDF; no explicit official statement observed.
- **Hazard:** WebFetch truncates the PDF; later rules may need the Cornell page
- **Hazard:** No as-amended date
- **Hazard:** WebFetch text of the PDF ends mid-Rule 5.8(a); Rules 5.8(b) onward must come from ny-nycrr-cornell (22 NYCRR 1200.0).
- **Probe:** Rules of Professional Conduct rule 1.7(a) (22 NYCRR 1200.0) → `https://www.nycourts.gov/legacypdfs/rules/jointappellate/NY Rules of Prof Conduct.pdf` — expect: "Except as provided in paragraph (b), a lawyer shall not"
- **Evidence (2026-10-16):** WebFetch: 'PART 1200 – RULES OF PROFESSIONAL CONDUCT', Rule 1.7(a) first words present; content truncated before end. | Independent check 2026-10-16: YES 1.7(a) 'Except as provided in paragraph (b), a lawyer shall not'; 'APRIL 1, 2009'
- **Notes:** The summariser's answer contradicted itself: it said 1.7(a) was 'NOT PRESENT' but then quoted it. Treat as verified with caution. Cornell has all of Part 1200 as a single section (22-NYCRR-1200.0); not probed.

### `ny-rules-ucr-nycourts` — Uniform Rules for the Trial Courts (22 NYCRR Parts 200-221), incl. Part 202 Uniform Civil Rules

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · NY Unified Court System (Office of Court Administration) · text: **fetch-and-quote** · official: unknown
- **Coverage:** 22 NYCRR Parts 200, 202, 205-208, 210, 212, 214-218, 220, 221 (one HTML page per Part). Parts 209, 211, 213, 219 are not on the index — use ny-nycrr-cornell.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.nycourts.gov/rules/part-{part}-{slug}`
  - Placeholders: The slug is descriptive and not derivable (e.g. part-202-uniform-civil-rules-supreme-court-and-county-court), so take it from the index. There are no section-level anchors or links; a whole Part is one page.
  - Index: `https://www.nycourts.gov/rules/trialcourts/202.shtml`
  - Navigation: The legacy trialcourts/*.shtml page lists the Part pages (see coverage) → Part page holds every section's text.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.nycourts.gov (via WebFetch): User-agent * disallows /core/, /profiles/, /admin/, /search/, /user/login/. /rules/ and /reporter/ are not disallowed.
  - From the shell, www.nycourts.gov returns 403 cf-mitigated: challenge, even for robots.txt. The new /rules landing page renders its menu with JavaScript, and WebFetch saw 'No results found'.
- **Currency:** none stated — observed: "none stated (202.8-g shown as '[Repealed]')"
- **Official status:** Court-system page; no official or unofficial statement and no currency statement observed.
- **Hazard:** Any Part page may exceed WebFetch's 100,000-character window (Part 202: 134,417, stops in 202.9-a; Part 208: 121,545, stops in 208.35). Watch for the window note and refetch with offset=100000.
- **Hazard:** No currency statement; cross-check with Cornell LII State Register notes
- **Probe:** 22 NYCRR 202.7 → `https://www.nycourts.gov/rules/part-202-uniform-civil-rules-supreme-court-and-county-court` — expect: "There shall be compliance with the procedures prescribed in the"
- **Evidence (2026-10-16):** WebFetch YES: body text of 202.1-202.9-a present; window note '134417 characters … covers 0 to 100000'. 202.8-g marked [Repealed]. | Independent check 2026-10-16: YES 202.7 'There shall be compliance with the procedures prescribed in'; window 0-100000 of 134417; second citation 22 NYCRR 208.4 ok
- **Notes:** Other court-rule families: the Court of Appeals is ny-rules-coa-500 and the Rules of Professional Conduct are ny-rules-rpc-1200. The Appellate Division practice rules (Part 1250) have no verified tier-1 text; the nycourts.gov/rules/jointappellate page lists joint orders only. A Part 1250 PDF exists at justicetraining.nycourts.gov/courts/ad4/Clerk/Part1250-StatewidePracticeRules.pdf (reported, not fetched). Use ny-nycrr-cornell for 22 NYCRR 1250.x. The CPLR is a statute: route it to ny-laws-senate (CVP).

## D. Administrative code

### `ny-nycrr-westlaw` — Official Compilation of Codes, Rules and Regulations of the State of New York (NYCRR) on Westlaw

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · NY Department of State (Division of Administrative Rules) / Thomson Reuters · text: **link-only** · official: unknown
- **Coverage:** All 23 NYCRR titles
- **Access:** `link-only` · format html
  - Index: `https://govt.westlaw.com/nycrr/`
- **Automation:** WebFetch blocked · shell http-error · robots: govt.westlaw.com/robots.txt returned HTTP 403 to curl
  - Not retried.
- **Currency:** unknown
- **Official status:** The DOS State Register page calls DAR 'the official compiler of state agency rules and regulations (NYCRR)' and links to the Westlaw search, but does not state that Westlaw is official.
- **Hazard:** Blocked
- **Probe:** index → `https://govt.westlaw.com/nycrr/` — expect: "NYCRR browse"
- **Evidence (2026-10-16):** WebFetch error_type SITE_BLOCKED 'Access to this website has been blocked'; curl robots.txt 403. | Re-confirmed blocked 2026-10-16: WebFetch SITE_BLOCKED 'Access to this website has been blocked'

### `ny-nycrr-cornell` — Cornell LII — New York Codes, Rules and Regulations

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NYCRR Titles 1-23 and 99, with up to two versions per section
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/new-york/{title}-NYCRR-{section}`
  - Placeholders: {section} is written exactly as cited, keeping dots and dashes: 22-NYCRR-202.8-g, 22-NYCRR-1250.1 and 12-NYCRR-23-1.7 all verified. A missing section silently returns the NYCRR title table of contents (22-NYCRR-202.70 did), so check the body.
  - Index: `https://www.law.cornell.edu/regulations/new-york`
  - Navigation: Title → Subtitle → Chapter → Part → section (if constructed URL falls to TOC)
- **Automation:** WebFetch ok · shell ok · robots: User-agent * Crawl-delay: 10. /regulations/ is not disallowed.
  - nginx, no challenge (robots.txt 200).
- **Currency:** Notes section per section — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party republication. Each page cites its State Register source and says 'State regulations are updated quarterly'.
- **Hazard:** A not-found section silently falls back to the title TOC (soft 404)
- **Hazard:** Shows repealed sections with body text, e.g. 202.8-g ('Repealed … eff. 7/7/2025'), so always read the Notes
- **Hazard:** Body text may appear twice (version comparison block)
- **Hazard:** The 'updated quarterly' currency line does not appear on every section page; when absent, report the State Register history notes as the currency evidence.
- **Probe:** 12 NYCRR 23-1.7 → `https://www.law.cornell.edu/regulations/new-york/12-NYCRR-23-1.7` — expect: "(a) Overhead hazards. (1) Every place where persons are required"
- **Evidence (2026-10-16):** WebFetch YES for 12 NYCRR 23-1.7, 22 NYCRR 1250.1 ('Adopted … State Register October 31, 2018'), and 22 NYCRR 202.8-g (repealed eff. 7/7/2025). 22-NYCRR-202.70 → TOC only. | Independent check 2026-10-16: YES 'Every place where persons are required to work or pass'; 'State regulations are updated quarterly; we currently have two versions available.'; second citation 10 NYCRR 405.7 ok
- **Notes:** This is the only free text source for agency NYCRR, and the fallback for 22 NYCRR court rules.

## D. Administrative register

### `ny-register-dos` — New York State Register

- **Status:** REPORTED 2026-10-16 · **Tier 1** · NY Department of State, Division of Administrative Rules · text: **link-only** · official: official
- **Coverage:** Weekly issues; archive filter 2015-2026 (656 results)
- **Access:** `index-anchored` · format html
  - Pattern: `https://dos.ny.gov/{month}-{day}-{year}vol-{roman}-issue-{n}`
  - Placeholders: Seen as october-14-2026vol-xlviii-issue-41. Take URLs from the index; do not construct them.
  - Index: `https://dos.ny.gov/state-register`
  - Navigation: State Register page → issue page → issue PDF(s)
- **Automation:** WebFetch fail · shell untested · robots: dos.ny.gov: 'User-agent: *' with Drupal defaults
  - WebFetch got the index but CLIENT_ERROR on the issue page. dos.ny.gov HTML returned 403 to curl for another page.
- **Currency:** Index — observed: "The October 14, 2026/Vol. XLVIII, Issue 41"
- **Official status:** DOS page: DAR is 'the official compiler of state agency rules and regulations (NYCRR)'; the Register is its weekly publication.
- **Hazard:** Issue pages not fetchable by WebFetch on probe date
- **Probe:** NY Reg, Oct. 14, 2026 → `https://dos.ny.gov/october-14-2026vol-xlviii-issue-41` — expect: "issue PDF links"
- **Evidence (2026-10-16):** The index fetched OK (latest issue Oct 14, 2026). The issue page returned CLIENT_ERROR.

## E. Case law

### `ny-cases-bound-volumes` — Official Reports bound volumes (PDF, 1999-)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · New York State Law Reporting Bureau · text: **link-only** · official: official
- **Coverage:** NY2d/NY3d, AD2d/AD3d, Misc 2d/Misc 3d bound volumes from 1999
- **Access:** `index-anchored` · format pdf
  - Placeholders: PDF link pattern unknown: WebFetch did not expose the volume links.
  - Index: `https://www.nycourts.gov/reporter/bound-volumes.shtml`
  - Navigation: series heading → volume PDF (links not visible to WebFetch)
- **Automation:** WebFetch fail · shell blocked-challenge · robots: See ny-rules-ucr-nycourts
  - Probably rendered with JavaScript.
- **Currency:** unknown
- **Official status:** Bound volumes page: 'PDF versions of the Official Reports bound volumes beginning in 1999'.
- **Hazard:** Whole-volume PDFs are very large and would truncate
- **Probe:** index → `https://www.nycourts.gov/reporter/bound-volumes.shtml` — expect: "volume PDF links"
- **Evidence (2026-10-16):** Series headings were listed with no volume links visible.

### `ny-cases-ctapps` — Court of Appeals — Decisions (slip opinion PDFs and decision lists)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York Court of Appeals · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly pages for 2025-2026 seen; older years move to LRB
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.nycourts.gov/ctapps/Decisions/{YYYY}/{Mon}{YY}/{docket}{opn|mem|ent}{YY}-Decision.pdf`
  - Placeholders: Monthly page: /ctapps/Decisions/{YYYY}/{Mon}{YY}/{MonthName}{YY}.html (e.g. 2025/Oct25/October25.html). Decision list PDF: …/DecisionList{MMDDYY}.pdf. The opinion type (opn, mem or ent) is not knowable in advance, so take links from the monthly page.
  - Index: `https://www.nycourts.gov/ctapps/decisions.htm`
  - Navigation: decisions.htm → month page → opinion PDF
- **Automation:** WebFetch ok · shell blocked-challenge · robots: See ny-rules-ucr-nycourts
- **Currency:** none
- **Official status:** Court's own slip opinions; the page says older slips 'no longer on this site' are on the Law Reporting Bureau site.
- **Hazard:** Slip pagination only ('- 2 - No. 48'); no NY3d page numbers, so use ny-cases-lrb for pinpoints
- **Hazard:** decisions.htm leaves some months unlinked (recess or not yet posted) — use ny-cases-lrb monthly index (cidxtable) for those
- **Hazard:** Listing gives the Court's 'No.' not a lower-court docket
- **Hazard:** An 'ent' document can be a one-page entry (e.g. accepting certified questions), not an opinion
- **Probe:** Matter of Nemeth v K-Tooling, No. 48 (Oct. 24, 2023) → `https://www.nycourts.gov/ctapps/Decisions/2023/Oct23/48opn23-Decision.pdf` — expect: "On this appeal we must determine whether, under CPLR 203"
- **Evidence (2026-10-16):** WebFetch YES, slip pagination only. The October25.html month page listed 70opn25, 67opn25 and DecisionList102325.pdf. | Independent check 2026-10-16: YES 'On this appeal we must determine whether, under CPLR 203'; slip pages '- 2 - No. 48'; second citation Asinga v Gatorade Co., No. 113 (Sept. 22, 2026) ok
- **Notes:** The probe URL was constructed by analogy and fetched successfully, but the pattern is not stable enough to call constructible.

### `ny-cases-lrb` — New York Slip Opinion Service (Law Reporting Bureau) — decisions

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York State Law Reporting Bureau · text: **fetch-and-quote** · official: official
- **Coverage:** Court of Appeals and Appellate Division decisions from October 2003 (4th Dept November 2003); Appellate Term from Sept/Oct 2003; other courts from December 2003; Commercial Division from January 2004. Selected trial decisions only.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.nycourts.gov/reporter/3dseries/{year}/{year}_{nnnnn}.htm`
  - Placeholders: Use the five-digit number from 'YYYY NY Slip Op NNNNN' and drop any '(U)': 2023 NY Slip Op 04822 → 3dseries/2023/2023_04822.htm; 2024 NY Slip Op 50001(U) → 3dseries/2024/2024_50001.htm (same pattern). 3xxxx(U) eCourts-sourced orders are PDFs at https://www.nycourts.gov/reporter/pdfs/{year}/{year}_{nnnnn}.pdf (seen for 2023_34927). Very recent decisions (the current month) are only at https://www.nycourts.gov/reporter/current/3dseries/{year}/{year}_{nnnnn}.shtml; the 3dseries/.htm URL returned 404 for 2026_05997, so try current/ when the plain path 404s. From (court, date, docket): use the monthly index https://www.nycourts.gov/reporter/slipidx/{idx}_{year}_{monthname}.shtml, where {idx} = cidxtable (Court of Appeals), aidxtable_1..4 (Appellate Division departments), at_1_idxtable / at_2_idxtable (Appellate Term), com_div_idxtable (Commercial Division); monthname is lower-case full (september). Other courts use miscolo for the current month; its archive name is not verified. Current month: https://www.nycourts.gov/reporter/current/index/{idx}.shtml.
  - Index: `https://www.nycourts.gov/reporter/Decisions.shtml`
  - Navigation: Monthly index rows list Title | Judge | Docket No. (Index/Appeal/Case No.) | Slip Op No., grouped by decision date → decision link.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: /reporter/ not disallowed (see ny-rules-ucr-nycourts)
  - nycourts.gov without www returns a 302 to www. www returns 403 cf-mitigated: challenge to curl. Do not work around it.
- **Currency:** Header of each decision page — observed: "As corrected through Wednesday, November 8, 2023"
- **Official status:** Official reporter's site. A corrected page shows the Official Reports cite in brackets (e.g. [219 AD3d 1251]) and 'As corrected through …'. New slips say 'uncorrected and subject to revision before publication in the Official Reports'. (U) decisions say 'will not be published in the printed Official Reports'. Bound-volumes page: 'Official Reports published on this website are subject to copyright.'
- **Hazard:** A corrected page has [*n] markers for the official pages. Court of Appeals pages also have {**40 NY3d at 407} markers; Appellate Division pages showed only [*1] for a one-page decision
- **Hazard:** Uncorrected (recent) slips have no official cite yet
- **Hazard:** Plain /reporter/3dseries/ path 404s for the current month; use /reporter/current/3dseries/…shtml
- **Hazard:** 3xxxx(U) items are PDF copies of trial orders with slip pagination only
- **Hazard:** Page markers [*n] and {**NN AD3d at NNN} can fall mid-word or mid-citation; strip them before quote matching
- **Hazard:** The docket number appears only in the monthly index listing, not on the decision page
- **Probe:** Matter of Nemeth v K-Tooling, 2023 NY Slip Op 05349, 40 NY3d 405 → `https://www.nycourts.gov/reporter/3dseries/2023/2023_05349.htm` — expect: "On this appeal we must determine whether, under CPLR 203"
- **Evidence (2026-10-16):** 05349: [40 NY3d 405], [*1]-[*5], complete, 'As corrected through Wednesday, January 17, 2024'. 04822: [219 AD3d 1251], complete. 2024_50001: 81 Misc 3d 1223(A). 2026_00100: [245 AD3d 484]. 2026_05997.htm 404; current/…shtml OK. Monthly indexes aidxtable_1_2023_september and cidxtable_2023_october OK with dockets. | Independent check 2026-10-16: YES CPLR 203 opening; [40 NY3d 405]; 'As corrected through Wednesday, January 17, 2024'; {**40 NY3d at 407}; second citation Apollo Funding Co. v Dave Reilly Constr., LLC, 2025 NY Slip Op 05055 (2d Dept, docket 2024-03453) ok
- **Notes:** Usable as a quote-verification text source: the page text is the official text and carries official pagination. This is the best free route to official page numbers in New York.

### `ny-cases-lrb-search` — Law Reporting Bureau Decision Search (iapps)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · NY Unified Court System · text: **link-only** · official: unknown
- **Coverage:** Slip opinion search
- **Access:** `search-only` · format html
  - Index: `https://iapps.courts.state.ny.us/lawReporting/Search`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: Not readable: robots.txt returned 403 cf-mitigated: challenge to the shell. WebFetch reported ROBOTS_DISALLOWED.
- **Currency:** 
- **Hazard:** Blocked
- **Probe:** search page → `https://iapps.courts.state.ny.us/lawReporting/Search`
- **Evidence (2026-10-16):** WebFetch ROBOTS_DISALLOWED; curl 403 cf-mitigated: challenge. | Re-confirmed blocked 2026-10-16: WebFetch error_type ROBOTS_DISALLOWED
- **Notes:** Use the monthly slipidx listings (ny-cases-lrb) instead.

### `ny-cases-official-reports-westlaw` — New York Official Reports Service (1847-present)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Law Reporting Bureau / Thomson Reuters · text: **link-only** · official: official
- **Coverage:** 1847-present
- **Access:** `link-only` · format html
  - Index: `https://govt.westlaw.com/nyofficial/Index`
- **Automation:** WebFetch blocked · shell http-error · robots: 403 to curl
  - Blocked on 2026-10-05 (skill note); not retried by any route per instructions.
- **Currency:** unknown
- **Official status:** Linked from nycourts.gov/reporter as the 'New York Official Reports Service', covering decisions 'from 1847 through the latest Advance Sheet'.
- **Hazard:** Blocked
- **Probe:** index → `https://govt.westlaw.com/nyofficial/Index`
- **Evidence (2026-10-16):** Carried over: WebFetch SITE_BLOCKED (2026-10-05). The same host returned SITE_BLOCKED for /nycrr/ on 2026-10-16. | Re-confirmed blocked 2026-10-16: WebFetch SITE_BLOCKED 'Access to this website has been blocked'

### `ny-cases-justia` — Justia — New York case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Court of Appeals and Appellate Division by year (e.g. 2023 App Div 1st Dept: 1,784 opinions)
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/new-york/{court-slug}/{year}/{slug}.html`
  - Placeholders: Court of Appeals: the slug is the docket number (2023/94.html; SSM variant 101-ssm-9.html). Appellate Division: the slug is built from the docket identifiers (e.g. ind-no-1032-17-appeal-no-1295-case-no-2018-04146.html). The Slip Op number is not in the URL.
  - Index: `https://law.justia.com/cases/new-york/court-of-appeals/2023/`
  - Navigation: court/year listing → case page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Not readable (403 challenge)
- **Currency:** none
- **Official status:** Justia: opinions 'may not be the official published versions'.
- **Hazard:** Mirrors the uncorrected LRB slip with [*n] markers; no NY3d/AD3d {**} official pagination — use ny-cases-lrb for official pin cites
- **Probe:** NY Court of Appeals 2023 listing → `https://law.justia.com/cases/new-york/court-of-appeals/2023/` — expect: "New York Court of Appeals Decisions 2023"
- **Evidence (2026-10-16):** Both the CoA 2023 and AD1 2023 listings were fetched. No individual case page was fetched. | Independent check 2026-10-16: YES 'New York Court of Appeals Decisions 2023'; links 2023/91.html, 94.html, 95.html; second citation Stoneham v Joseph Barsuk, Inc., 2023 NY Slip Op 06467 ok
- **Notes:** Listing verified; opinion-page body not probed. Case page body verified independently (Stoneham v Joseph Barsuk, 2023/94.html).

## F. Subsequent history

### `ny-history-lrb-motions` — Motion decisions (Court of Appeals leave to appeal; Appellate Division motions) — Law Reporting Bureau

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · New York State Law Reporting Bureau · text: **fetch-and-quote** · official: official
- **Coverage:** Court of Appeals civil motions from February 2003 and criminal leave applications from January 2004. Appellate Division motions: 1st Dept from January 2003, 2d from October 2003, 3d from July 2007, 4th from September 2007. Appellate Term motions: 1st from June 2005, 2d from March 2004.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.nycourts.gov/reporter/motions/{year}/{year}_{nnnnn}.htm`
  - Placeholders: Take the number from 'YYYY NY Slip Op NNNNN' and drop any '(U)'. Verified: 2024_74436 (Court of Appeals, leave denied) and 2023_73590 (2d Dept). In the current month use https://www.nycourts.gov/reporter/current/motions/{year}/{year}_{nnnnn}.shtml (verified for 2026_77266). To find a leave disposition by Court of Appeals motion number: monthly listing https://www.nycourts.gov/reporter/motindex/mots_coa_{MM}-{YYYY}.shtml (verified for 09-2024), whose rows show Title | Motion No. (e.g. 2024-363) | Slip Op No. Appellate Term 2d Dept: mots_at2_{MM}-{YYYY}.shtml (seen in search). Current month: /reporter/current/index/mots_coa_list.shtml, mots_crimleav_list.shtml, mots_ad{1-4}_list.shtml. Other lists: Appeals Dismissed /reporter/motindex/apps_dismissed.shtml and Appeals Withdrawn /reporter/motindex/apps_withdrawn.shtml.
  - Index: `https://www.nycourts.gov/reporter/current/index/mots_coa_list.shtml`
  - Navigation: To go from a case to its leave disposition, use the monthly motion index for the months after the AD decision and search rows by case title. Rows carry the Court of Appeals motion number, not the AD docket, and Court of Appeals pages do not name the decision below.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: See ny-rules-ucr-nycourts
  - The year-archive pages (coa-motions-archive.shtml) show year headings with no links visible to WebFetch, so construct the mots_coa_{MM}-{YYYY} URL instead.
- **Currency:** Page header — observed: "uncorrected and subject to revision before publication in the Official Reports"
- **Official status:** Each motion decision has its own NY Slip Op number. Court of Appeals entries are 'uncorrected and subject to revision before publication in the Official Reports' (they later appear in NY3d tables). Appellate Division motions are '(U)', 'not subject to publication in the Official Reports'.
- **Hazard:** Court of Appeals leave pages do not cite the order appealed from, so match on title and date
- **Hazard:** The Court of Appeals 'Docket No.' column is the motion number (2026-201), not the Appellate Division docket
- **Probe:** Matter of Brown v Annucci, 2024 NY Slip Op 74436 (Ct App) → `https://www.nycourts.gov/reporter/motions/2024/2024_74436.htm` — expect: "Motion for leave to appeal denied."
- **Evidence (2026-10-16):** 74436: 'Motion No: 2024-250', 'Motion for leave to appeal denied.' 73590 (2d Dept): 'ORDERED that the motion is denied.', with the order below and Index No. identified. mots_coa_09-2024 listing OK. | Independent check 2026-10-16: YES 'Motion for leave to appeal denied.'; Motion No 2024-250; 'uncorrected and subject to revision'; second citation Matter of Foreclosure of Tax Liens by County of Albany, 2025 NY Slip Op 65004 (Mot. No. 2024-837) ok
- **Notes:** Leave grants and denials are later printed in NY3d motion tables; their NY3d cite is not on the slip page. The Court of Appeals decision list PDFs (ny-cases-ctapps) also list motions decided each day.

## Not available (do not look for these again)

- **statutes** — Official (certified) online text of the Consolidated Laws: No official statement on nysenate.gov pages, and the Assembly LBDC site is unreachable. New York relies on the printed McKinney's and Gould editions. (2026-10-16)
- **case_law** — Free Official Reports for pre-2003 decisions in HTML: The slip-op reporter starts in 2003. The Official Reports Service (1847-) is on Westlaw and SITE_BLOCKED. Bound-volume PDFs start in 1999, and WebFetch could not see their links. (2026-10-16)
- **admin_code** — Free tier-1 NYCRR text: The DOS page links only to govt.westlaw.com/nycrr, which is SITE_BLOCKED. (2026-10-16)
- **court_rules** — Tier-1 HTML text of the 22 NYCRR Part 1250 Appellate Division practice rules: nycourts.gov/rules/jointappellate lists joint orders with no rule text or links. A PDF on justicetraining.nycourts.gov was found by search and not fetched. (2026-10-16)
- **statutes** — Constitution and NYCRR on public.law: The newyork.public.law/laws index lists neither. (2026-10-16)

## Open questions

- Confirm the archive filename for 'Other Courts' (miscolo) monthly slipidx pages.
- Fetch the Part 1250 PDF (justicetraining.nycourts.gov/courts/ad4/Clerk/Part1250-StatewidePracticeRules.pdf) and decide whether that host is acceptable as tier 1.
- Confirm Part 202 sections after 202.9-a (incl. 202.70) via WebFetch offset=100000 on the nycourts.gov Part page.
- Find the State Register issue PDF URL pattern; the issue page failed via WebFetch.
- Check the CourtListener court IDs (ny, nyappdiv, nyappterm, nysupct, …); they come from memory.
- Check whether the LRB bound-volume PDFs have a constructible pattern (links not visible to WebFetch).
- Confirm Senate LAWIDs for court acts and Workers' Compensation (FCT, SCP, CCA, WKC) on first use.

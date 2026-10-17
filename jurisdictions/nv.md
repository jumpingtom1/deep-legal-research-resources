# Nevada (NV) — free legal sources

_Generated from `data/nv.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, Constitution, court rules (NRCP, NRAP, SCR, RPC, district-court rules) and the NAC are all one-page-per-chapter/rule-set HTML on leg.state.nv.us with constructible URLs and #anchors; fetch_doc.py reads them in full, but WebFetch sees only the first ~110K characters, so later sections of long chapters (NRS 41.130, Const. art. 6, NRAP 36, SCR) need the script or Justia's per-section NRS pages. Case law: the appellate courts' ACIS portal is a JavaScript app, but its public JSON API (acis-api.nvcourts.gov) lists every Supreme Court advance opinion since 2000, Court of Appeals opinions since 2015 and unpublished orders, and serves the PDFs; nvcourts.gov itself is behind a Cloudflare challenge for scripts. Subsequent history (Court of Appeals → petition for review → Supreme Court) sits on the same docket number in ACIS. Justia is the tier-2 fallback for NRS, cases and (stale) Constitution; Cornell LII mirrors the NAC.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Nevada | `nev (unverified)` | Nev. | Nev., P.3d, P.2d, P. | 142 Nev., Adv. Op. 65 (advance-opinion number in the future Nevada Reports volume; replaced by Nev. page cite once printed) |
| Court of Appeals of Nevada | `nevapp (unverified)` | Nev. App. | Nev., P.3d | 142 Nev., Adv. Op. 6 (same Nev. advance-opinion series as the Supreme Court; docket suffix -COA) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Nevada Revised Statutes | `NRS 41.130`; `NRS 11.190(4)(e)`; `Nev. Rev. Stat. § 41.130`; `Nev. Rev. Stat. Ann. § 11.190`; `N.R.S. 41A.035`; `NRS 41.0305 to 41.039, inclusive`; `section 11.190 of the Nevada Revised Statutes`; `section 41.130 of NRS`; `chapter 41A of NRS`; `NRS chapter 116`; `Chapter 41 of the Nevada Revised Statutes` | `nv-nrs-leg` → `nv-nrs-justia` → `nv-nrs-publiclaw` |
| Statutes of Nevada (session laws) | `Statutes of Nevada 2025, p. 3910`; `Statutes of Nevada 2023, at page 1587`; `2025 Nev. Stat. 3910`; `Stats. 2025, ch. 12` | `nv-statutes-of-nevada` |
| Nevada Constitution | `Nev. Const. art. 1, § 8`; `Nev. Const. art. 6, § 4(1)`; `Nev. Const. art. 1, § 8A`; `Nev. Const. art. 4, sec. 21`; `Article 1, Section 8 of the Nevada Constitution`; `Section 4 of Article 6 of the Nevada Constitution` | `nv-constitution-leg` → `nv-constitution-justia` |
| Nevada Rules of Civil Procedure | `NRCP 12(b)(5)`; `Nev. R. Civ. P. 56(c)`; `NRCP 16.1(a)(1)`; `Rule 12(b)(5) of the Nevada Rules of Civil Procedure` | `nv-rules-nrcp` |
| Nevada Rules of Appellate Procedure | `NRAP 36(c)(3)`; `Nev. R. App. P. 40B`; `NRAP 3A(b)(1)`; `Rule 36(c) of the Nevada Rules of Appellate Procedure` | `nv-rules-nrap` |
| Nevada Supreme Court Rules | `SCR 99`; `Nev. Sup. Ct. R. 121.1`; `SCR 121.1`; `Supreme Court Rule 99 (Nevada)` | `nv-rules-scr` |
| Nevada Rules of Professional Conduct | `RPC 1.7`; `Nev. R. Prof'l Conduct 1.7`; `NRPC 8.4(c)`; `Rule 1.7 of the Nevada Rules of Professional Conduct` | `nv-rules-lcb-other` |
| District court and justice court rules (DCR, EDCR, WDCR, JCRCP, NSTR, NRCrP) | `DCR 13`; `EDCR 2.20`; `WDCR 12`; `JCRCP 12(b)`; `NSTR 4` | `nv-rules-lcb-other` |
| Nevada Administrative Code | `NAC 116.010`; `Nev. Admin. Code § 284.010`; `Nev. Admin. Code 116.300` | `nv-nac-leg` → `nv-nac-lii` |
| Register of Administrative Regulations (LCB File No.) | `LCB File No. R001-25`; `R123-21I`; `LCB File No. R058-98` | `nv-register-leg` |
| Nevada advance opinions (Nev., Adv. Op.) | `City of Sparks v. Bluth, 142 Nev., Adv. Op. 65 (2026)`; `142 Nev. Adv. Op. No. 65`; `Griffith v. Rivera, 140 Nev., Adv. Op. 60, 555 P.3d 1171, 1174 (2024)`; `142 Nev. Adv. Opn. No. 6` | `nv-opinions-acis` → `nv-cases-justia` |
| Nevada Reports / Pacific Reporter | `Arabella Mut. Ins. Co. v. Eighth Judicial Dist. Court, 122 Nev. 509, 512, 134 P.3d 710, 712 (2006)`; `135 Nev. 280`; `134 P.3d 710 (Nev. 2006)`; `367 P.3d 1286 (Nev. Ct. App. 2016)`; `485 P.3d 1250 (Nev. App. 2021)` | `nv-nevada-reports` → `nv-opinions-acis` → `nv-cases-justia` |
| Docket numbers and unpublished dispositions (NRAP 36(c)(3)) | `No. 89261-COA`; `Docket No. 90244`; `Smith v. Jones, No. 81234, 2021 WL 4234567 (Nev. Sept. 16, 2021) (unpublished disposition)`; `No. 85000-COA, 2023 WL 1234567 (Nev. Ct. App. Mar. 1, 2023) (Order of Affirmance)` | `nv-opinions-acis` → `nv-cases-justia` |

Regexes (case-insensitive):

- Nevada Revised Statutes: `(?:\bNRS|\bN\.\s*R\.\s*S\.|Nev\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?)\s*(?:§+\s*)?(?P<chapter>\d{1,3}[A-Z]{0,2})\.(?P<section>\d{3,5})(?!\d)|chapter\s+(?P<chapter3>\d{1,3}[A-Z]{0,2})\s+of\s+(?:the\s+)?(?:Nevada\s+Revised\s+Statutes|NRS)\b|\bNRS\s+(?:ch\.|chapter)\s*(?P<chapter4>\d{1,3}[A-Z]{0,2})\b|sec(?:tion|\.)\s+(?P<chapter2>\d{1,3}[A-Z]{0,2})\.(?P<section2>\d{3,5})(?:\([a-z0-9]+\))*\s+of\s+(?:the\s+)?(?:Nevada\s+Revised\s+Statutes|NRS)`
- Statutes of Nevada (session laws): `Statutes\s+of\s+Nevada\s+(?P<year>(?:18|19|20)\d\d),?\s*(?:at\s+)?(?:p\.|page)\s*(?P<page>\d+)|(?P<year2>(?:18|19|20)\d\d)\s+Nev\.\s*Stat\.\s*(?P<page2>\d+)|Stats\.\s*(?P<year3>(?:18|19|20)\d\d),\s*ch\.\s*(?P<chapter>\d+)`
- Nevada Constitution: `Nev\.\s*Const\.\s*art\.\s*(?P<article>\d{1,2}|[IVXL]+),?\s*(?:§|sec\.|section)\s*(?P<section>\d+[A-Z]?)|Article\s+(?P<article2>\d{1,2}|[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Z]?)\s+of\s+the\s+(?:Nevada\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Nevada)|Section\s+(?P<section3>\d+[A-Z]?)\s+of\s+Article\s+(?P<article3>\d{1,2}|[IVXL]+)\s+of\s+the\s+(?:Nevada\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Nevada)`
- Nevada Rules of Civil Procedure: `(?:\bNRCP|Nev\.\s*R\.\s*Civ\.\s*P\.)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Nevada\s+Rules\s+of\s+Civil\s+Procedure`
- Nevada Rules of Appellate Procedure: `(?:\bNRAP|Nev\.\s*R\.\s*App\.\s*P\.)\s*(?P<rule>\d+[A-Z]?)|Rule\s+(?P<rule2>\d+[A-Z]?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Nevada\s+Rules\s+of\s+Appellate\s+Procedure`
- Nevada Supreme Court Rules: `(?:\bSCR|Nev\.\s*Sup\.\s*Ct\.\s*R\.|Supreme\s+Court\s+Rule)\s*(?P<rule>\d+(?:\.\d+)?)`
- Nevada Rules of Professional Conduct: `(?:\bN?RPC|Nev\.\s*R\.\s*Prof'?l\s*Conduct)\s*(?P<rule>\d\.\d+[A-Z]?)|Rule\s+(?P<rule2>\d\.\d+[A-Z]?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Nevada\s+Rules\s+of\s+Professional\s+Conduct`
- District court and justice court rules (DCR, EDCR, WDCR, JCRCP, NSTR, NRCrP): `\b(?P<set>DCR|EDCR|WDCR|FJDCR|JCRCP|NSTR|NATR|NRCrP|NEFCR)\s*(?P<rule>\d+(?:\.\d+)?)`
- Nevada Administrative Code: `(?:\bNAC|Nev\.\s*Admin\.\s*Code)\s*(?:§+\s*)?(?:ch\.\s*)?(?P<chapter>\d{1,3}[A-Z]{0,2})\.(?P<section>\d{3,5})(?!\d)`
- Register of Administrative Regulations (LCB File No.): `(?:LCB\s+File\s+No\.\s*)?\bR(?P<number>\d{3})-(?P<yy>\d{2})(?P<stage>CAP|CA|RP2|RP|AP|NI|NW|NH|A|I|P|W)?\b`
- Nevada advance opinions (Nev., Adv. Op.): `(?P<volume>1[2-9]\d)\s+Nev\.,?\s*Adv\.\s*Op(?:n)?\.\s*(?:No\.\s*)?(?P<number>\d{1,3})`
- Nevada Reports / Pacific Reporter: `(?P<volume>\d{1,3})\s+Nev\.\s+(?P<page>\d{1,4})(?!\d)|(?P<pvol>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<ppage>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Nev\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?P<year>\d{4})\)`
- Docket numbers and unpublished dispositions (NRAP 36(c)(3)): `(?:Docket\s+)?No\.\s*(?P<docket>\d{5})(?P<coa>-COA)?\b|(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)\s*\((?P<court>Nev\.(?:\s*(?:Ct\.\s*)?App\.)?)`

Short forms → URL key:

NRS → `NRS`; N.R.S. → `NRS`; Nev. Rev. Stat. → `NRS`; Nev. Rev. Stat. Ann. → `NRS`; NAC → `NAC`; Nev. Admin. Code → `NAC`; NRCP → `NRCP`; Nev. R. Civ. P. → `NRCP`; NRAP → `NRAP`; Nev. R. App. P. → `NRAP`; SCR → `SCR`; Nev. Sup. Ct. R. → `SCR`; RPC → `RPC`; NRPC → `RPC`; Nev. R. Prof'l Conduct → `RPC`; DCR → `DCR`; EDCR → `EighthDCR`; WDCR → `SecondDCR`; FJDCR → `FirstDCR`; JCRCP → `JCRCP`; NSTR → `NSTR`; NATR → `NATR`; NRCrP → `NRCrP`; NEFCR → `NEFCR`; NRAD → `NRAD`; NCJC → `SCR_CJC`

Nevada's own statutory citation form is 'NRS 41.130' with no section sign (NRS 220.170(4) prescribes it); Bluebook is 'Nev. Rev. Stat. § 41.130'. The section number encodes the chapter (digits and letters before the dot), so NRS/NAC citations are fully constructible. A range 'NRS 41.0305 to 41.039, inclusive' is a span: take the first section. Advance opinions are cited '142 Nev., Adv. Op. 65, ___ P.3d ___ (2026)' (Supreme Court Law Library guide; ACIS docket text writes 'Adv. Opn. No.'); once the Nevada Reports page is printed, cite 'Nev.' with parallel P.3d. Court of Appeals opinions share the Nev. series with no distinct court designation in Nev. cites; Bluebook P.3d-only cites use '(Nev. App. YYYY)' and older practice '(Nev. Ct. App.)'. NRAP 36(c)(3): unpublished dispositions are citable for persuasive value only if issued by the Supreme Court on or after Jan. 1, 2016 or by the Court of Appeals on or after Aug. 15, 2024, cited by docket number and date with '(unpublished disposition)'. Docket numbers are 5-digit; Court of Appeals matters carry '-COA' on the same number, and a petition for review is decided on that same docket. Routing guards: 'SCR', 'RPC', 'DCR' and bare 'Rule 12(b)(5)' are shared with other states — route them here only with Nevada context (Nev./Nevada/NRS nearby). 'NRS', 'NAC', 'NRCP', 'NRAP', 'EDCR', 'WDCR' are Nevada-specific. A bare 'No. 12345' docket, 'Supreme Court Rule N' and 'R001-25' File numbers are generic shapes: route them here only with Nevada context (a '-COA' suffix is Nevada-specific). Nevada has no separate rules-of-evidence set: evidence law is NRS chapters 47-56 (e.g. NRS 48.035), handled by the NRS pattern. A parallel cite ('142 Nev., Adv. Op. 6, 573 P.3d 101 (Nev. App. 2026)') matches both the advance-opinion and the P.3d pattern: prefer the advance-opinion route. WL numbers cannot be turned into free URLs: search ACIS by party name or docket number. CourtListener ids 'nev' and 'nevapp' are from memory and unverified.

## A. Statutes / code

### `nv-nrs-leg` — Nevada Revised Statutes (Legislative Counsel Bureau)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau, Legal Division · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All NRS titles and chapters (Preliminary Chapter = NRS-000), one HTML page per chapter with every section's text and source notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/NRS/NRS-{chapter:03d}{suffix}.html#NRS{chapter:03d}{suffix}Sec{section}`
  - Placeholders: From 'NRS C.S': chapter = digits before the dot, zero-padded to 3, plus any upper-case letter suffix (41 → 041; 41A → 041A; 0.025 → 000). Section = the digits after the dot exactly as written, including leading zeros (41.130 → Sec130; 41.0305 → Sec0305). Anchor = 'NRS' + padded chapter + suffix + 'Sec' + section (NRS041Sec130, NRS041ASec003). Host is case-insensitive (leg.state.nv.us/nrs/nrs-011.html also serves).
  - Index: `https://www.leg.state.nv.us/NRS/`
  - Navigation: Not needed: the title/chapter index lists chapters only (no section ranges), but the chapter is read directly from the section number.
- **Automation:** WebFetch gated · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch on constructed chapter URLs waits on user approval (PROVENANCE_REQUIRED seen for NRS-011, NRS-041 and NRS-041A); use fetch_doc.py as the primary route. WebFetch sees only the first ~106-120K characters of a leg.state.nv.us page in total; offset=100000 reaches the tail of that window and no further (NRS ch. 41: body stops at NRS 41.0395 of 41.970; Constitution: stops in Art. 5 § 9). Everything later is reachable only by fetch_doc.py. Pages are windows-1252 (MS Word export): curly quotes, apostrophes, section signs and non-breaking spaces come out of fetch_doc.py as U+FFFD; quote-verify plain-ASCII runs of words (verify tolerates the whitespace runs).
- **Currency:** first line of each chapter page (varies by chapter) — observed: "[Rev. 4/15/2026 10:45:11 AM--2025] (ch. 41); some chapters '--2025R1'"
- **Official status:** NRS 220.170(3) makes the printed, certified copies of NRS the official codified version and prima facie evidence; the web edition carries no certification or UELMA statement (https://www.leg.state.nv.us/NRS/NRS-220.html).
- **Hazard:** WebFetch reach capped at ~110K characters per page: NRS 41.130 (offset ~120K of 316K in ch. 41) is NOT PRESENT even with offset=100000
- **Hazard:** very long chapters (NRS ch. 200 is ~460 KB of HTML) — use fetch_doc.py or Justia per-section pages
- **Hazard:** windows-1252 encoding: curly quotes and § signs become U+FFFD in fetch_doc.py output
- **Hazard:** revision stamp differs per chapter ('--2025' vs '--2025R1')
- **Hazard:** web edition is not the certified official text (NRS 220.170)
- **Probe:** NRS 11.190 → `https://leg.state.nv.us/NRS/NRS-011.html` — expect: "Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007"
- **Evidence (2026-10-16):** WebFetch ch. 11: 11.190 body YES 'Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007', complete to 11.500. WebFetch ch. 41: 41.130 NOT PRESENT (window ends at 41.0395 even with offset). fetch_doc.py: ch. 41 316,449 chars, verify 'whenever any person shall suffer personal injury by wrongful act' VERIFIED; ch. 11 verify VERIFIED. | Independent check 2026-10-16: WebFetch YES 'Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007'; ch. 11 '[Rev. 4/15/2026 10:40:13 AM--2025]', complete to 11.500; second citation NRS 200.010; NRS 41A.035 ok
- **Notes:** Lettered chapters verified (NRS-041A.html, anchors NRS041ASec003). No bulk download (XML/zip) found on the NRS index. Also mirrored under /Division/Legal/LawLibrary/NRS/.

### `nv-statutes-of-nevada` — Statutes of Nevada (session laws)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Statutes of Nevada by session, HTML split into large page-range files (e.g. Stats2025001.html begins with p. 1); special sessions under e.g. /Statutes/36thSS2025/.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.leg.state.nv.us/Statutes/{session}/Stats{year}{nn}.html#Stats{year}{nn}page{page}`
  - Placeholders: session = '83rd2025', special = '36thSS2025'. Stats{year}001.html is the CONTENTS file; the body is split into two-digit part files Stats{year}01.html ... Stats{year}24.html (2025) with page anchors #Stats{year}{nn}page{page} (e.g. Stats. 2025 p. 269 -> Stats202503.html#Stats202503page269). Stats2025002.html is 404. Which part holds a page is not derivable: follow the contents file's links.
  - Index: `https://www.leg.state.nv.us/Statutes/83rd2025/Stats2025001.html`
  - Navigation: Directory URLs (/Statutes/, /Statutes/83rd2025/) return 403; open the contents file Stats{year}001.html, find the chapter/page, follow its link to the two-digit part file (fetch_doc.py links works).
- **Automation:** WebFetch untested · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - Files are ~300K characters: WebFetch cap applies (see nv-nrs-leg).
- **Currency:** first line — observed: "[Rev. 8/22/2025 11:13:05 AM]"
- **Official status:** No certification statement on the HTML pages.
- **Hazard:** directory listings 403
- **Hazard:** page-to-part-file mapping not derivable
- **Hazard:** contents file is three-digit (...001), body parts two-digit (...01 to ...24)
- **Hazard:** long files exceed WebFetch window
- **Probe:** Statutes of Nevada 2025 (83rd Session), first file → `https://www.leg.state.nv.us/Statutes/83rd2025/Stats2025001.html` — expect: "Statutes of the State of Nevada - Eighty-Third Session, 2025"
- **Evidence (2026-10-16):** fetch_doc.py: 306,320 chars, header 'Statutes of the State of Nevada - Eighty-Third Session, 2025'; first act A.B. 171 'Approved February 13, 2025'. WebFetch not run. | Independent check 2026-10-16: script: offset 85 '[Rev. 8/22/2025 11:13:05 AM] Statutes of the State of Nevada - Eighty-Third Session, 2025'; second citation Stats. 2025, ch. 53 (p. 269) ok
- **Notes:** Low priority; also NRS comparative tables at /NRSCompTbls/.

### `nv-nrs-justia` — Justia — Nevada Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NRS editions by year; unversioned URL serves the 2025 edition; one page per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/nevada/chapter-{chapter}/statute-{chapter}-{section}/`
  - Placeholders: chapter unpadded, letters lower-case in both segments (chapter-41, chapter-41a/statute-41a-035, verified); section part after the dot verbatim (41.130 → statute-41-130). Year-specific: /codes/nevada/{year}/chapter-…
  - Index: `https://law.justia.com/codes/nevada/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (law.justia.com robots.txt returns a Cloudflare challenge to the shell)
  - fetch_doc.py: 'REFUSED: law.justia.com refused automated access earlier (robots.txt challenge)'. WebFetch only. Per-section pages make Justia the practical second fetch for NRS sections beyond the leg.state.nv.us WebFetch window.
- **Currency:** page heading — observed: "2025 Nevada Revised Statutes"
- **Official status:** Page states 'These codes may not be the most recent version' and advises checking official sources.
- **Hazard:** edition lags the official site
- **Hazard:** shell blocked by Cloudflare
- **Probe:** NRS 41.130 → `https://law.justia.com/codes/nevada/chapter-41/statute-41-130/` — expect: "Except as otherwise provided in NRS 41.745, whenever any person"
- **Evidence (2026-10-16):** WebFetch: 41.130 body YES 'Except as otherwise provided in NRS 41.745, whenever any person'; '2025 Nevada Revised Statutes'. Second: /chapter-11/statute-11-190 body YES, 2025 edition. | Independent check 2026-10-16: YES 'Except as otherwise provided in NRS 41.745, whenever any person'; '2025 Nevada Revised Statutes'; second citation NRS 41A.035 ok

### `nv-nrs-publiclaw` — public.law — Nevada Revised Statutes

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NRS, one page per section; statutes only (no Constitution, NAC or court rules for Nevada).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://nevada.public.law/statutes/nrs_{chapter}.{section}`
  - Placeholders: chapter unpadded with any letter suffix as printed; section verbatim (nrs_11.190, nrs_41.1397).
  - Index: `https://nevada.public.law/statutes`
- **Automation:** WebFetch gated · shell ok · robots: not separately recorded; fetch_doc.py allowed the fetch
  - WebFetch of a constructed URL (nrs_200.010) waited on approval (PROVENANCE_REQUIRED); use fetch_doc.py. Source line also shows '(last accessed May 10, 2025)'.
- **Currency:** statutes index header; per-section source line — observed: "Updated May 26, 2025 (index); section: '(accessed May 26, 2025)'"
- **Official status:** Third-party compilation attributing its text to leg.state.nv.us; source line gives an access date.
- **Hazard:** STALE: last updated May 26, 2025, before most 2025-session amendments took effect — compare with nv-nrs-leg before quoting
- **Probe:** NRS 11.190 → `https://nevada.public.law/statutes/nrs_11.190` — expect: "Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007"
- **Evidence (2026-10-16):** WebFetch: body YES, '(accessed May 26, 2025)'. fetch_doc.py info ok (7,990 chars, last-modified 11 May 2025); nrs_41.130 also ok (4,546 chars). Index still reads 'Updated May 26, 2025'. | Independent check 2026-10-16: YES 'Except as otherwise provided in NRS 40.4639, 125B.050 and 217.007'; '(accessed May 26, 2025)'; second citation NRS 200.010 ok
- **Notes:** The lead's 'Updated May 26, 2025' string is unchanged as of 2026-10-16.

## B. Constitution

### `nv-constitution-leg` — Constitution of the State of Nevada (LCB)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution on one page with source notes and pending amendments (e.g. Art. 6 § 3B effective 2028 if ratified).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/Const/NVConst.html#Art{article}Sec{section}`
  - Placeholders: article as Arabic integer (Nevada numbers articles 1-19 in Arabic); section with any letter suffix (Art1Sec8A). The anchor does not change what WebFetch reads.
  - Index: `https://www.leg.state.nv.us/Const/NVConst.html`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch: the first 100K window ends ~Art. 4 § 36; offset=100000 extends only to Art. 5 § 9 (115K of 325K characters); Art. 6 onward needs fetch_doc.py. Pages are windows-1252 (MS Word export): curly quotes, apostrophes, section signs and non-breaking spaces come out of fetch_doc.py as U+FFFD; quote-verify plain-ASCII runs of words (verify tolerates the whitespace runs).
- **Currency:** first line of page — observed: "[Rev. 4/15/2026 4:36:19 PM--2025]"
- **Official status:** Page notes the literal text of the signed original is retained and leadlines are supplied by the Legislative Counsel; no official/authentication statement.
- **Hazard:** single 325K-character page; WebFetch cannot reach Art. 6 and later
- **Hazard:** pending (unratified) amendments printed inline with effective-date notes
- **Probe:** Nev. Const. art. 1, § 8 → `https://www.leg.state.nv.us/Const/NVConst.html` — expect: "No person shall be tried for a capital or other infamous crime"
- **Evidence (2026-10-16):** WebFetch: Art. 1 § 8 YES 'No person shall be tried for a capital or other'; Art. 6 § 4 NOT PRESENT (window ends Art. 5 § 9). fetch_doc.py: verify Art. 1 § 8 VERIFIED; Art. 6 § 4 found at offset 139,492 ('The Supreme Court and the court of appeals have appellate jurisdiction'). | Independent check 2026-10-16: YES 'No person shall be tried for a capital or other infamous'; '[Rev. 4/15/2026 4:36:19 PM--2025]'; second citation Nev. Const. art. 10, § 1 ok

### `nv-constitution-justia` — Justia — Nevada Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Single page, #ArtN anchors.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/nevada/#Art{article}`
  - Placeholders: single page (law.justia.com/nevada/constitution/ also serves); WebFetch reads from character 0 regardless of anchor — use offset=100000 for Art. 6.
  - Index: `https://law.justia.com/constitution/nevada/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - 126K characters; Art. 6 § 19 is cut off in the offset=100000 window.
- **Currency:** none stated
- **Official status:** Third-party copy; no currency date.
- **Hazard:** STALE: Art. 6 § 4 reads 'The supreme court shall have appellate jurisdiction in all civil' — pre-2014 text with no court of appeals
- **Hazard:** articles after Art. 6 unreachable by WebFetch
- **Hazard:** shell blocked
- **Probe:** Nev. Const. art. 1, § 8 → `https://law.justia.com/nevada/constitution/` — expect: "No person shall be tried for a capital or other"
- **Evidence (2026-10-16):** WebFetch: Art. 1 § 8 YES; offset=100000: Art. 6 § 4 'The supreme court shall have appellate jurisdiction in all civil' (differs from official). Use only as last resort. | Independent check 2026-10-16: YES 'No person shall be tried for a capital or other'; no currency string

## C. Court rules

### `nv-rules-lcb-other` — Other Nevada court rules on the LCB court-rules index (RPC, DCR, EDCR, WDCR, JCRCP, NSTR, NRCrP …)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** ~40 rule sets: RPC, District Court Rules, each judicial district's local rules (FirstDCR … EleventhDCR; Second has civil and criminal), justice-court rules, short-trial and ADR rules, NEFCR, NRAD, SCR Parts VI-XI.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/CourtRules/{set}.html#{set}Rule{rule}`
  - Placeholders: set = page key from law_aliases (RPC, DCR, EighthDCR for EDCR, SecondDCR for WDCR, FirstDCR, JCRCP, NSTR, NATR, NRCrP, NEFCR, NRAD, SCR_CJC). Rule '.' → '_' (RPCRule1_7, EighthDCRRule2_20; anchors seen: EighthDCRRule1_10, SecondDCRRule2_1, DCRRule2). EDCR sub-numbers are two digits in anchors: EDCR 2.5 -> EighthDCRRule2_05, EDCR 1.1 -> EighthDCRRule1_01.
  - Index: `https://www.leg.state.nv.us/CourtRules/index.html`
  - Navigation: index lists each set's .html page
- **Automation:** WebFetch untested · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - RPC page 146K characters: WebFetch would stop around RPC 5.x.
- **Currency:** first line of each page — observed: "RPC page last-modified 24 Jun 2025"
- **Official status:** LCB reproduction; no official statement.
- **Hazard:** anchor key differs from citation abbreviation (EDCR → EighthDCR, WDCR → SecondDCR)
- **Hazard:** EDCR anchors zero-pad the sub-number (2.5 -> 2_05)
- **Hazard:** WebFetch cap on long sets
- **Probe:** RPC 1.7 → `https://www.leg.state.nv.us/CourtRules/RPC.html` — expect: "Except as provided in paragraph (b), a lawyer shall not represent a client"
- **Evidence (2026-10-16):** fetch_doc.py: RPC 145,672 chars; 'Rule 1.7. Conflict of Interest: Current Clients.' at offset 33,388 with body '(a) Except as provided in paragraph (b), a lawyer shall not'. Anchors of EighthDCR, DCR, SecondDCR, JCRCP, NSTR confirmed by HTML inspection. | Independent check 2026-10-16: script verify RPC 1.7 phrase VERIFIED at offset 33,420; second citation EDCR 2.20; RPC 8.4 ok
- **Notes:** Evidence: Nevada has no court-rule evidence code; see NRS chs. 47-56.

### `nv-rules-nrap` — Nevada Rules of Appellate Procedure (LCB court-rules page)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete NRAP, one page; header 'Including Amendments Through October 31, 2025'.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/CourtRules/NRAP.html#NRAPRule{rule}`
  - Placeholders: rule with letter suffix as printed (NRAPRule3A); '.' → '_'.
  - Index: `https://www.leg.state.nv.us/CourtRules/index.html`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch window ends in Rule 13(b); Rule 36 NOT PRESENT (fetch_doc.py finds 36(c)(3) at offset ~207K of 252K).
- **Currency:** first lines of page — observed: "[Rev. 9/9/2026 2:04:44 PM--2026R1]; Amendments Through October 31, 2025"
- **Official status:** LCB reproduction; no official statement.
- **Hazard:** WebFetch reaches only Rules 1-13
- **Hazard:** NRAP 36(c) (citation of unpublished dispositions) and 40B (petitions for review) only via fetch_doc.py
- **Probe:** NRAP 36(c)(3) → `https://www.leg.state.nv.us/CourtRules/NRAP.html` — expect: "A party may cite for its persuasive value, if any, an unpublished disposition"
- **Evidence (2026-10-16):** fetch_doc.py: 36(c)(3) VERIFIED at offset 207,738. WebFetch: 36(c)(3) NOT PRESENT; Rule 3A YES 'A party who is aggrieved by an appealable judgment or'. | Independent check 2026-10-16: script verify 36(c)(3) VERIFIED offset 207,738; WebFetch '[Rev. 9/9/2026 2:04:44 PM--2026R1]', ends Rule 13(b); second citation NRAP 3A(b)(1); NRAP 40B ok

### `nv-rules-nrcp` — Nevada Rules of Civil Procedure (LCB court-rules page)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau (rules adopted by the Supreme Court of Nevada) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete NRCP with amendment notes, one page.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/CourtRules/NRCP.html#NRCPRule{rule}`
  - Placeholders: rule number with '.' replaced by '_' (16.1 → NRCPRule16_1; 16.205 → NRCPRule16_205).
  - Index: `https://www.leg.state.nv.us/CourtRules/index.html`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch window ends inside NRCP 16.1(c)(2)(N); Rule 56 NOT PRESENT. 397K characters total — use fetch_doc.py for later rules. Pages are windows-1252 (MS Word export): curly quotes, apostrophes, section signs and non-breaking spaces come out of fetch_doc.py as U+FFFD; quote-verify plain-ASCII runs of words (verify tolerates the whitespace runs).
- **Currency:** first line of page — observed: "[Rev. 4/15/2026 4:39:25 PM--2025]"
- **Official status:** LCB reproduction of Supreme Court-adopted rules; no official statement. Amendment orders (ADKT) are issued by the Supreme Court on nvcourts.gov.
- **Hazard:** WebFetch reaches only Rules 1-16.1
- **Probe:** NRCP 12(b)(5) → `https://www.leg.state.nv.us/CourtRules/NRCP.html` — expect: "failure to state a claim upon which relief can be granted; and"
- **Evidence (2026-10-16):** WebFetch: Rule 12(b)(5) YES; Rule 56(a) NOT PRESENT; truncated in 16.1(c)(2)(N). fetch_doc.py: verify 12(b)(5) phrase VERIFIED at offset 71,730. | Independent check 2026-10-16: WebFetch 12(b)(5) YES 'failure to state a claim upon which relief can be granted'; ends in 16.1(c)(2)(N); second citation NRCP 56(a) ok

### `nv-rules-nvcourts` — Nevada Supreme Court rules and amendment pages (nvcourts.gov)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Nevada · text: **link-only** · official: unknown
- **Coverage:** Rule-amendment pages per rule set and a link to an Administrative Docket (ADKT) order search; per-rule PDFs exist (e.g. /__data/assets/pdf_file/0019/14428/nrcp_1.pdf seen in search, not fetched).
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://nvcourts.gov/supreme/rules/amendments`
  - Navigation: amendments page → per-set amendment page (e.g. /supreme/rules/amendments/nevada_rules_of_appellate_procedure)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: robots.txt itself answers with a Cloudflare 'Just a moment...' challenge
  - fetch_doc.py: 'REFUSED: nvcourts.gov answers robots.txt with a bot check (challenge)'. WebFetch works only on URLs it has been given provenance for (some nvcourts.gov URLs timed out awaiting permission).
- **Currency:** none stated
- **Official status:** Court's own site; makes no statement about which text is official.
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** does not host current rule text on the amendments page
- **Probe:** NRAP amendments → `https://nvcourts.gov/supreme/rules/amendments`
- **Evidence (2026-10-16):** WebFetch: page loads; links to SCR and NRAP amendment pages and an ADKT search; no rule text, no ADKT entries listed.
- **Notes:** Use for amendment history only; quote rule text from the LCB pages.

### `nv-rules-scr` — Nevada Supreme Court Rules, Parts I-V (LCB court-rules page)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** SCR Parts I-V on one page (609K characters); Parts VI-XI (Code of Judicial Conduct, sealing rules, etc.) on separate pages (SCR_CJC.html, SCR_RGSRCR.html …).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/CourtRules/SCR.html#SCRRule{rule}`
  - Placeholders: '.' → '_' (121.1 → SCRRule121_1).
  - Index: `https://www.leg.state.nv.us/CourtRules/index.html`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - Not WebFetched; by the ~110K cap seen on every other LCB page, WebFetch would reach only the first fifth (SCR 99 is at offset ~361K).
- **Currency:** first line of page — observed: "[Rev. 9/9/2026 2:05:02 PM--2026R1]"
- **Official status:** LCB reproduction; no official statement.
- **Hazard:** 609K-character page; WebFetch reach expected to stop early
- **Probe:** SCR 99 → `https://www.leg.state.nv.us/CourtRules/SCR.html` — expect: "Every attorney admitted to practice law in Nevada, specially admitted by a court"
- **Evidence (2026-10-16):** fetch_doc.py: 609,453 chars; 'Rule 99. Jurisdiction.' at offset 361,476 followed by 'Every attorney admitted to practice law in Nevada'. WebFetch not run. | Independent check 2026-10-16: script verify SCR 99 phrase VERIFIED at offset 361,515; second citation SCR 121.1 ok

## D. Administrative code

### `nv-nac-leg` — Nevada Administrative Code (LCB)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** All NAC chapters, one HTML page per chapter; chapter list at /NAC/Chapters.html.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.nv.us/NAC/NAC-{chapter:03d}{suffix}.html#NAC{chapter:03d}{suffix}Sec{section}`
  - Placeholders: File name AND anchor pad the chapter to 3 digits plus any letter suffix: NAC 62B.010 -> NAC-062B.html#NAC062BSec010; NAC 116.010 -> NAC-116.html#NAC116Sec010; NAC 38.350 -> #NAC038Sec350. Section = digits after the dot verbatim.
  - Index: `https://www.leg.state.nv.us/NAC/Chapters.html`
- **Automation:** WebFetch gated · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch worked on NAC-116 only after the URL appeared in a search result; constructed URLs wait on approval — use fetch_doc.py. NAC 116 (88K chars) fits in the WebFetch window; NAC 284 is 529K characters and will not. Pages are windows-1252 (MS Word export): curly quotes, apostrophes, section signs and non-breaking spaces come out of fetch_doc.py as U+FFFD; quote-verify plain-ASCII runs of words (verify tolerates the whitespace runs).
- **Currency:** first lines of each chapter page — observed: "[Rev. 6/7/2026 11:00:00 AM]; [NAC-116 Revised Date: 4-26]"
- **Official status:** NAC title page: compiled and published by the Legislative Counsel 'Pursuant to NRS 233B.062 to 233B.065'; no statement that the web text is official.
- **Hazard:** WebFetch cap on long chapters (NAC 284)
- **Hazard:** windows-1252 encoding
- **Hazard:** /NAC/ index is a title page; chapter list is Chapters.html
- **Probe:** NAC 116.010 → `https://www.leg.state.nv.us/NAC/NAC-116.html` — expect: "As used in this chapter, unless the context otherwise requires,"
- **Evidence (2026-10-16):** WebFetch: 116.010 YES, complete to 116.635, '[NAC-116 Revised Date: 4-26]'. fetch_doc.py: NAC-116 87,593 chars ok; NAC-284 528,863 chars, NAC 284.010 body present at offset ~28K. | Independent check 2026-10-16: WebFetch YES 'As used in this chapter, unless the context otherwise requires,'; '[NAC-116 Revised Date: 4-26]'; second citation NAC 284.010; NAC 62B.010 (anchor check) ok

### `nv-nac-lii` — Cornell LII — Nevada Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NAC chapters with per-section pages and register history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/nevada/NAC-{chapter}-{section}`
  - Placeholders: chapter as printed, section digits after the dot (NAC 116.010 → NAC-116-010). Chapter browse: /regulations/nevada/chapter-{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/nevada`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect the 10-second crawl delay.
- **Currency:** section page, above version comparison — observed: "State regulations are updated quarterly; we currently have two versions available"
- **Official status:** Third-party mirror: 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag (page last-modified Aug 2025)
- **Probe:** NAC 116.010 → `https://www.law.cornell.edu/regulations/nevada/NAC-116-010` — expect: "the words and terms defined in NAC 116.020 to 116.078, inclusive"
- **Evidence (2026-10-16):** fetch_doc.py: verify 'the words and terms defined in NAC 116.020 to 116.078, inclusive' VERIFIED; register note R058-98 present. | Independent check 2026-10-16: script verify 'the words and terms defined in NAC 116.020 to 116.078, inclusive' VERIFIED; second citation NAC 284.010 ok
- **Notes:** Cornell LII hosts no Nevada statutes or constitution (its Nevada page links out to leg.state.nv.us).

## D. Administrative register

### `nv-register-leg` — Register of Administrative Regulations (LCB)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Nevada Legislative Counsel Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Per-regulation PDFs by LCB File No. and stage; yearly numerical and keyword indexes (2010-2026 seen), temporary-regulation indexes, daily updates.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.leg.state.nv.us/Register/{year}Register/R{number:03d}-{yy}{stage}.pdf`
  - Placeholders: From 'LCB File No. R001-25': year = 20+yy, stage = I (initial agency draft), P (LCB proposed), RP/RP2 (revised), NW/NH (notices), NI (informational statement), A (adopted), CA, AP (approved), CAP, W. Which stages exist for a file: the year's index /Register/indexes/{year}_NAC_REGISTER_NUMERICAL.htm.
  - Index: `https://www.leg.state.nv.us/Register/`
- **Automation:** WebFetch gated · shell ok · robots: User-agent * disallows /*.axd, */Reports/*, /App/Opinions/*, */ExhibitDocument/*, two FiscalNote paths; /NRS, /NAC, /Const, /CourtRules, /Register, /Statutes allowed
  - WebFetch of a constructed PDF URL waited on approval (PROVENANCE_REQUIRED); use fetch_doc.py. Agency initial drafts (I) can be image scans: R123-21I is 5 pages with 241 characters of text.
- **Currency:** index pages (last-modified only) — observed: "2025 numerical index last-modified 25 Sep 2026"
- **Official status:** Official register compiled under NRS 233B; no online-authentication statement.
- **Hazard:** initial-draft PDFs may be scanned images (no text)
- **Hazard:** stage suffix must be known
- **Probe:** LCB File No. R001-25 (adopted) → `https://www.leg.state.nv.us/Register/2025Register/R001-25A.pdf` — expect: "ADOPTED REGULATION OF THE BOARD OF PSYCHOLOGICAL EXAMINERS"
- **Evidence (2026-10-16):** fetch_doc.py: R001-25A.pdf 4 pp, 'ADOPTED REGULATION OF THE BOARD OF PSYCHOLOGICAL EXAMINERS LCB File No. R001-25'. WebFetch: R123-21I.pdf returns title and submission note only (scan). | Independent check 2026-10-16: script verify 'ADOPTED REGULATION OF THE BOARD OF PSYCHOLOGICAL EXAMINERS' VERIFIED, 4 pp; second citation LCB File No. R050-24 (adopted) ok

## E. Case law

### `nv-nevada-reports` — Nevada Reports preliminary prints (official pagination)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Nevada · text: **fetch-and-quote** · official: official
- **Coverage:** Vols. 130-140 on the listing. Batches of 4-6 advance opinions with Nev. page numbers; most recent seen: 140 Nev. pp. 467-486 (Adv. Op. Nos. 51-53, 2024) — about two years behind the advance opinions.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: PDF URLs carry CMS asset ids (/__data/assets/pdf_file/0023/51458/140_Nevada_Reports_pages_467-486.pdf); not derivable.
  - Index: `https://nvcourts.gov/supreme/decisions/nevada_reports`
  - Navigation: listing → batch PDF whose page range covers the cited Nev. page
- **Automation:** WebFetch ok (listing only) · shell blocked-challenge · robots: Cloudflare challenge
  - Batch PDF not fetched: WebFetch permission was not granted in time; shell refused by bot check.
- **Currency:** listing — observed: "Volume 140, Adv. Op. Nos. 51-53, pages 467-486"
- **Official status:** Page says the preliminary prints carry Nevada Reports pages, are subject to typographical revision, and the bound volume controls on discrepancy.
- **Hazard:** lags advance opinions by ~2 years
- **Hazard:** shell blocked
- **Hazard:** asset-id URLs
- **Probe:** 140 Nev. 467 → `https://nvcourts.gov/supreme/decisions/nevada_reports`
- **Evidence (2026-10-16):** WebFetch of listing: three newest batches with PDF links (vol. 140 pp. 467-486, 430-466, 375-429). PDF itself not fetched.
- **Notes:** Only free source of official Nev. pagination found; listing reaches back to volume 130 (independent check).

### `nv-opinions-acis` — Nevada Appellate Courts ACIS public API (opinions, orders, dockets)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of Nevada / Nevada Appellate Courts · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court advance opinions from May 2000 (2,125 entries); Court of Appeals opinions from Mar. 2015 (95); dispositional orders (unpublished) for both courts (COA 9,532; Supreme ≥10,000 — counts cap at 10,000); full docket of each case since about 2000.
- **Read via (in order):** **script**
- **Access:** `constructible` · format json
  - Pattern: `https://acis-api.nvcourts.gov/courts/cms/docketentrydocuments?caseHeader.courtID={court_uuid}&docketEntryHeader.docketEntryTypeID={type}&size=25&sort=docketEntryHeader.filedDate,desc`
  - Placeholders: court_uuid: Supreme Court dc01122c-a19d-4eb7-bfe9-5b96e93c26fd; Court of Appeals 74764f58-a87f-4ec5-8233-7a1255e410b3. type: 1000014 = Opinion/Dispositional (advance opinions); 1000018 = Order/Dispositional (unpublished orders); filter a subtype with docketEntryHeader.docketEntrySubTypeID (e.g. 1000233 Opinion on Supreme Court Review, 1000339 Order Denying Petition for Review, 1000336 Order Granting Petition for Review). Date window: docketEntryHeader.docketEntryFiledDateFrom/To. Each row gives documentLinkUUID, caseInstanceUUID, filedDate, docket number, case title and a description that includes the advance-opinion number ('142 Nev. Adv. Opn. No. 65'). PDF: https://acis-api.nvcourts.gov/courts/{court_uuid}/cms/case/{caseInstanceUUID}/docketentrydocuments/{documentLinkUUID} (court_uuid must be the UUID; '1' → HTTP 400). Build the PDF URL from the SAME listing row's caseInstanceUUID with that row's court UUID: Court of Appeals rows carry their own COA case instance (90082-COA: 84f40c27...), different from the Supreme Court instance returned by cases?caseHeader.caseNumber=90082 (bd5396a8...). By docket: GET /courts/cms/cases?caseHeader.caseNumber={docket} (drop any -COA suffix) → caseInstanceUUID and originatingCourtCases; then GET /courts/{court_uuid}/cms/cases/{caseInstanceUUID}/docketentries?size=300 (adding sort= gives HTTP 500). caseHeader.caseNumber is ignored by the docketentrydocuments search.
  - Index: `https://acis.nvcourts.gov/portal/home`
  - Navigation: Human portal (acis.nvcourts.gov) is a Vue app: WebFetch gets an empty shell and its search URLs exceed WebFetch's URL-length limit. Use the API (config: acis.nvcourts.gov/properties.js apiRoot).
- **Automation:** WebFetch gated · shell ok · robots: acis-api.nvcourts.gov/robots.txt → 404 JSON (none); acis.nvcourts.gov/robots.txt returns the SPA HTML (none)
  - fetch_doc.py reads the JSON (as text) and the PDFs (City of Sparks v. Bluth: 9 pp, 14,971 chars). WebFetch on the portal: 'url exceeds the maximum fetchable length'; API URLs not WebFetched (no provenance).
- **Currency:** none; listing is live (newest entries filed 2026-10-16/17)
- **Official status:** Slip opinions and orders; official pagination comes later in the Nevada Reports. Docket-entry JSON marks entries 'official': true (meaning filed record, not reporter text).
- **Hazard:** slip PDFs: no Nev./P.3d pagination; the 'NNN Nev., Advance Opinion NN' label is not in the extracted text — take it from the docket description
- **Hazard:** totalElements caps at 10,000
- **Hazard:** COA document rows use a COA caseInstanceUUID that differs from the cases-search (Supreme Court) id; never mix them in a PDF URL
- **Hazard:** undocumented API: parameter names come from the portal's JS bundle and may change
- **Hazard:** docket-number filter ignored on the document search
- **Probe:** City of Sparks v. Bluth, 142 Nev., Adv. Op. 65 (Oct. 15, 2026), No. 90244 → `https://acis-api.nvcourts.gov/courts/dc01122c-a19d-4eb7-bfe9-5b96e93c26fd/cms/case/61b849df-c16d-4dbf-92f8-d4b2c1e02c99/docketentrydocuments/3e2b60be-61a8-4bb3-bf78-d4faa7367af4` — expect: "we are asked to determine whether the district court abused its discretion"
- **Evidence (2026-10-16):** API search (Supreme, type 1000014, newest first) → Bluth 90244 '142 Nev. Adv. Opn. No. 65'; PDF application/pdf 9 pp; fetch_doc.py verify VERIFIED p. 2. COA: Lorenzo v. Gendebien 90082-COA (June 18, 2026) and Moore v. Primadonna 89261 '142 Nev. Adv. Opn. No. 6' listed. | Independent check 2026-10-16: script verify Bluth phrase VERIFIED p. 2, 9 pp PDF; second citation Lorenzo v. Gendebien, No. 90082-COA, 142 Nev., Adv. Op. 46 (Nev. App. June 18, 2026) ok
- **Notes:** Strongest script candidate in this record.

### `nv-opinions-nvcourts` — nvcourts.gov decision pages (advance opinions, unpublished orders, forthcoming opinions)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Nevada · text: **link-only** · official: unofficial
- **Coverage:** Links to Supreme Court and Court of Appeals advance-opinion and unpublished-order searches in ACIS; forthcoming-opinions notices.
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://nvcourts.gov/supreme/decisions/forthcoming_opinions`
  - Navigation: page links: /supreme/decisions/advance_opinions_enterprise, /supreme/decisions/supreme_court_unplublished_orders_enterprise, and acis.nvcourts.gov search URLs (see nv-opinions-acis)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge on robots.txt
  - advance_opinions_enterprise not fetched (WebFetch permission timed out).
- **Currency:** page metadata — observed: "modified 2026-10-15"
- **Official status:** Landing pages that link into ACIS searches.
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** lists are ACIS links, not documents
- **Probe:** Forthcoming opinions page → `https://nvcourts.gov/supreme/decisions/forthcoming_opinions`
- **Evidence (2026-10-16):** WebFetch: real content (no challenge), links to ACIS opinion/order searches with court UUIDs used in nv-opinions-acis. fetch_doc.py: REFUSED (bot check).

### `nv-cases-justia` — Justia — Nevada Supreme Court and Court of Appeals decisions

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court by year (1960s-2026 seen) and Court of Appeals (2026 listing seen); slip text with Adv. Op. number.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/nevada/{court-slug}/{year}/{docket}.html`
  - Placeholders: court-slug: supreme-court | court-of-appeals. year = decision year. docket = 5-digit number, lower-case '-coa' for Court of Appeals (90244.html, 89261-coa.html). Year listing: /cases/nevada/{court-slug}/{year}/.
  - Index: `https://law.justia.com/cases/nevada/`
  - Navigation: year listing lists decisions with links
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - WebFetch only.
- **Currency:** none
- **Official status:** Listing notes its opinions may not be the official published versions.
- **Hazard:** OCR errors in text ('Prirnadonna', 'sumrnary')
- **Hazard:** no note of later Supreme Court review on Court of Appeals pages
- **Hazard:** unpublished-order coverage unknown
- **Hazard:** shell blocked
- **Probe:** City of Sparks v. Bluth, 142 Nev., Adv. Op. 65 (2026) → `https://law.justia.com/cases/nevada/supreme-court/2026/90244.html` — expect: "In this appeal, we are asked to determine whether the"
- **Evidence (2026-10-16):** WebFetch: '142 Nev., Adv. Op. No. 65', Oct. 15, 2026, body complete. COA: /court-of-appeals/2026/89261-coa.html Moore v. Primadonna '142 Nev. Adv. Op. No. 6', body complete, no review note. | Independent check 2026-10-16: YES 'By the Court, STIGLICH, J.: In this appeal, we are'; '142 Nev. Adv. Op. No. 65'; second citation Lorenzo v. Gendebien, No. 90082-COA (June 18, 2026) ok

## F. Subsequent history

### `nv-subsequent-history-acis` — Petitions for review and later history on the ACIS docket

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of Nevada · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Court of Appeals cases are pushed down from the Supreme Court (NRAP 17) and keep the same 5-digit docket; the petition for review (NRAP 40B), the order granting/denying it and any Supreme Court opinion on review are entries on that one docket. US Supreme Court cert notices are docketed too (subtypes 1000148 cert denied, 1000149 cert filed).
- **Read via (in order):** **script**
- **Access:** `constructible` · format json
  - Pattern: `https://acis-api.nvcourts.gov/courts/cms/cases?caseHeader.caseNumber={docket}`
  - Placeholders: Strip '-COA' from the docket; the case result gives caseInstanceUUID → GET https://acis-api.nvcourts.gov/courts/dc01122c-a19d-4eb7-bfe9-5b96e93c26fd/cms/cases/{caseInstanceUUID}/docketentries?size=300 and read entries typed 'Post-Judgment Petition', 'Post-Judgment Order', 'Opinion/Dispositional' (subtype 'Opinion on Supreme Court Review'), 'Case Status Update' ('Transferred to/from Court of Appeals'), 'Remittitur'. For recent review grants/denials across all cases: docketentrydocuments?docketEntryHeader.docketEntrySubTypeID=1000336 (granted) or 1000339 (denied). From a district-court case number, the case result's originatingCourtCases lists the trial docket.
  - Index: `https://acis-api.nvcourts.gov/courts/cms/cases`
- **Automation:** WebFetch untested · shell ok · robots: none (404)
- **Currency:** live
- **Official status:** Docket entries and orders.
- **Hazard:** no petition-for-review note on Justia COA pages — always check the docket
- **Hazard:** cases search returns the Supreme Court case instance; COA documents hang off a separate COA instance (see nv-opinions-acis)
- **Hazard:** docketentries endpoint returns HTTP 500 when a sort parameter is added
- **Probe:** Moore v. Primadonna Co., No. 89261-COA, 142 Nev., Adv. Op. 6 (Nev. App. Jan. 29, 2026) → review granted → 142 Nev., Adv. Op. 64 (Oct. 15, 2026) → `https://acis-api.nvcourts.gov/courts/cms/cases?caseHeader.caseNumber=89261` — expect: "MOORE VS. PRIMADONNA CO., LLC (CIVIL)"
- **Evidence (2026-10-16):** cases search → caseInstanceUUID d88ba868…, originating A834906; docket: 'Transferred to Court of Appeals' 2025-10-03, COA opinion 2026-01-29 'Adv. Opn. No. 6', petition for review 2026-02-19, 'Order Granting Petition for Review' 2026-04-13, Supreme Court opinion 2026-10-15 'Adv. Opn. No. 64'. Second: Herrmann 92238 'Order Denying Petition for Review' 2026-10-16. | Independent check 2026-10-16: script: cases search → 'MOORE VS. PRIMADONNA CO., LLC (CIVIL)', caseInstanceUUID d88ba868…; second citation No. 90082-COA (Lorenzo v. Gendebien) ok
- **Notes:** Answer to the brief: subsequent history is findable by docket number, not only by party name.

## Not available (do not look for these again)

- **statutes** — Official bulk download (XML/JSON/zip) of the NRS: NRS index (https://www.leg.state.nv.us/NRS/) links chapter HTML pages only; no zip/xml/json links; /Division/Legal/LawLibrary/index.html 404. (2026-10-16)
- **statutes** — Cornell LII copy of NRS / Nevada Constitution: https://www.law.cornell.edu/states/nevada links out to the Legislature and courts; LII hosts only the NAC for Nevada. (2026-10-16)
- **constitution** — public.law Nevada Constitution, NAC or court rules: nevada.public.law home links only /statutes (NRS). (2026-10-16)
- **court_rules** — Tier-2 copy of Nevada court rules (Justia/LII/public.law): None of the three vetted hosts lists Nevada court rules (public.law: statutes only; LII Nevada page links out to nvcourts.gov). (2026-10-16)
- **case_law** — Legacy docket site caseinfo.nvsupremecourt.us: fetch_doc.py: robots.txt unreachable ('Connection reset by peer'); curl HTTP 000. nvcourts.gov now links to acis.nvcourts.gov for opinions and dockets. (2026-10-16)
- **case_law** — Separate vendor-neutral citation (e.g. '2020-Ohio-1234' style): None: the 'NNN Nev., Adv. Op. NN' advance-opinion number is the only public-domain form (Supreme Court Law Library citation guide). (2026-10-16)

## Corpus candidates (maintainers)

- `nv-rules-nrcp` — 397K chars; WebFetch stops in NRCP 16.1
- `nv-rules-nrap` — 252K chars; WebFetch stops in NRAP 13 (36, 40B unreachable)
- `nv-rules-scr` — 609K chars; WebFetch expected to stop in the first fifth
- `nv-constitution-leg` — 325K chars; WebFetch stops in Art. 5 § 9 (Art. 6 judiciary unreachable)
- `nv-nrs-leg` — Long NRS chapters (41: 316K; 200: ~460 KB HTML) exceed the WebFetch window; e.g. NRS 41.130 unreachable
- `nv-rules-lcb-other` — 146K chars; later RPC rules beyond WebFetch window

## Open questions

- WebFetch on acis-api.nvcourts.gov JSON/PDF URLs untested (no URL provenance in this environment); skill may need fetch_doc.py for all ACIS reads.
- Nevada Reports batch PDF not fetched (WebFetch permission timeout; shell blocked) — confirm it carries Nev. page numbers in text and how far back the listing goes.
- SCR and RPC pages not WebFetched; truncation point inferred from the ~110K cap on other LCB pages.
- Whether Justia includes Nevada unpublished orders, and Justia's Supreme Court year range, not checked.
- CourtListener ids 'nev' and 'nevapp' unverified.
- NRAP 36(c)(3) Court of Appeals date (Aug. 15, 2024) read from the LCB text and the Law Library guide; confirm against the ADKT amendment order.

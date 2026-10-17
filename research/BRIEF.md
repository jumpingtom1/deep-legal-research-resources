# Research brief — one jurisdiction, families A–G

You are compiling the free-source record for ONE US jurisdiction for the
`deep-legal-research` skill. Read `SCHEMA.md`
first and follow it exactly. Your deliverables:

1. `data/<xx>.json` — the record, valid JSON
   (no comments), conforming to SCHEMA.md.
2. `research/<xx>-log.md` — a probe log: every
   URL you fetched, tool used, date, and what came back (HTTP code / first
   words / refusal message). Keep quoted page text ≤ 15 words per entry.

## What the skill needs from each source

The skill quotes statutes and rules only after two independent fetches agree,
reads opinions to verify quotes, and cites with official page numbers where
possible. So for every source, the questions that matter are:

- Can a citation be turned into a URL **deterministically**? Prove it on at
  least one real citation (two is better, from different codes/titles).
- Does a WebFetch of that URL return the **body text** (not just a table of
  contents, not a JS shell)? Long pages: does the text truncate? Where?
- Is there a **currency / edition statement**? Record the literal string.
- Is the online text **official**? Look for the publisher's disclaimer.
- Does the host allow automation? Fetch `robots.txt`. Test the shell too
  (`curl -sS -m 20 -o /dev/null -w '%{http_code}' URL`); a Cloudflare
  `cf-mitigated: challenge` header or 403 = `blocked-challenge`. Note that
  the end-user's sandbox may have a narrower network allowlist than this one;
  record what you saw.
- For case law: coverage years; HTML or PDF; does the PDF carry official
  reporter page numbers or only slip pagination; can an opinion be located
  from (court, docket number, date) via a listing page or a stable URL; is
  there any JSON API or structured listing (→ `script_candidates`).
- For subsequent history: where review/leave dispositions are published and
  whether they are findable by docket number.

## Rules

- **Tier 1 = official/government. Tier 2 = public.law, Justia, Cornell LII
  only.** Record tier-2 rows for every family where they exist, even when
  tier 1 is good — they are the fallback. No other third parties.
- **Never work around a block** (robots, challenge, login, "site blocked").
  Record it as `blocked` with the evidence and move on.
- **Do not use any CourtListener tool.** Its budget is precious. Give
  `courtlistener_id` values from your knowledge and add
  `"courtlistener_id_unverified": true` to each court entry.
- **Do not reproduce statute or opinion text** beyond ≤ 15-word evidence
  snippets. No full sections in the JSON or the log.
- WebFetch prompts: ask narrowly ("Does this page contain the body text of
  section X? Answer YES/NO, then the first 10 words of that section's body,
  then any currency/edition/'current through' statement verbatim, then
  whether the page appears truncated"). For long pages use the anti-
  fabrication wording: "do not infer text from a heading; if the body text
  of X is not actually present answer exactly NOT PRESENT".
- `WebSearch` is fine for discovering where things live; confirm every URL by
  fetching it. A URL you did not fetch is at most `reported`.
- Budget: aim for ≤ 60 WebFetch calls. Prioritise A (statutes), E (case
  law), G (citation map), then C, F, B, D. If you run low, record remaining
  items as `reported` with an `open_questions` entry rather than skipping.
- Today is 2026-10-16. Use it for every `date` field. `verification.by` is
  `"research"`.

## Finish

Validate the JSON (`python3 -c "import json;json.load(open(...))"`). Your
final message: ≤ 200 words — counts of verified/reported/blocked/absent
rows, the three most important findings (especially anything blocked or
surprising), and any schema field that did not fit this jurisdiction.

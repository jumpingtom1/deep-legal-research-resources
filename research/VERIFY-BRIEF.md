# Independent verification brief

You are checking ONE jurisdiction's source instructions cold. The question is
not "is the research good?" but **"can a fresh research run follow these
instructions and get the promised result?"**

The repo root is `/home/claude/deep-legal-research-resources`. Read ONLY `jurisdictions/<xx>.md` (and
`SCHEMA.md` for vocabulary). Do **not** read `data/<xx>.json`,
`research/<xx>-log.md`, or any other research file — independence is the
point.

## For every row marked VERIFIED

1. **Probe.** Fetch the row's probe URL with WebFetch, asking narrowly
   whether the expected body text is present (YES/NO, first ~10 words of the
   body, any currency/edition string verbatim, truncation?). Compare with the
   row's "expect" and "Currency observed" strings.
2. **Generalise** (constructible and index-anchored rows only). Pick a
   *different* real citation of the same family — ideally a different code,
   title or court than the probe — and follow the row's pattern/navigation
   exactly as written. Did it reach the body text? If the instructions were
   ambiguous or wrong, say exactly where.
3. For case-law rows: locate one real recent opinion (from the listing the
   row describes) by court + docket/date as the instructions say, and check
   the claimed format/pagination features.

4. Where the row lists the **script** route (or to test it), run
   `python3 scripts/fetch_doc.py --research grep <url> "<a phrase>"` and
   record whether it reached the text (REFUSED / TLS errors are findings,
   never something to work around).

## For every row marked REPORTED

One WebFetch of its probe/index URL; outcome `confirmed` (body text reachable
as described) or `failed`, with evidence.

## For every row marked BLOCKED

One WebFetch of its probe/index URL only (the same route the record names).
Confirm it is still refused. Never try another route, the shell, a mirror or
a cache.

## Citation map

Write five realistic citations for this jurisdiction that are NOT among the
listed examples (mix of families and citation styles, including prose like
"section 1714 of the Civil Code"). Test each against the regexes with
python (`re.search(rx, s, re.I)`), and record misses and false routes.

## Output

Write `research/<xx>-verify.json`:

```json
{
  "jurisdiction": "<xx>",
  "date": "2026-10-16",
  "rows": [
    {"id": "...", "outcome": "confirmed | discrepancy | failed | still-blocked | unblocked",
     "probe_evidence": "≤15 words seen / error",
     "generalised_citation": "...", "generalised_url": "...", "generalised_outcome": "ok | failed | n/a",
     "instruction_problems": "where a fresh run would go wrong, or ''",
     "suggested_fix": ""}
  ],
  "regex_tests": [{"citation": "...", "matched_label": "... | null", "expected_label": "..."}],
  "overall": "≤120 words"
}
```

Do not edit any other file. No CourtListener tools. Keep quoted page text
≤ 15 words per entry. Budget ≤ 45 WebFetch calls. WebFetch may wait on an approval prompt for URLs you built yourself; do not retry — run the probe with `python3 scripts/fetch_doc.py --research` instead (that counts as a confirmed probe) and say so in probe_evidence. If WebFetch fails for quota/rate reasons (not a site refusal), stop and write what you have. Today is 2026-10-16.
Final message: ≤ 150 words — counts by outcome and the most serious
instruction problems.

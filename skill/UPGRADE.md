# Upgrading the deep-legal-research skill

This folder always holds the newest release of the skill:

| File | What it is |
|---|---|
| `latest.json` | Version, release date, **what's new** (this release and the history of earlier ones), feedback contact, sha256 and file list. The skill checks this file. |
| `deep-legal-research.zip` | The newest release, **minus the GovInfo API key** (see below). |

## How you'll hear about a new version

At the start of every research run, the skill runs `scripts/update_check.py`.
When this folder holds a newer version than the one you have installed, the
skill does four things:

1. It shows **What's new**: the short notes for every release since yours.
2. It hands you a file named `deep-legal-research-v<X.Y>.zip`. That file is
   ready to upload, with your GovInfo key already copied in from your
   current installation.
3. It lists the steps below.
4. It carries on with your research on the version you have.

(Installations of v10.4 show steps 2–4 only. From v10.5 on, What's new is
shown too.)

## Steps

1. Download the zip the skill gave you.
2. In Claude, open **Customize → Skills**.
3. Find **deep-legal-research**, switch it off, click the **…** next to the
   toggle, choose **Delete** and confirm. An uploaded skill can't be
   replaced in place.
4. Click **+**, then **+ Create skill**, then **Upload a skill**, and choose
   the downloaded zip.
5. Switch the new skill on and start a new chat.

**Team / Enterprise.** If your organization provisions this skill for you,
send the zip to your Claude organization owner instead. They publish the
new version for everyone.

Source: Claude Help Center, [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
and [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
read 2026-10-17.

## Changing the skill yourself

Please don't. Send suggestions to the maintainer instead (the `feedback`
contact in `latest.json`).
- An upgrade replaces the whole skill, so local edits are lost.
- From v10.5 on, every release carries `MANIFEST.sha256`, a fingerprint of
  each file. The update check compares your copy with it. If anything was
  changed, removed or added, it tells you so and gives you the maintainer's
  contact.
- If you ask Claude to change the skill, it won't. It writes your
  suggestion up as a short note for you to send.

Nothing can stop someone from editing their own copy: the files are on their
account. The fingerprint makes edits visible, and the next upgrade
overwrites them.

## Why the public zip has no API key

The skill bundles an api.data.gov key (`scripts/govinfo.key`) for GovInfo.
The key may be shared with colleagues but must never be posted publicly, and
this repository is public. So:

- `scripts/release_skill.py` leaves the key out of
  `deep-legal-research.zip` and lists it in `latest.json` under
  `preserve_local`.
- When a user upgrades, the update check reads the key from their
  **installed** skill and writes it into the zip it hands them. The key
  passes from each user's old version to their new one, on their own
  account, and never travels through GitHub.

**Do not upload `deep-legal-research.zip` from this folder directly.** It has
no key, so GovInfo lookups would fail.

## First install for a colleague

A new user has no installed copy to take the key from, so they need the
**colleague zip**: the same release with the key inside.

- The maintainer makes it at release time with `--private-out` (below). It
  is named `deep-legal-research-v<X.Y>-with-key.zip`.
- Send it privately: e-mail, a shared drive, Teams/Slack. Never put it in
  this repository or anywhere public.
- The colleague installs it with steps 2, 4 and 5 above (there's nothing to
  delete). After that, upgrades come automatically, with the key carried
  forward.
- Anyone who already has the skill can also pass on the zip the update check
  gave them, since it includes their key.
- On Team/Enterprise plans, the org owner can upload the colleague zip once
  for everyone instead.

## Publishing a new release (maintainer)

1. Finish the release in a copy of the complete skill folder, including the
   skill's own checklist in `CHANGELOG.md`.
2. Write the release notes: a short file of `- ` bullets (1–8, each at most
   200 characters), in plain language, saying what upgrading gets the user.
   For example: `- Rhode Island court rules can now be quoted.`
3. From the repo root, run:
   `python3 scripts/release_skill.py <path-to>/deep-legal-research --notes NOTES.md --private-out <folder outside the repo>`
4. Commit `skill/latest.json` and `skill/deep-legal-research.zip`, then
   push to `main`. Send the `-with-key` zip from step 3 to any new
   colleagues.

The script refuses to publish if:
- there are no release notes, or the notes are too long;
- the version isn't higher than the one already published;
- a file from the previous release is missing;
- a remaining file looks like it holds a credential;
- `--private-out` points inside the repository.

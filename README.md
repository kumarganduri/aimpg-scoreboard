# aimpg scoreboard

Do token-savers, prompts, models and agents really save money on real code? This repo collects
results from [`aimpg verify`](https://github.com/kumarganduri/aimpg), which reruns a developer's own past
commits both ways in a sandbox and lets their own tests judge them. The page adds them up across many
projects.

**Page:** https://kumarganduri.github.io/aimpg-scoreboard

## Add your result

```bash
uv tool install aimpg
aimpg verify --repo ~/your-project --challenger rtk      # or a model, a prompt, codex, ...
aimpg submit ~/.aimpg/verify/<the record>.record.json    # shows exactly what's sent, asks, opens a pull request
```

`aimpg submit` needs the GitHub CLI (`gh auth login`). Your GitHub username appears with your submission.

## What's published

| | Private record (default) | `--public` record |
|---|---|---|
| Model, setup, pass/fail per run | ✓ | ✓ |
| Cost (to the cent), time (to 10 s), token sums (2 significant figures), energy range | ✓ | ✓ |
| Week of the run | ✓ | ✓ |
| Repo name / URL, commit ids | ✗ | ✓ (so anyone can rerun it) |
| Your prompts, CLAUDE.md, settings, commands | ✗ | ✓ |
| Code, diffs, commit messages, test output | ✗ never | ✗ never |

## How results are counted

- **One repo, one vote.** The newest record per repo counts; each account counts for at most 3 repos per claim.
- **A number appears only when there's enough behind it:** at least 5 repos and 3 people, and nobody supplying more than half of the runs.
- **Medians, never averages**, so one extreme repo can't swing a result.
- **Trust tiers:**
  - **Reproduced:** someone else reran a public record (`aimpg verify --rerun`) and got the same answer. Only these make the headline.
  - **Self-reported:** shown separately, labeled "not audited".
  - **Disputed:** a rerun disagreed. Both are shown; neither counts.
- **Vendors:** records from accounts listed in [`vendors.json`](vendors.json) about their own product count only once reproduced by someone else. Please state your affiliation when you submit.
- **Every run counts**, failures included. Incomplete records are rejected, and redone attempts are listed.

**What this can't prove:** `aimpg verify --check` confirms a record's arithmetic and consistency, not that its
runs happened. A determined person can fake a self-reported record, which is why only independent reruns reach
the headline.

## Withdraw

Open a pull request that deletes your file under `records/<your-username>/`. The page rebuilds when it's merged.
Copies others already downloaded can't be recalled.

## How this repo works

- `records/<github-username>/<sha256>.json`: one file per submission; the file name is the SHA-256 of its content.
- `.github/workflows/validate.yml`: on every pull request, checks that you only add or delete your own files, then
  runs `aimpg scoreboard validate`: format, privacy, consistency, complete runs and the verdict arithmetic.
  It uses `pull_request` (a read-only token) and never executes anything from a record.
- `.github/workflows/pages.yml`: on merge, `aimpg scoreboard build` makes the page (rules in
  [aimpg/scoreboard.py](https://github.com/kumarganduri/aimpg/blob/main/aimpg/scoreboard.py)).
- Data license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

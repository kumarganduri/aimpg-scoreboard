# Bring Your Claim

Does your token-saver, router, prompt pack, agent or model save money on real code? Prove it here, in the open, on the same rules for everyone.

## How it works
1. **Submit your setup.** Open an issue titled `Claim: <your setup>` with:
   - what it claims (for example "cuts tokens 40%" or "same results at half the cost");
   - how to install it as an `aimpg verify` challenger: a Claude Code prompt, CLAUDE.md, `settings.json` (hooks), a model, Codex, or any agent command (`cmd:'tool ... {task}'`);
   - your affiliation.
2. **It runs on the pre-registered protocol of the current report:**
   - the same public repos;
   - commits chosen by rule (the first qualifying commits after every model's training cutoff);
   - hidden tests, 3 repeats;
   - the same statistics.

   The protocol is fixed before any run. See [Report No. 1's pre-registration](https://github.com/kumarganduri/aimpg/blob/main/docs/study/report-1/PREREGISTRATION.md).
3. **Every run is published,** failures included, as `--public` records anyone can rerun with `aimpg verify --rerun`.
4. **You get a right of reply,** published next to the results.

You can run it yourself and submit with `aimpg submit`. Your own results are listed as **Self-reported** until someone unconnected to you reruns them.

## The badge
A setup earns **"Verified by aimpg"** only when all of these hold:
- the result is **SUPPORTED** under the protocol's headline rule (Holm-adjusted, holding in at least 5 of 6 repos);
- at least one person **unconnected** to the vendor has reproduced it (the **Reproduced** tier);
- no rerun disputes it.

The badge links to the exact records. It states the measured effect, for example `aimpg verified: −38% tokens per task (8 repos)`, never a vague "approved".
- **Disputes:** if a later rerun disputes the result, the badge reads "disputed" until it's resolved.
- **Versions:** results apply to the version tested. A new major version needs a new run.

## What we won't do
- Change the protocol for one entrant, or rerun something because the result was disliked.
- Hide results that don't flatter anyone, including our own tools.
- Accept payment to test, rank or word anything.

## Costs
Runs cost API money: roughly $0.10–0.30 per run, a few hundred runs per claim. The maintainer funds a limited number of runs per report. Entrants can run the protocol on their own API key; the result then still needs an independent rerun to count.

# RESUME (2026-10-23)

## Current state
- Fork `c10vis-poem/NvAEx-code-review-graph`, default branch `main` at 56685c6 (2026-10-23). This fork has no `staging`/`testing` branches on origin, so PRs here target `main` (branch protection on `main` requires status checks: lint, type-check, security, ...). The upstream branching model in CLAUDE.md (`staging` base) applies to upstream contributions only.
- Open PRs on the fork: none.

## Changed this week (2026-10-18..2026-10-23)
- PR #2: skip ignored paths before `stat` and tolerate `OSError` during file collection. `collect_all_files` rglob fallback called `is_file()` on ignored paths (e.g. `Drive_sync/`) before `_should_ignore`; on Python 3.14 an ENAMETOOLONG crashed the Obsidian-vault graph build. `_reconcile_stale_files` had the same ordering. Files: `code_review_graph/incremental.py`, `tests/test_collect_skips_ignored_before_stat.py` (2 tests; fail without the fix).

## Open items (in order)
1. Consider offering PR #2 upstream (`tirth8205/code-review-graph` lineage) if the fix is not already there.
2. Remote branch `origin/fix/collect-skip-ignored-before-stat` still exists after merge; delete only if the operator says so.
3. Track follow-ups with `bd` (not markdown lists), per AGENTS.md. `bd` is not installed in this Termux shell, so no issues were filed.

## Next steps
- Rebuild the vault graph with the fixed version and confirm no ENAMETOOLONG on Python 3.14.

## Notes
- AGENTS.md says do not use MEMORY.md or markdown TODO lists here (`bd remember`, `bd`), so no MEMORY.md/PENDING.md were created in this wrap-up.
- Operator dropped OmniRoute, mem0, Terrestrial Brain, OpenWiki and Qwen3-VL from the stack on 2026-10-23; no docs in this repo were found routing through them (grep over *.md, see Sources).

## Sources
Read: AGENTS.md, CLAUDE.md (via session context), `git log origin/main --since=2026-10-18`, PR #2 body/files, branch protection on `main`, grep of *.md for dropped tools. Not read: CONTRIBUTING.md, docs/, beads database, CI run logs.

# Profile Dynamic Modules

**Status:** ACTIVE AFTER MERGE  
**Scope:** Latest writing and selected public build signals only

## Purpose

Keep two small GitHub profile regions current without allowing automation to rewrite the full README or publish unsupported claims.

## Controlled regions

The updater may change content only between these marker pairs:

```text
<!-- DYNAMIC:WRITING:START -->
<!-- DYNAMIC:WRITING:END -->
```

```text
<!-- DYNAMIC:SIGNALS:START -->
<!-- DYNAMIC:SIGNALS:END -->
```

Changing content outside those regions is out of scope for the refresh workflow.

## Sources

Source configuration lives in `data/profile_sources.json`.

### Writing

- Public Substack feed candidates only.
- Maximum of three entries.
- A permanent link to the public Substack profile remains visible.

### Build signals

- Latest public Zeref Memory Engine release.
- Latest merged PerFin OS pull request authored by `kanadhiayash` and targeted to `dev`.
- Maximum of two signals.

The source list is deliberately small. Additions require a reviewed configuration change.

## Failure behavior

The updater fails closed:

- A failed or invalid remote source does not blank a README region.
- The last reviewed content remains in place.
- Invalid marker structure or configuration fails the workflow.
- Only HTTPS sources on the Substack and GitHub allowlists are accepted.

## Pull request behavior

The scheduled workflow does not commit directly to `main`.

When content changes, it creates or updates:

```text
automation/profile-refresh
```

A reviewer must verify titles, links, dates, relevance, attribution, and public safety before merge.

## Schedule

The workflow runs weekly on Monday and also supports manual execution through `workflow_dispatch`.

## Local commands

Validate structure without network access:

```bash
python3 scripts/update_dynamic_modules.py --check
```

Fetch public sources and update bounded regions:

```bash
GITHUB_TOKEN="${GITHUB_TOKEN:-}" python3 scripts/update_dynamic_modules.py --write
```

Review the generated diff:

```bash
git diff -- README.md
```

## Excluded modules

Do not add:

- visitor, follower, repository, or contribution counters,
- streak cards,
- raw commit feeds,
- random quotes,
- Spotify widgets,
- live clocks,
- unreviewed social activity,
- generated claims about impact, quality, adoption, or production readiness.

## Ownership and positioning

Dynamic content must preserve the locked profile decisions:

- Product Designer remains the sole title.
- PerFin OS remains a MADS team project.
- Development and AI-assisted execution remain supporting proof.
- Zeref and PerFin remain the primary build-signal sources.

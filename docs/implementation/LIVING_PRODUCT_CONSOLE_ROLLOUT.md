# Living Product Console Rollout

**Status:** ACTIVE, MOTION REVIEW OPEN  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`  
**Current branch:** `feat/profile__living-motion-layer`

This file tracks the controlled rollout of the GitHub profile redesign. Each phase remains reviewable and preserves the locked public positioning decisions.

## Phase 1: Information architecture and copy

**Status:** COMPLETE

Delivered:

- Product Designer remains the sole public title.
- Toronto, Ontario, Canada remains the public location.
- The approved tagline leads the profile.
- Selected work is the primary internal CTA.
- LinkedIn is the primary external CTA.
- Zeref Memory Engine and PerFin OS are the two flagship anchors.
- PerFin OS is credited to Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq.
- For Rent and StreamNexus form the built-product support lane.
- Arthenticate and DriveDeal form the Figma product-design lane.
- Five selected credentials are shown.
- Six Sigma Yellow Belt is excluded.
- The approved tool row is Figma, React, Swift, Firebase, Claude, and Codex.
- Development and AI-assisted execution remain supporting proof.

## Phase 2: Hero visual and motion system

**Status:** STATIC AND MOTION ASSETS COMPLETE, GITHUB RENDER REVIEW OPEN

Locked decisions:

- Use the approved dark Living Product Console as the only active hero direction.
- Do not publish a light-mode hero for the current release.
- Use Product Designer as the sole title.
- Show Toronto, Ontario, Canada.
- Show the approved tagline.
- Use exactly these metrics: 2 shipped projects, 1 MADS team project, 5 selected certifications.
- Use only Figma, React, Swift, Firebase, Claude, and Codex in the tool row.
- Keep Zeref Memory Engine and PerFin OS as the dominant visual cards.
- PerFin OS must carry the MADS team project cue and must not imply solo ownership.
- Use one animated hero above the fold and no competing large animation.
- Keep the approved PNG directly accessible as the static alternative.

Approved asset family:

`yash-kanadhia-living-product-console-dark`

Delivered repository files:

- `assets/hero/yash-kanadhia-living-product-console-dark-motion.svg`, active animated hero.
- `assets/hero/yash-kanadhia-living-product-console-dark.png`, static alternative.
- `assets/hero/yash-kanadhia-living-product-console-dark.jpg`, compressed preview.
- `assets/hero/yash-kanadhia-living-product-console-dark.svg`, static placement wrapper.

Motion delivered:

- Slow card-border breathing.
- Zeref project-state pulse.
- PerFin orbital project indicator.
- Restrained scanning light across the console.
- Sequential live-signal dots.
- Moving signal along the lower console rail.
- No rapid flashing, hard cuts, or unique motion-only information.

Verified:

- The README references the animated SVG as the active hero.
- The README provides the PNG through an expandable static alternative.
- Both hero images include descriptive alt text.
- Static file signatures, PNG dimensions, and the approved wide aspect ratio remain governed by the existing release validator.
- Superseded banner assets remain removed.

Open manual check:

- Review the animated SVG on the rendered GitHub profile in desktop light appearance.
- Review the animated SVG on the rendered GitHub profile in desktop dark appearance.
- Review the animated SVG and static alternative at narrow mobile width.
- Confirm GitHub or its image proxy does not suppress the SVG animation.

## Phase 3: Project media

**Status:** STATIC RELEASE COMPLETE, VERIFIED CAPTURE ENHANCEMENTS OPEN

Delivered:

- Added `assets/projects/flagship-systems.svg` for Zeref Memory Engine and PerFin OS.
- Added `assets/projects/built-product-proof.svg` for For Rent and StreamNexus.
- Added `assets/projects/product-design-studies.svg` for Arthenticate and DriveDeal.
- Integrated all three boards into the README with descriptive alt text.
- Preserved independent and team ownership boundaries.
- Preserved product limitations and avoided deployment claims.
- Added `docs/media/PROJECT_MEDIA_MANIFEST.md` as the source and replacement policy.
- Avoided StreamNexus placeholder screenshots as final public proof.
- Kept Arthenticate and DriveDeal labeled as interactive Figma studies with public case-study packaging in progress.

Open enhancement backlog:

- Add a short Zeref product demonstration loop beyond the profile hero, with a still equivalent.
- Add verified PerFin OS screenshots and a short workflow recording.
- Add verified For Rent renter and landlord captures.
- Replace StreamNexus repository placeholders with verified runtime captures.
- Add approved Arthenticate and DriveDeal prototype media.

The enhancement backlog does not block the Living Product Console hero release. It remains required before claiming a media-complete portfolio.

## Phase 4: Controlled dynamic modules

**Status:** COMPLETE

Delivered:

- Added bounded latest-writing and selected-build-signal regions to `README.md`.
- Added explicit start and end markers for both generated regions.
- Added `data/profile_sources.json` as the reviewed source allowlist.
- Added `scripts/update_dynamic_modules.py` using only the Python standard library.
- Limited writing output to three public Substack entries.
- Limited build output to two signals from Zeref Memory Engine and PerFin OS.
- Added HTTPS and host allowlists for Substack and GitHub.
- Preserved the last reviewed README content when a source fails.
- Added offline marker and configuration validation.
- Added `.github/workflows/profile-refresh.yml` for weekly and manual refreshes.
- Configured automation to open or update `automation/profile-refresh` instead of committing directly to `main`.
- Added `docs/automation/PROFILE_DYNAMIC_MODULES.md` as the operating and review guide.
- Excluded vanity counters, streak cards, random quotes, Spotify widgets, and raw commit feeds.

Post-merge operational check still required:

- Run Profile Refresh manually.
- Review the resulting automation pull request if content changes.
- Confirm generated changes stay inside the two marker regions.
- Confirm a source failure preserves the previous reviewed content.

## Phase 5: Quality gates and release

**Status:** AUTOMATED GATES COMPLETE, MANUAL MOTION REVIEW OPEN

Delivered:

- Added `scripts/validate_profile_release.py` as the deterministic release validator.
- Added `scripts/validate_profile_foundation.py` to verify non-hero release conditions independently.
- Added `scripts/validate_profile_links.py` with GET confirmation for unreliable HEAD responses.
- Added `.github/workflows/profile-quality.yml` as the pull-request, main-branch, and manual quality gate.
- Added `docs/qa/PROFILE_RELEASE_CHECKLIST.md` as the final automated and manual review record.
- Added checks for locked copy, project attribution, selected credentials, approved tools, metrics, and dynamic markers.
- Added checks for local assets, internal anchors, HTTPS links, alt text, placeholders, private paths, and common secret patterns.
- Added static hero file, dimension, aspect-ratio, README-reference, and alt-text requirements.
- Added a downloadable `profile-link-report` workflow artifact.
- Replaced the unpublished Zeref GitHub Release URL with the verified repository release record.

Verified automated results before the motion branch:

- Profile foundation: PASS.
- Release readiness: PASS.
- Online link gate: PASS.
- LinkedIn and Substack access restrictions are warnings, not confirmed broken links.

Motion-branch requirements:

- Existing automated gates must remain green.
- Animated SVG must resolve as a local README image with non-empty alt text.
- Static PNG must remain referenced exactly once as the accessible alternative.
- No locked title, metric, tool, credential, attribution, or dynamic-marker value may drift.

Remaining release checks:

- GitHub light appearance motion render review.
- GitHub dark appearance motion render review.
- Narrow mobile motion render review.
- Manual Profile Refresh run and review.
- Final public-claim and ownership review.
- Explicit merge approval for the motion pull request.

Release decision:

Do not call the motion layer released until its pull request passes the automated gates and the rendered GitHub profile is manually reviewed.

## Current risks

- GitHub or its image proxy may suppress some SVG animation features. The static PNG remains available if that occurs.
- The approved static hero is generated raster artwork. Its static SVG export is an embedded-image wrapper rather than editable vector paths.
- The animated hero is a separate reconstructed vector presentation and may differ slightly in typography from the static raster artwork.
- Verified project screenshots and recordings remain an enhancement backlog and must not be represented as already published.
- Substack feed availability still requires a live manual Profile Refresh run.

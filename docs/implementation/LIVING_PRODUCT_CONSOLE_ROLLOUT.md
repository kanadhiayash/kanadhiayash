# Living Product Console Rollout

**Status:** ACTIVE  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`  
**Branch:** `docs/profile__lock-public-positioning`

This file tracks the controlled rollout of the GitHub profile redesign. Each phase should remain reviewable and should preserve the locked public positioning decisions.

## Phase 1: Information architecture and copy

**Status:** COMPLETE ON REVIEW BRANCH

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

Verification required before merge:

- Render README in GitHub light theme.
- Render README in GitHub dark theme.
- Check mobile-width readability.
- Confirm every public link resolves.
- Confirm project attribution and limitations remain accurate.

## Phase 2: Hero visual system

**Status:** NEXT

Planned:

- Replace the existing static banner with the approved Living Product Console hero.
- Use Product Designer as the sole title.
- Show Toronto, Ontario, Canada.
- Show the approved tagline.
- Use exactly these metrics: 2 shipped projects, 1 MADS team project, 5 selected certifications.
- Use only Figma, React, Swift, Firebase, Claude, and Codex in the tool row.
- Produce light and dark static assets.
- Produce one restrained animated asset only after the static composition is approved.
- Include accessible alt text and a still equivalent.

## Phase 3: Project media

**Status:** PLANNED

Planned:

- Add Zeref product-system visual or motion proof.
- Add PerFin OS verified screenshots and a short workflow recording.
- Add For Rent verified product media.
- Replace StreamNexus placeholder media with verified captures.
- Add Arthenticate and DriveDeal Figma presentation media.
- Keep all motion slow, optional, and understandable without animation.

## Phase 4: Controlled dynamic modules

**Status:** PLANNED

Planned:

- Add bounded latest-writing updates from Substack.
- Add selected build or release signals only when they are meaningful and verified.
- Keep generated content inside explicit README markers.
- Do not add vanity counters, streak cards, random quotes, Spotify widgets, or raw commit feeds.

## Phase 5: Quality gates and release

**Status:** PLANNED

Planned:

- Validate internal and external links.
- Validate local asset paths.
- Scan for placeholders, private paths, secrets, and unsupported claims.
- Check alt text and static fallbacks.
- Review the final PR diff.
- Merge only after the visible banner, README copy, metrics, credentials, and project attribution agree.

## Current risk

The existing banner image may still contain the previous six-certification metric. It must not be reused in the final profile. Phase 2 will replace it before merge.

# Project Media Manifest

**Status:** ACTIVE MOTION SYSTEM  
**Applies to:** GitHub profile media under `assets/hero/` and `assets/projects/`  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`

This manifest separates active motion media, static alternatives, and future verified product captures. It prevents placeholder images, unverified product captures, misleading deployment claims, or inconsistent animation treatment from entering the public profile.

## Published motion and static pairs

| Active motion asset | Static alternative | Scope | Placement |
|---|---|---|---|
| `assets/hero/yash-kanadhia-living-product-console-dark-motion.svg` | `assets/hero/yash-kanadhia-living-product-console-dark.png` | Profile identity, title, metrics, tools, Zeref, and PerFin | First visual in the README |
| `assets/projects/flagship-systems-motion.svg` | `assets/projects/flagship-systems.svg` | Zeref Memory Engine and PerFin OS | Directly below `Flagship systems` and before project copy |
| `assets/projects/built-product-proof-motion.svg` | `assets/projects/built-product-proof.svg` | For Rent and StreamNexus | Directly below `Built product proof` and before project copy |
| `assets/projects/product-design-studies-motion.svg` | `assets/projects/product-design-studies.svg` | Arthenticate and DriveDeal | Directly below `Product design studies` and before project copy |

Each active motion asset must be followed by an expandable static alternative before the matching written section begins.

## Visual consistency contract

All four visual surfaces use:

- Dark charcoal and near-black foundations.
- Editorial serif headings and readable sans-serif support text.
- Restrained glass panels.
- Fine system grids and console rails.
- Project-specific accent colors inside one shared visual language.
- Rounded cards, compact state pills, and clear ownership or limitation cues.
- A slow scan signal.
- Breathing card borders.
- Pulsing project markers.
- Sequential live-status dots.
- A moving lower console signal.

The hero may use additional orbital motion inside the PerFin project indicator. Project boards should remain calmer than the hero.

## Placement rules

- Do not place an unrelated image between a section heading and its motion board.
- Do not place project copy above its matching board.
- Do not show the motion and static versions simultaneously at full size.
- Keep static alternatives inside collapsed `details` blocks by default.
- Preserve the order: hero, flagship systems, built product proof, product design studies.
- Do not add a second large animated decoration above the selected-work section.

## Source discipline

### Zeref Memory Engine

Current public media may show:

- Independent project attribution.
- Local-first memory and context infrastructure.
- Structured memory and guarded writes.
- Cross-harness handoffs and privacy controls.
- Deterministic evaluation and release gates.

Do not claim external benchmark superiority, production readiness, or perfect evaluation.

### PerFin OS

Current public media may show:

- MADS final team project attribution.
- Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq as the team.
- Session and authentication boundary work.
- Firebase service architecture.
- Theme systems, analytics, and privacy-related interface contributions.

Do not imply solo ownership.

### For Rent

Current public media may show:

- SwiftUI rental marketplace scope.
- Renter, landlord, and guest journeys.
- Feature-oriented MVVM.
- Firebase boundaries.
- Accessibility support and automated checks.

Do not claim an App Store release or deployed production backend.

### StreamNexus

Current public media may show:

- Separate admin and streamer journeys.
- Session authentication and role authorization.
- Express, MongoDB, EJS, tests, security middleware, and CI.
- Simulated checkout and rental completion.

Do not use the repository's placeholder screenshot paths as final public proof.

### Arthenticate

Current public media may show:

- Interactive Figma product-design study.
- Trust-critical flows.
- Information architecture, interface states, accessibility, and high-fidelity prototyping.
- Public case-study packaging in progress.

Do not describe Arthenticate as a deployed product unless verified public evidence is added later.

### DriveDeal

Current public media may show:

- Interactive Figma automotive marketplace study.
- Marketplace journeys, information architecture, interface design, and high-fidelity prototyping.
- Public case-study packaging in progress.

Do not describe DriveDeal as a deployed product unless verified public evidence is added later.

## Motion rules

- Motion must remain optional, slow, and decorative.
- No animation cycle may be shorter than four seconds.
- No flashing more than three times per second.
- No hard strobing, abrupt full-frame cuts, or large positional jumps.
- Every animation requires a still equivalent and descriptive alt text.
- No information may exist only inside motion.
- Motion must not imply product deployment, runtime activity, user counts, or live system status.
- Prefer product demonstrations from verified captures when they become available. Do not fabricate demonstrations from static mockups.

## Current generated motion

The active project-board motion is intentionally ambient. It does not represent real application runtime. It indicates an active portfolio console through:

- Slow scanning light.
- Card-border breathing.
- Project-marker pulses.
- Console status dots.
- Lower signal movement.

## Future verified capture backlog

The following are enhancement tasks, not current public proof:

| Project | Future media | Acceptance requirement |
|---|---|---|
| Zeref Memory Engine | Short product demonstration loop | Captured from a verified workflow; slow motion; static equivalent; evidence-bound copy |
| PerFin OS | Login, dashboard, expense, map, reports, and short workflow recording | Captured from a verified local runtime; team attribution preserved |
| For Rent | Renter and landlord journeys | Captured from the deterministic demo or verified Firebase mode |
| StreamNexus | Real home, browse, search, detail, and mobile captures | Replace repository placeholders only after verified runtime capture |
| Arthenticate | Hero frame and prototype walkthrough | Approved public Figma or exported case-study source |
| DriveDeal | Hero frame and prototype walkthrough | Approved public Figma or exported case-study source |

## Replacement policy

A motion or static board may be replaced only when the replacement:

1. Comes from a verified product or approved design source.
2. Preserves ownership and limitation wording.
3. Includes descriptive alt text.
4. Includes a static alternative when motion is used.
5. Does not introduce private paths, credentials, personal data, or unsupported metrics.
6. Preserves the placement order and shared visual system.
7. Passes the motion validator and the full profile quality gate.
8. Passes light-theme, dark-theme, desktop-width, and mobile-width review.

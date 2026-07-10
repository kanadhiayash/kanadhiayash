# Project Media Manifest

**Status:** ACTIVE  
**Applies to:** GitHub profile project media under `assets/projects/`  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`

This manifest separates currently published static media from future screenshots and recordings. It prevents placeholder images, unverified product captures, or misleading deployment claims from entering the public profile.

## Published static media

| Asset | Projects | Status | Purpose |
|---|---|---|---|
| `assets/projects/flagship-systems.svg` | Zeref Memory Engine, PerFin OS | Published on review branch | Evidence-backed flagship summary and ownership context |
| `assets/projects/built-product-proof.svg` | For Rent, StreamNexus | Published on review branch | Evidence-backed implementation summary and limitation context |
| `assets/projects/product-design-studies.svg` | Arthenticate, DriveDeal | Published on review branch | Figma study summary with case-study packaging status |

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

## Future capture backlog

The following are enhancement tasks, not current public proof:

| Project | Future media | Acceptance requirement |
|---|---|---|
| Zeref Memory Engine | Short product-system motion loop | Slow motion, static equivalent, evidence-bound copy |
| PerFin OS | Login, dashboard, expense, map, reports, and short workflow recording | Captured from a verified local runtime; team attribution preserved |
| For Rent | Renter and landlord journeys | Captured from the deterministic demo or verified Firebase mode |
| StreamNexus | Real home, browse, search, detail, and mobile captures | Replace repository placeholders only after verified runtime capture |
| Arthenticate | Hero frame and prototype walkthrough | Approved public Figma or exported case-study source |
| DriveDeal | Hero frame and prototype walkthrough | Approved public Figma or exported case-study source |

## Motion rules

- Motion must be optional and slow.
- No flashing more than three times per second.
- Every animation requires a still equivalent and descriptive alt text.
- No information may exist only inside motion.
- Prefer short workflow demonstrations over decorative animation.

## Replacement policy

Static SVG boards may be replaced only when the replacement:

1. Comes from a verified product or approved design source.
2. Preserves ownership and limitation wording.
3. Includes descriptive alt text.
4. Does not introduce private paths, credentials, personal data, or unsupported metrics.
5. Passes light-theme, dark-theme, desktop-width, and mobile-width review.

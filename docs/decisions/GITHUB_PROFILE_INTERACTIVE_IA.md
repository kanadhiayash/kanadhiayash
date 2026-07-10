# GitHub Profile Dual-Layer Evidence Architecture

**Status:** LOCKED FOR REVIEW  
**Effective date:** 2026-07-10  
**Applies to:** `kanadhiayash/kanadhiayash` profile README  
**Positioning source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`

## Decision

The GitHub profile uses a dual-layer evidence model:

1. A visible 60-second professional scan.
2. A deeper evidence layer opened only when a visitor chooses to inspect it.

The profile is a portfolio entry point, recruiter proof layer, industry-facing professional profile, and route into repository evidence. It is not a complete case-study website or a substitute for project documentation.

## Primary audiences

- Recruiters and talent partners performing an initial screen.
- Product and engineering hiring managers validating role fit.
- Designers, engineers, and industry peers inspecting decisions and operating discipline.
- Collaborators evaluating ownership, boundaries, and evidence quality.

## Locked page order

1. Motion hero and static alternative.
2. Identity, title, location, tagline, tools, and navigation.
3. `60-second profile` visible by default.
4. `Deep evidence` with Zeref first and three selected product drawers.
5. `Evidence map` connecting capabilities to inspectable proof.
6. `How I work` operating method.
7. `Current signals` with controlled dynamic modules.
8. `Selected credentials`.
9. `Connect`.

## 60-second profile contract

The visible scan must:

- remain at or below 220 words;
- state product, technical, and delivery range without a long biography;
- show Zeref Memory Engine, PerFin OS, For Rent, and StreamNexus;
- provide at least one direct evidence route for each selected system or product;
- avoid image cards, project banners, case-study prose, and diagrams;
- work when all images fail to load.

The 60-second scan is always present. It is not optional and does not depend on a recruiter choosing a special mode.

## Deep evidence contract

Zeref Memory Engine leads as the flagship system.

The deep layer uses four closed GitHub-native `<details>` drawers:

1. Zeref Memory Engine.
2. PerFin OS.
3. For Rent.
4. StreamNexus.

Each drawer may contain:

- one reserved media slot or approved verified capture;
- role and ownership;
- two to four concise proof points;
- evidence links;
- one explicit boundary or non-claim;
- a return route to the 60-second profile.

Project repositories remain the source for full architecture, workflows, tests, security notes, and implementation documentation.

## Ownership and boundary rules

### Zeref Memory Engine

- Present as a public independent project under Yash Kanadhia.
- Do not describe it as a hosted service, model provider, vector database, or replacement for human review.
- Route architecture and benchmark detail to the Zeref repository.

### PerFin OS

- Credit Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq before contribution claims.
- State that the profile does not imply solo ownership.
- Do not claim bank connectivity, payment processing, or public-safe media approval before verification.

### For Rent

- Present product and SwiftUI implementation evidence.
- Do not claim an App Store release or deployed production backend.

### StreamNexus

- Present full-stack product implementation evidence.
- State that it is a portfolio prototype, not a production OTT platform.
- State that checkout and rental completion are simulated.

## Interaction model

Use only GitHub-supported patterns:

- anchor navigation;
- `<details>` and `<summary>` disclosure;
- standard Markdown links;
- accessible static or motion images;
- reviewed dynamic marker regions.

Do not imitate unsupported application controls.

## Visual hierarchy

- Keep the existing approved hero.
- Do not use project thumbnail grids.
- Do not use text-heavy editorial posters as thumbnails.
- Do not repeat the same project cover in more than one location.
- Keep product media inside the related evidence drawer.
- Use one media slot per selected system or product until verified captures are approved.
- Keep all important facts outside images.

## Explicit exclusions

Do not add:

- profile changelogs or memorabilia;
- project-card presentation tables;
- duplicate covers or banners;
- Mermaid diagrams in the profile README;
- raw commit feeds;
- vanity counters, streak cards, contribution animations, music, quotes, or clocks;
- fake screenshots or fabricated runtime proof;
- unsupported claims of deployment, users, impact, scale, or ownership.

## Acceptance criteria

The dual-layer profile is ready for merge only when:

- the 60-second profile is visible and within its content budget;
- Zeref appears before the three selected products in Deep evidence;
- all four evidence drawers remain closed by default;
- the page contains no project thumbnail grid or duplicate project covers;
- all four reserved media slots are accessible and clearly non-final;
- every selected item has a public evidence route;
- PerFin team attribution and all product boundaries remain explicit;
- dynamic modules remain secondary;
- automated quality and online-link gates pass;
- GitHub light, dark, desktop, and narrow-width rendering are manually reviewed.

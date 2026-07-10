# GitHub Profile Interactive Information Architecture

**Status:** LOCKED  
**Effective date:** 2026-07-10  
**Applies to:** the next major README information-architecture rewrite after verified project media is collected  
**Positioning source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`

This decision replaces exploratory plans for the future interactive profile structure. Later changes require an explicit replacement decision.

## Objective

Turn `github.com/kanadhiayash` into a GitHub-native interactive portfolio index that helps a visitor choose a route, inspect a project, and open verified evidence without treating the README as a JavaScript website.

The profile must operate as:

- an interactive portfolio index;
- a recruiter-readable project switchboard;
- a route into case studies, repositories, prototypes, and live demonstrations;
- a concise proof layer rather than a complete portfolio website.

## Locked interaction model

Use GitHub-supported interaction patterns only:

- section anchors;
- linked images;
- relative repository links;
- `<details>` project drawers;
- static covers;
- restrained motion;
- reviewed dynamic modules;
- outbound links to full case studies, prototypes, repositories, and demos.

Do not simulate unsupported application controls or imply that the README is a full interactive web application.

## Locked README information architecture

Use this order:

1. Motion hero
2. Command palette
3. Featured work switchboard
4. Product design
5. Built products
6. AI systems
7. Evidence and practice
8. Live build console
9. Selected credentials
10. Connect

No profile changelog, memorabilia section, version-history timeline, or decorative activity archive may be added.

## Section requirements

### 1. Motion hero

Keep one restrained animated hero above the fold with a directly accessible static alternative.

The hero communicates only:

- Yash Kanadhia;
- Product Designer;
- Toronto, Ontario, Canada;
- the approved tagline;
- one primary route into selected work;
- one secondary professional contact route.

Do not place another large autoplaying animation above the fold.

### 2. Command palette

Provide four anchor routes:

- Product Design
- Built Products
- AI Systems
- Evidence and Practice

The command palette is navigation, not decoration.

### 3. Featured work switchboard

Lead with four projects:

1. Arthenticate
2. Zeref Memory Engine
3. PerFin OS
4. For Rent

Use StreamNexus and DriveDeal as supporting work below the featured set.

Each featured card includes:

- static cover;
- project name;
- role;
- platform;
- status;
- one-sentence product outcome;
- case-study, repository, prototype, or demo links when verified.

### 4. Product design

Include:

- Arthenticate;
- DriveDeal.

Keep both labeled according to verified public status. Do not imply deployment where only Figma or case-study evidence exists.

### 5. Built products

Include:

- PerFin OS;
- For Rent;
- StreamNexus.

PerFin OS must remain identified as a MADS final team project by Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq.

### 6. AI systems

Lead with Zeref Memory Engine as an independent project.

Use this section to show product framing, local-first context infrastructure, guarded memory, evaluation, and verified release evidence.

### 7. Evidence and practice

Compress architecture, accessibility, testing, delivery, and operating-manual evidence into a concise route-based section.

Do not restore a long generic skills table when project-specific proof is available.

### 8. Live build console

Use bounded, reviewed signals only:

- latest relevant writing;
- selected release or contribution signals;
- current public build focus when evidence-backed.

Do not add raw commit feeds, vanity counters, streak cards, random quotes, music widgets, or unrelated activity.

### 9. Selected credentials

Keep the approved five selected credentials. Do not expand this into a complete certificate inventory.

### 10. Connect

Keep concise links to LinkedIn, Substack, and the future portfolio site when available.

## Locked project interaction pattern

Every project uses the same progressive-disclosure pattern:

1. Static cover visible by default.
2. Compact project metadata and one-sentence outcome.
3. A user-triggered `<details>` case-file drawer.
4. One walkthrough GIF or motion asset inside the drawer.
5. Two or three verified static snapshots after the walkthrough.
6. Role, ownership, product decisions, evidence, limitations, and destination links.

Do not autoplay every project walkthrough at once.

## Project case-file contents

Each drawer contains:

- problem;
- role and ownership;
- product decision or contribution;
- key workflow;
- design or technical system;
- verified evidence;
- known limitations;
- repository, prototype, case-study, or live-demo links.

No project fact may exist only inside an image or animation.

## Asset contract

Use this structure for each project:

```text
assets/projects/<project-slug>/
├── cover.png
├── walkthrough.gif
├── poster.png
├── snapshot-01.png
├── snapshot-02.png
├── snapshot-03.png
└── architecture.png
```

Only `cover.png`, `walkthrough.gif`, `poster.png`, and the snapshots required for the case are mandatory. `architecture.png` is optional.

### Media rules

- Static cover visible by default.
- Walkthrough recommended length: 8 to 15 seconds.
- One coherent workflow per walkthrough.
- No rapid cuts, flashing, or purposeless cursor movement.
- Every motion asset requires a still equivalent.
- Images must remain readable at narrow GitHub widths.
- Team ownership and product limitations must remain visible in text.

## Current execution phase

The current phase is media collection, not README reconstruction.

Collect the minimum viable media kit first for:

1. Arthenticate
2. Zeref Memory Engine
3. PerFin OS
4. For Rent

Do not begin the major IA rewrite until those four projects have:

- an approved cover;
- a verified walkthrough;
- at least two useful snapshots;
- confirmed ownership wording;
- at least one valid evidence destination.

StreamNexus and DriveDeal then inherit the same component pattern without changing the locked IA.

## Migration from the current README

During the future rewrite:

- keep the Living Product Console hero;
- keep its static alternative;
- replace generic category boards with verified project covers and walkthroughs;
- remove repeated project explanations;
- compress Evidence of Practice and How I Work into project-specific or route-based proof;
- keep controlled dynamic modules bounded;
- preserve current quality, security, link, attribution, and accessibility gates.

The existing category motion boards may remain temporarily until verified project media replaces them. They are not the target final interaction model.

## Explicit exclusions

Do not add:

- profile changelog or memorabilia;
- public version-history timeline;
- contribution snake or Pacman as a primary visual;
- profile-view, follower, streak, repository, commit, or credential counters;
- Spotify or music widgets;
- random quote widgets;
- live clocks;
- multiple typing animations;
- raw commit feeds;
- decorative activity archives;
- unsupported claims of deployment, impact, or ownership.

## Acceptance criteria

The future interactive README is ready only when:

- the four featured projects are identifiable without reading long prose;
- each project has a static cover and user-triggered walkthrough;
- team ownership is explicit;
- every motion asset has a still equivalent;
- every project has at least one verified evidence destination;
- the page works in GitHub light, dark, desktop, and mobile views;
- the README remains understandable when images do not load;
- dynamic modules remain secondary to selected work;
- the external GitHub profile bio matches the locked Product Designer positioning;
- no profile changelog or memorabilia layer appears.

## Change control

Any change to section order, featured-project priority, ownership language, project interaction pattern, or the exclusion of profile changelog and memorabilia requires a new explicit decision record.
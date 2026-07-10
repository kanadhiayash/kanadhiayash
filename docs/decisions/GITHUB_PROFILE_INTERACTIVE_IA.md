# GitHub Profile Interactive Information Architecture

**Status:** LOCKED WITH STAGED BUILT-PRODUCT IMPLEMENTATION  
**Effective date:** 2026-07-10  
**Last revised:** 2026-07-10  
**Applies to:** the GitHub profile README and its progressive migration into a GitHub-native portfolio index  
**Positioning source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`

This decision replaces the earlier rule that final project media must be complete before any README information-architecture work begins.

The long-term information architecture remains stable. The active implementation now proceeds in reviewable stages so verified content, navigation, project covers, case-file drawers, evidence routes, and system diagrams can ship before final runtime captures.

## Objective

Turn `github.com/kanadhiayash` into a GitHub-native interactive portfolio index that helps a visitor choose a route, inspect a project, and open verified evidence without treating the README as a JavaScript website.

The profile operates as:

- an interactive portfolio index;
- a recruiter-readable project switchboard;
- a route into repositories, prototypes, case studies, and demonstrations;
- a concise proof layer rather than a complete portfolio website.

## Locked interaction model

Use GitHub-supported interaction patterns only:

- section anchors;
- linked images;
- relative repository links;
- `<details>` project drawers;
- static covers;
- restrained motion;
- Mermaid diagrams;
- reviewed dynamic modules;
- outbound evidence links.

Do not simulate unsupported application controls or imply that the README is a full interactive web application.

## Long-term README information architecture

The eventual complete profile retains this order:

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

## Active staged implementation

The current public-review branch uses this order:

1. Motion hero
2. Command palette
3. Featured work switchboard
4. Built product case files
5. Evidence and practice
6. Live build console
7. Selected credentials
8. Connect

The active project set is:

1. PerFin OS
2. For Rent
3. StreamNexus

The following modules are parked for a later review cycle:

- Product design: Arthenticate and DriveDeal
- AI systems: Zeref Memory Engine

Parking a module means no new case file, media collection, or section expansion is performed in the current stage. It does not remove the module from the long-term architecture.

The existing Living Product Console hero remains unchanged during this stage, including its existing project references. Rebuilding the hero is outside the active scope.

## Command palette

Provide four real anchor routes:

- Featured Work
- Built Products
- Evidence
- Build Signals

The command palette is navigation, not decoration.

## Featured work switchboard

Each active project uses:

- a finished metadata-based editorial cover visible by default;
- project name;
- ownership or collaboration status;
- platform;
- verified status;
- a one-sentence product outcome;
- an anchor route into its case file.

Metadata covers must use verified public facts only. They must not imitate screenshots, runtime dashboards, user metrics, deployment status, or product usage.

## Active project requirements

### PerFin OS

PerFin OS remains identified as a MADS final team project by:

- Yash Kanadhia
- Alexis Gorospe
- Sarmad Tariq

The profile must not imply solo ownership.

The case file may show reviewed contribution evidence, guest and authenticated workflow boundaries, system architecture, known limitations, and verified repository or pull-request destinations.

### For Rent

The case file may show:

- renter, landlord, and guest journeys;
- deterministic demo mode;
- Firebase clean mode;
- feature-oriented MVVM;
- accessibility and quality evidence;
- explicit non-claims around App Store release and production deployment.

### StreamNexus

The case file may show:

- administrator and streamer workflows;
- MVC and service boundaries;
- authentication and role authorization;
- MongoDB persistence;
- tests, security middleware, and CI;
- explicit simulated-checkout and non-production limitations.

## Locked project interaction pattern

Every active project uses the same progressive-disclosure pattern:

1. Static editorial cover visible by default.
2. Compact project metadata and one-sentence outcome.
3. A user-triggered `<details>` case-file drawer.
4. One clearly labeled media-capture state inside the drawer until verified runtime media exists.
5. Written sections for problem, role and ownership, contribution, key workflow, system, evidence, and limitations.
6. Verified repository, documentation, pull-request, prototype, or demo destinations.
7. A route back to Featured Work.

No project fact may exist only inside an image, animation, or diagram.

## Media staging contract

Until final runtime media is approved, each active project uses:

```text
assets/projects/<project-slug>/
├── cover.svg
└── media-pending.svg
```

The cover is a finished editorial asset based on verified metadata.

The media-capture state must say that reviewed walkthrough and static captures are pending. It must not resemble a product screenshot or fabricate interface evidence.

When final media is approved, the project migrates to:

```text
assets/projects/<project-slug>/
├── cover.svg
├── walkthrough.gif
├── poster.png
├── snapshot-01.png
├── snapshot-02.png
├── snapshot-03.png
└── architecture.png
```

Only useful snapshots are required. `architecture.png` remains optional when a readable Mermaid diagram already communicates the system.

## System diagrams

Mermaid diagrams may be used for verified architecture and workflow relationships.

Requirements:

- Diagram facts must also be explained in text.
- Labels must remain concise and readable.
- Diagrams must not imply deployment, scale, or integrations that are not verified.
- A failed diagram render must not prevent understanding of the case file.

## Evidence and practice

Compress product design, accessibility, architecture, testing, delivery, and AI-assisted execution into a concise route-based section.

Do not restore a long generic skills inventory when project-specific evidence is available.

## Live build console

Use bounded, reviewed signals only:

- latest relevant writing;
- selected pull requests, documentation, release, or verification signals;
- current public build focus when evidence-backed.

Do not add raw commit feeds, vanity counters, streak cards, random quotes, music widgets, or unrelated activity.

## Selected credentials

Keep the approved five selected credentials. Do not expand this into a complete certificate inventory.

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
- fake product screenshots;
- unsupported claims of deployment, impact, scale, or ownership.

## Acceptance criteria for the staged release

The staged interactive README is ready only when:

- PerFin OS, For Rent, and StreamNexus are identifiable without long prose;
- each active project has a visible metadata cover;
- each active project has one user-triggered case-file drawer;
- PerFin OS team ownership is explicit before contribution details;
- each active project has at least one verified evidence destination;
- each active project has a known-limitations section;
- media-capture states are clearly labeled and cannot be mistaken for product evidence;
- Mermaid diagrams remain supported by written explanations;
- the page works in GitHub light, dark, desktop, and mobile views;
- the README remains understandable when images or diagrams do not load;
- dynamic modules remain secondary to selected work;
- the external GitHub profile bio matches the locked Product Designer positioning;
- no profile changelog or memorabilia layer appears.

## Future expansion

When the parked modules resume:

- Product Design returns before Built Products.
- AI Systems returns after Built Products.
- Arthenticate, DriveDeal, and Zeref use the same cover, metadata, drawer, evidence, limitation, and media contract.
- The staged built-product case files do not require structural redesign.

## Change control

Any change to long-term section order, active project priority, ownership language, project interaction pattern, parked-module status, or the exclusion of profile changelog and memorabilia requires a new explicit decision record or revision approved through review.

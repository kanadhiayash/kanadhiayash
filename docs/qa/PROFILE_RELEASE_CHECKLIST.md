# GitHub Profile Release Checklist

**Status:** STAGED INTERACTIVE BRANCH UNDER REVIEW  
**Release surface:** `kanadhiayash/kanadhiayash` profile README  
**Branch:** `docs/profile__interactive-built-products`  
**Quality gate:** `.github/workflows/profile-quality.yml`

## Release rule

Do not merge or describe the staged interactive profile as released until automated gates pass and every remaining manual blocking item is reviewed.

## Locked public copy

The release validator must preserve:

- Yash Kanadhia
- Product Designer as the sole hero title
- Toronto, Ontario, Canada
- I design and build systems that connect people to outcomes.
- 2 shipped projects · 1 MADS team project · 5 selected certifications
- Figma · React · Swift · Firebase · Claude · Codex

## Active information architecture

The staged branch must render in this order:

1. Motion hero
2. Command palette
3. Featured work
4. Built product case files
5. Evidence and practice
6. Live build console
7. Selected credentials
8. Connect

Product Design and AI Systems are parked for this stage. Their long-term positions remain documented in `docs/decisions/GITHUB_PROFILE_INTERACTIVE_IA.md`.

## Active project contract

The active order is:

1. PerFin OS
2. For Rent
3. StreamNexus

Each project must have:

- one visible metadata cover;
- compact public metadata;
- one user-triggered case-file drawer;
- one clearly labeled media-capture state;
- problem statement;
- role and ownership wording;
- key workflow;
- system map;
- evidence links;
- known limitations;
- return route to Featured Work.

PerFin OS must credit:

- Yash Kanadhia
- Alexis Gorospe
- Sarmad Tariq

The profile must not imply solo ownership.

## Required active assets

```text
assets/hero/yash-kanadhia-living-product-console-dark-motion.svg
assets/hero/yash-kanadhia-living-product-console-dark.png
assets/hero/yash-kanadhia-living-product-console-dark.jpg
assets/hero/yash-kanadhia-living-product-console-dark.svg
assets/projects/perfin-os/cover.svg
assets/projects/perfin-os/media-pending.svg
assets/projects/for-rent/cover.svg
assets/projects/for-rent/media-pending.svg
assets/projects/streamnexus/cover.svg
assets/projects/streamnexus/media-pending.svg
```

## Automated blocking checks

The quality gate checks:

- all Python profile scripts compile;
- controlled dynamic modules remain structurally valid;
- the motion hero and static alternative remain present and ordered;
- the hero uses slow, accessible motion metadata;
- all six active project SVGs exist and include accessible title and description elements;
- the three project covers appear in the active project order;
- the three media-capture states remain inside project drawers;
- the README contains exactly four `<details>` elements: one static hero alternative and three project drawers;
- every README local image and link resolves;
- every README image has descriptive alt text;
- every internal anchor resolves;
- external links use HTTPS;
- definitive external 404 and 410 responses block release;
- transient source failures produce warnings rather than false release failures;
- disallowed draft markers are absent from the README;
- public text files contain no detected credentials, private keys, credentialed MongoDB URIs, or private workstation paths;
- PerFin OS ownership and all three team names remain present;
- every active project includes a known-limitations section and at least one verified evidence destination;
- the five selected credentials remain present once each;
- Six Sigma Yellow Belt remains excluded;
- the four dynamic-module markers each appear exactly once.

## Automated status

- [ ] Profile scripts compile
- [ ] Dynamic modules validate
- [ ] Motion hero validates
- [ ] Interactive structure validates
- [ ] Local image and link contract validates
- [ ] Public-copy and ownership contract validates
- [ ] Secret and private-path scan passes
- [ ] Online link gate passes or reports warnings only

## Manual blocking checks

Review the rendered README in GitHub:

- [ ] Desktop width in GitHub light appearance
- [ ] Desktop width in GitHub dark appearance
- [ ] Narrow mobile width
- [ ] Motion hero plays or fails gracefully through GitHub image proxy
- [ ] Static hero alternative renders correctly
- [ ] Command-palette routes reach the correct sections
- [ ] PerFin OS, For Rent, and StreamNexus covers remain readable without zooming
- [ ] Cover text does not clip at narrow widths
- [ ] Every case-file drawer opens and closes correctly
- [ ] Mermaid diagrams render and remain understandable from surrounding text
- [ ] Media-capture states cannot be mistaken for product screenshots
- [ ] PerFin OS team ownership is visible before contribution claims
- [ ] For Rent does not imply App Store release or deployed production backend
- [ ] StreamNexus does not imply real payments, playback, subscriptions, users, or production deployment
- [ ] Dynamic modules remain secondary to selected work
- [ ] The page remains understandable when images and diagrams fail to load
- [ ] All external evidence destinations open the intended public source
- [ ] Product Design and AI Systems do not appear as incomplete public sections
- [ ] No profile changelog, memorabilia, counter, music widget, quote widget, or decorative activity archive appears

## Dynamic-module operational check

1. Run **Profile Refresh** manually from GitHub Actions.
2. Confirm it creates or updates `automation/profile-refresh` only when reviewed content changes.
3. Review the generated pull request.
4. Confirm changes stay inside the two marker regions.
5. Confirm a failed writing source preserves the previous reviewed content.
6. Merge the automation pull request only after titles, URLs, attribution, and relevance are verified.

## Local verification commands

```bash
python3 -m py_compile scripts/update_dynamic_modules.py
python3 -m py_compile scripts/validate_profile_release.py
python3 -m py_compile scripts/validate_profile_foundation.py
python3 -m py_compile scripts/validate_profile_links.py
python3 -m py_compile scripts/validate_profile_motion.py
python3 scripts/update_dynamic_modules.py --check
python3 scripts/validate_profile_motion.py
python3 scripts/validate_profile_foundation.py
python3 scripts/validate_profile_release.py
python3 scripts/validate_profile_links.py
git diff --check
```

## Approval record

```text
Automated quality gate: __________________
GitHub light render: _____________________
GitHub dark render: ______________________
Mobile render: ___________________________
Case-file interaction review: ___________
Ownership and limitations review: _______
Final public-claim review: ______________
Approved by: _____________________________
Approval date: ___________________________
Release commit: __________________________
```

## Non-blocking media backlog

- PerFin OS reviewed workflow capture and static snapshots
- For Rent renter or landlord workflow capture and static snapshots
- StreamNexus browse, search, detail, or rental workflow capture and static snapshots
- Arthenticate module and approved prototype media
- DriveDeal module and approved prototype media
- Zeref Memory Engine case file and verified demonstration media

Do not describe the profile as media-complete until the active project media states have been replaced with reviewed captures.

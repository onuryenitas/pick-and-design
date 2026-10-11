# Pick & Design

A research-driven web UI/UX skill for founders and builders. Describe your product, inspect relevant references, choose a direction, and develop a usable website with a persistent design system.

## What it does

- Researches relevant startups with dated funding, adoption or growth evidence.
- Finds suitable web references through a curated pool of 40 resources, including Awwwards.
- Shows sources and explains which layout, typography, color and interaction decisions fit your product.
- Offers three distinct directions when needed, then follows your selection or explicit delegation.
- Applies UX principles, usability heuristics and accessibility guidance throughout design.
- Implements achievable web motion and identifies any specific external assets needed.
- Creates or maintains a project design-system module and updates affected rules alongside site changes.

## Scope

Version 1 covers websites, landing pages, web apps and dashboards, including responsive web. Native mobile apps are outside this release. Design-system synchronization happens during agent work; no background watcher is installed.

## Install

Clone this repository, then copy the complete skill folder into your Codex skills directory:

```sh
git clone https://github.com/onuryenitas/pick-and-design.git
mkdir -p ~/.codex/skills
cp -R pick-and-design/skills/pick-and-design ~/.codex/skills/
```

For an existing installation, review and back it up before replacing it. Reload your agent's skill discovery if needed. Other agents supporting SKILL.md can use the same complete folder in their documented skill location.

## Use

Invoke `$pick-and-design` and describe the product, target users and desired work. The skill also supports automatic discovery by compatible agents.

The workflow is: brief, live reference research, UX needs, reviewable directions, user selection, implementation and design-system handoff. Existing approved directions do not require repeated approval.

## Package

- [Skill entry](skills/pick-and-design/SKILL.md)
- [40-source registry](skills/pick-and-design/references/source-registry.md)
- [Research and visual constraints](skills/pick-and-design/references/design-method.md)
- [Motion delivery](skills/pick-and-design/references/motion.md)
- [Design-system lifecycle](skills/pick-and-design/references/design-system-lifecycle.md)
- [Bundled UX Principles](skills/pick-and-design/modules/ux-principles/GUIDE.md)

The UX module is a versioned snapshot of [UX Principles v1.0.0](https://github.com/onuryenitas/ux-principles-skill), containing 186 records across principles, heuristics, WCAG prompts, components and workflows. Update from upstream rather than maintaining divergent catalogs. The standalone UX skill remains available separately.

## Research and validation limits

The source registry records initial access limitations. Browsing/account access depends on the agent environment. References are inspected on demand; this package does not train a model or bundle third-party articles, artwork or paid libraries. Funding, awards and aesthetics do not independently prove usability.

Skill structure, local links and the bundled UX lookup were checked. Full end-to-end design and motion quality still require validation on real projects. No accessibility certification or conversion improvement is claimed.

## License

Original package content is MIT licensed. See [LICENSE](LICENSE) and [NOTICE](NOTICE). External source materials retain their own terms.

## Reference-inspired visual worlds

Selected [MengTo Skills](https://github.com/MengTo/Skills) methods are integrated for reference analysis, distinct visual-world directions, precise implementation briefs, interaction evidence, targeted revisions and asset versioning. The [Akilima listing](https://www.akilima.io/skills/mengto/skills/generate-reference-inspired-brand-worlds) points to the same upstream brand-world skill.

See [provenance and adaptations](skills/pick-and-design/references/upstream-sources.md) and [third-party license](THIRD_PARTY_LICENSES/MengTo-Skills-MIT.txt). User constraints and web UI/UX scope take precedence over upstream defaults.

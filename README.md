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

One shared design workflow, with separate setup instructions for each tool.

| Codex | Claude Code | Claude app |
| --- | --- | --- |
| [Install in Codex](#codex) | [Install in Claude Code](#claude-code) | [Download Claude ZIP](https://github.com/onuryenitas/pick-and-design/raw/refs/heads/main/pick-and-design-claude.zip) |
| Invoke `$pick-and-design` | Invoke `/pick-and-design` | Enable in Customize > Skills |

### Codex

Send this message to Codex:

```text
Install the skill from https://github.com/onuryenitas/pick-and-design,
using the skills/pick-and-design folder.
```

The complete folder belongs at `~/.codex/skills/pick-and-design/` (or `$CODEX_HOME/skills/pick-and-design/` for a custom Codex home). Start a new turn after installation; reload skill discovery if needed.

Then try:

```text
$pick-and-design Research references for my product, propose three web
UI directions, and maintain a design system for the direction I choose.
```

### Claude Code

For a first installation, run these commands in a terminal on macOS/Linux or a compatible shell. They stop if a skill already exists at the destination.

```sh
git clone https://github.com/onuryenitas/pick-and-design.git
mkdir -p ~/.claude/skills
if [ ! -e ~/.claude/skills/pick-and-design ]; then
  cp -R pick-and-design/skills/pick-and-design ~/.claude/skills/
else
  echo "Already installed. Back up and review the existing skill before updating."
fi
```

To share the skill with a single project instead, put the complete folder at `.claude/skills/pick-and-design/` inside that project. Choose one location to avoid duplicate installations.

Then try:

```text
/pick-and-design Research references for my product, propose three web
UI directions, and maintain a design system for the direction I choose.
```

See [Claude Code skill documentation](https://code.claude.com/docs/en/skills).

### Claude app

1. [Download the Claude skill ZIP](https://github.com/onuryenitas/pick-and-design/raw/refs/heads/main/pick-and-design-claude.zip).
2. Open **Customize > Skills** in Claude, add the ZIP and enable the skill. Code execution must be enabled; availability can depend on workspace settings.
3. Ask: "Use Pick & Design to research my product's web design references and propose three directions."

Upload this dedicated ZIP, not GitHub's full repository Source code ZIP. It contains:

```text
pick-and-design/
  SKILL.md
  references/
  modules/
  LICENSE
  NOTICE
  VERSION
```

The Claude ZIP uses a shorter discovery description for upload compatibility; its design instructions and supporting modules come from the same source. Rebuild it after skill changes with `python3 build-claude-package.py`. The archive preserves the licenses and includes no repository history.

See [Claude custom skill documentation](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### Updates and capabilities

Back up an existing installation before replacing the complete skill folder. Download and replace the Claude ZIP when updating that installation. GitHub changes do not automatically update separately copied or uploaded skills.

Browsing, image generation, filesystem access and code execution depend on the tools available in your agent. Installing this skill does not add those tools. Package structure is checked; the Claude upload and real-project behavior have not yet been tested in a signed-in Claude account.

## Use

Describe your product, target users and desired work in your own language. Use `$pick-and-design` in Codex, `/pick-and-design` in Claude Code, or request Pick & Design in Claude with the skill enabled.

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

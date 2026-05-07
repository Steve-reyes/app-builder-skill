# App Builder Skill

**Analyze any SaaS/competitor product → complete build plan with full infra design.**

## What It Does

Given a competitor URL or product description, this skill:
1. **Researches** the product (what they do, pricing, features, target market)
2. **Analyzes feasibility** — what's easy to build vs what's the moat
3. **Generates a complete build plan** with:
   - Architecture diagram
   - Full directory structure
   - PostgreSQL schema (users, orgs, core entities, activity log)
   - REST API route design
   - AI agent design (inputs → processing → outputs)
   - Tech stack decisions with rationale
   - Realistic build timeline by phase
   - Monthly cost estimates
   - Future scaling roadmap

## How to Use

> "analyze [competitor]"
> "build plan for [url]"
> "clone [product]"
> "what would it take to build [x]"

The skill produces a markdown file saved to the user's `steve_app_ideas/` workspace folder and auto-pushed to their `app_ideas` GitHub repo.

## Output Format

Every plan follows this structure:

```
1. What [Product] Is — Description, 3-step flow, pricing, target market
2. What Makes It Hard — Feature difficulty matrix, true moats
3. MVP That CAN Be Built — Honest scope, what's excluded
4. Complete Infra Design — Architecture, directory, DB schema, API, AI agents, stack, timeline, costs, phases
```

## Resources

| File | Purpose |
|---|---|
| `SKILL.md` | Main skill instructions and workflow |
| `scripts/research_competitor.py` | Automated competitor URL research |
| `scripts/generate_plan.py` | Validate research data and output plan path |
| `references/build-plan-template.md` | Full template for every build plan output |

## Requirements

- Python 3.12+
- web_search and web_fetch tools available
- Git configured with GitHub remote
- `steve_app_ideas/` directory with post-commit hook for auto-push

## Installation

Place this skill in your OpenClaw skills directory:

```bash
openclaw skill install app-builder
```

Or install from the packaged skill file:

```bash
openclaw skill install app-builder.skill
```

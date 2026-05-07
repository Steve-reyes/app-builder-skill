---
name: app-builder
description: |
  Analyze any SaaS/competitor product and produce a complete build plan with full infra design.
  Triggers: "analyze [competitor]", "build plan for [url]", "clone [product]", "what would it take to build [x]", "deconstruct [company]", "reverse engineer [tool]".
  Use when the user wants to understand a competitor's product, estimate build effort, or get a ready-to-execute project plan with architecture, DB schema, API routes, AI agent design, tech stack, timeline, and costs.
---

# App Builder

Given a competitor URL or product description, research it and produce a structured build plan saved to `steve_app_ideas/` folder and auto-pushed to the `app_ideas` GitHub repo.

## Workflow

### 1. Research the Competitor

Use `web_search` and `web_fetch` to gather:

- What the product does (homepage, tagline, positioning)
- How it works (3-step flow, key features)
- Pricing (plans, tiers, free trial)
- Target market (founders, SMBs, enterprise, etc.)
- Social proof (reviews, case studies, testimonials, Product Hunt)

### 2. Feasibility Breakdown

Classify each core feature into one of three buckets:

| Difficulty | Label | Criteria |
|---|---|---|
| 🟢 Easy | Python/API work | Standard CRUD, LLM calls, web scraping |
| 🟡 Medium | Infrastructure work | DB design, queues, auth, hosting |
| 🔴 Hard | The moat | API restrictions, proprietary data, regulatory, infrastructure heavy |

### 3. Generate the Build Plan

Create a markdown file at path: `steve_app_ideas/<product-name>.md`

The file must follow the structure in `references/build-plan-template.md`. Key sections:

```
# <Product> Analysis & Build Plan

## 1. What <Product> Is
## 2. What Makes It Hard (moats)
## 3. MVP That CAN Be Built
## 4. Complete Project Infra Design
### Architecture Overview
### Directory Structure
### Database Schema (PostgreSQL)
### API Endpoints
### AI Agent Design
### Tech Stack Summary
### Estimated MVP Build Time
### Cost Estimates (Monthly)
### Future Phases
```

### 4. Save & Push

```bash
# File location
steve_app_ideas/<product-name>.md

# Git operations (auto-commit + push via post-commit hook)
cd /root/.openclaw/agents/researcher/workspace/steve_app_ideas
git add <filename>.md
git commit -m "Add build plan: <Product>"
```

The post-commit hook auto-pushes to GitHub. Verify with:
```bash
cd /root/.openclaw/agents/researcher/workspace/steve_app_ideas
git status  # Should show clean
```

## Execution Rules

- Start every analysis with `web_search` against the competitor name and site
- Be honest about what's hard — do not sugarcoat moats
- Always include realistic timelines and cost estimates
- Database schema must include at minimum: users, orgs, leads, sequences, activity_log tables with proper FK relationships
- API endpoints must follow REST conventions
- AI agent design must describe inputs, processing steps, and outputs for each agent
- After writing the file, always commit and verify the push

## Resources

### scripts/
- `research_competitor.py` — Automated research script: fetches + summarizes competitor data
- `generate_plan.py` — Generates the markdown plan from research data

### references/
- `build-plan-template.md` — The full template structure used for every build plan

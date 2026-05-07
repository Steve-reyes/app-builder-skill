# {{PRODUCT_NAME}} Analysis & Build Plan

> **Date:** {{DATE}}
> **Source:** {{COMPETITOR_URL}}
> **Status:** Competitor analysis → MVP build scope

---

## 1. What {{PRODUCT_NAME}} Is

Brief description: what it does, how it works (3-step flow), pricing, target market, key features.

### Their 3-Step Flow
1. **Step 1** — Description
2. **Step 2** — Description
3. **Step 3** — Description

### Target Market
Who they sell to, claimed customer count, positioning.

---

## 2. What Makes It Hard

| Component | Difficulty | Why |
|---|---|---|
| {{Feature 1}} | 🟢/🟡/🔴 | Reason |
| {{Feature 2}} | 🟢/🟡/🔴 | Reason |
| {{Feature 3}} | 🟢/🟡/🔴 | Reason |

### The Moats
- List the real barriers (API restrictions, proprietary data, regulatory, infrastructure)

---

## 3. MVP That CAN Be Built

### MVP Features
1. **Feature 1** — Description
2. **Feature 2** — Description
3. **Feature 3** — Description

### What We DON'T Build (MVP)
- Items explicitly excluded from MVP scope

---

## 4. Complete Project Infra Design

### Product Requirements Document (PRD)
See `references/prd-template.md` for full PRD structure:
- User personas (2-3)
- Jobs to be Done
- User stories with acceptance criteria
- RICE feature prioritization table
- Success metrics & KPIs

### Competitive Landscape Matrix
See `references/competitive-landscape.md` for:
- 5-competitor feature comparison table (1-5 scoring)
- Positioning map (price vs ease of use)
- Differentiation opportunities

### Architecture Overview
```
┌─────────────────────────────────────────────────────────┐
│                     Frontend (Vercel)                     │
│                    Next.js 14 App Router                  │
│                   Tailwind + Shadcn/ui                    │
└──────────────────────┬──────────────────────────────────┘
                       │ REST/WebSocket
┌──────────────────────▼──────────────────────────────────┐
│                    Backend (Railway/Fly)                  │
│                   {{BACKEND_FRAMEWORK}}                   │
│              {{TASK_QUEUE}} for async tasks               │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   Database ({{DB}})                        │
│                {{DB_TYPE}} + {{SECURITY}}                  │
│         - {{TABLE_LIST}}                                  │
└──────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                 AI Layer ({{AI_PROVIDER}})                  │
│         - AI agent descriptions                          │
└──────────────────────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│              Background Workers ({{WORKER_TYPE}})          │
│         - Background task descriptions                  │
└──────────────────────────────────────────────────────────┘
```

### Directory Structure
```
{{PRODUCT_NAME}}/
├── frontend/
│   ├── app/
│   │   ├── (auth)/
│   │   ├── dashboard/
│   │   │   ├── page-1/
│   │   │   └── page-2/
│   │   └── api/
│   ├── components/
│   ├── lib/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── db/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── tasks/
│   │   └── utils/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── .env.example
└── README.md
```

### Database Schema (PostgreSQL)

```sql
-- Orgs
CREATE TABLE orgs ( ... );

-- Users
CREATE TABLE users ( ... );

-- Core entity tables
CREATE TABLE ... ( ... );

-- Activity log
CREATE TABLE activity_log ( ... );
```

### API Endpoints

```
POST   /api/auth/register
POST   /api/auth/login

GET    /api/resource
POST   /api/resource
GET    /api/resource/:id
PATCH  /api/resource/:id
DELETE /api/resource/:id
```

### AI Agent Design

**Agent 1 (e.g., Research Agent):**
```
Input:
Steps:
  1.
  2.
Output:
```

**Agent 2 (e.g., Scoring Agent):**
```
Input:
Logic:
Output:
```

### SEO & Content Strategy
See `references/seo-content-strategy.md`:
- 3 keyword clusters with search volume and intent
- TOFU/MOFU/BOFU content funnel
- 30-day content calendar
- Backlink strategy & technical SEO checklist
- Distribution channels with effort/impact scores

### Growth & Viral Loops
See `references/growth-loops.md`:
- Viral loop mechanics with target K coefficient
- Acquisition channel cost/impact matrix
- Referral program design (reward, trigger, friction)
- Retention loop design (email, push, in-app)

### Revenue Model & Unit Economics
See `references/revenue-model.md`:
- Revenue model comparison with recommendation
- Pricing tier structure with feature breakdown
- CAC per channel + blended CAC
- LTV calculation with churn assumptions
- 12-month revenue projection table
- Break-even analysis & upsell paths

### Tech Stack Summary

| Layer | Choice | Reason |
|---|---|---|
| Frontend | Next.js 14 + Tailwind + Shadcn | Fast dev, good DX, Vercel deploy |
| Backend | FastAPI (Python) | Async, auto-docs, AI integration |
| Database | Supabase (PostgreSQL) | Managed, auth, RLS, real-time |
| AI | OpenAI / Anthropic API | Best-in-class LLM |
| Queue | Celery + Redis | Async tasks |
| Auth | Supabase Auth + JWT | Built-in, RLS |
| Hosting | Vercel + Railway/Fly | Simple, scalable |
| Monitoring | Sentry + Logfire | Error + perf |

### Estimated MVP Build Time

| Phase | Time | Deliverable |
|---|---|---|
| Setup + Auth | X days | Scaffold, auth, org model |
| Core CRUD | X days | Entity management |
| Feature X | X days | Key feature |
| Feature Y | X days | Key feature |
| Polish + Deploy | X days | Docs, deploy |
| **Total** | **X days** | **Working MVP** |

### Cost Estimates (Monthly)

| Service | Cost | Notes |
|---|---|---|
| Vercel Pro | $20 | Frontend |
| Railway Starter | $5 | Backend |
| Supabase Pro | $25 | DB + Auth |
| OpenAI API | $50-200 | LLM calls |
| Other | $X | |
| **Total** | **$X/mo** | Scales with usage |

### Future Phases

**Phase 2 — Description**
- Feature list

**Phase 3 — Description**
- Feature list

**Phase 4 — Description**
- Feature list

---

*This doc serves as the source of truth for the {{PRODUCT_NAME}} clone project.*
*Last updated: {{DATE}}*

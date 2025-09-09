# Backlog Board — 4-Project Portfolio

> Move items between **To-Do → Doing → Done**. Use tags: [P1], [P2], [P3], [P4], [ALL].

## To-Do

- [ ] [ALL] Lock packages: `pip freeze > env/requirements.lock.txt`
- [ ] [ALL] Add repo usage to root README (Quickstart + DB path)
- [ ] [ALL] Add small `sample_*.csv` exceptions to `.gitignore` (if not already)
- [ ] [P1] Finish data dictionary notes (units, null rules, business meaning)
- [ ] [P1] Write KPI SQL: Revenue, GP, GM%, AOV, Units/Order, YoY
- [ ] [P1] Build dashboard (KPI strip, monthly revenue line, category profit bar, top products table)
- [ ] [P1] Write 1–2 page analysis answering 5 questions
- [ ] [P2] Finish data dictionary notes (definitions for CTR/CVR/CAC/ROAS)
- [ ] [P2] KPI SQL rollups by channel/campaign/month
- [ ] [P2] Build dashboard (KPI strip, ROAS by channel, monthly ROAS line, campaign table)
- [ ] [P2] Recommendations list (scale/hold/cut with thresholds)
- [ ] [P3] Finish data dictionary notes (label definition for `churned`)
- [ ] [P3] Create `at_risk` SQL + baseline logistic regression notebook
- [ ] [P3] Build dashboard (KPI strip, retention curve, churn by plan/tenure, at-risk table)
- [ ] [P3] 1-page memo: top 3 churn drivers + playbooks
- [ ] [P4] Finish data dictionary notes (timestamp types, SLA rule)
- [ ] [P4] KPI SQL (SLA %, first response hrs, resolution hrs, backlog, CSAT)
- [ ] [P4] Build dashboard (SLA heatmap, aging hist, first-resp by priority, agent table)
- [ ] [P4] Short ops recommendations (top 3 with expected impact)

## Doing

- [ ] _(move items here when in progress)_

## Done

- [x] [ALL] Repo scaffold (P1–P4 structure)
- [x] [ALL] Virtual environment + requirements
- [x] [ALL] SQLite `da4.db` + smoke test
- [x] [ALL] Sample data generated for P1–P4
- [x] [ALL] Raw tables loaded: `p1_sales_raw`, `p2_ads_raw`, `p3_churn_raw`, `p4_tickets_raw`
- [x] [ALL] Staging tables built: `p1_sales_stage`, `p2_ads_stage`, `p3_churn_stage`, `p4_tickets_stage`
- [x] [ALL] One-page briefs (P1–P4)
- [x] [ALL] EDA notebooks (first pass)
- [x] [ALL] Wireframes

## Notes

- Keep tasks objective and tied to artifacts (SQL in `/sql`, notebooks in `/notebooks`, dashboards exported to `/reports`).
- Prefer small commits per task.

# CapitalConductor API — Railway-Ready Override Repo

This is a clean backend-only repo that deploys reliably on Railway via Docker.

## Endpoints
- GET /health
- POST /deck/unlock   { "password": "Conductor2025" }
- POST /analytics/track   { "type":"deck_open", "id":"demo", "email":"x@y.com" }

## Deploy to Railway (bullet-proof)
1) Push this folder to GitHub (or upload as a ZIP).
2) Railway → New Project → Deploy from GitHub → select the repo.
3) Build method: **Dockerfile**, Root: `/`.
4) Deploy, then open `/health`.

## Env variables (optional)
LIVE_DECK_PASSWORD=Conductor2025

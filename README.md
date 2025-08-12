# CapitalConductor.ai — All‑in‑One Monorepo


## One‑Click Deploy

### Backend → Railway
1) Install Railway CLI: https://docs.railway.app/develop/cli
2) `railway login`
3) `./scripts/deploy_backend_railway.sh`

### Frontend → Netlify (Next.js)
1) Install Netlify CLI: https://docs.netlify.com/cli/get-started/
2) `netlify login`
3) `./scripts/deploy_frontend_netlify.sh`

### Frontend → Vercel
1) Install Vercel CLI: https://vercel.com/docs/cli
2) `vercel login`
3) `./scripts/deploy_frontend_vercel.sh`

### Environment Variables
- Backend (Railway):
  - `LIVE_DECK_PASSWORD`
  - `GHL_INCOMING_WEBHOOK_URL`
  - `SHEET_ID`
  - `GOOGLE_SERVICE_ACCOUNT_JSON`
- Frontend:
  - `NEXT_PUBLIC_API_BASE`

Generated: 2025-08-12T23:35:28.265888Z

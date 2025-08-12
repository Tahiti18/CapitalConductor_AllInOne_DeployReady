#!/usr/bin/env bash
set -euo pipefail
echo ">> Railway backend deploy (FastAPI)"
if ! command -v railway >/dev/null 2>&1; then
  echo "Railway CLI not found. Install: https://docs.railway.app/develop/cli"
  exit 1
fi
pushd backend >/dev/null
railway up --service capitalconductor-api
popd >/dev/null
echo ">> Done."

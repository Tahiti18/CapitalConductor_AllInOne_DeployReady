#!/usr/bin/env bash
set -euo pipefail
echo ">> Vercel frontend deploy (Next.js)"
if ! command -v vercel >/dev/null 2>&1; then
  echo "Vercel CLI not found. Install: https://vercel.com/docs/cli"
  exit 1
fi
pushd frontend >/dev/null
vercel --prod
popd >/dev/null
echo ">> Done."

#!/usr/bin/env bash
set -euo pipefail
echo ">> Netlify frontend deploy (Next.js)"
if ! command -v netlify >/dev/null 2>&1; then
  echo "Netlify CLI not found. Install: https://docs.netlify.com/cli/get-started/"
  exit 1
fi
pushd frontend >/dev/null
netlify deploy --build --prod
popd >/dev/null
echo ">> Done."

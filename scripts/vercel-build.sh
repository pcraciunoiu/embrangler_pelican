#!/usr/bin/env bash
# Vercel's requirements install can leave .vercel_python_packages without native
# extensions (watchfiles._rust_notify). Reinstall with uv before building the site.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf .vercel_python_packages
export UV_LINK_MODE=copy
uv pip install -r requirements.txt -t .vercel_python_packages --only-binary watchfiles

make html

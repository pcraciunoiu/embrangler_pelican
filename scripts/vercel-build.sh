#!/usr/bin/env bash
# Vercel prepends .vercel_python_packages to PYTHONPATH (broken watchfiles). Use uv's
# project env and unset PYTHONPATH so pelican loads wheels from .venv.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf .venv
export UV_LINK_MODE=copy
uv sync --frozen --no-dev

unset PYTHONPATH
uv run make html

#!/usr/bin/env bash
# Vercel prepends .vercel_python_packages to PYTHONPATH. That tree often has
# watchfiles without the Rust extension, which shadows any fix in the same path.
# Use a project venv and unset PYTHONPATH so pelican loads working wheels.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf .venv
uv venv .venv
export UV_LINK_MODE=copy
uv pip install -r requirements.txt --python .venv/bin/python --only-binary watchfiles

unset PYTHONPATH
make html PELICAN=".venv/bin/python -m pelican"

Welcome to the codebase for [embrangler.com](http://embrangler.com), the personal and professional blog of Paul Craciunoiu.

This blog is generated using [Pelican](https://github.com/getpelican/pelican/).

## Dependencies

[uv](https://docs.astral.sh/uv/) manages dependencies via `pyproject.toml` and `uv.lock`.

After changing dependencies in `pyproject.toml`:

```bash
uv lock
uv sync
```

[Dependabot](.github/dependabot.yml) updates `uv.lock` (patch and minor bumps grouped into one PR).

## Local build

```bash
uv sync
uv run make html    # or: ./deploy.sh
./develop_server
```

Output is written to `output/`.

## Vercel

Deploy uses `scripts/vercel-build.sh`: `uv sync --frozen --no-dev`, then `unset PYTHONPATH` and `uv run make html` so Pelican does not load the broken `watchfiles` copy under `.vercel_python_packages`.

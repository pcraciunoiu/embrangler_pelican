Welcome to the codebase for [embrangler.com](http://embrangler.com), the personal and professional blog of Paul Craciunoiu.

This blog is generated using [Pelican](https://github.com/getpelican/pelican/).

## Dependencies

[Poetry](https://python-poetry.org/) is the source of truth (`pyproject.toml` + `poetry.lock`). [requirements.txt](requirements.txt) is generated from the lockfile for [Vercel](https://vercel.com/) and must not be edited by hand.

After changing dependencies:

```bash
poetry lock          # if pyproject.toml changed
make export-requirements
```

Or install [pre-commit](https://pre-commit.com/) once; it regenerates `requirements.txt` when `pyproject.toml` or `poetry.lock` change:

```bash
poetry install
poetry run pre-commit install
```

## Local build

```bash
poetry install
poetry run make html    # or: ./deploy.sh
poetry run ./develop_server
```

Output is written to `output/`.

## Vercel

Deploy uses `scripts/vercel-build.sh`: a project `.venv` from `requirements.txt` and `unset PYTHONPATH` so Pelican does not load the broken `watchfiles` copy under `.vercel_python_packages`.

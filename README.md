# PriorAuth-Flow


PriorAuth-Flow is a demo project showing how to build a small prior authorization workflow with Django. Everything runs locally with no cloud dependencies.

The stack follows a layered architecture and keeps domain code independent from infrastructure. Development uses only local services so you can run the project completely offline.


Security settings enforce input validation and safe defaults:

- All input is validated with regex helpers.
- Rich text fields pass through an HTML sanitiser.
- CSRF and session cookies require HTTPS and secure flags.
- Clickjacking and other headers (CSP, Referrer-Policy, COOP) are set via middleware.

```
priorauth_flow/
    priorauth_flow/      # Django project
        settings/
            base.py
            dev.py
            prod.py
        urls.py
    core/                # domain entities and services
    ingestion/           # FastAPI adapters
    seed-config.yaml     # sample CPT/ICD pairs
    tests/               # unit tests
```


Currently the repository provides a small core with a single service and a unit test. Future updates will expand the data generation scripts and infrastructure modules while keeping everything runnable on a laptop.


## Running the ingestion service

The `ingestion` package contains a simple FastAPI app. During development you
can start it with Uvicorn:

```bash
uvicorn ingestion.adapters.main:app --reload --limit-max-requests 1000
```

Using the `--limit-max-requests` flag ensures long-lived processes are
recycled, which helps keep memory usage predictable during demos.


## Running the Django server

For a local demo of the web application, start the built-in server:

```bash
python priorauth_flow/manage.py runserver 8000
```

These commands require only Python 3.12 and the dependencies from
`requirements.txt`.




The project includes helper Makefile targets for inspecting firmware images.

| Need | OSS tool | Install hint |
| ---- | -------- | ------------ |
| Section breakdown of an ELF | `arm-none-eabi-size` (part of GNU Arm Embedded Toolchain) | `apt-get install gcc-arm-none-eabi` |
| Convert ELF → BIN | `arm-none-eabi-objcopy` | Same package |
| Fine-grained size diff | `bloaty` (Mozilla) | `brew install bloaty` / `apt ...` |
| Scriptable math | Python 3.12 std-lib | Already in CI image |

Run `make help` to see the available targets, including `elf-size`, `elf-to-bin` and `size-diff`. A GitHub Actions workflow executes these checks along with the unit tests and linting.


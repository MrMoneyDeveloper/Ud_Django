# Architecture Overview

This project demonstrates a self-hosted workflow that also runs on the AWS free tier. The services are containerised and orchestrated with Docker Compose by default, with optional Terraform modules for AWS deployment. Local development uses LocalStack and Redpanda to avoid any cloud dependencies.

```
.
├─ priorauth_flow/        # Django project and settings
├─ core/                 # domain logic and services
├─ ingestion/            # FastAPI ingestion adapters
└─ seed-config.yaml      # fake CPT/ICD pairs used in tests
```

The aim is to show intermediate DevOps and Django skills without needing real clinical data or insurer APIs. Local setup mirrors the cloud architecture so reviewers can run everything offline.

Security hardening touches every layer:
* Input validation helpers keep malformed IDs out.
* HTML sanitiser prevents rich text attacks.
* CSRF protection and secure cookies are enabled.
* Clickjacking denied and custom middleware sets CSP, Referrer-Policy and COOP headers.

During development the ingestion service runs with Uvicorn. The startup command
includes `--limit-max-requests` so worker processes periodically restart,
reducing memory bloat over time.

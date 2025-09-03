# Shipic Data — Starter Repo (MVP)

Shipic is a Data-as-a-Service layer for commerce. This starter repo gives you a secure Python backend to:
- Ingest product/catalog data (Shopify, Printful — stubs included)
- Normalize & store products
- Overlay trend data (Google Trends stub, TikTok placeholder)
- Expose a small FastAPI for health checks and listing products

> Stack: **Python 3.12**, **FastAPI**, **SQLAlchemy**, **PostgreSQL (docker-compose)**, **httpx**

---

## Quickstart (Local Dev)

1) **Clone & env**
```bash
cp backend/.env.example backend/.env
```

2) **Start Postgres with Docker**
```bash
docker compose -f backend/docker-compose.yml up -d
```

3) **Create venv & install**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

4) **Run API**
```bash
uvicorn app.main:app --reload
```
Visit http://127.0.0.1:8000/health and http://127.0.0.1:8000/products

---

## Environment Variables (`backend/.env`)

```ini
# DB
DATABASE_URL=postgresql+psycopg2://shipic:shipic@localhost:5432/shipic
# For quick dev without Docker, you can use SQLite (uncomment below and comment the Postgres line):
# DATABASE_URL=sqlite:///./shipic.db

# Connectors (replace with your secrets)
SHOPIFY_STORE_DOMAIN=example.myshopify.com
SHOPIFY_ADMIN_API_ACCESS_TOKEN=your_token_here

PRINTFUL_API_KEY=your_printful_key_here

# Trends
GOOGLE_TRENDS_GEO=US
```

> **Security note:** Never commit real secrets. Use a secret store in production (e.g., Azure Key Vault).

---

## Structure

```text
backend/
  app/
    main.py               # FastAPI app
    config.py             # Pydantic settings
    db.py                 # SQLAlchemy engine/session
    models.py             # SQLAlchemy models
    schemas.py            # Pydantic schemas
    utils/logging.py      # Logger setup
    routers/
      health.py
      products.py
    services/
      shopify.py
      printful.py
      enrichment.py
      trends/
        google_trends.py
        tiktok.py         # placeholder
    workers/
      jobs.py
      queues.py           # optional placeholder for RQ/Celery later
  tests/
    test_health.py
  requirements.txt
  docker-compose.yml
  Dockerfile
  .env.example
  Makefile
```

---

## Next Steps

- Wire in real Shopify & Printful calls (see stubs).
- Decide on job runner (Celery/RQ/Azure Functions timers) and implement `workers/`.
- Add Alembic migrations.
- Add API keys via Azure Key Vault + Managed Identity for production.
- Add auth (JWT via API Gateway or Azure APIM) when exposing beyond internal.

---

## License
MIT (or your choice)

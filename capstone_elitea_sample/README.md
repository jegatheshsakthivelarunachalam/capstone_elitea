# EliteA Sample Inventory API

A small Python REST API for demonstrating the EliteA Automated Documentation Sync workflow.

## Technology
- Python 3.11+
- FastAPI and Uvicorn
- Pydantic (through FastAPI)
- Pytest

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Interactive API documentation: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/products` | List sample products |
| GET | `/products/{product_id}` | Retrieve one product |

## Configuration
- `APP_ENV`: application environment; defaults to `development`.
- `APP_NAME`: application display name; defaults to `EliteA Sample Inventory API`.

Document environment-variable names only. Never commit actual secrets or credentials.

## Tests

```bash
pytest -q
```

FastAPI exposes the OpenAPI JSON schema at `/openapi.json`.

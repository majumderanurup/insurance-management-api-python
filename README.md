# 02 — Health Check Route

## Overview

Added a dedicated health check endpoint using a FastAPI router.

## What We Did

- Removed the default `GET /` route
- Created `app/routers/health.py`
- Added `GET /health`
- Registered the health router in `main.py`
- Added `Health` Swagger tag at router level

## Run

```bash
uv run uvicorn app.main:app --reload
```

Health: `http://127.0.0.1:8000/health`

Swagger: `http://127.0.0.1:8000/docs`

## Next

**03 — Customer Route — Mock Response**

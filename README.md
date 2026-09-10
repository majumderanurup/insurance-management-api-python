# 01 — Basic `uv` Setup & Project Foundation

## Overview

Set up the initial **Insurance Management API** using `uv` and FastAPI.

## What We Did

- Initialized the project with `uv`
- Added FastAPI and Uvicorn
- Created a minimal FastAPI application
- Added `GET /` root endpoint
- Added basic `.gitignore`
- Verified Swagger documentation

## Run

```bash
uv run uvicorn app.main:app --reload
```

API: `http://127.0.0.1:8000`

Swagger: `http://127.0.0.1:8000/docs`

## Next

**02 — Health Check Route**

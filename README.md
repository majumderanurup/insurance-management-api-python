# 03 — Customer Route — Mock Response

## Overview

Added the Customer router with a simple mock customer response.

## What We Did

- Created `customer.py` router
- Added `GET /customers`
- Added mock customer data
- Registered Customer router in `main.py`
- Added `Customer` Swagger tag

## Run

```bash
uv run uvicorn app.main:app --reload
```

Customers: `http://127.0.0.1:8000/customers`

Swagger: `http://127.0.0.1:8000/docs`

## Next

**04 — Introduce Service Layer — Simple Object**

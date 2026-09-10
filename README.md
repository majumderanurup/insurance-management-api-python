# 05 — Dependency Injection — Service Layer

## Overview

Introduced FastAPI Dependency Injection for the Customer Service.

## What We Did

- Created `app/dependencies.py`
- Added `get_customer_service()`
- Used `Depends()` in the Customer router
- Removed manual service instantiation

## Flow

```text
Customer Router
      ↓ Depends()
CustomerService
      ↓
Mock Data
```

## Next

**06 — Environment Configuration**

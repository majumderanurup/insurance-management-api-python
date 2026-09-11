# 14 — Product CRUD

## Overview

Added Insurance Product CRUD using the database, repository, service, and API schema layers.

## What We Did

- Added Product model
- Added Product type enum
- Added product age eligibility fields
- Added product sum assured fields
- Added Product Repository
- Added Product Service
- Added Product API schemas
- Added Product CRUD endpoints
- Registered Product dependencies and router

## Flow

```text
Product Router
      ↓
ProductService
      ↓
ProductRepository
      ↓
SQLAlchemy Session
      ↓
SQLite
```

## Next

**15 — Business Rules for Product**

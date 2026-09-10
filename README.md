# 08 — Customer CRUD

## Overview

Added full Customer CRUD using the database, repository, service, and transaction layers.

## What We Did

- Added `GET /customers`
- Added `GET /customers/{customer_id}`
- Added `POST /customers`
- Added `PUT /customers/{customer_id}`
- Added `DELETE /customers/{customer_id}`
- Added Customer date of birth
- Added Customer Repository CRUD operations
- Added transaction handling in `CustomerService`

## Flow

```text
Customer Router
      ↓
CustomerService
      ↓
CustomerRepository
      ↓
SQLAlchemy Session
      ↓
SQLite
```

## Next

**09 — API Schemas — Input & Output**

# 09 — API Schemas — Input & Output

## Overview

Introduced Pydantic schemas to define API request and response structures.

## What We Did

- Created Customer request schema
- Created Customer response schema
- Changed POST `/customers` to accept JSON request body
- Changed PUT `/customers/{customer_id}` to accept JSON request body
- Added response models to Customer endpoints
- Separated API schemas from the database model

## Flow

```text
JSON Request
      ↓
CustomerRequest
      ↓
Customer Router
      ↓
CustomerService
      ↓
CustomerRepository
      ↓
SQLAlchemy
      ↓
CustomerResponse
      ↓
JSON Response
```

## Next

**10 — Pydantic Validation & API Input Rules**

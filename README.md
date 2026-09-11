# 16 — Policy CRUD

## Overview

Added Policy CRUD with customer/product relationships, reusable dependents, and auto-generated policy numbers.

## What We Did

- Added Policy model
- Added PolicyStatus enum
- Added Dependent model
- Added Policy ↔ Dependent many-to-many relationship
- Added PolicyDependent association table
- Added Policy Repository
- Added Dependent Repository
- Added Policy Service
- Added Policy API schemas
- Added Policy CRUD endpoints
- Added auto-generated policy numbers
- Added Policy dependencies

## Flow

```text
Policy Router
      ↓
PolicyService
      ↓
PolicyRepository
      ↓
SQLAlchemy Session
      ↓
SQLite
```

## Next

**17 — Premium Calculation Service**

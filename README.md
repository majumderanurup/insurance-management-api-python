# 15 — Business Rules for Product

## Overview

Added Product field validation and service-level business rules.

## What We Did

- Added Product field validation using Pydantic
- Added common application exception base
- Added Product business rule exception
- Added entry age range validation
- Added sum assured range validation
- Added service-level business rule validation

## Flow

```text
Product Request
      ↓
Pydantic Validation
      ↓
ProductService
      ↓
Business Rules
      ↓
ProductRepository
      ↓
SQLAlchemy
      ↓
SQLite
```

## Next

**16 — Policy CRUD**

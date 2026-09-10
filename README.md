# 11 — Service and Database-Level Business Rules

## Overview

Added business rules, application exceptions, and centralized exception handling for Customer operations.

## What We Did

- Added customer email uniqueness business rule
- Added customer existence validation
- Added application exception hierarchy
- Added common application exception handler
- Added `409 Conflict` for duplicate customers
- Added `404 Not Found` for missing customers
- Added database uniqueness constraint as a final safeguard

## Flow

```text
Customer Router
      ↓
CustomerService
      ↓
Business Rules
      ↓
CustomerRepository
      ↓
SQLAlchemy
      ↓
SQLite

Business Exception
      ↓
Common Exception Handler
      ↓
HTTP Response
```

## Next

**12 — Application Logging**

# 07 — Database Layer — Real Responses

## Overview

Introduced the database layer using SQLite and SQLAlchemy, and replaced the Customer mock response with real database data.

## What We Did

- Added SQLAlchemy
- Added SQLite database configuration
- Created SQLAlchemy `Base`, engine and session
- Created Customer model
- Added database table creation at application startup
- Added Customer Repository
- Injected repository through the service layer
- Changed `GET /customers` to return database data

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

**08 — API Schemas — Input & Output**

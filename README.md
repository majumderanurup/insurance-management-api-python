# 13 — Correlation and Request IDs

## Overview

Added request-level correlation IDs to trace requests across application and database logs.

## What We Did

- Added request ID middleware
- Generated a unique UUID for each request
- Propagated request ID using `ContextVar`
- Added request ID to application logs
- Added request ID to SQLAlchemy logs
- Added `X-Request-ID` response header
- Added request ID to application error responses
- Added console and file log correlation

## Flow

```text
HTTP Request
      ↓
Request ID Middleware
      ↓
ContextVar
      ↓
Router / Service / Repository
      ↓
Application + Database Logs
      ↓
Console + app.log
```

## Next

**14 — Product CRUD**

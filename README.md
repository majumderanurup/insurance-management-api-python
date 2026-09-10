# 12 — Application Logging

## Overview

Introduced application logging with console and file output.

## What We Did

- Added centralized logging configuration
- Added console logging
- Added file logging
- Created `logs/app.log`
- Added `logs/` to `.gitignore`
- Added application logs to Customer operations
- Added `INFO`, `WARNING`, and exception logging

## Flow

```text
Application
      ↓
Python Logging
      ↓
 ┌────┴────┐
 ↓         ↓
Console   logs/app.log
```

## Next

**13 — Correlation and Request IDs**

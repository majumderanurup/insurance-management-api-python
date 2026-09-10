# 04 — Introduce Service Layer — Simple Object

## Overview

Introduced the Customer Service layer to separate application logic from the API router.

## What We Did

- Created `CustomerService`
- Moved mock customer data into the service
- Updated Customer router to use the service
- Kept the response behavior unchanged

## Flow

```text
Customer Router → CustomerService → Mock Data
```

## Next

**05 — Dependency Injection — Service Layer**

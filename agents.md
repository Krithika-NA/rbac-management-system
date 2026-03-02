# AI Usage & Guidance

## Overview

AI tools were used during development to assist with structure, debugging, and refinement. All generated content was reviewed and validated before integration.

The system design, architecture decisions, and final implementation choices were made manually.

---

## How AI Was Used

AI assistance was used for:

- Suggesting a layered architecture structure
- Reviewing import and migration errors
- Refactoring for cleaner separation of concerns
- Generating test scaffolding
- Reviewing API structure and error handling
- Identifying edge cases in permission enforcement

---

## Constraints Given to AI

AI was instructed to:

- Prefer simplicity over cleverness
- Avoid overengineering
- Follow clean separation of concerns
- Enforce deny-by-default access control
- Keep business logic centralized in service layer
- Avoid hardcoding roles inside routes
- Prevent invalid states (duplicate users, roles, permissions)

---

## Human Validation

All AI-generated code was:

- Manually reviewed
- Refactored where necessary
- Tested using pytest
- Validated through manual API testing
- Verified for logical correctness

No confidential, proprietary, or employer-owned code, data, or prompts were used.

---

## Design Ownership

Final architecture decisions, structure, and implementation strategy were manually designed and adjusted beyond initial AI suggestions.

AI was used as an assistant — not as an autonomous agent.
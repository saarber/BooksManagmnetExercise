# Test Documentation for Library Management API

## Overview

This document outlines the test cases implemented for the Library Management API as defined in the provided Flask application. The goal is to ensure correctness, stability, and proper error handling across all API endpoints.

---

## Test Coverage Summary

### Books (CRUD)
| Test Case | Description | Success Code | Failure Code |
|-----------|-------------|---------------|---------------|
| Get all books | Ensure book list is returned | 200 | - |
| Add book | Add valid book with required fields | 201 | - |
| Add book (missing title) | Fail to add book with missing fields | - | 400 |
| Update book | Update an existing book’s title | 200 | - |
| Update non-existent book | Attempt to update book that doesn't exist | - | 404 |
| Delete book | Delete a valid book | 200 | - |
| Delete book on loan | Prevent deletion of borrowed book | - | 400/409 |

### Users
| Test Case | Description | Success Code | Failure Code |
|-----------|-------------|---------------|---------------|
| Get users | Ensure user list is returned | 200 | - |

### Book Borrowing / Returning
| Test Case | Description | Success Code | Failure Code |
|-----------|-------------|---------------|---------------|
| Borrow book | Valid borrow action by existing user | 200 | - |
| Return book | Return a borrowed book | 200 | - |
| Borrow already borrowed book | Prevent double-borrow | - | 400 |
| Return unborrowed book | Prevent return of book not borrowed | - | 400 |

---

## Advanced & Edge Case Tests

### Edge Conditions
- **Duplicate ISBN** (planned): Adding a book with same ISBN should fail. (Currently not enforced by backend)
- **Partial Update**: Ensure unmentioned fields are preserved on update.
- **Delete While Loaned**: Prevent deletion of a loaned book.

### Concurrency
- Simultaneous borrow attempts by two users — only one should succeed (simulates race condition).

### Performance
- Bulk-create 100 books under 3 seconds to ensure acceptable response time and resource handling.

---

## Importance of Failure Scenarios

Failure paths are critical to test:
- They confirm that the backend properly validates data.
- Prevent inconsistent state (e.g., double-loans, null fields).
- Ensure concurrency safety in multi-user scenarios.
- Highlight missing constraints in the backend for future improvement.

---

## Recommendations for Backend

- Enforce unique ISBNs to prevent duplicate entries.
- Improve schema validation for PUT/POST (required fields, types).

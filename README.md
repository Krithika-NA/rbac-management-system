# RBAC Management System

## Overview

This project implements a Role-Based Access Control (RBAC) system using Flask (backend) and React (frontend). 

The system allows:
- Dynamic creation of permissions
- Assignment of permissions to roles
- Assignment of roles to users
- Enforcement of access control through middleware

Access is enforced using a deny-by-default policy.

---

## Architecture

The backend follows a layered architecture:

- Models → Database schema
- Repository Layer → Database access abstraction
- Service Layer → Business logic
- Middleware → Permission enforcement
- Routes → API endpoints
- Frontend → User interaction layer

This separation ensures simplicity, maintainability, and change resilience.

---

## Key Technical Decisions

- Used decorator-based middleware for permission enforcement.
- Implemented many-to-many relationship between roles and permissions.
- Used SQLite for portability and simplicity.
- Centralized business logic in service layer.
- Enforced deny-by-default security model.
- Added automated tests using pytest.

---

## Tech Stack

Backend:
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

Frontend:
- React

Database:
- SQLite

---

## Running the Project

### Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask --app backend.app db upgrade
python -m backend.app

### Frontend

cd frontend
npm install
npm start

---

## Limitations

- No authentication (trusts X-Username header)
- SQLite not production-ready
- No role hierarchy
- Minimal UI validation

---

## Extension Ideas

- Add JWT authentication
- Add role hierarchy
- Add audit logging
- Add permission management dashboard
- Deploy to cloud environment

---

## AI Usage

AI tools were used to:
- Scaffold project structure
- Suggest layered architecture
- Assist with debugging import and migration issues
- Review and refine test structure

All AI-generated code was reviewed and validated before integration.
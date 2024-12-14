# FastAPI LMS

## Overview & Requirements
This is a learning management system where teachers can manage students, and students can view their courses.

### Features
- **Teacher Functionality**:
  - Perform CRUD operations on students.
  - Create courses with sections and content blocks.
  - Assign courses to students.
- **Student Functionality**:
  - View their assigned courses in a list.
  - Explore sections and content blocks of individual courses.
  - Track their progress for each course.

## Running the App Locally

1. **Prerequisites**:
   - Ensure Python, Poetry, and Postgres are installed.
   - Postgres must be running. Refer to the linked video for setup instructions.

2. **Setup**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Install packages:
     ```bash
     poetry install
     ```
   - Run the development server:
     ```bash
     uvicorn main:app --reload
     ```

## Tech Stack
- **Backend Framework**: FastAPI
- **Language**: Python 3.9+
- **Package Management**: Poetry
- **Database**: Postgres
- **ORM**: SQLAlchemy 1.4+
- **Migrations**: Alembic
- **Validation**: Pydantic
- **Code Formatting**: Black
- **Linting**: Flake8
- **Pre-commit Hooks**

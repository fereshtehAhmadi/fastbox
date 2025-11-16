# FastBox

A lightweight sandbox project to practice and explore **FastAPI** concepts.

## Installation

Make sure you have Python 3.10+ installed.

Install FastAPI (with all recommended dependencies):

```
pip install -r requirements/base.txt
```
## Initialize Alembic

Alembic is a database migration tool for SQLAlchemy. Use the following commands to set it up and manage migrations:

```bash
# Initialize Alembic in your project
alembic init migrations

# Create a new migration file by detecting changes in your models
alembic revision --autogenerate -m "add user model"

# Apply all migrations up to the latest version
alembic upgrade head

# Revert all migrations back to the initial state
alembic downgrade base
```

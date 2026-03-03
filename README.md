# django-project

A small hands on project to practice django.

## Setup

1. Clone the repository
```bash
git clone https://github.com/AbdoAlshoki2/django-students-project.git
cd django-students-project
```
2. Create a virtual environment
```bash
python -m venv .venv

# or using uv
uv venv .venv
```
4. Run the server
```bash
python manage.py runserver
```

## Current Routes

- `/admin` - Admin panel.
- `/students` - Students list.
- `/students/<name>` - Just display the student name (for later use).

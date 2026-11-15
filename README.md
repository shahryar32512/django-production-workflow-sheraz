# Django Development and Production Workflow

A Django project demonstrating development and production workflow using Docker, Git and GitHub.

## Technologies Used
- Python 3.10
- Django 5.2
- Docker and Docker Compose
- Git and GitHub

## Project Applications
- Home App: http://localhost:8001/
- Menu App: http://localhost:8001/menu/

## Setup
Run: docker compose up --build

## System Check
Run: docker compose exec web python manage.py check

## Automated Tests
Run: docker compose exec web python manage.py test

## Git Branch Strategy
- main: Final approved code
- production: Production-ready code
- development: Integrated development code
- testing: Testing and automated tests

## Project Status
Home App and Menu App are working. All 4 automated tests are passing.

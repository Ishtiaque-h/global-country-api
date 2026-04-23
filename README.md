# Global Country API

A Django + Django REST Framework project for storing, querying, and managing country data.

## Live Demo

Production demo: https://countryapi-psi.vercel.app

Demo credentials:

- Username: admin
- Password: 123456

## Tech Stack

- Python 3.12+
- Django 5.2
- Django REST Framework
- PostgreSQL
- JWT authentication (Simple JWT)
- OpenAPI docs (drf-spectacular)

## Features

- Seed country data from an external API
- JWT-protected REST endpoints
- Country CRUD operations
- Filters by region, language, and name
- Browser UI for login and country listing/details
- Swagger UI for interactive API docs

## Project Structure

- country_api/core: models, serializers, web views, seed command
- country_api/api: REST API views and routes
- templates/core: login and country list UI templates

## Prerequisites

- Python 3.12 or later
- PostgreSQL 14 or later

## Setup

1. Clone the repository and move into the project root (where manage.py exists).
2. Create a PostgreSQL database.
3. Copy .sample_env to .env and set values.
4. Create and activate a virtual environment.
5. Install dependencies.
6. Run migrations.
7. Seed country data.
8. Create a user.
9. Run the server.

Example commands:

```bash
cp .sample_env .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

Windows activation example:

```bash
.venv\Scripts\activate
```

## Environment Variables

Configure these in .env:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASS=your-db-password
DB_HOST=localhost
DB_PORT=5432
API_URL=https://restcountries.com/v3.1/all?fields=name,cca2,region,latlng,latlng,area,population,flags,timezones,capital
```

## Authentication

Most API endpoints require a JWT access token.

1. Create a user with:

```bash
python manage.py createsuperuser
```

2. Get a token:

Endpoint:

- POST /api/login/

Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Success response includes a token:

```json
{
  "message": "Success",
  "status": 200,
  "token": "<access_token>"
}
```

3. Send the token in the Authorization header:

```text
Authorization: Bearer <access_token>
```

## API Documentation

- Swagger UI: /api/schema/swagger-ui/
- OpenAPI schema: /api/schema/

## API Endpoints

### Public

- POST /api/login/

### Protected

- GET /api/get-all-countries/
- GET /api/get-specific-country/{id}/
- POST /api/save-country-data/
- PUT /api/update-country-data/{id}/
- DELETE /api/delete-specific-country/{id}/
- GET /api/get-countries-with-region/?region={region}
- GET /api/get-countries-with-language/?language={language}
- GET /api/get-countries-with-name/?country={country}

### Sample Create/Update Payload

```json
{
  "cca2": "TSTCN",
  "common_name": "Test Country",
  "official_name": "Republic of Test Country",
  "region": "Asia",
  "subregion": "Southern Asia",
  "capital": "Test City",
  "latitude": -20.0,
  "longitude": 20.0,
  "area": 14500,
  "population": 12345,
  "flag": "https://flagcdn.com/w320/bw.png",
  "languages": ["English"],
  "timezones": ["UTC+05:00"]
}
```

## Web UI

- Login page: /login/
- Country list page: /
- Country details (AJAX): /get-country-details?country_id={id}

## Seed Command

Use this to pull country data from API_URL and store it in the database:

```bash
python manage.py seed_data
```

## Notes

- The API uses JWT auth for protected routes.
- Login endpoint has rate limiting for repeated attempts.


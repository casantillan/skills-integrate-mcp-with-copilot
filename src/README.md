# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities
- Authenticate as a teacher or student before changing registrations

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity (HTTP Basic authentication required)         |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister (HTTP Basic authentication required)                    |

## Authentication

`GET /activities` is public. Signup and unregister require HTTP Basic authentication.
Teachers can manage any registration; students can manage only their own registration.
User records are stored in `users.json` with PBKDF2-SHA256 password hashes. The sample
development accounts are `teacher` / `teacher-password` and
`michael@mergington.edu` / `student-password`; replace them before deployment.

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.

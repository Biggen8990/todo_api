# To-Do API

A personal to-do list REST API built with Python and Flask.

## Setup

Python version: 3.12

1. Create a virtual environment:
   `python3 -m venv .venv`

2. Activate the virtual environment on macOS/Linux:
   `source .venv/bin/activate`

3. Install the project dependencies:
   `pip install -r requirements.txt`

4. Start the Flask application:
   `flask --app "app:create_app('development')" run`


## Environment Variables

Copy `.env.example` to `.env` using:

`cp .env.example .env`

Then replace the placeholder values with your own settings.

- `JWT_SECRET` – A secret key used to sign authentication tokens so they can't be forged without the key. It should be long and random.
- `DATABASE_URL` – Tells the application which database to connect to. For local development, you can use `sqlite:///dev.db`.


## Migrations

Migrations are not set up yet for this project. Flask-Migrate has been configured, but no migrations have been created or ran yet.

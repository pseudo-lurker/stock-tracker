
Stock tracker




Stock tracker is a simple app that tracks significant stock price changes for
predetermined  companies.

Requirements

Python 3.10, RabbitMQ


Installation
Clone the repository with:

git clone git@github.com:pseudo-lurker/stock-tracker.git

Install requirements with:

pip install -r requirements.txt

Configuration

Several settings are read from the .env file, the template for which is provided.

RabitMQ needs to be set up as described here:
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html

Initialize database for testing

To generate the database, run migrations with:

python manage.py migrate

This will create the initial company entries, and fill the historic data for them.

Running the server

Server can be started for local development using:

python manage.py runserver

This will start a local server on http://127.0.0.1:8000.

The background tasks are handled by Celery which can be started with the following commands:
celery -A tracker.celery beat --loglevel=info

python -m celery -A tracker worker

from the `stock-tracker/tracker` folder


In production the server is run via gunicorn and nginx.

Database

For the simple current use the default SQLite database is sufficient, in case of 
further expansion PostgreSql would be used.

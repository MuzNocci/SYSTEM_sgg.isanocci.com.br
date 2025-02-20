#!/bin/sh



set -e

python manage.py makemigrations client
python manage.py migrate client
python manage.py makemigrations package
python manage.py migrate package
python manage.py makemigrations gallery
python manage.py migrate gallery

python manage.py collectstatic --noinput

gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 5
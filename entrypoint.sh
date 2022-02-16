#!/bin/sh

python manage.py migrate
gunicorn deals_sd.wsgi:application --bind 0:8000
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python seed_data.py
python manage.py collectstatic --noinput

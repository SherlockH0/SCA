#!/usr/bin/env sh

set -e

echo "Running migrations..."
uv run src/manage.py migrate --no-input

echo "Running daphne on port 8000..."
uv run src/manage.py runserver 0.0.0.0:8000

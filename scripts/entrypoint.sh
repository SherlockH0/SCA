#!/usr/bin/env sh

set -e

echo "Running migrations..."
poetry run python -m backend.manage migrate --no-input

echo "Running daphne on port 8000..."
poetry run daphne -b 0.0.0.0 -p 8000 backend.project.asgi:application

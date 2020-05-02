#!/usr/bin/env bash

set -e

THIS_DIR=$(dirname "$0")
cd ${THIS_DIR}
cd ..

# Frontend
npm install

# Backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Database
cd src/backend
FLASK_ENV=development python manage.py db upgrade

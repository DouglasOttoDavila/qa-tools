#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Start Gunicorn with the configuration file
gunicorn -c gunicorn_config.py app:app

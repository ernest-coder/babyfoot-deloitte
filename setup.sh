#!/bin/bash

# Use pyenv to set the Python version
pyenv global 3.11.2

# Verify Python version
python --version

# Install dependencies using pip
pip install --upgrade pip
pip install -r requirements.txt

# Run your application
python api/app.py

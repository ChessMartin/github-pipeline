#!/bin/bash

git pull origin main

pip install -r requirements.txt

echo "Deploying the app"

python3 main.py

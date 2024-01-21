#!/bin/bash

git pull origin staging

pip install -r requirements.txt

echo "Doing some tests on the staging branch"

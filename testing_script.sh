#!/bin/bash

git pull origin staging

pip install -r requirements.txt

echo "Printed from the testing script"

#!/bin/bash

echo "CREATE DATABASE"
python src/database/connect.py
tail -f /dev/null
#! /bin/bash

pipenv run csvsql \
    --db $DATABASE_URL \
    --insert ./data/*.csv

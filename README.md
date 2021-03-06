# medicare-appeals-prototyping

[WIP] An exploratory repository to test prototypes for viewing and interacting with the life cycle of a Medicare appeal.

## Overview

This project will

## Getting Started

### Using Docker

Docker offers fast, lightweight, automated development environments. [Download Docker](https://www.docker.com/products/docker-desktop) if you don’t have it.

#### Build and run Docker containers

```bash
docker-compose build
docker-compose run web pipenv run python manage.py migrate
docker-compose up
# Development server http://localhost:8000/
```

#### Database migrations

Run this the first time, and whenever there are new migrations. Docker containers must be running to execute this command.

```bash
docker-compose exec web pipenv run migrate
```

#### ETL loading sample data

```
docker-compose run etl bash ./scripts/insert_data.sh

docker-compose run etl pipenv run invoke createdata
```

#### Connecting to the database with PSQL

```
# Run psql connection command
docker-compose run db psql -h db -U medicare_appeals_user medicare_appeals_dev

# Next enter password `password`
Password for user medicare_appeals_user: password
```

#### Creating a local pg_dump

```
docker-compose run db pg_dump postgres://medicare_appeals_user:password@db/medicare_appeals_dev -a -F c -f /var/lib/postgresql/data/extract.pg
docker cp <CONTAINER_ID>:/var/lib/postgresql/data/extract.pg ./extract.pg
```

### Migrating local database extract to a Cloud.gov's shared-psql database

```
## Run ETL process for the sample data to load data into the model locally
docker-compose run etl bash ./scripts/insert_data.sh
docker-compose run etl pipenv run invoke createdata

## Create a dump of the data to be loaded into the Cloud.gov database
docker-compose run db pg_dump postgres://medicare_appeals_user:password@db/medicare_appeals_dev -a -F c -f /var/lib/postgresql/data/extract.pg
docker cp <CONTAINER_ID>:/var/lib/postgresql/data/extract.pg ./extract.pg

## Install the `connect-to-service` database plugin to be able to connect to remote database
cf connect-to-service --no-client medicare-appeals-app medicare-appeals-database
// returns
// Host: localhost
// Port: <PORT>
// Username: <USER>
// Password: <PASSWORD>
// Name: <DATABASE_NAME>

## Use your local extract created after running the ETL pipeline
pg_restore -U <USER> -h 127.0.0.1 -p <PORT> -d <DATABASE_NAME> --clean --no-owner --no-acl ./extract.pg
enter password: <PASSWORD>
```

#### Debugging

- Run commands in a one-off container: `docker-compose run web /bin/bash`
- Connect to running container: `docker-compose exec db /bin/bash`
- Get a psql shell: `docker-compose exec db psql -U postgres`

### Using your own local environment

#### Pre-reqs

- Python `v3.6.0`
- PostgreSQL `v10`

#### Setting up the environment variables

Make a copy the `.env.dev` file and save it as `.env`. This will have the environment variables necessary to work and run the project locally.

#### Installing Python and Pipenv

- [Install Python](https://www.python.org/downloads/) for your computer OS

- [Install Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) to manage and install Python environment and dependencies.

##### Installing the project dependencies with Pipenv

```bash
$ git clone git@github.com:18F/medicare-appeals-prototyping.git

$ cd medicare-appeals-prototyping

$ pipenv install
```

#### Setting up the database for local development and testing

[Installing PostgreSQL](https://www.postgresql.org/download/) for your computer's OS

##### Create the development database locally

```bash
# Create the medicare dev database
$ createdb medicare_appeals_dev

# Note - if a fresh database is necessary run
$ dropdb medicare_appeals_dev && createdb medicare_appeals_dev
```

##### Migrating the database

```bash
$ pipenv run migrate
```

#### Starting the development server

```bash
$ pipenv run develop
# Development server http://localhost:8000/
```

#### Running the tests

```bash
$ pipenv run test
```

#### Formatting the Python code

```bash
$ pipenv run format
# Formatting done with https://github.com/google/yapf
```

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

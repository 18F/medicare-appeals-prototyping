# medicare-appeals-prototyping

[WIP] An exploratory repository to test prototypes for viewing and interacting with the life cycle of a Medicare appeal.

## Overview

This project will

## Getting Started

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

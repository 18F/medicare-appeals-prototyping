FROM python:3.6.0

# Set locale
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Better console output through docker
ENV PYTHONUNBUFFERED 1

# Set Python Path
ENV PYTHONPATH=/usr/local/bin

# DB connnection URL.
ENV DATABASE_URL="postgresql://postgres:@db:5432/medicare_appeals_dev"

# Working directory
ENV app /medappeals
RUN mkdir $app
WORKDIR $app
ADD . $app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --deploy

# Start the server
CMD pipenv run develop 0.0.0.0:8000
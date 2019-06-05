FROM python:3.6.0

# Set locale
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Better console output through docker
ENV PYTHONUNBUFFERED 1

# Set Python Path
ENV PYTHONPATH=/usr/local/bin

# Working directory
ENV app /etl
RUN mkdir $app
WORKDIR $app
ADD . $app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --deploy

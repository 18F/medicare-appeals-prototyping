FROM python:3.6.0

# Better console output through docker
ENV PYTHONUNBUFFERED 1

# Don't write .pyc files
#ENV PYTHONDONTWRITEBYTECODE 1

# Set locale
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Set Python Path
ENV PYTHONPATH=/usr/local/bin

# Our working directory
ENV app /medappeals
RUN mkdir $app
WORKDIR $app

# Add everything else
ADD . $app


# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
# COPY Pipfile Pipfile.lock $app/
RUN pipenv install --system --verbose



CMD pipenv run develop
FROM python:3.10-slim-buster

# Set environment variables
COPY requirements.txt requirements.txt

# Install pipenv
RUN set -ex && pip install --upgrade pip

# Install dependencies
RUN set -ex && pip install -r requirements.txt

WORKDIR /CrudFastApi

COPY ./app/ /CrudFastApi/app
COPY ./tests/ /CrudFastApi/tests
COPY .env /CrudFastApi/
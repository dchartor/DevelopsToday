FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 .

COPY . /code/
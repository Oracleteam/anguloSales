FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . /src
WORKDIR /src

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000
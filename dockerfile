FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt
#RUN pipenv install --system --verbose
RUN python manage.py collectstatic -v 1 --link --clear
EXPOSE 8000
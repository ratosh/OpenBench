FROM python:3

RUN pip install --upgrade pip

COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install Django==2.0.6
RUN pip3 install django-htmlmin
RUN pip3 install requests

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py migrate --run-syncdb
RUN python3 manage.py createsuperuser
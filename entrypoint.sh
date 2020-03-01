#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py makemigrations OpenBench
python manage.py migrate OpenBench
python manage.py migrate --run-syncdb
python manage.py set_superuser
python manage.py runserver 0.0.0.0:8000
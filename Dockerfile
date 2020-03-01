FROM python:3

RUN apt-get update && apt-get install -y dos2unix

RUN pip install --upgrade pip

COPY . /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install -r requirements.txt

RUN dos2unix entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
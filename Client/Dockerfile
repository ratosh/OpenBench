FROM python:3

RUN apt list

RUN apt-get update && \
    apt-get install -y dos2unix && \
    apt-get install -y openjdk-11-jre-headless && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN find . -type f -print0 | xargs -0 dos2unix
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
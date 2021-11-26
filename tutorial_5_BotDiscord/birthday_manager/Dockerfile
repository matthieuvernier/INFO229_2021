FROM python:3.8-slim AS base
RUN apt-get update && apt-get install --no-install-recommends --yes python3

RUN pip install mysql.connector
RUN pip install pika

ENV PYTHONUNBUFFERED 1

ARG DATABASE_IP
ENV DATABASE_IP $DATABASE_IP

COPY ./create_database.py ./create_database.py
COPY ./manager.py ./manager.py

CMD ["python", "manager.py"]
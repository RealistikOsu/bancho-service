# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /bancho-service

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD scripts/start.sh

# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /amnesia

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD scripts/start.sh
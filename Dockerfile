FROM python:3.8.0-alpine3.10
LABEL maintainer="brandon@simpleltc.com"

WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

COPY . /app/

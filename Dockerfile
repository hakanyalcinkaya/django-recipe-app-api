FROM python:3.7-alpine
MAINTAINER Hakan Yalcinkaya

ENV PYTHONUNBUFFERED 1

COPY ./requierements.txt /requierements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requierements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D djangouser
USER djangouser

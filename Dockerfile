FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev && \
    pip install -r /requirements.txt && \
    apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . /app

EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "reservi.wsgi:application", "--capture-output", "--log-level=DEBUG"]

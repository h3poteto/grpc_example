FROM python:3.7-alpine3.8

ADD . /var/opt/app

WORKDIR /var/opt/app

RUN set -x && \
    apk add --no-cache \
    git \
    build-base \
    tar \
    gzip \
    curl \
    protobuf && \
    pip install grpcio-tools

RUN set -x && \
    python client_codegen.py

WORKDIR /var/opt/app/client/python

CMD python server.py

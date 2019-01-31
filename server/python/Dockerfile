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

ENV SERVER_IP 0.0.0.0
ENV SERVER_PORT 50051

EXPOSE 50051

RUN set -x && \
    python server_codegen.py

WORKDIR /var/opt/app/server/python

CMD python server.py

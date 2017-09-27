FROM golang:1.9-alpine

RUN set -x \
    && apk add --no-cache \
    git \
    build-base \
    curl

ENV GOPATH /go
ENV APP_DIR ${GOPATH}/src/github.com
ENV APPROOT ${APP_DIR}/h3poteto/grpc_example

RUN set -x \
    && adduser -D -u 1000 go \
    && echo 'go:password' | chpasswd \
    && mkdir -p ${APP_DIR} \
    && chown -R go:go /go

WORKDIR ${APP_DIR}


ADD . ${APPROOT}
RUN chown -R go:go ${GOPATH}

USER go

RUN set -x \
    && go get -u github.com/golang/dep/... \
    && go get github.com/golang/protobuf/protoc-gen-go

ENV SERVER_PORT 9090

EXPOSE 9090

WORKDIR ${APPROOT}

RUN set -x \
    && dep ensure \
    && cd server/go \
    && go build -o server

CMD server/go/server

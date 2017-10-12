# gRPC example

## configure
Set ip address and port in `.envrc`, for example:

```bash
export SERVER_IP=127.0.0.1
export SERVER_PORT=9090
```

## server
### go

Generate a server interface, and start gRPC server.

```
$ protoc  \
        --proto_path=${GOPATH}/src \
        --proto_path=${GOPATH}/src/github.com/gogo/protobuf/protobuf \
        --proto_path=. \
        --go_out=plugins=grpc:./server/go \
        --govalidators_out=gogoimport=true:./server/go \
        proto/*.proto
$ go run server/go/server.go
```

### scala

Generate a server interface, and start gRPC server.

```
$ cd server/scala
$ sbt "compile"
$ sbt "run"
```

## client
### ruby

Generate a ruby interface.

```
$ brew install protobuf
$ gem install grpc
$ gem install grpc-tools
$ grpc_tools_ruby_protoc -I ./proto --ruby_out=client/ruby/lib --grpc_out=client/ruby/lib ./proto/customer_service.proto
```

# gRPC example

## configure
Set ip address and port in `.envrc`, for example:

```bash
export SERVER_IP=127.0.0.1
export SERVER_PORT=9090
```

And Install `protobuf`:

```bash
$ brew install protobuf
```

## server
### python
Install `grpcio-tools`:

```bash
$ pip install grpcio-tools
```

Generate a server interface, and start gRPC server.

```bash
$ python server_codegen.py
$ cd server/python
$ python server.py
Starting server...
Listen :50051
```




### go

Generate a server interface, and start gRPC server.

```
$ protoc  \
        --go_out=plugins=grpc:./server/go \
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
$ gem install grpc
$ gem install grpc-tools
$ grpc_tools_ruby_protoc -I ./proto --ruby_out=client/ruby/lib --grpc_out=client/ruby/lib ./proto/customer_service.proto
```


### python

Generate a python interface.

```bash
$ client_codegen.py
```

And request to server.

```bash
$ python add.py
Added

$ python list.py
Name: akira, Age: 12
```

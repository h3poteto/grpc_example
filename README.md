# gRPC example

## server
### go

Generate a server interface.

```bash
$  protoc --go_out=plugins=grpc:./server/go ./proto/customer_service.proto
```

## client
### ruby

Generate a ruby interface.

```bash
$ grpc_tools_ruby_protoc -I ./proto --ruby_out=client/ruby/lib --grpc_out=client/ruby/lib ./proto/customer_service.proto
```

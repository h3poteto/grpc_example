# gRPC example

## server
### go

Generate a server interface.

```bash
$  protoc --go_out=plugins=grpc:./server/go ./proto/customer_service.proto
```

## client
### ruby


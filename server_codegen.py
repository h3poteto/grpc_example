from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=./server/python',
        '--grpc_python_out=./server/python',
        './proto/customer_service.proto',
    )
)

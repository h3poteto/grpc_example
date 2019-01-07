import grpc
import os
from proto import customer_service_pb2
from proto import customer_service_pb2_grpc


def run():
    channel = grpc.insecure_channel(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    stub = customer_service_pb2_grpc.CustomerServiceStub(channel)
    responses = stub.ListPerson(customer_service_pb2.RequestType())
    for response in responses:
        print('Name: {}, Age: {}'.format(response.name, response.age))


if __name__ == '__main__':
    run()

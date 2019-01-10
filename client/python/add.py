import grpc
import os
from proto import customer_service_pb2
from proto import customer_service_pb2_grpc


def run():
    channel = grpc.insecure_channel(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    stub = customer_service_pb2_grpc.CustomerServiceStub(channel)
    stub.AddPerson(customer_service_pb2.Person(age=20, tags=['go', 'ruby']))
    print('Added')


if __name__ == '__main__':
    run()

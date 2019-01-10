import time
import os
from concurrent import futures
import grpc
from proto import customer_service_pb2
from proto import customer_service_pb2_grpc

persons = []


class Servicer(customer_service_pb2_grpc.CustomerServiceServicer):
    def AddPerson(self, request, context):
        person = {
            'name': request.name,
            'age': request.age,
            'tags': request.tags,
        }
        persons.append(person)
        print('Person added: ', person)

        return customer_service_pb2.ResponseType()

    def ListPerson(self, request, context):
        print(persons)
        for person in persons:
            yield customer_service_pb2.Person(name=person['name'], age=person['age'], tags=person['tags'])


def serve():
    print('Starting server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_service_pb2_grpc.add_CustomerServiceServicer_to_server(
        Servicer(), server
    )
    server.add_insecure_port(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    server.start()
    print('Listen :' + os.environ['SERVER_PORT'])
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print('Stop server')
        server.stop(0)


if __name__ == '__main__':
    serve()

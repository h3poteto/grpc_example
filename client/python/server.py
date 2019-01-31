import grpc
import time
import os
from proto import customer_service_pb2
from proto import customer_service_pb2_grpc

person_list = [
    {
        'name': 'Kana Asumi',
        'age': 35
    },
    {
        'name': 'Ryoko Shintani',
        'age': 37
    },
    {
        'name': 'Ayane Sakura',
        'age': 25
    },
    {
        'name': 'Aoi Yuuki',
        'age': 26
    },
    {
        'name': 'Yuuko Goto',
        'age': 43
    },
    {
        'name': 'Yui Horie',
        'age': 42
    },
    {
        'name': 'Yukari Tamura',
        'age': 42
    },
    {
        'name': 'Kana Hanazawa',
        'age': 29
    },
    {
        'name': 'Yuka Iguchi',
        'age': 30
    },
    {
        'name': 'Ayana Taketatsu',
        'age': 29
    },
    {
        'name': 'Yoko Hikasa',
        'age': 33
    }
]


def addPerson():
    channel = grpc.insecure_channel(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    stub = customer_service_pb2_grpc.CustomerServiceStub(channel)
    for person in person_list:
        stub.AddPerson(customer_service_pb2.Person(name=person['name'], age=person['age']))
    print('People are added', flush=True)


def ListPerson(stub):
    responses = stub.ListPerson(customer_service_pb2.RequestType())
    for response in responses:
        print('Name {}, Age: {}'.format(response.name, response.age), flush=True)


if __name__ == '__main__':
    addPerson()
    channel = grpc.insecure_channel(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    stub = customer_service_pb2_grpc.CustomerServiceStub(channel)
    while True:
        ListPerson(stub)
        print('-------------------------------------------------------------', flush=True)
        time.sleep(2)

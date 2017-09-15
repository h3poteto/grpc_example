#!/usr/bin/env ruby

$LOAD_PATH.push('./lib')

require 'grpc'
require 'customer_service_services_pb'

def main
  stub = Proto::CustomerService::Stub.new("127.0.0.1:9090", :this_channel_is_insecure)
  if ARGV.size == 2
    stub.add_person(Proto::Person.new(name: ARGV[0], age: ARGV[1].to_i))
  else
    stub.list_person(Proto::RequestType.new).each do |x|
      puts "name=#{x.name}, age=#{x.age}"
    end
  end
end

main

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: customer_service.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_message "proto.ResponseType" do
  end
  add_message "proto.RequestType" do
  end
  add_message "proto.Person" do
    optional :name, :string, 1
    optional :age, :int32, 2
  end
end

module Proto
  ResponseType = Google::Protobuf::DescriptorPool.generated_pool.lookup("proto.ResponseType").msgclass
  RequestType = Google::Protobuf::DescriptorPool.generated_pool.lookup("proto.RequestType").msgclass
  Person = Google::Protobuf::DescriptorPool.generated_pool.lookup("proto.Person").msgclass
end

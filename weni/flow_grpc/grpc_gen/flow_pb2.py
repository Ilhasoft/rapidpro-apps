# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/flow_grpc/grpc_gen/flow.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/flow_grpc/grpc_gen/flow.proto',
  package='flow',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"weni/flow_grpc/grpc_gen/flow.proto\x12\x04\x66low\"6\n\x0f\x46lowListRequest\x12\x11\n\tflow_name\x18\x01 \x01(\t\x12\x10\n\x08org_uuid\x18\x02 \x01(\t\"\"\n\x04\x46low\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t2?\n\x0e\x46lowController\x12-\n\x04List\x12\x15.flow.FlowListRequest\x1a\n.flow.Flow\"\x00\x30\x01\x62\x06proto3'
)




_FLOWLISTREQUEST = _descriptor.Descriptor(
  name='FlowListRequest',
  full_name='flow.FlowListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flow_name', full_name='flow.FlowListRequest.flow_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='flow.FlowListRequest.org_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=98,
)


_FLOW = _descriptor.Descriptor(
  name='Flow',
  full_name='flow.Flow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='flow.Flow.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['FlowListRequest'] = _FLOWLISTREQUEST
DESCRIPTOR.message_types_by_name['Flow'] = _FLOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowListRequest = _reflection.GeneratedProtocolMessageType('FlowListRequest', (_message.Message,), {
  'DESCRIPTOR' : _FLOWLISTREQUEST,
  '__module__' : 'weni.flow_grpc.grpc_gen.flow_pb2'
  # @@protoc_insertion_point(class_scope:flow.FlowListRequest)
  })
_sym_db.RegisterMessage(FlowListRequest)

Flow = _reflection.GeneratedProtocolMessageType('Flow', (_message.Message,), {
  'DESCRIPTOR' : _FLOW,
  '__module__' : 'weni.flow_grpc.grpc_gen.flow_pb2'
  # @@protoc_insertion_point(class_scope:flow.Flow)
  })
_sym_db.RegisterMessage(Flow)



_FLOWCONTROLLER = _descriptor.ServiceDescriptor(
  name='FlowController',
  full_name='flow.FlowController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=136,
  serialized_end=199,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='flow.FlowController.List',
    index=0,
    containing_service=None,
    input_type=_FLOWLISTREQUEST,
    output_type=_FLOW,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FLOWCONTROLLER)

DESCRIPTOR.services_by_name['FlowController'] = _FLOWCONTROLLER

# @@protoc_insertion_point(module_scope)

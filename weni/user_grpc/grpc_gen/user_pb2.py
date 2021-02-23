# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/user_grpc/grpc_gen/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/user_grpc/grpc_gen/user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"weni/user_grpc/grpc_gen/user.proto\x12\x04user\"2\n\x0fUserListRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06org_id\x18\x02 \x01(\x05\" \n\nPermission\x12\x12\n\npermission\x18\x01 \x01(\t2E\n\x0eUserController\x12\x33\n\x04List\x12\x15.user.UserListRequest\x1a\x10.user.Permission\"\x00\x30\x01\x62\x06proto3'
)




_USERLISTREQUEST = _descriptor.Descriptor(
  name='UserListRequest',
  full_name='user.UserListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user.UserListRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_id', full_name='user.UserListRequest.org_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=94,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='user.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='permission', full_name='user.Permission.permission', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=96,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['UserListRequest'] = _USERLISTREQUEST
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListRequest = _reflection.GeneratedProtocolMessageType('UserListRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTREQUEST,
  '__module__' : 'weni.user_grpc.grpc_gen.user_pb2'
  # @@protoc_insertion_point(class_scope:user.UserListRequest)
  })
_sym_db.RegisterMessage(UserListRequest)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'weni.user_grpc.grpc_gen.user_pb2'
  # @@protoc_insertion_point(class_scope:user.Permission)
  })
_sym_db.RegisterMessage(Permission)



_USERCONTROLLER = _descriptor.ServiceDescriptor(
  name='UserController',
  full_name='user.UserController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=199,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='user.UserController.List',
    index=0,
    containing_service=None,
    input_type=_USERLISTREQUEST,
    output_type=_PERMISSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERCONTROLLER)

DESCRIPTOR.services_by_name['UserController'] = _USERCONTROLLER

# @@protoc_insertion_point(module_scope)
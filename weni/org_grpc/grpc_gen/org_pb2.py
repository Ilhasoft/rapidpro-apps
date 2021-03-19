# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/org_grpc/grpc_gen/org.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/org_grpc/grpc_gen/org.proto',
  package='weni.rapidpro.org',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n weni/org_grpc/grpc_gen/org.proto\x12\x11weni.rapidpro.org\x1a\x1bgoogle/protobuf/empty.proto\"|\n\x03Org\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x61te_format\x18\x05 \x01(\t\x12&\n\x05users\x18\x06 \x03(\x0b\x32\x17.weni.rapidpro.org.User\"Z\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\"$\n\x0eOrgListRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\"X\n\x10OrgCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08timezone\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\"\"\n\x12OrgRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"5\n\x11OrgDestroyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\"\xa4\x03\n\x10OrgUpdateRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\x12\x11\n\x04name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08timezone\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x61te_format\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04plan\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08plan_end\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05\x62rand\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\x14\n\x07is_anon\x18\t \x01(\x08H\x06\x88\x01\x01\x12\x1a\n\ris_multi_user\x18\n \x01(\x08H\x07\x88\x01\x01\x12\x19\n\x0cis_multi_org\x18\x0b \x01(\x08H\x08\x88\x01\x01\x12\x19\n\x0cis_suspended\x18\x0c \x01(\x08H\t\x88\x01\x01\x42\x07\n\x05_nameB\x0b\n\t_timezoneB\x0e\n\x0c_date_formatB\x07\n\x05_planB\x0b\n\t_plan_endB\x08\n\x06_brandB\n\n\x08_is_anonB\x10\n\x0e_is_multi_userB\x0f\n\r_is_multi_orgB\x0f\n\r_is_suspended2\x8d\x03\n\rOrgController\x12\x45\n\x04List\x12!.weni.rapidpro.org.OrgListRequest\x1a\x16.weni.rapidpro.org.Org\"\x00\x30\x01\x12G\n\x06\x43reate\x12#.weni.rapidpro.org.OrgCreateRequest\x1a\x16.weni.rapidpro.org.Org\"\x00\x12K\n\x08Retrieve\x12%.weni.rapidpro.org.OrgRetrieveRequest\x1a\x16.weni.rapidpro.org.Org\"\x00\x12T\n\x06Update\x12#.weni.rapidpro.org.OrgUpdateRequest\x1a#.weni.rapidpro.org.OrgUpdateRequest\"\x00\x12I\n\x07\x44\x65stroy\x12$.weni.rapidpro.org.OrgDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ORG = _descriptor.Descriptor(
  name='Org',
  full_name='weni.rapidpro.org.Org',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.rapidpro.org.Org.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.rapidpro.org.Org.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.rapidpro.org.Org.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='weni.rapidpro.org.Org.timezone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='weni.rapidpro.org.Org.date_format', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users', full_name='weni.rapidpro.org.Org.users', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=208,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='weni.rapidpro.org.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.rapidpro.org.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='weni.rapidpro.org.User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='weni.rapidpro.org.User.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='weni.rapidpro.org.User.first_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='weni.rapidpro.org.User.last_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=210,
  serialized_end=300,
)


_ORGLISTREQUEST = _descriptor.Descriptor(
  name='OrgListRequest',
  full_name='weni.rapidpro.org.OrgListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.rapidpro.org.OrgListRequest.user_email', index=0,
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
  serialized_start=302,
  serialized_end=338,
)


_ORGCREATEREQUEST = _descriptor.Descriptor(
  name='OrgCreateRequest',
  full_name='weni.rapidpro.org.OrgCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.rapidpro.org.OrgCreateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='weni.rapidpro.org.OrgCreateRequest.timezone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.rapidpro.org.OrgCreateRequest.user_email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='weni.rapidpro.org.OrgCreateRequest.username', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=340,
  serialized_end=428,
)


_ORGRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrgRetrieveRequest',
  full_name='weni.rapidpro.org.OrgRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.rapidpro.org.OrgRetrieveRequest.uuid', index=0,
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
  serialized_start=430,
  serialized_end=464,
)


_ORGDESTROYREQUEST = _descriptor.Descriptor(
  name='OrgDestroyRequest',
  full_name='weni.rapidpro.org.OrgDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.rapidpro.org.OrgDestroyRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.rapidpro.org.OrgDestroyRequest.user_email', index=1,
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
  serialized_start=466,
  serialized_end=519,
)


_ORGUPDATEREQUEST = _descriptor.Descriptor(
  name='OrgUpdateRequest',
  full_name='weni.rapidpro.org.OrgUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.rapidpro.org.OrgUpdateRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.rapidpro.org.OrgUpdateRequest.user_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.rapidpro.org.OrgUpdateRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='weni.rapidpro.org.OrgUpdateRequest.timezone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='weni.rapidpro.org.OrgUpdateRequest.date_format', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plan', full_name='weni.rapidpro.org.OrgUpdateRequest.plan', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plan_end', full_name='weni.rapidpro.org.OrgUpdateRequest.plan_end', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brand', full_name='weni.rapidpro.org.OrgUpdateRequest.brand', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_anon', full_name='weni.rapidpro.org.OrgUpdateRequest.is_anon', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_multi_user', full_name='weni.rapidpro.org.OrgUpdateRequest.is_multi_user', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_multi_org', full_name='weni.rapidpro.org.OrgUpdateRequest.is_multi_org', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_suspended', full_name='weni.rapidpro.org.OrgUpdateRequest.is_suspended', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='_name', full_name='weni.rapidpro.org.OrgUpdateRequest._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_timezone', full_name='weni.rapidpro.org.OrgUpdateRequest._timezone',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_date_format', full_name='weni.rapidpro.org.OrgUpdateRequest._date_format',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_plan', full_name='weni.rapidpro.org.OrgUpdateRequest._plan',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_plan_end', full_name='weni.rapidpro.org.OrgUpdateRequest._plan_end',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_brand', full_name='weni.rapidpro.org.OrgUpdateRequest._brand',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_is_anon', full_name='weni.rapidpro.org.OrgUpdateRequest._is_anon',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_is_multi_user', full_name='weni.rapidpro.org.OrgUpdateRequest._is_multi_user',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_is_multi_org', full_name='weni.rapidpro.org.OrgUpdateRequest._is_multi_org',
      index=8, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_is_suspended', full_name='weni.rapidpro.org.OrgUpdateRequest._is_suspended',
      index=9, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=522,
  serialized_end=942,
)

_ORG.fields_by_name['users'].message_type = _USER
_ORGUPDATEREQUEST.oneofs_by_name['_name'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['name'])
_ORGUPDATEREQUEST.fields_by_name['name'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_name']
_ORGUPDATEREQUEST.oneofs_by_name['_timezone'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['timezone'])
_ORGUPDATEREQUEST.fields_by_name['timezone'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_timezone']
_ORGUPDATEREQUEST.oneofs_by_name['_date_format'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['date_format'])
_ORGUPDATEREQUEST.fields_by_name['date_format'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_date_format']
_ORGUPDATEREQUEST.oneofs_by_name['_plan'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['plan'])
_ORGUPDATEREQUEST.fields_by_name['plan'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_plan']
_ORGUPDATEREQUEST.oneofs_by_name['_plan_end'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['plan_end'])
_ORGUPDATEREQUEST.fields_by_name['plan_end'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_plan_end']
_ORGUPDATEREQUEST.oneofs_by_name['_brand'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['brand'])
_ORGUPDATEREQUEST.fields_by_name['brand'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_brand']
_ORGUPDATEREQUEST.oneofs_by_name['_is_anon'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['is_anon'])
_ORGUPDATEREQUEST.fields_by_name['is_anon'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_is_anon']
_ORGUPDATEREQUEST.oneofs_by_name['_is_multi_user'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['is_multi_user'])
_ORGUPDATEREQUEST.fields_by_name['is_multi_user'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_is_multi_user']
_ORGUPDATEREQUEST.oneofs_by_name['_is_multi_org'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['is_multi_org'])
_ORGUPDATEREQUEST.fields_by_name['is_multi_org'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_is_multi_org']
_ORGUPDATEREQUEST.oneofs_by_name['_is_suspended'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['is_suspended'])
_ORGUPDATEREQUEST.fields_by_name['is_suspended'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_is_suspended']
DESCRIPTOR.message_types_by_name['Org'] = _ORG
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['OrgListRequest'] = _ORGLISTREQUEST
DESCRIPTOR.message_types_by_name['OrgCreateRequest'] = _ORGCREATEREQUEST
DESCRIPTOR.message_types_by_name['OrgRetrieveRequest'] = _ORGRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['OrgDestroyRequest'] = _ORGDESTROYREQUEST
DESCRIPTOR.message_types_by_name['OrgUpdateRequest'] = _ORGUPDATEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Org = _reflection.GeneratedProtocolMessageType('Org', (_message.Message,), {
  'DESCRIPTOR' : _ORG,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.Org)
  })
_sym_db.RegisterMessage(Org)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.User)
  })
_sym_db.RegisterMessage(User)

OrgListRequest = _reflection.GeneratedProtocolMessageType('OrgListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGLISTREQUEST,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.OrgListRequest)
  })
_sym_db.RegisterMessage(OrgListRequest)

OrgCreateRequest = _reflection.GeneratedProtocolMessageType('OrgCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGCREATEREQUEST,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.OrgCreateRequest)
  })
_sym_db.RegisterMessage(OrgCreateRequest)

OrgRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrgRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGRETRIEVEREQUEST,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.OrgRetrieveRequest)
  })
_sym_db.RegisterMessage(OrgRetrieveRequest)

OrgDestroyRequest = _reflection.GeneratedProtocolMessageType('OrgDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGDESTROYREQUEST,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.OrgDestroyRequest)
  })
_sym_db.RegisterMessage(OrgDestroyRequest)

OrgUpdateRequest = _reflection.GeneratedProtocolMessageType('OrgUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGUPDATEREQUEST,
  '__module__' : 'weni.org_grpc.grpc_gen.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.rapidpro.org.OrgUpdateRequest)
  })
_sym_db.RegisterMessage(OrgUpdateRequest)



_ORGCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrgController',
  full_name='weni.rapidpro.org.OrgController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=945,
  serialized_end=1342,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='weni.rapidpro.org.OrgController.List',
    index=0,
    containing_service=None,
    input_type=_ORGLISTREQUEST,
    output_type=_ORG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='weni.rapidpro.org.OrgController.Create',
    index=1,
    containing_service=None,
    input_type=_ORGCREATEREQUEST,
    output_type=_ORG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.rapidpro.org.OrgController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_ORGRETRIEVEREQUEST,
    output_type=_ORG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='weni.rapidpro.org.OrgController.Update',
    index=3,
    containing_service=None,
    input_type=_ORGUPDATEREQUEST,
    output_type=_ORGUPDATEREQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='weni.rapidpro.org.OrgController.Destroy',
    index=4,
    containing_service=None,
    input_type=_ORGDESTROYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGCONTROLLER)

DESCRIPTOR.services_by_name['OrgController'] = _ORGCONTROLLER

# @@protoc_insertion_point(module_scope)

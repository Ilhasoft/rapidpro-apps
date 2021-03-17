# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/billing/grpc_gen/billing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/billing/grpc_gen/billing.proto',
  package='billing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#weni/billing/grpc_gen/billing.proto\x12\x07\x62illing\x1a\x1fgoogle/protobuf/timestamp.proto\"y\n\x0e\x42illingRequest\x12\x10\n\x08org_uuid\x18\x01 \x01(\t\x12*\n\x06\x62\x65\x66ore\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x05\x61\x66ter\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"*\n\x0f\x42illingResponse\x12\x17\n\x0f\x61\x63tive_contacts\x18\x01 \x01(\x05\"u\n\x03Msg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12+\n\x07sent_on\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\tdirection\x18\x04 \x01(\x0e\x32\x12.billing.Direction\"%\n\x07\x43hannel\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"o\n\x13\x41\x63tiveContactDetail\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x03msg\x18\x03 \x01(\x0b\x32\x0c.billing.Msg\x12!\n\x07\x63hannel\x18\x04 \x01(\x0b\x32\x10.billing.Channel*\"\n\tDirection\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x32\x8e\x01\n\x07\x42illing\x12<\n\x05Total\x12\x17.billing.BillingRequest\x1a\x18.billing.BillingResponse\"\x00\x12\x45\n\x08\x44\x65tailed\x12\x17.billing.BillingRequest\x1a\x1c.billing.ActiveContactDetail\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='billing.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=519,
  serialized_end=553,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
INPUT = 0
OUTPUT = 1



_BILLINGREQUEST = _descriptor.Descriptor(
  name='BillingRequest',
  full_name='billing.BillingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='billing.BillingRequest.org_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='billing.BillingRequest.before', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='billing.BillingRequest.after', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=81,
  serialized_end=202,
)


_BILLINGRESPONSE = _descriptor.Descriptor(
  name='BillingResponse',
  full_name='billing.BillingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_contacts', full_name='billing.BillingResponse.active_contacts', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=204,
  serialized_end=246,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='billing.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='billing.Msg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='billing.Msg.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_on', full_name='billing.Msg.sent_on', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='billing.Msg.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=248,
  serialized_end=365,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='billing.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='billing.Channel.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='billing.Channel.name', index=1,
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
  serialized_start=367,
  serialized_end=404,
)


_ACTIVECONTACTDETAIL = _descriptor.Descriptor(
  name='ActiveContactDetail',
  full_name='billing.ActiveContactDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='billing.ActiveContactDetail.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='billing.ActiveContactDetail.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='billing.ActiveContactDetail.msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='billing.ActiveContactDetail.channel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=406,
  serialized_end=517,
)

_BILLINGREQUEST.fields_by_name['before'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BILLINGREQUEST.fields_by_name['after'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MSG.fields_by_name['sent_on'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MSG.fields_by_name['direction'].enum_type = _DIRECTION
_ACTIVECONTACTDETAIL.fields_by_name['msg'].message_type = _MSG
_ACTIVECONTACTDETAIL.fields_by_name['channel'].message_type = _CHANNEL
DESCRIPTOR.message_types_by_name['BillingRequest'] = _BILLINGREQUEST
DESCRIPTOR.message_types_by_name['BillingResponse'] = _BILLINGRESPONSE
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['ActiveContactDetail'] = _ACTIVECONTACTDETAIL
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingRequest = _reflection.GeneratedProtocolMessageType('BillingRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGREQUEST,
  '__module__' : 'weni.billing.grpc_gen.billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.BillingRequest)
  })
_sym_db.RegisterMessage(BillingRequest)

BillingResponse = _reflection.GeneratedProtocolMessageType('BillingResponse', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGRESPONSE,
  '__module__' : 'weni.billing.grpc_gen.billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.BillingResponse)
  })
_sym_db.RegisterMessage(BillingResponse)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'weni.billing.grpc_gen.billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.Msg)
  })
_sym_db.RegisterMessage(Msg)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'weni.billing.grpc_gen.billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.Channel)
  })
_sym_db.RegisterMessage(Channel)

ActiveContactDetail = _reflection.GeneratedProtocolMessageType('ActiveContactDetail', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVECONTACTDETAIL,
  '__module__' : 'weni.billing.grpc_gen.billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ActiveContactDetail)
  })
_sym_db.RegisterMessage(ActiveContactDetail)



_BILLING = _descriptor.ServiceDescriptor(
  name='Billing',
  full_name='billing.Billing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=556,
  serialized_end=698,
  methods=[
  _descriptor.MethodDescriptor(
    name='Total',
    full_name='billing.Billing.Total',
    index=0,
    containing_service=None,
    input_type=_BILLINGREQUEST,
    output_type=_BILLINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Detailed',
    full_name='billing.Billing.Detailed',
    index=1,
    containing_service=None,
    input_type=_BILLINGREQUEST,
    output_type=_ACTIVECONTACTDETAIL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLING)

DESCRIPTOR.services_by_name['Billing'] = _BILLING

# @@protoc_insertion_point(module_scope)
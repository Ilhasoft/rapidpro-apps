# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='billing.proto',
  package='billing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbilling.proto\x12\x07\x62illing\"<\n\x0e\x42illingRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\")\n\x0f\x42illingResponse\x12\x16\n\x0e\x61\x63tiveContacts\x18\x01 \x01(\x05\x32I\n\x07\x42illing\x12>\n\x07Summary\x12\x17.billing.BillingRequest\x1a\x18.billing.BillingResponse\"\x00\x62\x06proto3'
)




_BILLINGREQUEST = _descriptor.Descriptor(
  name='BillingRequest',
  full_name='billing.BillingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='billing.BillingRequest.org', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='billing.BillingRequest.before', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='billing.BillingRequest.after', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=86,
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
      name='activeContacts', full_name='billing.BillingResponse.activeContacts', index=0,
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
  serialized_start=88,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['BillingRequest'] = _BILLINGREQUEST
DESCRIPTOR.message_types_by_name['BillingResponse'] = _BILLINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingRequest = _reflection.GeneratedProtocolMessageType('BillingRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGREQUEST,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.BillingRequest)
  })
_sym_db.RegisterMessage(BillingRequest)

BillingResponse = _reflection.GeneratedProtocolMessageType('BillingResponse', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGRESPONSE,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.BillingResponse)
  })
_sym_db.RegisterMessage(BillingResponse)



_BILLING = _descriptor.ServiceDescriptor(
  name='Billing',
  full_name='billing.Billing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=131,
  serialized_end=204,
  methods=[
  _descriptor.MethodDescriptor(
    name='Summary',
    full_name='billing.Billing.Summary',
    index=0,
    containing_service=None,
    input_type=_BILLINGREQUEST,
    output_type=_BILLINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLING)

DESCRIPTOR.services_by_name['Billing'] = _BILLING

# @@protoc_insertion_point(module_scope)

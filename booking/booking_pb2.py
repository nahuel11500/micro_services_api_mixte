# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x1a\x1bgoogle/protobuf/empty.proto\"7\n\x0b\x42ookingUser\x12\x18\n\x05\x64\x61tes\x18\x01 \x03(\x0b\x32\t.DateItem\x12\x0e\n\x06userid\x18\x02 \x01(\t\"\x18\n\x06userid\x12\x0e\n\x06userid\x18\x01 \x01(\t\"(\n\x08\x44\x61teItem\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"?\n\x0e\x42ookingRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07movieid\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x03 \x01(\t\"!\n\x0eSuccessMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\xa5\x01\n\x07\x42ooking\x12\x35\n\x0bGetBookings\x12\x16.google.protobuf.Empty\x1a\x0c.BookingUser0\x01\x12+\n\x12getBookingByUserId\x12\x07.userid\x1a\x0c.BookingUser\x12\x36\n\x12\x41\x64\x64NewMovieBooking\x12\x0f.BookingRequest\x1a\x0f.SuccessMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BOOKINGUSER']._serialized_start=46
  _globals['_BOOKINGUSER']._serialized_end=101
  _globals['_USERID']._serialized_start=103
  _globals['_USERID']._serialized_end=127
  _globals['_DATEITEM']._serialized_start=129
  _globals['_DATEITEM']._serialized_end=169
  _globals['_BOOKINGREQUEST']._serialized_start=171
  _globals['_BOOKINGREQUEST']._serialized_end=234
  _globals['_SUCCESSMESSAGE']._serialized_start=236
  _globals['_SUCCESSMESSAGE']._serialized_end=269
  _globals['_BOOKING']._serialized_start=272
  _globals['_BOOKING']._serialized_end=437
# @@protoc_insertion_point(module_scope)
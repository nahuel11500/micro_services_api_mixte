# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x1a\n\nMovie_Date\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\'\n\x08Schedule\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2_\n\x08Showtime\x12\'\n\x0egetMoviesTimes\x12\x06.Empty\x1a\t.Schedule\"\x00\x30\x01\x12*\n\x0egetMovieByDate\x12\x0b.Movie_Date\x1a\t.Schedule\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MOVIE_DATE']._serialized_start=18
  _globals['_MOVIE_DATE']._serialized_end=44
  _globals['_SCHEDULE']._serialized_start=46
  _globals['_SCHEDULE']._serialized_end=85
  _globals['_EMPTY']._serialized_start=87
  _globals['_EMPTY']._serialized_end=94
  _globals['_SHOWTIME']._serialized_start=96
  _globals['_SHOWTIME']._serialized_end=191
# @@protoc_insertion_point(module_scope)

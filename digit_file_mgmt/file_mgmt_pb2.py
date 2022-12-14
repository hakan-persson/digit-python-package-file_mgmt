# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: digit_file_mgmt/file_mgmt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x64igit_file_mgmt/file_mgmt.proto\"R\n\x10ListFilesRequest\x12\x0e\n\x06siteId\x18\x01 \x01(\t\x12\x0f\n\x07\x64riveId\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0f\n\x07pattern\x18\x04 \x01(\t\"\x1f\n\x0eListFilesReply\x12\r\n\x05\x66iles\x18\x01 \x01(\t\"b\n\x0fReadFileRequest\x12\x0e\n\x06siteId\x18\x01 \x01(\t\x12\x0f\n\x07\x64riveId\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x10\n\x08\x66ileName\x18\x04 \x01(\t\x12\x0e\n\x06\x66ileId\x18\x05 \x01(\t\".\n\rReadFileReply\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x32m\n\x08\x46ileMgmt\x12\x31\n\tListFiles\x12\x11.ListFilesRequest\x1a\x0f.ListFilesReply\"\x00\x12.\n\x08ReadFile\x12\x10.ReadFileRequest\x1a\x0e.ReadFileReply\"\x00\x62\x06proto3')



_LISTFILESREQUEST = DESCRIPTOR.message_types_by_name['ListFilesRequest']
_LISTFILESREPLY = DESCRIPTOR.message_types_by_name['ListFilesReply']
_READFILEREQUEST = DESCRIPTOR.message_types_by_name['ReadFileRequest']
_READFILEREPLY = DESCRIPTOR.message_types_by_name['ReadFileReply']
ListFilesRequest = _reflection.GeneratedProtocolMessageType('ListFilesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESREQUEST,
  '__module__' : 'digit_file_mgmt.file_mgmt_pb2'
  # @@protoc_insertion_point(class_scope:ListFilesRequest)
  })
_sym_db.RegisterMessage(ListFilesRequest)

ListFilesReply = _reflection.GeneratedProtocolMessageType('ListFilesReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTFILESREPLY,
  '__module__' : 'digit_file_mgmt.file_mgmt_pb2'
  # @@protoc_insertion_point(class_scope:ListFilesReply)
  })
_sym_db.RegisterMessage(ListFilesReply)

ReadFileRequest = _reflection.GeneratedProtocolMessageType('ReadFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _READFILEREQUEST,
  '__module__' : 'digit_file_mgmt.file_mgmt_pb2'
  # @@protoc_insertion_point(class_scope:ReadFileRequest)
  })
_sym_db.RegisterMessage(ReadFileRequest)

ReadFileReply = _reflection.GeneratedProtocolMessageType('ReadFileReply', (_message.Message,), {
  'DESCRIPTOR' : _READFILEREPLY,
  '__module__' : 'digit_file_mgmt.file_mgmt_pb2'
  # @@protoc_insertion_point(class_scope:ReadFileReply)
  })
_sym_db.RegisterMessage(ReadFileReply)

_FILEMGMT = DESCRIPTOR.services_by_name['FileMgmt']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LISTFILESREQUEST._serialized_start=35
  _LISTFILESREQUEST._serialized_end=117
  _LISTFILESREPLY._serialized_start=119
  _LISTFILESREPLY._serialized_end=150
  _READFILEREQUEST._serialized_start=152
  _READFILEREQUEST._serialized_end=250
  _READFILEREPLY._serialized_start=252
  _READFILEREPLY._serialized_end=298
  _FILEMGMT._serialized_start=300
  _FILEMGMT._serialized_end=409
# @@protoc_insertion_point(module_scope)

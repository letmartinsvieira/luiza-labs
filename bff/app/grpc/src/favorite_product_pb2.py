# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: favorite_product.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'favorite_product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66\x61vorite_product.proto\x12\x10product_favorite\"E\n\x1c\x43reateFavoriteProductRequest\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\x05\"<\n\x1d\x43reateFavoriteProductResponse\x12\x1b\n\x13\x66\x61vorite_product_id\x18\x01 \x01(\x05\"L\n\x1aListFavoriteProductRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\x05\"P\n\x15\x46\x61voriteProductObject\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\r\n\x05image\x18\x05 \x01(\t\"X\n\x1bListFavoriteProductResponse\x12\x39\n\x08products\x18\x01 \x01(\x0b\x32\'.product_favorite.FavoriteProductObject2\x83\x02\n\x0f\x46\x61voriteProduct\x12z\n\x15\x43reateFavoriteProduct\x12..product_favorite.CreateFavoriteProductRequest\x1a/.product_favorite.CreateFavoriteProductResponse\"\x00\x12t\n\x13ListFavoriteProduct\x12,.product_favorite.ListFavoriteProductRequest\x1a-.product_favorite.ListFavoriteProductResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'favorite_product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEFAVORITEPRODUCTREQUEST']._serialized_start=44
  _globals['_CREATEFAVORITEPRODUCTREQUEST']._serialized_end=113
  _globals['_CREATEFAVORITEPRODUCTRESPONSE']._serialized_start=115
  _globals['_CREATEFAVORITEPRODUCTRESPONSE']._serialized_end=175
  _globals['_LISTFAVORITEPRODUCTREQUEST']._serialized_start=177
  _globals['_LISTFAVORITEPRODUCTREQUEST']._serialized_end=253
  _globals['_FAVORITEPRODUCTOBJECT']._serialized_start=255
  _globals['_FAVORITEPRODUCTOBJECT']._serialized_end=335
  _globals['_LISTFAVORITEPRODUCTRESPONSE']._serialized_start=337
  _globals['_LISTFAVORITEPRODUCTRESPONSE']._serialized_end=425
  _globals['_FAVORITEPRODUCT']._serialized_start=428
  _globals['_FAVORITEPRODUCT']._serialized_end=687
# @@protoc_insertion_point(module_scope)

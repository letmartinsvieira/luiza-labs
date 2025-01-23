from typing import Dict

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message
from google.protobuf.timestamp_pb2 import Timestamp

from datetime import datetime

def proto_dt_to_datetime(pb_time: Timestamp) -> datetime:
    if pb_time is None:
        return None
    
    return pb_time.ToDatetime()

def date_time_to_proto_dt(dt: datetime) -> Timestamp:
    if dt is None:
        return None
    
    pb_time = Timestamp()
    return pb_time.FromDatetime(dt)

def load_to_dict(proto_object: Message) -> Dict:
    dict_data = MessageToDict(
        proto_object,
        preserving_proto_field_name=True
    )

    for field, value in proto_object.ListFields():
        if field.type == FieldDescriptor.TYPE_MESSAGE and \
            field.message_type is not None and \
            field.message_type.full_name == 'google.protobuf.Timestamp':

            field_value = getattr(proto_object, field.name)
            dict_data[field.name] = proto_dt_to_datetime(field_value)

    return dict_data


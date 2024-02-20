#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""


import uuid
import datetime


class BaseModel:
    def __init__(self):
        id = uuid.uuid4()
        self.id = str(id)
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

obj = BaseModel()
print(obj.id)
print(obj.created_at)
print(obj.updated_at)
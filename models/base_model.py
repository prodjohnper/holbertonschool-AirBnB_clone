#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""


import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

# obj = BaseModel()
# print(obj.id)
# print(obj.created_at)
# print(obj.updated_at)
# print(obj)
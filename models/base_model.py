#!/usr/bin/python3
'''
    base_model.py

    Class BaseModel that defines common attributes/methods for other classes
'''


import uuid
import datetime
from models import storage


class BaseModel:
    '''
        Defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
            Initialize new instance
        '''
        date_format = '%Y-%m-%dT%H:%M:%S.%f'

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = self.created_at

        if kwargs:
            kwargs.pop('__class__', None)  # Remove __class__ from kwargs
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime(
                        value, date_format))  # Convert string to datetime obj
                else:
                    setattr(self, key, value)
        else:
            storage.new(self)

    def save(self):
        '''
            Update timestamp to the current date and time
        '''
        self.updated_at = datetime.datetime.today()
        storage.save()

    def __str__(self):
        '''
            Returns string representation
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        '''
            Returns dictionary representation
        '''
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__  # Add class name to dict

        return my_dict

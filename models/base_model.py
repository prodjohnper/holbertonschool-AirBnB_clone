#!/usr/bin/python3
'''
    base_model.py

    Class BaseModel that defines common attributes/methods for other classes
'''


import uuid
import datetime


class BaseModel:
    '''
        Defines all common attributes/methods for other classes
    '''

    def __init__(self):
        '''
            Initialize new instance
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''
            Update timestamp to the current date and time
        '''
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''
            Returns string representation
        '''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        '''
            Returns dictionary representation
        '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        
        return my_dict

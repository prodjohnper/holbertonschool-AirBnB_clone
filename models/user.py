#!/usr/bin/python3
"""comment"""


from models.base_model import BaseModel


class User(BaseModel):
    '''
        User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        '''
            String representation of User object
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.email)

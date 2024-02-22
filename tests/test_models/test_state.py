#!/usr/bin/python3
'''
    test_state.py
    
    Unittest
'''
import unittest
from models.state import State


class test_state(unittest.TestCase):
    '''
        Class State Unittest
    '''

    def test_state_attr(self):
        '''
            Class State test cases
        '''
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()

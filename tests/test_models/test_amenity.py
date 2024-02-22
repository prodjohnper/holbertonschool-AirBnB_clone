#!/usr/bin/python3
'''
    test_amenity.py

    Unittest for class Amenity
'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
        Class Amenity unittest
    '''

    def test_amenity_attributes(self):
        '''
            Class Amenity test cases'''
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()

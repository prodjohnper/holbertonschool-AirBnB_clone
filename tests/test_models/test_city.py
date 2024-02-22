#!/usr/bin/python3
'''
    test_city.py
    
    Unittest for class City
'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''
        Class City Unittest
    '''

    def test_city_attr(self):
        '''
            Class City test cases
        '''
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()

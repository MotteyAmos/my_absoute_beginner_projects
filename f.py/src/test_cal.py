import unittest

import index
from index import *

'''
class TestCal(unittest.TestCase):
    def test_add(self):
        self.assertEqual(index.add(1, 1), 2)
        self.assertEqual(index.add(-1, 1), 0)
        self.assertEqual(index.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(index.subtract(2, 1), 1)
        self.assertEqual(index.subtract(-2, 1), -3)
        self.assertEqual(index.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(index.multiple(1, 2), 2)
        self.assertEqual(index.multiple(-2, -2), 4)
        self.assertEqual(index.multiple(-2, 1), -2)

    def test_divides(self):
        self.assertEqual(index.divide(4, 2), 2)
        self.assertEqual(index.divide(-4, 2), -2)
        self.assertEqual(index.divide(-4, -2), 2)

'''

class Employee(unittest.TestCase):
    emply_1 = index.Employee('router', 'sky', 1000)
    emply_2 = index.Employee("maka", 'green', 2000, 1000)

    def test_default_raise(self):
        self.assertEqual(self.emply_1.default_raise(), 6000)
        self.assertEqual(self.emply_2.default_raise(), 7000)

    def test_individual_income_raise(self):
        self.assertEqual(self.emply_1.custom_raise(), 'sky router salary current salary is {}'.format(6000))
        self.assertEqual(self.emply_2.custom_raise(), 'green maka salary current salary is {}'.format(8000))



if __name__ == "__main__":
    unittest.main()










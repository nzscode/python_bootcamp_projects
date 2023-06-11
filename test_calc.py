import unittest
from unittest import TestCase

import calc


# class TestCalc(unittest.TestCase):
#
#     def test_add(self):
#         result = calc.add(10, 5)
#         self.assertEqual(result, 15)


class TestMultiply(TestCase):
    def test_multiply(self):
        self.assertEqual(calc.multiply(0, 1), 0)
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.multiply(3, 2), 6)
        self.assertEqual(calc.multiply(-4, 8), -32)
        self.assertEqual(calc.multiply(-9, -2), 18)
        self.assertEqual(calc.multiply(7, 1), 7)

class TestAdd(TestCase):
    def test_add(self):
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(0, 5), 5)
        self.assertEqual(calc.add(2, 6), 8)
        self.assertEqual(calc.add(10, 20), 30)
        self.assertEqual(calc.add(-1, 0), -1)
        self.assertEqual(calc.add(-9, 3), -6)
        self.assertEqual(calc.add(-5, -2), -7)
        self.assertEqual(calc.add(-4, 13), 9)

class TestDivide(TestCase):
    def test_divide(self):
        self.assertEqual(calc.divide(0, 1), 0)
        self.assertEqual(calc.divide(5, 10), 0.5)
        self.assertEqual(calc.divide(12, 2), 6)
        self.assertEqual(calc.divide(-16, 8), -2)
        self.assertEqual(calc.divide(-9, -3), 3)
        self.assertEqual(calc.divide(-4, 2), -2)
        self.assertEqual(calc.divide(15, 2), 7.5)


class TestSubtract(TestCase):
    def test_subtract(self):
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(0, 5), -5)
        self.assertEqual(calc.subtract(2, 6), -4)
        self.assertEqual(calc.subtract(10, 20), -10)
        self.assertEqual(calc.subtract(-1, 0), -1)
        self.assertEqual(calc.subtract(-9, 3), -12)
        self.assertEqual(calc.subtract(-5, -2), -3)
        self.assertEqual(calc.subtract(-4, 13), -17)
        self.assertEqual(calc.subtract(12, -5), 17)
        self.assertEqual(calc.subtract(4, -15), 19)


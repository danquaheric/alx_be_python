# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test with positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test with negative + positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zeros
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_subtraction(self):
        # positive result
        self.assertEqual(self.calc.subtract(10, 3), 7)
        # negative result
        self.assertEqual(self.calc.subtract(3, 10), -7)
        # subtract zeros
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # mix negative and positive
        self.assertEqual(self.calc.subtract(-4, 5), -9)

    def test_multiplication(self):
        # positive * positive
        self.assertEqual(self.calc.multiply(4, 5), 20)
        # positive * zero
        self.assertEqual(self.calc.multiply(7, 0), 0)
        # negative * positive
        self.assertEqual(self.calc.multiply(-3, 6), -18)
        # negative * negative
        self.assertEqual(self.calc.multiply(-2, -8), 16)

    def test_division_normal(self):
        # integer division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # float result
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # negative / positive
        self.assertEqual(self.calc.divide(-8, 2), -4)
        # positive / negative
        self.assertEqual(self.calc.divide(8, -2), -4)
        # negative / negative
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_division_by_zero(self):
        # dividing by zero should return None according to the class definition
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    # Optional / additional tests
    def test_division_non_integer(self):
        # test with floats
        self.assertAlmostEqual(self.calc.divide(5.5, 2.0), 2.75)
        self.assertAlmostEqual(self.calc.divide(-5.5, 2.2), -2.5)

if __name__ == '__main__':
    unittest.main()

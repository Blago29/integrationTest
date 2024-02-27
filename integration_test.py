# integration_test.py
import unittest
from calculator import multiply
from validator import validate_arguments

class TestCalculatorIntegration(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            validate_arguments('a', 3)
            validate_arguments(2, 'b')
            validate_arguments('x', 'y')

    def test_multiply_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            validate_arguments('a', 3)
            multiply('a', 3)

    def test_multiply_integration(self):
        validate_arguments(2, 3)
        result = multiply(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

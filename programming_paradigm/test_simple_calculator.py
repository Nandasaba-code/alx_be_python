#Test the SimpleCalculator class to ensure all arithmetic operations work correctly.

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """
        This method runs before each test.
        We create a fresh SimpleCalculator instance each time.
        """
        self.calc = SimpleCalculator()

    # 🔹 Test addition
    def test_addition(self):
        """Test adding two numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)       # normal case
        self.assertEqual(self.calc.add(-1, 1), 0)      # negative + positive
        self.assertEqual(self.calc.add(-2, -3), -5)    # two negatives

    # 🔹 Test subtraction
    def test_subtraction(self):
        """Test subtracting two numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # normal case
        self.assertEqual(self.calc.subtract(3, 5), -2) # result is negative
        self.assertEqual(self.calc.subtract(-2, -3), 1) # negatives

    # 🔹 Test multiplication
    def test_multiplication(self):
        """Test multiplying two numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20) # normal
        self.assertEqual(self.calc.multiply(-2, 3), -6) # negative * positive
        self.assertEqual(self.calc.multiply(0, 100), 0) # anything times zero

    # 🔹 Test division
    def test_division(self):
        """Test dividing two numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)    # normal
        self.assertEqual(self.calc.divide(-9, 3), -3)   # negative / positive
        self.assertEqual(self.calc.divide(0, 5), 0)     # zero divided by number
        self.assertIsNone(self.calc.divide(5, 0))       # division by zero case

if __name__ == "__main__":
    unittest.main()

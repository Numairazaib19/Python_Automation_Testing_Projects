# Importing the unittest module, which provides a testing framework.
import unittest

# The Calculator class with basic arithmetic operations
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

# Test cases
# Creating a test case class that inherits from unittest.TestCase.
class TestCalculator(unittest.TestCase):
    
    # A setUp method that is executed before each test method.
    # It creates an instance of the Calculator class for testing.
    def setUp(self):
        self.calculator = Calculator()
        
    # Test cases for the 'add' method.
    def test_add(self):
        # Asserting that the add method returns the correct results for different inputs.
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(0, 0), 0)
        self.assertEqual(self.calculator.add(-5, 5), 0)
    
    # Test cases for the 'subtract' method.
    def test_subtract(self):
        # Asserting that the subtract method returns the correct results for different inputs.
        self.assertEqual(self.calculator.subtract(5, 2), 3)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
        self.assertEqual(self.calculator.subtract(5, 5), 0)

    # Test cases for the 'multiply' method.
    def test_multiply(self):
        # Asserting that the multiply method returns the correct results for different inputs.
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)
        self.assertEqual(self.calculator.multiply(-2, 4), -8)

    # Test cases for the 'divide' method.
    def test_divide(self):
        # Asserting that the divide method returns the correct results for different inputs.
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.divide(-8, 4), -2)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

# This block checks if the current script is the main module (i.e., not imported).
# If it is the main module, it runs the tests defined in the TestCalculator class.
if __name__ == "__main__":
    unittest.main()





    

    
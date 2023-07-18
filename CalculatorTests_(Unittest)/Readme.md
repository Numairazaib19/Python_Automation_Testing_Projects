
# Calculator Test Suite

This repository contains a Python class, `Calculator`, that provides basic arithmetic operations such as addition, subtraction, multiplication, and division. The code also includes a set of unit tests using the `unittest` framework to ensure the correctness of these arithmetic methods.

## Getting Started

Follow the instructions below to set up and run the unit tests for the `Calculator` class.

### Prerequisites

- Python 3.x (tested with Python 3.7)
- pip install unittest2
  
## Calculator Class

The `Calculator` class provides the following basic arithmetic methods:

- `add(a, b)`: Returns the sum of two numbers, `a` and `b`.
- `subtract(a, b)`: Returns the result of subtracting `b` from `a`.
- `multiply(a, b)`: Returns the product of two numbers, `a` and `b`.
- `divide(a, b)`: Returns the result of dividing `a` by `b`. If `b` is zero, a `ValueError` will be raised.

## Test Cases

The test cases are defined in the `TestCalculator` class, which inherits from `unittest.TestCase`. Each test method verifies the correctness of one of the `Calculator` class methods.

**Note**: The `Calculator` class and the test cases provided in this repository may not cover all edge cases. In a real-world scenario.

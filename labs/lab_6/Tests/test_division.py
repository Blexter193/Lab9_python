import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestDivision(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_positive_negative(self):
        self.assertEqual(divide(-6, 3), -2)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
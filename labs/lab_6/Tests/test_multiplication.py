import unittest

def multiply(a, b):
    return a * b

class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_positive_negative(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
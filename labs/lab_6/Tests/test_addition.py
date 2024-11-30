import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_positive_negative(self):
        self.assertEqual(add(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
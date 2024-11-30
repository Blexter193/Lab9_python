import unittest

def subtract(a, b):
    return a - b

class TestSubtraction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_zero(self):
        self.assertEqual(subtract(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
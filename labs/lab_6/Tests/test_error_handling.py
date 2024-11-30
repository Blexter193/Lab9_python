import unittest
from labs.lab_6.Tests.test_division import divide
from labs.lab_6.Tests.test_addition import add

class TestErrorHandling(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add("a", 5)

if __name__ == '__main__':
    unittest.main()

import unittest
from main import add_numbers

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(5, 7)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()

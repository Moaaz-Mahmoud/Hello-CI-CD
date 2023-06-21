import unittest
from main import add_numbers


class TestMain(unittest.TestCase):
    def test_add_numbers_c1(self):
        result = add_numbers(5, 7)
        self.assertEqual(result, 12)
        
    def test_add_numbers_c2(self):
    	result = add_numbers(8, 2)
    	self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()

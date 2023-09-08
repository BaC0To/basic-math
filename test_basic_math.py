import unittest
from basic_math_functions import BasicMath


class TestBasicMath(unittest.TestCase):
    
    def setUp(self):
        self.basic_math = BasicMath()

    def tearDown(self):
        del self.basic_math
        
    def test_add_two_positive_numbers(self):
        expected = 4
        result = self.basic_math.add(2, 2)
        self.assertEqual(expected,result)
       
    def test_add_two_negative_numbers(self):
        expected = -4
        result = self.basic_math.add(-2, -2)
        assert result == expected

    def test_add_negative_and_positive_numbers(self):
        expected = 0
        result = self.basic_math.add(-2, 2)
        assert result == expected

    def test_add_positive_and_negative_numbers(self):
        expected = 0
        result = self.basic_math.add(2, -2)
        assert result == expected

    def test_subtract_two_positive_numbers(self):
        expected = 0
        result = self.basic_math.subtract(2, 2)
        assert result == expected

    def test_subtract_two_negative_numbers(self):
        expected = 0
        result = self.basic_math.subtract(-2, -2)
        assert result == expected

    def test_subtract_positive_and_negative_numbers(self):
        expected = 7
        result = self.basic_math.subtract(5, -2)
        assert result == expected

if __name__ == "__main__":
    unittest.main()

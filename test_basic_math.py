import unittest
#from basic_math_functions import BasicMath
from basic_math_functions import *

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

# sum function end

    def test_subtract_two_positive_numbers(self):
        expected = 1
        result = self.basic_math.subtract(3, 2)
        assert result == expected

    def test_subtract_two_negative_numbers(self):
        expected = 1
        result = self.basic_math.subtract(-2, -3)
        assert result == expected

    def test_subtract_positive_and_negative_numbers(self):
        expected = 6
        result = self.basic_math.subtract(5, -1)
        assert result == expected

    def test_subtract_and_negative_positive_numbers(self):
        expected = -6
        result = self.basic_math.subtract(-5, 1)
        assert result == expected

# subtract function end

    def test_multiply_two_positive_numebrs(self):
        expected = 6
        result = self.basic_math.multiply(2, 3)
        assert result == expected

    def test_multiply_two_negative_numebrs(self):
        expected = 200
        result = self.basic_math.multiply(-10, -20)
        assert result == expected

    def test_multiply_positive_negative_numebrs(self):
        expected = -8
        result = self.basic_math.multiply(2, -4)
        assert result == expected

    def test_multiply_negative_positive_numebrs(self):
        expected = -36
        result = self.basic_math.multiply(-12, 3)
        assert result == expected
    
# multiply function end

    def test_divide_two_positive_numebrs(self):
        expected = 5
        result = self.basic_math.divide(10, 2)
        assert result == expected

    def test_divide_two_negative_numebrs(self):
        expected = 5
        result = self.basic_math.divide(-10, -2)
        assert result == expected

    def test_divide_negative_positive_numebrs(self):
        expected = -5
        result = self.basic_math.divide(-10, 2)
        assert result == expected

    def test_divide_positive_negative_numebrs(self):
        expected = -5
        result = self.basic_math.divide(10, -2)
        assert result == expected

    def test_divide_by_zero(self):
        #self.assertRaises(ValueError, self.basic_math.divide, 2, 2)
            with self.assertRaises(ValueError):
                self.basic_math.divide(10, 0) #contacs manager

                          
# divide function end

if __name__ == "__main__":
    unittest.main()

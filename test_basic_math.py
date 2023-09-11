import unittest
#from basic_math_functions import BasicMath
from basic_math_functions import *


class TestBasicMath(unittest.TestCase):


    def setUp(self):
        #print("\nsetUp")
        self.basic_math = BasicMath() # "self" creates an instance of the class BasicMath() before every test
        
    def tearDown(self):
        #print("tearDown\n")
        del self.basic_math

    def test_add_two_positive_numbers(self):
        #print("test_add_two_positive_numbers")
        expected = 3.26
        result = self.basic_math.add([3.14, 0.12])
        self.assertAlmostEqual(result, expected)

    def test_add_two_negative_numbers(self):
        expected = -4
        result = self.basic_math.add([-2, -2])
        self.assertEqual(result, expected)

    def test_add_negative_and_positive_numbers(self):
        expected = 0
        result = self.basic_math.add([-2, 2])
        self.assertEqual(result, expected)

    def test_add_positive_and_negative_numbers(self):
        expected = 0
        result = self.basic_math.add([2, -2])
        self.assertEqual(result, expected)

    def test_add_positive_numbers_as_string(self):
        with self.assertRaises(TypeError):
            self.basic_math.add(["demo_string1", "demo_string2"])

    def test_subtract_two_positive_numbers(self):
        expected = 2
        result = self.basic_math.subtract(3, 1)
        self.assertEqual(result, expected)

    def test_subtract_two_negative_numbers(self):
        expected = 1
        result = self.basic_math.subtract(-2, -3)
        self.assertEqual(result, expected)

    def test_subtract_positive_and_negative_numbers(self):
        expected = 6
        result = self.basic_math.subtract(5, -1)
        self.assertEqual(result, expected)

    def test_subtract_and_negative_positive_numbers(self):
        expected = -6
        result = self.basic_math.subtract(-5, 1)
        self.assertEqual(result, expected)

# subtract function tests end

    def test_multiply_two_positive_numebrs(self):
        expected = 6
        result = self.basic_math.multiply(2, 3)
        self.assertEqual(result, expected)

    def test_multiply_two_negative_numebrs(self):
        expected = 200
        result = self.basic_math.multiply(-10, -20)
        self.assertEqual(result, expected)

    def test_multiply_positive_negative_numebrs(self):
        expected = -8
        result = self.basic_math.multiply(2, -4)
        self.assertEqual(result, expected)

    def test_multiply_negative_positive_numebrs(self):
        expected = -36
        result = self.basic_math.multiply(-12, 3)
        self.assertEqual(result, expected)

# multiply function tests end

    def test_divide_two_positive_numebrs(self):
        expected = 5
        result = self.basic_math.divide(10, 2)
        self.assertEqual(result, expected)

    def test_divide_two_negative_numebrs(self):
        expected = 5
        result = self.basic_math.divide(-10, -2)
        self.assertEqual(result, expected)

    def test_divide_negative_positive_numebrs(self):
        expected = -5
        result = self.basic_math.divide(-10, 2)
        self.assertEqual(result, expected)

    def test_divide_positive_negative_numebrs(self):
        expected = -5
        result = self.basic_math.divide(10, -2)
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.basic_math.divide(10, 0)
             
# divide function tests end

if __name__ == "__main__":
    unittest.main()

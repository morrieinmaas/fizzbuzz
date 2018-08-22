import unittest
import fizzbuzz
from fizzbuzz import fizzbuzz
from fizzbuzz.fizzbuzz import FizzBuzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    
    def test_assertions_int_1(self):
        self.assertRaises(AssertionError, lambda: FizzBuzz(3.5))
    
    def test_assertions_int_2(self):
        self.assertRaises(AssertionError, lambda: FizzBuzz(3.5, 4.6))
        
    def test_assertions_int_3(self):
        self.assertRaises(AssertionError, lambda: FizzBuzz(3.5, 'foo'))
        
    def test_assertions_int_1(self):
        self.assertRaises(AssertionError, lambda: FizzBuzz('foo'))
            
    def test_fizz_start(self):
        res = []
        for i in FizzBuzz(3):
            res.append(str(i))
        self.assertEqual(res, ['1', '2', 'Fizz'])
    
    def test_fizz_start_end(self):
        res = []
        expected_list = ['Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        for i in FizzBuzz(10, 15):
            res.append(str(i))
        self.assertEqual(res,  expected_list)
        
    def test_fizz_end_start(self):
        res = []
        expected_list = ['Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        for i in FizzBuzz(15, 10):
            res.append(str(i))
        self.assertEqual(res, expected_list)
    
    def test_fizz_end_equal_start(self):
        res = []
        expected_list = ['FizzBuzz']
        for i in FizzBuzz(15, 15):
            res.append(str(i))
        self.assertEqual(res, expected_list)
        
if __name__ == '__main__':
    unittest.main()

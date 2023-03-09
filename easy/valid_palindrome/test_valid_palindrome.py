import unittest
from valid_palindrome import check_valid_palindrome

class TestTwoSum(unittest.TestCase):
    def test_check_valid_palindrome(self):
        self.assertEqual(check_valid_palindrome("race a car"), False)
        self.assertEqual(check_valid_palindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(check_valid_palindrome(" "), True)
    
if __name__ == '__main__':
    unittest.main()
    
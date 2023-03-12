import unittest
from valid_anagram import isAnagram

class TestValidAnagram(unittest.TestCase):
    def test_isAnagram(self):
        self.assertEqual(isAnagram("anagram", "nagaram"), True)
        self.assertEqual(isAnagram("rat", "car"), False)
    
if __name__ == '__main__':
    unittest.main()
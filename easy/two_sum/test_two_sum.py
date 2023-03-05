import unittest
from two_sum import find_two_sum

class TestTwoSum(unittest.TestCase):
    def test_find_two_sum(self):
        self.assertEqual(set(find_two_sum(nums=[1,3,5,7], target=6)), set([0,2]))
        self.assertEqual(set(find_two_sum(nums=[3,6,3], target=6)), set([0,2]))
    
if __name__ == '__main__':
    unittest.main()
    
import unittest
from binary_search import search

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([1,3,5,7,9,11], 7), 3)
        self.assertEqual(search([0,1,2,3,4,5], 5), 5)
        self.assertEqual(search([0,1,2,3,4,5], 6), -1)
    
if __name__ == '__main__':
    unittest.main()
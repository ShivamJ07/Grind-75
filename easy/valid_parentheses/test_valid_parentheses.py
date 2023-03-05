import unittest
from valid_parentheses import check_valid_parens

class TestValidParentheses(unittest.TestCase):
    def test_check_valid_parens(self):
        self.assertEqual(check_valid_parens('[]'), True)
        self.assertEqual(check_valid_parens('[{(}]'), False)

if __name__ == '__main__':
    unittest.main()
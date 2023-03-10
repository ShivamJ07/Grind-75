import unittest
from invert_binary_tree import invertTree, TreeNode

class TestInvertTree(unittest.TestCase):
    def test_max_profit(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        invertTree(root)
        self.assertEqual(root.left.val, TreeNode(7).val)
        self.assertEqual(root.right.val, TreeNode(2).val)
        self.assertEqual(root.right.left.val, TreeNode(3).val)
        self.assertEqual(root.right.right.val, TreeNode(1).val)
        self.assertEqual(root.left.left.val, TreeNode(9).val)
        self.assertEqual(root.left.right.val, TreeNode(6).val)
    
if __name__ == '__main__':
    unittest.main()
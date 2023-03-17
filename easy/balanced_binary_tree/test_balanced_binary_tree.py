import unittest
from balanced_binary_tree import TreeNode, isBalanced

class TestBalancedBinaryTree(unittest.TestCase):
    def test_isBalanced(self):
        baseNode = TreeNode(3)
        baseNode.left = TreeNode(9)
        baseNode.right = TreeNode(20)
        baseNode.right.left = TreeNode(15)
        baseNode.right.right = TreeNode(7)
        self.assertEqual(isBalanced(baseNode), True)
        baseNode.right.right.right = TreeNode(8)
        self.assertEqual(isBalanced(baseNode), False)

if __name__ == '__main__':
    unittest.main()
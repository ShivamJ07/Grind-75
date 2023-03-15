import unittest
from LCA_BST import lowestCommonAncestor, TreeNode

class TestLowestCommonAncestor(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        baseNode = TreeNode(6)
        baseNode.left = TreeNode(2)
        baseNode.right = TreeNode(8)
        baseNode.left.left = TreeNode(0)
        baseNode.left.right = TreeNode(4)
        baseNode.right.left = TreeNode(7)
        baseNode.right.right = TreeNode(9)
        baseNode.left.right.left = TreeNode(3)
        baseNode.left.right.right = TreeNode(5)

        p = TreeNode(2)
        q = TreeNode(8)
        self.assertEqual(lowestCommonAncestor(baseNode, p, q).val, 6)

        q = TreeNode(4)
        self.assertEqual(lowestCommonAncestor(baseNode, p, q).val, 2)

if __name__ == '__main__':
    unittest.main()
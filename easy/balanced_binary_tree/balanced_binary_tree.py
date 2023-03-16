from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For a tree to be balanced from the perspective of the root node, it must satisfy two conditions
# The difference of height of both subtrees must be less than equal to 1
# Both subtrees must be balanced themselves
# To determine if a subtree is balanced, we must essentially determine if the subtrees of all descendants have a height diff <= 1
# This is a recursive problem, we must compute the height of each subtree of each descendant, if even once the height diff is greater than 1 the tree is unbalanced  

def isBalanced(root: Optional[TreeNode]) -> bool:
   get_balanced_height(root)


def get_balanced_height(root: Optional[TreeNode]):
    if not root:

        # Empty tree is balanced and has a height of 0
        return (True, 0)

    left_tree = get_balanced_height(root.left)
    right_tree = get_balanced_height(root.right)

    # If subtrees are balanced and height diff of subtrees is less than 1, then current tree is balanced, else not
    is_balanced = left_tree[0] and right_tree[0] and (abs(left_tree[1] - right_tree[1]) <= 1)

    # 1 + max(left_tree[1], right_tree[1]) computes the height of the current subtree
    return (is_balanced, 1 + max(left_tree[1], right_tree[1]))

baseNode = TreeNode(3)
baseNode.right = TreeNode(20)
baseNode.left = TreeNode(9)
baseNode.right.right = TreeNode(7)
baseNode.right.left = TreeNode(15)

print(get_balanced_height(baseNode))
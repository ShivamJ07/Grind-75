class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive approach, create a function to switch children of any node, apply that to every node in the tree
# Post order depth first search traversal, base case is that the root is None in which case we simply return to the caller
# Time complexity: O(n) - since we are essentially just visitng every node in the tree, it's linear time where n refers to the number of nodes
# Space complexity: O(n) - since this is a recursive function, the amount of space used refers to the space required on the call stack
# the number of recursive function calls will depend on the number of nodes in the tree, if all nodes were on one side, there would be n function call

def invertTree(root):
    if root is not None:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)
        return root
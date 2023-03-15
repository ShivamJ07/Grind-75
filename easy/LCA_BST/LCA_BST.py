class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Current node can be LCA under two conditions, either it is greater than (p/q) and lesser than (q/p) or it is equal to either p or q
# If this is not the case, the LCA must exist in either the left or right subtree of current node
# If both p and q are greater, LCA is in right subtree else it is in the right subtree - recursively call the function again
# Time complexity: O(n) if tree is skewed and O(log(n)) is tree is balanced, in a skewed tree, you may have to traverse through almost all the nodes before finding LCA, in a balanced tree, you halve the number of nodes to search with each iteration so time taken is logarithmic with respect to number of nodes
# Space complexity: Similar logic to time complexity since space used depends on space used in call stack i.e. maximum number of stack frames on the call stack at a given time, since each recursive call corresponds to a single node, the logic is the same as the time complexity

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if (root.val > p.val and root.val < q.val) or (root.val > q.val and root.val < p.val) or (root.val == q.val) or (root.val == p.val):
        return root

    if (root.val < p.val and root.val < q.val):
        return lowestCommonAncestor(root.right, p, q)
    else:
        return lowestCommonAncestor(root.left, p, q)

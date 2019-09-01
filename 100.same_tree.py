# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

### Solution: https://leetcode.com/problems/symmetric-tree/solution/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """

    # Recursively check nodes at same level
    # If both p & ! are not empty and their values match, go deeper left and right
    # If previous condition fails it's because either p or q is empty OR their values fon't match, hence:
    #   - if both p or q are empty, then they are =, return True
    #   - if last condition fails, their values don't match, return False

    def check_node(p, q):
        if p and q and p.val == q.val:
            return check_node(p.left, q.left) and check_node(p.right, q.right)
        if p is None and q is None:
            return True
        return False

    return check_node(p, q)
        
        

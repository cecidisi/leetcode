# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    def add_node(node, level, order_trav):
        if node:
            if level == len(order_trav):
                order_trav.append([])
            order_trav[level].append(node.val)

            order_trav = add_node(node.left, level+1, order_trav)
            order_trav = add_node(node.right, level+1, order_trav)
        return order_trav

    order_trav = add_node(root, 0, [])[::-1]
    return order_trav
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def is_mirror(tree_left, tree_right):
        # goo deeper if subtrees not empty and values match
        if tree_left and tree_right:        
            return tree_left.val == tree_right.val and \
                   is_mirror(tree_left.left, tree_right.right) and \
                   is_mirror(tree_left.right, tree_right.left)

        # if we reach leaves i both subtrees, they are mirrored
        if tree_left is None and tree_right is None:
            return True

        # subtrees aren't empty and values don't match
        return False

    return is_mirror(root, root)
            
        

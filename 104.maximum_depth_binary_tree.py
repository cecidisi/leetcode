# 104. Maximum Depth of Binary Tree
# 
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


def maxDepth(self, root):
  """
  :type root: TreeNode
  :rtype: int
  """

  def get_max_depth(tree, cur_depth):
      if tree is None:
          return cur_depth
      return max(get_max_depth(tree.left, cur_depth+1), get_max_depth(tree.right, cur_depth+1))


  return get_max_depth(root, 0)
        

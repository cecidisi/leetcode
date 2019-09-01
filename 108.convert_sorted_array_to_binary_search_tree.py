## Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
## 
## For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
## 
## Example:
## 
## Given the sorted array: [-10,-3,0,5,9],
## 
## One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
## 
##       0
##      / \
##    -3   9
##    /   /
##  -10  5
## 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def build_tree(l, h, nums):
        if l<=h:
            m = (l+h)/2
            node = TreeNode(nums[m])
            node.left = build_tree(l, m-1, nums)
            node.right = build_tree(m+1, h, nums)
            return node
        else:
            return None


    return build_tree(0, len(nums)-1, nums)
        

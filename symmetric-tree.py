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
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
        def __init__(self, val, left = None, right = None):
            self.val = val
            self.left = left
            self.right = right

class Solution:
    

    def areTreesSymmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None and left.val == right.val:
            
            return self.areTreesSymmetric(left.left, right.right) and self.areTreesSymmetric(left.right, right.left)
        
        else:
            return False

    def isSymmetric(self, node):
        if node is None:
            return True
        else:
            
            return self.areTreesSymmetric(node.left, node.right)





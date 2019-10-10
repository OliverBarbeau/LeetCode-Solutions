
# Problem #98
# https://leetcode.com/problems/validate-binary-search-tree
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    isValid = True
    def isValidBST(self, root: TreeNode, mini = float("inf"), maxi = float("-inf")) -> bool:
        
        if root is None:
            return True
        if self.isValid is False:
            return False
        print(root.val)
        if (mini != float('inf') and mini >= root.val) or (maxi != float("-inf") and maxi <= root.val):
            self.isValid = False
            return False
        
        #check if left and right are valid
        #call isValidBST on left, and right
        #return AND operation on results of left and right
        #if either left or right is invalid return false
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            if root.right.val > root.val:
                return self.isValidBST(root.right, min(mini, root.val), maxi)
        elif root.right is None:
            if root.left.val < root.val:
                return self.isValidBST(root.left, mini, max(root.val, maxi))
        elif root.right is not None and root.left is not None:
            if root.left.val < root.val and root.right.val > root.val:
                return self.isValidBST(root.left, mini, max(root.val, maxi)) and self.isValidBST(root.right, min(mini, root.val), maxi)
        self.isValid = False
        return False
# Problem #404
# https://leetcode.com/problems/sum-of-left-leaves
# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if root is None:
            return 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                sum += root.left.val
            sum += self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            sum += self.sumOfLeftLeaves(root.right)
        return sum
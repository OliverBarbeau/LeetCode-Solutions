# Problem #124
# https://leetcode.com/problems/binary-tree-maximum-path-sum
# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x    
        self.left = None
        self.right = None

class Solution:
    mx = float('-inf')
    def maxPathSumFromRoot(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxPathSumFromRoot(root.left)
        right = self.maxPathSumFromRoot(root.right)
        thisMax = max(root.val, root.val+right, root.val + left)
        self.mx = max(self.mx, thisMax, root.val + right + left)
        
        return thisMax
            
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxPathSumFromRoot(root)
        return self.mx
            
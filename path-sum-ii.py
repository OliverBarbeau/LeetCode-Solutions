# Problem #113
# https://leetcode.com/problems/path-sum-ii
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    paths = []
    def pathSumHelper(self,root: TreeNode, sum: int, path: list):
        if root == None:
            return
        newSum = sum-root.val
        if root.left == None and root.right == None and newSum == 0:
            self.paths.append(path+[root.val])
        else:
            self.pathSumHelper(root.left, newSum, path+[root.val])
            self.pathSumHelper(root.right, newSum, path+[root.val])

    def pathSum(self, root: TreeNode, sum: int) -> list:
        self.paths = []
        self.pathSumHelper(root, sum, [])
        return self.paths
# Problem #100
# https://leetcode.com/problems/same-tree
# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        same = True
        que = queue.Queue()
        que.put([p,q])
        while same and que.qsize() != 0:
            nodes = que.get()
            if nodes[0] != None and nodes[1] != None:
                if nodes[0].val != nodes[1].val:
                    same = False
                que.put([nodes[0].left,nodes[1].left])
                que.put([nodes[0].right,nodes[1].right])
            elif nodes[0] != nodes[1]:
                same = False
        return same

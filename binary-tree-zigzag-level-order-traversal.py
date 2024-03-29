# Problem #103
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        #first level is left
        #add to stack its children, right to left
        s = [root]
        left_right = True
        newS = []
        layers = []
        thisLayer = []
        while s != []:
            item = s.pop()
            thisLayer.append(item.val)
            if left_right:
                if item.left is not None:
                    newS.append(item.left) 
                if item.right is not None:
                    newS.append(item.right) 
            else:
                if item.right is not None:
                    newS.append(item.right) 
                if item.left is not None:
                    newS.append(item.left) 
                
            if s == []:
                layers.append(thisLayer)
                thisLayer = []
                s = newS.copy()
                newS = []
                left_right = not left_right

        return layers
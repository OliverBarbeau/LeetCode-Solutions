# Problem #445
# https://leetcode.com/problems/add-two-numbers-ii/
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l1Stack = []
        l2Stack = []
        while l1 is not None:
            l1Stack.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2Stack.append(l2.val)
            l2 = l2.next
            
        node = None
        while len(l1Stack) != 0 or len(l2Stack) != 0:
            l1Item = l1Stack.pop() if len(l1Stack) != 0 else 0
            l2Item = l2Stack.pop() if len(l2Stack) != 0 else 0
            s = l1Item + l2Item + carry
            carry = s // 10
            item = s % 10
            newNode = ListNode(item)
            newNode.next = node
            node = newNode
        if carry == 1:
            newNode = ListNode(1)
            newNode.next = node
            return newNode
        return node
            
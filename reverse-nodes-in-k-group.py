# Problem #25
# https://leetcode.com/problems/reverse-nodes-in-k-group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head == None:
            return head
        startK = k
        node = head
        while k > 0 and node is not None:

            node = node.next
            
            k -= 1
        if k != 0:
            return head
        k = startK
        node = head
        nextNode = head.next
        if nextNode is not None:
            after = nextNode.next
        # 2 - 1 - 3 - 4 - 5 k = 3
        while k > 1:
            k -= 1
            nextNode.next = head
            head = nextNode
            node.next = after
            nextNode = after
            if nextNode is not None:
                after = nextNode.next
            else:
                after = None
        if nextNode is not None:
            node.next = self.reverseKGroup(node.next, startK)

        return head
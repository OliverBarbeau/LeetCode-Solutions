# Problem #61
# https://leetcode.com/problems/rotate-list/
# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if head is None or k == 0:
#             return head
        
#         lNodeList = []
#         node = head
#         while node is not None:
#             lNodeList.append(node)
#             node = node.next
#         length = len(lNodeList)
#         diff = k %  (length)
#         lNodeList = lNodeList[-diff:] + lNodeList[:-diff]
#         strin = ""
#         head = lNodeList[0]
#         node = head
#         for n in lNodeList[1:]:
#             strin = strin + str(n.val) + "->"
#             node.next = n
#             node = n
#         node.next = None
#         print(strin)
#         return head
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        diff = k % (length)
        if diff == 0:
            return head
        node = head
        prior = None
        i = 0
        while node is not None:
            if i == (length-diff):
                prior.next = None
                newHead = node
            prior = node
            node = node.next
            i += 1
        prior.next = head

        return newHead
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curNode = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        if l1 is not None:
            
            curNode.next = l1
        else:
            curNode.next = l2
            
        return head.next
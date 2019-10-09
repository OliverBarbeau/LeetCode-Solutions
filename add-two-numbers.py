# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        newList = head
        carry = 0
        sum = 0
        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            sum = sum % 10
            newList.next = ListNode(sum)
            newList = newList.next
        if carry:
            newList.next = ListNode(carry)
        return head.next
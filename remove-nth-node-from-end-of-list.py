# Definition for singly-linked list.

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s = []
        current = head
        while(current != None):
            s.append(current)
            current = current.next
        
        nthNode = head
        for _ in range(n):
            nthNode = s.pop()
        print("Value is",nthNode.val)
        if nthNode == head:
            print('nthNode=head')
            return head.next
        else:
            prior = s.pop()
            prior.next = prior.next.next
        
        return head
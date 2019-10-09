# Definition for singly-linked list.
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
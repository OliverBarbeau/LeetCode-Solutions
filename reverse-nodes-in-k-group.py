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
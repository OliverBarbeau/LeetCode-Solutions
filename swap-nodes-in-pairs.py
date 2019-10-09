# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node = head
        if node.next is None:
            return node
        nex = node.next
        head = nex
        while node is not None and nex is not None:
            nextSetNode = nex.next
            if nextSetNode is not None:
                nextSetNex = nextSetNode.next
            else:
                nextSetNex = None
            
            nex.next = node
            if nextSetNex is not None:
                node.next = nextSetNex
            else:
                node.next = nextSetNode
            node = nextSetNode
            nex = nextSetNex
            
        return head
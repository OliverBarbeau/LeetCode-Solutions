// # Remove all elements from a linked list of integers that have value val.

// # Example:

// # Input:  1->2->6->3->4->5->6, val = 6
// # Output: 1->2->3->4->5

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode prior = null;
        ListNode cur = head;
        while (cur != null){
            if (cur.val == val){
                if (prior == null){
                    head = cur.next;
                    prior = null;
                }else{
                    prior.next = cur.next;
                }
            }else {
                prior = cur;

            }
            cur = cur.next;
            
        }
        return head;
    }
}
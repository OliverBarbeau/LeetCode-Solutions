// Problem # 206
// https://leetcode.com/problems/reverse-linked-list
//Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?

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
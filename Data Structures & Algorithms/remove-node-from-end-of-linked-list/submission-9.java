/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (n == 1 && head.next == null) {
            return null;
        }

        ListNode end = head;
        ListNode target = head;
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode prev = dummy;

        while (end != null && n > 0) {
            end = end.next;
            n = n - 1;
        }

        while (end != null) {
            end = end.next;
            target = target.next;
            prev = prev.next;
        }

        ListNode temp = target.next;
        prev.next = temp;
        target.next = null;

        return dummy.next;
    }
}

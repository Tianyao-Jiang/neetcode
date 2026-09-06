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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;

        int carryover = 0;
        while(l1 != null || l2 != null) {
            int temp = carryover;
            if (l1 != null) {
                temp += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                temp += l2.val;
                l2 = l2.next;
            }

            if (temp < 10) {
                cur.next = new ListNode(temp);
                cur = cur.next;
                carryover = 0;
            } else {
                cur.next = new ListNode(temp % 10);
                cur = cur.next;
                carryover = 1;
            }
        }

        if (carryover == 1) {
            cur.next = new ListNode(1);
        }

        return dummy.next;
    }
}

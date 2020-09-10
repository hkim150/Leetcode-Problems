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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        // split
        ListNode slow = head;
        ListNode fast = head;

        while (true) {
            fast = fast.next;
            if (fast == null)
                break;

            fast = fast.next;
            if (fast == null)
                break;

            slow = slow.next;
        }

        ListNode l1 = head;
        ListNode l2 = slow.next;
        slow.next = null;

        l1 = this.sortList(l1);
        l2 = this.sortList(l2);

        // merge
        ListNode dummyHead = new ListNode();
        ListNode curr = dummyHead;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }

            curr = curr.next;
        }

        if (l1 != null)
            curr.next = l1;

        if (l2 != null)
            curr.next = l2;

        return dummyHead.next;
    }
}
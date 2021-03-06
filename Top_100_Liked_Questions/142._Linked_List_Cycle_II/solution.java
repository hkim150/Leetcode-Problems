/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null)
            return null;

        ListNode fast = head;
        ListNode slow = head;

        while (true) {
            fast = fast.next;
            if (fast == null)
                return null;

            fast = fast.next;
            if (fast == null)
                return null;

            slow = slow.next;

            if (fast == slow)
                break;
        }

        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        return fast;
    }
}
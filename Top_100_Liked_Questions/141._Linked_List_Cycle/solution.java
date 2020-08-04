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
    public boolean hasCycle(ListNode head) {
        // fast and slow pointer method
        if (head == null)
            return false;

        ListNode fast = head;
        ListNode slow = head;

        do {
            fast = fast.next;
            if (fast == null)
                return false;

            fast = fast.next;
            if (fast == null)
                return false;

            slow = slow.next;
        } while (fast != slow);

        return true;
    }
}
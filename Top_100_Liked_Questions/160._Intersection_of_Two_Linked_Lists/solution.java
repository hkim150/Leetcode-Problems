/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null)
            return null;

        ListNode pt1 = headA;
        ListNode pt2 = headB;

        int flipCount = 0;

        while (flipCount <= 2) {
            if (pt1 == pt2)
                return pt1;

            if (pt1.next != null)
                pt1 = pt1.next;
            else {
                pt1 = headB;
                flipCount++;
            }

            if (pt2.next != null)
                pt2 = pt2.next;
            else {
                pt2 = headA;
                flipCount++;
            }
        }

        return null;
    }
}
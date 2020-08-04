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
    private ListNode frontPointer;

    public boolean isPalindrome(ListNode head) {
        // store and two pointer
        List<Integer> mem = new ArrayList<>();

        while (head != null) {
            mem.add(head.val);
            head = head.next;
        }

        int i=0;
        int j=mem.size()-1;

        while (i < j) {
            if (!mem.get(i++).equals(mem.get(j--)))
                return false;
        }

        return true;
    }

    public boolean isPalindrome2(ListNode head) {
        // recursive method
        this.frontPointer = head;
        return this.checkPal(head);
    }

    public boolean checkPal(ListNode node) {
        if (node == null || this.frontPointer == null)
            return true;

        boolean ans = checkPal(node.next) && (this.frontPointer.val == node.val);

        this.frontPointer = this.frontPointer.next;
        return ans;
    }
}
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null)
            return null;

        // for every node, create its copy and insert it between itself and next
        Node curr = head;
        while (curr != null) {
            Node copy = new Node(curr.val);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }

        // for every copied node, connect its random to its next's random's next
        curr = head;
        while (curr != null) {
            if (curr.random != null)
                curr.next.random = curr.random.next;
            else
                curr.next.random = null;

            curr = curr.next.next;
        }

        // separate the copied node list and return its head
        Node copyHead = head.next;
        Node copyCurr = copyHead;
        curr = head;

        while (copyCurr.next != null) {
            curr.next = copyCurr.next;
            curr = curr.next;
            copyCurr.next = curr.next;
            copyCurr = copyCurr.next;
        }

        curr.next = null;
        copyCurr.next = null;

        return copyHead;
    }
}
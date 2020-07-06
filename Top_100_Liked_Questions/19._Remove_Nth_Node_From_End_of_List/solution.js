/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let dummyHead = new ListNode(0, head);
    let slow = dummyHead;
    let fast = dummyHead;
    
    for (let i=0; i<n; i++) {
        fast = fast.next;
    }
    
    while (fast.next) {
        fast = fast.next;
        slow = slow.next;
    }
    
    let delNode = slow.next;
    slow.next = delNode.next;
    delNode.next = null;
    delete delNode;
    
    head = dummyHead.next;
    dummyHead.next = null;
    delete dummyHead;
    
    return head;
};
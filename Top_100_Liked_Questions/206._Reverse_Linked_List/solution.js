/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = head => {
    if (head === null || head.next === null) {
        return head;
    }
    
    const newHead = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    
    return newHead;
}

var reverseListIterative = function(head) {
    let prev = null;
    
    while (head) {
        [head.next, prev, head] = [prev, head, head.next];
    }
    
    return prev;
};
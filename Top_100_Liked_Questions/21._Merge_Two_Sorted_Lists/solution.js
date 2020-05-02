/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    let dummyNode = new ListNode();
    let currNode = dummyNode;
    
    while (l1 && l2) {
        if (l1.val < l2.val) {
            currNode.next = l1;
            l1 = l1.next;
        } else {
            currNode.next = l2;
            l2 = l2.next;
        }
        currNode = currNode.next;
    }
    
    currNode.next = l1 ? l1 : l2;
    
    const newHead = dummyNode.next;
    // remove the reference to the dummyNode instance so that the GC removes it
    dummyNode = undefined;
    
    return newHead;
};
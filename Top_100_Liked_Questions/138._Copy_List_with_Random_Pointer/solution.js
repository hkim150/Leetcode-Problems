/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    if (!head) {
        return null;
    }
    
    // create copy node and put it between its next node
    let curr = head;
    while (curr) {
        let copyNode = new Node(curr.val, curr.next, null);
        let next = curr.next;
        curr.next = copyNode;
        curr = next;
    }
    
    // set copy node's random as prev.random.next
    let prev = head;
    while (prev) {
        curr = prev.next;
        if (prev.random === null) {
            curr.random === null;
        } else {
            curr.random = prev.random.next;
        }
        prev = curr.next;
    }
    
    // separate the copy nodes and return its head
    let copyHead = head.next;
    let originalNode = head;
    let copyNode = copyHead;
    while (copyNode.next) {
        originalNode.next = copyNode.next;
        originalNode = originalNode.next;
        copyNode.next = originalNode.next;
        copyNode = copyNode.next;
    }
    originalNode.next = null;
    
    return copyHead;
};
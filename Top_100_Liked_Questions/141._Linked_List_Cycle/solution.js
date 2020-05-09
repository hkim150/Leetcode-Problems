/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    // two pointer method
    if (!head || !head.next) {
        return false;
    }
    
    let slow = head;
    let fast = head.next;
    
    while (slow !== fast) {
        slow = slow.next;
        
        fast = fast.next;
        if (!fast) {
            return false;
        }
        
        fast = fast.next;
        if (!fast) {
            return false;
        }
    }
    
    return true;
};
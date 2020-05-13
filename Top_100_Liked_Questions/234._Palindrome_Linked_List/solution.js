/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    // slice and compare and restore method
    if (!head) {
        return true;
    }
    
    let curr = head;
    let nodeCount = 0;
    
    while (curr) {
        nodeCount++;
        curr = curr.next;
    }
    
    let tail1 = head;
    for (let i=0; i<Math.floor((nodeCount-1)/2); i++) {
        tail1 = tail1.next;
    }
    
    let head2 = tail1.next;
    tail1.next = null;
    
    const reverseLinkedList = function(node) {
        let prev = null;
        
        while (node) {
            let nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        
        return prev;
    }
    
    head2 = reverseLinkedList(head2);
    
    let ans = true;
    let p1 = head;
    let p2 = head2;
    
    while (p2) {
        if (p1.val !== p2.val) {
            ans = false;
            break;
        }
        p1 = p1.next;
        p2 = p2.next;
    }
    
    head2 = reverseLinkedList(head2);
    tail1.next = head2;
    
    return ans;
}

var isPalindrome3 = function(head) {
    // recursive method
    let front = head;
    const checkPalindrome = function(node) {
        if (node) {
            if (!checkPalindrome(node.next) || front.val !== node.val) {
                return false;
            }
            
            front = front.next;
        }
        
        return true;
    }
    
    return checkPalindrome(head);
};

var isPalindrome2 = function(head) {
    // store and two pointer method
    arr = [];
    while (head) {
        arr.push(head.val);
        head = head.next;
    }

    p1 = 0
    p2 = arr.length-1;
    
    while (p1 < p2) {
        if (arr[p1++] !== arr[p2--]) {
            return false;
        }
    }
    
    return true;
};
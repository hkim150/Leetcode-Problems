/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    /* If we call the part of the linked list where the two lists overlap as x
and call the unique parts as a and b for linked lists A and B respectively, then A = a->x, B = b->x if we linked the end of the each list to the other like the following: A->B and B->A which is also a->x->b->x and b->x->a->x, where the two have the same number of nodes. If len(a) == len(b) then the two pointers will meet at the first entering point of x. Else, since len(a->x->b) == len(b->x->a), the two pointrs will meet at the second entering point of x. Thus, they are guaranteed to meet at the intersection.
    */
    if (!headA || !headB)
        return null;
    
    let p1 = headA;
    let p2 = headB;
    
    let cnt = 0;
    while (cnt <= 2) {
        if (p1 === p2)
            return p1;
        
        if (p1.next)
            p1 = p1.next;
        else {
            p1 = headB;
            cnt ++;
        }
        
        if (p2.next)
            p2 = p2.next;
        else {
            p2 = headA;
            cnt++;
        }
    }
    
    return null;
};
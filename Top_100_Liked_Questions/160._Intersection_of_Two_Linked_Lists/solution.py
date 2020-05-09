# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        
        cnt = 0
        while cnt <= 2:
            if p1 is p2:
                return p1
            
            if p1.next:
                p1 = p1.next
            else:
                p1 = headB
                cnt += 1
            
            if p2.next:
                p2 = p2.next
            else:
                p2 = headA
                cnt += 1
        
        return None
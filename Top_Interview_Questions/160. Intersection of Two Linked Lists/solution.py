# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # we can use hashmap to store the nodes of listA and find the first overlap in listB
        hashmap = {}
        while headA:
            hashmap[headA] = True
            headA = headA.next
        
        while headB:
            if headB in hashmap:
                return headB
            
            headB = headB.next
        
        return None
    
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        # two pointer method that uses only a constant space
        # if there is an intersection between two lists, each have the form AO, BO
        # if we connect the each tail to each other's tail, they become AOBO, BOAO
        # they have the same length and has same ending starting from the intersection
        # thus, we are garanteed to find the first intersection if there is one
        # within the length of both lists combined
        pA = headA
        pB = headB
        firstA = firstB = True
        
        while True:
            if pA is pB:
                return pA
            
            if pA:
                pA = pA.next
            else:
                if firstA:
                    pA = headB
                    firstA = False
                else:
                    return None
            
            if pB:
                pB = pB.next
            else:
                if firstB:
                    pB = headA
                    firstB = False
                else:
                    return None
        
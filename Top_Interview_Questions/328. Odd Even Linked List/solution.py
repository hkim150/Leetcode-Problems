# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        # we need to keep track of the tail of the odd list
        # as we need to connect it with the head of even list
        curr = oddTail = head
        evenHead = head.next
        
        # a flipping boolean for keeping track of even/odd
        odd = True
        
        while True:
            # save next node
            nxt = curr.next
            
            if not nxt:
                if odd:
                    curr.next = evenHead
                else:
                    oddTail.next = evenHead
                break

            # curr node points next node's next
            curr.next = nxt.next

            if odd:
                oddTail = curr
            
            odd = not odd
            
            # move on to next
            curr = nxt
        
        return head
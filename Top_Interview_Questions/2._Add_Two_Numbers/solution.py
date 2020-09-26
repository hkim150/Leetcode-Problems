# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy node
        retHead = curr = ListNode(0)
        carry = 0
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            newVal = a + b + carry
            if newVal >= 10:
                carry = 1
                newVal -= 10
            else:
                carry = 0

            curr.next = ListNode(newVal)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            curr.next = ListNode(1)
        
        # delete dummy node and return the real head
        head = retHead.next
        del retHead
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    
    
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            # store the next node
            nxt = head.next

            # point .next to prev node
            head.next = prev

            # go to the stored next node
            prev = head
            head = nxt
        
        return prev
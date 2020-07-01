# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # double pointer method
        if not head:
            return None
        
        slow = fast = head
        while True:
            fast = fast.next
            if not fast:
                return None
            
            fast = fast.next
            if not fast:
                return None
            
            slow = slow.next
            if slow is fast:
                break
        
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return fast
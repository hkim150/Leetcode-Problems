# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # two pointer method
        # have slow pointer advance by 1 node and fast pointer advance by 2
        # since the gap between the two pointers increase by 1 every step
        # they must meet before the slow pointer finishes one loop
        # if there is no loop, the fast pointer reaches the end
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            slow = slow.next
            
            fast = fast.next
            if not fast:
                return False
            
            fast = fast.next
            if not fast:
                return False
        
        return True
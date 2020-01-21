# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # we can have a fast pointer that goes over two nodes
        # and a slow pointer that goes over one node
        # and check if they meet or the fast pointer meets an end
        fast = slow = head
        
        while True:
            if not fast:
                return False

            fast = fast.next
            slow = slow.next

            if not fast:
                return False

            fast = fast.next

            if fast is slow:
                return True
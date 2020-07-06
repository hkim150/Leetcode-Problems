# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # two pointer with constant gap method
        dummyHead = ListNode(0, head)
        fast = slow = dummyHead
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
      
        delNode = slow.next
        slow.next = delNode.next
        delNode.next = None
        del delNode

        head = dummyHead.next
        dummyHead.next = None
        del dummyHead
        
        return head
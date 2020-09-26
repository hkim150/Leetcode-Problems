# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy node for the first node
        dummyHead = curr = ListNode(0)
        
        # compare the heads of each lists and use the smaller one
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        # get the real head and delete the dummy head
        head = dummyHead.next
        del dummyHead
        
        return head
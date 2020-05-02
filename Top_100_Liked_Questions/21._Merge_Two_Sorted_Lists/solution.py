# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use a dummy node for the newHead
        curr = dummyNode = ListNode()
        
        # while both have next
        while l1 and l2:
            # append the smaller node to the combined list
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        # append the list that has not reached the end to the combined list
        curr.next = l1 if l1 else l2
        
        # get the real head and delete the dummy node
        newHead = dummyNode.next
        del dummyNode
        
        return newHead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            # store the next node
            nxt = curr.next

            # make current node point to prev node
            curr.next = prev

            # update prev as current node
            prev = curr

            # go to the stored node and repeat
            curr = nxt
        
        return prev
    

    # recursive solution
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        def reverse(prev, curr):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev

            return reverse(curr, nxt)

        return reverse(None, head)
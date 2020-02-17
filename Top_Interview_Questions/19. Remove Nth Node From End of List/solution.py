# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # one pass algorithm - leave a gap of size n+1 steps between two pointers: first and second
        # both pointers go over to each of their next node until the first pointer meets the end
        # second node is the previous node of the node to be deleted as we had an extra gap
        # thus we can remove the second pointer's next node
        
        # we can use a dummyHead node for the case of removing a head node
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        first = second = dummyHead
        
        # move first pointer n+1 steps to leave n nodes in between second pointer
        for _ in range(n+1):
            first = first.next
        
        # move both first and second pointer until first pointer meets the end
        while first:
            first = first.next
            second = second.next
        
        # remove the second's next node from the list
        delNode = second.next
        second.next = delNode.next
        del delNode
        
        # get the head from dummyHead's next as original one could have been the one that was deleted
        head = dummyHead.next
        del dummyHead
        
        return head
            
    
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # two pass algorithm - count the total num and remove the (count - n)'th node
        # count the number of nodes, cnt
        cnt = 0
        
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        
        if cnt == n:
            ret = head.next
            del head
            return ret
        
        # remove the cnt - n th node from the start
        prev = curr = head
        
        for _ in range(cnt-n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        del curr
        
        return head
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        # copy the list within it self A-B-C => A-A'-B-B'-C-C'
        curr = head
        while curr:
            nxt = curr.next
            copyNode = ListNode(curr.val)
            copyNode.next = nxt
            curr.next = copyNode
            curr = nxt
        
        # fill out the copied nodes' random by the original nodes' random.next
        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = copy.next
        
        # separate the original and copied nodes
        curr = head
        copyHead = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if curr.next:
                copy.next = curr.next.next
            curr = curr.next
        
        return copyHead
            
        
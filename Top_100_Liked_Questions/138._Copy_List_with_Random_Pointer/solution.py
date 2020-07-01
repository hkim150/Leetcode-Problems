"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # make a copy node and place it between current and next node
        curr = head
        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode
            curr = newNode.next
        
        # set the random of the copy nodes as prev node's random's next
        prev = head
        while prev:
            curr = prev.next
            curr.random = prev.random.next if prev.random else None
            prev = curr.next
        
        # separate the copy nodes from the list and return its head
        orig = head
        copy = copyHead = head.next
        while copy.next:
            orig.next = copy.next
            orig = copy.next
            copy.next = orig.next
            copy = orig.next
        
        orig.next = None
        
        return copyHead
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # traverse the tree in level order
        q = [(root, 0)]
        curr_lvl = 0
        level = []
        
        while q:
            node, lvl = q.pop(0)
            if not node:
                continue
        
            # on end of a level, make each node to point to the one on its right
            if lvl > curr_lvl:
                curr_lvl = lvl
                for i in range(len(level)-1):
                    level[i].next = level[i+1]
                level = []
            
            level.append(node)
            
            q.append( (node.left, lvl+1) )
            q.append( (node.right, lvl+1) )
        
        # flush out the last level of nodes as the loop exits early
        if level:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        
        return root
        
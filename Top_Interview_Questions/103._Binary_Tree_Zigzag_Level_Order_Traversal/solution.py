# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [(root, 0)]
        inOrder = []
        while q:
            root, lvl = q.pop(0)
            if not root:
                continue
            if lvl == len(inOrder):
                inOrder.append([root.val])
            else:
                inOrder[-1].append(root.val)
                
            q.append((root.left, lvl+1))
            q.append((root.right, lvl+1))
        
        for lvl in range(len(inOrder)):
            if lvl % 2 == 1:
                inOrder[lvl] = inOrder[lvl][::-1]
        
        return inOrder
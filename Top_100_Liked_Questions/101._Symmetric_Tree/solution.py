# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [(root.left, root.right)]
        while queue:
            L, R = queue.pop(0)
            
            if not L and not R:
                continue

            if bool(L) != bool(R) or L.val != R.val:
                return False
            
            queue.append((L.left, R.right))
            queue.append((L.right, R.left))

        return True
    
    
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(L, R):
            if not L and not R:
                return True
            
            if bool(L) != bool(R):
                return False
            
            return L.val == R.val and helper(L.left, R.right) and helper(L.right, R.left)
        
        return helper(root.left, root.right)
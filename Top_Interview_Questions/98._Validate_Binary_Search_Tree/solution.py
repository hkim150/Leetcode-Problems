# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # iterative solution based on the recursive solution
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            root, lower, upper = stack.pop()
            
            if not root:
                continue
            
            v = root.val
            
            if v <= lower or v >= upper:
                return False
            
            stack.append((root.left, lower, v))
            stack.append((root.right, v, upper))
        
        return True
    
    def isValidBST2(self, root: TreeNode) -> bool:
        # straightforward solution using recursion
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            
            v = root.val
            
            if lower >= v or upper <= v:
                return False
            
            if not helper(root.left, lower, v):
                return False
            
            if not helper(root.right, v, upper):
                return False
            
            return True
        
        return helper(root)
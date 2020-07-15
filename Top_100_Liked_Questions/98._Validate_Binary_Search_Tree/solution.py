# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # iterative method
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lb, rb = stack.pop()
            if not node:
                continue
                
            if not lb < node.val < rb:
                return False
            
            stack.append((node.left, lb, node.val))
            stack.append((node.right, node.val, rb))
        
        return True
    
    
    def isValidBST2(self, root: TreeNode) -> bool:
        # recursive method
        # needs to fall between ranges
        def helper(node, leftBound, rightBound):
            if not node:
                return True
            
            return leftBound < node.val < rightBound and helper(node.left, leftBound, node.val) and helper(node.right, node.val, rightBound)
        
        return helper(root, float('-inf'), float('inf'))
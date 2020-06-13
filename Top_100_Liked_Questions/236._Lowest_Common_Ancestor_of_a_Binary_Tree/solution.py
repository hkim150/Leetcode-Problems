# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        def helper(node):
            if not node:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            
            mid = (node == p or node == q)
            
            if left + right + mid >= 2:
                ans[0] = node
            
            return left or right or mid
        
        helper(root)
        return ans[0]
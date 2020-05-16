# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        ans = []
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    
        return ans

                
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            ans.append(node.val)
            helper(node.right)
        
        helper(root)
        
        return ans
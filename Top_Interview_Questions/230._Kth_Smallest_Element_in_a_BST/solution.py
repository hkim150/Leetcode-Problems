# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # we can return the kth element during the inorder traversal
        self.count = 0
        self.ans = None
        
        def helper(r):
            if not r:
                return
            
            helper(r.left)
            if self.ans is not None:
                return
            self.count += 1
            if self.count == k:
                self.ans = r.val
                return
            helper(r.right)
        
        helper(root)
        
        return self.ans
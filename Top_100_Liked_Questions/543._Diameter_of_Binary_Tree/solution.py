# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # we need a variable that is outside the scope of the maxDepth function
        # either self.ans or a list would work
        # normal variable will not work as it would be considered local within the maxDepth function
        ans = [-1]
        
        def maxDepth(root):
            if not root:
                return -1

            L = maxDepth(root.left)
            R = maxDepth(root.right)
            ans[0] = max(ans[0], L + R + 2)
            return 1 + max(L, R)
        
        maxDepth(root)
        return ans[0]
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # a more compact solution
        def helper(root):
            if not root:
                return -1, 0
            
            l1, d1 = helper(root.left)
            l2, d2 = helper(root.right)
            
            return 1 + max(l1, l2), max(d1, d2, 2 + l1 + l2)
        
        return helper(root)[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # recursive inorder traversal
        inOrder = []
        
        def helper(root):
            if not root:
                return None

            helper(root.left)
            inOrder.append(root)
            helper(root.right)
        
        helper(root)
        
        idx = inOrder.index(p)
        if idx >= len(inOrder)-1:
            return None
        
        return inOrder[idx+1]
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # if sucessor is its descendants
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            
            return p
        
        # if not, then the successor could be its anscestor
        # iteratively inorder traverse with storing the prev node
        stack = []
        prev = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev == p:
                return root

            prev = root
            root = root.right
            
        # no successor found
        return None
            
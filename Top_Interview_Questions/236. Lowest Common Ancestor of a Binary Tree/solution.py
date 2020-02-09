# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find p and q's anscestors in order from closest to furthest
        path = []
        def getPath(root, node):
            if not root:
                return False
            
            if root is node:
                path.append(root)
                return True
            
            if getPath(root.left, node) or getPath(root.right, node):
                path.append(root)
                return True
            
            return False
        
        getPath(root, p)
        pathP = set(path)
        path = []
        
        getPath(root, q)
        
        # find the first common anscestor
        for pa in path:
            if pa in pathP:
                return pa
        
        return None
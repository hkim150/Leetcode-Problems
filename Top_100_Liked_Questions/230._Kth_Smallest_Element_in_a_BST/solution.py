# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            k -= 1
            if not k:
                return root.val
            
            root = root.right
            
        raise Expection("answer not found")
        
    
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        # inorder traversal
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        print(inorder(root))
        return inorder(root)[k-1]
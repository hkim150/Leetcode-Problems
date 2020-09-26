# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # for a root element in an inorder list, all the elements to its left is in its left subtree
        # and all the elements to its right is in its right subtree
        # we can traverse in the order of preorder to know the root
        # while using the inorder elements to know the remaining left and right subtree
        def helper(io=inorder):
            if not io:
                return None
            
            v = preorder.pop(0)
            root = TreeNode(v)
            i = io.index(v)
              
            root.left = helper(io[:i])
            root.right = helper(io[i+1:])
            
            return root
        
        return helper()
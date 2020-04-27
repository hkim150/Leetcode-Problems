# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # if either of the nodes is None, return the other one
        # this will return None if both are None
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        # create a new node from the sum and recurse for its children
        newNode = TreeNode(t1.val + t2.val)
        newNode.left = self.mergeTrees(t1.left, t2.left)
        newNode.right = self.mergeTrees(t1.right, t2.right)
        
        return newNode
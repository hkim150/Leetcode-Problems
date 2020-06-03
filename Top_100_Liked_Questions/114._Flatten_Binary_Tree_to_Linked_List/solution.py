# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def flatten_and_return_leaf_node(node):
            if not node.left and not node.right:
                return node
            
            if not node.left:
                return flatten_and_return_leaf_node(node.right)
            
            if not node.right:
                node.left, node.right = None, node.left
                return flatten_and_return_leaf_node(node.right)
            
            left_leaf = flatten_and_return_leaf_node(node.left)
            right_leaf = flatten_and_return_leaf_node(node.right)
            node.left, left_leaf.right, node.right = None, node.right, node.left
            return right_leaf
        
        flatten_and_return_leaf_node(root)
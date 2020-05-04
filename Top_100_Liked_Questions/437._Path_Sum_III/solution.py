# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        ans = [0]
        
        # count the paths with the starting point at the root
        def helper(root, s=sum):
            if not root:
                return
            
            if root.val == s:
                ans[0] += 1
            
            helper(root.left, s - root.val)
            helper(root.right, s - root.val)
        
        # traverse the tree and call the above function for every node
        
        # preorder traversal
#         currNode = root
#         stack = [root]
#         while stack:
#             if currNode:
#                 if currNode.right:
#                     stack.append(currNode.right)
            
#                 helper(currNode)
#                 currNode = currNode.left
            
#             else:
#                 currNode = stack.pop()
        
        # level-order traversal
        queue = [root]
        while queue:
            currNode = queue.pop(0)
            helper(currNode)
            
            if currNode.left:
                queue.append(currNode.left)

            if currNode.right:
                queue.append(currNode.right)
            
        return ans[0]
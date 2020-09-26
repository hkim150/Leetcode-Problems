# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # recursive solution using a helper method
        ans = []
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
        
        helper(root)
        return ans

    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # iterative solution
        ans = []
        stack = []
        
        while True:
            # push self in the stack and go to left child until None
            while root:
                stack.append(root)
                root = root.left

            # pop stack and add the value to the answer array
            if stack:
                root = stack.pop()
            else:
                break

            ans.append(root.val)

            # go to right node and repeat until the stack is empty
            root = root.right
        
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        s = set(to_delete)
        
        def helper(root, parent, isLeftChild):
            if not root:
                return
            
            helper(root.left, root, True)
            helper(root.right, root, False)
            
            if root.val in s:
                if isLeftChild:
                    parent.left = None
                else:
                    parent.right = None
            
                if root.left:
                    ans.append(root.left)

                if root.right:
                    ans.append(root.right)
        
        if root.val not in s:
            ans.append(root)
        
        dummyRoot = TreeNode()
        dummyRoot.left = root
        
        helper(root, dummyRoot, True)
        del dummyRoot
            
        return ans
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # iterative level order traversal
        q = [(root, 0)]
        ans = []
        while q:
            node, lvl = q.pop(0)
            if not node:
                continue
                
            if len(ans) < lvl+1:
                ans.append([node.val])
            else:
                ans[lvl].append(node.val)
            q.append((node.left, lvl+1))
            q.append((node.right, lvl+1))
        
        return ans
    
    
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        # recursive level order traversal
        ans = []
        def helper(node, lvl):
            if not node:
                return
            
            if len(ans) == lvl:
                ans.append([])
            
            ans[lvl].append(node.val)
            helper(node.left, lvl+1)
            helper(node.right, lvl+1)
        
        helper(root, 0)
        return ans
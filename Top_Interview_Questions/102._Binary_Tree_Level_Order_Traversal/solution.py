# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # we can use queue to traverse in level order
        # we also need to keep track of the level so that we can divide each level into different list
        curr_lvl = 0
        q = [(root, curr_lvl)]
        ans = [[]]
        while q:
            node, lvl = q.pop(0)
            if node:
                if curr_lvl == lvl:
                    ans[-1].append(node.val)
                else:
                    ans.append([node.val])
                    curr_lvl += 1
                
                q.append((node.left, lvl+1))
                q.append((node.right, lvl+1))
            
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
                                
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # recursive postorder traversal
        preorder_idx = [0]
        
        def findNodeAndConnectChildren(inorder_left, inorder_right):
            if inorder_left >= inorder_right:
                return None
            
            preorder_val = preorder[preorder_idx[0]]
            preorder_idx[0] += 1
            
            i_idx = None
            for i in range(inorder_left, inorder_right):
                if inorder[i] == preorder_val:
                    i_idx = i
                    break
            
            if i_idx is None:
                raise Exception("{} not found in inorder {}".format(preorder_val, inorder[inorder_left:inorder_right]))
                
            left = findNodeAndConnectChildren(inorder_left, i_idx)
            right = findNodeAndConnectChildren(i_idx+1, inorder_right)
            return TreeNode(preorder_val, left, right)
        
        return findNodeAndConnectChildren(0, len(inorder))
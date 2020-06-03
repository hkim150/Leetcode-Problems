# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # recursive dp - O(n)
        def maxRob(node):
            if not node:
                return 0, 0
            
            cannotRob_left, canRob_left = maxRob(node.left)
            cannotRob_right, canRob_right = maxRob(node.right)
            
            noRob = canRob_left + canRob_right
            rob = max(noRob, node.val + cannotRob_left + cannotRob_right)
            
            return noRob, rob
        
        return maxRob(root)[1]
            
    
    
    def rob3(self, root: TreeNode) -> int:
        # iterative dp
        arr = []
        def treeToArr(node, i):
            if not node:
                return
            
            if len(arr) <= i:
                arr.extend([None] * (i - len(arr) + 1))
                
            arr[i] = node.val
            
            treeToArr(node.left, i*2+1)
            treeToArr(node.right, i*2+2)
        
        treeToArr(root, 0)
        
        mem = [[0,0] for _ in range(len(arr)+1)]
        for i in range(len(arr)-1, -1, -1):
            if arr[i] is None:
                continue
            
            leftIdx = min(i*2+1, len(arr))
            rightIdx = min(i*2+2, len(arr))
            
            mem[i][0] = mem[leftIdx][1] + mem[rightIdx][1]
            mem[i][1] = max(mem[i][0], arr[i] + mem[leftIdx][0] + mem[rightIdx][0])

        return mem[0][1]
    
    
    def rob2(self, root: TreeNode) -> int:
        # recursive dp - double recursive
        def maxRob(node, canRob):
            if not node:
                return 0
            
            if canRob:
                rob = node.val + maxRob(node.left, False) + maxRob(node.right, False)
                noRob = maxRob(node.left, True) + maxRob(node.right, True)
                return max(rob, noRob)
            else:
                return maxRob(node.left, True) + maxRob(node.right, True)
        
        return maxRob(root, True)
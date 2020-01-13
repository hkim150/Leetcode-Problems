# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # get the middle node, divide into left half and right half
        # left child is left chunk's middle and right child is right chunk's middle
        # this can go on in recursive fashion

        if not nums:
            return None

        mid = len(nums) // 2
        newNode = TreeNode(nums[mid])
        newNode.left = self.sortedArrayToBST(nums[:mid])
        newNode.right = self.sortedArrayToBST(nums[mid+1:])

        return newNode
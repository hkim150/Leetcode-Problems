class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 1:
            return 0
        
        nums.append(float('-inf'))
        
        def helper(i, j):
            if i >= len(nums):
                return 0
            
            if nums[i] > nums[j]:
                return max(1 + helper(i+1, i), helper(i+1, j))
            
            else:
                return helper(i+1, j)
        
        return helper(0,-1)
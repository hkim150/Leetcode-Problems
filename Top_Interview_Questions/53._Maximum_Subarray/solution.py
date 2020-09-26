class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum
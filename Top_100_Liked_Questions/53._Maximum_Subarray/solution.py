class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we can keep track of the max sum seen so far while looping
        # if the current sum is negetive start fresh
        # because it will only bring down the combined sum
        # if positive, keep it and continue
        currSum = maxSum = float(-inf)
        
        for n in nums:
            if currSum > 0:
                currSum += n
            else:
                currSum = n
                
            maxSum = max(currSum, maxSum)
        
        return maxSum
class Solution:
    def rob(self, nums: List[int]) -> int:
        # constant space from memoization
        curr_max = 0
        prev_max = 0
        
        for i in range(len(nums)-1, -1, -1):
            curr_max, prev_max = max(nums[i] + prev_max, curr_max), curr_max
        
        return curr_max
        
    
    def rob3(self, nums: List[int]) -> int:
        # memoization from recursive
        maxRob = [[0,0] for _ in range(len(nums)+1)]
        
        for i in range(len(nums)-1, -1, -1):
            maxRob[i][0] = max(nums[i] + maxRob[i+1][1], maxRob[i+1][0])
            maxRob[i][1] = maxRob[i+1][0]
        
        return maxRob[0][0]
    
    
    def rob2(self, nums: List[int]) -> int:
        # dp recursive
        def maxRob(i, canRob):
            if i >= len(nums):
                return 0
            
            rob = nums[i] + maxRob(i+1, False) if canRob else 0
            return max(rob, maxRob(i+1, True))
            
        return maxRob(0, True)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # iterative dp - this works as the max sum is capped at 1000
        N = 1000
        if S > N:
            return 0
        
        mem = [[0] * (2*N+1) for _ in range(len(nums)+1)]
        mem[len(nums)][S+N] = 1
            
        for i in range(len(nums)-1, -1, -1):
            for j in range(2*N+1):
                add = mem[i+1][j - nums[i]] if j - nums[i] >= 0 else 0
                sub = mem[i+1][j + nums[i]] if j + nums[i] <= 2*N else 0
                mem[i][j] = add + sub
        
        return mem[0][N]
    
    
    def findTargetSumWays3(self, nums: List[int], S: int) -> int:
        # use index instead of subarray copy
        def helper(i, target):
            if i == len(nums):
                return 1 if target == 0 else 0
            
            return helper(i+1, target - nums[i]) + helper(i+1, target + nums[i])
        return helper(0, S)
    
    
    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        #recursive dp
        if not nums:
            return 1 if S == 0 else 0
        
        return self.findTargetSumWays(nums[1:], S-nums[0]) + self.findTargetSumWays(nums[1:], S+nums[0])

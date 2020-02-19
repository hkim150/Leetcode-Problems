class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # one pass greedy solution
        # all we need to keep track is whether the current value
        # is equal or bigger than distance to the last seen viable position
        lastGood = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastGood:
                lastGood = i
        
        return lastGood == 0
    
    def canJump3(self, nums: List[int]) -> bool:
        # dp with memoization
        mem = [False] * len(nums)
        mem[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i + j <= len(nums)-1:
                    if mem[i+j]:
                        mem[i] = True
        
        return mem[0]
    
    def canJump2(self, nums: List[int]) -> bool:
        # dp with recursion
        def helper(i):
            if i == len(nums)-1:
                return True
            
            for j in range(nums[i], 0, -1):
                if i + j <= len(nums)-1:
                    if helper(i+j):
                        return True
            
            return False
        
        return helper(0)
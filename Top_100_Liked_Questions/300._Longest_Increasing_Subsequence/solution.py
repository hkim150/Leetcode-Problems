class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        mem = [0] * (len(nums))
        mem[0] = 1
        maxAns = 1
        for i in range(1, len(nums)):
            maxVal = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxVal = max(maxVal, mem[j])    
            
            mem[i] = maxVal + 1
            maxAns = max(maxAns, mem[i])
        
        return maxAns
    
    
    def lengthOfLIS3(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.insert(0, float('-inf'))
        mem = [[0] * len(nums) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[i] > nums[j]:
                    mem[i][j] = max(mem[i+1][j], 1 + mem[i+1][i])
                else:
                    mem[i][j] = mem[i+1][j]
                    
        return mem[1][0]
    
    
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # recursive dp
        nums.insert(0, float('-inf'))
        
        def LIS(i, j):
            if i >= len(nums):
                return 0
            
            if nums[i] > nums[j]:
                return max(LIS(i+1, j), 1 + LIS(i+1, i))
            else:
                return LIS(i+1, j)
        
        return LIS(1,0)
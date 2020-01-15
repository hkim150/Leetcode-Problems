class Solution:
    def rob(self, nums: List[int]) -> int:
        # given a choice of to rob or to not rob for each day,
        # we can use dynamic programming
        
        # naive solution using recursion
        def helper(i=0):
            if i >= len(nums):
                return 0
            
            return max(helper(i+1), nums[i] + helper(i+2))
        
        #return helper()
    
        # with memoization we can improve the code in one pass
        mem = [0] * (len(nums) + 2)
        for i in range(len(nums)-1, -1, -1):
            mem[i] = max(mem[i+1], nums[i] + mem[i+2])
        
        return mem[0]
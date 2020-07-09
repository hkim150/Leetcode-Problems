class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy method
        # we only need to store the first good position because if we can jump to second good or anything after the first good position, we can also land on the first good one by taking a shorter jump
        fgp = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= fgp:
                fgp = i
        
        return fgp == 0
    
    
    def canJump3(self, nums: List[int]) -> bool:
        # iterative dp
        mem = [False] * len(nums)
        mem[-1] = True
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if mem[min(i+j, len(nums)-1)]:
                    mem[i] = True
                    break

        return mem[0]
    
    
    def canJump2(self, nums: List[int]) -> bool:
        # recursive dp
        def helper(i):
            if i >= len(nums)-1:
                return True
            
            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    return True
            
            return False
        
        return helper(0)
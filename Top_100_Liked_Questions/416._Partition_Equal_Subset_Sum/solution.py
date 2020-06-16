class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        
        if sumNums % 2 == 1:
            return False

        mem = {}
        def hasSubsetSum(i, s):
            if s == 0:
                return True
            
            if s < 0:
                return False
            
            if i >= len(nums):
                return False
            
            include = mem[(i+1, s-nums[i])] if (i+1, s-nums[i]) in mem else hasSubsetSum(i+1, s-nums[i])
            
            if include:
                mem[(i+1, s-nums[i])] = True
                return True
            
            exclude = mem[(i+1, s)] if (i+1, s) in mem else hasSubsetSum(i+1, s)
            if exclude:
                mem[(i+1, s)] = True
                return True
            
            mem[(i+1, s)] = False
            return False
            
        return hasSubsetSum(0, sumNums/2)
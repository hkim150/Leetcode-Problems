class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # swap method
        ans = []
        
        def backtrack(first=0):
            if first == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        backtrack()
        
        return ans
    
    
    def permute2(self, nums: List[int]) -> List[List[int]]:
        # decreasing pool method
        ans = []

        def helper(remainingPool, currList=[]):
            if not remainingPool:
                ans.append(currList)
                return
            
            for i,v in enumerate(remainingPool):
                copyRemainingPool = remainingPool[:]
                del copyRemainingPool[i]
                helper(copyRemainingPool, currList + [v])
        
        helper(nums)
        
        return ans
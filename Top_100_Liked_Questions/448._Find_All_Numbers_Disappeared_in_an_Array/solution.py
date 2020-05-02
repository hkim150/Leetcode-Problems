class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(1) space solution
        # use the number as index of the list and set the value of the index as negative
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] *= -1
        
        ans = []
        for i,v in enumerate(nums):
            if v > 0:
                ans.append(i+1)
                
        return ans
            
            
    def findDisappearedNumbersHashMap(self, nums: List[int]) -> List[int]:
        mem = [False] * len(nums)
        ans = []
        
        for n in nums:
            mem[n-1] = True
            
        for i,v in enumerate(mem):
            if v == 0:
                ans.append(i+1)
        
        return ans
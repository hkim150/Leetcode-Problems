class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        umn = float('inf')
        umx = float('-inf')
        
        # find minimum and maximum unordered element
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                umx = max(umx, nums[i])
                umn = min(umn, nums[i+1])
        
        # find the index where the minimum unordered element is supposed to be
        l,r = len(nums), -1
        for i in range(len(nums)):
            if nums[i] > umn:
                l = i
                break
                
        # find the index where the maximum unordered element is supposed to be
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < umx:
                r = i
                break
        
        return max(r - l + 1, 0)
        
    
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        # naive solution - sort and compare
        sorted_nums = sorted(nums)
        l,r = len(nums), -1
        
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                l = i
                break
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != sorted_nums[i]:
                r = i
                break
        
        return max(r - l + 1, 0)
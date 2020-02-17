class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # find the first index
        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = max(l+1, m)
            else:
                r = m
        
        ans = [-1, -1]
        if nums[l] == target:
            ans[0] = l
        else:
            return ans
    
        # find the last index
        r = len(nums) - 1
        
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] <= target:
                l = m
            else:
                r = min(r-1, m)
        
        ans[1] = l
        
        return ans
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        cumul = 1
        for i in range(len(nums)-1):
            cumul *= nums[i]
            ans[i+1] *= cumul
        
        cumul = 1
        for i in range(len(nums)-1, 0, -1):
            cumul *= nums[i]
            ans[i-1] *= cumul
        
        return ans
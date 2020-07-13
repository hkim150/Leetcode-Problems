class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = mn = mx = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            mx, mn = max(n, mn*n, mx*n), min(n, mn*n, mx*n)
            ans = max(ans, mx)
        
        return ans
    
    
    def maxProduct2(self, nums: List[int]) -> int:
        # brute force
        ans = float('-inf')
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]
                ans = max(ans, curr)
        
        return ans
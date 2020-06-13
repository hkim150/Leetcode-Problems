class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # using hash and seeking for diff
        d = {0:1}
        curr_sum = 0
        sum_minus_k = 0
        count = 0
        for num in nums:
            curr_sum += num
            sum_minus_k = curr_sum - k
            if sum_minus_k in d:
                count += d[sum_minus_k]
            d[curr_sum] = d.get(curr_sum, 0) + 1
        return count
    
    
    def subarraySum2(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)-1, -1, -1):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    ans += 1
        
        return ans
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # choose two and check if complement exists in the hash
        ans = []
        found = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    mx = max(nums[i], nums[j], complement)
                    mn = min(nums[i], nums[j], complement)
                    if (mn, mx) not in found:
                        ans.append([nums[i], nums[j], complement])
                        found.add((mn, mx))
                
                seen.add(nums[j])
        
        return ans
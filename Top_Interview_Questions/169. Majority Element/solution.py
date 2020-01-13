class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # keep track of the number of occurrances of each element
        d = {}
        half = len(nums) // 2
        for n in nums:
            if n in d:
                d[n] += 1
                if d[n] > half:
                    return n
            else:
                d[n] = 1
        
        # not found, error
        return -1
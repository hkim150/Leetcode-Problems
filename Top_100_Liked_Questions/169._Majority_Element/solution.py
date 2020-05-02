class Solution:
    def majorityElementHashMap(self, nums: List[int]) -> int:
        # hashMap
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        
        return candidate
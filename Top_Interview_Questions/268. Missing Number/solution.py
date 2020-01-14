class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR'ing oneself results in zero
        # we can use this property of XOR to find out the number without a pair
        ans = len(nums)
        
        for i,n in enumerate(nums):
            ans ^= (i ^ n)
        
        return ans
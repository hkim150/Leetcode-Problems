class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor'ing oneself results in 0
        # thus xoring everything will leave the one number that does not have a pair
        ans = 0;
        for n in nums:
            ans ^= n
        
        return ans
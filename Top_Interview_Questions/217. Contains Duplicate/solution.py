class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # we can use hash function to keep track of seen numbers
        d = {}
        
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = True
        
        return False
    
        # one liner using built in hash set
        # return len(nums) != len(set(nums))
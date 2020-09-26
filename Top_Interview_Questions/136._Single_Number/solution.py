class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # record the number of occurancces in a dictionary
        d = {}
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        # find the number that occurred only once in the dictionary
        for k,v in d.items():
            if v == 1:
                return k
            
        
        # XOR'ing oneself returns zero and XOR'ing with zero returns oneself
        # Thus, XOR'ing all numbers will leave us with the number that occurred only once
        a = 0
        
        for n in nums:
            a ^= n
        
        return a
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we can iteratively choose a number for the spot
        # and then recursively repeat the process for the next spot
        # by choosing among the remaining numbers
        ans = []
        
        def helper(rem, perm=[]):
            if not rem:
                ans.append(perm)
                
            for i,v in enumerate(rem):
                newRem = rem[:]
                del newRem[i]
                helper(newRem, perm + [v])
        
        helper(nums)
        
        return ans
        
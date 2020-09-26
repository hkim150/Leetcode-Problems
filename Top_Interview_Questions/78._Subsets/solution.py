class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
	# for every element, we can either include or not include in a subset
	# we can exhaustively recurse over the elements
        ans = []
        
        def helper(rem=nums, subset=[]):
            if not rem:
                ans.append(subset)
                return
            
            remCopy = rem[:]
            v = remCopy[0]
            del remCopy[0]
            helper(remCopy, subset + [v])
            helper(remCopy, subset)
        
        helper()
        return ans

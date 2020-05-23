class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # cascading method
        ans = [[]]
        for n in nums:
            for subset in ans[:]:
                ans.append(subset + [n])
        
        return ans
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # using binary
        ans = []
        for dec in range(2**len(nums)):
            b = bin(dec)[2:]
            s = ('0' * (len(nums) - len(b))) + b
            subset = []
            for i,v in enumerate(s):
                if v == '1':
                    subset.append(nums[i])
            ans.append(subset)
        
        return ans
                    
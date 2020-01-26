class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        # product except self is product of numbers on its left and right
        leng = len(nums)
        l = [1] * leng
        r = [1] * leng
        ans = [0] * leng
        
        for i in range(1,leng):
            l[i] = l[i-1] * nums[i-1]
        
        for i in range(leng-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]
        
        for i in range(leng):
            ans[i] = l[i] * r[i]
        
        return ans
    
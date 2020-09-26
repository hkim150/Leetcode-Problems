class Solution:
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass algorithm
        # store the number of each color and overwrite
        cnt = [0,0,0]
        for n in nums:
            cnt[n] += 1
        
        cumul = 0
        for i in range(3):
            for j in range(cumul, cumul + cnt[i]):
                nums[j] = i
                
            cumul += cnt[i]
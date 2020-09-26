class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer method
        l = 0
        r = 1
        leng = len(nums)
        
        while r < leng:
            lv = nums[l]
            rv = nums[r]
            if lv == 0 and rv == 0:
                r += 1
            elif lv == 0 and rv != 0:
                #swap the values of l and r
                nums[l] = rv
                nums[r] = lv
                
                l += 1
                r += 1  
            else:
                l += 1
                r += 1
    
    def moveZeroes2(self, nums: List[int]) -> None:
        # memoization method
        
        # fillout the non-zeros from the beginning of the list
        leng = len(nums)
        num_none_zero = 0
        for i in range(leng):
            if nums[i] != 0:
                nums[num_none_zero] = nums[i]
                num_none_zero += 1
        
        # fillout the remaining space with zeroes
        for i in range(num_none_zero, leng):
            nums[i] = 0
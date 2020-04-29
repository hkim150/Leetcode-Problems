class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep a pointer to the leftmomst zero and
        # swap with the non-zero value
        lmz = 0;
        for i,v in enumerate(nums):
            if v != 0:
                nums[i], nums[lmz], lmz = 0, v, lmz+1
    
    
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # get all non-zero numbers
        nonZeros = list(filter(lambda n: n != 0, nums))
        
        # fillout the array with the non-zero numbers
        # and set the remaining values to zero
        for i in range(len(nums)):
            nums[i] = nonZeros[i] if i < len(nonZeros) else 0
    
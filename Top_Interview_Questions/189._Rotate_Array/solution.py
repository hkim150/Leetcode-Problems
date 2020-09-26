class Solution:
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force
        l = len(nums)
        
        def shiftRight():
            hold = nums[l-1]

            for i in range(l-1, 0, -1):
                nums[i] = nums[i-1]

            nums[0] = hold
        
        def shiftLeft():
            hold = nums[0]
            
            for i in range(l-1):
                nums[i] = nums[i+1]
                
            nums[l-1] = hold
        
        j = k % l
        
        if j <= l // 2:
            for _ in range(j):
                shiftRight()
        else:
            for _ in range(l - j):
                shiftLeft()
                
                
    def rotate3(self, nums: List[int], k: int) -> None:
        # store the array and copy values from it
        copy = nums[:]
        
        l = len(nums)
        j = k % l
        
        for i in range(j):
            nums[i] = copy[l - j + i]
        
        for i in range(l-j):
            nums[j + i] = copy[i]
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        # using reverse function
        l = len(nums)
        
        def reverse(l, r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                
                l += 1
                r -= 1
        
        j = k % l
        
        reverse(0, l-1)
        reverse(0, j-1)
        reverse(j, l-1)
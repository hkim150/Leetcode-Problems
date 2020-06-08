class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0 = pcurr = 0
        p2 = len(nums)-1
        
        while pcurr <= p2:
            if nums[pcurr] == 0:
                nums[pcurr], nums[p0] = nums[p0], nums[pcurr]
                p0 += 1
                pcurr += 1
            elif nums[pcurr] == 2:
                nums[pcurr], nums[p2] = nums[p2], nums[pcurr]
                p2 -= 1
            else:
                pcurr += 1
    
    
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass overwrite
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        
        
        i = 0
        while (i < len(nums)):
            for j in range(len(counts)):
                for _ in range(counts[j]):
                    nums[i] = j
                    i += 1
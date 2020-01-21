class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # by filling up from the back, we can avoid shifting numbers
        
        l = len(nums1)
        
        while m > 0 and n > 0:
            n1 = nums1[m-1]
            n2 = nums2[n-1]

            if n1 > n2:
                nums1[l-1] = n1
                m -= 1
            else:
                nums1[l-1] = n2
                n -= 1

            l -= 1
        
        while n > 0:
            nums1[l-1] = nums2[n-1]
            n -= 1
            l -= 1
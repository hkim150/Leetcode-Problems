class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # we can use the hash map to store the number of occurrances of each number
        d = {}
        ans = []
        
        for n in nums1:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        # we can subtract the occurances of each matching number while appending the number to the answer list
        for n in nums2:
            if n in d:
                if d[n] > 0:
                    d[n] -= 1
                    ans.append(n)
                else:
                    del d[n]
        
        return ans
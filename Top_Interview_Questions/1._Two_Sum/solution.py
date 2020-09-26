class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # we can use the hash map to search a number in constant time
        d = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in d:
                return [i, d[complement]]
            else:
                d[n] = i
        
        sys.exit("twoSum solution not found")
class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # nlog(n)
        return sorted(nums)[-k]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlog(k)
        return heapq.nlargest(k, nums)[-1]
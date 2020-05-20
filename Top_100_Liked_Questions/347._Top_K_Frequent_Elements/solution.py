class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the number of occurances in O(n)
        # max heapify the occurences in O(n)
        # get the k largest elements in O(klog(n))
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
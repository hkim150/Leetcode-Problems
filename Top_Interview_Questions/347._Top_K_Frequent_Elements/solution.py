class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        pairs = [(ke,v) for ke,v in count.items()]
        return [ke for ke,_ in sorted(pairs, key=lambda x: -x[1])[:k]]
        
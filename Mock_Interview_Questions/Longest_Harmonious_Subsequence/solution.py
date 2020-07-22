class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # count the number of elements
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        ans = 0
        # for every count c[i], get max c[i] + c[i+1]
        for k,v in count.items():
            if k+1 in count:
                ans = max(ans, v + count[k+1])
        
        return ans
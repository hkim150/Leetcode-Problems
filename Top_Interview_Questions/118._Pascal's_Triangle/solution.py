class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        prev = [1]
        ans = [prev]
        
        for _ in range(numRows-1):
            l = len(prev)
            curr = [1] * (l+1)

            for i in range(l-1):
                curr[i+1] = prev[i] + prev[i+1]

            ans.append(curr)
            prev = curr
        
        return ans
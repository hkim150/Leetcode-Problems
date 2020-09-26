class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        
        for intv in intervals:
            if intv[0] <= ans[-1][1]:
                ans[-1][1] = max(intv[1], ans[-1][1])
            else:
                ans.append(intv)
        
        return ans
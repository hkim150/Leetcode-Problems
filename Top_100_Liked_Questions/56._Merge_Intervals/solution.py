class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        
        for s,e in intervals:
            if s > ans[-1][1]:
                ans.append([s,e])
            else:
                ans[-1][1] = max(e, ans[-1][1])
        
        return ans
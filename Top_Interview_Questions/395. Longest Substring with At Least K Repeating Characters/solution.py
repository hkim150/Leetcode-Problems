class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # count the occurances of each unique letter
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        
        # we have to avoid including letters that occur fewer than k times in s
        # recurse over those segments in between unqualified letters
        startIdx = 0
        maxSeen = 0
        for i,ch in enumerate(s):
            if d[ch] < k:
                maxSeen = max(maxSeen, self.longestSubstring(s[startIdx:i], k))
                startIdx = i+1
        
        if startIdx == 0:
            return len(s)
        
        return max(maxSeen, self.longestSubstring(s[startIdx:], k))
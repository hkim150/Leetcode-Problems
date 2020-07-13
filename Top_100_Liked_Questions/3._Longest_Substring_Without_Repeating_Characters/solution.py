class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window method O(n)
        # have pointers l and r
        # and a hash map for the latest index for the letter
        ans = l = 0
        hashMap = {}
        
        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(hashMap[s[r]] + 1, l)
            ans = max(ans, r - l + 1)
            hashMap[s[r]] = r
        
        return ans
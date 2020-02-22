class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        hashSet = set()
        ans = 0
        
        while l < len(s) and r < len(s):
            if s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            else:
                hashSet.add(s[r])
                r += 1
                ans = max(ans, r - l)
        
        return ans
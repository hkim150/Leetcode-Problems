class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        
        # we can use the hash map to store the index of the characters
        # if it is a seen character, then make it a large number
        # and return the minimum index if there is one other than the large numbers
        d = {}
        
        for i,ch in enumerate(s):
            if ch in d:
                d[ch] = float('inf')
            else:
                d[ch] = i
        
        ans = min(d.values())
        if ans == float('inf'):
            return -1
        
        return ans
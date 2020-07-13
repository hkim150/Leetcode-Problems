class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand around the center
        def expand(l,r):
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l, r = l-1, r+1
            
            return r - l - 1
            
        start = end = 0
        for i in range(len(s)):
            l1 = expand(i, i)
            l2 = expand(i, i+1)
            l = max(l1, l2)
            if l > end - start:
                start = i - (l-1)//2
                end = i + l//2
        
        return s[start:end+1]
        
        
    def longestPalindrome2(self, s: str) -> str:
        # dp with memoization
        ans = 1 if len(s) else 0
        mem = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            mem[i][i] = True
            if i > 0:
                mem[i][i-1] = True

        l = r = 0
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                mem[i][j] = s[i] == s[j] and mem[i+1][j-1]
                if mem[i][j]:
                    if j - i + 1 > ans:
                        ans = j - i + 1
                        l, r = i, j

        return s[l:r+1]
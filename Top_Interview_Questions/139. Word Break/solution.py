class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming with memoization
        l = len(s)
        mem = [[False] * (l+1) for _ in range(l+1)]
        
        for end in range(l+1):
            mem[l][end] = True
        
        for start in range(l):
            mem[start][l] = s[start:] in wordDict

        for start in range(l-1, -1, -1):
            for end in range(l-1, -1, -1):
                if s[start:end+1] in wordDict:
                    mem[start][end] = mem[end+1][end+1] or mem[start][end+1]
                else:
                    mem[start][end] = mem[start][end+1]
        
        return mem[0][0]
    
    
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming with recursion
        def helper(start, end):
            if start >= len(s):
                return True
            
            if end >= len(s):
                return s[start:] in wordDict
            
            if s[start:end+1] in wordDict:
                return helper(end+1, end+1) or helper(start, end+1)
            else:
                return helper(start, end+1)
        
        return helper(0, 0)
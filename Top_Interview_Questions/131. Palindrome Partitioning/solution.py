class Solution:
    def partition(self, s: str) -> List[List[str]]:
        leng = len(s)
        
        # get the memoization of dp palindrome
        memPal = [[False] * leng for _ in range(leng)]
        memPal[leng-1][leng-1] = True
        
        for i in range(leng-1):
            memPal[i][i] = memPal[i+1][i] = True
        
        for l in range(leng-2, -1, -1):
            for r in range(l+1, leng):
                memPal[l][r] = s[l] == s[r] and memPal[l+1][r-1]
                
        ans = []
        # dp possible break point
        def breakPoint(start, end, lst=[]):
            if end == leng-1:
                if memPal[start][end]:
                    lst.append(s[start:end+1])
                    ans.append(lst)
                return
            
            if memPal[start][end]:
                breakPoint(end+1, end+1, lst+[s[start:end+1]])
            
            breakPoint(start, end+1, lst)
        
        breakPoint(0, 0)
        
        return ans
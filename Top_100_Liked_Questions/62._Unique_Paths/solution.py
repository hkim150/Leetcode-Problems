from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))
        
    
    def uniquePaths2(self, m: int, n: int) -> int:
        mem = [[1] * n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
        
        return mem[-1][-1]
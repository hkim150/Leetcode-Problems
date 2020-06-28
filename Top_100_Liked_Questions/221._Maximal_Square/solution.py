class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp with memoization - O(mn) time,  O(n)space
        numRow = len(matrix)
        numCol = len(matrix[0]) if numRow >= 1 else 0
        
        if not numRow or not numCol:
            return 0;
        
        mem = [0] * (numCol+1)
        ms = 0
        for j in range(numCol):
            if matrix[-1][j] == "1":
                ms = 1
                mem[j] = 1
            
        for i in range(numRow-2, -1, -1):
            mem2 = [0] * (numCol+1)
            for j in range(numCol-1, -1, -1):
                mem2[j] = min(mem[j], mem[j+1], mem2[j+1]) + 1 if matrix[i][j] == "1" else 0
                ms = max(ms, mem2[j])
                
            mem = mem2
        
        return ms**2
    
    
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        # dp with memoization - O(mn) time,  O(mn)space
        numRow = len(matrix)
        numCol = len(matrix[0]) if numRow >= 1 else 0
        
        mem = [[0]*(numCol+1) for _ in range(numRow+1)]
        ms = 0
        for i in range(numRow-1, -1, -1):
            for j in range(numCol-1, -1, -1):
                mem[i][j] = min(mem[i+1][j], mem[i][j+1], mem[i+1][j+1]) + 1 if matrix[i][j] == "1" else 0
                ms = max(ms, mem[i][j])
        
        return ms**2
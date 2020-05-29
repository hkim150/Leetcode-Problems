class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp with memoization from recursive solution
        # create a memoization grid with a padding on the right and bottom
        mem = [[0] * (len(grid[0])+1) for _ in range(len(grid)+1)]
        
        # pad the overflowing regions with max number
        for row in mem:
            row[-1] = float('inf')
            
        for colIdx in range(len(mem[0])):
            mem[-1][colIdx] = float('inf')
        
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[0])-1, -1, -1):
                if row == len(grid)-1 and col == len(grid[0])-1:
                    mem[row][col] = grid[row][col]
                    continue
                
                mem[row][col] = grid[row][col] + min(mem[row+1][col], mem[row][col+1])
        
        return mem[0][0]
                
    
    def minPathSum2(self, grid: List[List[int]]) -> int:
        # recursive brute force
        def helper(row, col):
            if row == len(grid)-1 and col == len(grid[0])-1:
                return grid[row][col]
            
            down = helper(row+1, col) if row < len(grid)-1 else float('inf')
            right = helper(row, col+1) if col < len(grid[0])-1 else float('inf')
            
            return grid[row][col] + min(down, right)
        
        return helper(0,0)
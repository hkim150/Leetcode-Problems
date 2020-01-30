class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we can use dynamic programming with memoization
        grid = [[0] * m for _ in range(n)]
        
        for row in range(n):
            for col in range(m):
                if row == 0 or col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        
        return grid[n-1][m-1]
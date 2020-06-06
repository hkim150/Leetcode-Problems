class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_row = len(grid)
        if num_row < 1:
            return 0
        
        num_col = len(grid[0])
        if num_col < 1:
            return 0
        
        def dfs_fill(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                grid[r][c] = '2'
                if c + 1 < num_col and grid[r][c+1] == '1':
                    stack.append((r, c+1))
                if r + 1 < num_row and grid[r+1][c] == '1':
                    stack.append((r+1, c))
                if c > 0 and grid[r][c-1] == '1':
                    stack.append((r, c-1))
                if r > 0 and grid[r-1][c] == '1':
                    stack.append((r-1, c))
                    
        def bfs_fill(row, col):
            q = [(row, col)]
            grid[row][col] = '2'
            while q:
                r, c = q.pop(0)
                if c + 1 < num_col and grid[r][c+1] == '1':
                    q.append((r, c+1))
                    grid[r][c+1] = '2'
                if r + 1 < num_row and grid[r+1][c] == '1':
                    q.append((r+1, c))
                    grid[r+1][c] = '2'
                if c > 0 and grid[r][c-1] == '1':
                    q.append((r, c-1))
                    grid[r][c-1] = '2'
                if r > 0 and grid[r-1][c] == '1':
                    q.append((r-1, c))
                    grid[r-1][c] = '2'
        
        num_islands = 0
        # loop through the grid and find unseen land, a.k.a '1'
        for r in range(num_row):
            for c in range(num_col):
                if grid[r][c] == '1':
                    # get connected tiles and mark them '2'
                    #dfs_fill(r,c)
                    bfs_fill(r,c)
                    
                    # increment the number of lands found and repeat
                    num_islands += 1
        
        return num_islands
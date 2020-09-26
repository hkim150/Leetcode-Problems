class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for every element, if num is 1, increment island count
        # and mark itself and its connected neighbors 2
        if not grid:
            return 0
        
        nRows = len(grid)
        nCols = len(grid[0])
        ans = 0
        
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == '1':
                    q = [(r,c)]
                    while q:
                        rr,cc = q.pop(0)
                        if grid[rr][cc] == '1':
                            if cc < nCols-1:
                                q.append((rr, cc+1))
                            if rr < nRows-1:
                                q.append((rr+1,cc))
                            if cc > 0:
                                q.append((rr, cc-1))
                            if rr > 0:
                                q.append((rr-1, cc))
                            grid[rr][cc] = '2'
                    ans += 1
        
        return ans
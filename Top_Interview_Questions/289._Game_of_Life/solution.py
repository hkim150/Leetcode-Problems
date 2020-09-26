class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        numCol = len(board[0])
        
        copy = []
        for row in board:
            copy.append(row[:])
        
        def getNumLiveNeighbor(row, col):
            num = 0
            
            # top left
            if row > 0 and col > 0:
                num += copy[row-1][col-1]
            
            # top
            if row > 0:
                num += copy[row-1][col]
            
            # top right
            if row > 0 and col+1 < numCol:
                num += copy[row-1][col+1]
            
            # left
            if col > 0:
                num += copy[row][col-1]
            
            # right
            if col+1 < numCol:
                num += copy[row][col+1]
            
            # bottom left
            if row+1 < numRow and col > 0:
                num += copy[row+1][col-1]
            
            # bottom
            if row+1 < numRow:
                num += copy[row+1][col]
            
            # bottom right
            if row+1 < numRow and col+1 < numCol:
                num += copy[row+1][col+1]
                
            return num
            
        for r in range(numRow):
            for c in range(numCol):
                n = getNumLiveNeighbor(r,c)
                
                if copy[r][c]:
                    if n <= 1 or n >= 4:
                        board[r][c] = 0
                else:
                    if n == 3:
                        board[r][c] = 1
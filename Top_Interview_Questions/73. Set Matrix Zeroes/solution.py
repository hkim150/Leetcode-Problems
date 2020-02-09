class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        nRows = len(matrix)
        if nRows < 1:
            return
        
        nCols = len(matrix[0])
        
        firstRow = firstCol = False
        for r in range(nRows):
            for c in range(nCols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
                    if r == 0:
                        firstRow = True
                    if c == 0:
                        firstCol = True
        
        for c in range(1,nCols):
            if matrix[0][c] == 0:
                for r in range(1,nRows):
                    matrix[r][c] = 0
        
        for r in range(1,nRows):
            if matrix[r][0] == 0:
                for c in range(1,nCols):
                    matrix[r][c] = 0
        
        if firstRow:
            for c in range(nCols):
                matrix[0][c] = 0
        
        if firstCol:
            for r in range(nRows):
                matrix[r][0] = 0
        
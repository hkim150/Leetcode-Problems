class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nRows = len(matrix)
        if nRows < 1:
            return False
        
        nCols = len(matrix[0])
        if nCols < 1:
            return False
        
        r,c = nRows-1, 0
        while r >= 0 and c <= nCols-1:
            print(matrix[r][c])
            if matrix[r][c] < target:
                c += 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                return True
        
        return False
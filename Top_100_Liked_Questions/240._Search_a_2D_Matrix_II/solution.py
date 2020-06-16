class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Search space reduction method
        numRow = len(matrix)
        if not numRow:
            return False
        
        numCol = len(matrix[0])
        if not numCol:
            return False
        
        r, c = numRow-1, 0
        while r >= 0 and c <= numCol-1:
            if matrix[r][c] < target:
                c += 1
            elif matrix[r][c] > target:
                r -= 1
            else:
                return True
        
        return False
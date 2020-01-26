class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we can first transpose and then reverse the row
        if not matrix:
            return
        
        l = len(matrix)
        if l <= 1:
            return
        
        for row in range(l):
            for col in range(row, l):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(l):
            matrix[row].reverse()
class Solution:
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose and reverse
        l = len(matrix)
        if l < 2:
            return
        
        for row in range(l-1):
            for col in range(row+1,l):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in matrix:
            row.reverse()
        
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate swap
        l = len(matrix)
        if l < 2:
            return
        
        for row in range(l//2):
            for col in range(row, l-row-1):
                i = []
                r, c = row, col
                for _ in range(4):
                    i.append((r,c))
                    r, c = c, l-r-1
                
                matrix[i[1][0]][i[1][1]], matrix[i[2][0]][i[2][1]], matrix[i[3][0]][i[3][1]], matrix[i[0][0]][i[0][1]] = matrix[i[0][0]][i[0][1]], matrix[i[1][0]][i[1][1]], matrix[i[2][0]][i[2][1]], matrix[i[3][0]][i[3][1]]
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            tmp = [False] * 9
            for col in row:
                if col == ".":
                    continue
                v = int(col) - 1
                if tmp[v]:
                    return False
                tmp[v] = True
        
        # check cols
        for col in range(9):
            tmp = [False] * 9
            for row in range(9):
                if board[row][col] == ".":
                    continue
                v = int(board[row][col]) - 1
                if tmp[v]:
                    return False
                tmp[v] = True
        
        # check boxes
        # first box
        for x in range(3):
            for y in range(3):
                tmp = [False] * 9
                for row in range(x*3, x*3+3):
                    for col in range(y*3, y*3+3):
                        if board[row][col] == ".":
                            continue
                        v = int(board[row][col]) - 1
                        if tmp[v]:
                            return False
                        tmp[v] = True
        
        return True
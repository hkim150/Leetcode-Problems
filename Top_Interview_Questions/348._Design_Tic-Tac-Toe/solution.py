class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.board = [[-1] * n for _ in range(n)]
        self.gameOver = False
        self.winner = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.gameOver:
            print("GameOver, no more move possible")
            return None
        
        self.board[row][col] = player
        if self.checkWin(row, col, player):
            self.gameOver = True
            self.winner = player
            return player
        
        return 0
        
    def checkWin(self, row, col, player):
        # check row is all player
        noWin = False
        for c in range(self.size):
            if self.board[row][c] != player:
                noWin = True
                break

        if not noWin:
            return True
        
        noWin = False
        # check col
        for r in range(self.size):
            if self.board[r][col] != player:
                noWin = True
                break

        if not noWin:
            return True
        
        noWin = False
        # check diagonal
        if row == col:
            # check left diagonal
            for i in range(self.size):
                if self.board[i][i] != player:
                    noWin = True
                    break
                    
            if not noWin:
                return True

        noWin = False
        if row + col == self.size - 1:
            # check right diagonal
            for i in range(self.size):
                if self.board[i][self.size-i-1] != player:
                    noWin = True
            
            if not noWin:
                return True
        
        return False
                    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRow = len(board)
        numCol = len(board[0])
        
        def backtrack(r,c,i):
            if i == len(word):
                return True
            
            if not 0 <= r <= numRow-1 or not 0 <= c <= numCol-1 or board[r][c] != word[i]:
                return False

            ret = False
            board[r][c] = '#'
            for ro, co in [(0,1), (1,0), (0,-1), (-1,0)]:
                ret = backtrack(r+ro, c+co, i+1)
                if ret:
                    break

            board[r][c] = word[i]
            return ret
        
        for r in range(numRow):
            for c in range(numCol):
                if backtrack(r,c,0):
                    return True
        
        return False
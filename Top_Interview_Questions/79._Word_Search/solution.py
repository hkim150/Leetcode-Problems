class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(visited, last, word):
            if not word:
                return True
            
            r, c = last
            
            if r > 0 and board[r-1][c] == word[0] and (r-1,c) not in visited:
                v = visited.copy()
                v.add((r-1,c))
                if helper(v, (r-1,c), word[1:]):
                    return True
            
            if c > 0 and board[r][c-1] == word[0] and (r,c-1) not in visited:
                v = visited.copy()
                v.add((r,c-1))
                if helper(v, (r,c-1), word[1:]):
                    return True
            
            if r < len(board)-1 and board[r+1][c] == word[0] and (r+1,c) not in visited:
                v = visited.copy()
                v.add((r+1,c))
                if helper(v, (r+1,c), word[1:]):
                    return True
                
            if c < len(board[0])-1 and board[r][c+1] == word[0] and (r,c+1) not in visited:
                v = visited.copy()
                v.add((r,c+1))
                if helper(v, (r,c+1), word[1:]):
                    return True
                
            return False
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    s = set()
                    s.add((r,c))
                    if helper(s, (r,c), word[1:]):
                        return True
        
        return False
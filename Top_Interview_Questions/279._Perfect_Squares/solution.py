class Solution:
    def numSquares(self, n: int) -> int:
        if n < 1:
            return 0
        
        if n == 1:
            return 1
        
        # we can use dynamic programming
        lst = [float('inf')] * (n+1)
        lst[0] = 0
        squares = []
        i = sq = 1
        while sq <= n:
            squares.append(sq)
            i += 1
            sq = i**2
        
        for i in range(n+1):
            for sq in squares:
                if i + sq > n:
                    break
                lst[i+sq] = min(lst[i+sq], lst[i]+1)

        return lst[n]
                
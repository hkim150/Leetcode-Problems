class Solution:
    def numSquares(self, n: int) -> int:
        mem = [float('inf')] * (n+1)
        mem[0] = 0
        
        squares = []
        sqr = 0
        for i in range(1, int(sqrt(n))+1):
            sqr = i**2
            mem[sqr] = 1
            squares.append(sqr)
        
        if sqr == n:
            return 1
        
        for i in range(2, n+1):
            if mem[i] == 1:
                continue
                
            for square in squares:
                if square >= i:
                    break;
                mem[i] = min(mem[i], 1 + mem[i-square])
            
        print(mem)
        return mem[n]
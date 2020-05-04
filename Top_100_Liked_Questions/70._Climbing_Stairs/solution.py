class Solution:
    def climbStairs2(self, n: int) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0
        
        # you can take 1 step and have climbStairs(n-1) number of ways
        # or you can take 2 steps and have climbStairs(n-2) number of ways
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        
        # the above is equivalent to the Fibonacci sequence; n_2 = n_1 + n_0
        # for n times, update n_1 <- n_1 + n_0 and n_0 <- n_1
        i, j = 1, 0
        for _ in range(n):
            i, j = i + j, i
        
        return i
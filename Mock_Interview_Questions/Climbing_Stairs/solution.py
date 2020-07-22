class Solution:
    def climbStairs(self, n: int) -> int:
        # start with 1 step, you are left with n-1 steps
        # start with 2 steps, you are left with n-2 steps
        # thus ans(n) = ans(n-1) + ans(n-2) a.k.a fibonacci seq
        i, j = 1, 0
        for _ in range(n):
            i, j = i+j, i
        
        return i
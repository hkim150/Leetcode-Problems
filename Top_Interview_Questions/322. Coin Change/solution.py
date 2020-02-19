class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp with memoization
        mem = [0] * (amount+1)
        for a in range(1, amount+1):
            cand = [mem[a - c] for c in coins[::-1] if c <= a]
            mem[a] = 1 + min(cand) if cand else float('inf')
        
        return mem[-1] if mem[-1] != float('inf') else -1
                    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        # dp solution using recursion
        def helper(amount):
            if amount == 0:
                return 0
            
            cand = [float("inf")]
            for i in range(len(coins)-1, -1, -1):
                if coins[i] <= amount:
                    cand.append(helper(amount - coins[i]))
            
            return 1 + min(cand)
        
        ans = helper(amount)
        if ans == float("inf"):
            return -1
        
        return ans
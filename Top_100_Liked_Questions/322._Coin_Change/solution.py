class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp memoization bottom up
        mem = [float('inf')] *  (amount+1)
        mem[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                mem[i] = min(mem[i], mem[i-coin] + 1)
        
        return mem[amount] if mem[amount] != float('inf') else -1
    
    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        # recursive dp
        d = {}
        
        def minCoins(amount):
            if amount == 0:
                return 0

            minCoin = float('inf')
            for coin in coins:
                if amount >= coin:
                    rem = amount - coin
                    minCoin = min(minCoin, 1 + d.get(rem, minCoins(amount-coin)))
            
            d[amount] = minCoin
            return minCoin
        ans = minCoins(amount)
        return -1 if ans == float('inf') else ans
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        mem = [[0]*(l+1) for _ in range(l+2)]
        
        for i in range(l-1, -1, -1):
            mem[i][0] = max(mem[i+1][i+1], mem[i+1][0])
            for j in range(i):
                mem[i][j+1] = max(prices[i] - prices[j] + mem[i+2][0], mem[i+1][j+1])
        
        return mem[0][0]
        
    
    def maxProfit2(self, prices: List[int]) -> int:
        # recursive dp
        def helper(idx, bought_idx):
            if idx >= len(prices):
                return 0;
            
            if bought_idx == -1:
                return max(helper(idx+1, idx), helper(idx+1, -1))
            
            return max(prices[idx] - prices[bought_idx] + helper(idx+2, -1), helper(idx+1, bought_idx))
    
        return helper(0, -1)

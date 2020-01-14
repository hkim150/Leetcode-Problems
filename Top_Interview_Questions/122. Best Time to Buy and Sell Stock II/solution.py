class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can add the consecutive increases
        ans = 0
        last = float('inf')
        
        for price in prices:
            if price > last:
                ans += price - last
                
            last = price
            
        return ans
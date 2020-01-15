class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can keep track of the minimum price and the maximum profit we've seen so far
        # this way, we ensure that the purchase comes before the selling
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
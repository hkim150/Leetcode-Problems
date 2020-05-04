class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = float('inf')
        
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProf = max(maxProf, price - minPrice)
        
        return maxProf
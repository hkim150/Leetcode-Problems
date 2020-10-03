class Solution {
    public int maxProfit(int[] prices) {
        // hold the value of the minimum price
        // and update the max profit
        int minPrice = Integer.MAX_VALUE;
        int mp = 0;

        for (int price : prices) {
            if (price < minPrice)
                minPrice = price;
            else
                mp = Math.max(mp, price - minPrice);
        }

        return mp;
    }
}
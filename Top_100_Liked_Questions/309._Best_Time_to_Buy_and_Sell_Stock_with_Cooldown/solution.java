class Solution {
    // iterative dp
    public int maxProfit(int[] prices) {
        int[][] mem = new int[prices.length+2][prices.length+1];
        for (int i=prices.length-1; i>-1; i--) {
            mem[i][0] = Math.max(mem[i+1][i+1], mem[i+1][0]);
            for (int j=0; j<i; j++) {
                mem[i][j+1] = Math.max(prices[i] - prices[j] + mem[i+2][0], mem[i+1][j+1]);
            }
        }
        return mem[0][0];
    }
}


class Solution2 {
    // recursive dp
    public int maxProfit(int[] prices) {
        return this.maxProfit(prices, 0, -1);
    }

    public int maxProfit(int[] prices, int idx, int buy_idx) {
        if (idx >= prices.length)
            return 0;

        if (buy_idx == -1)
            return Math.max(this.maxProfit(prices, idx+1, idx), this.maxProfit(prices, idx+1, -1));

        return Math.max(prices[idx] - prices[buy_idx] + this.maxProfit(prices, idx+2, -1), this.maxProfit(prices, idx+1, buy_idx));
    }
}
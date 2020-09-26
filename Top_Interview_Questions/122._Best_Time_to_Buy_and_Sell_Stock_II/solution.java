class Solution {
    public int maxProfit(int[] prices) {
        int mx = 0;
        for (int i=1; i<prices.length; i++) {
            if (prices[i] > prices[i-1])
                mx += prices[i] - prices[i-1];
        }

        return mx;
    }
}

class Solution4 {
    public int maxProfit(int[] prices) {
        int[] mem = new int[prices.length+1];

        for (int i=prices.length-1; i>-1; i--) {
            for (int j=i; j>-1; j--) {
                if (j == 0)
                    mem[j] = Math.max(mem[j], mem[i]);
                else
                    mem[j] = Math.max(mem[j], prices[i] - prices[j-1] + mem[0]);
            }
        }

        return mem[0];
    }
}

class Solution3 {
    public int maxProfit(int[] prices) {
        int[][] mem = new int[prices.length+1][prices.length+1];

        for (int i=prices.length-1; i>-1; i--) {
            for (int j=0; j<=i; j++) {
                if (j == 0)
                    mem[j][i] = Math.max(mem[j][i+1], mem[i][i+1]);
                else
                    mem[j][i] = Math.max(mem[j][i+1], prices[i] - prices[j-1] + mem[0][i+1]);
            }
        }
        return mem[0][0];
    }
}

class Solution2 {
    public int maxProfit(int[] prices) {
        return maxProfit(prices, -1, 0);
    }

    public int maxProfit(int[] prices, int buyIdx, int currIdx) {
        if (currIdx == prices.length)
            return 0;

        if (buyIdx == -1)
            return Math.max(maxProfit(prices, buyIdx, currIdx+1), maxProfit(prices, currIdx, currIdx+1));
        else
            return Math.max(maxProfit(prices, buyIdx, currIdx+1), prices[currIdx] - prices[buyIdx] + maxProfit(prices, -1, currIdx+1));
    }
}
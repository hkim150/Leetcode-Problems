class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] mem = new int[amount+1];

        for (int i=1; i<amount+1; i++) {
            int min = Integer.MAX_VALUE;
            for (int coin : coins) {
                if (i - coin >= 0 && mem[i - coin] >= 0)
                    min = Math.min(min, mem[i - coin]);
            }

            mem[i] = min == Integer.MAX_VALUE ? -1 : min + 1;
        }

        return mem[amount];
    }
}


class Solution2 {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0)
            return 0;

        if (amount < 0)
            return Integer.MAX_VALUE;

        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            min = Math.min(min, coinChange(coins, amount - coin));
        }

        return min + 1;
    }
}
class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        // iterative dp - max sum capped at 1000
        final int max_sum = 1000;

        if (Math.abs(S) > max_sum)
            return 0;

        int[][] mem = new int[nums.length+1][max_sum*2+1];
        mem[nums.length][max_sum] = 1;

        for (int i=mem.length-2; i>-1; i--) {
            for (int j=0; j<mem[0].length; j++) {
                int add = j - nums[i] >= 0 ?  mem[i+1][j-nums[i]] : 0;
                int sub = j + nums[i] < mem[0].length ? mem[i+1][j+nums[i]] : 0;
                mem[i][j] = add + sub;
            }
        }
        return mem[0][S+max_sum];
    }
}

class Solution2 {
    public int findTargetSumWays(int[] nums, int S) {
        // recursive dp O(2^n)
        return findTargetSumWays(nums, S, 0);
    }

    public int findTargetSumWays(int[] nums, int S, int i) {
        if (i == nums.length)
            return S == 0 ? 1 : 0;

        return findTargetSumWays(nums, S - nums[i], i+1) + findTargetSumWays(nums, S + nums[i], i+1);
    }
}
class Solution {
    public int maxSubArray(int[] nums) {
        // one pass algorithm
        int ans = Integer.MIN_VALUE;
        int sum = 0;
        for (int n : nums) {
            // if the sum is negative, start fresh
            if (sum < 0)
                sum = 0;

            sum += n;
            ans = Math.max(ans, sum);
        }

        return ans;
    }
}
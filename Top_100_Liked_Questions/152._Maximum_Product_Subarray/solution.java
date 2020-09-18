class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0)
            return 0;

        int max = nums[0];
        int min = nums[0];
        int ans = nums[0];

        for (int i=1; i<nums.length; i++) {
            int curr = nums[i];
            int temp_max = Math.max(Math.max(curr, max * curr), min * curr);
            min = Math.min(Math.min(curr, max * curr), min * curr);
            max = temp_max;

            ans = Math.max(ans, max);
        }

        return ans;
    }
}
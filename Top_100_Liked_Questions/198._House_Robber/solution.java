class Solution {
    public int rob(int[] nums) {
        int n0 = 0, n1 = 0, n2 = 0;

        for (int i=nums.length-1; i>-1; i--) {
            n0 = Math.max(n1, nums[i] + n2);
            n2 = n1;
            n1 = n0;
        }

        return n0;
    }

    public int rob3(int[] nums) {
        int[] mem = new int[nums.length+2];

        for (int i=nums.length-1; i>-1; i--) {
            mem[i] = Math.max(nums[i] + mem[i+2], mem[i+1]);
        }

        return mem[0];
    }

    public int rob2(int[] nums) {
        return this.helper(nums, 0);
    }

    public int helper(int[] nums, int i) {
        if (i >= nums.length)
            return 0;

        return Math.max(nums[i] + helper(nums, i+2), helper(nums, i+1));
    }
}
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];

        // [1, a, ab, abc, ...]
        ans[0] = 1;
        for (int i=0; i<nums.length-1; i++) {
            ans[i+1] = ans[i] * nums[i];
        }

        // [..., bcd, cd, d, 1]
        int mult_val = 1;
        for (int i=nums.length-1; i>0; i--) {
            mult_val *= nums[i];
            ans[i-1] *= mult_val;
        }

        return ans;
    }
}
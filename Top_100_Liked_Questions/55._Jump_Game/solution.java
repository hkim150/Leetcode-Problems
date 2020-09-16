class Solution {
    public boolean canJump(int[] nums) {
        // n: smallest index that can chain jump reach the last index
        // n is reachable from index n-1 if nums[n-1] >= 1
        // or from index n-2 if nums[n-2] >= 2 ... and so on
        // so n is reachable from index i if nums[i] >= n - i
        // and if i can reach n, then i becomes the new n
        int n = nums.length-1;
        for (int i=nums.length-2; i>-1; i--) {
            if (nums[i] >= n - i)
                n = i;
        }

        return n == 0;
    }
}
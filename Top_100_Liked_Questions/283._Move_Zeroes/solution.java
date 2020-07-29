class Solution {
    public void moveZeroes(int[] nums) {
        // two pointer method
        // have one pointer iterate through the loop
        // have another point to where the next last non-zero number should come
        // swap the two values if the fast pointer is non-zero
        int next_non_zero = 0;
        for (int i=0; i<nums.length; i++) {
            if (nums[i] == 0) continue;

            int temp = nums[next_non_zero];
            nums[next_non_zero++] = nums[i];
            nums[i] = temp;
        }
    }
}
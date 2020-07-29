class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // use indices to mark the positions where number is present
        // mark the index with negative
        for (int n : nums) {
            int i = Math.abs(n) - 1;

            if (nums[i] > 0)
                nums[i] *= -1;
        }

        List<Integer> ans = new ArrayList<Integer>();

        for (int i=0; i<nums.length; i++) {
            if (nums[i] > 0)
                ans.add(i+1);
        }

        return ans;
    }
}
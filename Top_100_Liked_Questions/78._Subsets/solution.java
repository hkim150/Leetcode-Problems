// iterative
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<Integer>());

        for (int n : nums) {
            int size = ans.size();
            for (int i=0; i<size; i++) {
                List<Integer> subset = new ArrayList<>(ans.get(i));
                subset.add(n);
                ans.add(subset);
            }
        }

        return ans;
    }
}

// recursive
class Solution2 {
    public List<List<Integer>> subsets;

    public List<List<Integer>> subsets(int[] nums) {
        this.subsets = new ArrayList<>();
        this.helper(new ArrayList<>(), nums, 0);
        return this.subsets;
    }

    public void helper(List<Integer> subset, int[] nums, int i) {
        if (i == nums.length) {
            this.subsets.add(subset);
            return;
        }
        this.helper(subset, nums, i+1);

        List<Integer> subset2 = new ArrayList<>(subset);
        subset2.add(nums[i]);
        this.helper(subset2, nums, i+1);
    }
}
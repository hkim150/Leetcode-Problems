class Solution {
    public List<List<Integer>> permutations = new ArrayList<List<Integer>>();

    public List<List<Integer>> permute(int[] nums) {
        List<Integer> rem = new ArrayList<Integer>();
        for (int n : nums)
            rem.add(n);

        this.helper(new ArrayList<Integer>(), rem);
        return this.permutations;
    }

    public void helper(List<Integer> perm, List<Integer> rem) {
        if (rem.isEmpty()) {
            this.permutations.add(perm);
            return;
        }

        for (int i=0; i<rem.size(); i++) {
            List<Integer> perm_copy = new ArrayList<>(perm);
            List<Integer> rem_copy = new ArrayList<>(rem);
            perm_copy.add(rem_copy.remove(i));
            this.helper(perm_copy, rem_copy);
        }
    }
}
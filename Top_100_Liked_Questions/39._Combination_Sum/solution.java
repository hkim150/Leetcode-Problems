class Solution {
    public List<List<Integer>> ans = new ArrayList();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        backTrack(new ArrayList<>(), candidates, 0, target);
        return this.ans;
    }

    public void backTrack(List<Integer> combination, int[] candidates, int idx, int target) {
        if (target == 0) {
            this.ans.add(new ArrayList<Integer>(combination));
            return;
        }

        for (int i=idx; i<candidates.length; i++) {
            if (target - candidates[i] >= 0) {
                combination.add(candidates[i]);
                this.backTrack(combination, candidates, i, target - candidates[i]);
                combination.remove(combination.size()-1);
            }
        }
    }
}
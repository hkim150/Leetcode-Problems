class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();

        if (numRows == 0)
            return ans;

        List<Integer> prev = new ArrayList<>(Arrays.asList(1));
        ans.add(prev);
        for (int i=0; i<numRows-1; i++) {
            System.out.println(prev);
            List<Integer> curr = new ArrayList<>(Arrays.asList(1));
            for (int j=0; j<prev.size()-1; j++) {
                curr.add(prev.get(j) + prev.get(j+1));
            }
            curr.add(1);
            ans.add(curr);
            prev = curr;
        }

        return ans;
    }
}
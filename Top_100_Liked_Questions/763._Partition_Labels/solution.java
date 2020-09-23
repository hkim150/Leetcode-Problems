class Solution {
    public List<Integer> partitionLabels(String S) {
        // put the last occuring indices of each letter in array of size 26
        int[] lastIndices = new int[26];
        List<Integer> ans = new ArrayList<>();
        int a_ascii = (int) 'a';

        for (int i=0; i<S.length(); i++)
            lastIndices[(int) S.charAt(i) - a_ascii] = i;

        for (int i=0; i<S.length();) {
            int earliest_partition = lastIndices[(int) S.charAt(i) - a_ascii];
            int j;
            for (j=i; j<earliest_partition; j++) {
                earliest_partition = Math.max(earliest_partition, lastIndices[(int) S.charAt(j) - a_ascii]);
            }
            ans.add(j - i + 1);
            i = j + 1;
        }

        return ans;
    }
}
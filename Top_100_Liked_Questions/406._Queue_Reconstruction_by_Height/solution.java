class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // sort the people first by the height in descending order
        // and then by the numer of people in front
        Arrays.sort(people, new Comparator<int[]>() {
            @Override
            public int compare(final int[] e1, final int[] e2) {
                return e1[0] == e2[0] ? e1[1] - e2[1] : e2[0] - e1[0];
            }
        });

        List<int[]> ans = new ArrayList<>();
        // iterate through the sorted people and
        // place the person in the ans array at the index of person[1]
        for (int[] person : people) {
            ans.add(person[1], person);
        }

        return ans.toArray(new int[people.length][2]);
    }
}
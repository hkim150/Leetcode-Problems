class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1)
            return intervals;

        Arrays.sort(intervals, (a, b) -> {
            if (a[0] != b[0])
                return a[0] - b[0];
            else
                return a[1] - b[1];
        });

        int count = 1;
        int i = 0;
        while (i < intervals.length-1) {
            if (intervals[i+1][0] <= intervals[i][1]) {
                intervals[i+1][0] = intervals[i][0];
                intervals[i+1][1] = Math.max(intervals[i][1], intervals[i+1][1]);
                intervals[i][0] = -1;
            }
            else
                count++;

            i++;
        }

        int[][] ans = new int[count][2];
        int k=0;
        for (int j=0; j<intervals.length; j++) {
            if (intervals[j][0] >= 0) {
                ans[k][0] = intervals[j][0];
                ans[k][1] = intervals[j][1];
                k++;
            }
        }

        return ans;
    }
}
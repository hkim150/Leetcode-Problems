class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // sort the intervals, first with start time and next with end time
        Arrays.sort(intervals, (a, b) -> a[0] - b[0] == 0 ? a[1] - b[1] : a[0] - b[0]);
        // create a priority queue that stores the end time of the rooms
        Queue<Integer> q = new PriorityQueue<>();

        int count = 0;
        // for every interval
        for (int[] interval : intervals) {
            // if the start time is greater or equal to the top element pop the element
            if (!q.isEmpty() && interval[0] >= q.peek())
                q.poll();

            // add a new element with the end time
            q.add(interval[1]);

            count = Math.max(count, q.size());
        }

        return count;
    }
}
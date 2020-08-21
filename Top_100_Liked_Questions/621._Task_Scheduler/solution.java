class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] task_count = new int[26];
        int a_ascii = (int) 'A';

        for (char task : tasks) {
            task_count[(int) task - a_ascii]++;
        }

        int t_max = 0;
        for (int count : task_count) {
            t_max = Math.max(t_max, count);
        }

        int n_t_max = 0;
        for (int count : task_count) {
            if (count == t_max)
                n_t_max++;
        }

        return Math.max(tasks.length, (n+1) * (t_max-1) + n_t_max);
    }
}
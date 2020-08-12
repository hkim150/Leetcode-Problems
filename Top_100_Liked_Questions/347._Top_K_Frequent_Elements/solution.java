class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count occurances of each number using a hash map
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1);
        }

        Queue<Integer> pq = new PriorityQueue<>((n1, n2) -> count.get(n1) - count.get(n2));

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            if (pq.size() < k) {
                pq.add(entry.getKey());
                continue;
            }

            // if the occurance is greater than the head of the min heap, remove the head and add the element
            if (count.get(pq.peek()) < entry.getValue()) {
                pq.poll();
                pq.add(entry.getKey());
            }
        }

        int[] ans = new int[k];
        Iterator<Integer> it = pq.iterator();
        int i = 0;

        while (it.hasNext()) {
            ans[i++] = it.next();
        }

        return ans;
    }
}
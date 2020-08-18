class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>(k);

        for (int i=0; i<k; i++) {
            pq.add(nums[i]);
        }

        for (int i=k; i<nums.length; i++) {
            if (pq.peek() < nums[i]) {
                pq.poll();
                pq.add(nums[i]);
            }
        }

        return pq.peek();
    }
}
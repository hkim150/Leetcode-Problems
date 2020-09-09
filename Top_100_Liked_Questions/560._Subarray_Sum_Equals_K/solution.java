class Solution {
    public int subarraySum(int[] nums, int k) {
        int cumul_sum = 0;
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int i=0; i<nums.length; i++) {
            cumul_sum += nums[i];
            ans += map.getOrDefault(cumul_sum - k, 0);
            map.put(cumul_sum, map.getOrDefault(cumul_sum, 0) + 1);
        }

        return ans;
    }
}
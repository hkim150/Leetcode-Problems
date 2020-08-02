class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int other = target - nums[i];
            if (map.containsKey(other))
                return new int[]{map.get(other), i};

            map.put(nums[i], i);
        }

        try {
            throw new Exception("no answer found");
        } catch (Exception e) {
            System.out.println(e.toString());
        }

        return null;
    }
}
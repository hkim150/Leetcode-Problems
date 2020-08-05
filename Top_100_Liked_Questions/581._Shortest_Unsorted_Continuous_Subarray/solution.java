class Solution {
    public int findUnsortedSubarray(int[] nums) {
        List<Integer> stack = new ArrayList<>();
        int l = nums.length - 1;
        int r = 0;

        // find the minimum unsorted element position l
        for (int i=0; i<nums.length; i++) {
            while (!stack.isEmpty() && nums[stack.get(stack.size()-1)] > nums[i])
                l = Math.min(l, stack.remove(stack.size()-1));

            stack.add(i);
        }

        stack.clear();
        // find the maximum unsorted element position r
        for (int i=nums.length-1; i>-1; i--) {
            while (!stack.isEmpty() && nums[stack.get(stack.size()-1)] < nums[i])
                r = Math.max(r, stack.remove(stack.size()-1));

            stack.add(i);
        }

        return Math.max(r - l + 1, 0);
    }
}
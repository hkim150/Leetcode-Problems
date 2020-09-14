class Solution {
    public int[] searchRange(int[] nums, int target) {
        int init = binarySearch(nums, 0, nums.length-1, target);
        if (init == -1)
            return new int[]{-1, -1};

        int[] ans = new int[2];

        int left = init;
        int prev = left;
        while (left != -1) {
            prev = left;
            left = binarySearch(nums, 0, left-1, target);
        }

        ans[0] = prev;

        int right = init;
        prev = right;
        while (right != -1) {
            prev = right;
            right = binarySearch(nums, right+1, nums.length-1, target);
        }

        ans[1] = prev;

        return ans;
    }

    public int binarySearch(int[] nums, int left, int right, int target) {
        if (left > right)
            return -1;

        int mid = left + Math.floorDiv(right - left, 2);
        if (nums[mid] < target) {
            return binarySearch(nums, mid+1, right, target);
        } else if (nums[mid] > target) {
            return binarySearch(nums, left, mid-1, target);
        } else
            return mid;
    }
} 
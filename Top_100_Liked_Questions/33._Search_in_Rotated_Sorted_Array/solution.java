class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;

        while (left <= right) {
            int mid = left + Math.floorDiv(right - left, 2);
            if (nums[mid] == target)
                return mid;
            else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else if (nums[mid] <= nums[right]) {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return -1;
    }
}


class Solution2 {
    public int search(int[] nums, int target) {
        return binarySearchRotation(nums, 0, nums.length-1, target);
    }

    public int binarySearchRotation(int[] nums, int left, int right, int target) {
        if (left > right)
            return -1;

        int mid = left + Math.floorDiv(right - left, 2);
        if (target == nums[mid])
            return mid;
        else if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid])
                return binarySearchRotation(nums, left, mid-1, target);
            else
                return binarySearchRotation(nums, mid+1, right, target);
        } else { // nums[mid] <= nums[right]
            if (nums[mid] < target && target <= nums[right])
                return binarySearchRotation(nums, mid+1, right, target);
            else
                return binarySearchRotation(nums, left, mid-1, target);
        }
    }
}
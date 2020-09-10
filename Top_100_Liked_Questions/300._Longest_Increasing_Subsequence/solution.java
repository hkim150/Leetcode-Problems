class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] mem = new int[nums.length];
        int len=0;
        for (int num : nums) {
            int i = Arrays.binarySearch(mem, 0, len, num);
            if (i < 0)
                i = -(i + 1);

            mem[i] = num;

            if (i == len)
                len++;
        }

        return len;
    }
}


class Solution4 {
    public int lengthOfLIS(int[] nums) {
        int[] new_nums = new int[nums.length+1];
        new_nums[0] = Integer.MIN_VALUE;

        for (int i=0; i<nums.length; i++)
            new_nums[i+1] = nums[i];

        int[] mem = new int[nums.length+1];

        for (int i=nums.length; i>0; i--) {
            for (int j=i-1; j>-1; j--) {
                if (new_nums[i] > new_nums[j])
                    mem[j] = Math.max(1 + mem[i], mem[j]);
            }
        }

        return mem[0];
    }
}


class Solution3 {
    public int lengthOfLIS(int[] nums) {
        int[] new_nums = new int[nums.length+1];
        new_nums[0] = Integer.MIN_VALUE;

        for (int i=0; i<nums.length; i++)
            new_nums[i+1] = nums[i];

        int[][] mem = new int[nums.length+2][nums.length+1];

        for (int i=nums.length; i>0; i--) {
            for (int j=i-1; j>-1; j--) {
                if (new_nums[i] > new_nums[j])
                    mem[i][j] = Math.max(1 + mem[i+1][i], mem[i+1][j]);
                else
                    mem[i][j] = mem[i+1][j];
            }
        }

        return mem[1][0];
    }
}


class Solution2 {
    public int lengthOfLIS(int[] nums) {
        int[] new_nums = new int[nums.length+1];
        new_nums[0] = Integer.MIN_VALUE;

        for (int i=0; i<nums.length; i++)
            new_nums[i+1] = nums[i];

        return LIS(new_nums, 1, 0);
    }

    public int LIS(int[] nums, int idx, int max_idx) {
        if (idx == nums.length)
            return 0;

        if (nums[idx] > nums[max_idx])
            return Math.max(1 + LIS(nums, idx+1, idx), LIS(nums, idx+1, max_idx));

        return LIS(nums, idx+1, max_idx);
    }
}
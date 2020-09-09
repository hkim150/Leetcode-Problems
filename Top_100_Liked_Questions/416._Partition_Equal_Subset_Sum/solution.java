class Solution {
    public boolean canPartition(int[] nums) {
        // O(n) memory bottom up solution
        int totalSum = 0;
        for (int n : nums)
            totalSum += n;

        if (totalSum % 2 != 0)
            return false;

        int subsetSum = totalSum / 2;
        boolean[] mem = new boolean[subsetSum+1];
        mem[0] = true;

        for (int i=0; i<nums.length; i++) {
            for (int j=subsetSum; j>-1; j--) {
                if (j >= nums[i])
                    mem[j] |= mem[j-nums[i]];
            }
        }

        return mem[subsetSum];
    }
}


class Solution3 {
    public boolean canPartition(int[] nums) {
        // bottom up solution
        int totalSum = 0;
        for (int n : nums)
            totalSum += n;

        if (totalSum % 2 != 0)
            return false;

        int subsetSum = totalSum / 2;
        boolean[][] mem = new boolean[nums.length+1][subsetSum+1];
        mem[0][0] = true;

        for (int i=1; i<nums.length+1; i++) {
            for (int j=subsetSum; j>-1; j--) {
                if (j < nums[i-1])
                    mem[i][j] = mem[i-1][j];
                else
                    mem[i][j] = mem[i-1][j] || mem[i-1][j-nums[i-1]];
            }
        }

        return mem[nums.length][subsetSum];
    }
}


class Solution2 {
    public Map<String, Boolean> mem;

    public boolean canPartition(int[] nums) {
        // the total sum needs to be an even number
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for (int n : nums) {
            sum += n;
            max = Math.max(max, n);
        }

        if (sum % 2 != 0)
            return false;

        // if there is a number greater than sum/2 then cannot be partitioned
        if (max > sum/2)
            return false;

        if (max == sum)
            return true;

        // if there is a combination sum of sum/2 then the remaining numbers will add up to sum/2
        this.mem = new HashMap<String, Boolean>();
        return this.helper(nums, 0, sum/2);
    }

    public boolean helper(int[] nums, int idx, int sum) {
        if (sum == 0)
            return true;

        if (sum < 0 || idx == nums.length)
            return false;

        String s_include = Integer.toString(idx+1) + "-" + Integer.toString(sum - nums[idx]);
        boolean include;
        if (this.mem.containsKey(s_include))
            include = this.mem.get(s_include);
        else {
            include = this.helper(nums, idx+1, sum - nums[idx]);
            this.mem.put(s_include, include);
        }

        String s_exclude = Integer.toString(idx+1) + "-" + Integer.toString(sum);
        boolean exclude;
        if (this.mem.containsKey(s_exclude))
            exclude = this.mem.get(s_exclude);
        else {
            exclude = this.helper(nums, idx+1, sum);
            this.mem.put(s_exclude, exclude);
        }

        return include || exclude;
    }
}
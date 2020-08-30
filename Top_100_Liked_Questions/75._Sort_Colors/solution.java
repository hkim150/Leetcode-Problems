class Solution {
    public void sortColors(int[] nums) {
        // one pass using two pointer
        int next_0 = 0;
        int next_2 = nums.length-1;

        int i = 0;
        while (i <= next_2) {
            if (nums[i] == 0) {
                nums[i] = nums[next_0];
                nums[next_0++] = 0;
                i++;
            } else if (nums[i] == 2) {
                nums[i] = nums[next_2];
                nums[next_2--] = 2;
            } else {
                i++;
            }
        }
    }
}


class Solution2 {
    public void sortColors(int[] nums) {
        // two pass using count
        int[] count = new int[3];

        for (int i=0; i<nums.length; i++) {
            count[nums[i]]++;
        }

        int idx = 0;
        for (int i=0; i<count.length; i++) {
            for (int j=0; j<count[i]; j++) {
                nums[idx++] = i;
            }
        }
    }
}
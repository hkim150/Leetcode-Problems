class Solution {
    public int[] countBits(int num) {
        int[] ans = new int[num + 1];
        for (int i=1; i<=num; i++)
            ans[i] = ans[i & (i - 1)] + 1;

        return ans;
    }

    public int[] countBits2(int num) {
        int[] ans = new int[num+1];

        int upto = 1;
        while (true) {
            for (int i=0; i<upto; i++) {
                if (upto + i == num + 1)
                    return ans;

                ans[upto+i] = ans[i] + 1;
            }

            upto *= 2;
        }
    }
}
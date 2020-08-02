class Solution {
    public int climbStairs(int n) {
        // take 1 step and left with (n-1) steps
        // take 2 steps and left with (n-2) steps
        // fibonacci: f(n) = f(n-1) + f(n-2)

        int i=1;
        int j=0;
        int temp;

        for (int k=0; k<n; k++) {
            temp = i;
            i = i + j;
            j = temp;
        }

        return i;
    }
}
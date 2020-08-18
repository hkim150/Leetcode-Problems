class Solution {
    public int numTrees(int n) {
        int[] mem = new int[n+1];
        mem[0] = 1;

        for (int i=1; i<n+1; i++) {
            for (int j=0; j<i; j++) {
                mem[i] += mem[j] * mem[i-j-1];
            }
        }

        return mem[n];
    }
}


class Solution2 {
    public int numTrees(int n) {
        // numTrees(n) = numTrees(0)*numTrees(n-1) + numTrees(1)*numTrees(n-2) + numTrees(2)*numTrees(n-3) ... numTrees(n-1)*numTrees(0)
        if (n == 0)
            return 1;

        int sum = 0;
        for (int i=0; i<n; i++) {
            sum += this.numTrees(i) * this.numTrees(n-i-1);
        }
        return sum;
    }
}
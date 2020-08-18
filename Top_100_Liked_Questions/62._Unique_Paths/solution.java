class Solution {
    public int uniquePaths(int m, int n) {
        int[][] mem = new int[n][m];

        for (int row=n-1; row>-1; row--) {
            for (int col=m-1; col>-1; col--) {
                if (row == n-1 && col == m-1)
                    mem[row][col] = 1;

                else if (row == n-1)
                    mem[row][col] = mem[row][col+1];

                else if (col == m-1)
                    mem[row][col] = mem[row+1][col];

                else
                    mem[row][col] = mem[row][col+1] + mem[row+1][col];
            }
        }

        return mem[0][0];
    }
}

class Solution2 {
    public int uniquePaths(int m, int n) {
        // uniquePaths(x,y) = uniquePaths(x+1,y) + uniquePaths(x,y+1)
        if (m == 1 && n == 1)
            return 1;

        else if (m == 1)
            return this.uniquePaths(m, n-1);

        else if (n == 1)
            return this.uniquePaths(m-1, n);

        else
            return this.uniquePaths(m-1, n) + uniquePaths(m, n-1);
    }
}
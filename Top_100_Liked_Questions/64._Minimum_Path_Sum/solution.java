class Solution {
    public int minPathSum(int[][] grid) {
        // dp with memoization 1d
        int[] mem = new int[grid[0].length];

        for (int row=grid.length-1; row>-1; row--) {
            for (int col=grid[0].length-1; col>-1; col--) {
                if (row == grid.length-1 && col == grid[0].length-1)
                    mem[col] = grid[grid.length-1][grid[0].length-1];

                else if (row == grid.length-1)
                    mem[col] = grid[row][col] + mem[col+1];

                else if (col == grid[0].length-1)
                    mem[col] = grid[row][col] + mem[col];

                else
                    mem[col] = grid[row][col] + Math.min(mem[col], mem[col+1]);
            }
        }
        return mem[0];
    }
}

class Solution3 {
    public int minPathSum(int[][] grid) {
        // dp with memoization 2d
        int[][] mem = new int[grid.length][grid[0].length];

        for (int row=grid.length-1; row>-1; row--) {
            for (int col=grid[0].length-1; col>-1; col--) {
                if (row == grid.length-1 && col == grid[0].length-1) {
                    mem[row][col] = grid[row][col];
                    continue;
                }

                int below = row < grid.length-1 ? mem[row+1][col] : Integer.MAX_VALUE;
                int right = col < grid[0].length-1 ? mem[row][col+1] : Integer.MAX_VALUE;

                mem[row][col] = grid[row][col] + Math.min(below, right);
            }
        }

        return mem[0][0];
    }
}

class Solution2 {
    public int minPathSum(int[][] grid) {
        // dp mps(i,j) = grid[i][j] + min(mps[i+1][j], mps[i][j+1])
        return this.helper(grid, 0, 0);
    }

    public int helper(int[][] grid, int row, int col) {
        if (row == grid.length || col == grid[0].length)
            return Integer.MAX_VALUE;

        else if (row == grid.length-1 && col == grid[0].length-1)
            return grid[row][col];

        return grid[row][col] + Math.min(this.helper(grid, row+1, col), this.helper(grid, row, col+1));
    }
}
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0)
            return 0;

        int[][] mem = new int[matrix.length][matrix[0].length];
        int ans = 0;

        for (int i=mem.length-1; i>-1; i--) {
            for (int j=mem[0].length-1; j>-1; j--) {
                if (matrix[i][j] == '0')
                    mem[i][j] = 0;
                else {
                    mem[i][j] = 1;
                    if (i+1 < mem.length && j+1 < mem[0].length)
                        mem[i][j] += Math.min(Math.min(mem[i+1][j], mem[i][j+1]), mem[i+1][j+1]);
                    ans = Math.max(ans, mem[i][j]);
                }
            }
        }

        return ans * ans;
    }
}
class Solution {
    public void rotate(int[][] matrix) {
        // x, y => y, n-x
        // flip x and transpose, or transpose and flip y

        // transpose
        for (int row=0; row<matrix.length; row++) {
            for (int col=row+1; col<matrix[0].length; col++) {
                int temp = matrix[row][col];
                matrix[row][col] = matrix[col][row];
                matrix[col][row] = temp;
            }
        }

        // flip y
        for (int row=0; row<matrix.length; row++) {
            int l=0;
            int r=matrix[0].length-1;
            while (l < r) {
                int temp = matrix[row][l];
                matrix[row][l] = matrix[row][r];
                matrix[row][r] = temp;
                l++;
                r--;
            }
        }
    }
}
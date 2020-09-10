class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numRow = matrix.length;
        if (numRow == 0)
            return false;

        int numCol = matrix[0].length;
        if (numCol == 0)
            return false;

        int row = numRow-1;
        int col = 0;

        while (true) {
            if (matrix[row][col] < target) {
                if (++col == numCol)
                    return false;
            } else if (matrix[row][col] > target) {
                if (row-- == 0)
                    return false;
            } else
                return true;
        }
    }
}
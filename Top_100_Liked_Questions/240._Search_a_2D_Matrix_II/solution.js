/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    let numRows = matrix.length;
    if (numRows == 0) {
        return false;
    }
    
    let numCols = matrix[0].length;
    if (numCols == 0) {
        return false;
    }
    
    let [r, c] = [numRows-1, 0];
    while (r >= 0 && c <= numCols-1) {
        if (matrix[r][c] < target) {
            c++;
        } else if (matrix[r][c] > target) {
            r--;
        } else {
            return true;
        }
    }
    
    return false;
};
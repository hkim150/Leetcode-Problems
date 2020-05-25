/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    // transverse and reverse method
    const l = matrix.length;
    if (!l || l < 2) {
        return;
    }
    
    for (let row=0; row<l; row++) {
        for (let col=row+1; col<l; col++) {
            [ matrix[row][col], matrix[col][row] ] = [ matrix[col][row], matrix[row][col] ];
        }
    }
    
    for (let row of matrix) {
        row.reverse();
    }
}

var rotate2 = function(matrix) {
    // rotate swap four elements
    let n = matrix.length;
    if (!n || n < 2) {
        return;
    }
    
    for (let i=0; i<Math.floor(n/2); i++) {
        for (let j=i; j<n-i-1; j++) {
            let idx = [];
            let r = i;
            let c = j;

            for(let k=0; k<4; k++) {
                idx.push([r,c]);
                [r,c] = [c, n-1-r];
            }

            [ matrix[idx[1][0]][idx[1][1]], matrix[idx[2][0]][idx[2][1]], matrix[idx[3][0]][idx[3][1]], matrix[idx[0][0]][idx[0][1]] ] = [ matrix[idx[0][0]][idx[0][1]], matrix[idx[1][0]][idx[1][1]], matrix[idx[2][0]][idx[2][1]], matrix[idx[3][0]][idx[3][1]] ];
        }
    }
};
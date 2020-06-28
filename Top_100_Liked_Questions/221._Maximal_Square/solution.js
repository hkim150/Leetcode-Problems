/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    // dp with mem - O(n) space
    let numRow = matrix.length;
    let numCol = numRow >= 1 ? matrix[0].length : 0;
    
    let mem = new Array(numCol+1).fill(0);
    let ans = 0;
    for (let j=numCol-1; j>-1; j--) {
        if (matrix[numRow-1][j] === "1") {
            ans = 1;
            mem[j] = 1;
        }
    }
    
    for (let i=numRow-2; i>-1; i--) {
        let mem2 = new Array(numCol+1).fill(0);
        for (let j=numCol-1; j>-1; j--) {
            mem2[j] = matrix[i][j] === "1" ? Math.min(mem[j], mem[j+1], mem2[j+1]) + 1 : 0;
            ans = Math.max(ans, mem2[j]);
        }
        mem = mem2;
    }
    
    return ans*ans;
}


var maximalSquare2 = function(matrix) {
    // dp with memoization - O(mn) space
    let numRow = matrix.length;
    if (numRow < 1) {
        return 0;
    }
    let mem = new Array(matrix.length+1);
    
    let numCol = matrix[0].length;
    if (numCol < 1) {
        return 0;
    }
    for (let i=0; i<mem.length; i++) {
        mem[i] = new Array(matrix[0].length+1).fill(0);
    }
    
    let maxSq = 0;
    for (let i=matrix.length-1; i>-1; i--) {
        for (let j=matrix[0].length-1; j>-1; j--) {
            if (matrix[i][j] === 0 || matrix[i][j] === "0") {
                mem[i][j] = 0;
            } else {
                mem[i][j] = Math.min(mem[i][j+1], mem[i+1][j], mem[i+1][j+1]) + 1;
                maxSq = Math.max(maxSq, mem[i][j]);
            }
        }
    }
    
    return maxSq * maxSq;
}
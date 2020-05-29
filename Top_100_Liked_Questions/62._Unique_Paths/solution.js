/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let factorial = function(x) {
        let num = x;
        let ans = 1;
        while (num > 1) {
            ans *= num;
        }
    }
    
    return factorial(m+n+2) / (factorial(m-1) * factorial(n-1));
}

var uniquePaths = function(m, n) {
    mem = new Array(m);
    for (let i=0; i<mem.length; i++) {
        mem[i] = new Array(n).fill(1);
    }
    
    for (let i=1; i<mem.length; i++) {
        for (let j=1; j<mem[0].length; j++) {
            mem[i][j] = mem[i-1][j] + mem[i][j-1];
        }
    }
    
    return mem[m-1][n-1];
};
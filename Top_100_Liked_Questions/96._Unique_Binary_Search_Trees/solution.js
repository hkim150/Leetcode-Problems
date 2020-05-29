/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    // iterative dp
    let mem = new Array(n+1).fill(0);
    mem[0] = 1;
    mem[1] = 1;
    
    for (let i=2; i<n+1; i++) {
        for (let j=0; j<i; j++) {
            mem[i] += mem[j] * mem[i-j-1];
        }
    }
    
    return mem[n];
}

var numTrees2 = function(n) {
    // recursive dp
    let numSubTrees = function(n) {
        if (n < 2) {
            return 1;
        }
        
        let tot = 0
        for (let i=0; i<n; i++) {
            tot += numSubTrees(i) * numSubTrees(n-1-i);
        }
        
        return tot;
    }
    
    return numSubTrees(n);
};
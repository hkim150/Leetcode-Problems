/**
 * @param {number} num
 * @return {number[]}
 */
var countBits = function(num) {
    // hamming weight method
    let ans = new Array(num+1).fill(0);
    
    for (let i=1; i<num+1; i++) {
        ans[i] = ans[i & (i-1)] + 1;
    }
    
    return ans;
}

var countBits2 = function(num) {
    // array doubling method
    let ans = [0];
    
    while (ans.length < num+1) {
        ans = [...ans, ...ans.map(x => x+1)];
    }
    
    return ans.slice(0,num+1);
};
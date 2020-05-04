/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (!n) {
        return 0;
    }
    
    let [i,j] = [1,0];
    
    // repeat n times
    [...Array(n)].forEach(_ => [i,j] = [i+j, i]);
    
    return i;
};
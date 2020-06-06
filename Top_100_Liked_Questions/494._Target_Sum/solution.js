/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
var findTargetSumWays = function(nums, S) {
    let N = 1000;
    if (S > N) {
        return 0;
    }
    
    let mem = new Array(nums.length+1);
    for (let i=0; i<nums.length+1; i++) {
        mem[i] = new Array(2*N+1).fill(0);
    }
    mem[nums.length][S+N] = 1;
    
    for (i=nums.length-1; i>-1; i--) {
        for (j=0; j<2*N+1; j++) {
            let add = j - nums[i] >= 0 ? mem[i+1][j - nums[i]] : 0;
            let sub = j + nums[i] <= 2*N ? mem[i+1][j + nums[i]] : 0;
            mem[i][j] = add + sub;
        }
    }
    
    return mem[0][N]
}


var findTargetSumWays2 = function(nums, S) {
    if (!nums.length) {
        return S === 0 ? 1 : 0;
    }
    
    return findTargetSumWays(nums.slice(1), S - nums[0]) + findTargetSumWays(nums.slice(1), S + nums[0]);
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    // O(n) space
    if (nums.length <= 1) {
        return nums.length;
    }
    
    let mem = new Array(nums.length).fill(0);
    mem[0] = 1;
    let maxAns = 1;
    
    for (let i=0; i<mem.length; i++) {
        let maxVal = 0;
        for (let j=0; j<i; j++) {
            if (nums[i] > nums[j]) {
                maxVal = Math.max(maxVal, mem[j]);
            }
        }
        mem[i] = maxVal + 1;
        maxAns = Math.max(maxAns, mem[i]);
    }
    
    return maxAns;
}


var lengthOfLIS3 = function(nums) {
    // dp with memoization - O(n^2) space
    if (nums.length <= 1) {
        return nums.length;
    }
    
    nums.unshift(-Infinity);
    
    let mem = new Array(nums.length+1);
    for (let i=0; i<mem.length; i++) {
        mem[i] = new Array(nums.length).fill(0);
    }
    
    for (let i=nums.length-1; i>0; i--) {
        for (let j=0; j<i; j++) {
            if (nums[i] > nums[j]) {
                mem[i][j] = Math.max(1 + mem[i+1][i], mem[i+1][j]);
            } else {
                mem[i][j] = mem[i+1][j];
            }
        }
    }

    return mem[1][0];
}


var lengthOfLIS2 = function(nums) {
    // recursion
    nums = [-Infinity, ...nums];
    let LTS = function(i, j) {
        if (i >= nums.length) {
            return 0;
        }
        
        if (nums[i] > nums[j]) {
            return Math.max(1 + LTS(i+1, i), LTS(i+1, j));
        } else {
            return LTS(i+1, j);
        }
    }
    
    return LTS(1, 0);
};
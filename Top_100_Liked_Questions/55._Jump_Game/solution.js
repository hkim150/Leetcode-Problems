/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    // greedy method
    let fgp = nums.length-1;
    for (let i=nums.length-2; i>-1; i--) {
        if (i + nums[i] >= fgp) {
            fgp = i;
        }
    }
    
    return fgp === 0;
};
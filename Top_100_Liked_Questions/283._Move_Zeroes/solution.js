/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    // left most zero index
    let lmz = -1;
    
    for (const [i,v] of nums.entries()) {
        if (v === 0) {
            if (lmz < 0) {
                lmz = i;
            }
        } else {
            if (lmz >= 0) {
                [nums[lmz++], nums[i]] = [v, 0];
            }
        }
    }
};

var moveZeroes2 = function(nums) {
    const non_zeroes = nums.filter(n => n != 0);

    for (const [i,v] of nums.entries()) {
        nums[i] = i < non_zeroes.length ? non_zeroes[i] : 0;
    }
};
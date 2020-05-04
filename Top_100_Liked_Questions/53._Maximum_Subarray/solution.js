/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = -Infinity;
    let currSum = -Infinity;
    
    nums.forEach(v => {
        currSum = (currSum > 0 ? currSum + v : v);
        maxSum = Math.max(maxSum, currSum);
    });
    
    return maxSum;
};
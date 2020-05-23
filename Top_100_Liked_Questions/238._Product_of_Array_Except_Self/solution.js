/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let ans = new Array(nums.length).fill(1);
    
    let cumul = 1;
    for (let i=0; i<nums.length-1; i++) {
        cumul *= nums[i];
        ans[i+1] *= cumul;
    }
    
    cumul = 1;
    for (let i=nums.length-1; i>0; i--) {
        cumul *= nums[i];
        ans[i-1] *= cumul;
    }
    
    return ans;
};
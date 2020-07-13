/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let ans = nums[0];
    let mn = nums[0];
    let mx = nums[0];
    
    for (let i=1; i<nums.length; i++) {
        let n = nums[i];
        [mn, mx] = [Math.min(n, mn*n, mx*n), Math.max(n, mn*n, mx*n)];
        ans = Math.max(ans, mx);
    }
    
    return ans;
};
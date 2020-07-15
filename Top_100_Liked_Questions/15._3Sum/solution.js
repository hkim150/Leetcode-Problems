/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let ans = [];
    let found = {};
    
    for (let i=0; i<nums.length; i++) {
        let seen = {};
        for (let j=i+1; j<nums.length; j++) {
            let complement = -nums[i] - nums[j];
            if (seen.hasOwnProperty(complement)) {
                mx = Math.max(nums[i], nums[j], complement);
                mn = Math.min(nums[i], nums[j], complement);
                if (!found.hasOwnProperty([mn, mx])) {
                    ans.push([nums[i], nums[j], complement]);
                    found[[mn, mx]] = 0;
                }
            }
            seen[nums[j]] = 0;
        }
    }
    
    return ans;
};
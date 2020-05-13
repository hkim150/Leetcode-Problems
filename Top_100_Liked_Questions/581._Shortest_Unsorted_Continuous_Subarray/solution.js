/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {    
    // find the minimum and maximum unordered element
    let umin = Infinity;
    let umax = -Infinity;
    
    for (let i=0; i<nums.length-1; i++) {
        if (nums[i] > nums[i+1]) {
            umin = Math.min(umin, nums[i+1]);
            umax = Math.max(umax, nums[i]);
        }
    }
    
    // find the right index of the minimum unordered element
    let l = nums.length;
    for (let i=0; i<nums.length; i++) {
        if (nums[i] > umin) {
            l = i;
            break;
        }
    }
    
    // find the right index of the maximum unordered element
    let r = -1;
    for (let i=nums.length-1; i>-1; i--) {
        if (nums[i] < umax) {
            r = i;
            break;
        }
    }
    
    return Math.max(r - l + 1, 0);
}

var findUnsortedSubarray2 = function(nums) {
    // sort and find the first and last mismatch
    const sorted_nums = [...nums].sort((a,b) => a-b);
    
    let l = nums.length;
    let r = -1;
    
    for (let [i,v] of sorted_nums.entries()) {
        if (v !== nums[i]) {
            l = i;
            break;
        }
    }
    
    for (let i=nums.length-1; i>-1; i--) {
        if (sorted_nums[i] !== nums[i]) {
            r = i;
            break;
        }
    }
    
    return Math.max(r - l + 1, 0);
};
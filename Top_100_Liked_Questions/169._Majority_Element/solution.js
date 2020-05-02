/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    // Boyer-Moore Voting Algorithm
    let count = 0;
    let candidate = null;
    
    for (n of nums) {
        if (count == 0) {
            candidate = n;
        }
        count += (n == candidate ? 1 : -1);
    }
    return candidate;
}

var majorityElementHashMap = function(nums) {
    if (nums.length === 1) {
        return nums[0];
    }
    
    const hash = {}
    const l = Math.floor(nums.length/2);
    
    for (const n of nums) {
        if (n in hash) {
            hash[n] += 1;
            if (hash[n] > l) {
                return n;
            }
        } else {
            hash[n] = 1;
        }
    }
};
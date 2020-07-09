/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    // iterative binary search
    let l = 0;
    let r = nums.length-1;
    
    while (l <= r) {
        let m = l + Math.floor((r-l)/2);
        if (nums[m] === target) {
            return m;
        }

        if (nums[l] < nums[r]) {
            if (target < nums[m]) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        } else {
            if (nums[l] <= nums[m]) {
                if (nums[l] <= target && target < nums[m]) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else if (nums[m] <= nums[r]) {
                if (nums[m] < target && target <= nums[r]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }
    }
    
    return -1;
}


var search2 = function(nums, target) {
    // recursive binary search
    let helper = function(l, r) {
        if (l > r) {
            return -1;
        }
        let m = l + Math.floor((r-l)/2);
        if (nums[m] === target) {
            return m;
        }
        
        if (nums[l] <= nums[m]) {
            if (nums[l] <= target && target < nums[m]) {
                return helper(l, m-1);
            } else {
                return helper(m+1, r);
            }
        } else if (nums[m] <= nums[r]) {
            if (nums[m] < target && target <= nums[r]) {
                return helper(m+1, r);
            } else {
                return helper(l, m-1);
            }
        } else {
            throw "array not sorted";
        }
    }
    
    return helper(0, nums.length-1);
};
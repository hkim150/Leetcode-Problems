/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {
    let sum = nums.reduce((x, y) => x + y);
    
    // if sum is odd number, it cannot be divided evenly
    if (sum % 2 === 1) {
        return false;
    }
    
    let hash = {};
    
    let hasSubSum = function(i, s) {
        if (s === 0) {
            return true;
        } else if (s < 0) {
            return false;
        }
        
        if (i >= nums.length) {
            return false;
        }
        
        let include = hash.hasOwnProperty([i+1,s-nums[i]]) ? hash[[i+1,s-nums[i]]] : hasSubSum(i+1, s-nums[i]);
        
        if (include) {
            hash[[i, s]] = true;
            return true;
        }
        
        let not_include = hash.hasOwnProperty([i+1,s]) ? hash[[i+1,s]] : hasSubSum(i+1, s);
        
        if (not_include) {
            hash[[i, s]] = true;
            return true;
        }

        hash[[i, s]] = false;
        return false;
    }
    
    return hasSubSum(0, sum/2);
};
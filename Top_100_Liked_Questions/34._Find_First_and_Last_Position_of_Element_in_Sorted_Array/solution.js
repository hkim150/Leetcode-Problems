/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let l = 0;
    let r = nums.length-1;
    while (l < r) {
        let m = (l+r) >>> 1;
        if (nums[m] < target) {
            l = m+1
        } else if (nums[m] > target) {
            r = m-1;
        } else {
            r = m;
        }
    }
    
    if (nums[l] != target) {
        return [-1,-1];
    }
    let left = l;
    
    r = nums.length-1;
    while (l < r) {
        let m = (l+r+1) >>> 1;
        if (nums[m] > target) {
            r = m-1;
        } else {
            l = m;
        }
    }
    
    return [left,r];
}


var searchRange2 = function(nums, target) {
    let findLeft = function(l,r,t) {
        if (l === r) {
            return nums[l] === t ? l : -1;
        }
        
        let m = (l+r) >>> 1;
        if (nums[m] < t) {
            return findLeft(m+1,r,t);
        } else if (nums[m] > t) {
            return findLeft(l,m-1,t);
        } else {
            return findLeft(l,m,t);
        }
    }
    
    let findRight = function(l,r,t) {
        if (l === r) {
            return nums[l] === t ? l : -1;
        }
        
        let m = (l+r+1) >>> 1;
        if (nums[m] > t) {
            return findRight(l,m-1,t);
        } else if (nums[m] < t) {
            return findRight(m+1,r,t);
        } else {
            return findRight(m,r,t);
        }
    }
    
    let l = findLeft(0, nums.length-1, target);
    return l === -1 ? [-1,-1] : [l, findRight(l, nums.length-1, target)];
};
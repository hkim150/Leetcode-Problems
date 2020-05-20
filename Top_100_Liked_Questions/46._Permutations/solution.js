/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let ans = [];
    
    let backtrack = function(first=0) {
        if (first === nums.length) {
            ans.push([...nums]);
            return;
        }
        
        for (let i=first; i<nums.length; i++) {
            [nums[first], nums[i]] = [nums[i], nums[first]];
            backtrack(first+1);
            [nums[first], nums[i]] = [nums[i], nums[first]];
        }
    }
    
    backtrack();
    
    return ans;
}

var permute2 = function(nums) {
    let ans = [];

    let helper = function(rem, per=[]) {
        if (rem.length === 0) {
            ans.push(per);
            return;
        }
        
        for (let i=0; i<rem.length; i++) {
            remCopy = [...rem];
            remCopy.splice(i,1);
            helper(remCopy, [...per, rem[i]]);
        }
    }
    
    helper(nums);
    
    return ans;
};
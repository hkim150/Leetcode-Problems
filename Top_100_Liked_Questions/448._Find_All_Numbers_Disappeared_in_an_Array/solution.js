/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    // const space solution
    for (const n of nums) {
        if (nums[Math.abs(n)-1] > 0) {
            nums[Math.abs(n)-1] *= -1;
        }
    }
    
    const ans = [];
    for (const [i,v] of nums.entries()) {
        if (v > 0) {
            ans.push(i+1);
        }
    }
    
    return ans;
}

var findDisappearedNumbersHashMap = function(nums) {
    const mem = new Array(nums.lengath).fill(0);
    
    for (const n of nums) {
        mem[n-1] = 1;
    }
    
    const ans = [];
    for (const [i,v] of mem.entries()) {
        if (v === 0) {
            ans.push(i+1);
        }
    }
    
    return ans;
};
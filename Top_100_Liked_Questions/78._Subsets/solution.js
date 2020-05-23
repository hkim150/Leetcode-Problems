/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    // cascading method
    let ans = [[]];
    for (const n of nums) {
        for (let subset of [...ans]) {
            ans.push([...subset, n]);
        }
    }
    return ans;
}

var subsets2 = function(nums) {
    // using binary
    let ans = [];
    
    for (let i=0; i<Math.pow(2,nums.length); i++) {
        let bin = i.toString(2);
        let zeroFilledBin = '0'.repeat(nums.length - bin.length) + bin;
        let subset = []
        for (let i=0; i<zeroFilledBin.length; i++) {
            if (zeroFilledBin[i] === '1') {
                subset.push(nums[i]);
            }
        }
        ans.push(subset);
    }
    
    return ans;
};
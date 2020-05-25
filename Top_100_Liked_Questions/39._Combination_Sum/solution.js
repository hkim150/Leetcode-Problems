/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    candidates.sort((a,b) => a - b);
    
    let ans = [];
    let helper = function(tar, lst=[], idx=0) {
        for (let i=idx; i<candidates.length; i++) {
            next_t = tar - candidates[i];
            if (next_t > 0) {
                helper(next_t, [...lst, candidates[i]], i);
            } else if (next_t === 0) {
                lst.push(candidates[i]);
                ans.push(lst);
                return
            }
        }
    }
    
    helper(target);
    return ans;
};
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (!intervals.length) {
        return [];
    }
    
    intervals.sort((a,b) => a[0] - b[0]);
    let ans = [intervals[0]];
    for (let i=1; i<intervals.length; i++) {
        let [s,e] = intervals[i];
        if (s <= ans[ans.length-1][1]) {
            ans[ans.length-1][1] = Math.max(e, ans[ans.length-1][1]);
        } else {
            ans.push([s, e]);
        }
    }
    
    return ans;
};
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let l = 0;
    let ans = 0;
    let latestIdx = {}
    
    for (let r=0; r<s.length; r++) {
        if (latestIdx.hasOwnProperty(s[r])) {
            l = Math.max(l, latestIdx[s[r]] + 1);
        }
        ans = Math.max(ans, r - l + 1);
        latestIdx[s[r]] = r;
    }
    
    return ans;
};
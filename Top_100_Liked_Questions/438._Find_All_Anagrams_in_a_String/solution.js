/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let len_s = s.length;
    if (len_s === 0) {
        return [];
    }
    
    let len_p = p.length;
    if (len_p === 0) {
        return [];
    }
    
    if (len_p > len_s) {
        return [];
    }
    
    let p_cnt = new Array(26).fill(0);
    let curr_cnt = new Array(26).fill(0);
    let ascii_a = 'a'.charCodeAt(0);
    for (let i=0; i<len_p; i++) {
        p_cnt[p.charCodeAt(i) - ascii_a]++;
        curr_cnt[s.charCodeAt(i) - ascii_a]++;
    }
    
    let ans = p_cnt.toString() != curr_cnt.toString() ? [] : [0];
    for (let i=0; i<len_s-len_p; i++) {
        if (s[i] != s[i+len_p]) {
            curr_cnt[s.charCodeAt(i) - ascii_a]--;
            curr_cnt[s.charCodeAt(i+len_p) - ascii_a]++;
        }
        
        if (curr_cnt.toString() === p_cnt.toString()) {
            ans.push(i+1);
        }
    }
    
    return ans;
};
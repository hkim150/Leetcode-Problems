/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    // expand around the center
    let expand = function(l, r) {
        while (l >= 0 && r <= s.length-1 && s[l] === s[r]) {
            l--;
            r++;
        }
        
        return r - l - 1;
    }
    
    let start = 0;
    let end = 0;
    for (let i=0; i<s.length; i++) {
        let l1 = expand(i, i);
        let l2 = expand(i, i+1);
        let l = Math.max(l1, l2);
        if (l > end - start) {
            start = i - Math.floor((l-1)/2);
            end = i + Math.floor(l/2);
        }
    }
        
    return s.slice(start, end+1);
}


var longestPalindrome2 = function(s) {
    // dp with memoization
    let mem = new Array(s.length);
    for (let i=0; i<mem.length; i++) {
        mem[i] = new Array(s.length).fill(false);
        mem[i][i] = true;
        if (i > 0) {
            mem[i][i-1] = true;
        }
    }
    
    let l = 0;
    let r = 0;
    let currMax = 0;
    for (let i=s.length-1; i>-1; i--) {
        for (let j=i+1; j<s.length; j++) {
            if (s[i] === s[j] && mem[i+1][j-1]) {
                mem[i][j] = true;
                if (j - i + 1 > currMax) {
                    currMax = j - i + 1;
                    l = i;
                    r = j;
                }
            }
        }
    }
    
    return s.slice(l, r + 1);
};
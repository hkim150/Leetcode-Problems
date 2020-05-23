/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let ans = 0;
    for (let center=0; center<s.length*2-1; center++) {
        let left = Math.floor(center / 2);
        let right = left + center % 2;
        
        while (left >= 0 && right < s.length && s[left] == s[right]) {
            ans++;
            left--;
            right++;
        }
    }
    
    return ans;
}

var countSubstrings2 = function(s) {
    // dp with memoization
    let mem = [];
    for (let i=0; i<s.length; i++) {
        let row = new Array(s.length).fill(false);
        mem.push(row);
    }

    for (let i=0; i<s.length-1; i++) {
        mem[i+1][i] = true;
    }
    
    let ans = 0;
    for (let left=s.length-1; left>-1; left--) {
        for (let right=left; right<s.length; right++) {
            if (left == right || (mem[left+1][right-1] && s[left] == s[right])) {
                ans++;
                mem[left][right] = true;
            }
        }
    }

    return ans;
};
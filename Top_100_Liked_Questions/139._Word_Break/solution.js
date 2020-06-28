/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    let hashSet = {};
    for (let word of wordDict) {
        hashSet[word] = null;
    }
    
    let mem = new Array(s.length+1).fill(false);
    mem[0] = true;
    
    for (let i=1; i<mem.length; i++) {
        for (let j=0; j<i; j++) {
            if (mem[j] && hashSet.hasOwnProperty(s.slice(j,i))) {
                mem[i] = true;
                break;
            }
        }
    }
    
    return mem[s.length];
}


var wordBreak2 = function(s, wordDict) {
    if (s.length <= 0) {
        return true;
    }
    
    for (let word of wordDict) {
        if (startsWith(s, word)) {
            if (wordBreak(s.slice(word.length), wordDict)) {
                return true;
            }
        }
    }
    return false;
};

let startsWith = function(s, i, word) {
    for (let j=0; j<word.length; j++) {
        if (s[i+j] != word[j]) {
            return false;
        }
    }
    return true;
}
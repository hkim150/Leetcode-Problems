/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // hash count method
    let hash = {};
    for (let s of strs) {
        let count = new Array(26).fill(0);
        for (let i=0; i<s.length; i++) {
            count[s.charCodeAt(i) - "a".charCodeAt(0)] += 1;
        }
        if (hash.hasOwnProperty(count)) {
            hash[count].push(s);
        } else {
            hash[count] = [s];
        }
    }
    
    ans = [];
    Object.values(hash).forEach(v => ans.push(v));
    
    return ans;
};

var groupAnagrams2 = function(strs) {
    // sorting method
    let hash = {};
    for (let s of strs) {
        let key = s.split("").sort()
        if (hash.hasOwnProperty(key)) {
            hash[key].push(s);
        } else {
            hash[key] = [s];
        }
    }
    
    ans = [];
    Object.values(hash).forEach(v => ans.push(v));
    
    return ans;
};
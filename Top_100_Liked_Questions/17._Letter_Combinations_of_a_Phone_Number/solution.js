/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (!digits.length) {
        return [];
    }
    
    let d2l = {}
    
    let ascii = 'a'.charCodeAt(0);
    for (let i=2; i<10; i++) {
        d2l[i] = String.fromCharCode(ascii++);
        for (let j=0; j<2; j++) {
            d2l[i] += String.fromCharCode(ascii++);
        }
        if (i == 7 || i == 9) {
            d2l[i] += String.fromCharCode(ascii++);
        }
    }
    
    let repeatArr = function(arr, num) {
        let ret = new Array(arr.length);
        for (let i=0; i<arr.length; i++) {
            ret[i] = new Array(num).fill(arr[i]);
        }
        return ret.flat();
    }
    
    let ans = [""];
    for (let digit of digits) {
        let chars = d2l[digit];
        ans = repeatArr(ans, chars.length);
        for (let i=0; i<ans.length; i++) {
            ans[i] += chars[i%chars.length];
        }
    }
    
    return ans;
};
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let ans = [];
    
    let helper = function(s='', opening=0, closing=0) {
        if (s.length == 2*n) {
            ans.push(s);
            return;
        }
        
        if (opening < n) {
            helper(s+'(', opening+1, closing);
        }
        if (opening > closing) { 
            helper(s+')', opening, closing+1);
        }
    }
    
    helper()
    return ans;
};
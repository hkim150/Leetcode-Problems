/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    const stack = [];
    const openingParen = {
        '(': 1,
        '{': 1,
        '[': 1
    }
    const matchingParen = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for (const paren of s) {
        if (openingParen[paren]) {
            // if it is an opening paren, push it to the stack
            stack.push(paren);
        } else {
            // if it is a closing paren, pop the stack and check if it is a pair
            if (!stack.length || matchingParen[paren] !== stack.pop()) {
                return false;
            }
        }
    }
    
    return stack.length === 0;
};
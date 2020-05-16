/**
 * @param {number[]} T
 * @return {number[]}
 */
var dailyTemperatures = function(T) {
    // strictly increasing stack
    stack = [];
    ans = new Array(T.length).fill(0);
    
    for (let i=T.length-1; i>-1; i--) {
        while (stack.length) {
            let top = stack[stack.length-1];
            if (T[top] > T[i]) {
                ans[i] = top - i;
                break;
            }
            stack.pop();
        }
        stack.push(i);
    }
    
    return ans;
};

var dailyTemperatures2 = function(T) {
    // brute memoization
    let mem = new Array(102).fill(Infinity);
    let ans = new Array(T.length).fill(0);
    
    for (let i=T.length-1; i>-1; i--) {
        let minIdx = Infinity;
        
        for (let j=T[i]+1; j<102; j++) {
            minIdx = Math.min(minIdx, mem[j]);
        }
        
        if (minIdx != Infinity) {
            ans[i] = minIdx - i;
        }
        
        mem[T[i]] = i;
    }
    
    return ans;
};
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // no extra storage solution
    let currMax = 0;
    let prevMax = 0;
    
    for (let i=nums.length-1; i>-1; i--) {
        [currMax, prevMax] = [Math.max(nums[i] + prevMax, currMax), currMax];
    }
    
    return currMax;
}

var rob3 = function(nums) {
    // iterative with memoization based on the recursive solution
    maxRob = new Array(nums.length+1);
    for (let i=0; i<nums.length+1; i++) {
        maxRob[i] = new Array(2).fill(0);
    }
    
    for (let i=nums.length-1; i>-1; i--) {
        maxRob[i][0] = Math.max(nums[i] + maxRob[i+1][1], maxRob[i+1][0]);
        maxRob[i][1] = maxRob[i+1][0];
    }
    
    return maxRob[0][0];
}

var rob2 = function(nums) {
    // recursive dynamic programming solution
    const maxRob = (i, canRob) => {
        if (i >= nums.length) {
            return 0;
        }
        
        const rob = canRob ? nums[i] + maxRob(i+1, false) : 0
        return Math.max(rob, maxRob(i+1, true));
    }
    
    return maxRob(0, true);
};
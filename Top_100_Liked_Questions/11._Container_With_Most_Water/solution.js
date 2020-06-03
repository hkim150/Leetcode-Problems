/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    // keep track of max area, indices of the left and right at that max    
    let l = 0;
    let r = height.length-1;
    let ma = 0;
    
    while (l < r) {
        let area = Math.min(height[l], height[r]) * (r - l);
        ma = Math.max(ma, area);
        if (height[l] < height[r]) {
            l += 1;
        } else {
            r -= 1;
        }
    }
    
    return ma;
};
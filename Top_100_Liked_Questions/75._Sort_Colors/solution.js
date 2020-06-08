/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    // one pass
    let p0 = 0;
    let pcurr = 0;
    let p2 = nums.length - 1;

    while (pcurr <= p2) {
        if (nums[pcurr] === 0) {
            [nums[pcurr], nums[p0]] = [nums[p0], nums[pcurr]];
            p0++;
            pcurr++;
        } else if (nums[pcurr] === 2) {
            [nums[pcurr], nums[p2]] = [nums[p2], nums[pcurr]];
            p2--;
        } else {
            pcurr++;
        }
    }
}

var sortColors2 = function(nums) {
    // two pass overwrite
    let counts = [0, 0, 0];
    for (let num of nums) {
        counts[num]++;
    }
    
    let k=0;
    for (let i=0; i<counts.length; i++) {
        for (let j=0; j<counts[i]; j++) {
            nums[k++] = i;
        }
    }
};
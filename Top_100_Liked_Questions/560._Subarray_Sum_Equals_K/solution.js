/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let hash = {0: 1};
    let count = 0;
    let sum = 0;
    let sum_minus_k = null;
    
    for (let num of nums) {
        sum += num;
        sum_minus_k = sum - k;
        if (hash.hasOwnProperty(sum_minus_k)) {
            count += hash[sum_minus_k];
        }
        hash[sum] = hash.hasOwnProperty(sum) ? hash[sum] + 1 : 1;
    }
    return count;
}


var subarraySum2 = function(nums, k) {
    let count = 0;
    for (let i=0; i<nums.length; i++) {
        let currSum = 0;
        for (let j=i; j<nums.length; j++) {
            currSum += nums[j];
            if (currSum === k) {
                count++;
            }
        }
    }
    return count;
};
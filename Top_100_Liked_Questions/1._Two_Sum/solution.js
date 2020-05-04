/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // one pass solution
    const hashMap = {}
    
    for (const [i,v] of nums.entries()) {
        const other = target - v;
        
        if (other in hashMap) {
            return [i, hashMap[other]];
        }
        
        hashMap[v] = i;
    }
    
    throw "no solution found";
}
    
var twoSum2 = function(nums, target) {
    // two pass solution - actually faster!
    const hashMap = {}
    nums.forEach((v,i) => hashMap[v] = i);
    
    for (const [i,v] of nums.entries()) {
        const other = target - v;
        
        if (other in hashMap && hashMap[other] != i) {
            return [i, hashMap[other]];
        }
    }
    
    throw "no solution found";
};
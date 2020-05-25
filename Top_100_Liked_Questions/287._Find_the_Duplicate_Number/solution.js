/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    // two pointer cycle dectection
    let slow = nums[0];
    let fast = nums[0];
    
    while (true) {
        slow = nums[slow];
        fast = nums[nums[fast]];
        
        if (slow === fast) {
            break;
        }
    }
    
    slow = nums[0];
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    
    return slow;
}

var findDuplicate3 = function(nums) {
    // hash set
    set = {};
    for (let n of nums) {
        if (n in set) {
            return n;
        }
        set[n] = true;
    }
    
    throw "Duplicate number not found";
}

var findDuplicate2 = function(nums) {
    // sorting
    nums.sort((a,b) => a-b);
    
    let prev = nums[0];
    for (let i=1; i<nums.length; i++) {
        if (prev === nums[i]) {
            return prev;
        }
        prev = nums[i];
    }
    
    throw "Duplicate nummber not found";
};
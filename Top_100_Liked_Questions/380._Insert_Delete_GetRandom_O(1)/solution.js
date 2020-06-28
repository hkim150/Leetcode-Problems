/**
 * Initialize your data structure here.
 */
var RandomizedSet = function() {
    this.hashmap = {};
    this.valArray = [];
};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (!this.hashmap.hasOwnProperty(val)) {
        this.hashmap[val] = this.valArray.length;
        this.valArray.push(val);
        return true;
    }
    
    return false;
};

/**
 * Removes a value from the set. Returns true if the set contained the specified element. 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (this.hashmap.hasOwnProperty(val)) {
        let idx = this.hashmap[val];
        let tailVal = this.valArray.pop();
        if (idx != this.valArray.length) {
            this.valArray[idx] = tailVal;
            this.hashmap[tailVal] = idx;
        }
        delete this.hashmap[val];
        return true;
    }
    
    return false;
};

/**
 * Get a random element from the set.
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    return this.valArray[Math.floor(Math.random() * this.valArray.length)];
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
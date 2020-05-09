/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stack = [];
};

const last = arr => arr[arr.length - 1];

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    if (this.stack.length === 0) {
        this.stack.push([x,x]);
    } else {
        const currMin = last(this.stack)[1];
        this.stack.push([x, Math.min(x, currMin)]);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return last(this.stack)[0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return last(this.stack)[1];
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
/**
 * Initialize your data structure here.
 * @param {number} size
 */
var MovingAverage = function(size) {
    this.moves = new Array(size).fill(0);
    this.curr_size = 0;
    this.max_size = size;
    this.total = 0;
    this.idx = 0;
};

/** 
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function(val) {
    this.total -= this.moves[this.idx];
    this.total += val;
    this.moves[this.idx] = val;
    this.idx = (this.idx + 1) % this.max_size;
    
    if (this.curr_size < this.max_size) {
        this.curr_size += 1;
    }
    
    return this.total / this.curr_size;
};

/** 
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
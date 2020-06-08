/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {    
    // sort intervals by first the starting time and then the end time
    intervals.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    
    // keep track of the endtimes in minHeap
    let endTimes = new MinHeap();
    
    for (let [s,e] of intervals) {
        // if the starting time is before the end time, push the new endtime into the heap
        if (endTimes.size() && s >= endTimes.peek()) {
            endTimes.pop();
        }
        endTimes.push(e);
    }
    
    return endTimes.size();
};

function MinHeap(arr=[]) {
    this.heap = [];
    this.heapify(arr);
}

MinHeap.prototype.peek = function() {
    return this.heap[0];
}

MinHeap.prototype.size = function(i) {
    return this.heap.length;
}

MinHeap.prototype.push = function(n) {
    this.heap.push(n);
    this.siftUp(this.heap.length-1);
}

MinHeap.prototype.pop = function() {
    if (this.heap.length == 1) {
        return this.heap.pop();
    }
    
    let popVal = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.siftDown(0);
    return popVal;
}

MinHeap.prototype.heapify = function(arr) {
    this.heap = arr;
    for (let i=this.heap.length-1; i>-1; i--) {
        this.siftDown(i);
    }
}

MinHeap.prototype.siftUp = function(i) {
    while (i > 0) {
        let parIdx = this.getParent(i);
        if (this.heap[i] < this.heap[parIdx]) {
            this.swap(i, parIdx);
            i = parIdx;
        } else {
            break;
        }
    }
}

MinHeap.prototype.siftDown = function(i) {
    let leng = this.heap.length - 1;
    while (i < leng) {
        let [leftIdx, rightIdx] = this.getChildren(i);
        
        if (leftIdx > leng) {
            break;
        }
        
        let minChildIdx = (rightIdx <= leng && this.heap[rightIdx] < this.heap[leftIdx]) ? rightIdx : leftIdx;
        
        if (this.heap[i] <= this.heap[minChildIdx]) {
            break;
        }
        
        this.swap(i, minChildIdx);
        i = minChildIdx;
    }
}

MinHeap.prototype.getParent = function(i) {
    return Math.floor((i - 1) / 2);
}

MinHeap.prototype.getChildren = function(i) {
    return [i*2+1, i*2+2];
}

MinHeap.prototype.swap = function(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
}

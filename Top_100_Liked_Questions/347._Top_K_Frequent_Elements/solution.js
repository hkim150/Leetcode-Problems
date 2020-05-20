/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const count = {};
    for (const n of nums) {
        count[n] = count[n] ? count[n] + 1 : 1;
    }
    
    let heap = [];
    let cnt = 0;
    
    for (const key in count) {
        if (count.hasOwnProperty(key)) {
            const pair = [key, count[key]];
            if (cnt++ < k) {
                minHeap.insert(heap, pair, x => x[1]);
            } else {
                if (pair[1] > minHeap.peakTopVal(heap, x => x[1])) {
                    minHeap.deleteTop(heap, x => x[1]);
                    minHeap.insert(heap, pair, x => x[1]);
                }
            }
        }
    }
 
    let ans = [];
    heap.forEach(v=>ans.push( Number(v[0])) );
    
    return ans;
};

class minHeap {
    constructor(arr, acc=x => x) {
        this.heap = arr;
        minHeap.heapify(this.heap, acc);
    }
    
    static insert(arr, val, acc=x => x) {
        arr.push(val);
        minHeap.siftUp(arr, arr.length-1, acc);
    }
    
    static deleteTop(arr, acc=x => x) {
        if (!arr.length) {
            return null;
        }
        const delVal = arr.pop();
        arr[0] = delVal;
        minHeap.siftDown(arr, 0, acc);
        return delVal;
    }
    
    static peakTopVal(arr, acc=x => x) {
        return acc(arr[0]);
    }
    
    static siftUp(arr, idx, acc=x => x) {        
        if (!arr.length) {
            return;
        }
        
        while (idx > 0) {
            const parentIdx = minHeap.getParentIdx(arr, idx);
            if (acc(arr[idx]) >= acc(arr[parentIdx])) {
                return;
            }
            minHeap.swapVal(arr, idx, parentIdx);
            idx = parentIdx;
        }
    }
    
    static siftDown(arr, idx, acc=x => x) {
        if (!arr.length) {
            return;
        }
        
        while (idx < arr.length) {
            const [left,right] = minHeap.getChildrenIdx(arr, idx);
            if (!left && !right) {
                return;
            }
            let swapIdx = left;
            if (right && acc(arr[left]) > acc(arr[right])) {
                swapIdx = right;
            }
            if (acc(arr[swapIdx]) >= acc(arr[idx])) {
                return;
            }
            minHeap.swapVal(arr, swapIdx, idx);
            idx = swapIdx;
        }
    }
    
    static heapify(arr, acc=x => x) {
        for (const i=arr.length; i>-1; i--) {
            minHeap.siftDown(arr, i, acc);
        }
    }
    
    static swapVal(arr, idx1, idx2) {
        [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
    }
    
    static getChildrenIdx(arr, idx) {
        const left = idx*2+1 < arr.length ? idx*2+1 : null;
        const right = idx*2+2 < arr.length ? idx*2+2 : null;
        
        return [left, right];
    }
    
    static getParentIdx(arr, idx) {
        return arr.length == 0 || idx == 0 ? null : Math.floor((idx-1)/2);
    }
}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    // quick select
    let partition = function(left, right, pivot_idx) {
        let pivot_val = nums[pivot_idx];
        [ nums[right], nums[pivot_idx] ] = [ nums[pivot_idx], nums[right] ];
        let new_pivot_idx = left;
        for (let i=left; i<right; i++) {
            if (nums[i] < pivot_val) {
                [ nums[i], nums[new_pivot_idx] ] = [ nums[new_pivot_idx], nums[i] ];
                new_pivot_idx++;
            }
        }
        [ nums[new_pivot_idx], nums[right] ] = [ nums[right], nums[new_pivot_idx] ];
        return new_pivot_idx;
    }
    
    let select = function(left, right, k_smallest) {
        if (left === right) {
            return nums[left];
        }
        
        let pivot_idx = left + Math.floor(Math.random() * (right - left + 1));
        pivot_idx = partition(left, right, pivot_idx);
        
        if (pivot_idx === k_smallest) {
            return nums[pivot_idx];
        } else if (k_smallest < pivot_idx) {
            return select(left, pivot_idx-1, k_smallest);
        } else {
            return select(pivot_idx+1, right, k_smallest);
        }
    }
    
    return select(0, nums.length-1, nums.length-k);
};

var findKthLargest3 = function(nums, k) {
    // min heap
    class minHeap {
        static heapify(arr) {
            for (let i=arr.length; i>-1; i--) {
                minHeap.siftDown(arr, i);
            }
            return arr;
        }
        
        static insert(heap, num) {
            heap.push(num);
            minHeap.siftUp(heap, heap.length-1);
        }
        
        static pop(heap) {
            let top = heap[0];
            heap[0] = heap.pop();
            minHeap.siftDown(heap, 0);
            return top;
        }
        
        static siftUp(heap, idx) {
            while (idx > 0) {
                let par_idx = minHeap.getParentIdx(heap, idx);
                if (heap[idx] < heap[par_idx]) {
                    [ heap[idx], heap[par_idx] ] = [ heap[par_idx], heap[idx] ];
                    idx = par_idx;
                } else {
                    break;
                }
            }
        }
        
        static siftDown(heap, idx) {
            while (idx < heap.length) {
                let child_idx = minHeap.getMinChildIdx(heap, idx);
                if (!child_idx) {
                    break;
                }
                
                if (heap[idx] > heap[child_idx]) {
                    [ heap[idx], heap[child_idx] ] = [ heap[child_idx], heap[idx] ];
                    idx = child_idx;
                } else {
                    break;
                }
            }
        }
        
        static getParentIdx(idx) {
            return Math.floor((idx-1)/2);
        }
        
        static getMinChildIdx(heap, idx) {
            let left = idx * 2 + 1;
            let right = idx * 2 + 2;
            
            if (left >= heap.length) {
                return null;
            }
            
            if (right >= heap.length) {
                return left;
            }
            
            return heap[left] < heap[right] ? left : right;
        }
    }
    
    let heap = minHeap.heapify(nums.slice(0,k));
    
    for (let i=k; i<nums.length; i++) {
        if (nums[i] > heap[0]) {
            minHeap.insert(heap, nums[i]);
            minHeap.pop(heap);
        }
    }
    
    return heap[0];
};

var findKthLargest2 = function(nums, k) {
    // sorting
    return nums.sort((a,b) => b - a)[k-1];
};
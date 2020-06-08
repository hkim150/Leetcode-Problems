class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        endTimes = minHeap()
        
        for s,e in intervals:
            if endTimes.size() and s >= endTimes.peek():
                endTimes.pop()
                
            endTimes.push(e)
        
        return endTimes.size()
        
        
    
class minHeap:
    def __init__(self, arr=[]):
        self.heap = []
        self.heapify(arr)
    
    
    def heapify(self, arr):
        self.heap = arr
        for i in range(len(self.heap)-1, -1, -1):
            self.siftDown(i)
    
    
    def push(self, n):
        self.heap.append(n)
        self.siftUp(len(self.heap)-1)
    
    
    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        
        popVal = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0)
        return popVal
    
    
    def peek(self):
        return self.heap[0]
    
    
    def siftUp(self, i):
        while i > 0:
            parentIdx = self.getParentIdx(i)
            if self.heap[i] >= self.heap[parentIdx]:
                break
            
            self.swap(i, parentIdx)
            i = parentIdx
    
    
    def siftDown(self, i):
        leng = len(self.heap) - 1
        while i < leng:
            leftIdx, rightIdx = self.getChildrenIdx(i)
            
            if leftIdx > leng:
                break
            
            minChildIdx = rightIdx if rightIdx <= leng and self.heap[rightIdx] < self.heap[leftIdx] else leftIdx
            
            if self.heap[i] <= self.heap[minChildIdx]:
                break
            
            self.swap(i, minChildIdx)
            i = minChildIdx
    
    
    def getParentIdx(self, i):
        return (i-1)//2
    
    
    def getChildrenIdx(self, i):
        return i*2+1, i*2+2
    
    
    def size(self):
        return len(self.heap)
    
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
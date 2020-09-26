class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # we can use heap for n^2log(k) solution
        heap = []
        n = len(matrix[0])
        for r in range(n):
            for c in range(n):
                heap.append(matrix[r][c])
             
        return heapq.nsmallest(k, heap)[-1]
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # we can flatten the matrix and sort it for n^2log(n) solution
        l = []
        for row in matrix:
            l.extend(row)
        
        return sorted(l)[k-1]
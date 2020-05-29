class Solution:
    def numTrees(self, n: int) -> int:
        # iterative dp with memoization
        mem = [0] * (n+1)
        mem[0] = mem[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                mem[i] += mem[j] * mem[i-1-j]
        
        return mem[n]
        
    
    def numTrees3(self, n: int) -> int:
        # better recursive dp
        if n < 2:
            return 1
        
        tot = 0
        for i in range(n):
            tot += self.numTrees(i) * self.numTrees(n-1-i)
        
        return tot
    
    
    def numTrees2(self, n: int) -> int:
        # recursive dp
        # we want to choose a root and divide the rest into smaller and bigger groups for legal BST
        # since the list is in order, simply slicing on its left and right would do the job
        # the number of possible subtrees per choice of root is that of left times that of right
        def numSubTree(lst):
            if len(lst) < 2:
                return 1
            
            tot = 0
            for i in range(len(lst)):
                tot += numSubTree(lst[:i]) * numSubTree(lst[i+1:])
            
            return tot
        
        return numSubTree(range(1,n+1))
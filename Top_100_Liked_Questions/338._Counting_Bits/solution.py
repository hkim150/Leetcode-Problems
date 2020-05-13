class Solution:
    def countBits(self, num: int) -> List[int]:
        # hamming weight method
        # AND operation with one less than itself results in
        # zeroing out the right most 1
        ans = [0] * (num+1)
        
        for i in range(1, num+1):
            ans[i] = ans[i & (i-1)] + 1
        
        return ans
    
    def countBits4(self, num: int) -> List[int]:
        # length precise method
        ans = [0] * (num+1)
        pow2 = 1
        
        for i in range(1,num+1):
            if i == 2*pow2:
                pow2 = i
            ans[i] = ans[i-pow2] + 1
        
        return ans
    
    def countBits3(self, num: int) -> List[int]:
        # for every 2**n, we have an extra 1 and repeat the past bits
        # numbers : 0 / 1 / 2 3 / 4 5 6 7 / 8 9 10 11 12 13 14 15 ...
        # # of 1's: 0 / 1 / 1 2 / 1 2 2 3 / 1 2  2  3  2  3  3  4 ...
        
        # (0)+1 => (1)
        # (0 1)+1 => (1 2)
        # (0 1 1 2)+1 => (1 2 2 3)
        # (0 1 1 2 1 2 2 3)+1 => (1 2 2 3 2 3 3 4)
        # ... and so on
        
        # we can use this property to create a list of number of 1's
        # and then return the list[:num+1]
        
        ans = [0]
        while len(ans) < num+1:
            ans.extend( list( map(lambda x: x+1, ans) ) )
        
        return ans[:(num+1)]
    
    
    def countBits2(self, num: int) -> List[int]:
        # naive brute force solution
        ans = []
        for n in range(num+1):
            ans.append( bin(n).count('1') )
            
        return ans

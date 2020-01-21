class Solution:
    def countPrimes2(self, n: int) -> int:
        # we can check mod until its sqrt
        if n <= 2:
            return 0
        
        def isPrime(m):
            for i in range(2,int(m**0.5)+1):
                if m%i == 0:
                    return False
            return True
        
        numPrime = 1
        for x in range(3,n,2):
            if isPrime(x):
                numPrime += 1
                
        return numPrime
    
    def countPrimes(self, n: int) -> int:
        # we can crossout the multiples of the found primes
        if n <= 2:
            return 0
        
        arr = [True] * n
        ans = 1
        
        for i in range(3,n,2):
            if arr[i]:
                ans += 1
                for j in range(i, n, i):
                    arr[j] = False
            
        return ans
            
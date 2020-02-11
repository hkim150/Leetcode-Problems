# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:        
        candidates = set(range(n))
        
        for i in range(n-1):
            for j in range(i+1, n):
                a = knows(i,j)
                b = knows(j,i)
                
                if a and not b:
                    if i in candidates:
                        candidates.remove(i)
                elif not a and b:
                    if j in candidates:
                        candidates.remove(j)
                else:
                    if i in candidates:
                        candidates.remove(i)
                    if j in candidates:
                        candidates.remove(j)
                
                if not candidates:
                    return -1
        
        if len(candidates) == 1:
            return candidates.pop()
        else:
            return -1
                    
class Solution:
    def confusingNumber(self, N: int) -> bool:
        # parse digits
        d = []
        noConfusion = set([2,3,4,5,7])
        
        while N:
            currDigit = N % 10
            # if contain any(2,3,4,5,7) -> false
            if currDigit in noConfusion:
                return False
            
            d.append(currDigit)
            N = N // 10
        
        # two pointer method
        l, r = 0, len(d)-1
        while l <= r:            
            # 0,1,8 (6<->9) -> !isPalindrome
            ld = d[l]
            if ld == 6:
                ld = 9
            elif ld == 9:
                ld = 6
            
            if ld != d[r]:
                return True
            
            l += 1
            r -= 1
        
        return False
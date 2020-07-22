class Solution:
    def addDigits(self, num: int) -> int:
        # if a number is divisible by 9, then the sum of its digits is also divisible by 9
        # any number can be represented as 9x + k, where the 9x will leave its digit sum 9 and k will remain
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        else:
            return num % 9
    
    
    def addDigits2(self, num: int) -> int:
        # brute force
        n = num
        while n > 9:
            s = 0
            while n > 0:
                s += n % 10
                n = n // 10

            n = s
        
        return s
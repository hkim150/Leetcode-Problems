class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            sum_square = 0

            while n > 0:
                digit = n % 10       
                sum_square += digit **2
                n = n // 10

            if sum_square == 1:
                return True

            if sum_square in seen:
                return False
            else:
                seen.add(sum_square)
            
            n = sum_square
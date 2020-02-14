class Solution:
    def calculate(self, s: str) -> int:
        # parse the numbers
        n = 0
        sign = '+'
        lst = []
        signs = set("+-*/")
        
        for ch in s:
            if ch.isdigit():
                n = n*10 + int(ch)
            elif ch in signs:
                if sign == '+':
                    lst.append(n)
                elif sign == '-':
                    lst.append(-n)
                elif sign == '*':
                    lst[-1] *= n
                elif sign == '/':
                    lst[-1] = int(lst[-1] / n)
                
                sign = ch
                n = 0
        
        # need to do one more time for the last number
        if sign == '+':
            lst.append(n)
        elif sign == '-':
            lst.append(-n)
        elif sign == '*':
            lst[-1] *= n
        elif sign == '/':
            lst[-1] = int(lst[-1] / n)
        
        return sum(lst)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d = {}
        for num in range(2, 10):
            asc = 97 + (num-2)*3
            if num > 7:
                asc += 1
                
            d[str(num)] = [chr(asci) for asci in range(asc, asc+3)]
        
        d['7'].append('s')
        d['9'].append('z')
        
        ans = d[ digits[0] ]
        for digit in digits[1:]:
            temp = []
            for ch in d[digit]:
                for comb in ans:
                    temp.append(comb + ch)
            ans = temp
        
        return ans
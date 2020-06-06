class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        d2c = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        ans = [""]
        
        for digit in digits:
            chars = d2c[digit]
            newAns = []
            for item in ans:
                newAns += [item] * len(chars)
            ans = newAns
            
            for i in range(len(ans)):
                ans[i] += chars[i%len(chars)]
        
        return ans
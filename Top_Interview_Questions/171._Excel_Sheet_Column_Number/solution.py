class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        # A character can be converted into a number by getting its ascii code
        # the string is then a number with base 26
        # we can convert this number to decimal
        for i,ch in enumerate(s[::-1]):
            ans += 26**i * (ord(ch) - 64)
        
        return ans
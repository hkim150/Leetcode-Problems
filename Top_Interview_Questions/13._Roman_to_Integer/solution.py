class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            v = m[s[i]]
            if i+1 != len(s) and v < m[s[i+1]]:
                v = -v

            ans += v

        return ans
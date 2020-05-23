class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand around center method - constant space
        ans = 0
        for center in range(len(s)):
            for i in range(2):
                left = center
                right = center + i
                if right == len(s):
                    break
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    ans += 1
                    left -= 1
                    right += 1
        
        return ans
                    
    
    def countSubstrings2(self, s: str) -> int:
        # dp using memoization
        # a string is palindrome if the first and last characters are same and the remaining substring is a palindrome
        mem = [[False] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)-1):
            mem[i+1][i] = True
        
        ans = 0
        
        for leftIdx in range(len(s)-1,-1,-1):
            for rightIdx in range(leftIdx, len(s)):
                if leftIdx == rightIdx or (mem[leftIdx+1][rightIdx-1] and s[leftIdx] == s[rightIdx]):
                    mem[leftIdx][rightIdx] = True
                    ans += 1
                    
        return ans

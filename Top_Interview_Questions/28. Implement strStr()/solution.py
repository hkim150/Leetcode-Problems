class Solution:
    def strStr2(self, haystack: str, needle: str) -> int:
        # sliding window with immidiate exit on a character mismatch
        lenH = len(haystack)
        lenN = len(needle)
        
        if lenN < 1:
            return 0
        
        if lenH < lenN:
            return -1
        
        i = 0
        while i < lenH:
            if lenH - i < lenN:
                return -1
            
            if haystack[i] == needle[0]:
                ans = i
                for j in range(1, lenN):
                    if haystack[i + j] != needle[j]:
                        ans = -1
                        break
                if ans != -1:
                    return ans
                
            i += 1
        
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        # we can translate the slice into a base 26 number and compare that to the needle's number
        def str2base26(s):
            num = 0
            for i, v in enumerate(s.lower()[::-1]):
                num += 26**i * (ord(v) - 97)
            
            return num
        
        lenN = len(needle)
        lenH = len(haystack)
        
        if lenN < 1:
            return 0
        
        if lenH < lenN:
            return -1
        
        needleNum = str2base26(needle)
        sliceNum = str2base26(haystack[:lenN])
        
        if sliceNum == needleNum:
            return 0
        
        for leftIdx in range(lenH - lenN):
            rightIdx = leftIdx + lenN
            leftNum = (ord(haystack[leftIdx]) - 97) * 26**(lenN-1)
            rightNum = ord(haystack[rightIdx]) - 97
            sliceNum = (sliceNum - leftNum) * 26 + rightNum
            if sliceNum == needleNum:
                return leftIdx + 1
        
        return -1
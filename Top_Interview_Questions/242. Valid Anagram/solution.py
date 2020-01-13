class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        len_s = len(s)
        len_t = len(t)
        
        # if the lengths are different, cannot be an anagram
        if len_s != len_t:
            return False
        
        # we can subtract the number of occurances and see if all of them are zero
        # dictionary to keep track of the subtraction
        d = {}
        
        # add 1 if in s, subtract 1 if in t
        for i in range(len_s):
            char_s = s[i]
            if char_s in d:
                d[char_s] += 1
            else:
                d[char_s] = 1
            
            char_t = t[i]
            if char_t in d:
                d[char_t] -= 1
            else:
                d[char_t] = -1
        
        for v in d.values():
            if v != 0:
                return False
        
        return True
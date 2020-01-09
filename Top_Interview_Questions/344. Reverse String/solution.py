class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        # Could do s = s[::-1]
        
        # swap the char at front and char at back upto the middle
        l = len(s)
        for i in range(l//2):
            temp = s[i]
            s[i] = s[l-i-1]
            s[l-i-1] = temp
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # number of unique letters must be fewer or equal ceil(word_length / 2)
        # count of every letter must be even unless word_length is odd in which case one letter must be odd
        l = len(s)
        count = {}
        num_unique = 0
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                num_unique += 1
                if num_unique > (l+1) // 2:
                    return False
                count[ch] = 1
        
        num_odd = 0
        for v in count.values():
            if v % 2 == 1:
                if l % 2 == 0:
                    return False
                num_odd += 1
                if num_odd > 1:
                    return False
        
        if l % 2 == 1 and num_odd == 0:
            return False
        
        return True
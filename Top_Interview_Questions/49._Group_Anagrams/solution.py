class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert a word to a tuple that has counts of each of 26 letters
        def countChars(word):
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            return tuple(count)
        
        # use the tuple as a hashkey of the word
        ans = {}
        for s in strs:
            t = countChars(s)
            if t in ans:
                ans[t].append(s)
            else:
                ans[t] = [s]
        
        return ans.values()
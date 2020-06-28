class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashSet = set(wordDict)
        mem = [False] * (len(s)+1)
        mem[0] = True
        
        for i in range(1,len(mem)):
            for j in range(i):
                if mem[j] and s[j:i] in hashSet:
                    mem[i] = True
                    break
        
        return mem[len(s)]
    
    
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wd = sorted(wordDict, key=lambda x: len(x), reverse=True)
        def wb(s):
            if len(s) <= 0:
                return True

            for w in wd:
                if s.startswith(w):
                    if wb(s[len(w):]):
                        return True

            return False
        return wb(s)
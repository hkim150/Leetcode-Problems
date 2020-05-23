class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using count as hash
        d = {}
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
                
            key = tuple(count)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
                
        return d.values()
    
    
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        # sorting method - O(n*m*log(m))
        d = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in d:
                d[sortedStr].append(s)
            else:
                d[sortedStr] = [s]
                
        return d.values()
    
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # brute force - O(n**2 + n*m)
        ans = []
        for s in strs:
            curr = collections.Counter(s)
            found = False
            for lst in ans:
                if lst[0] == curr:
                    lst.append(s)
                    found = True
                    break
            
            if not found:
                ans.append([curr, s])
        
        for lst in ans:
            del lst[0]
        
        return ans
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # store the source in the hash {letter: index}
        hashMap = {}
        for i,v in enumerate(source):
            if v in hashMap:
                hashMap[v].append(i)
            else:
                hashMap[v] = [i]
        
        count = 0
        prevIdx = float('inf')
        for ch in target:
            # if the letter does not exist in hash, return -1
            if ch not in hashMap:
                return -1
            
            # if the index did not increase from the previous one, count++
            currIndices = hashMap[ch]
            if prevIdx >= currIndices[-1]:
                count += 1
                prevIdx = currIndices[0]
            else:
                for idx in currIndices:
                    if idx > prevIdx:
                        prevIdx = idx
                        break

        return count
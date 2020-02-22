class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def isBigger(s1, s2):
            return int(s1+s2) > int(s2+s1)
        
        def mergeSort(lst):
            l = len(lst)
            if l < 2:
                return lst
            
            l1 = mergeSort(lst[:l//2])
            l2 = mergeSort(lst[l//2:])
            
            i = j = 0
            merged = []
            
            while i < l//2 and j < (l+1)//2:
                if isBigger(l1[i], l2[j]):
                    merged.append(l1[i])
                    i += 1
                else:
                    merged.append(l2[j])
                    j += 1
            
            while i < l//2:
                merged.append(l1[i])
                i += 1
            
            while j < (l+1)//2:
                merged.append(l2[j])
                j += 1
            
            return merged
        
        strNums = [str(n) for n in nums]
        ans = ""
        for s in mergeSort(strNums):
            ans = ans + s
        
        return str(int(ans))
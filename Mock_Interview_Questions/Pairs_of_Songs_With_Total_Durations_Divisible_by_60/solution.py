class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = {}
        ans = 0
        for t in time:
            mod = t % 60
            ans += rem.get((60 - mod) % 60, 0)
            rem[mod] = rem.get(mod, 0) + 1
        
        return ans
    
    
    def numPairsDivisibleBy60_2(self, time: List[int]) -> int:
        # brute force
        count = 0
        for i in range(len(time)-1):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        
        return count
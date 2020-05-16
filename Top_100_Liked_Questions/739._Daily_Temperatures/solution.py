class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # use stack to keep track of the strictly increasing temperatures
        # pop the stack until it finds a higher temperature
        # if the stack is empty, it mean no higher temperature on its right
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)-1,-1,-1):
            while stack:
                if T[stack[-1]] > T[i]:
                    ans[i] = stack[-1] - i
                    break
                stack.pop()
            
            stack.append(i)
        
        return ans
    
    
    def dailyTemperatures3(self, T: List[int]) -> List[int]:
        # brute memoization
        # since there are only 71 possible temperatures [30,100]
        # we can memorize the indices of each temperatures
        ans = [0] * len(T)
        nxt = [float('inf')] * 102
        for i in range(len(T)-1,-1,-1):
            nxt_idx = min(nxt[j] for j in range(T[i]+1, 102))
            if nxt_idx != float('inf'):
                ans[i] = nxt_idx - i
            nxt[T[i]] = i
        
        return ans
    
    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        # brute force method
        # nest loop and find a higher temperature on its right side
        ans = []
        for i in range(len(T)-1):
            for j in range(i+1,len(T)):
                if T[i] < T[j]:
                    ans.append(j-i)
                    break
                if j == len(T)-1:
                    ans.append(0)
        
        ans.append(0)
        
        return ans
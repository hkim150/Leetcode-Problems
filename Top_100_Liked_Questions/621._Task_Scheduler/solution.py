class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # perform the most number of remaining task among those that are not in cooldown
        # we can also check the earilest possible itvl for any task to skip looping through idle
        
        # array of 26 characters with [count, earliest_interval]
        arr = [[0,0] for _ in range(26)]
        num_remaining_task = len(tasks)
        
        for task in tasks:
            arr[ord(task) - ord('A')][0] += 1
        
        itvl = 0
        while num_remaining_task:
            maxCnt = 0
            earilest_itvl = itvl + n
            maxCntTask = None
            
            for i in range(26):
                cnt, er_itvl = arr[i]
                if er_itvl <= itvl and cnt > maxCnt:
                    maxCnt = cnt
                    maxCntTask = i
                if cnt:
                    earilest_itvl = min(earilest_itvl, er_itvl)    
                    
            if maxCntTask is not None:
                arr[maxCntTask][0] -= 1
                num_remaining_task -= 1
                arr[maxCntTask][1] = itvl + n + 1

            itvl = max(itvl+1, earilest_itvl)
        
        return itvl
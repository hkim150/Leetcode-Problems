class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = curr_gas = start_idx = 0
        
        for i in range(len(gas)):
            rem = gas[i] - cost[i]
            total_tank += rem
            curr_gas += rem
            if curr_gas < 0:
                curr_gas = 0
                start_idx = i+1
                
        return start_idx if total_tank >= 0 else -1
            
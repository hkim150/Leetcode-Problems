class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 pass solution
        hashMap = {}
        for i,v in enumerate(nums):
            # check if the 'target - n' exists in hashMap
            other = target - v
            if other in hashMap:
                # if found return the indices right away since it is guaranteed to have exactly one answer
                return [hashMap[other], i]
            
            # add the {n: i} to the hashMap if not found
            hashMap[v] = i
        
        raise Exception('no solution found')
        
        
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 2 pass solution - actually faster!
        # make a hash map of {num:index} out of the nums list
        hashMap = {v:i for i,v in enumerate(nums)}
        
        # for every number 'n' in the list, check if the 'target - n' exists in the hash map
        for i, v in enumerate(nums):
            other = target - v

            # since it is guaranteed to have exactly one answer, return the indices right away
            if other in hashMap and hashMap[other] != i:
                return [i, hashMap[other]]
        
        raise Exception('no solution found')
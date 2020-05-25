class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # two pointer cycle detection method
        # time: O(n), space: O(1)
        # detect cycle
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # find the start of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
        
    
    def findDuplicate3(self, nums: List[int]) -> int:
        # hash map
        # time: O(n), space: O(n)
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
        
        raise Exception("duplicate number not found")
    
    
    def findDuplicate2(self, nums: List[int]) -> int:
        # sorting 
        # time: O(nlog(n)), space: O(n)
        sorted_nums = sorted(nums)
        
        prev = sorted_nums[0]
        
        for i in range(1, len(sorted_nums)):
            if prev == sorted_nums[i]:
                return prev
            prev = sorted_nums[i]
        
        raise Exception("duplicate number not found")
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left and then right with iteration
        if not nums:
            return [-1,-1]
        
        left = None
        l, r = 0, len(nums)-1
        while True:
            if l+1 >= r:
                if nums[l] == target:
                    left = l
                elif nums[r] == target:
                    left = r
                else:
                    left = -1
                break
            
            m = (l+r)//2
            if nums[m] >= target:
                r = m
            else:
                l = m
        
        if left == -1:
            return [-1, -1]
        
        right = None
        l, r = left, len(nums)-1
        while True:
            if l+1 >= r:
                right = r if nums[r] == target else l
                break
            
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        
        return [left, right]
    
    
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        # find left and then right with recursion
        if not nums:
            return [-1,-1]
        
        def getLeft(l,r,t):
            if l+1 >= r:
                if nums[l] == t:
                    return l
                elif nums[r] == t:
                    return r
                else:
                    return -1
            
            m = (l+r)//2
            if nums[m] >= t:
                return getLeft(l,m,t)
            else:
                return getLeft(m,r,t)
        
        def getRight(l,r,t):
            if l+1 >= r:
                return r if nums[r] == t else l
            
            m = (l+r)//2
            if nums[m] <= t:
                return getRight(m,r,t)
            else:
                return getRight(l,m,t)
            
        l = getLeft(0, len(nums)-1, target)
        r = -1 if l == -1 else getRight(l, len(nums)-1, target)
        
        return [l,r]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get the l,m,r; left, middle, right
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # if m < r < l => a point of ratation between l and m; e.g. 6,7,0,1,2,3,4,5
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # if r < l < m => a point of rotation between m and r; e.g. 3,4,5,6,7,0,1,2        
            elif nums[r] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # l < m < r => straight forward case
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
        
        return -1
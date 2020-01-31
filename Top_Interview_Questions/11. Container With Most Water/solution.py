class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        # we can use the two pointer method
        l = 0
        r = len(height) - 1
        
        maxArea = -float('inf')
        
        while l < r:
            hl = height[l]
            hr = height[r]
            area = min(hl, hr) * (r - l)
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
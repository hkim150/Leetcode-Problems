class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select - O(n) average, O(n**2) worst
        def partition(left, right, piv_idx):
            piv_val = nums[piv_idx]
            nums[piv_idx], nums[right] = nums[right], nums[piv_idx]
            st_idx = left
            for i in range(left, right):
                if nums[i] < piv_val:
                    nums[st_idx], nums[i] = nums[i], nums[st_idx]
                    st_idx += 1
            
            nums[right], nums[st_idx] = nums[st_idx], nums[right]
            return st_idx
        
        
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)
 
        return select(0, len(nums) - 1, len(nums) - k)
        
    
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # minHeap - O(k + (n - k)log(k))
        return heapq.nlargest(k, nums)[-1]
    
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # sorting - O(n*log(n))
        return sorted(nums, reverse=True)[k-1]
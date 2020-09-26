# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome2(self, head: ListNode) -> bool:
        # we can store the values and see if it is a palindrome
        
        val = []
        # walk through the list while storing the values in an array
        while head:
            val.append(head.val)
            head = head.next
        
        # check if the array is palindrome
        left = 0
        right = len(val) - 1
        
        while left < right:
            if val[left] != val[right]:
                return False
            left += 1
            right -= 1
        
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        # we can reverse the half of the list so that we only use constant memory
        fast = slow = head
        
        while fast:
            fast = fast.next
            slow = slow.next
            
            if fast:
                fast = fast.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        second_half = prev
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True
        
        
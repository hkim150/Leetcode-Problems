# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        # constant space solution
        # count the number of nodes
        numNode = 0
        curr = head
        while curr:
            numNode += 1
            curr = curr.next
        
        # slice the list in half at the mid point
        end1 = head
        for _ in range((numNode-1)//2):
            end1 = end1.next
            
        start2 = end1.next
        end1.next = None
        
        # reverse the list of the second half
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
                
            return prev
        
        start2 = reverse(start2)
        
        # compare if the two lists are identical
        p1 = head
        p2 = start2
        
        ans = True
        while p2:
            if p1.val != p2.val:
                ans = False
                break
            p1 = p1.next
            p2 = p2.next
            
        # re-reverse the second half and connect it with the first
        end1.next = reverse(start2)
        
        return ans
    
    
    def isPalindrome3(self, head: ListNode) -> bool:
        # recursive solution
        headPtr = [head]
        def checkPalindrome(node):
            if node:
                if not checkPalindrome(node.next) or headPtr[0].val != node.val:
                    return False
                
                headPtr[0] = headPtr[0].next
            
            return True
        
        return checkPalindrome(head)
            
    
    def isPalindrome2(self, head: ListNode) -> bool:
        # naive solution, store the values in an array
        mem = []
        while head:
            mem.append(head.val)
            head = head.next
        
        l = 0
        r = len(mem)-1
        
        while l < r:
            if mem[l] != mem[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
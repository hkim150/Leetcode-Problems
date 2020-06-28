# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            retHead = None;
            if l1.val < l2.val:
                retHead = l1
                l1 = l1.next
            else:
                retHead = l2
                l2 = l2.next
                
            curr = retHead
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
                
            return retHead
        
        def mergeSort(lst):
            if not lst or not lst.next:
                return lst
            
            slow = fast = lst
            while True:
                fast = fast.next
                if not fast:
                    break
                
                fast = fast.next
                if not fast:
                    break
                
                slow = slow.next
            
            lst2 = slow.next
            slow.next = None
            
            l1 = mergeSort(lst)
            l2 = mergeSort(lst2)
            return merge(l1, l2)
        
        return mergeSort(head)
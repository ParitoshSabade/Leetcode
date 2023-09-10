# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev,curr = None, slow
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            
        return True
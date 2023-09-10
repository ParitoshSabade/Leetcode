# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stck = []
        pntr = head
        
        while pntr != None:
            stck.append(str(pntr.val))
            pntr = pntr.next
            
        straight_str = ",".join(stck)
        stck = reversed(stck)
        rev_str = ",".join(stck)
        if straight_str == rev_str:
            return True
        else:
            return False
        
        
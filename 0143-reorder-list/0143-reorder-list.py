# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stck = []
        end_pointer = head
        while end_pointer:
            stck.append(end_pointer)
            end_pointer = end_pointer.next
            
        end_pointer = stck.pop()
        
        while head.next != end_pointer and head != end_pointer:
            print(end_pointer.val)
            next_to_head = head.next
            end_pointer.next = head.next
            head.next = end_pointer
            
            end_pointer = stck.pop()
            end_pointer.next = None
            head = next_to_head
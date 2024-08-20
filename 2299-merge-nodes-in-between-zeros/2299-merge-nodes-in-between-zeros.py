# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        root  = head.next
        prev = None
        total = 0
        while node:
            if node.val == 0:
                if prev:
                    prev.val = total
                    prev.next = node.next
                prev = node.next
                total = 0
            else:
                total+=node.val
            node = node.next

        return root

        
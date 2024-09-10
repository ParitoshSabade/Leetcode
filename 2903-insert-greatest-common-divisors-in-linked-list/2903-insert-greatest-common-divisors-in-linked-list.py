# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findGCD(num1, num2):
            while num2:
                num1, num2 = num2, num1 % num2
            return num1
            
        def Insert(first,second,gcd):
            node = ListNode(gcd)
            first.next = node
            node.next = second

        first = head
        second = head.next

        while first and second:
            gcd = findGCD(first.val,second.val)
            Insert(first,second,gcd)
            first = second
            second = second.next
        return head
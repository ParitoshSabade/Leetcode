# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0
        multiplier = 1
        while l1:
            num1 += l1.val*multiplier
            multiplier = multiplier * 10
            l1 = l1.next
        multiplier = 1
        while l2:
            num2 += l2.val*multiplier
            multiplier = multiplier * 10
            l2 = l2.next
        n = num1+num2
        print(n)
        prev = head = None
        numb = n
        if n == 0:
            return ListNode(0)
        while (n):
            v = n % 10
            node = ListNode(v)
            if n==numb:
                head = node
            if prev:
                prev.next = node
            n = n//10
            prev = node
        #node.next = None
            

        return head


            

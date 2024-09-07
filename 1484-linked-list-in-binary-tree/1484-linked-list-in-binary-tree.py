# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def recurse(ListP,TreeP):
            left,right = False,False
            if ListP == None:
                return True
            if TreeP == None and ListP != None:
                return False

            if ListP.val != TreeP.val:
                return False

            left = recurse(ListP.next,TreeP.left)
            right = recurse(ListP.next,TreeP.right)
            return left or right

        q = deque([root])
        while q:
            node = q.popleft()
            ans = recurse(head,node)
            if ans:
                return ans
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
            
            
            

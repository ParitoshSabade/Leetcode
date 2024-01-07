# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        if not root:
            return answer
        def ReversePreOrder(node,level):
            if len(answer) <= level:
                answer.append(node.val)
            if node.right != None:
                ReversePreOrder(node.right,level+1)
            if node.left != None:
                ReversePreOrder(node.left,level+1)
        
        ReversePreOrder(root,0)
        return answer
            
        
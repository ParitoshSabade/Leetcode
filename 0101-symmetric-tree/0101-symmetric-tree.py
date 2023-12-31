# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def predfs(node,trace):
            if node == None:
                trace+="N"
                return trace
            trace+=str(node.val)
            trace = predfs(node.left,trace)
            trace = predfs(node.right,trace)
            return trace
            
        def postdfs(node,trace):
            if node == None:
                trace+="N"
                return trace
            trace+=str(node.val)
            trace = postdfs(node.right,trace)
            trace = postdfs(node.left,trace)
            return trace
            
            
        pre = predfs(root.left,"")
        post = postdfs(root.right,"")
        
        if pre == post:
            return True
        else:
            return False
            
            
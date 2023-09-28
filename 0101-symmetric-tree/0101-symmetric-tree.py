# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        
        
        
        key = 0
        OrderLeft,OrderRight = "",""
        order = ""
        def DFS(node):
            nonlocal order 
            if node:
                
                order += str(node.val)
                
                if key == 0:
                    DFS(node.left)
                    DFS(node.right)
                else:
                    DFS(node.right)
                    DFS(node.left)
            else:
                order+="N"
                    
            
            
        DFS(root.left)
        
        OrderLeft = order
        order = ""
        key = 1
        DFS(root.right)
        OrderRight = order
        
        if OrderLeft == OrderRight:
            return True
        else:
            return False
        
        
            
            
            
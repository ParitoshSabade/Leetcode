# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def DFS(node,v,parent,depth):
            l,r = None,None
            if node.val == v:
                return (depth,parent)
            if node.left:
                l = DFS(node.left,v,node.val,depth+1)
                
            if node.right:
                r = DFS(node.right,v,node.val,depth+1)
            if l:
                return l
            if r:
                return r
            return None
        
        ans1 = DFS(root,x,-1,0)
        if ans1:
            d1,p1 = ans1
            
        ans2 = DFS(root,y,-1,0)
        if ans2:
            d2,p2= ans2
            
        if d1 == d2 and p1 != p2:
            return True
        return False
             
                
        
        
                
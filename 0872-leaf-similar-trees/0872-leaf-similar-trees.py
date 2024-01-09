# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node,leaf):
            
            if node.left == None and node.right == None:
                leaf.append(node.val)
            if node.left:
                dfs(node.left,leaf)
            if node.right:
                dfs(node.right,leaf)
            return leaf
        
        leaf1 = dfs(root1,[])
        leaf2 = dfs(root2,[])
       
        
        if leaf1 == leaf2:
            return True
        else:
            return False
                
                